---
name: Plan your Cloud TPU resources | Google Cloud Documentation
keywords: (placeholder)
metadata:
  url: https://docs.cloud.google.com/tpu/docs/plan-tpus
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Plan your Cloud TPU resources | Google Cloud Documentation
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
Español – América Latina
Français
Indonesia
Italiano
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
Choose a consumption option
Request TPU quota
Choose TPU version
What's next
Home
Documentation
AI and ML
Cloud TPU
Guides
Was this helpful?
Send feedback
On this page
Choose a consumption option
Request TPU quota
Choose TPU version
What's next
Plan your Cloud TPU resources Stay organized with collections Save and categorize content based on your preferences. Dismiss Got it
This page describes how to plan your Tensor Processing Unit (TPU) usage.
Choose a consumption option
Consumption options refers to the ways to get and use compute resources. You can request Cloud TPU VM capacity based on your needs for speed, duration, cost, and preemption tolerance. Options include:
On-demand: Standard pay-as-you-go instances.
Spot VMs: Lower-cost, preemptible instances. Uses preemptible quota.
Flex-start VMs: Reserve capacity as needed, for up to 7 days, without long-term reservations or complex quota management.
Reservations: Reserve capacity for a specific duration (up to 90 days or 1 year+), guaranteeing availability. Uses on-demand quota.
For TPU v6e and later generations, you can also use GKE with TPU Cluster Director. This feature is available through an All Capacity mode reservation. It provides full access to your reserved capacity and complete visibility into the TPU's hardware layout, usage, and health. For more information, see All Capacity mode overview.
The following table compares TPU consumption options based on how they work, their ideal use cases, supported TPU versions and zones, and required quota types.
Consumption option
How it works
Best used for
Supported TPU versions and zones
Quota type for Cloud TPU API
Future reservations for one year or longer
You request TPU resources for one year or longer in advance. These resources are reserved for your exclusive use during that time.
Reservations provide the highest level of assurance for capacity and provide a lower price than on-demand resources.
Future TPU reservations include a committed use discount (CUD) CUDs provide discounted prices when you purchase a committed use contract. For more information, see Future reservations for one year or longer
Future reservations for one year or longer are ideal for long-running training jobs and inference workloads.
All TPU versions: See TPU regions and zones
On-demand quota
Future reservations for up to 90 days (calendar mode)
You request TPU resources for a specific start time and duration, between one and 90 days. These resources are reserved for your exclusive use during that time. For more information, see Future reservations for up to 90 days (in calendar mode)
Reservations provide the highest level of assurance for capacity and provide a lower price than on-demand resources.
Future reservations in calendar mode are a good fit for training and experimentation workloads that require precise start times and have a defined duration.
TPU7x (Ironwood) for training and serving: us-central1-c
v6e (Trillium) for training and serving: asia-northeast1-b, us-east5-a
v5p for training and serving: us-east5-a
v5e for training: us-west4-a
v5e for serving: us-central1-a
No quota required
On-demand
You request TPU resources for immediate use, for as long as you need them.
On-demand provides significant flexibility. On-demand resources aren't preempted, but there's no guarantee that there are enough available TPU resources to satisfy your request. On-demand is the default option when you create TPU resources. For more information about creating and using on-demand TPUs, see Create TPU VMs.
On-demand is a good fit for urgent jobs and workloads that require a flexible end time.
All TPU versions: See TPU regions and zones
On-demand quota
Flex-start ( Preview)
You request TPU resources for a specific amount of time, up to seven days, without reserving capacity in advance.
TPU Flex-start VMs are delivered from a dedicated pool of capacity, so the availability of these resources is higher than on-demand. For more information, see Request TPU Flex-start VMs.
For more information about using TPU Flex-start VMs with Google Kubernetes Engine (GKE), see About GPU and TPU provisioning with flex-start provisioning mode.
Flex-start is ideal for experimentation, small-scale testing, dynamic provisioning of TPUs for inference workloads, model fine-tuning, and workload runs that take less than seven days.
TPU7x (Ironwood): us-central1-c (using GKE only)
v6e (Trillium): asia-northeast1-b, us-east5-a
v5p: us-east5-a
v5e: us-west4-a
Preemptible quota
Spot
You request TPU resources that can be preempted.
Spot VMs are available at a significantly lower price than on-demand resources. Spot VMs are often easier to obtain than on-demand resources but can be preempted (shut down) at any time. There is no limit on runtime duration. For more information about TPU Spot VMs, see Manage TPU Spot VMs.
Spot is a good fit for scheduling lower priority workloads like model pre-training, model fine-tuning, and simulation jobs that are tolerant to availability disruptions.
All TPU versions: See TPU regions and zones
Preemptible quota
Request TPU quota
To use TPU VMs, regardless of the consumption option, you need either on-demand or preemptible quota for Cloud TPU cores or chips. Make sure you have enough quota for your chosen option, TPU version, size, and zone. Quotas are specific to each TPU version and differ for on-demand versus preemptible use. Some TPU versions have default quotas; for others, you must request quota. For more information, see Cloud TPU quotas.
If you use TPUs with Google Kubernetes Engine (GKE), you need Compute Engine API quota instead of the standard TPU API quota. For more information about TPU quotas in GKE, see Ensure that you have TPU quota.
Choose TPU version
Select the TPU version, for example, v5e, v5p, v6e, or TPU7x (Ironwood) based on your model's training or inference needs. For more information, see TPU versions.
What's next
Learn how to create TPU VMs
Learn how to manage TPUs
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
Español – América Latina
Français
Indonesia
Italiano
Português – Brasil
עברית
中文 – 简体
中文 – 繁體
日本語
한국어
