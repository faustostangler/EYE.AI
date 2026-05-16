---
name: gp3 vs io2 Block Express: Performance Comparison - Datafy
keywords: (placeholder)
metadata:
  url: https://datafy.io/gp3-vs-io2-when-should-you-actually-pay-for-block-express/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
gp3 vs io2 Block Express: Performance Comparison
Product
EBS Auto-Scaler
Datafy Sensor
Solutions
EC2
Kubernetes
Self-Hosted Data
Resources
Resources
Blog
Events
Glossary
Deep Dives
Case Study: H2O.ai - Bottlerockets
Case Study: NoTraffic - ClickHouse
gp3 vs. io2: Comparison
LVM in the Modern Cloud
Kubernetes Storage Bottlenecks
Shrinking MongoDB storage
Company
Partners
About
Careers
Documentation
Home Old
Product
EBS Auto-Scaler
Datafy Sensor
Use Cases
EC2
Kubernetes
Self-Hosted Data
Resources
Glossary
Events
Blog
Case Study: H2O.ai - Bottlerockets
Case Study: NoTraffic - ClickHouse
gp3 vs. io2: Comparison
Is LVM on EBS Still Worth It?
Kubernetes Storage Bottlenecks
Shrinking MongoDB Storage
Company
About
Careers
Book a Demo
Log In
Book a Demo
gp3 vs. io2: When Should You Actually Pay for Block Express?
Amazon Elastic Block Store (EBS) has some impressive statistics. It's the essential storage that powers EC2 and many other AWS managed services and therefore AWS users run trillions of I/O operations every day. They store exabytes of data across millions of active volumes, yet the service delivers reliable performance across a variety of SSD- and HDD-based volume types.
AWS customers will choose a balance of value and performance by factoring what their applications will need and what they can justifiably afford. In terms of popularity, we see customers adopting two volume types, General Purpose SSD class gp3 and Provisioned IOPS SSD class io2 Block Express. They're the latest generation disk types in their respective categories, both having superseded gp2 and io1 with superior performance and value.
It's common knowledge that gp3 is the EC2 default volume type when provisioning new EC2 resources, and io2 Block Express is the highest performance and more expensive SSD volume type, but how do you truly decide when to select one over the other? Are you risking durability with one or driving up substantial costs with the other? It's worth reflecting.
September 2025: The performance gap narrows
As of September 26, 2025, gp3 volumes have seen a massive increase in performance limits, officially surpassing io1 in both IOPS and volume capacity. This substantially closes the gap to io2 Block Express. Today, gp3 matches io2 Block Express capacity as both now go up to 64TiB; gp3 reaches 80,000 IOPS which is sufficient for most use-cases and 2 GiB/s throughput. To compare, io2 Block Express goes all the way up to 256,000 IOPS per volume and a throughput of up to 4 GiB/s.
This gp3 update was a significant jump over the previous limits of 16TiB/16K IOPS/1GiB/s bandwidth, and has opened the door for most customers to take advantage of gp3 rather than pay the premium for io2 Block Express.
Why go for io2 Block Express in 2026 and beyond?
However, there are some other considerations and benefits for io2 Block Express.
First, io2 Block Express is the only volume type with 99.999% durability (0.001% annual failure rate) on EBS, contrasting with gp3 (and the other EBS volume types) at 99.8% – 99.9% durability (0.1% – 0.2% annual failure rate). Unoptimized legacy environments migrated to the cloud with little change need more assurance and stand to benefit with higher durability. This can be a substantial reason to pick io2 Block Express, but it comes with a cost: io2 Block Express is 56% more expensive per GiB of capacity vs. gp3.
Second, io2 Block Express has much lower and more consistent latency guarantees than gp3. Recently AWS advertised some EBS comparisons. They demonstrated io2 Block Express average latency is guaranteed to be <0.5ms (measured on 16KiB I/Os), whereas the gp3 guarantee is just “milliseconds,” although in practice, we observe most customers achieve 1ms-2ms average latency on gp3. In terms of latency consistency (long tail), io2 Block Express guarantees that 99.9% of I/Os will complete in under 0.8ms, whereas gp3 only guarantees that 99% of I/Os will complete in <10ms: this is dramatically better. The main use case where this really makes an impact is SQL (transactional) databases under high load and response sensitivity. Unlike scale-up SQL architectures, most sharded and NoSQL databases will revert to serving I/Os from an alternative replica if the original data store shows bad performance, so are less sensitive to this kind of latency consistency.
Third, io2 Block Express has some specific features that are missing from gp3. Specifically, the ability to attach a single EBS volume to multiple EC2 instances (“Multi-attach”), which is useful for clustered applications, but not a widespread use case. Again, something that is more typical of traditional SQL (shared-everything) databases than NoSQL (shared-nothing) databases.
Bottom line: gp3 is your storage multi-tool while io2 BX is a high-end forged cutting knife
One interesting nuance is that io2 Block Express capacity is 56% more expensive, but its IOPS are 13x more expensive than gp3! Is it really worth it? If your application is a critical underpinning of your business and is sensitive enough to benefit from those latency guarantees, it's a solid choice.
Otherwise, be pragmatic. For most users, the best course of action is: “choose gp3 unless proven otherwise.” Given the price differential, you need a very good justification to use io2 Block Express. If you do use it, you've got the freedom to modify performance and volume type up to four times in a 24 hour period. Transitioning between the two is easily done using the ModifyVolume function-just don't forget to move back to gp3 when you no longer need premium performance!
In This Article
September 2025: The performance gap narrows
Why go for io2 Block Express in 2026 and beyond?
Bottom line: gp3 is your storage multi-tool while io2 BX is a high-end forged cutting knife
EBS Auto-Scaler
Sensor
About
Documentation
Careers
Blog
Events
Glossary
Terms of Use
Privacy Policy
© 2026 Datafy. All rights reserved
