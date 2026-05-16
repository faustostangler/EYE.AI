---
name: EBS Snapshots: How They Work, Measuring and Reducing Costs [2025] - N2W Software
keywords: (placeholder)
metadata:
  url: https://n2ws.com/blog/aws-ebs-snapshot/aws-ebs-snapshots-all-you-need-to-know
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
EBS Snapshots: How They Work, Measuring and Reducing Costs [2025]
Manage Consent
We use cookies for analytics (Google Analytics, HubSpot) and marketing (Bing, Google, Facebook, LinkedIn). You can accept or deny all.
Functional [x] 1 Functional Always active
The technical storage or access is strictly necessary for the legitimate purpose of enabling the use of a specific service explicitly requested by the subscriber or user, or for the sole purpose of carrying out the transmission of a communication over an electronic communications network.
Preferences [-] 1 Preferences
The technical storage or access is necessary for the legitimate purpose of storing preferences that are not requested by the subscriber or user.
Statistics [-] 1 Statistics
The technical storage or access that is used exclusively for statistical purposes. The technical storage or access that is used exclusively for anonymous statistical purposes. Without a subpoena, voluntary compliance on the part of your Internet Service Provider, or additional records from a third party, information stored or retrieved for this purpose alone cannot usually be used to identify you.
Marketing [-] 1 Marketing
The technical storage or access is required to create user profiles to send advertising, or to track the user on a website or across several websites for similar marketing purposes.
Manage options
Manage services
Manage {vendor_count} vendors
Read more about these purposes
Accept Deny View preferences Save preferences View preferences
Privacy Policy
{title}
Contact 
Skip to content
Product
AWS Backup & Recovery
Azure Backup & Recovery
Pricing
Solutions
Resources
Blog
AWS Backup
Azure Backup
Azure Disaster Recovery
Disaster Recovery in Cloud
AWS Disaster Recovery
AWS Costs
Cloud Costs
Cloud Backup Services
S3 Backup
Ransomware Protection
Data Breaches
Immutable Backups
Kubernetes Security
Multi-Cloud
NIS2 Compliance
Support
Documentation
Knowledge Base
Submit a Ticket
Company
Customers
Product
AWS Backup & Recovery
Azure Backup & Recovery
Pricing
Solutions
Resources
Blog
AWS Backup
Azure Backup
Azure Disaster Recovery
Disaster Recovery in Cloud
AWS Disaster Recovery
AWS Costs
Cloud Costs
Cloud Backup Services
S3 Backup
Ransomware Protection
Data Breaches
Immutable Backups
Kubernetes Security
Multi-Cloud
NIS2 Compliance
Support
Documentation
Knowledge Base
Submit a Ticket
Company
Customers
Try it Free
Search
Get a demo
Try it Free
Product
AWS Backup & Recovery
Azure Backup & Recovery
Pricing
Solutions
Resources
Blog
AWS Backup
Azure Backup
Azure Disaster Recovery
Disaster Recovery in Cloud
AWS Disaster Recovery
AWS Costs
Cloud Costs
Cloud Backup Services
S3 Backup
Ransomware Protection
Data Breaches
Immutable Backups
Kubernetes Security
Multi-Cloud
NIS2 Compliance
Support
Documentation
Knowledge Base
Submit a Ticket
Company
Customers
Product
AWS Backup & Recovery
Azure Backup & Recovery
Pricing
Solutions
Resources
Blog
AWS Backup
Azure Backup
Azure Disaster Recovery
Disaster Recovery in Cloud
AWS Disaster Recovery
AWS Costs
Cloud Costs
Cloud Backup Services
S3 Backup
Ransomware Protection
Data Breaches
Immutable Backups
Kubernetes Security
Multi-Cloud
NIS2 Compliance
Support
Documentation
Knowledge Base
Submit a Ticket
Company
Customers
Try it Free
Search
Get a demo
Try it Free
AWS EBS Snapshot
12min read
EBS Snapshots: How They Work, Measuring and Reducing Costs [2025]
Everything you need to know about Amazon EBS snapshots, including how they work, pricing, and automation options. 
Catalin Voicu
August 15, 2025
Share post:
What Is an EBS Snapshot?
An Amazon EBS snapshot is a backup of the data on an Amazon Elastic Block Store (EBS) volume at a specific point in time. Snapshots are stored in Amazon S3 and are used to create new volumes or restore existing ones. Unlike traditional full-volume backups, EBS snapshots are incremental, which means only the blocks that have changed since the last snapshot are saved. This makes the backup process more storage- and cost-efficient.
Snapshots can be created manually or automatically via AWS Backup or lifecycle policies. Once a snapshot is created, it can be used to launch a new EC2 instance, restore a damaged volume, or replicate data to another region for disaster recovery. Because the snapshot is stored in S3, it is decoupled from any specific availability zone, making it a portable and durable backup solution.
EBS snapshots are commonly used for scheduled backups, cross-region replication, long-term archival, and rapid disaster recovery.
This is part of a series of articles about AWS backup
How Do EBS Snapshots Work?
AWS EBS snapshots work by capturing the state of an EBS volume at a particular point in time and storing the data in Amazon S3. The first snapshot of a volume is a full copy of all the blocks in use. Subsequent snapshots are incremental, saving only the blocks that have changed since the last snapshot. This incremental model reduces storage consumption and shortens the time required for snapshot creation.
When a snapshot is created, EBS identifies which blocks on the volume have changed since the previous snapshot. These changed blocks are compressed and stored in Amazon S3. The snapshot metadata maintains a reference to all blocks—both unchanged and new—so that the complete volume can be reconstructed at any point. Users interact with snapshots through the EBS and EC2 APIs, which abstract the S3 storage layer.
Snapshots can be used to create new EBS volumes, either in the same region or in a different region for disaster recovery. When a volume is created from a snapshot, the data is lazily loaded from S3. This means that only the blocks accessed are fetched and restored, enabling fast volume creation and reduced time-to-recovery. Meanwhile, AWS handles background retrieval of the remaining data.
EBS Snapshot Pricing – How Much Does It Cost?
The following table summarizes EBS snapshot pricing.
Learn more about AWS EBS pricing in this post.
EBS snapshot pricing example
Let's take an example of a daily snapshot supporting a data retention policy of 30 days. Next, let's assume the initial backup was of 2TB and that your incremental daily changes are 5% of the total data on the volume. At the end of a 30-day month the snapshot size will be: 2TB (baseline) + 30(days)2TB5%/day = 5TB (without counting compression)
How to Estimate Your Actual AWS EBS Snapshot Costs
Estimating EBS snapshot costs can be tricky. Let's see the basic steps involved.
Rough Estimation
In order to estimate how large your EBS snapshots will be, you need to know how much your volumes are changing. One way would be to guesstimate, we can use a simple thumb rule that is often used in- backup planning: A typical data volume of a production server changes about 3% a day.
Let's try and calculate the cost. Assuming a 1TB EBS volume, that is 70% full at first. We take snapshots and keep them for 30 days. So, the first full will be taking 700GB (70% of 1TB). For the incremental snapshots, we can multiply 30 (days) by 30GB (3% of 1TB) and we reach 900GB. Add them together and we reach about 1.6TB of total snapshot storage. AWS compresses the snapshots when they are stored in S3. It is hard to estimate how much data will be reduced by compression.
If compression is zip-like and data on the EBS volume consists mostly of text files and can be compressed very well. On the other hand, if data on the volume is already compressed (e.g. compressed file system, media files), it will not be compressed at all. You can decide not to factor compression into your calculation or give it mostly a 2:1 ratio. The cost of storing EBS snapshot data is $0.05 per GB per month (Virginia region, August 2025). For 1600GB the price will be $80/month. If we assume compression is effective, it will be half: $40/month. Accurate? No. Something we can work with, maybe…
A More Accurate Method
For more accurate AWS EBS pricing, you need a more accurate method of knowing how much your EBS volumes are changing. To do this, you can sample them. To do that you can install software that monitors your disk changes and reports them to you. Take a large enough sample at typical times, and you can get a very good idea on how much any specific EBS volume is changing.
For Windows instances you can use the internal Windows tool, Performance Monitor (simply type run > perfmon), Perfmon can give you the number of bytes written on average per second, just add the logical disk related counters.
Another tool would be Disk Monitor, a tool you can download from Microsoft's site (originally written by SysInternals), it can monitor writes to disk and create a file from it that can later be imported to a spreadsheet. You can download it from here. In Linux instances, you can use a command-line Python-based open source tool named Iotop.
Write Patterns and How They Affect Snapshot Size
Write IO patterns affect the amount of data your snapshots will take. Let's take an example: An EBS volume with 1GB of data and then every day there is a 1GB change on the volume. So the first full snapshot will take 1GB of snapshot storage space, and then every daily incremental will also take 1GB. Now let's assume we keep snapshots for 10 days and delete any older ones.
So, if every 1GB is written to new unused blocks on the volumes (e.g. new static files were written, older ones don't change), then my snapshot data will grow by 1GB every day forever (or until the EBS volume if full).
Deleting old snapshots won't matter because all the blocks they occupy will need to be saved. So after 10 days, you will have 10GB of snapshot data, and after 100 days 100GB. Now let's assume the other extreme: There is only 1GB of occupied space on this EBS volume, and every day that same 1GB is overwritten (e.g. a bit like a database file that changes a lot, but not necessarily grows).
In this case, you will have 10GB of snapshot data after 10 days, but after 100 days you will still have 10GB of snapshot data because older snapshots are deleted.
Number of Snapshots Don't Necessarily Matter
We keep talking about daily change. How does the frequency of snapshot-taking fit into that? Well, that depends. You can take one snapshot a day or take six. If in the same day blocks won't be written and then rewritten it doesn't matter. One or six snapshots will use the same amount of storage space, and therefore will cost the same.
This is a very significant conclusion when configuring your EBS volumes backup solution; you can actually take a higher resolution of snapshots without increasing the cost, giving you a better RPO (Recovery Point Objective). In reality, things will probably not be that “clean,” but in a typical application, most data will probably not be rewritten all the time, and in most cases, you will be able to take more frequent snapshots without affecting your AWS bill by much.
Limitations of Amazon EBS Snapshots
While EBS snapshots offer a convenient way to back up volumes in AWS, they come with several important limitations when compared to traditional backup solutions.
1. Not Application-Aware
EBS snapshots do not automatically ensure application consistency. Many applications and databases cache data in RAM and do not immediately write changes to disk. As a result, a snapshot may not capture the most current data unless the application is properly quiesced first. AWS recommends manually flushing caches and stopping the EC2 instance or detaching the volume before creating a snapshot to avoid data inconsistency.
2. No Support for Offsite or On-Premises Copies
Snapshots are stored exclusively in Amazon S3, and AWS does not allow direct access to the snapshot data. This restriction prevents copying snapshot data to other environments, such as on-premises systems or alternate cloud providers. This limits the ability to implement broader disaster recovery strategies that require data portability across platforms.
3. No Native Deduplication
EBS snapshots can become costly over time due to the lack of built-in deduplication. Even though they are incremental, repetitive data across volumes or snapshots is not automatically deduplicated. This leads to higher storage consumption and increased costs, especially for environments with redundant data.
4. Limited Scheduling and Retention Controls
While AWS offers basic snapshot automation using CloudWatch Events and cron expressions, the scheduling features are limited. These methods require custom configuration and scripting to manage retention policies, such as deleting old snapshots. In contrast, many third-party backup tools offer more intuitive interfaces and advanced scheduling options that simplify management.
AWS Backup Checklist
Fill in the gaps in your backup and DR strategy
Fortify your cloud across every critical dimension.
Efficiency + Optimization
Security + Control
Orchestration + Visibility
Download now 
Best Practices for Reducing EBS Snapshot Costs
Here are some useful practices to help reduce the costs of using snapshots in Amazon EBS.
1. Store Snapshots as Archival Data
Moving infrequently accessed snapshots to the archive tier can cut storage costs by up to 75%. Archive snapshots are ideal for compliance, auditing, or long-term retention needs. While standard snapshots store only the changed blocks, archival snapshots store full copies, which simplifies retrieval for point-in-time recovery.
You can automate snapshot archiving using lifecycle policies in AWS Backup. This helps ensure that older backups are transitioned to low-cost storage without manual effort, aligning snapshot retention with organizational policies and compliance requirements.
2. Automatically Delete Older Snapshots
Snapshots that are older than 30 days and not recently accessed often provide minimal recovery value. Regularly identifying and deleting such snapshots can significantly reduce storage costs.
A practical approach is to retrieve all snapshot metadata using AWS SDK tools like boto3, analyze snapshot age, and retain only the latest relevant snapshot per EBS volume if it exceeds 30 days. Automating this cleanup process ensures cost control without compromising backup integrity.
3. Define the Right Lifecycle Policies for Snapshots
Implementing well-defined lifecycle policies allows you to standardize how long snapshots are kept and when they are deleted or archived. For example, you can keep daily snapshots for one week, weekly for a month, and monthly for a year. This strikes a balance between cost efficiency and recovery flexibility.
Use AWS Data Lifecycle Manager (DLM) to enforce these policies automatically. DLM enables scheduled creation and deletion of snapshots across volumes, reducing manual oversight and eliminating forgotten snapshots that continue to accrue charges.
4. Consider Frequency of Use and Unreferenced Data
Not all snapshots are equally valuable. Snapshots that haven't been used recently or contain mostly redundant data blocks offer limited utility. By identifying such snapshots—especially those that are not the most recent and have over 25% unreferenced data—you can decide whether to delete or move them to the archive tier.
Automated tools can help detect low-value snapshots based on age, usage patterns, and block-level data comparison. Using this data to guide retention decisions helps optimize storage and ensures only high-utility snapshots incur ongoing charges.
Key Considerations for Automating EBS Snapshots
Even when dealing with a non-critical IT environment, you still want to wake up in the morning and find your data safe and sound. To continue development and testing of your applications without interruption or to ensure your customer data remains available you must automate your snapshot schedule. However, there are several considerations to keep in mind before writing the first line command for this purpose. One of the most important when dealing with backups is consistency.
That's why EBS snapshots are “crash-consistent,” which means each backup captures all data at exactly the same point in time. However, when an EBS snapshot is taken while an instance is up and running, data in memory is discarded which may not work well for sensitive database-intensive applications. So, if we want to make sure a snapshot is application consistent, which means applications start from a consistent state and experience no issues when we recover them, we need to implement application consistent snapshots.
Considering its dynamic manner, your automated backup should keep track of the changes to your environment such as new attached EBS volumes (which can be done using AWS resource tagging). You should also consider your AWS environment growth rate and try to prepare for a sudden peak in line with your specific growth trend. Finally, a data backup is worth nothing if you can't actually restore the running service. You're not necessarily protected just because your automated procedures are running. So make sure you monitor your backup procedures and run recovery tests periodically.
Automating AWS Backups and Reducing Costs with N2W
Native AWS tools give you snapshots, but they leave you juggling scripts, lifecycle rules, and unpredictable bills. N2WS takes the pain out of the process:
AnySnap Archiver: Ingest and archive existing EBS snapshots to slash costs instantly.
Set-it-and-forget-it policies: Define retention once, and we'll automatically rotate, archive, and delete old snapshots—no more forgotten charges.
Cross-region & cross-cloud recovery: Restore snapshots into AWS, Azure, or Wasabi in just 4 clicks.
Cost Explorer: See exactly what you're spending on snapshots—and where to cut back.
👉 Snapshots are just one piece of the cost puzzle. Our AWS Cost Optimization Guide shows you proven strategies to reclaim your budget and future-proof your cloud spend. 
Get the monthly TL;DR newsletter
UTM Campaign
UTM Content
UTM Medium
UTM Source
UTM Term
[-] true By submitting this form, you agree to our Privacy Policy* Sign me up
Related posts
How to estimate your AWS EBS snapshot pricing cost
5 AWS EBS Volume Types: Cost-Performance Based Comparison [2025]
Backup Your AWS Cloud Environment Using AWS CloudFormation – Part 2
4 Ways to Automate AWS EC2 Instance Backups
Why EBS snapshots are not enough for AWS backup
AWS Backup: Top 15 Questions, How It Works, Pricing and Pros/Cons
AWS Backup Vault: The Basics and a Quick Tutorial
AWS Backup Snapshots: How It Works, Tutorial, and Best Practices
EC2 Snapshot: Using EBS vs. AMI Snapshots for Backup and Recovery
AWS Backup for RDS: How It Works, Where It Falls Short, and How to Do It Right
Working With Amazon RDS Snapshots: The Basics and a Quick Tutorial
Top 3 Reasons to Automate Your Manual Redshift Snapshots
Saving AWS Backups to Cold Storage: Why and How
Major AWS Outages and 6 Tips for Surviving One
AWS Data Lifecycle Manager: How It Works, Pros/Cons, and Best Practices
Best AWS Backup Tools for Disaster Recovery: Top 3 in 2026
AWS Backup Pricing: 7 Cost Components with Examples
Best Secure Backup Options for AWS Environments: Top 10 in 2026
Best AWS Backup Options for Dynamic Workloads: Top 8 in 2026
Featured posts
AWS Backup: Top 15 Questions, How It Works, Pricing and Pros/Cons
Estimate storage costs with N2WS' NEW AWS Cost Savings Calculator
Leverage AI Tools to Streamline Cloud Disaster Recovery
What Is Azure Site Recovery? A Practical Guide to your BCDR strategy in Azure
You might also like
N2W Blog
05/10/2026
Jessica Eisenberg
The Latest AWS's “Thermal Event” and what it means for your disaster recovery planning
AWS's latest 'thermal event' in US-East-1 took down Coinbase, FanDuel, CME Group and more for nearly two days because a
Read more
Microsoft Azure Cloud
13min read
05/01/2026
Adam Bertram
Best Azure Backup Services: Top 8 Solutions in 2026
Azure Backup Services help teams protect critical workloads, applications, and virtual machines by enabling efficient data recovery. Let's review.
Read more
N2W Blog
21min read
05/01/2026
Sebastian Straub
9 Enterprise Cloud Backup Services to Know in 2026
Cloud backup services play a critical role in modern data protection, offering reliable and scalable options for safeguarding data.
Read more
Don't wait for a disaster
With N2W, your data is safe, your recovery is fast, and your peace of mind is guaranteed. It's backup you can rely on—no superhero cape required.
Protect your cloud assets now
[
Get a demo
](https://n2ws.com/demo/?utm_internal__c=footer&)
[
Try it free
](https://n2ws.com/trial/?utm_internal__c=footer&) 
Ridiculously easy backup & recovery
 
Product
Product Overview
AWS Backup
Azure Backup
Free Trial
Get a Demo
Pricing
Solutions
Compliance
Cost Savings
Disaster Recovery
Public Sector
Ransomware
Resellers & MSPs
Resources
Blog
Documentation
Cost Savings Calculator
More Resources
Tutorials
Company
About N2W
Careers
Contact
Customer Stories
Events
Become a Partner
Support
Knowledge Base
Submit a Ticket
Trial Install Guide
Trust Center
Legal
EULA
© N2W Software, Inc. All rights reserved.
Follow us on social
Linkedin-in X-twitter Facebook-f Youtube
Manage consent
