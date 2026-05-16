---
name: The Complete Guide to Cloud Networking Costs: VPCs, NAT ...
keywords: (placeholder)
metadata:
  url: https://zop.dev/resources/blogs/the-complete-guide-to-cloud-networking-costs-vpcs-nat-gateways-and-data-transfer/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Skip to main contentThe System to Manage Smarter .The Platform to Build Faster .BlogDocsIntegrationEbooksContact UsPlaygroundLog in Log inSign up Sign upcloud-managementThe Complete Guide to Cloud Networking Costs: VPCs, NAT Gateways and Data Transfer
Most cloud networking costs hide in "EC2 - Other" for months. Here's exactly what you're paying for across NAT Gateways, cross-AZ traffic, and VPC endpoints, and the fixes that take under an hour.
By Riya Mittal   ·   Published: April 3, 2026   ·   8 min read  Most teams discover their networking bill late. Compute shows up in cost dashboards. Storage has clear metrics. Networking hides inside line items like “EC2 - Other” until someone investigates. By then, the bill had been high for months.
This is a practical breakdown of how AWS networking pricing works, where the money actually goes, and which optimizations deliver the highest return for the least effort.
What You’re Actually Paying For
The first thing to understand is the split between free and paid components.
Free:
Creating a VPC, subnets, route tables, and internet gateways
Security groups and network ACLs
Data transfer within the same AZ using private IPs (including across VPC peers)
Gateway VPC Endpoints for S3 and DynamoDB (no hourly charge, no data fee)
Inbound data transfer from the internet to AWS
Paid:
Component Cost NAT Gateway $0.045/hr + $0.045/GB Public IPv4 address $0.005/hr (~$3.65/month per IP) Interface VPC Endpoint (PrivateLink) $0.01/hr per AZ + $0.01/GB Transit Gateway attachment $0.05/hr (~$36.50/month) Transit Gateway data processing $0.02/GB Cross-AZ data transfer $0.01/GB per direction Internet egress, first 10 TB/month $0.09/GB VPC peering, cross-region $0.02-$0.17/GB  
The pattern here is consistent: traffic that stays within a single AZ on private IPs is free. Every boundary you cross starts a meter. The cross-AZ charge of $0.01/GB per direction sounds small. It compounds.
The NAT Gateway Tax
A NAT Gateway in us-east-1 costs $0.045/hour. That is $32.85/month before a single byte of traffic. Add data processing at $0.045/GB processed, and for any traffic that also exits to the internet, you add egress at $0.09/GB on top.
One byte of data leaving through NAT to the internet costs: $0.045 (NAT processing) + $0.09 (egress) = $0.135/GB total.
Since February 2024, AWS has also charged $0.005/hour for every public IPv4 address. The Elastic IP attached to a NAT Gateway is $3.65/month more.
The costs stack in ways that are easy to miss until the architecture review happens after the bill.
Figure: NAT Gateway applies multiple charges per outbound byte—data processing, internet egress, and public IPv4 costs
This is how a team at one company ended up spending over $10,000 per day on NAT Gateway charges. They had large data volumes routing through a public-internet NAT at $0.045/GB processing plus egress. Switching to AWS Direct Connect connections dropped that bill by $310,000 per month.
A more common case: a CI/CD pipeline misconfiguration. A team’s pipeline was firing 340 jobs per day instead of the intended 10. Each job pulled container images through a NAT Gateway. The result was 47 TB/month in NAT traffic and a $12,000 monthly bill, 87% of which came from that single pipeline bug. Fixing the configuration dropped costs to $667/month.
The NAT Gateway is doing its job. The problem is using it for traffic that has no business leaving the AWS network in the first place.
The Hidden Cross-AZ Problem
Inter-AZ traffic costs $0.01/GB per direction, $0.02/GB round-trip. That is cheap for a handful of requests. For microservices sending thousands of requests per second, it is not.
Datadog’s 2024 State of Cloud Costs report measured cross-AZ traffic at approximately 50% of all data transfer costs, with 98% of organizations affected. The reason is architectural: most services are deployed across multiple AZs for redundancy, and default routing has no AZ awareness.
Kubernetes is the clearest example. Default service routing sends requests to any healthy pod in any AZ. A request landing on a node in us-east-1a might be forwarded to a pod in us-east-1c. That single hop costs $0.02/GB round-trip. Multiply by the number of microservice calls per second, and the bill becomes visible.
Figure: Default Kubernetes routing can incur ~$0.02/GB cross-AZ traffic, while topology-aware routing keeps traffic local within the same AZ and avoids these costs
One team found 991,980 GB/month of cross-AZ traffic, generating $9,919/month in charges. That was 94.1% of their entire data transfer bill. The fix was a single route table update: 56 EC2 instances were routing through a NAT Gateway in the wrong AZ. Correcting the route tables so each subnet used the NAT in its own AZ saved $36,000/year.
For Kubernetes, Topology Aware Routing (available in Kubernetes 1.27+) enables AZ-locality for service traffic. Adding  service.kubernetes.io/topology-mode: auto  to a service annotation is a one-line change that routes requests to pods in the same AZ first. For teams running Cilium or Istio, locality-aware load balancing configuration achieves the same result with more control.
VPC Endpoints: The Free Optimization You’re Skipping
The most cost-effective networking change in most AWS architectures costs nothing to implement and has no ongoing hourly charge. Gateway VPC Endpoints for S3 and DynamoDB are free. They route traffic from your VPC directly to S3 or DynamoDB over AWS’s internal network, bypassing the NAT Gateway entirely.
If your workload moves 10 TB/month to S3 and you have no gateway endpoint, you are paying $450/month ($0.045 x 10,000 GB) in NAT processing fees for traffic that never needed to touch a public IP address. A financial services team discovered they were spending $80,000/year this way, routing S3, CloudWatch, and DynamoDB API calls through NAT when free endpoints were available.
For other AWS services, interface endpoints (PrivateLink) are not free but are significantly cheaper than NAT:
Service Without Endpoint (NAT + processing) With Interface Endpoint ECR (container pulls) $0.135/GB (NAT + egress) $0.01/GB SSM Parameter Store $0.045/GB (NAT processing) $0.01/GB CloudWatch Logs $0.045/GB (NAT processing) $0.01/GB Secrets Manager $0.045/GB (NAT processing) $0.01/GB S3 (gateway endpoint) $0.045/GB (NAT processing) Free DynamoDB (gateway endpoint) $0.045/GB (NAT processing) Free  
A team running EKS was pulling container images from ECR through a NAT Gateway. At 178,000 GB/month in image pulls, that was $8,010/month in NAT processing fees alone. Adding an ECR VPC interface endpoint at $0.01/GB dropped the cost to $1,780/month. Annual savings: $74,760.
Interface endpoints cost $0.01/hour per AZ plus $0.01/GB. For a service receiving 10 TB/month in traffic routed through NAT, the endpoint pays for itself in the first week.
Connecting Multiple VPCs: Peering vs Transit Gateway vs PrivateLink
As environments scale beyond a single VPC, three options appear. They have very different cost structures.
Option Connection Cost Data Cost Total at 500 GB/month cross-AZ Best For VPC Peering Free $0.01/GB/direction $10 2-5 VPCs with high traffic Transit Gateway $36.50/mo per attachment $0.02/GB $83 10+ VPCs, transitive routing needed PrivateLink $7.20/mo per AZ $0.01/GB $19.40 Service exposure (1 producer, many consumers)  
VPC Peering is cheapest for small topologies. The connection itself is free; you pay only for cross-AZ or cross-region data. At two to five VPCs, direct peering is almost always the right answer.
Transit Gateway becomes cost-competitive when the number of VPCs grows. At 20 VPCs, full-mesh peering requires 190 peer connections. Transit Gateway requires 20 attachments at $730/month total. The operational overhead of managing 190 peering routes justifies that cost. Below 10 VPCs, it usually does not.
PrivateLink works differently. It is not a routing mechanism but a service exposure model: one producer, many consumers, no shared network access. Consumers call an endpoint DNS name; traffic goes directly to the producer service. The per-AZ charge ($0.01/hour, $7.20/month) applies per endpoint, not per consumer. For internal APIs serving many VPCs, PrivateLink adds security isolation that peering cannot provide.
Egress: CloudFront Changes the Math
Standard AWS egress costs $0.09/GB for the first 10 TB/month, dropping to $0.085/GB for the next 40 TB and $0.07/GB for the next 100 TB.
CloudFront changes the economics for any deliverable content. Data transferred from AWS origins (S3, EC2, ALB, API Gateway) to CloudFront edge locations is completely free. You pay only the CloudFront rate for delivery to end users, which starts slightly lower than direct egress and compounds with cache hit ratios.
For static assets with cache hit ratios above 70%, the effective cost per byte delivered through CloudFront is a fraction of direct egress. One team enabling CloudFront in front of an S3 bucket reported a 98% drop in egress costs with no changes to application code.
AWS expanded the free egress tier to 100 GB/month aggregated across all regions in 2025, which helps small workloads but changes nothing for high-traffic applications.
Where to Start
Not every optimization is equally accessible. This list is ordered by effort-to-savings ratio.
Action Monthly Savings Potential Implementation Effort Add S3 gateway endpoint (free) $45/TB/month in NAT fees eliminated Under 30 minutes Add DynamoDB gateway endpoint (free) $45/TB/month in NAT fees eliminated Under 30 minutes Add ECR interface endpoint $6,000-$74,000/year for busy EKS clusters 1-2 hours Add SSM, CloudWatch, Secrets Manager endpoints $200-$2,000/month depending on call volume 2-4 hours Fix cross-AZ NAT routing in route tables $36,000/year from one config change 2-4 hours Enable Topology Aware Routing in Kubernetes 50-80% reduction in cross-AZ fees for K8s traffic 1 hour Put CloudFront in front of S3 for static content Up to 98% reduction in egress costs 2-4 hours Remove idle NAT Gateways in dev/staging $32.85/month per gateway removed 1 hour  
The first two items on this list cost nothing and take under an hour. Most teams skip them. The S3 gateway endpoint is a route entry in a route table; it does not change how your application code works. If your VPC does not have one, add it today.
For teams running EKS or ECS pulling images from ECR, the interface endpoint ROI is immediate. At $0.01/GB versus $0.045/GB (plus egress), the endpoint pays for itself at roughly 200 GB/month of image traffic. Most clusters exceed that on the first day of a rolling deployment.
The cross-AZ routing audit is the highest-variance item. Teams with correctly configured routing see no savings. Teams with misaligned NAT Gateway placement or default Kubernetes service routing sometimes find that their entire data transfer bill is cross-AZ charges. Run AWS Cost Explorer filtered by “EC2 - Other” and look for DataTransfer-Regional-Bytes. If that line is large, the route table audit is worth two hours of investigation.
Networking costs are not usually the largest line item in a cloud bill. They are often the most addressable one, because the root cause is almost always configuration, not scale.
Written by
Riya MittalAuthor  
Engineer at Zop.Dev
Tagged in
cloud-managementRelated Articles
10 min 
FinOps Anomaly Detection: Why Your Cost Alerts Arrive 3 Days Late
Amanpreet Kaur May 6, 202611 min 
The Shadow Cloud Spend: $50k a Month FinOps Audit of Forgotten Dev Accounts
Amanpreet Kaur May 6, 20267 min 
Developer Productivity Metrics: What to Measure and How to Improve Them
Story points and PR counts measure activity, not outcomes. Here's how to use DORA and SPACE metrics to understand what's actually slowing your team down and what to fix first.
Riya Mittal Apr 9, 2026Read next  How to Detect and Fix CPU Throttling in Kubernetes (And Why It's Costing You)
Most teams discover CPU throttling only after p99 latency spikes and costs climb. Learn how to detect it in minutes using PromQL and fix it by right-sizing your CPU requests and limits.
 Continue reading  ZopDev Resources 
 Stay in the loop 
 Get the latest articles, ebooks, and guides 
  delivered to your inbox. No spam, unsubscribe anytime. 
Open in Claude  ↗   Ask questions about this page  Open in ChatGPT  ↗   Ask questions about this page  Copied!  
 Copyright © ZopDev Technology PVT.LTD. All rights reserved 
 Refund policy  Terms of Service  Privacy policy  built with  love  by ZopDev   ZopDev 
