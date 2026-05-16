---
name: 2026-05-10 GPU Memory Hierarchy — How AI Training Actually Works | by AIQuest | Medium
keywords: (placeholder)
metadata:
  url: None
  source: SOURCE_TYPE_TEXT
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
WebSync metadata
title: GPU Memory Hierarchy — How AI Training Actually Works | by AIQuest | Medium
url: https://medium.com/@indiai/gpu-memory-hierarchy-how-ai-training-actually-works-24f00cc13050
date: 2026-05-10T23:13:12.590Z
parsing method: defuddle
Sitemap
Your H100 has 80GB of HBM3 with over 3 TB/s bandwidth. So why does training feel slow?
The answer lies in a 6-level memory hierarchy where the fastest tier (registers) is 1 million times faster than the slowest (NVMe storage). Understanding this hierarchy explains why your GPU spends most of its time waiting, not computing.
The Six-Tier Memory Hierarchy
Src: https://www.youtube.com/watch?v=ZQKMZIP3Fzg
Modern GPU training systems have six memory tiers, each with vastly different characteristics:
Tier 1: Registers (~KB per SM, <1 cycle)
H100: 64K 32-bit registers per SM, 255 registers max per thread [1]
Fastest memory, closest to compute cores
Zero-latency access from thread perspective
Tier 2: L1 Cache + Shared Memory (~256 KB per SM, 1–2 cycles)
H100: 256 KB unified L1/texture/shared memory per SM [2]
A100: 192 KB per SM with 33-cycle hit latency [3]
Programmer-managed (shared memory) or automatic (L1)
Tier 3: L2 Cache (40–50 MB, 200–743 cycles)
H100: 50 MB with bifurcated latency (258–264 cycles near-hit, up to 743 cycles far-hit) [4]
A100: 40 MB with 200-cycle access latency [5]
6.5× slower than L1 across Hopper, Ampere, Ada Lovelace architectures [4]
Tier 4: HBM (High Bandwidth Memory) (80–141 GB, ~120 ns)
H100: 3–3.9 TB/s bandwidth, ~120 ns random-access latency [6]
A100: 1.6–2 TB/s bandwidth, ~100 ns latency [7]
Main GPU memory where models and activations live
Tier 5: CPU RAM (512 GB — 2 TB, ~70–180 ns)
DDR4: ~25.6 GB/s per channel, ~10 ns latency [8]
DDR5: ~38.4–67.2 GB/s per channel, ~12 ns latency [9]
NUMA penalty: 1.5–2× latency for remote socket access [10]
Tier 6: NVMe Storage (TB scale, milliseconds)
Required throughput: 1–5 GB/s (LLM), 5–20 GB/s (vision), 20+ GB/s (video) [11]
Millions of cycles slower than registers
The performance gap is staggering. An L2 cache miss costs 500+ cycles. An HBM access costs ~600 cycles on H100. A trip to CPU RAM? Thousands of cycles. This hierarchy determines everything.
Training: The Six-Stage Data Journey
Training follows a predictable pipeline. Consider Llama 70B training on 8× H100 GPUs:
Stage 1: Storage → CPU RAM
Training data (tokenized text, ~1 TB) lives on NVMe. PyTorch DataLoader spawns worker processes to read batches into CPU RAM. Default DataLoader achieves only 57.4% GPU utilization due to CPU preprocessing bottlenecks [12].
Stage 2: CPU Preprocessing
Each worker decodes, preprocesses, and batches data on CPU. For vision tasks (ImageNet), this includes JPEG decoding, resizing, augmentation — CPU-intensive operations. Multi-process loading provides 1.5–5× speedup by parallelizing across cores [13].
Stage 3: CPU → GPU Transfer
Batch transfers via PCIe. PCIe Gen4 x16: ~32 GB/s. PCIe Gen5 x16: ~64 GB/s [14]. But here’s the catch: in an 8-GPU server, all GPUs share uplinks. Each GPU gets ~8 GB/s effective bandwidth, not 64 GB/s.
PCIe has 1.54% encoding overhead (128b/130b scheme) [15]. Real-world utilization: graphics cards reach only ~19% of theoretical bandwidth due to protocol overhead, interrupt processing, and OS latency [16].
Stage 4: HBM → L2 → L1 → Registers (Forward Pass)
Model weights live in HBM (70B parameters × 2 bytes = 140 GB for FP16). During forward pass:
Weights stream from HBM to L2 cache (258–743 cycles on H100)
L2 feeds L1 (6.5× faster)
L1 feeds registers for actual computation
Each transformer layer performs matrix multiplications (Q, K, V projections), attention, and feed-forward networks. Activations accumulate in HBM between layers.
Stage 5: Backward Pass (Gradients → HBM)
Backpropagation computes gradients for every parameter. These gradients write back to HBM. For Llama 70B, that’s another 140 GB of gradient storage.
Multi-GPU training adds gradient synchronization (all-reduce) via NVLink or InfiniBand, as we covered in our network bandwidth analysis.
Stage 6: Optimizer Update
AdamW optimizer maintains two state tensors per parameter (momentum and variance). For 70B parameters, that’s 420 GB total in FP32. Optimizer reads gradients from HBM, computes updates, writes new weights back to HBM.
Training is memory bandwidth-bound. Model FLOPs Utilization (MFU) of 30–50% is typical — GPUs stall on memory access, not compute [17].
Inference: Simpler Flow, Different Bottleneck
Inference skips stages 5–6 (no gradients, no optimizer). But it introduces a new memory hog: the KV cache.
KV Cache Mechanics
Transformers use attention: each token attends to all previous tokens. In the decode phase, each new token needs key (K) and value (V) tensors from every previous token. Recomputing these every step is wasteful.
Solution: cache K and V tensors in HBM.
Memory calculation for Llama 2 7B [18]:
d_head = 128, n_heads = 32, n_layers = 32
Per token KV cache: 2 × (128 × 32 × 32) × 2 bytes (FP16) = ~512 KB
For 4096-token context: ~2 GB just for KV cache
For long contexts, KV cache dominates memory. A 32K context on Llama 70B consumes 60+ GB just for cached tensors — more than the model weights [19].
Prefill vs Decode
Inference has two phases:
Prefill: Process all input tokens in parallel (compute-bound)
Decode: Generate tokens autoregressively (memory bandwidth-bound)
Decode is the bottleneck. Each token generation requires loading the entire model from HBM (~140 GB for Llama 70B) to produce one token. Memory bandwidth, not compute, determines throughput.
In large-batch inference, DRAM bandwidth saturation in attention is the primary bottleneck. Over 50% of attention cycles stall waiting for memory [20].
Flash Attention: The Register Optimization
Flash Attention (Dao et al., 2022) [21] is a textbook example of memory hierarchy optimization.
Standard Attention:
Compute Q·K^T → n×n matrix (quadratic memory: O(n²))
Write Q·K^T to HBM
Read from HBM → Softmax → Write to HBM
Read from HBM → Multiply by V → Output
For 4K sequence, Q·K^T is 4096×4096 = 64 MB. Standard attention writes and reads this matrix multiple times.
HBM accesses: Ω(Nd + N²) where N = sequence length, d = head dimension [21]
Flash Attention Strategy:
Break Q, K, V into tiles that fit in SRAM (shared memory + registers). For H100, SRAM = 228 KB per SM.
Load Q tile, K tile, V tile into SRAM
Compute attention block-by-block entirely in SRAM
Use online softmax (incremental computation without materializing full matrix)
Write only final output to HBM
HBM accesses: O(N²d²M⁻¹) where M = SRAM size [21]
For typical values (d=128, M=228KB), Flash Attention makes 9× fewer HBM accesses.
Benchmark results:
GPT-2 (1K sequence): 3× speedup [21]
BERT-large (512 sequence): 15% end-to-end speedup over MLPerf record [21]
Sequence length 2K: 10× memory savings
Sequence length 4K: 20× memory savings [21]
Flash Attention 2 (Dao, 2023) [22] further optimizes parallelism:
2× faster than Flash Attention 1
Up to 9× faster than PyTorch standard attention
Achieves 50–73% of theoretical maximum FLOPs/s on A100 [22]
The key insight: avoid writing intermediate results (Q·K^T) to slow HBM. Keep everything in fast SRAM/registers until final output. This reduces memory traffic by 10–20×.
Modern Data Loading: Bypassing CPU
Src: https://developer.nvidia.com/blog/gpudirect-storage/
The storage → CPU → GPU pipeline has a CPU bottleneck. Modern libraries bypass it.
GPU Direct Storage (GDS)
Traditional: Storage → CPU RAM → GPU HBM (two copies, PCIe crossed twice) GDS: Storage → GPU HBM (direct DMA, single copy)
NVMe communicates directly with GPU memory via DMA, skipping CPU entirely.
Performance: 2–8× bandwidth improvement, 3.8× latency reduction [23]. On TPC-H benchmarks: 6.7–32.8× speedup vs non-GDS [24].
NVIDIA DALI
Moves preprocessing (decode, resize, augment) from CPU to GPU.
Why? GPU has 3,000+ GB/s internal bandwidth (HBM + registers + compute). CPU has 25–67 GB/s (DDR4/DDR5). Preprocessing on GPU is 10–100× faster for data-parallel operations.
Benchmarks [25]:
ResNet50: 37% training time reduction
ResNet152: 43% training time reduction
U-Net3D: 2× end-to-end speedup
FFCV
Optimizes file format for sequential GPU ingestion. Pre-processes offline (resize, normalize) and stores in optimized layout.
Result: 30× speedup on ImageNet training by eliminating CPU preprocessing bottleneck [26]. On AWS A100, FFCV achieves 52–68% total training cost savings vs vanilla PyTorch [27].
These libraries share a philosophy: minimize data movement between slow memory tiers. Move computation to where data already lives (GPU), or optimize data layout to maximize sequential access patterns (FFCV).
Takeaways: Why Memory Determines Everything
Memory hierarchy has 1,000,000× latency spread. Registers (0 cycles) to NVMe (millions of cycles). Optimization means keeping data in fast tiers.
Training is memory bandwidth-bound. 30–50% maximum flops utilization is typical because GPUs wait for data from HBM. Flash Attention achieves 50–73% by reducing HBM traffic.
Inference decode is memory bandwidth-bound. Generating one token requires loading entire model from HBM. Batch size helps amortize this, but attention still saturates bandwidth at large batches.
Data loading matters. Default PyTorch achieves 57.4% GPU utilization. DALI/FFCV/GDS reach 80%+ by bypassing CPU preprocessing.
Quantization is capacity optimization, not speed optimization. INT4 doesn’t make operations faster — it lets you fit more operations in fixed memory.
The GPU is fast. Memory is slow. All optimization comes down to minimizing data movement between slow memory tiers. Understand the hierarchy, and you understand why training and inference behave the way they do.
Common Myths Debunked
Myth 1: “More VRAM = Faster Training”
False. VRAM capacity determines what fits in memory, not speed. An 80GB H100 isn’t faster than a 40GB A100 because of capacity — it’s faster due to 50% more bandwidth (3 TB/s vs 2 TB/s). Training speed depends on bandwidth, not capacity. You need enough capacity to fit your model, but beyond that, bandwidth dominates.
Myth 2: “Flash Attention is Always Faster”
Not quite. Flash Attention excels at long sequences (1K+ tokens) where memory access dominates. For short sequences (<512 tokens), standard attention may be comparable or faster because the Q·K^T matrix fits in L2 cache. Flash Attention’s tiling overhead isn’t worth it when everything already fits in fast memory. Use it for long-context workloads.
Myth 3: “PCIe Gen5 Eliminates the CPU Bottleneck”
False. PCIe Gen5 doubles bandwidth (64 GB/s vs 32 GB/s), but preprocessing still happens on CPU. Decoding JPEGs, resizing images, tokenizing text — all CPU-bound. Gen5 helps with data transfer but doesn’t touch preprocessing. That’s why DALI (GPU preprocessing) provides 2× speedup even with fast PCIe.
Myth 4: “L1 Cache is Automatic and Always Optimal”
False for shared memory. L1 cache is automatic, but shared memory (same physical hardware) is programmer-managed. CUDA kernels can explicitly load data into shared memory for reuse. Flash Attention manually tiles data into shared memory — that’s why it’s faster. Relying on automatic L1 caching alone misses optimization opportunities.
Myth 6: “GPU Direct Storage Fixes All Data Loading Issues”
False. GDS bypasses CPU for storage → GPU transfers, but only helps for large sequential reads from NVMe. It doesn’t help with preprocessing, small random I/O, or datasets that need CPU augmentation (random crops, flips). GDS + DALI together solve the full pipeline — GDS for transfer, DALI for preprocessing.
Sources
NVIDIA Hopper Tuning Guide — https://docs.nvidia.com/cuda/hopper-tuning-guide/
NVIDIA Hopper Architecture In-Depth — https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
NVIDIA Ampere GPU Architecture Tuning Guide — https://docs.nvidia.com/cuda/ampere-tuning-guide/
Benchmarking and Dissecting the Nvidia Hopper GPU Architecture — https://arxiv.org/pdf/2402.13499
NVIDIA Ampere Architecture Whitepaper — https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/nvidia-ampere-architecture-whitepaper.pdf
NVIDIA H100 Tensor Core GPU — https://www.nvidia.com/en-us/data-center/h100/
The Critical Role of High Bandwidth Memory (HBM) in Modern GPUs — https://bytebridge.medium.com/the-critical-role-of-high-bandwidth-memory-hbm-in-modern-gpus-63b0164f29bc
DDR4 vs DDR5 RAM: Performance, Comparison, and Key Differences — https://servermall.com/blog/ddr4-vs-ddr5-ram-performance-comparison-and-key-differences/
DDR4 vs. DDR5: All Differences — https://www.adata.com/en/quikTips/differences-between-ddr4-and-ddr5/
NUMA (Non-Uniform Memory Access): An Overview — https://queue.acm.org/detail.cfm?id=2513149
AI Training Data Pipeline Optimization — https://www.runpod.io/articles/guides/ai-training-data-pipeline-optimization-maximizing-gpu-utilization-with-efficient-data-loading
MinatoLoader: Accelerating Machine Learning Training — https://arxiv.org/html/2509.10712
PyTorch data loader bottleneck — https://discuss.pytorch.org/t/pytorch-data-loader-bottleneck/116829
PCIe 5.0 vs 4.0: A Comprehensive Technical Deep Dive — https://www.wevolver.com/article/pcie-50-vs-40-a-comprehensive-technical-deep-dive-for-engineers
PCI Express 5 vs. 4: What’s New? — https://www.rambus.com/blogs/pci-express-5-vs-4/
Comparison of different PCI-E slots for AI calculations — https://medium.com/@jaroslav.streit/comparison-of-different-pci-e-slots-for-ai-calculations-fa397404a3a2
Mastering LLM Techniques: Inference Optimization — https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/
Understanding and Coding the KV Cache in LLMs from Scratch — https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms
KVQuant: Towards 10 Million Context Length LLM Inference — https://arxiv.org/html/2401.18079v3
Mind the Memory Gap: Unveiling GPU Bottlenecks in Large-Batch LLM Inference — https://arxiv.org/html/2503.08311v2
FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness (NeurIPS 2022) — https://arxiv.org/abs/2205.14135
FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning — https://arxiv.org/abs/2307.08691
GPUDirect Storage: A Direct Path Between Storage and GPU Memory — https://developer.nvidia.com/blog/gpudirect-storage/
Quantifying Performance Gains of GPUDirect Storage — https://ieeexplore.ieee.org/document/9925516/
Fast AI Data Preprocessing with NVIDIA DALI — https://developer.nvidia.com/blog/fast-ai-data-preprocessing-with-nvidia-dali/
FFCV: Accelerating Training by Removing Data Bottlenecks — https://arxiv.org/pdf/2306.12517
Optimize Deep Learning Performance — https://www.genesiscloud.com/blog/how-to-optimize-i-o-performance-of-your-deep-learning-model
Some basic knowledge of LLM: Parameters and Memory Estimation — https://medium.com/@baicenxiao/some-basic-knowledge-of-llm-parameters-and-memory-estimation-b25c713c3bd8
Reduce AI Model Operational Costs With Quantization Techniques — https://newsletter.theaiedge.io/p/reduce-ai-model-operational-costs
A Practical Guide to LLM Quantization — https://compute.hivenet.com/post/llm-quantization-guide
