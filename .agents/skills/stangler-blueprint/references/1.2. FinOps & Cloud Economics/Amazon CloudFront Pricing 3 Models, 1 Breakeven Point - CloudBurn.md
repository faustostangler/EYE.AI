---
name: Amazon CloudFront Pricing: 3 Models, 1 Breakeven Point - CloudBurn
keywords: (placeholder)
metadata:
  url: https://cloudburn.io/blog/amazon-cloudfront-pricing
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Amazon CloudFront Pricing: 3 Models, 1 Breakeven Point | Cloud Burn
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
amazon-cloudfront aws-pricing cloudfront-pricing cost-optimization finops aws-cdn
Amazon CloudFront Pricing: 3 Models, 1 Breakeven Point
Complete guide to Amazon CloudFront pricing. Compare flat-rate vs pay-as-you-go plans, see real cost examples, and estimate costs with our free calculator.
April 1st, 2026
25 min read
385 views
0 likes
Amazon CloudFront pricing has three different models, regional rate variations, tiered volume discounts, and over a dozen additional cost components that can appear on your bill. Most guides just copy the rate tables from the AWS pricing page and call it a day.
That's not helpful when you're trying to figure out which pricing model saves you money.
In this guide, I'll break down exactly how Amazon CloudFront pricing works, calculate the breakeven point between flat-rate and pay-as-you-go (something no other guide covers), walk through real-world cost examples, and show you the hidden charges that catch teams off guard. All pricing data is sourced from the official CloudFront pay-as-you-go pricing page and verified as of February 2026.
If you want to jump straight to estimating your specific costs, try the CloudFront pricing calculator and come back for the details.
How CloudFront Pricing Works
Before diving into rate tables, you need to understand the pricing landscape. CloudFront gives you three distinct pricing paths, and picking the right one is the most impactful decision you'll make for your CDN costs.
Here are the key principles that apply across all models:
No minimum fees or fixed platform costs
No charge for data transfer from AWS origins (S3, EC2, ALB) to CloudFront
No premium for dynamic content delivery
Tiered volume discounts on pay-as-you-go (the more you use, the less per unit)
Regional pricing (rates vary by geographic edge location)
Always Free tier included for all AWS accounts, indefinitely
Three Pricing Models at a Glance
The flat-rate plans launched in November 2025 and represent the biggest pricing change in CloudFront's history. If you're reading older guides, they won't cover this option. Another recent change worth knowing: since October 2024, CloudFront no longer charges for requests blocked by AWS WAF, which can meaningfully reduce costs if you use WAF.
Main Cost Components
Here's every billable component at a glance. Most CloudFront bills are dominated by just two: data transfer out and HTTP/HTTPS requests.
Yes
No
Yes, want
simple billing
No, variable
traffic
Yes
No
CloudFront Pricing
Which model?
Need Lambda@Edge,
real-time logs, or
field-level encryption?
Traffic volume
predictable?
Can commit
for 1 year?
Pay-As-You-Go
(Usage-based billing)
Flat-Rate Plan
($0 / $15 / $200 / $1,000)
Pay-As-You-Go
Savings Bundle (30% off)
The biggest decision you'll make is choosing between flat-rate and pay-as-you-go pricing. Let me show you the math so you can figure out which one actually saves you money.
Flat-Rate vs. Pay-As-You-Go: Which Should You Choose?
This is the question every CloudFront user needs to answer, and surprisingly, no other pricing guide has done the breakeven analysis. I've calculated the costs at multiple traffic levels so you can see exactly where each model wins.
The key insight: flat-rate plans bundle CDN, WAF, DDoS protection, Route 53 DNS, logging, and edge compute into one price. So a fair comparison needs to account for those bundled services, not just raw CDN costs.
Breakeven Analysis by Traffic Level
Here's what you'd pay under each model for US/EU traffic served over HTTPS. Pay-as-you-go rates use the first paid tier ($0.085/GB for data transfer, $1.00/1M for HTTPS requests).
Wait, the Pro plan at $15/month beats pay-as-you-go at 2 TB? Yes, but there's a catch. The Pro plan includes 50 TB of data transfer and 10M requests. At 2 TB/month with 20M requests, you're well within the Pro plan's data transfer allowance but you exceed the 10M request limit. When you exceed allowances on flat-rate plans, AWS doesn't charge overages. Instead, they reduce performance by serving traffic from fewer or more distant edge locations.
Decision Framework
Choose flat-rate when:
You want predictable, fixed monthly billing
Bundled WAF, DDoS protection, and Route 53 DNS add value (these would cost extra on pay-as-you-go)
Your traffic stays within the plan's allowances most of the time
You don't need Lambda@Edge, real-time logs, or field-level encryption
Choose pay-as-you-go when:
Your traffic is highly variable or seasonal
You need Lambda@Edge, real-time logs, Dedicated IP SSL, or field-level encryption (not available on flat-rate)
You're within the free tier (1 TB + 10M requests covers many sites)
Your traffic volume is low enough that free tier covers it entirely
Consider the Savings Bundle when:
Pay-as-you-go is the right base model for your needs
You can commit to a consistent monthly spend for 1 year
You want 30% savings plus a 10% WAF credit on top
Use the CloudFront pricing calculator to compare pay-as-you-go vs. Savings Bundle costs for your specific traffic patterns.
Now that you know which pricing model fits your situation, let me walk you through the details of each one.
CloudFront Flat-Rate Pricing Plans
Launched in November 2025, flat-rate plans combine CDN, security, DNS, and edge compute into a single monthly price with no overage charges. This is a fundamentally different approach from traditional usage-based CDN billing.
The flat-rate pricing plan documentation covers the full details, but here's the practical comparison you need.
Plan Comparison (Free, Pro, Business, Premium)
The bundled S3 storage credits are a nice bonus. If CloudFront is serving content from S3, the Pro plan's 50 GB credit and the Business plan's 1 TB credit offset your origin storage costs. For a full breakdown of S3 storage class pricing and request costs, see the Amazon S3 pricing guide or use the S3 pricing calculator.
What Flat-Rate Plans Do NOT Support
This is critical to check before choosing a flat-rate plan. The following features require pay-as-you-go:
Lambda@Edge functions (only CloudFront Functions available)
Real-time access logs (standard logging is included)
Dedicated IP/SSL ($600/month feature on pay-as-you-go)
Field-level encryption
Multi-tenant distributions
Continuous deployment / staging distributions
Anycast IP list configuration
If your architecture depends on Lambda@Edge for server-side rendering, A/B testing, or origin routing with network access, flat-rate plans are off the table.
When Flat-Rate Plans Make Sense
The sweet spot for flat-rate plans is websites and applications that need CDN + security in a single package. If you'd otherwise pay separately for CloudFront, AWS WAF, Route 53, and Shield Advanced, the Business plan at $200/month is often cheaper than the sum of those individual services. The bundled security features align with AWS security best practices while simplifying your cost structure.
One important behavioral note: when traffic exceeds your plan allowances, AWS reduces performance (fewer/more distant edge locations, reduced throughput) rather than charging overages. DDoS traffic and WAF-blocked requests don't count against your allowances, so you're protected during attacks without worrying about cost spikes.
If flat-rate plans don't fit your needs, pay-as-you-go is your path. Here's exactly what you'll pay.
CloudFront Pay-As-You-Go Pricing
Pay-as-you-go is CloudFront's traditional model, and it's still the right choice for workloads that need advanced features or have traffic patterns that fit within the free tier. The two main cost drivers are data transfer out and HTTP/HTTPS requests, both of which vary by region.
Data Transfer Out Pricing by Region
Data transfer is typically the largest line item on a CloudFront bill. Rates vary by geographic region and decrease with volume. The first 1 TB per month is free across all regions.
A few things stand out:
US/Europe are the cheapest regions, starting at $0.085/GB and dropping to $0.020/GB at petabyte scale
Australia/NZ are the most expensive, starting at $0.114/GB
Volume discounts are significant: up to 76% reduction from the first paid tier to the highest tier in US/Europe
Custom pricing is available for commitments of 10 TB/month or higher (contact AWS sales)
Data transfer from any AWS origin to CloudFront is free. This is a major cost advantage when your origin is S3, EC2, or an Application Load Balancer. If your origin is an EC2 instance, understanding Amazon EC2 pricing alongside CloudFront costs gives you the complete picture.
HTTP/HTTPS Request Pricing
Every request CloudFront processes incurs a charge, with HTTPS costing more than HTTP due to TLS processing overhead. The first 10 million requests per month are free.
Key details:
HTTPS costs 25-38% more than HTTP depending on region
All HTTP methods (GET, POST, PUT, DELETE) are priced the same
WebSocket and gRPC incur no additional charge beyond standard data transfer and request fees
Price Classes: Limit Regions to Lower Costs
CloudFront Price Classes let you exclude expensive edge locations to reduce costs. If most of your traffic is from the US and Europe, there's no reason to pay for global edge coverage.
Here's an important nuance: if CloudFront occasionally serves content from an edge location outside your selected price class, you only pay the rate for the cheapest location in your selected class. So Price Class 100 caps your per-GB rate at US/Europe levels even if a request is served from Asia.
Data transfer and requests make up the bulk of your CloudFront bill. But if you use edge compute, there are additional costs to factor in.
Edge Compute Costs: CloudFront Functions vs. Lambda@Edge
CloudFront offers two options for running code at the edge. They have very different pricing, and choosing the wrong one can inflate your bill by 6x or more.
Let me show you both options side by side so you can make the right call.
CloudFront Functions Pricing
CloudFront Functions are lightweight, sub-millisecond JavaScript functions running at edge POPs. They're designed for simple request/response manipulations like URL rewrites, header manipulation, and cache key normalization.
$0.10 per 1 million invocations (flat rate, no duration charge)
2 million invocations/month free (Always Free tier)
The absence of a duration charge is the key pricing advantage. You pay the same $0.10/1M whether your function runs for 0.1ms or 0.9ms.
Lambda@Edge Pricing
Lambda@Edge is a full serverless compute platform at regional edge caches. It supports Node.js and Python, with up to 30 seconds of execution time and network access.
$0.60 per 1 million requests
$0.00005001 per GB-second of compute time
No free tier
When to Use Which
Here's a concrete cost comparison. For a media streaming workload with 60 million invocations at 10ms each with 128 MB memory:
Lambda@Edge:
Requests: 60M x $0.60/1M = $36.00
Compute: 60M x 0.01s x (128/1024) x $0.00005001 = $3.75
Total: $39.75/month
CloudFront Functions (if the logic fits within its constraints):
Invocations: (60M - 2M free) x $0.10/1M = $5.80
Total: $5.80/month
That's a 6.8x cost difference. My recommendation: use CloudFront Functions for everything you can (URL rewrites, header manipulation, redirects, cache key normalization), and reserve Lambda@Edge only for workloads that require network access, longer execution times, or the Python runtime.
Beyond the core pricing components, CloudFront has several additional features that appear on your bill if you enable them.
Additional Costs You Should Know
These are the charges that catch teams off guard. Most CloudFront guides mention one or two of these in passing. Here's the complete inventory with specific pricing so nothing surprises you.
Origin Shield
Origin Shield adds a centralized caching layer between regional edge caches and your origin. It reduces duplicate origin fetches, which can save money on origin compute, but it adds a per-request fee on top of standard CloudFront charges.
Cost estimation rule: AWS recommends estimating roughly 10% of your HTTPS requests will reach Origin Shield. For 200M HTTPS requests with 10% going to Origin Shield (20M requests) at US pricing: 20,000,000 / 10,000 x $0.0075 = $15/month.
Origin Shield is worth enabling when you have geographically distributed audiences, high cache-hit ratios, or use multiple CDNs pointing to the same origin.
Invalidation Requests
The 1,000 free paths are usually sufficient for most sites. If you find yourself exceeding this regularly, switch to versioned URLs (e.g., app.v2.js ) instead of invalidating cached files. Wildcard invalidations ( /images/* ) count as a single path, so use them to cover multiple files efficiently.
Dedicated IP Custom SSL
$600/month per certificate, pro-rated hourly. This is charged even when the distribution is disabled, as long as the certificate is associated.
Most users should use SNI Custom SSL, which is free. Dedicated IP SSL is only needed for supporting very old browsers that don't support Server Name Indication (SNI). Unless you have a specific legacy client requirement, avoid this cost entirely.
Real-Time Logs
$0.01 per 1 million log lines, plus Amazon Kinesis Data Streams charges for the delivery stream. Each CloudFront request generates one log line.
For 10 million requests/month, real-time logs add about $0.10/month, but the Kinesis Data Streams charges for the underlying stream can cost significantly more. Standard access logs are available at no additional charge for log delivery and are sufficient for most use cases.
Field-Level Encryption
$0.02 per 10,000 requests, in addition to standard HTTPS request fees. This encrypts specific data fields (like credit card numbers) at the CloudFront edge before forwarding to your origin.
For 1 million requests: 1,000,000 / 10,000 x $0.02 = $2.00/month. Only relevant for compliance scenarios (GDPR, HIPAA, PCI-DSS).
Other Charges (Anycast IPs, SaaS Manager)
Two enterprise-level charges to be aware of:
Anycast Static IPs: $3,000/month per list. This is an enterprise feature for dedicated IP addresses at CloudFront edge locations.
SaaS Manager (Distribution Tenants): First 10 tenants free, 11-200 at $20/month subscription, over 200 at $0.10/tenant/month. Used for managing content delivery across multiple customer websites.
If you're on pay-as-you-go pricing and want to lock in a discount, the Security Savings Bundle offers up to 30% off.
CloudFront Security Savings Bundle
The Security Savings Bundle is CloudFront's commitment-based discount for pay-as-you-go customers. It's conceptually similar to AWS Savings Plans but specific to CloudFront (and includes a WAF bonus).
How the 30% Discount Works
You commit to a fixed monthly CloudFront spend for 1 year. In return, that commitment covers 30% more CloudFront usage than its face value, and you get a 10% WAF credit as a bonus.
The bundle covers all pay-as-you-go usage types: data transfer, requests, edge compute, Origin Shield, real-time logs, invalidations, Dedicated IP SSL, and everything else.
Important restrictions:
Does not apply to flat-rate pricing plans
Cannot combine with custom pricing agreements
Purchase through the CloudFront console only (not via API)
Right-Sizing Your Commitment
I recommend covering 70-80% of your lowest observed monthly spend over the past year. This creates a buffer against unexpected traffic dips while still capturing significant savings. Any usage above your committed amount bills at standard on-demand rates.
The bundle is stackable (buy multiple bundles as usage grows) and supports AWS Organizations with credit sharing enabled. You can also enable auto-renewal to avoid gaps in coverage. For organizations running CloudFront across multiple accounts, consider reviewing your AWS cloud foundation guide to ensure credit sharing is properly configured.
Before committing to any paid plan, check whether the CloudFront free tier covers your needs.
CloudFront Free Tier
CloudFront's free tier is Always Free, meaning it doesn't expire after 12 months like many other AWS free tiers. This makes it particularly generous for personal projects and small sites.
Always Free Tier Allowances
The free tier applies per AWS account (not per distribution). If you use consolidated billing, it's shared across the organization.
Free Tier vs. Flat-Rate Free Plan
This comparison trips people up because there are technically two "free" options. Here's how they differ:
The pay-as-you-go free tier is more generous for pure CDN usage (10x more data transfer, 10x more requests). But the flat-rate free plan bundles WAF, DDoS protection, and DNS at no cost, which is valuable if you'd otherwise pay for those services separately.
For a personal blog or portfolio site with moderate traffic, the pay-as-you-go free tier likely covers your entire CloudFront bill.
Now let me show you what CloudFront actually costs for real workloads.
Real-World CloudFront Cost Examples
Abstract rate tables only tell part of the story. Here are five realistic scenarios with component-level cost breakdowns, calculated using US/Europe pay-as-you-go rates. All calculations assume HTTPS traffic.
Personal Blog / Portfolio Site
Traffic: 10 GB data transfer, 500K HTTPS requests, US-only
Both the pay-as-you-go free tier and the flat-rate free plan cover this entirely. The flat-rate free plan adds WAF and DDoS protection at no extra cost.
Business Website
Traffic: 500 GB data transfer, 5M HTTPS requests, US/EU
Still within the free tier. Many business websites are surprised to learn their CloudFront costs are effectively zero.
SaaS Application
Traffic: 2 TB data transfer, 30M HTTPS requests, US/EU
This is where the flat-rate Pro plan starts to shine. At $15/month vs. $105/month for CDN alone, the Pro plan is dramatically cheaper, and it includes WAF, DDoS protection, and Route 53 DNS. The trade-off: if your SaaS needs Lambda@Edge, you can't use flat-rate.
E-Commerce Platform
Traffic: 10 TB data transfer, 100M HTTPS requests, global, with Origin Shield
The Business flat-rate plan at $200/month covers 50 TB data transfer and 125M requests, which is well above this workload. It also includes Advanced WAF (50 rules), DDoS protection, VPC Origins, and a 1 TB S3 storage credit. For an e-commerce site that doesn't need Lambda@Edge, the Business plan is a clear winner.
Media Streaming Service
Traffic: 50 TB data transfer, 500M HTTPS requests, Lambda@Edge (60M invocations at 10ms/128MB), Origin Shield
Flat-rate plans are not an option here because Lambda@Edge is required. The Savings Bundle is the best discount path, saving roughly $1,360/month. At this scale, contacting AWS for custom pricing (available at 10+ TB/month) could yield even better rates.
Whatever pricing model you choose, these optimization strategies can further reduce your CloudFront costs.
How to Reduce Your CloudFront Costs
These six strategies apply regardless of whether you're on flat-rate or pay-as-you-go. In my experience, implementing the first three alone can cut costs by 30-50% for most workloads.
Optimize Your Cache Hit Ratio
This is the single most impactful optimization. Every cache hit avoids an origin fetch and serves content from the edge, reducing both data transfer and origin compute costs.
Minimize your cache key: only include the query strings, headers, and cookies that actually affect your response. Every unnecessary cache key value creates duplicate cache entries.
Set long TTLs for static assets: use Cache-Control: public, max-age=31536000, immutable with versioned file names
Use managed cache policies: CloudFront provides predefined policies for common use cases that follow best practices
Versioned file names: use hashed URLs (e.g., app.a1b2c3.js ) so you never need to invalidate
Enable Compression
Automatic Gzip and Brotli compression reduces data transfer volumes by 60-80% for text-based content. That's a direct reduction in your data transfer costs.
Brotli achieves 15-25% better compression than Gzip for most text content
Use modern image formats ( WebP/AVIF) instead of PNG/JPEG for further savings
If CloudFront doesn't natively compress certain file types, pre-compress at the origin and set the Content-Encoding header
Use the Right Price Class
If most of your traffic comes from the US and Europe, switch from Price Class All (the default) to Price Class 100. This caps your per-GB rates at US/Europe levels without restricting viewer access. Users in Asia can still access your content, they'll just be served from a US/EU edge location.
Put CloudFront in Front of Your ALB
Data transfer from AWS origins to CloudFront is free. If you're currently serving traffic directly from an Application Load Balancer, placing CloudFront in front saves roughly $0.085/GB on data transfer out. For a typical 1 TB workload, that's about $77/month in savings, according to the AWS blog on CloudFront cost optimization. This strategy also applies to EC2 instances and other AWS origins, as noted in the Well-Architected data transfer cost optimization guidance.
This is also relevant if you're managing NAT Gateway costs. CloudFront can offload significant data transfer that would otherwise flow through your NAT Gateway.
Block Bot Traffic with AWS WAF
Since October 2024, CloudFront no longer charges for requests blocked by AWS WAF. This means blocking bot traffic, scrapers, and malicious requests with WAF rate-based rules directly reduces your CloudFront request costs at zero additional CloudFront cost (standard WAF charges still apply).
Geo-restrictions can also limit delivery to the countries where you have actual users, preventing unnecessary edge location costs.
Use Versioned URLs Instead of Invalidations
The first 1,000 invalidation paths per month are free, but relying on invalidations creates both cost and cache performance issues. Versioned file names (e.g., app.v2.js or content-hashed URLs) provide immediate cache busting without any invalidation cost, and they improve cache hit ratios since old URLs remain cacheable.
If you're deploying CloudFront distributions via Infrastructure as Code, you can estimate AWS CDK costs before deploying to catch expensive configuration changes in code review. For teams managing CloudFront distributions programmatically, following AWS CDK best practices ensures your infrastructure definitions stay maintainable.
Before committing to CloudFront, you might be wondering how it compares to alternatives like Cloudflare.
CloudFront vs. Cloudflare Pricing
"Is CloudFront cheaper than Cloudflare?" is one of the most common questions I see, and the answer depends entirely on your use case.
Pricing Model Comparison
Cost Comparison at Different Traffic Levels
At 100 GB/month (North America):
At 10 TB/month (North America):
When CloudFront Wins vs. When Cloudflare Wins
Choose CloudFront when:
You're already in the AWS ecosystem (free data transfer from S3, EC2, ALB is a major cost advantage)
You need deep AWS integration (native support for S3, ALB, API Gateway, Lambda)
You want edge compute with Lambda@Edge (full server-side logic at the edge)
You prefer the new flat-rate plans with bundled AWS security services
Choose Cloudflare when:
You need truly unlimited bandwidth at a flat rate
Simpler pricing is a priority (no per-GB regional calculations)
Budget constraints favor predictable flat-rate over usage-based billing
AWS ecosystem integration isn't a requirement
Both are strong CDN options. CloudFront's advantage is its AWS integration and the cost savings from free origin data transfer. Cloudflare's advantage is its simpler, unlimited-bandwidth pricing model. For small AWS workloads that don't need CloudFront's full feature set, Amazon Lightsail pricing bundles CDN distribution with flat-rate instance plans, which can be a more cost-effective starting point.
Ready to calculate your specific CloudFront costs? Here's how to get an accurate estimate.
Estimate Your CloudFront Costs
The best way to estimate your CloudFront costs is to use actual traffic numbers. Here are the tools available:
CloudBurn CloudFront Pricing Calculator: I built this to compare pay-as-you-go vs. Savings Bundle costs with regional cost breakdowns. Input your data transfer volume and request counts to get an instant monthly estimate.
AWS Pricing Calculator: The official AWS tool for detailed estimates. You can configure data transfer, requests, edge compute, Origin Shield, and other features. No AWS account required.
For existing CloudFront customers:
AWS Cost Explorer: filter by "Amazon CloudFront" to analyze historical spending and usage trends
AWS Budgets: set CloudFront-specific thresholds and receive alerts when costs approach your limits
CloudFront console: provides Savings Bundle recommendations based on your historical usage, and for flat-rate plans, shows usage percentage against monthly allowances with email notifications at 50%, 80%, and 100%
Key Takeaways
Amazon CloudFront pricing comes down to three decisions: which pricing model, which features, and which optimizations.
Three pricing models: pay-as-you-go (flexible, usage-based), flat-rate plans (predictable, bundled security), and Security Savings Bundle (30% off pay-as-you-go with 1-year commitment)
For most workloads, the flat-rate Pro plan at $15/month or Business at $200/month is simpler and often cheaper than pay-as-you-go once you factor in bundled WAF, DDoS, and DNS
The Always Free tier covers many small to medium websites entirely (1 TB data transfer + 10M requests per month)
Enable compression, optimize caching, and choose the right price class. These three changes alone can reduce costs by 30-50%
Use the CloudFront pricing calculator to estimate your specific monthly cost, then compare flat-rate vs. pay-as-you-go
Which CloudFront pricing model are you using, and have you evaluated the flat-rate plans since they launched? Share your experience in the comments below.
CloudBurn
See Infrastructure Costs in Code Review, Not on Your AWS Bill
CloudBurn is an open-source policy engine that scans your Terraform and CloudFormation for costly CDN patterns in CI. Same rules also run against your live AWS account to find what's already wasting money.
Get CloudBurn on GitHub
Frequently Asked Questions
Is Amazon CloudFront free?
CloudFront has an Always Free tier that includes 1 TB of data transfer out and 10 million HTTP/HTTPS requests per month, with no expiration. There's also a flat-rate free plan that includes 100 GB of data transfer, 1 million requests, and bundled WAF/DDoS/DNS. Many personal and small business websites run entirely within the free tier.
How much does CloudFront cost per month?
CloudFront costs depend on your pricing model and traffic. Pay-as-you-go starts at $0.085/GB for data transfer and $1.00 per million HTTPS requests in US/Europe. Flat-rate plans range from $0 (free) to $1,000/month. A typical business website serving 500 GB/month costs $0 (within the free tier), while a SaaS application serving 10 TB/month costs roughly $200/month on the Business flat-rate plan.
What is included in CloudFront flat-rate pricing?
CloudFront flat-rate plans bundle CDN, AWS WAF, DDoS protection, Route 53 DNS, serverless edge compute (CloudFront Functions), logging, and S3 storage credits into a single monthly price. Plans range from Free ($0) to Premium ($1,000). There are no overage charges. If usage exceeds your plan allowance, AWS reduces performance rather than billing extra.
How do CloudFront price classes affect my costs?
Price classes let you exclude expensive edge locations. Price Class 100 (US/Canada/Europe only) is the cheapest, Price Class 200 adds Asia, and Price Class All includes global coverage. Using Price Class 100 instead of All can reduce per-GB costs since you only pay US/Europe rates. Users outside your price class can still access content but may be served from more distant edge locations.
Does CloudFront charge for traffic between AWS services?
No. Data transfer from any AWS origin (S3, EC2, ALB, API Gateway) to CloudFront is free. This is one of CloudFront's biggest cost advantages. Placing CloudFront in front of an ALB can save roughly $0.085/GB compared to serving directly from the ALB, which adds up to about $77/month savings for a 1 TB workload.
What is the CloudFront Security Savings Bundle?
The Security Savings Bundle provides a 30% discount on all CloudFront pay-as-you-go usage in exchange for a 1-year monthly spend commitment. A $100/month commitment covers $142.86 in CloudFront usage, plus 10% of your commitment ($10) is applied to AWS WAF charges. It covers all usage types including data transfer, requests, edge compute, and Origin Shield.
Is CloudFront cheaper than Cloudflare?
It depends on your use case. At 10 TB/month, CloudFront's Business flat-rate plan costs $200 versus Cloudflare Business at $250. However, Cloudflare offers unlimited bandwidth at flat-rate pricing, which can be cheaper for very high-traffic sites. CloudFront's advantage is free data transfer from AWS origins (S3, EC2, ALB), making it more cost-effective if you're already in the AWS ecosystem.
How can I reduce my CloudFront costs?
The three most impactful optimizations are: enable Gzip/Brotli compression (reduces data transfer by 60-80%), optimize cache hit ratios by minimizing cache keys and setting long TTLs, and use Price Class 100 if your traffic is primarily US/Europe. Additionally, block bot traffic with AWS WAF (blocked requests are free since October 2024) and use versioned URLs instead of invalidations.
Share this article on ↓
Share this article on →
 [](https://www.reddit.com/submit?url=https%3A%2F%2Fcloudburn.io%2Fblog%2Famazon-cloudfront-pricing&title=Amazon CloudFront Pricing: 3 Models, 1 Breakeven Point) [](https://api.whatsapp.com/send?text=Amazon CloudFront Pricing: 3 Models, 1 Breakeven Point%0A%0Ahttps%3A%2F%2Fcloudburn.io%2Fblog%2Famazon-cloudfront-pricing) 
0 comments
Write Preview 
Sign in with GitHub
Related reading
[
Amazon RDS Pricing: MySQL 5.7 Users Just Got a $292/Month Fee
Mar 9, 2026 29 min amazon-rds / aws-pricing 231 0](https://cloudburn.io/blog/amazon-rds-pricing)
[
AWS KMS Pricing: Complete Breakdown + Real-World Cost Examples
Mar 8, 2026 22 min aws-kms / aws-pricing 88 0](https://cloudburn.io/blog/aws-kms-pricing)
[
Amazon Lightsail Pricing: 2026 Guide to True Total Cost
Feb 15, 2026 28 min amazon-lightsail / lightsail-pricing 270 0](https://cloudburn.io/blog/amazon-lightsail-pricing)
[
Amazon Bedrock Pricing: Token Rates Hide a $350/Month Trap
Feb 8, 2026 24 min amazon-bedrock / aws-pricing 1,357 0](https://cloudburn.io/blog/amazon-bedrock-pricing)
[
AWS Backup Pricing: Full Breakdown + Cost Calculator
Jan 24, 2026 20 min aws-backup / aws-pricing 206 0](https://cloudburn.io/blog/aws-backup-pricing)
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
