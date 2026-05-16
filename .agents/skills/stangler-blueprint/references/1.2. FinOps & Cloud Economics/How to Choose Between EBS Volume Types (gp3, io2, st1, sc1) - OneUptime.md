---
name: How to Choose Between EBS Volume Types (gp3, io2, st1, sc1) - OneUptime
keywords: (placeholder)
metadata:
  url: https://oneuptime.com/blog/post/2026-02-12-choose-between-ebs-volume-types/view
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
How to Choose Between EBS Volume Types (gp3, io2, st1, sc1)
Skip to main content
OneUptime
Open menu
Products
Essentials
Monitoring Uptime & synthetic checks
Status Page Communicate incidents to users
Incidents Detect, manage & resolve
On-Call & Alerts Smart routing & escalations
Scheduled Maintenance Plan & communicate downtime
Observability
Logs Fastest log ingest & search
Metrics Application & infra metrics
Traces Distributed request tracing
Exceptions Error tracking & debugging
Profiles CPU & memory profiling
Infrastructure
Kubernetes Cluster & pod observability
Docker Host & container observability
Hosts Auto-discovered server metrics
Automation & Analytics
Workflows No-code automation builder
Dashboards Custom data visualizations
AI Agent Auto-fix issues with AI-powered PRs. Let AI analyze incidents and automatically create pull requests to resolve them.
Resources
Documentation API Reference GitHub Blog & Guides
Get Started
Start Free Trial Request Demo
sales@oneuptime.com
Open Source — Self-host or use our cloud. Your data, your choice.
View Pricing Enterprise
Enterprise
Enterprise
Built for how you work
Scale your reliability operations with enterprise-grade tools.
Enterprise Overview Scale with confidence
Request Demo See it in action
Contact Sales
Enterprise
Enterprise Overview Solutions for large organizations
Request Demo Schedule a personalized demo
Teams
DevOps
SRE
Platform
Developers
Industries
FinTech
SaaS
Healthcare
E-Commerce
Media
Government
Documentation Pricing Blog
Get Started Free
Pricing
Resources
Resources
Learn & Connect
Everything you need to get started and succeed.
Documentation Guides & tutorials
API Reference REST API & SDKs
Star on GitHub
Learn
Blog News & insights
Status System status
Changelog What's new
Videos Watch & learn
Support
Help Center
Contact Us
Company
About Us
Merch Store
Legal Privacy Terms
100% Open Source
Sign in Sign up 
Close menu
Status Page
Incidents
Monitoring
On-Call
Maintenance
Logs
Metrics
Traces
Exceptions
Kubernetes
Docker
Hosts
Profiles
Workflows
Dashboards
AI Agent
Enterprise
DevOps
SRE
Platform
Pricing Docs Request Demo Support
Sign up
Existing customer? Sign in 
How to Choose Between EBS Volume Types (gp3, io2, st1, sc1)
A practical comparison of EBS volume types including gp3, gp2, io2, io1, st1, and sc1, with guidance on matching each type to the right workload.
 @nawazdhandala
• Feb 12, 2026
• Reading time 6 min read
AWS EC2 EBS Storage Performance Cost Optimization
On this page
The Quick Answer Volume Types at a Glance gp3: The Default Choice gp2: The Legacy General Purpose io2: For Databases and Latency-Critical Workloads st1: Throughput-Optimized HDD sc1: Cold HDD Decision Flowchart Comparing Costs for Common Scenarios Monitoring and Optimization Key Takeaways   
AWS offers six EBS volume types, and picking the right one makes a real difference in both performance and cost. The wrong choice can mean paying 10x more than you need to, or getting 10x less performance than you expected. Each type is designed for specific access patterns, and understanding those patterns is the key to choosing well.
The Quick Answer
If you're in a hurry:
Most workloads: gp3. It's the best general purpose option.
Databases needing guaranteed IOPS: io2 or io2 Block Express.
Big data, streaming, logs: st1.
Archival, infrequent access: sc1.
Now let's dig into why.
Volume Types at a Glance
gp3: The Default Choice
gp3 is the newest general purpose SSD type and should be your go-to for most workloads. Here's why:
Baseline performance without gimmicks. Every gp3 volume gets 3,000 IOPS and 125 MB/s throughput included in the price, regardless of size. A 1 GB volume and a 1 TB volume both get the same baseline.
Independent scaling of IOPS and throughput. Need more IOPS? Add them. Need more throughput? Add that. You pay for exactly what you configure.
20% cheaper than gp2. Same (or better) performance at a lower price per GB. There's almost no reason to use gp2 anymore.
gp3 pricing example (200 GB, 6,000 IOPS, 400 MB/s):
Storage: 200 GB x $0.08 = $16.00/month
Additional IOPS: (6,000 - 3,000) x $0.005 = $15.00/month
Additional throughput: (400 - 125) x $0.04 = $11.00/month
Total: $42.00/month
gp2: The Legacy General Purpose
gp2 ties performance to volume size: you get 3 IOPS per GB, with a minimum of 100 IOPS and a burst capability up to 3,000 IOPS for volumes under 1 TB.
The burst model is the problem. Small gp2 volumes (under 1 TB) rely on burst credits for decent IOPS. When credits run out, you're stuck at the baseline (e.g., 300 IOPS for a 100 GB volume). This creates unpredictable performance.
gp3 Performance
Baseline: 3,000 IOPS
Always
Predictable
Any Size
gp2 Performance
Baseline: 300 IOPS
Burst: 3,000 IOPS
Baseline: 1,500 IOPS
Burst: 3,000 IOPS
Baseline: 3,000+ IOPS
No burst needed
Unpredictable
100 GB
500 GB
Better
1 TB+
Predictable
Migration tip: Switch all your gp2 volumes to gp3 online with no downtime. See our guide on resizing EBS volumes without downtime.
io2: For Databases and Latency-Critical Workloads
io2 volumes provide provisioned IOPS with guaranteed performance. You specify exactly how many IOPS you want, and you get them consistently.
When to use io2:
Production databases (PostgreSQL, MySQL, Oracle, SQL Server)
Applications requiring sub-millisecond latency
Workloads needing more than 16,000 IOPS per volume
Multi-Attach scenarios (attaching one volume to multiple instances)
io2 vs gp3 for databases:
The real question is whether you need guaranteed IOPS or whether gp3's 16,000 IOPS ceiling is enough. For many databases, gp3 at 16,000 IOPS is plenty and costs much less:
gp3 at 16,000 IOPS, 200 GB: $16 + (13,000 x $0.005) = $81/month
io2 at 16,000 IOPS, 200 GB: $25 + (16,000 x $0.065) = $1,065/month
io2 costs roughly 13x more for the same IOPS. The premium buys you:
99.999% durability (vs 99.8-99.9% for gp3)
Multi-Attach capability
More consistent latency
Up to 64,000 IOPS per volume
io2 Block Express
For instances that support it (R5b, X2idn, etc.), io2 Block Express pushes the limits further: up to 256,000 IOPS and 4,000 MB/s throughput per volume. This is for the most demanding database workloads.
st1: Throughput-Optimized HDD
st1 is an HDD type designed for sequential access patterns. It's much cheaper than SSD but has a completely different performance profile.
When to use st1:
Big data and data warehouse workloads (EMR, Hadoop)
Log processing
Streaming data (Kafka, Kinesis)
Any workload that reads/writes large amounts of data sequentially
When NOT to use st1:
Random I/O workloads (databases, boot volumes)
Anything needing low latency (HDD latency is much higher than SSD)
Boot volumes (st1 can't be used as root volumes)
st1 throughput scales with size: 40 MB/s per TB, up to 500 MB/s. A 2 TB volume gives you 80 MB/s baseline with burst to 250 MB/s.
Cost comparison for 2 TB:
gp3: 2,000 x $0.08 = $160/month
st1: 2,000 x $0.045 = $90/month
For sequential workloads, st1 saves 44% and might actually deliver better throughput for your use case.
sc1: Cold HDD
sc1 is the cheapest EBS volume type, designed for data you rarely access.
When to use sc1:
Archival data that needs to stay on block storage
Infrequently accessed file shares
Backup storage where cost matters more than speed
sc1 offers just 12 MB/s per TB baseline throughput. For 5 TB, that's 60 MB/s. If you need even cheaper storage and don't require block-level access, consider S3 instead.
Decision Flowchart
Yes
Frequent
Infrequent
Yes, 16K+ IOPS
No, 16K or less
Not sure
What's your access pattern?
Random I/O?
Sequential I/O?
Need guaranteed IOPS?
st1
sc1
io2
gp3
Comparing Costs for Common Scenarios
Web Server (100 GB, moderate I/O)
Winner: gp3, by a large margin.
Production Database (500 GB, 10,000 IOPS)
Winner: gp3 unless you need io2's guarantees.
Data Processing (5 TB, sequential)
Winner: st1 for sequential workloads.
Monitoring and Optimization
After selecting a volume type, monitor its performance to verify your choice:
Use OneUptime to build dashboards that track I/O performance across your entire fleet and alert when volumes are undersized or burst credits are depleting.
Key Takeaways
Start with gp3. It's the right answer for 80% of workloads.
Use io2 only when you need it. The cost premium is substantial, so make sure you're getting value from it.
Don't forget HDD types. For sequential workloads, st1 costs less and can outperform SSD in throughput.
Migrate from gp2 to gp3. It's a free performance upgrade with lower cost.
Match the volume to the workload, not the other way around. A 10 TB gp3 volume for archival data wastes money. A 100 GB sc1 volume for a database wastes time.
The right volume type saves money and improves performance. The wrong one does neither. Take the time to understand your workload's I/O patterns, and the choice becomes obvious.
Share this article    
Nawaz Dhandala
Author
@nawazdhandala • Feb 12, 2026 • 6 min read
Nawaz is building OneUptime with a passion for engineering reliable systems and improving observability.
GitHub
Improve this Blog Post
All our blog posts are open source. Found a typo, want to add more detail, or have a better explanation? Anyone can contribute and make this post better for everyone.
Edit this Post on GitHub Contributing Guidelines
Open source
OneUptime is the Open-Source Observability Platform
Your complete reliability stack unified: infrastructure monitoring, incident management, status pages, and APM. Open-source and self-hostable.
Get started for free Request a demo
Status Page Real-time status updates
Incidents Detect and resolve fast
Monitoring Monitor any resource
On-Call Smart alert routing
Maintenance Plan & communicate downtime
Logs Fastest log ingest and search
Metrics Performance insights
Traces End-to-end distributed tracing
Exceptions Catch and fix bugs early
Workflows Automate any process
Dashboards Visualize all your data
Kubernetes Monitor K8s clusters
Profiles CPU & memory profiling
AI Agent Automatically detect, diagnose, and resolve incidents with AI-powered root cause analysis and code fixes.
We use cookies to enhance your browsing experience and provide personalized content. By clicking "Accept," you consent to the use of cookies.
Our product uses both first-party and third-party cookies for session storage and for various other purposes.
Please note that disabling certain cookies may affect the functionality and performance of our product.
For more information about how we handle your data and cookies, please read our Privacy Policy.
By continuing to use our site without changing your cookie settings, you agree to our use of cookies as described above. See our terms and our privacy policy
Accept all Reject all
Footer
Open Source Observability
Build reliable systems with confidence
Join thousands of developers using OneUptime to monitor, debug, and optimize their infrastructure, stack, and apps.
Read Blog Star on GitHub
The complete open-source observability platform. Monitor, debug, and improve your entire stack in one place.
GitHub X YouTube Reddit LinkedIn
Trusted by thousands of teams worldwide - from Fortune 500 enterprises to fast-growing startups.
Products
Status Page
Incidents
Monitoring
On-Call
Logs
Metrics
Traces
Exceptions
Profiles
Kubernetes
Docker
Hosts
Workflows
Dashboards
AI Agent
Solutions
Enterprise
Request Demo
Pricing
Data Residency
Teams
DevOps
SRE
Platform
Developers
Tools
MCP Server
CLI
Resources
Documentation
API Reference
Blog
Help & Support
GitHub
Changelog
Open Source Friends
Industries
FinTech
SaaS
Healthcare
E-Commerce
Media
Government
Company
About Us
Careers
Merch Store
Contact
Legal
Trust Center
Terms of Service
Privacy Policy
SLA
Legal Center
Compare
vs PagerDuty
vs Statuspage
vs Incident.io
vs Pingdom
vs Datadog
vs New Relic
vs Better Stack
vs Uptime Robot
vs Checkly
vs SigNoz
© 2026 HackerBay, Inc. All rights reserved.
Open Source | Made with care for developers worldwide
SOC 2 HIPAA GDPR ISO 27001    
