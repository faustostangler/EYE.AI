---
name: Prefill-Decode Disaggregation Architecture - Emergent Mind
keywords: (placeholder)
metadata:
  url: https://www.emergentmind.com/topics/prefill-decode-disaggregation-pd-disaggregation
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Prefill-Decode Disaggregation Architecture 
Papers Videos Whiteboards Open Problems Panoramas Email Digest Labs Pricing Updates Log in Sign up
Research Explorer
Papers
Videos
Whiteboards
Open Problems
Email Digest
Panorama Generator
Labs
Hybridarium
Pixel Art Bench
Science Tweets
AI Pixel Art Generator
All Projects
Pricing Log in Sign up Discord Discord Logo Streamline Icon: https://streamlinehq.com
5
Prefill-Decode Disaggregation (PD Disaggregation)
Papers
Topics
Authors
Recent
View all
Search
Search
Search by paper, topic, or author
Research
Succinct overviews based on relevant paper abstracts
Deep Research Max
In-depth responses based on relevant abstracts and paper content
2000 character limit reached
Chrome Extension
Install our Chrome Extension to automatically enhance arXiv.
Sponsor
Promote your business to millions of monthly visitors.
Prefill-Decode Disaggregation Architecture
Updated 29 December 2025
Prefill-Decode Disaggregation is an architectural paradigm that decouples LLM inference into a parallel, compute-bound prefill phase and a sequential, memory-bound decode phase.
The approach enhances throughput, latency, and scalability by enabling independent resource scaling and specialized hardware for each phase, as shown by significant empirically measured gains.
Key techniques include KV cache management, dynamic scheduling, and phase-aware hardware specialization, resulting in performance improvements such as over 7.4× rps increase and 12× tighter 99th-percentile latency SLOs.
Prefill-Decode Disaggregation (PD Disaggregation) is an architectural paradigm for efficient inference serving of large, decoder-only Transformer-based LLMs that physically and logically separates the compute-bound “prefill” phase of prompt ingestion from the memory-bound, sequential “decode” phase of token generation. By decoupling these two heterogeneous stages onto independently scaled resource pools or services, PD Disaggregation eliminates detrimental resource contention, enables hardware specialization per phase, and offers substantial, quantifiable improvements in throughput, latency, scalability, and operational cost relative to traditional monolithic GPU inference deployments ( Kumar et al., 16 Oct 2025).
1. Prefill and Decode: Computational Dichotomy
In GPT-style decoder-only models, inference for a single request is inherently two-phased:
Prefill Phase: The model ingests a prompt of length N p N_p N p , executing a fully parallelized forward pass through all Transformer layers to produce both the first output token and the key/value (KV) cache necessary for attention during autoregressive generation. Each layer computes:
Q = X W Q , K = X W K , V = X W V Q = XW_Q,~K = XW_K,~V = XW_V Q= X W Q , K= X W K , V= X W V ,
followed by multi-head attention and feed-forward modules.
This phase is FLOP-intensive, compute-bound, and highly parallel, dominated by large matrix-matrix operations and batch-friendly GEMMs.
The operational metric is Time to First Token: T first = T prefill ( N p ) T_{\text{first}} = T_{\text{prefill}}(N_p) T first = T prefill ( N p ).
Decode Phase: The model autoregressively generates output tokens, one at a time, using the previously constructed KV cache and model weights:
Each decode step retrieves cached K/V, computes matrix-vector attention, applies a feed-forward block, and SoftMax sampling.
This phase is memory-bandwidth-bound, with low intra-token parallelism; it is characterized by high-frequency, small-batch, bandwidth-limited memory accesses.
The operational metric is Inter-token Latency: L inter L_{\text{inter}} L inter .
Resource contention arises in monolithic systems because the GPU must trade off peak FLOP utilization (best for prefill) against peak memory bandwidth (decode), leading to underutilization and high, unpredictable tail latencies—often as low as 0.2% of peak GPU utilization in overload scenarios ( Kumar et al., 16 Oct 2025).
2. System Architecture and Service Decomposition
PD Disaggregation decomposes LLM inference serving into a modular, microservices-style architecture comprising three principal tiers:
A front-end load balancer or smart router mediates request routing: new prompts are directed to prefill workers, subsequent decode calls tagged by context ID are dispatched to decode workers. The centralized KV store isolates compute and memory traffic, supports prefix sharing to reduce memory usage, and provides asynchronous, zero-copy transfers ( Kumar et al., 16 Oct 2025).
This enables independent provisioning and autoscaling of resources for each phase—prefill and decode clusters can be sized, run, and optimized based on their characteristic bottlenecks and workload patterns.
3. Performance Modeling and Resource Utilization
PD Disaggregation allows each phase's resource allocation to be optimized according to its dominant constraint:
Prefill Latency: T prefill ( N p ) ∝ N p ⋅ d model 2 TFLOPS GPU T_{\text{prefill}}(N_p)\propto\frac{N_p\cdot d_{\text{model}}^2}{\text{TFLOPS}_\text{GPU}} T prefill ( N p ) ∝ TFLOPS GPU  N p  ⋅ d model 2
Decode Token Latency: L inter ≈ Size ( KV_block ) B HBM + d model 2 TFLOPS decode L_{\text{inter}} \approx \frac{\text{Size}(\text{KV_block})}{B_{\text{HBM}}} + \frac{d_{\text{model}}^2}{\text{TFLOPS}_{\text{decode}}} L inter  ≈ B HBM  Size( KV_block) + TFLOPS decode  d model 2
The total sequence latency for N o N_o N o  tokens:
T total ( N p , N o ) = T prefill ( N p ) + N o ⋅ L inter T_\text{total}(N_p, N_o) = T_\text{prefill}(N_p) + N_o \cdot L_\text{inter} T total ( N p , N o )= T prefill ( N p )+ N o  ⋅ L inter
Throughput can trade off against latency via batching and pipelining, while network overheads for KV transfer amortize over longer outputs—per-token transfer drops to < 0.2 <0.2 < 0.2 ms for N o > 50 N_o > 50 N o > 50 with 400 GB/s NVLink interconnects and 100MB/layer KV blocks ( Kumar et al., 16 Oct 2025). Empirical “knee” points show diminishing returns on latency as decode clusters are scaled and network/cache lookup bottlenecks dominate.
Resource-level optimizations unlocked by PD Disaggregation include:
Maximal tensor-core tiling and FlashAttention for prefill, keeping memory stalls Q = X W Q , K = X W K , V = X W V Q = XW_Q,~K = XW_K,~V = XW_V Q= X W Q , K= X W K , V= X W V  05%.
KV paging and radix prefix sharing reduce working set size Q = X W Q , K = X W K , V = X W V Q = XW_Q,~K = XW_K,~V = XW_V Q= X W Q , K= X W K , V= X W V  1 for decode, effectively doubling memory bandwidth per token.
Speculative decoding can overlap draft-model and main-model computations.
Empirical results include 7.4 Q = X W Q , K = X W K , V = X W V Q = XW_Q,~K = XW_K,~V = XW_V Q= X W Q , K= X W K , V= X W V  2 rps increase, Q = X W Q , K = X W K , V = X W V Q = XW_Q,~K = XW_K,~V = XW_V Q= X W Q , K= X W K , V= X W V  390% TTFT SLO compliance, and %%%%14 Q = X W Q , K = X W K , V = X W V Q = XW_Q,~K = XW_K,~V = XW_V Q= X W Q , K= X W K , V= X W V  215%%%% tighter 99 Q = X W Q , K = X W K , V = X W V Q = XW_Q,~K = XW_K,~V = XW_V Q= X W Q , K= X W K , V= X W V  6-percentile SLOs versus monoliths (DistServe, AIBrix, Dynamo) ( Kumar et al., 16 Oct 2025).
4. Scheduling, Autoscaling, and Deployment
PD Disaggregation decouples service scheduling, enabling distinct autoscalers for each phase:
Prefill: Scale based on FLOP saturation, e.g., increase Q = X W Q , K = X W K , V = X W V Q = XW_Q,~K = XW_K,~V = XW_V Q= X W Q , K= X W K , V= X W V  7 to decrease Q = X W Q , K = X W K , V = X W V Q = XW_Q,~K = XW_K,~V = XW_V Q= X W Q , K= X W K , V= X W V  8.
Decode: Scale on HBM bandwidth, KV cache hit-rates; batch continuous decode iterations to maximize utilization.
Key deployment practices include:
Provision high-bandwidth network backbone (RDMA/NVLink) to keep Q = X W Q , K = X W K , V = X W V Q = XW_Q,~K = XW_K,~V = XW_V Q= X W Q , K= X W K , V= X W V  9 end-to-end.
Accept eventual consistency in the KV-store, but enforce eviction policies (LRU/cost-aware) to bound staleness.
Isolate failures—decode-only outage should not block prefill ingress.
Monitor phase-wise TTFT, inter-token latency, cache miss/hit, and network latency histograms for anomaly detection ( Kumar et al., 16 Oct 2025).
Batching and speculative decoding are essential for high throughput; speculative pipelines overlap early draft-model decode with accurate main-model computation to further reduce inter-token latency.
5. Phase-Aware Hardware Specialization
Disaggregation enables hardware specialization per phase. Prefill chips maximize systolic arrays, favor cheaper GDDR memory, and de-emphasize bandwidth; decode chips shrink compute resources but retain full high-bandwidth HBM (see SPAD architecture) ( Zhang et al., 9 Oct 2025). Prefill-optimized hardware can attain 8% higher throughput at half the cost; decode-optimized hardware saves 28% TDP with marginal performance loss.
Edge deployment variants exploiting PD Disaggregation use dynamic partial reconfiguration (DPR) to hot-swap attention engines, maximizing LUT/URAM utilization in FPGAs for each phase ( Zhang et al., 12 Dec 2025).
6. Advanced Scheduling, Dynamic Balancing, and Adaptation
Modern serving systems extend base PD Disaggregation with dynamic scheduling and phase-aware migration strategies:
ARES introduces predictive decode-phase balancing via lightweight length predictors operating on LLM hidden states to anticipate future token load, reducing TPOT tail by 74.77% and more than doubling goodput under long-output workloads ( Wang et al., 15 Oct 2025).
TaiChi unifies PD Disaggregation and aggregation, with scheduling mechanisms (“latency shifting,” flowing-decode, and length-aware prefill) and configurable resource ratios, enabling hybrid configurations that achieve up to 77% higher goodput under balanced SLOs ( Wang et al., 4 Aug 2025).
DOPD dynamically derives and maintains the optimal P/D instance ratio online, using ARIMA-based forecasting of arrival rate, input and output lengths, thereby achieving up to 1.5 T first = T prefill ( N p ) T_{\text{first}} = T_{\text{prefill}}(N_p) T first = T prefill ( N p ) 0 higher goodput and T first = T prefill ( N p ) T_{\text{first}} = T_{\text{prefill}}(N_p) T first = T prefill ( N p ) 199% SLO attainment even under workload bursts ( Liao et al., 26 Nov 2025).
Phase-aware pruning strategies further optimize the model for each disaggregated phase, reducing computation, memory, and communication demands with stage-specific block pruning and token-aware KV cache transmission ( Zhang et al., 29 Aug 2025).
PD Disaggregation is also extensible: for large multimodal models, EPD Disaggregation further splits encoding (for images/audio) from prefill and decode, yielding even greater memory and batch-size gains ( Singh et al., 2024); for online/offline collocation workloads, latency-strict vs. relaxed pool partitioning (OOCO) enables strict SLO compliance while maximizing offline throughput ( Wu et al., 26 Nov 2025).
7. Significance, Limitations, and Forward Directions
PD Disaggregation has become the dominant industrial deployment paradigm for large-context and throughput-sensitive LLM inference, enabling modular, autoscalable, cloud-native serving at enterprise scale ( Kumar et al., 16 Oct 2025).
Key benefits, directly verified in empirical evaluations:
Predictable and low tail latency for both TTFT and per-token decode.
Order-of-magnitude throughput gains and near-linear scalability.
Hardware and cloud cost reductions exceeding 40% by phase-specialized resource provisioning ( Zhang et al., 9 Oct 2025).
Immediate applicability to advanced serving stacks (DistServe, Dynamo, Mooncake, vLLM, etc.) and extension to retrieval-augmented scenarios ( Liu et al., 1 Dec 2025).
Current limitations include increased system complexity; deployment of elastic scaling and adaptive scheduling policies is essential to avoid producer-consumer imbalance and resource underutilization under skewed or bursty workloads ( Mitra et al., 5 Jun 2025, Liao et al., 26 Nov 2025). Scaling further requires robust network infrastructure for low-latency KV transfer and ongoing research targets optimal pruning, phase-aware quantization, and dynamic adaptation in multi-tenancy or edge environments.
PD Disaggregation, together with its variants and extensions, is fundamental for the efficient, scalable, and cost-effective serving of ever-larger LLMs in modern cloud and edge inference deployments.
Markdown Report Issue Upgrade to Chat
Definition Search Book Streamline Icon: https://streamlinehq.com
References (11)
1.
From Attention to Disaggregation: Tracing the Evolution of LLM Inference (2025)
2.
SPAD: Specialized Prefill and Decode Hardware for Disaggregated LLM Inference (2025)
3.
PD-Swap: Prefill-Decode Logic Swapping for End-to-End LLM Inference on Edge FPGAs via Dynamic Partial Reconfiguration (2025)
4.
Adaptive Rescheduling in Prefill-Decode Disaggregated LLM Inference (2025)
5.
Prefill-Decode Aggregation or Disaggregation? Unifying Both for Goodput-Optimized LLM Serving (2025)
6.
A Dynamic PD-Disaggregation Architecture for Maximizing Goodput in LLM Inference Serving (2025)
7.
Enhancing LLM Efficiency: Targeted Pruning for Prefill-Decode Disaggregation in Inference (2025)
8.
Efficiently Serving Large Multimodal Models Using EPD Disaggregation (2024)
9.
OOCO: Latency-disaggregated Architecture for Online-Offline Co-locate LLM Serving (2025)
10.
Trinity: Disaggregating Vector Search from Prefill-Decode Disaggregation in LLM Serving (2025)
11.
Beyond the Buzz: A Pragmatic Take on Inference Disaggregation (2025)
Topic to Video (Beta)
No one has generated a video about this topic yet.
Sign Up to Generate All Videos Subscribe on YouTube
Whiteboard
No one has generated a whiteboard explanation for this topic yet.
Sign Up to Generate
Follow Topic
Get notified by email when new papers are published related to Prefill-Decode Disaggregation (PD Disaggregation).
Sign Up to Follow Topic by Email
Continue Learning
How does PD Disaggregation mitigate resource contention in large-scale LLM inference deployments?
What role does KV cache management play in optimizing prefill and decode phases?
How do dynamic scheduling and autoscaling mechanisms contribute to the overall performance of PD Disaggregation systems?
In what ways can phase-aware hardware specialization further improve efficiency and reduce operational costs?
Find recent papers about dynamic scheduling in LLM inference.
Related Topics
Prefill-Decode Disaggregated Architectures
Prefix Prefill Workloads Overview
Disaggregated Inference in LLMs
PDP: Partially Disaggregated Prefill
Disaggregated LLM Serving Infrastructure
PD Disaggregation in LLM Inference
Disaggregated LLM Inference
DistServe: Optimized Disaggregated LLM Serving
Goodput-Optimized LLM Serving
Prefill-Oriented Inference Architecture
Content
Overview References Topic to Video Whiteboard Follow Topic Continue Learning Related Topics
Stay informed about trending AI papers: Subscribe
About Updates Chrome Extension Sponsorship RSS Terms Privacy Contact Twitter Discord
