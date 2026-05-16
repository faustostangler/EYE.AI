---
name: DynamoDB GSIs Are Doubling Your Bill Silently | LeanOps
keywords: (placeholder)
metadata:
  url: https://leanopstech.com/blog/aws-dynamodb-pricing-2026/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
DynamoDB GSIs Are Doubling Your Bill Silently | LeanOps
Home Services Blog Free Resources Careers About Talk to an Expert
Back to Engineering Insights
Cloud Cost Optimization
Apr 26, 2026
By Ravi Kanani
DynamoDB GSIs Double Your Write Costs: How a $200/Month Table Becomes $2,400
Key Takeaway
DynamoDB on-demand costs $1.25 per million writes and $0.25 per million reads in 2026. At 100M daily reads and 20M daily writes, monthly cost is roughly $825 on-demand vs $185 with provisioned capacity and auto-scaling. Each Global Secondary Index doubles your write costs for that index. The single biggest savings lever is switching from on-demand to provisioned with auto-scaling once your traffic is predictable, typically saving 60-80%.
$1.25 Per Million Writes Sounds Reasonable Until You Count the GSIs
Here is what happens to almost every team that adopts DynamoDB. They read the pricing page, see $1.25 per million write request units and $0.25 per million reads in on-demand mode, model their expected traffic, and project a comfortable monthly bill. Maybe $200 for their workload.
Then the real bill shows up at $800. Or $2,400.
Where does the money go? Into three places that never register until invoice day: Global Secondary Indexes that silently replicate every write (doubling or tripling your write costs), storage that grows invisibly because nobody set TTLs on session data, and the delta between on-demand pricing and what provisioned capacity would have cost once traffic stabilized.
We see this pattern at LeanOps with roughly 70% of DynamoDB-heavy clients. The service is genuinely excellent for the right access patterns. But its pricing model punishes teams who do not understand capacity modes, indexing costs, and storage lifecycle. This post breaks down every DynamoDB cost in 2026, models real bills at three production scales, and shows you how to cut 40-60% without sacrificing performance.
DynamoDB Pricing: The Complete 2026 Breakdown
DynamoDB pricing has four core dimensions: read/write throughput, storage, optional features (backups, streams, global tables), and data transfer. The throughput pricing depends entirely on whether you choose on-demand or provisioned capacity mode.
On-Demand Mode Pricing
On-demand mode charges per request with zero capacity planning. You pay exactly for what you use, but at a significant premium.
Key details that matter for your bill:
1 WRU handles items up to 1KB. A 3.5KB item consumes 4 WRUs per write. A 400KB item (DynamoDB's maximum) consumes 400 WRUs per write. Item size directly multiplies your cost.
1 RRU handles items up to 4KB for strongly consistent reads. Eventually consistent reads use 0.5 RRU per 4KB, effectively halving your read cost.
Transactional operations cost 2x. Every TransactWriteItems or TransactGetItems call doubles the unit consumption.
The 25GB free tier only applies to storage, not throughput. And 25GB is nothing for production tables with any real data volume.
Provisioned Mode Pricing
Provisioned mode requires you to set a capacity level (in WCU and RCU per second) and charges hourly for that capacity whether you use it or not. It is dramatically cheaper at steady-state traffic.
The math speaks for itself. On-demand writes cost $1.25 per million. Provisioned writes (with auto-scaling at reasonable utilization) cost approximately $0.19 per million. That is an 85% discount for the same operation, assuming you have enough baseline traffic to justify provisioned capacity.
The breakeven point is surprisingly low. If your table sustains more than roughly 5-10 writes per second consistently, provisioned mode with auto-scaling is cheaper. Below that, or with wildly unpredictable spikes, on-demand makes sense.
Auto-Scaling: The Best of Both Worlds
DynamoDB auto-scaling adjusts provisioned capacity based on actual utilization, with a target utilization percentage (default 70%). This gives you provisioned pricing with near-on-demand flexibility.
The catch: auto-scaling reacts in 1-2 minutes, not seconds. If you get a sudden 10x traffic spike in 30 seconds, you will hit throttling before auto-scaling catches up. For truly spiky workloads with no warning, on-demand is still the safer choice despite the cost premium.
Our recommendation: Set a provisioned baseline with auto-scaling for your predictable floor, then evaluate whether the spiky portion justifies on-demand pricing.
The Hidden Costs: Where DynamoDB Bills Go Sideways
Global Secondary Indexes: The Silent Bill Multiplier
This is the #1 cost surprise in DynamoDB and the source of more "why is my bill so high" conversations than any other feature.
Every write to a table with GSIs triggers a write to each GSI that projects the modified attributes. If your table has 3 GSIs and you write a 1KB item that appears in all three indexes, you consume:
1 WRU for the base table write
1 WRU for GSI #1 replication
1 WRU for GSI #2 replication
1 WRU for GSI #3 replication
Total: 4 WRUs per logical write
At 50 million writes per month, that is the difference between $62.50 (base table only) and $250.00 (with 3 GSIs). The indexes quadrupled your write cost.
It gets worse. GSI capacity is provisioned and billed separately from the base table. Each GSI has its own WCU/RCU allocation, its own auto-scaling configuration, and its own storage bill. A table with 5 GSIs has 6 independent capacity configurations to manage.
What to do about it:
Audit your GSIs. If a GSI has not been queried in 30 days, delete it.
Use sparse indexes. Only project items that match a specific condition into the GSI.
Prefer composite sort keys over additional GSIs. One well-designed sort key can replace 2-3 GSIs.
Consider single-table design patterns that minimize GSI count.
DynamoDB Streams: Cheap Until You Are Not Careful
DynamoDB Streams captures item-level changes and is commonly used for replication, event processing, and triggering Lambda functions.
At first glance, $0.02 per 100K reads seems negligible. But if you have a Lambda function polling the stream every second across 100 shards, you generate 8.6 million read requests per day, costing roughly $1,728/month. The stream is free; the polling is not.
Use Lambda event source mapping with appropriate batch sizes and parallelization to minimize read request costs.
Global Tables: 2x Write Cost for Multi-Region
DynamoDB Global Tables replicate data across AWS regions for disaster recovery and low-latency multi-region access. The cost model:
Replicated writes: Charged at 1.5 WRU per replicated write (50% premium over local writes)
Storage: Billed in each region independently
Data transfer: Cross-region replication transfer at standard rates
A table with 2 regions pays roughly 2.5x the write cost of a single-region table. Three regions: 4x. This adds up fast on write-heavy workloads.
Real-World DynamoDB Cost Modeling
Abstract per-unit pricing is meaningless without production context. Let us model actual costs at three scales.
Assumptions for All Models
Item size: Average 2KB writes, 4KB reads
Read consistency: 80% eventually consistent, 20% strongly consistent
GSIs: 2 active indexes (projecting all attributes)
Storage growth: 50GB current, growing 5GB/month
PITR enabled
Scale 1: 10M Reads + 2M Writes Per Day (Startup SaaS)
At this scale, on-demand costs 4.7x more than provisioned with auto-scaling. The GSI writes alone cost $300 on-demand. If your traffic is remotely predictable at this volume, on-demand is burning money.
Scale 2: 100M Reads + 20M Writes Per Day (Growth-Stage Product)
$5,269 vs $1,026 per month. Same data, same access patterns, same performance. The only difference is capacity mode. And yet we see teams running at this scale on on-demand because "we might spike" or because nobody revisited the initial choice.
If you add Reserved Capacity (1-year term) for the baseline 70% of traffic:
That is $56,652 in annual savings from a configuration change and a commitment. No application code modifications. No migration. No downtime.
Scale 3: 1B Reads + 200M Writes Per Day (High-Scale Platform)
At this scale, the difference between on-demand and optimized provisioned is $46,835 per month. That is $562,000 per year. If your DynamoDB spend is anywhere near this range and you are on on-demand, you are leaving a half-million dollars on the table annually.
The DynamoDB Cost Explosion Calculator: How $200/Month Becomes $2,400
Here is the exact anatomy of how a table that should cost $200/month balloons to $2,400. We see this pattern constantly. Teams start with a clean, well-scoped table and incrementally add features without recalculating total cost.
Starting point: A DynamoDB table in on-demand mode handling 10M reads and 2M writes per day with an average 2KB item size.
From $225 (base reads + writes) to $2,355. The multiplier is 10.5x. And every single line item above is something we have found in real production DynamoDB deployments.
The three biggest offenders:
GSIs on Global Tables (3 GSIs x 2 regions = 6x write amplification): $900/month
DAX cluster running 24/7 for a workload that only needs caching during business hours: $589/month
No TTL on session/temp data causing storage to grow indefinitely: compounds monthly
5 Changes That Cut DynamoDB Bills 60-80%
These are the exact changes, in priority order, that take a $2,355/month table down to $400-600/month. No application rewrites. No migrations. Configuration and data modeling changes only.
Change 1: Switch to Provisioned + Auto-Scaling
Before: On-demand at $1.25/million writes After: Provisioned with auto-scaling at ~$0.19/million writes (target utilization 70%)
How to implement: In the DynamoDB console, select the table, go to "Additional settings" > "Read/write capacity settings" > change to "Provisioned" with auto-scaling enabled. Set target utilization to 70%. Takes effect immediately, zero downtime. You can switch back to on-demand once every 24 hours if needed.
Change 2: Remove Unused GSIs
The audit command (CloudWatch): Check ConsumedReadCapacityUnits for each GSI over the last 30 days in CloudWatch Metrics. Filter by TableName and GlobalSecondaryIndexName. Any GSI averaging under 1 read/second is costing you writes for zero value.
Typical finding: 1-2 of 3 GSIs were created during development for queries that no longer exist or happen once a month (should be a scan, not a dedicated index).
Savings per removed GSI: Eliminates 1x write replication. At 120M WRU/month on provisioned = $23/month per GSI removed. On on-demand = $150/month per GSI removed.
Change 3: Replace Scans with Queries Using Sparse Indexes
Before: Weekly reporting job scans the entire 50M-item table ($50/month in on-demand reads). After: Create a sparse GSI that only contains items matching the reporting criteria. Query the sparse index instead of scanning the full table.
Example: If your report needs only items where status = "completed" in the last 7 days, create a GSI with status as partition key and completedDate as sort key. Only items with these attributes are projected into the index. Query cost drops 90-95% because you read 500K items instead of 50M.
Change 4: Enable TTL to Auto-Delete Expired Data
The problem: Session tokens, rate-limit counters, OTP codes, shopping carts, and event dedup records accumulate forever without TTL.
The fix: Add a ttl attribute (Unix timestamp) to all ephemeral records. Set the TTL attribute in table settings. DynamoDB deletes expired items automatically at zero cost.
Savings calculation:
200GB table where 60% is expired data = 120GB wasted
Storage savings: 120GB x $0.25/GB = $30/month
PITR savings: 120GB x $0.20/GB = $24/month
GSI storage savings: 120GB x 3 GSIs x $0.25/GB = $90/month
Total: $144/month from one TTL attribute
Change 5: Use Eventually Consistent Reads + Compression
Eventually consistent reads: Switch all read operations that tolerate 100-200ms staleness (dashboards, analytics, product catalogs, user profiles) from strongly consistent to eventually consistent. Cost drops 50% on reads instantly.
Compression: For items containing JSON blobs, event payloads, or text content, compress with gzip before writing. A 5KB JSON document compresses to 1.5KB, reducing write cost from 5 WRU to 2 WRU (60% savings on those items).
Combined result of all 5 changes:
That takes the $2,355/month bill down to roughly $1,385/month (41% reduction) from these changes alone. With provisioned mode applied across all components (including Global Tables and DAX scheduling), the bill drops to $500-700/month range (70-75% reduction).
DynamoDB vs Alternatives: When to Consider Switching
DynamoDB is not always the cheapest option. Depending on your access patterns, scale, and operational requirements, alternatives may save 30-70%.
DynamoDB vs Aurora (PostgreSQL/MySQL)
DynamoDB wins on operational simplicity and latency consistency. Aurora wins on cost-per-query for complex workloads and when you need relational features. The worst pattern we see: teams using DynamoDB with elaborate GSI structures to simulate relational queries, paying 3-5x what Aurora would cost.
DynamoDB vs ElastiCache (Redis)
For pure key-value caching with sub-millisecond latency, ElastiCache costs roughly $0.017/hour for a cache.t4g.micro. That is $12.24/month for millions of reads/writes per second. DynamoDB DAX (DynamoDB's built-in caching layer) starts at $0.269/hour ($193/month) for a dax.t3.small.
If your DynamoDB read pattern is mostly hot-key lookups on a small dataset, a $12 Redis node can replace thousands of dollars in DynamoDB read costs.
8 Strategies to Cut Your DynamoDB Bill by 40-70%
These are ordered by impact. The first two alone typically save 50%+.
1. Switch from On-Demand to Provisioned with Auto-Scaling
If your table has sustained more than 10 writes per second for the last 30 days, provisioned mode is almost certainly cheaper. Set auto-scaling target utilization to 70%, with minimum capacity at your baseline floor and maximum at 2x your peak.
The migration is zero-downtime. You can switch capacity modes once every 24 hours.
Expected savings: 60-80% for steady workloads.
2. Audit and Remove Unnecessary GSIs
Run this query in CloudWatch Metrics to find underused GSIs: check ConsumedReadCapacityUnits for each GSI over the past 30 days. Any GSI with near-zero reads is pure write-cost overhead.
We routinely find tables with 4-5 GSIs where only 1-2 are actively queried. Each removed GSI eliminates one full replication of write costs.
Expected savings: 20-50% on write costs per removed GSI.
3. Enable TTL on Ephemeral Data
Session tokens, cart data, rate-limit counters, cache entries. If the data has a natural expiry, set a TTL attribute. DynamoDB deletes expired items automatically at zero cost, reducing storage and backup charges.
A table with 500GB of data where 60% is expired sessions wastes $75/month in storage plus $60/month in backup costs. TTL eliminates this.
Expected savings: $0.45/GB/month on storage + backup for expired data.
4. Use Eventually Consistent Reads (Where Possible)
Eventually consistent reads cost half as much as strongly consistent reads (0.5 RRU vs 1 RRU per 4KB). For read-heavy workloads where data can be a few milliseconds stale (dashboards, analytics, product catalogs, user profiles), this halves your read bill instantly.
In practice, eventual consistency in DynamoDB means "consistent within 100-200ms." For most use cases, that is indistinguishable from strong consistency.
Expected savings: 50% on applicable reads.
5. Compress Large Attributes
DynamoDB charges by item size in 1KB increments for writes. If you store JSON blobs, event payloads, or document content, compressing with gzip or zstd before writing can reduce item size by 60-80%.
A 5KB JSON document compressed to 1.5KB costs 2 WRU instead of 5 WRU. At 100M writes per month, that saves $375 in on-demand mode.
Expected savings: 50-75% on write costs for compressible data.
6. Use Projection Expressions to Reduce Read Size
When reading items, specify only the attributes you need with ProjectionExpression. A 10KB item where you only need 3 attributes (2KB total) costs 1 RCU instead of 3 RCU with a full-item read.
This is especially impactful in scan operations where you might be reading millions of items.
Expected savings: 30-70% on reads of partially-needed items.
7. Implement Write Batching
BatchWriteItem processes up to 25 items per request with the same per-item cost but significantly reduced overhead per operation compared to individual PutItem calls. For Lambda-triggered workloads, batch events before writing.
More importantly, batching reduces the total number of round trips, which cuts Lambda execution time and associated CloudWatch Logs volume.
Expected savings: 15-25% on total stack cost (DynamoDB + Lambda + CloudWatch).
8. Reserved Capacity for Baseline Load
If your minimum sustained traffic is predictable for 1-3 years, Reserved Capacity (separate from provisioned auto-scaling) offers an additional 53-76% discount on the baseline.
Buy Reserved Capacity for your 30th-percentile traffic level, let auto-scaling handle everything above that.
Expected savings: 50-75% on baseline capacity cost.
When DynamoDB Is the Right Choice (And When It Is Not)
DynamoDB Wins
Single-digit millisecond reads at any scale: From 10 to 10 million requests per second with consistent latency. Nothing else in the AWS ecosystem matches this.
Serverless architectures: Zero connection management, no connection pooling, scales from zero to millions without cold starts.
Key-value and simple document access patterns: Partition key + sort key lookups. This is DynamoDB's sweet spot and where it is cost-effective.
Global multi-region replication: Global Tables give you active-active multi-region with conflict resolution built in.
Event-driven systems: DynamoDB Streams + Lambda is a powerful pattern for change data capture and event sourcing.
DynamoDB Loses
Complex queries and reporting: If you need JOINs, aggregations, GROUP BY, or ad-hoc analytics, use Aurora, Redshift, or Athena. Trying to build relational patterns in DynamoDB with GSIs is expensive and fragile.
Low-volume, complex-access workloads: A $30/month Aurora Serverless instance handling 50 queries/second with JOINs will outperform and undercut a DynamoDB table with 5 GSIs trying to serve the same use case.
Large item workloads: DynamoDB's 400KB item limit and per-KB write pricing makes it expensive for document storage. Use S3 for objects, DynamoDB for metadata pointers.
Full-text search: Do not build search on DynamoDB. Use OpenSearch or Elasticsearch. We have seen teams spend $10K/month on DynamoDB scans that a $500/month OpenSearch cluster handles better.
Analytics on operational data: DynamoDB is an OLTP database. Running analytical queries against it (scans, filters across millions of items) is both expensive and slow. Export to S3 + Athena for analytics.
Common DynamoDB Anti-Patterns That Inflate Costs
Anti-Pattern 1: Scan Instead of Query
A Scan reads every item in the table and then filters. A table with 10M items where you need 100 matching records still reads all 10M items (consuming RCU for each) and charges you for the full scan.
Fix: Design your key schema so every access pattern can use Query (partition key + optional sort key condition). If you find yourself using Scan in production, your data model needs restructuring.
Anti-Pattern 2: On-Demand Forever
On-demand mode is designed for unpredictable or new workloads. Once traffic stabilizes (usually within 2-4 weeks of launch), switch to provisioned. We have seen teams leave tables on on-demand for 2+ years, paying 5-7x what provisioned would cost, because nobody revisited the original decision.
Fix: Set a calendar reminder 30 days after launching any new DynamoDB table to evaluate capacity mode.
Anti-Pattern 3: GSI Per Access Pattern
Single-table design is powerful, but some teams interpret it as "add a GSI for every query." Five GSIs means 6x write cost. Before adding a GSI, ask: can this query be served by a composite sort key, a sparse index, or an application-level lookup?
Fix: Audit GSI usage monthly. Remove any GSI with read consumption under 5% of its provisioned capacity.
Anti-Pattern 4: No TTL on Temporary Data
Session tables, rate-limit tables, and event deduplication tables grow forever unless you set TTLs. We have seen 500GB tables where 80% of items expired months ago but still incur storage and backup costs.
Fix: Every table with temporary or expiring data must have a TTL attribute defined at creation time. This is not optional.
The Bottom Line
DynamoDB is a genuinely powerful database with pricing that rewards informed operators and punishes uninformed ones. The gap between on-demand and optimized provisioned capacity is 60-90%, which translates to thousands or tens of thousands of dollars monthly at production scale.
The three highest-impact changes for most teams:
Switch to provisioned + auto-scaling once traffic is predictable (saves 60-80%)
Remove or consolidate GSIs you are not actively querying (saves 20-50% on writes)
Enable TTL on all ephemeral data (eliminates storage waste)
If your DynamoDB bill exceeds $1,000/month and you are on on-demand mode, you are almost certainly overpaying by 4-7x. Our cloud cost optimization team specializes in DynamoDB cost analysis and has helped teams cut NoSQL bills by 40-70% without application changes. Start with a free Cloud Waste Assessment to see where your DynamoDB spend ranks against similar workloads.
For related AWS cost deep-dives, see our full breakdown of AWS Lambda pricing and AWS ECS/Fargate pricing.
Further reading:
AWS Lambda Pricing in 2026: Full Cost Breakdown
AWS ECS and Fargate Pricing in 2026
AWS Cost Optimization Playbook
Cloud Cost Optimization Services
AWS DynamoDB Pricing (Official AWS Documentation)
DynamoDB Best Practices (AWS Well-Architected)
Frequently Asked Questions
How much does AWS DynamoDB cost per read and write in 2026?
Is DynamoDB on-demand or provisioned capacity cheaper?
How much do DynamoDB Global Secondary Indexes cost?
What is DynamoDB Reserved Capacity and how much does it save?
How do I reduce my AWS DynamoDB bill by 50% or more?
Stop Overpaying for Cloud Infrastructure
Our clients save 30-60% on their cloud bill within 90 days. Get a free Cloud Waste Assessment and see exactly where your money is going.
Free Cloud Waste Assessment Our Services
Related Insights
View All
Cloud Cost Optimization May 7, 2026 80% of GPU Spend Wasted: 3 K8s Changes That Cut AI Infra Bills 60% in 2 Weeks Learn how to achieve cloud cost optimization for AI and machine learning workloads on Kubernetes using right-sizing, Karpenter, Spot strategies, and scale-to-zero techniques to modernize infrastructure and reduce cloud waste.
Cloud Cost Optimization May 6, 2026 EKS vs GKE vs AKS Pricing in 2026: Control Plane, Node Costs, and the Real Bill at 50-500 Nodes AWS EKS charges $0.10/hour ($73/month) per cluster for the control plane alone. GKE Standard is free but Autopilot charges per pod resource. AKS control plane is free. But the control plane is less than 5% of your total Kubernetes bill. We compare the real all-in cost at 50, 200, and 500 nodes including compute, networking, storage, and load balancers.
Cloud Cost Optimization May 5, 2026 Your $10 Lambda Bill Is Really $57: API Gateway, NAT, and CloudWatch Add 82% AWS Lambda charges per request ($0.20/1M) and per GB-second of compute ($0.0000166667). But the real bill includes Provisioned Concurrency, data transfer, CloudWatch Logs, and API Gateway fees that can 3-5x your expected cost. We break down every Lambda fee in 2026 with real-world modeling at 1M, 10M, and 100M invocations.
View All Insights
Elite Cloud Engineering for fast-moving teams. We automate ops, slash waste, and harden infrastructure without the fluff.
LinkedIn Twitter
Services
Cost Optimization & FinOps
Cloud Migration & Modernization
Automated Cloud Operations
Company
About Us
Careers
Engineering Blog
Free Resources
Talk to an Expert
Status
Systems Operational
Infrastructure grade engineering delivered on-demand.
© 2026 LeanOps Technologies. Built for Speed.
Privacy Terms Security
