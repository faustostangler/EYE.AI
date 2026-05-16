---
name: TPU7x (Ironwood) - Google Cloud Documentation
keywords: (placeholder)
metadata:
  url: https://docs.cloud.google.com/tpu/docs/tpu7x
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
TPU7x (Ironwood) | Google Cloud Documentation
Skip to main content
docs.cloud.google.com uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. Learn more
OK, got it
Technology areas
close
AI and ML
Application development
Application hosting
Compute
Data analytics and pipelines
Databases
Distributed, hybrid, and multicloud
Industry solutions
Migration
Networking
Observability and monitoring
Security
Storage
Cross-product tools
close
Access and resources management
Costs and usage management
Infrastructure as code
SDK, languages, frameworks, and tools
More /
Console
[x] light Light theme [-] dark Dark theme [-] device Device default
Language
English
Deutsch
Español
Español – América Latina
Français
Indonesia
Italiano
Português
Português – Brasil
עברית
中文 – 简体
中文 – 繁體
日本語
한국어
Sign in 
Cloud TPU
Start free
Overview Guides Reference Samples Support Resources More
Technology areas
More
Overview
Guides
Reference
Samples
Support
Resources
Cross-product tools
More
Console
Discover
Introduction to Cloud TPU
TPU architecture
TPU software versions
TPU versions
TPU7x (Ironwood)
TPU v6e
TPU v5p
TPU v5e
TPU v4
TPU v3
TPU v2
Regions and zones
JAX AI stack
TPU Cluster Director overview
Get started
Set up a Google Cloud project
Plan your Cloud TPU resources
Create TPU VMs
Reserve TPUs
About TPU reservations
Request a reservation for up to 90 days (in calendar mode)
Request a future reservation for one year or longer
Share a reservation
Request an All Capacity mode reservation
Consume a reservation
Run JAX on Cloud TPU VM
Run PyTorch on Cloud TPU VM
Train on Cloud TPU slices
Run JAX on Cloud TPU slices
Run PyTorch on Cloud TPU slices
Configure TPUs
Encrypt a TPU VM boot disk with a CMEK
Connect a TPU to a shared VPC network
Connect to a TPU VM without a public IP address
Configure networking and access
Use a cross-project service account
Storage options
Storage options for Cloud TPU
Attach durable block storage to a TPU VM
Connect to Cloud Storage buckets
Mount a Filestore instance on a TPU VM
Training and inference
Train a model using TPU7x
Train a model using v6e
Train a model using v5e
TPU inference
Multislice training
Scale a model on TPUs
Scale ML workloads using Ray
Run TPU applications in a Docker container
Work with image datasets
Convert an image classification dataset for use with Cloud TPU
Download, pre-process and upload the ImageNet dataset
Download, pre-process and upload the COCO dataset
Manage TPUs
Manage TPU resources
Manage queued resources
Request TPU Flex-start VMs
Manage TPU Spot VMs
Manage All Capacity mode TPUs
View the topology and health of All Capacity mode TPUs
Manage All Capacity mode maintenance events
Report and repair faulty hosts in All Capacity mode
Prepare for maintenance events
Schedule TPU collections for inference workloads
Autocheckpoint
View maintenance notifications
Manually start host maintenance
Preemptible TPUs
Optimize performance
Cloud TPU performance guide
Improve your model's performance with bfloat16
TPU7x (Ironwood) performance optimizations
Monitor and troubleshoot TPUs
Troubleshoot TPU VMs
Monitor TPU VMs
Monitor TPU health
Monitor TPU goodput
Dashboards for monitoring and logging
TPU monitoring Library
Monitor with tpu-info CLI
Troubleshoot TensorFlow models
Troubleshoot PyTorch models
Troubleshoot JAX models
Cloud TPU error glossary
Cloud TPU audit logs
ML Diagnostics platform
Overview
Set up GKE
Get started with the SDK
Get started with the CLI
Use ML Diagnostics with MaxText
View machine learning runs
Monitor workloads
Profile TPUs
Profile TPU VMs
Profile Multislice environments
Profile PyTorch XLA workloads
Tutorials
Train ResNet with PyTorch
MaxDiffusion inference on v6e
Notebooks
Notebooks
AI and ML
Application development
Application hosting
Compute
Data analytics and pipelines
Databases
Distributed, hybrid, and multicloud
Industry solutions
Migration
Networking
Observability and monitoring
Security
Storage
Access and resources management
Costs and usage management
Infrastructure as code
SDK, languages, frameworks, and tools
On this page
System architecture
Memory hierarchy
Dual-chiplet architecture
Programming model and framework exposure
Supported configurations
TPU7x VM
Hyperdisk
What's next
Home
Documentation
AI and ML
Cloud TPU
Guides
Was this helpful?
Send feedback
On this page
System architecture
Memory hierarchy
Dual-chiplet architecture
Programming model and framework exposure
Supported configurations
TPU7x VM
Hyperdisk
What's next
TPU7x (Ironwood) Stay organized with collections Save and categorize content based on your preferences. Dismiss Got it
This page describes the architecture and available configurations for TPU7x, the latest TPU available on Google Cloud. TPU7x is the first release within the Ironwood family, Google Cloud's seventh generation TPU. The Ironwood generation is designed for large-scale AI training and inference.
With a 9,216-chip footprint per Pod, TPU7x shares many similarities with TPU v5p. TPU7x provides high performance for large scale dense and MoE models, pre-training, sampling and decode-heavy inference.
To use TPU7x, you must use Google Kubernetes Engine (GKE). For more information, see About TPUs in GKE.
You can also use TPU7x and GKE with TPU Cluster Director. TPU Cluster Director is available through an All Capacity mode reservation, which gives you full access to all of your reserved capacity (no hold-backs) and full visibility into the TPU hardware topology, utilization status, and health status. For more information, see All Capacity mode overview.
To get access to TPU7x, contact your account team.
Note: You can use the JAX framework on TPU7x. TensorFlow is not supported.
System architecture
Each TPU7x chip contains two TensorCores and four SparseCores. The following table shows the key specifications and their values for TPU7x compared to prior generations.
The following diagram illustrates the architecture of Ironwood: 
Memory hierarchy
TPU7x features a multi-tiered memory system, and managing data movement between these tiers is crucial for performance:
High-bandwidth memory (HBM): Each chip is equipped with 192 GB of HBM, with bandwidth of approximately 7.37 TB/s. The large HBM capacity enables large batch sizes, which can improve throughput. However, despite its size, HBM can still be a bottleneck, particularly for memory-bound vector operations or inefficient data access patterns.
Vector memory (VMEM): VMEM is a smaller, on-chip SRAM (static random-access memory) with significantly higher bandwidth to the Matrix Multiply Unit (MXU) than HBM. This memory acts as a high-speed scratchpad for custom kernels. The size of this buffer is a tunable parameter. Optimizing the buffer size is critical for tuning custom Pallas kernels, as their block sizes are often constrained by the available VMEM.
Host memory and PCIe: Each set of four TPU chips is connected to a CPU host using a PCIe network. While this connection has much lower bandwidth than HBM, the host's main memory can be used for offloading activations or optimizer states to free up HBM, a technique particularly useful for managing memory pressure in large models.
For more on efficiently managing data movement between the tiers of the TPU7x memory hierarchy, see Ironwood performance optimizations.
Dual-chiplet architecture
The Ironwood programming model lets you access two TPU chiplets instead of a single logical core (also known as MegaCore) architecture used in previous generations (TPU v4 and v5p). This change improves the cost-effectiveness and efficiency of manufacturing the chip. While this represents an architectural shift, the new design ensures that you can reuse existing software models with minimal changes.
Ironwood TPUs are composed of two distinct chiplets, each with its own dedicated memory space. This is a departure from the unified memory space of the MegaCore architecture.
Chiplet composition: Each chiplet is a self-contained unit with one TensorCore, two SparseCores, and 96 GB of high-bandwidth memory (HBM).
High-speed interconnect: The two chiplets are connected by a die-to-die (D2D) interface that is six times faster than a 1D inter-chip interconnect (ICI) link. Inter-chiplet communication is managed using collective operations.
Programming model and framework exposure
The programming model for Ironwood is similar to that of TPU generations earlier than v4, such as TPU v3. The new architecture is exposed in the following ways:
Two devices per chip: Frameworks like JAX expose each Ironwood chip as two separate "devices," one for each chiplet.
Chiplet specification: You can specify which chiplet to use for a computation. JAX adds a fourth dimension to the topology specification to distinguish between chiplets. This design lets you reuse existing software models with minimal changes.
For more information about achieving optimal performance with the dual-chiplet architecture, see Performance recommendations for Ironwood's dual-chiplet architecture
Supported configurations
Note: Use the TPU topology visualizer to view 3D renderings of different TPU configurations.
TPU7x chips have a direct connection to the nearest neighboring chips in 3 dimensions, resulting in a 3D mesh of networking connections. Slices larger than 64 chips are made up of one or more 4x4x4 "cubes" of chips.
TPU7x chips have a 3D torus interconnect topology. This topology allows slices to scale up to 9216 chips. It has bi-directional bandwidth of 200 GBps per axis for communication between chips within a pod.
The following table shows common 3D slice shapes that are supported for TPU7x:
Note: All TPU7x topologies use the tpu7x-standard-4t machine type.
TPU7x VM
Each TPU7x virtual machine (VM) contains 4 chips. Each VM has access to two NUMA nodes. For more information about NUMA nodes, see Non-uniform memory access on Wikipedia.
All TPU7x slices use full-host, 4-chip VMs. The technical specifications for a TPU7x VM are:
Number of vCPUs per VM: 224
RAM per VM: 960 GB
Number of NUMA nodes per VM: 2
Hyperdisk
By default, the VM boot disk for TPU7x is Hyperdisk Balanced. You can attach more disks to your TPU VM for additional storage. The following disk types are supported on TPU7x:
Hyperdisk Balanced
Hyperdisk ML
For more information about Hyperdisk, see Hyperdisk overview. For more information about storage options for Cloud TPU, see Storage options for Cloud TPU data.
What's next
Use TPU7x with GKE
Use TPU7x with TPU Cluster Director
Use the Google Cloud ML Diagnostics platform to optimize and diagnose your workloads
Run a training workload using a recipe optimized for TPU7x
Run a TPU7x microbenchmark
Ironwood performance optimizations
Train large-scale machine learning models on GKE with Multi-Tier Checkpointing
Was this helpful?
Send feedback
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-05-08 UTC.
Products and pricing
See all products
Google Cloud pricing
Google Cloud Marketplace
Contact sales
Support
Community forums
Support
Release Notes
System status
Resources
GitHub
Getting Started with Google Cloud
Code samples
Cloud Architecture Center
Training and Certification
Engage
Blog
Events
X (Twitter)
Google Cloud on YouTube
Google Cloud Tech on YouTube
About Google
Privacy
Site terms
Google Cloud terms
Manage cookies
Our third decade of climate action: join us
Sign up for the Google Cloud newsletter Subscribe
Language
English
Deutsch
Español
Español – América Latina
Français
Indonesia
Italiano
Português
Português – Brasil
עברית
中文 – 简体
中文 – 繁體
日本語
한국어
