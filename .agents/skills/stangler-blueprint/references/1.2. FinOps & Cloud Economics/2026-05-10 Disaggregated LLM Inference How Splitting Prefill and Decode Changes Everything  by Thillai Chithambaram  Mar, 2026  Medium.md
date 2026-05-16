---
name: 2026-05-10 Disaggregated LLM Inference: How Splitting Prefill and Decode Changes Everything | by Thillai Chithambaram | Mar, 2026 | Medium
keywords: (placeholder)
metadata:
  url: None
  source: SOURCE_TYPE_TEXT
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
WebSync metadata
title: Disaggregated LLM Inference: How Splitting Prefill and Decode Changes Everything | by Thillai Chithambaram | Mar, 2026 | Medium
url: https://medium.com/@thillaic/disaggregated-llm-inference-how-splitting-prefill-and-decode-changes-everything-7404d09d5ec2
date: 2026-05-10T23:13:57.939Z
parsing method: defuddle
Sitemap
Why teams building the fastest LLM serving stacks are quietly rearchitecting from the ground up.
Here’s something most people working with LLMs don’t think about: the GPU serving your ChatGPT-style request is often wasting a significant portion of its compute cycles, especially at scale.
Not because the model is too big or the hardware is too slow, but because we’ve been forcing two fundamentally different workloads to share the same chip, at the same time, and pretending that’s fine.
It’s not fine. And the people who figured this out first are already seeing 70% throughput gains and nearly 90% faster time-to-first-token. Let me explain what they’re doing differently.
The Two Lives of an LLM Request
When you send a prompt to an LLM, two very different things happen inside the GPU. Most tutorials gloss over this, but once you understand the split, you can’t unsee it.
Prefill vs. Decode Comparison
Phase 1: Prefill (The Heavy Lift)
The moment your prompt arrives, the model needs to process the entire input, every token, all at once. This is the prefill phase, and it behaves a lot like training. The GPU runs massive matrix-matrix multiplications in parallel, chewing through your input to build something called the KV cache: a set of key-value pairs that encode the contextual understanding of your prompt.
This phase is compute-bound. The GPU cores are maxed out, and that’s exactly what you want. It determines your TTFT (Time To First Token), which is how long the user stares at a blank screen before the first word appears.
Phase 2: Decode (The Drip Feed)
Once the KV cache is built, the model switches to generating tokens one at a time, each conditioned on all the tokens before it. This is autoregressive decoding, and it has completely different hardware characteristics.
Instead of big parallel matrix operations, decode does small matrix-vector multiplications and spends most of its time reading from the ever-growing KV cache. The GPU compute cores sit mostly idle while the memory bus works overtime.
This phase is memory-bandwidth-bound. It controls TPOT (Time Per Output Token), basically how smooth or stuttery the streaming experience feels to the user.
Why This Matters
Prefill wants raw compute power. Decode wants memory bandwidth. Running both on the same GPU means neither gets what it actually needs.
Think of it like a restaurant where your best prep cook, the one who can dice 30 onions a minute, is also expected to plate each dish individually, one at a time, walking it to the table. Totally different rhythms, totally different skills, and forcing both onto the same person slows everything down.
The Monolithic Conflict
In practice, this means prefill jobs get queued behind decode batches, inflating TTFT. Meanwhile, decode jobs share GPU compute that they can’t even use efficiently. You’re paying for GPU time that’s serving neither phase well.
At low concurrency, you might not notice. But scale to hundreds or thousands of concurrent users, and this conflict becomes the bottleneck. You throw more GPUs at the problem, and your cost-per-token climbs while your latency stays frustratingly high.
The Fix: Just… Separate Them
The core idea behind disaggregated inference is embarrassingly simple: stop running prefill and decode on the same GPU. Split them into independent services, each on hardware optimized for its workload, connected by a high-speed data transfer layer.
Disaggregated Inference Architecture
The prefill instance does the heavy compute, builds the KV cache, then shoots it over to a decode instance via high-speed networking (more on that in a second). The decode instance picks up right where prefill left off and starts streaming tokens.
Why This Is a Bigger Deal Than It Sounds
On paper it seems like you’re just adding a network hop. In practice, the benefits compound:
Independent scaling. Your traffic pattern might need 3x the decode capacity but only 1x prefill during evening chatbot hours. With a monolithic server, you’d scale everything together. With disaggregation, you scale each pool independently based on actual demand.
Hardware specialization. You can put prefill on beefy compute GPUs (think H100 SXM with massive FLOPS) and decode on GPUs with high memory bandwidth or even different accelerator types entirely. You’re not forced to compromise.
Lower latency. Prefill instances never get slowed down by decode work sharing their GPU. They just crunch prompts and hand off the cache. TTFT drops dramatically.
Better utilization. When prefill and decode aren’t fighting over the same resources, GPU utilization goes up across the board. That means fewer GPUs for the same throughput, which directly translates to lower cost-per-token.
Operational flexibility. Different SLAs for prefill vs. decode? Different autoscaling policies? Different hardware generations in each pool? All possible now.
Disaggregation doesn’t replace continuous batching. It amplifies it. Prefill and decode pools can each run their own batching strategies, improving utilization independently. Instead of forcing a single batching policy across two fundamentally different workloads, each phase can optimize for its own constraints and bottlenecks.
How llm-d Makes This Production-Ready
The concept is elegant. Making it work in production on a Kubernetes cluster with real traffic, real failure modes, and real cost constraints? That’s the hard part, and that’s where llm-d comes in.
llm-d is a Kubernetes-native, open-source distributed inference framework that was recently accepted as a CNCF Sandbox project. It’s backed by an impressive coalition: Red Hat, Google Cloud, IBM Research, NVIDIA, AMD, Cisco, Hugging Face, Intel, and others. It uses vLLM as its default model engine.
What makes llm-d interesting isn’t just that it supports disaggregated inference. It’s that it treats disaggregation as a first-class architectural pattern, with production-grade plumbing around it.
Disaggregated Prefill/Decode Workers
In llm-d, prefill and decode run as separate Kubernetes pods. They scale independently via Horizontal Pod Autoscaler (HPA). You define your prefill pool and decode pool separately, each with its own resource requests, replica counts, and scaling triggers.
This is a natural fit for Kubernetes because the two workloads already have different resource profiles, different scaling characteristics, and different failure domains. Treating them as separate deployments just makes operational sense.
KV Cache Transfer: NIXL + RDMA
Here’s the critical engineering challenge in disaggregated inference: the KV cache generated by the prefill instance needs to get to the decode instance fast. We’re talking about potentially gigabytes of tensor data per request for long-context models.
llm-d solves this with NIXL (NVIDIA Inference Xfer Library), a vendor-agnostic data movement library purpose-built for this exact problem. NIXL provides an abstraction over various memory types (GPU, CPU) and storage backends through a modular plugin architecture. Under the hood, data moves over RDMA (Remote Direct Memory Access) via InfiniBand or RoCE, which means GPU-to-GPU memory transfer without involving the CPU or OS at all.
The result: KV cache transfer latency that’s negligible compared to the compute time of prefill itself. The decode instance gets the cache and starts generating tokens almost immediately.
Intelligent Request Routing
You can’t just round-robin requests across prefill and decode pools. llm-d includes an Envoy-based load balancer with inference-aware scheduling that makes routing decisions based on:
KV cache hit rates: if a similar prefix was recently processed, route to the instance that still has it cached
Queue depth: avoid overloading any single instance
In-flight request count: balance across the cluster in real time
This routing intelligence is also integrated with the Kubernetes Gateway API for standardized traffic management.
Tiered KV Cache: GPU > CPU > Disk > Remote
One of the more compelling features in llm-d v0.5 is the hierarchical KV cache architecture. Instead of throwing away cached KV states when GPU memory fills up, the system offloads them through tiers:
GPU HBM (fastest, most expensive, limited capacity)
CPU DRAM (slower, cheaper, more capacity)
Local SSD / shared filesystem (slowest access, but massive capacity)
Tiered KV Cache Hierarchy
And here’s what makes this really powerful: the shared filesystem tier isn’t just local. New nodes joining the cluster can “hydrate” their cache from this shared store, completely bypassing the slow warm-up phase that normally kills performance when you scale out.
In their benchmarks, standard GPU-only deployments experienced sharp performance collapse once HBM saturated. The storage-backed configuration maintained roughly 185K tokens/sec even as user concurrency scaled well beyond local memory limits, a 13.9x improvement at 250 concurrent users (measured on Llama-3.1–70B across 4x NVIDIA H100s with IBM Storage Scale).
This also means prefix caching for repeated prompts (chatbot system prompts, agentic workflows, RAG templates) becomes incredibly efficient because the cached KV states persist across restarts and scale-out events.
Of course, this only works if KV transfer is fast enough. Without RDMA or efficient data movement, the network can become the new bottleneck.
The Numbers
Let’s talk benchmarks, because performance claims without data are just marketing.
Performance Comparison
A fair caveat: these gains are most pronounced at high concurrency and with long input sequences. If you’re running a single request on a single GPU, disaggregation adds complexity for minimal benefit. The inflection point where it starts paying off is roughly when your monolithic server starts queuing prefill jobs behind decode batches, and for production workloads, that happens sooner than most people expect.
When Should You Actually Use This?
Disaggregated inference isn’t for everyone. Here’s a quick decision framework:
It’s a great fit when:
You’re serving LLMs at high concurrency (hundreds to thousands of concurrent requests)
You’re working with long-context inputs: RAG pipelines, document analysis, code generation with large codebases
You’re running a multi-tenant platform where different users share inference capacity
Your workloads have repetitive prefixes: chatbot system prompts, agent frameworks with fixed instructions, standardized templates
It’s overkill when:
You’re running single-user local inference on your desktop
Your model fits on one GPU with room to spare
You’re building a low-traffic side project or prototype
The dividing line is really about whether you’re GPU-constrained at scale. If you are, disaggregation is probably the single highest-impact architectural change you can make.
Where This Is All Heading
Disaggregated inference isn’t a niche optimization. It’s becoming the default architecture for production LLM serving, and the ecosystem is converging fast:
Standards are emerging. llm-d’s acceptance into CNCF signals that the Kubernetes ecosystem is taking LLM inference seriously as a workload primitive, not just a “special” deployment. The Kubernetes Inference Gateway is being designed to understand inference-specific routing concerns natively.
Optimizations are stacking. Disaggregation composes well with other inference optimizations. Speculative decoding, quantization, continuous batching, LoRA-aware scheduling: all of these benefit from or are enabled by having independent prefill/decode pools. In llm-d v0.5, LoRA-precise prefix caching in the scheduler prevents the “thundering herd” problem where every replica tries to load every adapter.
Hardware is diversifying. As AMD, Intel, and custom silicon enter the inference market, disaggregation becomes even more valuable because you can mix and match hardware across pools without being locked into a single vendor’s GPU for everything.
The stack is maturing. vLLM + llm-d + NIXL + Kubernetes is quickly becoming the open-source reference architecture for production LLM serving. Every major cloud provider and hardware vendor is either contributing to or integrating with this stack.
The Bottom Line
Here’s the TL;DR:
LLM inference isn’t one workload, it’s two. Prefill is compute-hungry; decode is memory-hungry. Cramming both onto the same GPU wastes resources. Disaggregated inference separates them, so each phase gets the hardware it actually needs.
llm-d makes this practical with Kubernetes-native orchestration, NIXL-powered GPU-to-GPU KV cache transfer, intelligent cache-aware routing, and a tiered storage hierarchy that prevents performance collapse at scale.
The numbers are real: 70% higher throughput, 88% faster time-to-first-token, and a sustained performance floor where monolithic deployments would have already collapsed.
If you’re running LLMs in production, or planning to, this is the architectural shift that will define how production LLM systems are built.
Want to Try It Yourself?
llm-d has a quickstart guide that gets you up and running on a Kubernetes cluster in minutes. If you want to see disaggregated inference in action rather than just reading about it, start here: llm-d Quickstart Guide
Full disclosure: I’ve been actively contributing to both vLLM   and llm-d, which led me to dive deep into this space. If this was useful, find me on GitHub   or LinkedIn. I write about LLM infrastructure, ML systems, and open-source MLOps.
References & Further Reading
vLLM Project: High-throughput LLM serving engine
llm-d Project: Kubernetes-native distributed LLM inference framework
llm-d v0.5 Release Blog: Performance benchmarks and architecture details
NIXL (NVIDIA Inference Xfer Library): Vendor-agnostic data movement for inference
vLLM V1 Architecture Blog: Core engine redesign
CNCF Sandbox Acceptance: llm-d’s entry into the Cloud Native ecosystem
Kubernetes Gateway API: Standard for inference-aware traffic routing
ML Engineer focused on LLM infrastructure, high-performance inference, and scaling GenAI systems from research to production.
