---
name: AWS EBS Volume Types: The Complete Guide for 2025 - Lucidity
keywords: (placeholder)
metadata:
  url: https://www.lucidity.cloud/blog/ebs-volume-types
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
AWS EBS Volume Types: The Complete Guide for 2025 
AWS EBS Volume Types: The Complete Guide for 2025
Asawari Ghatage
|
April 18, 2026 
Amazon Elastic Block Store (EBS) provides persistent block-level storage volumes for use with Amazon EC2 instances. As a critical component of AWS infrastructure, choosing the right EBS volume types can significantly impact application performance, reliability, and cost-effectiveness.
In this comprehensive guide, we'll explore all AWS EBS volume types currently available, including their specifications, optimal use cases, performance characteristics, and pricing considerations. We'll also dive into advanced topics like performance optimization, monitoring, backup strategies, and integration with other AWS services.
By the end of this article, you'll have the knowledge to make informed decisions about your storage infrastructure in AWS.
EBS Volume Types Overview
Amazon offers several EBS volume types optimized for different use cases, varying in performance characteristics and cost:
Solid-State Drive (SSD) Volumes
General Purpose SSD (gp3) - Latest generation general-purpose SSD volume
General Purpose SSD (gp2) - Previous generation general-purpose SSD volume
Provisioned IOPS SSD (io2) Block Express - Highest performance SSD volume
Provisioned IOPS SSD (io2) - High-performance SSD volume designed for critical workloads
Provisioned IOPS SSD (io1) - Previous generation provisioned IOPS volume
Hard Disk Drive (HDD) Volumes
Throughput Optimized HDD (st1) - Low-cost HDD designed for frequently accessed, throughput-intensive workloads
Cold HDD (sc1) - Lowest cost HDD designed for less frequently accessed workloads
Each of these EBS volume types is engineered to address different storage needs, from high-performance databases to long-term archival storage. Let's examine each type in detail to understand their capabilities and ideal use cases.
SSD-Backed Volumes: Detailed Analysis
General Purpose SSD (gp3)
Key Specifications:
Base performance: 3,000 IOPS and 125 MiB/s throughput
Scalable to 16,000 IOPS and 1,000 MiB/s throughput
Volume size: 1 GiB to 16 TiB
Performance independent of volume size
Performance Characteristics:
The gp3 volumes provide predictable 3,000 IOPS and 125 MiB/s throughput baseline performance regardless of volume size. Unlike gp2, gp3 allows independent scaling of IOPS and throughput without increasing volume size, offering more flexibility and potential cost savings.
Optimal Use Cases:
Development and test environments
Medium-sized single instance databases
Boot volumes
Virtual desktops
Low-latency interactive applications
Web servers and content management systems
Pricing Advantage:
Gp3 volumes are designed to be 20% cheaper than gp2 volumes at the same provisioned performance levels. The ability to independently provision IOPS and throughput allows for optimizing costs based on your specific workload requirements.
General Purpose SSD (gp2)
Key Specifications:
Performance tied to volume size: 3 IOPS per GiB with a minimum of 100 IOPS
Maximum of 16,000 IOPS per volume
Volume size: 1 GiB to 16 TiB
Burst capability using I/O credits
I/O Credit System:
Gp2 volumes use an I/O credit mechanism where smaller volumes can burst to 3,000 IOPS when needed. The baseline performance is 3 IOPS per GiB, meaning a 100 GiB volume has a baseline of 300 IOPS but can burst to 3,000 IOPS.
Burst Duration Calculation:
Burst duration = (Credit balance) / (Burst IOPS - Baseline IOPS)
For example, a 100 GiB volume with 5.4 million I/O credits and baseline 300 IOPS can burst to 3,000 IOPS for approximately 30 minutes.
Optimal Use Cases:
Similar to gp3, but ideal when burst capacity is needed for smaller volumes
Boot volumes and low-IOPS applications
Development and testing environments
Provisioned IOPS SSD (io2) Block Express
Key Specifications:
Performance: Up to 256,000 IOPS and 4,000 MiB/s throughput
Volume size: 4 GiB to 64 TiB
99.999% durability (highest among EBS volumes)
Sub-millisecond latency
Performance Characteristics:
io2 Block Express is one of AWS's most powerful EBS volume types, delivering SAN-level performance in the cloud. It offers consistent sub-millisecond latency and the highest durability among all EBS types.
Optimal Use Cases:
High-performance databases (Oracle, Microsoft SQL Server, SAP HANA)
ERP systems requiring extreme performance
Critical business applications demanding high throughput and low latency
Data warehousing and analytics platforms processing large datasets
Provisioned IOPS SSD (io2)
Key Specifications:
Performance: Up to 64,000 IOPS and 1,000 MiB/s throughput
Volume size: 4 GiB to 16 TiB
99.999% durability
IOPS to volume size ratio of 500:1
Performance Characteristics:
Io2 volumes deliver more consistent performance than io1 with the same durability as io2 Block Express, making them suitable for mission-critical workloads that don't require the extreme performance of Block Express.
Optimal Use Cases:
Medium to large relational databases
NoSQL databases (MongoDB, Cassandra)
Critical business applications with moderate to high I/O requirements
Applications requiring consistent performance and high durability
Provisioned IOPS SSD (io1)
Key Specifications:
Performance: Up to 64,000 IOPS and 1,000 MiB/s throughput
Volume size: 4 GiB to 16 TiB
99.8-99.9% durability
IOPS to volume size ratio of 50:1
Performance Characteristics:
Now considered a previous generation volume type, io1 offers similar maximum performance to io2 but with lower durability and a more restrictive IOPS-to-volume ratio.
Optimal Use Cases:
Legacy systems that were configured for io1
Applications where the migration to io2 has not yet been completed
HDD-Backed Volumes: Cost-Effective Options
Throughput Optimized HDD (st1)
Key Specifications:
Baseline throughput: 40 MiB/s per TiB
Burst throughput: Up to 250 MiB/s per TiB
Maximum throughput of 500 MiB/s per volume
Baseline IOPS: 500 IOPS
Burst IOPS: Up to 500 IOPS per TiB with a maximum of 1,000 IOPS
Volume size: 125 GiB to 16 TiB
Performance Characteristics:
St1 volumes use a throughput credit system similar to the I/O credit system on gp2. The baseline throughput is 40 MiB/s per TiB, with the ability to burst to 250 MiB/s per TiB when needed.
Optimal Use Cases:
Big data analytics
Log processing
Data warehousing
Streaming workloads
ETL processes
Sequential data access patterns
Cold HDD (sc1)
Key Specifications:
Baseline throughput: 12 MiB/s per TiB
Burst throughput: Up to 80 MiB/s per TiB
Maximum throughput of 250 MiB/s per volume
Baseline IOPS: 250 IOPS
Volume size: 125 GiB to 16 TiB
Performance Characteristics:
Sc1 is one of the most cost-effective EBS volume types, designed for infrequently accessed data. Like st1, they use a throughput credit system but with lower performance characteristics.
Optimal Use Cases:
Archived data
Infrequently accessed data
Cold storage scenarios
Backup and disaster recovery
Compliance data that must be retained but rarely accessed
Comparative Analysis of EBS Volume Types
Performance Comparison Matrix
Cost Efficiency Analysis
When considering cost efficiency, it's important to look at the total cost of ownership (TCO) rather than just the per-GB price:
Gp3 provides the best cost-efficiency for general-purpose workloads, especially with the ability to independently scale IOPS and throughput.
Io2 offers better value than io1 due to higher durability at the same price point.
HDD volumes (st1 and sc1) are significantly cheaper per GB but come with performance trade-offs that may impact application performance and user experience.
Io2 Block Express provides the highest performance but at a premium price, making it suitable only for the most demanding workloads where performance justifies the cost.
Advanced EBS Features and Best Practices
RAID Configurations
While individual EBS volumes and most EBS volume types provide good performance, some applications require even higher IOPS or throughput than a single volume can deliver. Using RAID configurations can address these requirements:
RAID 0 (Striping): Distributes I/O across volumes for higher performance
Pro: Increases IOPS and throughput linearly with number of volumes
Con: Failure of any single volume results in complete data loss
RAID 1 (Mirroring): Duplicates data across volumes for redundancy
Pro: Improves read performance and data durability
Con: Write performance doesn't improve, and storage cost doubles
Implementation Example:
For a high-performance database requiring 40,000 IOPS, you could create a RAID 0 array with three gp3 volumes, each provisioned with 16,000 IOPS.
Performance Optimization Techniques
Instance Types: Ensure your EC2 instance type can support your EBS performance requirements. EBS-optimized instances provide dedicated throughput between EC2 and EBS.
Volume Initialization: Pre-warm new volumes that were created from snapshots to avoid the performance hit of reading data blocks for the first time.
I/O Block Size: Align your application's I/O block size with the volume type. For example, SSD volumes perform best with smaller block sizes, while HDD volumes prefer larger block sizes.
Queue Depth Management: Optimize the number of pending I/O requests to maximize throughput without introducing excessive latency.
Monitoring EBS Performance with CloudWatch
AWS CloudWatch provides several metrics for monitoring EBS volume performance:
VolumeReadOps and VolumeWriteOps: Track the number of read and write operations
VolumeReadBytes and VolumeWriteBytes: Monitor the amount of data read and written
VolumeTotalReadTime and VolumeTotalWriteTime: Measure the total time spent on I/O operations
VolumeQueueLength: Track the number of pending I/O requests
BurstBalance: Monitor the burst bucket balance for gp2, st1, and sc1 volumes
Setting up CloudWatch alarms for these metrics can help you identify performance issues before they impact your applications.
EBS vs. Other AWS Storage Services
EBS vs. Amazon EFS
Read our detailed EBS vs EFS comparison here.
EBS:
Block-level storage attached to a single EC2 instance
Higher performance for single-instance workloads
Supports a wide range of file systems
Pay for provisioned capacity
EFS:
Fully managed NFS file system
Multi-AZ redundancy built-in
Can be mounted on multiple EC2 instances simultaneously
Pay for what you use
Better for shared access scenarios
EBS vs. Amazon S3
EBS:
Block storage with low latency
Designed for frequent, random access
Attached to a specific EC2 instance
Good for databases and file systems
S3:
Object storage with higher latency
Highly durable and globally accessible
Independent of EC2 instances
Excellent for static content, backups, and data lakes
More cost-effective for large data sets
Backup and Disaster Recovery Strategies
EBS Snapshots
EBS snapshots provide point-in-time backups of your volumes:
Incremental backups: Only changed blocks are saved, reducing storage costs and backup time
Cross-region replication: Copy snapshots to different regions for disaster recovery
Encryption: Snapshots of encrypted volumes are automatically encrypted
Best Practices for Snapshots:
Schedule regular automated snapshots
Create snapshots during low-activity periods
Tag snapshots for better organization and lifecycle management
Implement a retention policy based on RPO (Recovery Point Objective)
AWS Backup Integration
AWS Backup provides a centralized service for managing backups across AWS services:
Centralized management: Manage EBS, RDS, DynamoDB, and other backups from a single console
Automated backup scheduling: Set up backup plans with specific frequencies and retention periods
Cross-region and cross-account backup: Enhance disaster recovery capabilities
Backup policies: Apply organization-wide backup policies to ensure compliance
Third-Party Backup Solutions
Several third-party solutions enhance AWS's native backup capabilities:
N2WS Backup & Recovery: Specialized for AWS workloads with application-consistent backups
NetApp Cloud Volumes ONTAP: Provides efficient snapshot technology and cross-regionreplication ****
Veeam Backup for AWS: Offers comprehensive backup and recovery options integrated with on-premises infrastructure
Conclusion
Choosing the right EBS volume type is crucial for optimizing performance, reliability, and cost-efficiency in AWS environments. The right choice depends on your specific workload characteristics, performance requirements, and budget constraints.
For most general-purpose workloads, gp3 volumes offer the best balance of performance and cost. For high-performance databases and critical applications, io2 or io2 Block Express volumes provide the necessary IOPS and durability.
For large sequential workloads with cost sensitivity, the HDD-based st1 and sc1 volumes offer attractive options.
Lucidity's AutoScaler automatically rightsizes EBS volumes depending on demand, helping you optimize costs while maintaining performance as your needs change. Book a demo today to see how AutoScaler can transform your AWS storage management.
Beyond just selecting the right EBS volume types, implementing proper monitoring, backup strategies, and performance optimization techniques will ensure that your AWS storage infrastructure meets your business requirements efficiently and reliably.
By understanding the strengths and limitations of each of the EBS volume types and implementing the best practices outlined in this guide, you can build a robust, high-performance, and cost-effective storage infrastructure in AWS.
FAQ: Common Questions About EBS Volume Types
Q: Can I change the volume type of an existing EBS volume?
A: Yes, you can modify the volume type of an existing EBS volume without losing data. For example, you can convert a gp2 volume to gp3, or an io1 volume to io2. The modification in EBS volume types can be done while the volume is in use, although there may be performance impacts during the conversion process.
Q: What happens when I hit the burst limit on a gp2 volume?
A: When a gp2 volume exhausts its I/O credit balance, its performance reverts to the baseline rate of 3 IOPS per GiB. For example, a 1,000 GiB volume delivers 3,000 IOPS under normal conditions. Some volume types may also support burstable performance, where accumulated I/O credits allow temporary increases beyond the baseline IOPS limit. If your application requires sustained performance above this baseline, consider upgrading to a larger gp2 volume or migrating to gp3.
Q: Are EBS volumes automatically replicated for redundancy?
A: Yes, EBS volumes are automatically replicated within their Availability Zone to prevent data loss from component failure. For additional protection against AZ failures, you should regularly create EBS snapshots or replicate data to volumes in different AZs.
Q: How do I encrypt my EBS volumes?
A: EBS volumes can be encrypted using AWS Key Management Service (KMS). You can enable encryption when creating a new volume or by creating an encrypted snapshot of an unencrypted volume and then creating a new encrypted volume from that snapshot.
Table of Contents
EBS Volume Types Overview
• Solid-State Drive (SSD) Volumes
• Hard Disk Drive (HDD) Volumes
SSD-Backed Volumes: Detailed Analysis
• HDD-Backed Volumes: Cost-Effective Options
Comparative Analysis of EBS Volume Types
• Performance Comparison Matrix
• Cost Efficiency Analysis
Advanced EBS Features and Best Practices
EBS vs. Other AWS Storage Services
Backup and Disaster Recovery Strategies
Conclusion
FAQ: Common Questions About EBS Volume Types
Sign Up
Keep up to date with our weekly digest of articles. Submit
 
Thank you! Your submission has been received!
Oops! Something went wrong while submitting the form.
Author 
Asawari Ghatage
Share this post
Related Blogs
The 2026 Cloud Storage Reset: Why AWS, Azure, and Google Just Made Your Storage Bill Bigger
Raj Dutt
•
May 5, 2026
Read Blog
category
cloud
Industry 
The free lunch is over: How AI broke the cloud storage pricing trend
Sharad Singla
•
May 1, 2026
Read Blog
category
cloud
Industry 
Terraform azurerm_managed_disk in Production: How to Use, Patterns and Pitfalls
Josh Dreyfuss
•
April 28, 2026
Read Blog
category
cloud
Industry   
Get a demo
Company
About Us Newsroom Careers Customers
Helpful Links
Resources Demo
© 2026 Lucidity
Terms
.
Privacy 
Products
AutoScaler Eliminate block storage overprovisioning, autonomously
Lumen Visibility, recommendations, and actions for cloud storage
Assessment Uncover hidden disk metrics and potential savings 
AutoScaler Demo
Watch a recorded walkthrough of AutoScaler
Watch now
Resources
Corporate Resources Blog ROI Calculator Case Studies 
How ESO automates cloud storage optimization with Lucidity
Read case study
Customers Partners
Company
About Us Newsroom Careers Events and Webinars 
Lucidity named a 2025 Gartner Cool Vendor in Storage
Read More
Get a demo  

Back

Product

Resources

Customers
Partners
Company

Product

AutoScaler Eliminate block storage overprovisioning, automatically
Lumen Visibility, recommendations, and actions for cloud storage
Assessment Uncover hidden disk metrics and potential savings
Resources

All Resources Blog ROI Calculator Case Studies
Company

About Us Newsroom Careers Events and Webinars
Get a demo 
