---
name: Amazon DynamoDB Pricing: Why GSIs Triple Your Bill (2026) - CloudBurn
keywords: (placeholder)
metadata:
  url: https://cloudburn.io/blog/amazon-dynamodb-pricing
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Amazon DynamoDB Pricing: Why GSIs Triple Your Bill (2026) | Cloud Burn
 CloudBurn Home
Blog
Docs
Tools
Features
Roadmap
Changelog
⌘K Search
Toggle theme
Join the CloudBurn Discord community
1.8k
Open main menu
Toggle theme Join the CloudBurn Discord community 1.8k Close menu
Home
Blog
Docs
Tools
Features
Roadmap
Changelog
amazon-dynamodb dynamodb-pricing cost-optimization aws-database finops dynamodb-calculator
Amazon DynamoDB Pricing: Why GSIs Triple Your Bill (2026)
Complete guide to Amazon DynamoDB pricing. Compare on-demand vs provisioned modes, learn hidden costs, and estimate your bill with our free calculator.
April 7th, 2026
23 min read
192 views
5 likes
Amazon DynamoDB pricing looks simple at first glance: pick a capacity mode, pay for reads, writes, and storage. But then you add a few Global Secondary Indexes, enable backups, maybe set up a Global Table, and suddenly your bill is 3x what you expected. The official pricing page lists every rate, but it doesn't help you answer the question that actually matters: how much will DynamoDB cost for my specific workload?
On top of that, two major pricing changes in the last 18 months have reshuffled the economics. AWS cut on-demand throughput prices by 50% in November 2024, and then launched Database Savings Plans in December 2025 with up to 18% additional savings. Most pricing guides haven't caught up.
This guide breaks down every Amazon DynamoDB pricing dimension with current numbers, walks through real-world cost scenarios, and gives you a decision framework for choosing between capacity modes. If you want a quick estimate, the DynamoDB pricing calculator lets you model your workload in minutes.
All prices are for US East (N. Virginia) as of February 2026. Prices vary by region.
How Much Does DynamoDB Cost?
DynamoDB is pay-as-you-go with no minimum fees or upfront commitments. Your total cost depends on four dimensions: throughput (reads and writes), storage, backups, and add-on features like Global Tables or DAX.
Here's a quick ballpark:
Hobby project (small CRUD app, under 25 GB): $0/month (fits within the free tier)
Mid-size SaaS (50 GB, 100M reads/month, 20M writes/month): $50-200/month
High-volume production (500 GB, 1B reads/month, 500M writes/month): $1,000-5,000+/month
These ranges swing based on your capacity mode choice, number of GSIs, and whether you're using commitment discounts. The capacity mode alone can create a 2-3x cost difference for the same workload.
Here's the full pricing summary for quick reference:
To understand where your costs will land, you need to know how DynamoDB's pricing model is structured.
How DynamoDB Pricing Works
DynamoDB pricing has two layers. The first is your capacity mode, which determines how you pay for reads and writes. This is the biggest cost driver for most workloads. The second layer is add-on features like storage, backups, DynamoDB Streams, Global Tables, and DAX, which each add incremental costs on top of throughput.
Each table independently has its own capacity mode and table class. You can run some tables on on-demand and others on provisioned within the same account, mixing and matching based on each table's access patterns.
DynamoDB Table Cost
Throughput
(Capacity Mode)
Additional Costs
On-Demand
(Pay per request)
$1.25/M writes
$0.25/M reads
Provisioned
(Pay per hour)
~$0.47/mo per WCU
~$0.09/mo per RCU
Storage
$0.25/GB standard
$0.10/GB IA
Backups
PITR $0.20/GB
DynamoDB Streams
$0.02/100K reads
Data Transfer
$0.09/GB cross-region
Global Tables
Replicated writes
per region
DAX Cache
Per node-hour
Capacity Modes (The Biggest Cost Driver)
You choose between two capacity modes per table. On-demand charges per request with zero capacity planning. You pay for exactly what you use. Provisioned requires you to specify reads and writes per second, billing hourly for that reserved capacity regardless of actual usage.
The November 2024 price cut made on-demand 50% cheaper, which fundamentally changed the break-even point between these two modes. I'll cover the comparison in detail after breaking down each mode's pricing.
Storage and Add-On Features
Beyond throughput, you'll pay for data storage ($0.25/GB-month for Standard tables), optional backups, and any add-on features you enable. For most applications, throughput dwarfs storage costs. But for data-heavy, low-traffic tables (think audit logs or historical records), storage can become the dominant cost component, and that's where the Standard-IA table class saves money.
On-Demand Pricing (Pay-Per-Request)
On-demand mode is the simplest pricing model: you pay per request with no capacity planning. DynamoDB handles scaling automatically. After the November 2024 price reduction, on-demand costs dropped by 50%, making it the default recommendation for most workloads.
How request units are calculated:
1 WRU = one write of up to 1 KB. Items larger than 1 KB consume additional WRUs, rounded up to the next KB boundary. A 2.5 KB write costs 3 WRUs.
1 RRU = one strongly consistent read of up to 4 KB, or two eventually consistent reads of up to 4 KB each.
Transactional operations cost double: 2 WRUs per transactional write, 2 RRUs per transactional read.
Worked example: 10 million writes and 50 million eventually consistent reads per month. Writes: 10M x $1.25/M = $12.50. Reads: 25M RRUs (eventually consistent = half) x $0.25/M = $6.25. Total throughput: $18.75/month.
One feature worth knowing about: you can set a maximum throughput on on-demand tables to cap costs. If a runaway Lambda function or a traffic spike pushes reads beyond your configured ceiling, DynamoDB throttles instead of racking up charges. I've seen this prevent bill surprises on more than one occasion.
On-demand tables start at 4,000 writes/second and 12,000 reads/second for new tables, and can instantly handle up to double the previous peak traffic. If traffic exceeds 2x the previous peak within 30 minutes, you might see throttling. For most applications, this auto-scaling behavior is invisible.
Provisioned Capacity Pricing
Provisioned mode charges by the hour for read and write capacity you reserve, regardless of whether you actually use it. The tradeoff is clear: lower unit costs in exchange for capacity planning overhead.
The capacity unit calculation mirrors on-demand: 1 WCU = one write per second up to 1 KB, 1 RCU = one strongly consistent read per second up to 4 KB (or two eventually consistent reads). Transactional operations still cost double.
Worked example: Provisioning 100 WCUs and 500 RCUs for a full month. Writes: 100 WCU x $0.47/month = $47.00. Reads: 500 RCU x $0.09/month = $45.00. Total throughput: $92.00/month. But if your actual peak usage only hits 60 WCUs and 300 RCUs, you're paying for 40% unused write capacity and 40% unused read capacity.
One operational detail that trips people up: provisioned throughput can only be decreased 27 times per day (4 decreases available at the start of the day, plus 1 additional decrease per hour). If you're manually adjusting capacity, this limit matters.
Auto Scaling with Provisioned Mode
Auto scaling removes most of the manual capacity management pain. You set a target utilization percentage (typically 70%), a minimum, and a maximum, and DynamoDB adjusts capacity within those bounds.
The catch: auto scaling responds to sustained load changes, not sudden spikes. It's watching CloudWatch metrics at one-minute intervals and making adjustments based on trends. If you get a burst of traffic that doubles in 30 seconds, auto scaling won't react fast enough. For workloads with less than 30% traffic variance, provisioned with auto scaling is the sweet spot. For anything spikier, on-demand handles the unpredictability better.
On-Demand vs Provisioned: Which Mode Should You Choose?
This is the question I see most often on AWS forums, and the November 2024 price cut changed the answer for a lot of workloads.
Before the cut, on-demand was roughly 6.5x more expensive per unit than provisioned at full utilization. Now it's about 2.5-3x. That narrower gap means on-demand wins for a much wider range of workloads than it used to, because you need very high, consistent utilization to make provisioned cheaper after accounting for the capacity you provision but don't use.
Here's my decision framework:
New application, unknown traffic? Start with on-demand. Always. Analyze CloudWatch metrics for at least 2 weeks before even considering provisioned.
Unpredictable or spiky traffic? Stay on on-demand. The cost premium over provisioned is smaller than it used to be, and over-provisioning to handle spikes often eliminates the savings.
Predictable traffic with less than 30% variance? Switch to provisioned with auto scaling. This is where provisioned actually pays off.
High-volume, steady workload? Provisioned with reserved capacity (53-77% discount) or Database Savings Plans (up to 18% on-demand discount).
Yes
No
No
Yes
No
Yes
Yes
No
New application?
Start with On-Demand
(Analyze 2+ weeks before switching)
Is traffic
predictable?
On-Demand
Less than 30%
variance?
On-Demand
Provisioned +
Auto Scaling
High volume,
steady baseline?
Add Reserved Capacity
or Database Savings Plans
Stay with
Auto Scaling
To see the exact cost difference for your workload, run the numbers through the DynamoDB pricing calculator.
You can switch between capacity modes up to twice per 24-hour period, so this isn't a permanent commitment. I've seen teams run on-demand during business hours and switch to provisioned overnight for batch processing, though that's an edge case.
Storage and Table Class Pricing
DynamoDB charges for storage based on raw byte size plus a small per-item overhead. There's no limit on table size, and storage pricing is the same regardless of capacity mode.
Standard vs Standard-IA Table Classes
Standard-IA cuts storage costs by 60% but charges approximately 25% more for reads and writes. The math is straightforward: switch to Standard-IA when storage costs exceed 50% of your total table cost (throughput plus storage combined).
This crossover happens more often than you'd expect. Application logs, old social media posts, historical time-series data, audit trails: any table where data grows fast but gets accessed infrequently. A 500 GB table with minimal read/write traffic costs $125/month on Standard vs $50/month on Standard-IA. That's $900/year saved on one table.
A few details that matter for planning:
Standard-IA provides identical latency, throughput, durability, and availability as Standard. There's no performance tradeoff.
Table class can be changed at any time, but limited to 2 changes per 30-day period.
All GSIs on a table inherit the table class. You can't mix Standard and Standard-IA within the same table.
Reserved capacity is not available for Standard-IA tables. If you're comparing Standard + reserved capacity vs Standard-IA, factor in the reserved capacity discount.
Commitment Discounts: Reserved Capacity and Database Savings Plans
If you have steady DynamoDB usage, two commitment mechanisms can significantly cut costs. They work differently and target different scenarios, but both offer real savings for workloads past the experimentation phase.
The key distinction: reserved capacity gives deeper discounts (up to 77%) but only works with provisioned mode and locks you into a specific region. Database Savings Plans offer smaller discounts (up to 18%) but cover both capacity modes, all regions, and multiple AWS database services from a single commitment. They cannot be combined on the same workload.
Reserved Capacity (Provisioned Mode Only)
Reserved capacity is the deepest discount available for DynamoDB, but it comes with significant constraints.
Reservations are purchased in blocks of 100 WCUs or 100 RCUs. They only apply to the Standard table class (not Standard-IA), and they're tied to the specific region where you buy them. You can't sell, cancel, or transfer reservations to another account.
At high volumes, the savings are substantial. A workload consuming 1,000 WCUs steady-state costs about $470/month on standard provisioned pricing. With a 3-year reservation, that drops to roughly $108/month. But you're committing to 3 years of that exact capacity in that exact region, which is a bet not every team should make.
Database Savings Plans (New, December 2025)
Database Savings Plans launched at re:Invent 2025, and they're the first commitment discount that works with DynamoDB on-demand mode. You commit to a $/hour spend amount for a 1-year term with no upfront payment.
What makes Database Savings Plans interesting is their flexibility. The discount applies automatically regardless of region, table class, or billing mode. They also cover Global Tables replicated writes. And the same commitment covers 9 other AWS database services including Aurora, RDS, ElastiCache, DocumentDB, and OpenSearch.
For teams running DynamoDB alongside Aurora or RDS, this is a single commitment that covers your entire database footprint. The discount is shallower than reserved capacity, but the flexibility is worth it for workloads that might shift between on-demand and provisioned or across regions.
Currently only 1-year terms are available (no 3-year option yet). For a deeper comparison of how Database Savings Plans fit alongside Compute, EC2 Instance, and SageMaker Savings Plans, see all four types of AWS Savings Plans.
Additional Feature Pricing
Beyond capacity and storage, DynamoDB has several add-on features that each carry their own costs. None of these are required, but most production workloads use at least one or two. Here's what each costs.
Global Tables
Global Tables replicate data across multiple AWS regions for low-latency local reads and multi-region writes. The November 2024 price reduction cut replicated write costs by up to 67%, making multi-region architectures significantly more affordable.
Post-reduction, replicated writes are priced the same as single-region writes:
The cost multiplier is straightforward: a 3-region Global Table costs 3x the write throughput of a single-region table, since every write replicates to all regions. A Global Table with 3 replicas generating 42.5 million writes per month now costs roughly $8.71/month, down from $26.56 before the price cut.
Backup and Restore
DynamoDB offers two backup mechanisms, and the costs are separate from your throughput and storage charges.
PITR is the one most teams should enable for production tables. At $0.20/GB-month, a 100 GB table adds $20/month for the ability to restore to any second within the last 35 days. Cold storage via AWS Backup is dramatically cheaper for long-term retention, but requires a 90-day minimum. The free tier includes 25 GB of on-demand backup storage.
Restore costs include the full table size plus all Local and Global Secondary Indexes. A 100 GB table with 30 GB of GSI data costs $19.50 to restore (130 GB x $0.15). You can estimate backup costs for DynamoDB and other services with the AWS Backup pricing calculator.
DynamoDB Streams
Streams captures item-level changes for event-driven architectures, CDC pipelines, and cross-service integration. DynamoDB Streams is one of the sources that EventBridge Pipes can consume for point-to-point integrations.
The pricing is simple, but the free tier is generous. Lambda triggers read Streams for free (this is the most common consumer). Global Tables replication reads are also free. And every account gets 2.5 million free read requests per month per region. For most Lambda-driven architectures, Streams costs nothing beyond the Lambda invocation itself.
DAX (In-Memory Cache)
DAX provides microsecond read latency for DynamoDB, priced per node-hour with no free tier and no reserved pricing.
A 3-node cluster is the minimum for production (fault tolerance across availability zones). The smallest production-grade option, three dax.t3.small nodes, runs about $86/month. That's a meaningful cost, so DAX only makes sense when you're either saving more than $86/month in DynamoDB read throughput by caching, or you need sub-millisecond latency that DynamoDB's single-digit millisecond reads can't satisfy.
T3 instances run in unlimited mode, meaning CPU credits beyond the baseline are charged at $0.096 per vCPU-hour. For read-heavy caching workloads that consistently spike above baseline, R5 nodes with dedicated CPU might be cheaper despite the higher sticker price.
Data Transfer
One quick win: VPC gateway endpoints for DynamoDB eliminate data transfer charges within the same region and keep traffic off the public internet. They're free to create and maintain, so there's no reason not to use them.
DynamoDB Free Tier
DynamoDB's free tier is always-free. Unlike most AWS free tier benefits that expire after 12 months, these allowances remain available indefinitely on every AWS account.
What actually fits within the free tier: 25 RCUs and 25 WCUs support roughly 25 strongly consistent reads/second and 25 writes/second, which translates to about 2.1 million reads and 2.1 million writes per day for items under 4 KB and 1 KB respectively. That's enough for personal projects, prototypes, small CRUD applications with a few hundred active users, and dev/test environments.
What doesn't fit: the free tier only applies to provisioned mode. On-demand tables don't get free capacity units. And if your data exceeds 25 GB or you need more than 25 reads/writes per second sustained, you'll start paying. For a hobby project, though, DynamoDB is genuinely free.
What DynamoDB Actually Costs: Real-World Examples
Unit prices don't tell you much without context. Here are three workload profiles with full cost breakdowns using current pricing. Use the DynamoDB pricing calculator to model your own workload.
Hobby Project (Free Tier)
Scenario: Personal task management app, 500 items averaging 500 bytes each, fewer than 100 reads and writes per hour, 25 MB of storage.
This fits entirely within the free tier using provisioned mode. If you used on-demand instead, you'd pay a few cents per month for the same traffic, since on-demand doesn't qualify for the free capacity units.
Mid-Size SaaS Application
Scenario: Multi-tenant SaaS backend. 50 GB storage, 100 million eventually consistent reads/month, 20 million writes/month (average item size 1 KB for writes, 2 KB for reads). 3 GSIs with INCLUDE projection. PITR enabled.
Notice how 3 GSIs turned 20 million base writes into 80 million total write request units. That 4x multiplier is the hidden cost most people miss. I'll dig into this more in the hidden costs section.
Provisioned with auto scaling is cheaper here because this SaaS workload has predictable daily patterns. But if traffic is spiky (think a product launch or viral moment), on-demand avoids the risk of throttling and over-provisioning.
High-Volume Production Workload
Scenario: IoT data ingestion platform. 500 GB storage, 1 billion eventually consistent reads/month, 500 million writes/month (average 512 bytes per write, 1 KB per read). 5 GSIs. Global Table across 2 regions. PITR enabled.
At this scale, the capacity mode choice is dramatic. On-demand costs 5x more than provisioned with auto scaling, and 8x more than provisioned with reserved capacity. The 5 GSIs multiply base writes by 6x, making the throughput cost 6x what you'd expect from the base table alone.
This is the kind of workload where reserved capacity pays for itself within the first few months, even accounting for the upfront payment and the inflexibility.
Hidden Costs and Gotchas
If your DynamoDB bill is higher than you expected, one of these is usually the reason.
GSI write amplification is the #1 hidden cost. Every write to your base table triggers a write to each GSI that contains the item's attributes. With 5 GSIs, a single base table write consumes 6 total write units (1 base + 5 GSIs). It gets worse: if an update changes a GSI key attribute value, that GSI incurs 2 write units (a delete plus a put). With 10 GSIs, a single write can consume 11 total write units in the worst case. I've seen teams add GSIs casually during development and then wonder why their production write costs are 5x the estimate.
Item size rounding adds up at scale. Writes are billed in 1 KB increments, reads in 4 KB increments, always rounded up. A 1.1 KB write costs 2 WRUs, not 1. At 100 million writes per month, that rounding from 1.1 KB to 2 KB doubles your write cost. Keeping items compact, especially under the 1 KB and 4 KB boundaries, has a real dollar impact.
Transactional operations cost double. TransactWriteItems costs 2 WRUs per 1 KB. TransactGetItems costs 2 RRUs per 4 KB. If you're using transactions heavily, your effective throughput cost is 2x what the standard pricing table suggests.
Filter expressions still consume full read capacity. A query that reads 100 items from a partition but filters down to 10 results still consumes capacity for all 100 items. The filtering happens after DynamoDB reads the data. If you're relying heavily on filter expressions, you're paying for data you're throwing away. Design your key schema and GSIs so the query itself returns only what you need.
GSI storage is a separate copy. Each GSI stores its own copy of projected attributes plus 100 bytes of overhead per item. Using ALL projection on a table with 5 GSIs means you're storing 6 copies of your data. Switch to KEYS_ONLY or INCLUDE projection to keep GSI storage lean.
Auto scaling can't handle sudden spikes. It watches CloudWatch metrics and adjusts based on sustained trends, not instantaneous changes. A flash sale that doubles traffic in 30 seconds will cause throttling before auto scaling reacts. If spiky traffic is your reality, on-demand is the safer choice even at higher per-unit cost.
How to Reduce Your DynamoDB Bill
Here are the most impactful cost optimization strategies, ordered by typical savings magnitude. Most teams can cut their DynamoDB bill by 30-60% by implementing the first four.
1. Choose the right capacity mode. This is the highest-impact decision. Start with on-demand for new applications, then analyze usage patterns for at least 2 weeks. If your traffic is predictable with less than 30% variance, switch to provisioned with auto scaling. On-demand is the better choice when utilization would be below ~14% of provisioned capacity.
2. Lock in commitment discounts. For steady provisioned workloads, reserved capacity saves 53-77%. For flexible or mixed workloads, Database Savings Plans save up to 18% across both modes with no upfront payment. A hybrid approach works well: reserved capacity for your predictable baseline, Database Savings Plans for variable usage.
3. Manage GSIs aggressively. Use KEYS_ONLY or INCLUDE projection instead of ALL. Remove unused GSIs. Use sparse indexes (only items with the indexed attribute are included, which reduces both write amplification and storage). Every GSI you remove saves write costs on every single write operation.
4. Optimize item size. Compress attribute values (JSON compression achieves 70-80% reduction). Use short attribute names. Use epoch timestamps instead of ISO date strings. Store items larger than ~100 KB in S3 with a DynamoDB pointer. Keeping items under the 1 KB write boundary and 4 KB read boundary avoids costly rounding.
5. Default to eventually consistent reads. Eventually consistent reads cost half the capacity of strongly consistent reads. Unless your application requires the most up-to-date data on every read, use the default eventually consistent option.
6. Enable TTL for automatic cleanup. DynamoDB TTL deletes expired items at zero cost (no WCU consumption for TTL deletions). This reduces storage costs and keeps tables lean without writing deletion logic.
7. Switch to Standard-IA for storage-heavy tables. When storage exceeds 50% of your total table cost, Standard-IA saves 60% on storage at the expense of 25% higher read/write rates. This is common for log tables, historical data, and infrequently accessed archives.
8. Use queries instead of scans. Scans read the entire table and consume capacity proportional to table size. Queries target specific partition and sort key ranges, consuming capacity proportional to the result set. A well-designed key schema eliminates most scans.
9. Set max throughput on on-demand tables. This prevents runaway costs from application bugs, traffic spikes, or DDoS scenarios. It's a cost safety net with no downside for workloads that have a known upper bound.
10. Deploy VPC gateway endpoints. Free to set up, they eliminate data transfer charges for DynamoDB traffic within the same region and keep data off the public internet. If your application talks to DynamoDB from within a VPC (Lambda in VPC, EC2, ECS), this is a no-brainer.
11. Monitor and right-size continuously. Use AWS Cost Explorer to break down DynamoDB spending by table. Enable Cost Anomaly Detection for alerts. Tag tables with cost allocation tags for team-level breakdowns. Review CloudWatch consumed vs provisioned capacity to identify over-provisioned tables.
12. Choose the cheapest region. If data residency isn't a constraint, us-east-1, us-east-2, and us-west-2 offer the lowest DynamoDB pricing. The regional difference is significant: storage costs $0.25/GB in us-east-1 vs $0.375/GB in sa-east-1 (Sao Paulo), a 50% premium.
For a broader framework on reducing your AWS bill beyond DynamoDB, check out our AWS cost optimization best practices, why your AWS bill keeps growing, and the AWS cost optimization checklist.
Key Takeaways
DynamoDB pricing depends on four dimensions: throughput (the biggest driver for most workloads), storage, backups, and add-on features. The capacity mode choice has the largest cost impact, and after the November 2024 price cut, on-demand is the right starting point for most workloads. Switch to provisioned with auto scaling only after confirming predictable traffic patterns.
Database Savings Plans (December 2025) offer a new way to save 12-18% across both capacity modes without the rigidity of reserved capacity. For high-volume steady workloads, reserved capacity still delivers the deepest discounts at 53-77%.
GSIs are the #1 hidden cost multiplier. Each GSI multiplies write costs, and ALL projection inflates storage. Be deliberate about every index you add.
Run your workload through the DynamoDB pricing calculator to compare costs across on-demand, provisioned, and commitment-discounted options before you commit. For teams deploying DynamoDB via CDK or Terraform, you can estimate infrastructure costs before deploying and follow AWS CDK best practices to catch pricing surprises during code review instead of on your monthly bill.
What's driving your DynamoDB costs? Have you found optimization strategies beyond what's covered here? Drop your experience in the comments.
CloudBurn
Stop Deploying Blind: Get Cost Visibility in Every PR
CloudBurn is an open-source policy engine that scans your Terraform and CloudFormation for costly patterns in CI, and discovers waste in your live AWS account. Install with brew or npm.
Get CloudBurn on GitHub
Frequently Asked Questions
Is Amazon DynamoDB free?
Yes, DynamoDB has an always-free tier that includes 25 RCUs, 25 WCUs, and 25 GB of storage. Unlike most AWS free tier benefits, these allowances never expire. Small apps and prototypes can run indefinitely at $0/month using provisioned mode.
Is DynamoDB expensive?
It depends on your access patterns. DynamoDB is cost-effective for key-value lookups at scale but gets expensive for workloads with many GSIs, heavy full-table scans, or frequent transactional operations. The November 2024 price cut reduced on-demand costs by 50%, making it significantly cheaper than before.
How does the November 2024 price reduction affect my costs?
On-demand throughput dropped by 50% and Global Tables replicated writes dropped by up to 67%. If you're on on-demand mode, your throughput costs automatically halved. The break-even point between on-demand and provisioned shifted significantly in on-demand's favor, meaning fewer workloads benefit from switching to provisioned.
Can I switch between on-demand and provisioned mode?
Yes, you can switch up to twice per 24-hour period. Start with on-demand, analyze CloudWatch metrics for 2 or more weeks, then evaluate provisioned if your traffic is predictable with less than 30% variance.
Do Database Savings Plans work with DynamoDB?
Yes, since December 2025. Database Savings Plans offer up to 18% discount on DynamoDB on-demand throughput and up to 12% on provisioned capacity. They apply automatically regardless of region, table class, or billing mode, and also cover 9 other AWS database services from a single commitment.
How do I estimate my DynamoDB costs before deploying?
Use the CloudBurn DynamoDB pricing calculator to model your specific workload across capacity modes. Input your expected read/write volumes, storage size, number of GSIs, and any add-on features to get a detailed monthly cost estimate.
Share this article on ↓
Share this article on →
 [](https://www.reddit.com/submit?url=https%3A%2F%2Fcloudburn.io%2Fblog%2Famazon-dynamodb-pricing&title=Amazon DynamoDB Pricing: Why GSIs Triple Your Bill (2026)) [](https://api.whatsapp.com/send?text=Amazon DynamoDB Pricing: Why GSIs Triple Your Bill (2026)%0A%0Ahttps%3A%2F%2Fcloudburn.io%2Fblog%2Famazon-dynamodb-pricing) 
0 comments
Write Preview 
Sign in with GitHub
Related reading
[
Amazon RDS Pricing: MySQL 5.7 Users Just Got a $292/Month Fee
Mar 9, 2026 29 min amazon-rds / aws-pricing 231 0](https://cloudburn.io/blog/amazon-rds-pricing)
[
Amazon Macie Pricing: What 500M S3 Objects Actually Costs
Mar 13, 2026 22 min amazon-macie / macie-pricing 34 5](https://cloudburn.io/blog/amazon-macie-pricing)
[
Amazon ECR Pricing: What $0.10/GB Doesn't Tell You
Mar 11, 2026 24 min amazon-ecr / ecr-pricing 206 0](https://cloudburn.io/blog/amazon-ecr-pricing)
[
AWS KMS Pricing: Complete Breakdown + Real-World Cost Examples
Mar 8, 2026 22 min aws-kms / aws-pricing 88 0](https://cloudburn.io/blog/aws-kms-pricing)
[
Amazon EventBridge Pricing: 6 Components, 1 Surprise Bill
Feb 22, 2026 23 min amazon-eventbridge / eventbridge-pricing 49 0](https://cloudburn.io/blog/amazon-eventbridge-pricing)
Newsletter
Get product updates and practical AWS cost writeups.
Subscribe for changelogs, new tools, and technical cost optimization posts built for engineers.
Email address
Subscribe
Or
OR SIGN UP WITH
By signing up you agree to our privacy policy.
← Back to blog
 CloudBurn
AWS cost intelligence platform that automatically identifies waste, optimizes resources, and provides actionable recommendations to reduce cloud spend.    
Product
Features
Roadmap
Changelog
About
Blog
Newsletter
Docs
Contact
Free Tools
Lambda Cost Calculator
EC2 Pricing Calculator
S3 Pricing Calculator
EBS Pricing Calculator
Fargate Pricing Calculator
RDS Pricing Calculator
Aurora Cost Calculator
See all tools →
[
Newsletter
](https://cloudburn.io/newsletter)
Subscribe for CloudBurn product updates, changelogs, and actionable AWS cost optimization tips delivered to your inbox.
Email address
Subscribe
3 subscribers
OR SIGN UP WITH
By signing up you agree to our privacy policy.
CloudBurn © 2026 | Terms & Privacy
Built with ❤ by Towards the Cloud
