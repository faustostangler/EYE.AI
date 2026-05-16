---
name: Spot Instances and Preemptible GPUs: Cutting AI Costs by 70% | Introl Blog
keywords: (placeholder)
metadata:
  url: https://introl.com/blog/spot-instances-preemptible-gpus-ai-cost-savings
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Spot Instances and Preemptible GPUs: Cutting AI Costs by 70% | Introl Blog
Services GPU Infrastructure Install, cable, test, commission Remote Hands 4-hour SLA support Data Center Migration Zero-downtime relocations Structured Cabling Fiber & containment
Projects
About Us
Blog
Careers
Contact
EN EN English ES Español DE Deutsch FR Français ZH 中文 AR العربية JA 日本語 UK Українська KO 한국어 NL Nederlands ID Bahasa Indonesia PT Português HI हिन्दी VI Tiếng Việt TH ไทย
Back
EN English ES Español DE Deutsch FR Français ZH 中文 AR العربية JA 日本語 UK Українська KO 한국어 NL Nederlands ID Bahasa Indonesia PT Português HI हिन्दी VI Tiếng Việt TH ไทย
Blog
Spot Instances and Preemptible GPUs: Cutting AI Costs by 70%
Spotify cut ML costs from $8.2M to $2.4M using AWS Spot. Get 70-91% GPU discounts with 2-minute warnings. Complete interruption handling playbook.
Blake Crosley
Jan 24, 2026 11 min read Disclaimer 
December 2025 Update: Spot and on-demand GPU prices have converged significantly as supply constraints eased. AWS cut on-demand H100 prices 44% in June 2025 (to ~$3.90/hr), narrowing the spot premium advantage. Budget providers like Hyperbolic offer H100 at $1.49/hr and H200 at $2.15/hr, often competitive with traditional spot pricing. The GPU rental market is growing from $3.34B to $33.9B (2023-2032). While spot instances still offer savings for interruptible workloads, the calculus has shifted—on-demand now makes sense for more use cases, and new budget cloud providers have disrupted the traditional spot economics.
Spotify reduced their machine learning infrastructure costs from $8.2 million to $2.4 million annually by architecting their entire recommendation engine training pipeline around AWS Spot instances, proving that interruptible GPUs can power production AI workloads.¹ The catch: their p4d.24xlarge instances vanish with 2-minute warning whenever AWS needs the capacity back, forcing the team to checkpoint every 5 minutes and maintain triple redundancy for critical jobs. Organizations mastering spot instance orchestration achieve 70-91% cost reductions compared to on-demand pricing, but those who deploy naively lose weeks of training progress to unexpected terminations.²
AWS Spot, Google Cloud Preemptible VMs, and Azure Spot VMs offer identical hardware at massive discounts because cloud providers sell excess capacity that might disappear at any moment.³ A p5.48xlarge instance with 8 H100 GPUs costs $98.32 per hour on-demand but averages $19.66 on Spot—an 80% discount that transforms AI economics.⁴ The model works because cloud providers maintain 15-30% spare capacity for maintenance, failures, and demand spikes, monetizing otherwise idle resources while retaining the right to reclaim them instantly.
The economics of interruptible GPU capacity
Cloud providers price spot instances through continuous auctions where prices fluctuate based on supply and demand. AWS Spot prices for GPU instances vary from 70% to 91% below on-demand rates, with ml.p4d.24xlarge instances ranging from $3.90 to $29.49 per hour against the $32.77 on-demand price.⁵ Google Preemptible GPUs offer fixed 60-80% discounts but terminate after maximum 24 hours regardless of demand.⁶ Azure Spot provides similar 60-90% discounts with configurable maximum prices that prevent bill shock.
The deepest discounts appear in less popular regions and older GPU generations. US-West-2 spot prices run 20% higher than US-East-2 due to demand concentration. V100 instances achieve 91% discounts while newer H100s rarely exceed 75% discounts. Night and weekend periods offer 10-15% additional savings as enterprise workloads decrease. Smart orchestration exploits these patterns, migrating workloads across regions and time zones to minimize costs.
Interruption rates vary dramatically by instance type, region, and time. Analysis of 10 million spot instance hours reveals:⁷ - A100 instances: 2.3% hourly interruption rate - V100 instances: 0.8% hourly interruption rate - H100 instances: 4.1% hourly interruption rate - Weekend interruption rates: 40% lower than weekdays - US-East-1: 3x higher interruption rate than US-West-2
Workload patterns that thrive on spot instances
Certain AI workloads naturally fit the spot instance model:
Hyperparameter Tuning: Parallel exploration of parameter spaces tolerates individual job failures. Each experiment runs independently, so interruptions affect only single configurations. Optuna and Ray Tune automatically handle spot instance failures, restarting terminated jobs on new instances.⁸ Organizations report 75% cost savings for hyperparameter searches using spot instances exclusively.
Batch Inference: Processing millions of images or documents distributes across many instances. Work queues track completed versus pending items. Interruptions simply return unfinished work to the queue. Autoscaling groups launch replacement instances automatically. Netflix processes 100 million thumbnails daily using spot instances, saving $3.2 million annually.⁹
Data Preprocessing: ETL pipelines for training data benefit from spot capacity. Frameworks like Apache Spark checkpoint progress automatically. Interrupted tasks resume from checkpoints on new instances. The stateless nature of most preprocessing makes spot instances ideal. Uber's feature engineering pipeline runs 90% on spot instances.¹⁰
Development and Testing: Non-production environments tolerate interruptions gracefully. Developers expect occasional disruptions during experimentation. Cost savings enable larger development clusters. CI/CD pipelines retry failed jobs automatically. GitHub Actions offers 70% lower pricing for spot runners.¹¹
Distributed Training with Checkpointing: Large model training becomes feasible with proper checkpointing strategies. Save model state every 10-30 minutes to durable storage. Use gradient accumulation to maintain effective batch sizes during instance fluctuations. Implement elastic training that adjusts to available instances. OpenAI trained early GPT models using 60% spot instances.¹²
Interruption handling strategies
Successful spot instance usage requires sophisticated interruption management:
Checkpointing Frameworks: Implement automatic checkpointing at regular intervals. PyTorch Lightning provides built-in spot instance support with configurable checkpoint frequencies.¹³ Save optimizer state, learning rate schedules, and random seeds alongside model weights. Store checkpoints in object storage for durability. Resume training seamlessly on new instances.
Instance Diversification: Spread workloads across multiple instance types, availability zones, and regions. AWS Spot Fleet automatically manages diverse capacity pools.¹⁴ Configure 10-15 different instance types to maximize availability. Accept slightly suboptimal instances for better availability. Maintain 20% capacity buffer for smooth transitions.
Graceful Shutdown Handlers: AWS provides 2-minute termination notices via instance metadata service. Google gives 30-second Preemptible warnings. Implement signal handlers that trigger immediate checkpointing upon termination notice. Flush logs and metrics before shutdown. Clean up temporary resources to prevent orphaned costs.
Hybrid Architectures: Combine spot instances with on-demand capacity for critical components. Run parameter servers on on-demand while workers use spot. Maintain minimum viable capacity on stable instances. Burst to spot for additional throughput. Scale spot capacity based on price and availability signals.
Queue-Based Architectures: Decouple work scheduling from execution using message queues. Amazon SQS or Apache Kafka track pending work. Workers pull tasks when available. Completed work updates persistent storage. Failed tasks return to queue for retry.
Implementation patterns for production systems
Production-grade spot instance deployments follow proven patterns:
Multi-Region Orchestration:
Checkpoint Management:
Cost Monitoring Dashboard: Track spot savings versus on-demand baseline. Monitor interruption rates by instance type and region. Alert when spot prices exceed thresholds. Calculate effective cost per training epoch. Project monthly savings based on usage patterns.
Introl helps organizations implement spot instance strategies across our global coverage area, with expertise optimizing costs for over 100,000 GPU deployments.¹⁵ Our automation frameworks handle interruptions seamlessly while maintaining training progress and inference availability.
Real-world spot instance architectures
Pinterest - Recommendation Model Training: - Workload: Training recommendation models on 2 billion pins - Architecture: 200 V100 GPUs, 80% on spot instances - Checkpointing: Every 15 minutes to S3 - Interruption rate: 1.2% daily average - Cost savings: $4.8 million annually (72% reduction) - Key technique: Regional failover within 5 minutes
Snap - Computer Vision Pipeline: - Workload: Processing 500 million images daily - Architecture: 1,000 T4 GPUs across 6 regions - Spot percentage: 90% for batch processing - Recovery time: 30 seconds average - Cost savings: $6.2 million annually (78% reduction) - Key technique: Work-stealing queue architecture
DoorDash - Demand Forecasting: - Workload: Real-time delivery demand prediction - Architecture: Hybrid with 30% on-demand baseline - Spot usage: 70% for training, 0% for inference - Interruption handling: Automatic failover to on-demand - Cost savings: $2.1 million annually (65% reduction) - Key technique: Predictive scaling based on spot prices
When to avoid spot instances
Certain scenarios make spot instances inappropriate:
Latency-Sensitive Inference: Customer-facing APIs cannot tolerate sudden capacity loss. Model serving requires consistent availability. Interruptions cause unacceptable user experience degradation. Use reserved capacity or on-demand for production inference.
Long-Running Single Jobs: Training runs exceeding 24 hours without checkpointing face guaranteed interruption on Google Preemptible. Jobs that cannot resume from checkpoints waste entire runs. Workloads with complex state restoration should avoid spot.
Regulated Workloads: Healthcare and financial services may require guaranteed capacity for compliance. Audit requirements might prohibit infrastructure uncertainty. Data residency rules could prevent multi-region failover strategies.
Time-Critical Deadlines: Product launches or time-sensitive research cannot risk interruptions. Conference deadlines or customer commitments require guaranteed completion. Use on-demand when schedule matters more than cost.
Advanced optimization techniques
Spot Price Prediction: Machine learning models predict future spot prices based on historical patterns. Time series analysis identifies recurring availability windows. Proactive bidding strategies secure capacity before price spikes. Academic research shows 15% additional savings through price prediction.¹⁶
Adaptive Checkpointing: Adjust checkpoint frequency based on interruption probability. Increase frequency when prices approach interruption thresholds. Decrease frequency during stable periods to reduce overhead. Dynamic strategies save 20% on storage costs while maintaining recovery speed.
Cross-Cloud Arbitrage: Simultaneously bid across AWS, Google, and Azure for lowest prices. Unified orchestration layers abstract provider differences. Move workloads to cheapest available capacity. Multi-cloud strategies achieve 10-15% better pricing than single-cloud.
Spot-Native Architecture: Design systems assuming interruption from the start. Implement stateless components wherever possible. Use external state stores for all persistent data. Build resumability into every processing stage.
Cost comparison calculator
Calculate your potential savings:
Implementation checklist
Before deploying spot instances:
[ ] Implement comprehensive checkpointing every 10-30 minutes
[ ] Configure termination notice handlers for all platforms
[ ] Establish minimum on-demand capacity for critical paths
[ ] Deploy across multiple instance types and regions
[ ] Set up cost tracking and interruption monitoring
[ ] Test interruption recovery in staging environment
[ ] Document runbooks for common failure scenarios
[ ] Train team on spot instance best practices
Organizations that architect AI workloads around spot instances achieve transformational cost reductions while maintaining production reliability. The 70-90% discounts fundamentally change AI economics, enabling experiments and scales previously impossible. Success requires embracing interruption as a design constraint rather than fighting against the model. Companies mastering spot orchestration gain sustainable competitive advantages through dramatically lower infrastructure costs that compound as AI workloads grow.
Quick decision framework
Spot vs On-Demand Selection:
Key takeaways
For infrastructure architects: - AWS Spot achieves 70-91% discounts; GCP Preemptible fixed 60-80% off; Azure Spot 60-90% - Interruption rates vary: A100 2.3%, V100 0.8%, H100 4.1% hourly - AWS gives 2-minute warning; Google gives 30 seconds; Azure is configurable - Checkpoint every 10-30 minutes; store in durable object storage - Instance diversification: configure 10-15 types across multiple AZs/regions
For financial planners: - p5.48xlarge (8×H100): $98.32 on-demand → $19.66 spot (80% savings) - Spotify: $8.2M → $2.4M annually (71% reduction) - Netflix: $3.2M annual savings on batch inference with spot - Pinterest: $4.8M annual savings (72% reduction) with 15-minute checkpointing - Budget providers (Hyperbolic $1.49/hr H100) now compete with traditional spot
For MLOps engineers: - PyTorch Lightning provides built-in spot instance support - Ray Tune and Optuna automatically handle spot failures for HPO - AWS Spot Fleet manages diverse capacity pools automatically - Kubernetes cluster autoscaler supports spot node pools natively - Queue-based architectures (SQS, Kafka) decouple work from execution
References
Spotify Engineering. "Optimizing ML Training Costs with Spot Instances." Spotify R&D Blog, 2024. https://engineering.atspotify.com/2024/01/ml-spot-instances/
AWS. "Spot Instance Pricing History and Savings Analysis." Amazon Web Services, 2024. https://aws.amazon.com/ec2/spot/pricing/
Google Cloud. "Preemptible VM Instances Documentation." Google Cloud Platform, 2024. https://cloud.google.com/compute/docs/instances/preemptible
AWS. "EC2 Spot Instances Pricing." Amazon Web Services, 2024. https://aws.amazon.com/ec2/spot/pricing/
———. "Spot Instance Advisor." Amazon Web Services, 2024. https://aws.amazon.com/ec2/spot/instance-advisor/
Google Cloud. "GPU Pricing with Preemptible Discounts." Google Cloud Platform, 2024. https://cloud.google.com/compute/gpus-pricing
SpotInst. "State of Spot Instances Report 2024." Spot by NetApp, 2024. https://spot.io/resources/state-of-spot-2024/
Ray Team. "Fault Tolerance for Ray Tune on Spot Instances." Ray Documentation, 2024. https://docs.ray.io/en/latest/tune/tutorials/tune-fault-tolerance.html
Netflix Technology Blog. "Batch Processing with Spot Instances at Scale." Netflix, 2024. https://netflixtechblog.com/spot-instances-batch-processing
Uber Engineering. "Optimizing Feature Engineering Costs with Spot Instances." Uber, 2024. https://eng.uber.com/feature-engineering-spot-instances/
GitHub. "GitHub Actions Spot Runners." GitHub Documentation, 2024. https://docs.github.com/en/actions/hosting-your-own-runners/spot-runners
OpenAI. "Training Large Models on Spot Instances." OpenAI Research, 2024. https://openai.com/research/training-on-spot
PyTorch Lightning. "Spot Instance Training Guide." Lightning AI, 2024. https://lightning.ai/docs/pytorch/stable/clouds/spot_instances.html
AWS. "EC2 Spot Fleet Documentation." Amazon Web Services, 2024. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html
Introl. "Spot Instance Optimization Services." Introl Corporation, 2024. https://introl.com/coverage-area
Kang, Liang, et al. "Deep Learning for Spot Price Prediction in Cloud Computing." IEEE Transactions on Cloud Computing, 2024. https://ieeexplore.ieee.org/document/9876543
Azure. "Azure Spot Virtual Machines." Microsoft Azure, 2024. https://azure.microsoft.com/en-us/products/virtual-machines/spot/
Kubernetes. "Spot Instance Support in Cluster Autoscaler." CNCF, 2024. https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler/cloudprovider/aws
HashiCorp. "Managing Spot Instances with Terraform." HashiCorp, 2024. https://www.terraform.io/docs/providers/aws/r/spot_instance_request.html
Apache Spark. "Running Spark on Spot Instances." Apache Software Foundation, 2024. https://spark.apache.org/docs/latest/cloud-integration.html
NVIDIA. "Best Practices for GPU Workloads on Spot Instances." NVIDIA Developer, 2024. https://developer.nvidia.com/blog/gpu-spot-instances-best-practices/
Databricks. "Optimizing Costs with Spot Instances." Databricks Documentation, 2024. https://docs.databricks.com/clusters/configure/spot-instances.html
SageMaker. "Managed Spot Training in Amazon SageMaker." AWS Documentation, 2024. https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html
Flyte. "Spot Instances in Flyte Workflows." Union.ai, 2024. https://docs.flyte.org/en/latest/deployment/cluster_config/spot_instances.html
Kubeflow. "Using Preemptible VMs with Kubeflow." Google Cloud, 2024. https://www.kubeflow.org/docs/distributions/gke/preemptible/
You Might Also Like
[
Singapore's $27B AI Infrastructure Boom: Opportunities for D...
](https://introl.com/blog/singapore-27b-ai-infrastructure-boom-data-center-opportunities)
[
Malaysia and Thailand: Emerging AI Data Center Hubs in South...
](https://introl.com/blog/malaysia-thailand-emerging-ai-data-center-hubs-southeast-asia)
[
Backup and Recovery for AI: Protecting Petabyte-Scale Traini...
](https://introl.com/blog/backup-recovery-ai-protecting-petabyte-scale-training-data)
Disclaimer: This content is for informational purposes only and does not constitute professional advice. Information may not reflect current industry developments. Results described are illustrative and depend on specific circumstances. For guidance tailored to your needs, contact us.
← Back to Blog
Services
GPU Infrastructure
Remote Hands
Data Center Migration
Structured Cabling
Company
About Us
Careers
Blog
Coverage Area
Press Inquiries
Resources
Case Study: Frankfurt
Case Study: London
FAQ
Request a Quote
Connect
solutions@introl.com
Contact
Privacy Policy Terms of Service
© 2026 Introl Solutions, LLC. All rights reserved.
Capabilities described may vary by engagement and are subject to applicable statements of work.
×
Request a Quote_
Tell us about your project and we'll respond within 72 hours.
Full Name *
Company *
Email *
Phone
Service Required *
Select a service...
GPU Infrastructure Deployments
Remote Hands
Data Center Migration
Structured Cabling & Containment
Multiple Services
Other
Project Timeline
Select timeline...
Urgent (Within 1 week)
Within 1 month
1-3 months
3-6 months
Planning phase
How did you hear about us?
Select...
ChatGPT, Claude, Perplexity, or other AI Assistant
Google, Bing, or other Search Engine
LinkedIn
Instagram
Industry Event / Conference
Referral / Word of Mouth
Sales Contact
Blog Article
Other
Project Location
Project Details * [-]
I agree to the Privacy Policy and consent to being contacted about my inquiry.
Submit Request Sending...
✓
Request Received_
Thank you for your inquiry. Our team will review your request and respond within 72 hours.
QUEUED FOR PROCESSING
Close
