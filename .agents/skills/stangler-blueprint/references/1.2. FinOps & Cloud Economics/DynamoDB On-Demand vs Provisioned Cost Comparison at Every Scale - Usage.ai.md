---
name: DynamoDB On-Demand vs Provisioned: Cost Comparison at Every Scale - Usage.ai
keywords: (placeholder)
metadata:
  url: https://usage.ai/blogs/aws/reserved-instances/dynamodb/on-demand-vs-provisioned/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
DynamoDB On-Demand vs Provisioned: You Pick, You Pay
Skip to content
Product
Resources
Blogs Case Studies Documentation FAQ
Pricing
Company
Become a Partner Careers About Us
Login Get a Demo
Product
Resources
Blogs Case Studies Documentation FAQ
Pricing
Company
Become a Partner Careers About Us
Login Get a Demo
All blog posts
AWS, Dynamodb
DynamoDB On-Demand vs Provisioned: Cost Comparison at Every Scale
Debesh Singh
Engineering and Chief of Staff
Originally Published on April 23, 2026 
Updated April 29, 2026 
11 min read 
On this page
How Does DynamoDB On-Demand vs Provisioned Pricing Compare Side by Side?
What Is the Break-Even Utilization Rate for DynamoDB On-Demand vs Provisioned?
How Does DynamoDB On-Demand vs Provisioned Cost Scale from 1 Million to 1 Billion Requests?
How Did the November 2024 On-Demand Price Cut Change the Comparison?
How Does DynamoDB Auto Scaling Affect Provisioned Capacity Cost?
How Do Database Savings Plans Change the DynamoDB On-Demand vs Provisioned Decision?
How Should You Measure Utilization to Choose Between DynamoDB On-Demand and Provisioned?
How Does Reserved Capacity Stack on Top of Provisioned Mode?
Choose On-Demand When… Choose Provisioned When…
Frequently Asked Questions
Choose DynamoDB on-demand mode if your traffic is unpredictable, spiky, or under 10 million requests per month. Choose provisioned mode if your workload sustains consistent throughput where capacity utilization stays above 40%, and choose provisioned with reserved capacity if utilization stays above 70% for predictable, long-running workloads. After the November 2024 price cut, on-demand is now the better default for most new tables. Provisioned still delivers 5-6x cheaper per-request costs at full utilization. 
How Does DynamoDB On-Demand vs Provisioned Pricing Compare Side by Side?
The core DynamoDB on-demand vs provisioned capacity cost difference comes down to billing model: per-request versus per-hour. Here is the direct pricing comparison for US East.
The per-million-write cost gap tells the story: on-demand at $1.25/M is approximately 26x more expensive than provisioned at 100% utilization ($0.047/M), and 96x more expensive than 3-year reserved ($0.013/M). But 100% utilization is unrealistic. Real-world provisioned utilization rates typically range from 30% to 70%, which narrows the gap considerably.
What Is the Break-Even Utilization Rate for DynamoDB On-Demand vs Provisioned?
The critical question in the DynamoDB on-demand vs provisioned capacity cost decision is: at what utilization percentage does provisioned become cheaper than on-demand?
A single provisioned WCU running for one month costs: $0.00065 x 730 hours = $0.4745/month. That WCU supports 1 write/second, or approximately 2,628,000 writes/month (1 x 60 x 60 x 24 x 30.4). The same 2.628 million writes on-demand cost: 2.628M x $1.25/M = $3.285.
Break-even: $0.4745 / $3.285 = 14.4% utilization. If a single provisioned WCU is utilized more than 14.4% of the time, provisioned mode is cheaper than on-demand for that unit. However, you must provision for your peak, not your average. If your peak is 100 WCU but your average is 30 WCU (30% utilization), you pay for 100 WCU-hours while using 30. The effective cost per write rises as utilization drops.
Practical break-even with auto scaling overhead: accounting for auto scaling delays (1-2 minutes to scale up), scaling buffer (typically 20-30% headroom), and the minimum provisioned floor, the practical break-even for DynamoDB provisioned vs on-demand pricing sits at approximately 35-40% sustained utilization. Below 35%, on-demand is almost always cheaper. Above 40%, provisioned starts winning. Above 70%, provisioned with reserved capacity is the clear winner. 
Also read: AWS Budgets vs Cost Explorer: Key Differences Explained
How Does DynamoDB On-Demand vs Provisioned Cost Scale from 1 Million to 1 Billion Requests?
Here is the full DynamoDB on-demand vs provisioned capacity cost comparison across six scale tiers, assuming 1 KB writes with a 50/50 read-write ratio and eventually consistent reads.
At 1 billion requests per month, the gap between DynamoDB on-demand cost ($750) and provisioned with 1-year reserved capacity ($255.60) is $494.40/month, or $5,933 per year. At this scale, reserved capacity pays for itself within the first two months of the commitment term.
How Did the November 2024 On-Demand Price Cut Change the Comparison?
AWS reduced DynamoDB on-demand pricing by 50% effective November 1, 2024 (verify at aws.amazon.com/blogs/database/new-amazon-dynamodb-lowers-pricing-for-on-demand-throughput-and-global-tables). Before the cut, on-demand write pricing was $2.50 per million WRU. After the cut, it dropped to $1.25 per million WRU. Read pricing dropped from $0.50 to $0.25 per million RRU.
This halved the cost gap between on-demand and provisioned. Before November 2024, on-demand was roughly 10-12x more expensive per request than well-utilized provisioned capacity. After the cut, it is 5-6x more expensive. The practical impact: workloads with 20-35% utilization that previously justified provisioned mode are now cheaper on on-demand. AWS itself now recommends on-demand as the default starting point for most workloads.
How Does DynamoDB Auto Scaling Affect Provisioned Capacity Cost?
DynamoDB auto scaling adjusts provisioned WCU and RCU based on actual consumption using target tracking policies. You set a target utilization rate (default: 70%), and auto scaling provisions enough capacity to keep utilization at or below that target.
The cost impact of DynamoDB auto scaling: you always pay for more capacity than you consume, because the auto scaler maintains a buffer above actual traffic. At a 70% target, you provision approximately 43% more capacity than your average consumption (1/0.7 = 1.43x). Scale-up delay is typically 1-2 minutes. Scale-down delay is 15 minutes by default, and DynamoDB limits scale-down actions to 4 per hour per table/GSI. This asymmetry means your provisioned capacity stays elevated longer than necessary after traffic drops.
Net effect: auto scaling with a 70% target turns theoretical provisioned pricing (at 100% utilization) into practical provisioned pricing at approximately 60-70% utilization. The cost per request is still 3-4x cheaper than on-demand, but the gap is narrower than theoretical calculations suggest.
How Do Database Savings Plans Change the DynamoDB On-Demand vs Provisioned Decision?
AWS launched Database Savings Plans in December 2025, offering a commitment-based discount that works across both DynamoDB capacity modes and nine other AWS database services (verify at aws.amazon.com/savingsplans/database-pricing — rates change).
Database Savings Plans provide 12-18% discount on DynamoDB usage for a 1-year commitment at a $/hour spend level, with no upfront payment required. The discount applies automatically to both on-demand and provisioned throughput, across any region and table class. This is the first commitment discount that covers DynamoDB on-demand mode.
For the DynamoDB provisioned vs on-demand pricing decision, Database Savings Plans add a middle option: on-demand with a 12-18% Savings Plan discount. For workloads that are too variable for provisioned mode but large enough to justify a commitment, this combination delivers better economics than raw on-demand pricing without the operational complexity of capacity planning.
However, for steady provisioned workloads, reserved capacity (53-73% discount) still delivers far deeper savings than Database Savings Plans (12-18%). The two are complementary: use reserved capacity for your predictable baseline, and Database Savings Plans for variable or on-demand overflow.
How Should You Measure Utilization to Choose Between DynamoDB On-Demand and Provisioned?
The DynamoDB on-demand vs provisioned decision depends on your actual utilization rate, not your peak traffic. Here is how to measure it.
Step 1: Enable CloudWatch Metrics
DynamoDB automatically publishes ConsumedReadCapacityUnits, ConsumedWriteCapacityUnits, ProvisionedReadCapacityUnits, and ProvisionedWriteCapacityUnits to CloudWatch. For on-demand tables, only the Consumed metrics are available.
Step 2: Calculate Average Utilization Over 30 Days
Utilization = Average(ConsumedWriteCapacityUnits) / Average(ProvisionedWriteCapacityUnits) over 30 days. Repeat for reads. If both read and write utilization stay above 40% consistently, provisioned mode is likely cheaper. If either drops below 30% regularly, on-demand may be the better choice.
Step 3: Evaluate Peak-to-Average Ratio
If your peak throughput exceeds 5x your average, on-demand handles the spikes without throttling risk. If your peak-to-average ratio is under 3x, auto scaling can handle the variation with provisioned mode at lower cost.
Step 4: Check Cost Explorer for the Actual Bill
AWS Cost Explorer shows your DynamoDB spend by usage type. Filter by service and group by usage type to see WCU-hours, RCU-hours, and on-demand request charges separately. Compare the actual on-demand bill against what provisioned would cost at your observed utilization rate. 
Also Read: AWS Savings Plan Buying Strategy: Layering, Timing & Right-Sizing Commitment
How Does Reserved Capacity Stack on Top of Provisioned Mode?
Once you commit to provisioned mode, reserved capacity is the next cost lever. DynamoDB reserved capacity is purchased in blocks of 100 WCU or 100 RCU for a 1-year or 3-year term with an upfront payment (verify at aws.amazon.com/dynamodb/pricing/provisioned — rates change).
Reserved capacity pricing for DynamoDB provisioned capacity (US East — N. Virginia):
Reserved capacity cannot be purchased for on-demand tables, DynamoDB Standard-IA table class, or Global Tables replicated write capacity (rWCU). It applies only to standard single-region provisioned WCU and RCU.
The purchasing decision requires accurately forecasting your baseline capacity for the full commitment term. Over-purchasing means paying for unused capacity. Under-purchasing means the excess runs at the standard provisioned rate. AWS Cost Explorer generates recommendations, but these refresh every 72+ hours and use a backward-looking window that may not reflect current workload patterns.
Usage.ai automates this exact purchasing decision through its Flex Reserved Instances product for DynamoDB. The platform continuously monitors your provisioned capacity consumption across all tables and regions, then purchases reserved capacity blocks where utilization justifies the commitment.
Usage.ai refreshes its analysis every 24 hours, catching workload changes 3 days faster than AWS Cost Explorer. If a reservation becomes underutilized because traffic shifted, Usage.ai provides cashback and credits on the unused portion. The fee is a percentage of realized savings only: zero savings means zero cost.
Book a DynamoDB savings assessment at usage.ai to see how Reserved Capacity compares to DAX for your specific workload.
Choose On-Demand When… Choose Provisioned When…
Choose DynamoDB On-Demand When:
Your traffic is unpredictable or you are launching a new application without baseline data. Your peak-to-average throughput ratio exceeds 5:1. Your table handles under 10 million requests per month. Your workload is development, staging, or testing with sporadic traffic. You want zero capacity planning overhead and accept the 5-6x per-request premium. You need to handle flash-sale or event-driven spikes without throttling risk.
Choose DynamoDB Provisioned When:
Your traffic is steady and predictable with a peak-to-average ratio under 3:1. Your average capacity utilization stays above 40% consistently. Your table handles over 50 million requests per month and cost is a priority. You are willing to manage auto scaling policies (or use Usage.ai to automate them). You want to stack reserved capacity (53-73% savings) on top of provisioned pricing for maximum cost reduction.
Choose DynamoDB Provisioned + Reserved Capacity When:
Your baseline capacity has been stable for 30+ days. Your utilization rate stays above 70% consistently. You can forecast capacity needs for a 1-year or 3-year term. You want the absolute lowest per-request cost, which at 3-year reserved is approximately 96% cheaper than on-demand ($0.013/M writes vs $1.25/M writes).
Frequently Asked Questions
1. What is the difference between provisioned capacity and on-demand in DynamoDB?
Provisioned capacity requires you to specify read and write units per second and bills hourly for that capacity regardless of usage. On-demand charges per request with no capacity planning. Provisioned is cheaper at consistent utilization above 40%, while on-demand is better for unpredictable or low-traffic workloads. You can switch between modes once per 24-hour period per table.
2. Is DynamoDB provisioned throughput cheaper than on-demand?
Yes, at sufficient utilization. Provisioned throughput at 100% utilization costs approximately $0.047 per million writes, compared to on-demand at $1.25 per million writes, a 26x difference. At a realistic 70% utilization with auto scaling, provisioned is still 3-4x cheaper. The break-even point is approximately 35-40% utilization (verify at aws.amazon.com/dynamodb/pricing — rates change).
3. How much does DynamoDB on-demand cost?
DynamoDB on-demand costs $1.25 per million write request units (WRU) and $0.25 per million read request units (RRU) in US East (N. Virginia) after the November 2024 50% price reduction. These rates apply to the Standard table class. Standard-IA table class has higher request rates but lower storage costs (verify at aws.amazon.com/dynamodb/pricing — rates change).
4. Does DynamoDB on-demand have a free tier?
The DynamoDB free tier (25 GB storage, 25 WCU, 25 RCU) applies to provisioned mode only. On-demand tables receive the 25 GB storage free tier but do not get free request units. Every read and write on an on-demand table is billed from the first request.
5. Can you switch between DynamoDB on-demand and provisioned modes?
Yes. You can switch a table between on-demand and provisioned modes once every 24 hours. The switch takes effect immediately. When switching from on-demand to provisioned, you must specify initial WCU and RCU values. When switching from provisioned to on-demand, existing provisioned capacity is removed and billing switches to per-request.
6. How does DynamoDB auto scaling affect provisioned cost?
DynamoDB auto scaling maintains a target utilization rate (default 70%) by adjusting provisioned capacity. This means you always provision more than you consume. Scale-up takes 1-2 minutes, and scale-down is limited to 4 actions per hour per table/GSI. The net effect is provisioned costs at approximately 60-70% effective utilization, still 3-4x cheaper than on-demand.
7. What are Database Savings Plans for DynamoDB?
Database Savings Plans (launched December 2025) offer 12-18% discount on DynamoDB usage for a 1-year $/hour commitment. They apply to both on-demand and provisioned modes, across all regions and table classes. This is the only commitment discount available for on-demand DynamoDB usage (verify at aws.amazon.com/savingsplans/database-pricing — rates change).
8. What is the cheapest way to run DynamoDB at scale?
Provisioned mode with 3-year reserved capacity delivers the lowest per-request cost: approximately $0.013 per million writes, which is 96% cheaper than on-demand. For workloads above 100 million requests per month with stable traffic, provisioned plus reserved capacity saves thousands of dollars per year compared to on-demand.
Cut cloud cost with automation
Coverage that grows itself
Get paid for under utilization
Real time recommendations
Book Demo
Latest from our blogs 
View all posts
AWS, Reserved Instances
RDS MariaDB: Same Price as MySQL, Better Engine Features
Read More
AWS, Guides
Your AWS Bill Is 30% Waste. France Has a Fix.
Read More
AWS, RDS
RDS Free Tier: 750 Hours of db.t3.micro — What Is Actually Free
Read More 
Company
Product
About Us
Events
Resources
Case Studies
Blogs
Documentation
FAQ
Company
Privacy
Term
725 5th Ave, New York, NYC, 10022 Copyright 2026 Usage AI
