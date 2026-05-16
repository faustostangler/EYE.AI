---
name: Choosing the Right EC2 Instance Type for Your Application | AWS News Blog
keywords: (placeholder)
metadata:
  url: https://aws.amazon.com/blogs/aws/choosing-the-right-ec2-instance-type-for-your-application/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Choosing the Right EC2 Instance Type for Your Application | AWS News Blog
Select your cookie preferences
We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.
If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”
Accept Decline Customize
Customize cookie preferences
We use cookies and similar tools (collectively, "cookies") for the following purposes.
Essential
Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.
Performance
Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes. [x]
Allowed
Functional
Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly. [x]
Allowed
Advertising
Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising. [x]
Allowed
Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the AWS Cookie Notice .
Cancel Save preferences
Your privacy choices
We and our advertising partners (“we”) may use information we collect from or about you to show you ads on other websites and online services. Under certain laws, this activity is referred to as “cross-context behavioral advertising” or “targeted advertising.”
To opt out of our use of cookies or similar technologies to engage in these activities, select “Opt out of cross-context behavioral ads” and “Save preferences” below. If you clear your browser cookies or visit this site from a different device or browser, you will need to make your selection again. For more information about cookies and how we use them, read our Cookie Notice . [x] allowed
Allow cross-context behavioral ads [-] not allowed Opt out of cross-context behavioral ads
To opt out of the use of other identifiers, such as contact information, for these activities, fill out the form here .
For more information about how AWS handles your information, read the AWS Privacy Notice .
Cancel Save preferences
Unable to save cookie preferences
We will only store essential cookies at this time, because we were unable to save your cookie preferences.
If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.
Dismiss
Skip to Main Content 
Filter: All
English
Contact us
AWS Marketplace
Support
My account
More
Search Filter: All
Sign in to console
Create account
AWS Blogs
AWS News Blog
Choosing the Right EC2 Instance Type for Your Application
by Jeff Barr on 14 MAY 2013 in Amazon EC2 Permalink Share
 https://aws.amazon.com/blogs/aws/choosing-the-right-ec2-instance-type-for-your-application/
Over the past six or seven years I have had the opportunity to see customers of all sizes use Amazon EC2 to power their applications, including high traffic web sites, Genome analysis platforms, and SAP applications. I have learned that the developers of the most successful applications and services use a rigorous performance testing and optimization process to choose the right instance type(s) for their application.
In order to help you to do this for your own applications, I'd like to review some important EC2 concepts and then take a look at each of the instance types that make up the EC2 instance family.
Important Concepts
Let's start with some concepts, just to make sure that we are all on the same page.
An Amazon Machine Image (AMI) is a template that defines your operating environment, including the operating system. A single AMI can be used to launch one or thousands of instances.
Instances provide compute power and are the fundamental building blocks. Instances are created by launching an Amazon Machine Image (AMI) on a particular instance type. You can scale the number of instances you are running up or down on demand, either manually or automatically, using Auto Scaling.
Instance Types comprise various combinations of CPU, memory, storage, and networking capacity and give you the flexibility to choose the appropriate mix of resources for your applications. Each instance type has one or more size options that address different workload sizes. For the best experience, you should launch on instance types that are the best fit for your applications.
Instance Families are collections of instance types designed to meet a common goal. To make it easier for you to select the best option for your applications, Amazon EC2 instance types are grouped together into families based on target application profiles.
A vCPU is a virtual Central Processing Unit (CPU). A multicore processor has two or more vCPUs.
Meet the Family
Today, Amazon EC2 gives you the option of choosing between 10 different instance types, distributed across 6 instance families. You have the flexibility to choose the combination of instance types and sizes most appropriate for your application today, and you can always change the type you use later as your business and application needs change. So what are the available instance families and instance types?
General-Purpose. This family includes the M1 and M3 instance types, both of which provide a balance of CPU, memory, and network resources making them a good choice for many applications. For many of you, this family is often the first choice, with sizes ranging from 1 vCPU with 2 GiB of RAM to 8 vCPUs with 30 GiB of RAM. The balance of resources makes them ideal for running small and mid-size databases, more memory-hungry data processing tasks, caching fleets, and backend servers for SAP, Microsoft SharePoint, and other enterprise applications.
M3 instances are the newest generation of general-purpose instances, and give you the option of a larger number of virtual CPUs (vCPUs) that provide higher performance. M3 instances are recommended if you are seeking general-purpose instances with demanding CPU requirements. M1 instances are the original family of general-purpose instances and provide the lowest cost options for running your applications. M1 instances are a great option if you want smaller instance sizes with moderate CPU performance, and a lower overall price.
Compute-Optimized. This family includes the C1 and CC2 instance types, and is geared towards applications that benefit from high compute power.
Compute-optimized instances have a higher ratio of vCPUs to memory than other families and the lowest cost per vCPU of all the Amazon EC2 instance types. If you are running any CPU-bound scale-out applications, you should look at compute-optimized instances first. Examples of such applications include front end fleets for high-traffic web sites, on-demand batch processing, distributed analytics, web servers, video encoding, and high performance science and engineering applications like genome analysis, high-energy physics, or computational fluid dynamics.
CC2 instances are the latest generation of compute-optimized instances and provide the lowest cost for CPU performance for all Amazon EC2 instance types. In addition, CC2 instances provide a number of advanced capabilities: Intel Xeon E5-2670 processors; high core count (32 vCPUs); and support for cluster networking. These capabilities allowed us to create a cluster of 1064 CC2 instances that achieved a Linpack score of 240.09 Teraflops, good for an entry at number 42 in the November 2011 Top500 supercomputer list.
C1 instances are the first generation of compute-optimized instances. They are available in smaller sizes and are ideal for massively scaled-out applications at massive scale. Most examples of customers launching 1000s of instances to transcode videos or for virtual drug design are likely to take advantage of C1 instances.
Memory-Optimized. This family includes the M2 and CR1 instance types and is designed for memory-intensive applications. Instances in this family have the lowest cost per GiB of RAM of all Amazon EC2 instance types. If your application is memory-bound, you should use these instances. Examples include high performance databases and distributed cache, in-memory analytics, genome assembly, and larger deployments of SAP, Microsoft SharePoint, and other enterprise applications. In general, if you are running a performance-sensitive database you should first look at this family.
CR1 instances are the latest generation of memory-optimized instances and provide more memory (244 GiB), faster CPU (Intel Xeon E5-2670) compared to M2 instances. CR1 instances also support cluster networking for bandwidth intensive applications.
M2 instances are available in smaller sizes, and are an excellent option for many memory-bound applications.
Storage-Optimized. This family includes the HI1 and HS1 instance types, and provides you with direct-attached storage options optimized for applications with specific disk I/O and storage capacity requirements. Currently there are two types of storage-optimized instances.
HI1 instances are optimized for very high random I/O performance and low cost per IOPS. These instances can deliver over 120,000 4k random read IOPS making them ideal for transactional applications. In particular, we designed these instances to be the best platform for large deployments of NoSQL databases like Cassandra and MongoDB.
HS1 instances are optimized for very high storage density, low storage cost, and high sequential I/O performance. HS1 instances give 48 TB of storage capacity across 24 hard disk drives, high network performance, and are capable of supporting throughput performance of as much as 2.6 GBps. These instances are designed for large-scale data warehouses, large always-on Hadoop clusters, and for cluster file systems. Indeed, HS1 instances are the underlying instance type for our petabyte-scale data warehousing service, Amazon Redshift.
Micro Instances. Micro, or T1, instances are a very low-cost instance option providing a small amount of CPU resources. Micro instances may opportunistically increase CPU capacity in short bursts when additional cycles are available. They are well suited for lower throughput applications like bastion hosts or administrative applications, or for low-traffic websites that require additional compute cycles from time to time.
Micro instances are available in the AWS Free Usage Tier to allow you to explore EC2 functionality at no charge. Due to the opportunistic scheduling used by Micro instances, you should not use them for applications that require sustained CPU performance. You can learn more about the characteristics of Micro instances and appropriate workload characteristics in the Amazon EC2 documentation.
GPU Instances. This family includes the CG1 instance type, and allows you to take advantage of the parallel performance of NVidia Tesla GPUs using the CUDA or OpenCL programming models for GPGPU computing. GPU instances also provide high CPU capabilities and support cluster networking. For applications like AMBER, a molecular dynamics application, you can get 4-5x improvement in performance compared to CC2 instances. Many of you are running computational chemistry, rendering, and financial analysis applications on CG1 instances today to take advantage of the speedup you can get from GPGUs.
Your Choice 
I hope that this classification will help you to select the instance type that best fits your application. Because you can launch and terminate instances as desired, profiling and load testing across a variety of instance types is simple and cost effective. Unlike a traditional environment where you are locked in to a particular hardware configuration for an extended period of time, you can easily change instance types as your needs change. You can even profile multiple instance types as part of your Continuous Integration process and use a different set of instance types for each minor release.
The availability of multiple instance types, combined with features like EBS-optimization, and cluster networking allow applications to be optimized for increased performance, improved application resilience, and lower costs.
In particular, you should evaluate the most important performance metrics for your application. For applications that benefit from a low cost per CPU, you should try compute-optimized instances (C1 or CC2) first. For applications that require the lowest cost per GiB of memory, we recommend memory-optimized instances (M2 or CR1). If you are running a database, you should also take advantage of EBS-optimization or instances that support cluster networking. For applications with high inter-node network requirements, you should choose instances that support cluster networking. You can get all the detailed specifications for Amazon EC2 instances types on the EC2 Instance Types Table.
Our goal is to continue to provide you with instance types that address the needs of a broad swath of applications and we welcome feedback on how the currently available instance types are addressing those needs. Post a message in the EC2 forum and we'll make sure that the team sees it.
Hopefully the information provided in this post will help you get your applications revved up right away.
— Jeff (with help from Deepak Singh and Paul Duffy); 
Jeff Barr
Jeff Barr is Chief Evangelist for AWS. He started this blog in 2004 and has been writing posts just about non-stop ever since.
Resources
Getting Started
What's New
Top Posts
Official AWS Podcast
Case Studies
AWS re:Post
Follow
Twitter
Facebook
LinkedIn
Twitch
RSS Feed
Email Updates
Create an AWS account
Learn
What Is AWS?
What Is Cloud Computing?
What Is Agentic AI?
Cloud Computing Concepts Hub
AWS Cloud Security
What's New
Blogs
Press Releases
Resources
Getting Started
Training
AWS Trust Center
AWS Solutions Library
Architecture Center
Product and Technical FAQs
Analyst Reports
AWS Partners
Developers
Builder Center
SDKs & Tools
.NET on AWS
Python on AWS
Java on AWS
PHP on AWS
JavaScript on AWS
Help
Contact Us
File a Support Ticket
AWS re:Post
Knowledge Center
AWS Support Overview
Get Expert Help
AWS Accessibility
Legal
English
Back to top
Amazon is an equal opportunity employer and does not discriminate on the basis of protected veteran status, disability or other legally protected status.        
Privacy
Site terms
Your Privacy Choices
Cookie Preferences
© 2026, Amazon Web Services, Inc. or its affiliates. All rights reserved.
