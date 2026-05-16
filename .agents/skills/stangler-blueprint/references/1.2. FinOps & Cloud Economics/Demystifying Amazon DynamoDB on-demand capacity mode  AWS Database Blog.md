---
name: Demystifying Amazon DynamoDB on-demand capacity mode | AWS Database Blog
keywords: (placeholder)
metadata:
  url: https://aws.amazon.com/blogs/database/demystifying-amazon-dynamodb-on-demand-capacity-mode/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Demystifying Amazon DynamoDB on-demand capacity mode | AWS Database Blog
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
AWS Database Blog
Demystifying Amazon DynamoDB on-demand capacity mode
by Esteban Serna Parra on 10 MAR 2025 in Amazon DynamoDB, Best Practices, Intermediate (200) Permalink Comments Share
 https://aws.amazon.com/blogs/database/demystifying-amazon-dynamodb-on-demand-capacity-mode/
As AWS Solutions Architects, we regularly work with customers to optimize their Amazon DynamoDB deployments. Through these engagements, we've identified several common misconceptions about on-demand throughput mode that often prevent teams from making optimal choices for their workloads. While on-demand capacity mode can significantly reduce operational complexity, questions persist about its cost-effectiveness, performance, and operational characteristics.
In this post, we examine the realities behind common myths about DynamoDB on-demand capacity mode across three key areas: cost implications and efficiency, operational overhead and management, and performance considerations. We provide practical guidance to help you make informed decisions about throughput management.
Examining cost-related misconceptions
There are three common myths about DynamoDB on-demand capacity costs that we frequently encounter:
Myth 1: Per-request price for on-demand is always more expensive than provisioned mode.
The per-request price for provisioned capacity is directly co-related to table-level utilization, which refers to how much of the provisioned throughput is actually being consumed by your calculation. For example, if you're only using 20% of the capacity you have pre-allocated with standard provisioned mode, you're effectively paying five times more per request than the base rate. On the other hand, if your table-level utilization is 75%, you are still paying 33% higher than the base rate. It's highly unlikely you are fully-utilizing your provisioned capacity units because production applications generally require providing a buffer to handle variable workloads or traffic patterns that evolve over time. With provisioned capacity, you are also responsible for scaling up and down to account for traffic patterns and to think about capacity-planning for your database, whereas with on-demand mode you are always 100% utilized due to pay-per-request billing and on-demand scales transparently, without needing to specify a scaling policy.
The true cost of running DynamoDB tables on on-demand vs. provisioned capacity extends beyond the simple per-request pricing comparison. Teams must also consider Total Cost of Ownership (TCO), which includes engineering time for capacity management, over-provisioning for peak demands, and ongoing operational overhead for monitoring and adjusting auto-scaling settings. When factoring in both utilization patterns and these operational costs, on-demand mode often proves more economical, especially for variable workloads or development environments where precise capacity planning is challenging. Learn more about the DynamoDB on-demand throughput price reduction in November 2024.
Myth 2: It is always cheaper to use provisioned mode with auto-scaling.
The reality is that you reduce costs when you move provisioned mode tables with less than 30% utilization to on-demand mode. This myth oversimplifies the cost dynamics of auto-scaling as the cost-effectiveness of provisioned mode with auto-scaling depends on your workload patterns and how accurately you can predict and manage capacity.
Auto-scaling has inherent limitations that affect costs. You pay for allocated capacity whether you use it or not, and scaling down unused capacity isn't immediate—it requires a minimum 15-minute period of lower usage, with up to 30 minutes between scale-downs. This delay means you continue paying for higher provisioned capacity even after your workload decreases. When you account for these scaling constraints and total cost of ownership (TCO) factors, provisioned mode with auto-scaling isn't always the most cost-effective choice.
Myth 3: On-demand mode charges you for unused capacity.
Unlike provisioned capacity mode, where you pay for a fixed amount of throughput regardless of usage, with on-demand mode's simple, pay-per-request pricing model, you don't have to worry about idle capacity because you only pay for the capacity you actually use. You are billed per read or write request, so your costs directly reflect your actual usage. There are no charges for maintaining scaling capability or idle capacity, and no minimum capacity requirements.
To optimize costs in either mode, Amazon CloudWatch provides comprehensive metrics for monitoring usage patterns. You can configure maximum throughput settings to control upper limits and implement AWS Budgets for cost tracking. For read-heavy workloads, consider implementing DynamoDB Accelerator (DAX) to reduce costs through caching.
Performance and scaling myths
While cost considerations are important, performance and scaling capabilities often raise equally important questions. When discussing DynamoDB performance, we often hear three misconceptions:
Myth 4: On-demand tables have a slower response time.
The first misconception is based on a misunderstanding of the architecture of DynamoDB. In reality, DynamoDB delivers consistent single-digit millisecond latency regardless of your chosen throughput mode. When you select on-demand mode, you're not changing the underlying infrastructure or performance characteristics—you are adjusting how you manage and pay for capacity. Both modes use the same high-performance infrastructure and offer identical enterprise-ready features.
Myth 5: On-demand tables won't scale higher than 40,000 read and write capacity units.
While new tables start with a default quota of 40,000 read capacity units (RCUs) and write capacity units (WCUs), this isn't a hard limit. Through the Service Quotas console, you can request increases to the level you need. We regularly work with customers operating at hundreds of thousands or even millions of capacity units. The following figure is an example of a quota increase for write capacity units from the default quota of 40,000 WCU to 120,000 WCU. 
Myth 6: You can't scale beyond twice your previous peak.
This myth requires understanding how on-demand scaling works. New on-demand tables start with capacity for 4,000 writes per second and 12,000 reads per second. From there, DynamoDB automatically accommodates up to double your previous peak traffic within a 30-minute window. For example, if your previous peak was 50,000 reads per second, DynamoDB instantly handles up to 100,000 reads per second. Once you sustain that new level, it becomes your peak, enabling scaling to 200,000 reads per second.
If you know you'll need to scale beyond twice your previous peak, you can set your desired warm throughput value ahead of time, as shown in the following figure. This eliminates the need to gradually scale up and makes sure that your table can immediately handle your target workload. For unplanned scaling beyond twice your previous peak, DynamoDB continues to add capacity as your traffic increases, but you should plan to implement this growth at least 30 minutes in advance to avoid throttling. 
CloudWatch metrics are available to help you understand your application's scaling patterns and plan for growth. Work with your AWS account team to plan for maintaining consistent performance during larger scaling events.
Operational myths
After addressing performance and scaling, let's examine three persistent myths about operational aspects of on-demand tables:
Myth 7: You can't control on-demand consumption.
While DynamoDB automatically handles scaling in on-demand mode, you retain significant control over your table's operation. Through the AWS Management Console, you can set maximum throughput limits to protect downstream systems and control costs. Here's how the write request units work:
Default limit: 40,000 write request units
Additional approved capacity: 80,000 write request units
Total available capacity: 120,000 write request units
In this example, although the account has been approved for up to 120,000 write request units, we're setting a maximum limit of 100,000 units to establish predictable cost boundaries while maintaining substantial scaling headroom, as shown in the following figure. 
Myth 8: On-demand tables need to be pre-warmed frequently.
Pre-warming is not a regular necessity for on-demand tables, but it can be crucial for handling significant, anticipated traffic spikes. DynamoDB's on-demand mode is designed to handle most traffic fluctuations automatically. However, there are scenarios where pre-warming provides a distinct advantage. Here's the key difference: With pre-warming, your table can be immediately ready to handle an anticipated load surge. Without it, scaling happens gradually – for example, if your gaming application typically handles 50,000 requests per second and you need to handle 250,000 requests during an event, your table would need to scale in steps: first to 100,000 requests, wait 30 minutes, then to 200,000 requests, and after another 30 minutes reach 400,000 requests. That's a full hour before reaching the needed capacity. The good news is that once you pre-warm once, DynamoDB maintains that capacity for future similar traffic patterns – including regular weekly events at that scale. You won't need to pre-warm again unless you expect traffic significantly higher than your new peak.
Myth 9: Changing table capacity requires downtime.
You can switch between provisioned and on-demand modes once every 24 hours without experiencing any downtime. During the transition, which typically takes several minutes, your table remains fully available for read and write operations. The switch preserves all your table configurations, including global secondary indexes, monitoring settings, and backup configurations.
One of the key benefits of on-demand mode is the reduced need for active monitoring and management. Your teams can focus on building features and improving applications rather than frequently reviewing and adjusting capacity settings.
Common implementation misconceptions
After addressing operational concerns, let's examine two final misconceptions about on-demand table usage:
Myth 10: On-demand tables will fix my throttling.
Switching to on-demand mode doesn't automatically eliminate all throttling concerns. While on-demand mode significantly reduces throttling concerns through automated capacity management, certain fundamental limits still apply. DynamoDB maintains partition-level throughput limits—3,000 RCUs and 1,000 WCUs per partition—to ensure consistent performance across all tables. These hardware-level limits apply regardless of your chosen capacity mode.
In our customer engagements, we frequently encounter throttling caused by partition key design, both in base tables and global secondary indexes (GSIs). For example, an order processing system might use timestamps as partition keys in the base table, while a GSI tracks order status using a small set of possible values such as pending, processing, and completed. During high-traffic events such as flash sales, both the base table and the GSI can experience throttling as writes independently concentrate on single partitions. The solution involves implementing distributed partition key strategies—such as combining timestamps with product categories in the base table and adding more granular values to GSI keys to improve their distribution.
Myth 11: On-demand mode is only for spiky workloads.
On-demand mode's flexibility extends far beyond just handling spiky traffic patterns. While on-demand capacity excels at handling variable workloads, its benefits extend to many different usage patterns. Consider an ecommerce platform where order processing handles variable traffic, customer profiles maintain steady access patterns, and inventory updates run as periodic batch processes. On-demand mode effectively serves all these components, reducing operational overhead across the entire application.
Development and operations teams benefit from this flexibility throughout the application lifecycle. During development and testing, teams can focus on building features instead of managing capacity. In production, teams spend less time on capacity planning and more time improving application functionality. The key advantage isn't just handling spiky workloads; it's the overall reduction in operational complexity and the ability to automatically adapt to your application's needs.
Conclusion and next steps
Throughout this post, we've examined several common myths about Amazon DynamoDB on-demand throughput mode and provided clarity about its actual capabilities. The total cost of ownership often proves more economical when considering operational overhead and elimination of over-provisioning. On-demand tables provide the same consistent, single-digit millisecond performance as provisioned capacity, with the added benefit of automatic scaling beyond default quotas. You maintain significant control over your tables while eliminating the complexity of capacity management and pre-warming activities.
Based on our experience helping customers across various industries optimize their DynamoDB implementations, we recommend evaluating capacity modes based on your specific workload characteristics and operational requirements. Successful implementations focus on workload patterns, operational efficiency, and actual usage rather than common assumptions about capacity modes.
To get started with DynamoDB on-demand capacity mode, visit the Amazon DynamoDB console to create your first on-demand table, or review the DynamoDB Developer Guide to learn about capacity mode best practices. Read Amazon DynamoDB re:Invent 2024 recap | AWS Database Blog to see interesting presentations you might have missed.
About the Author
Esteban Serna, Principal DynamoDB Specialist Solutions Architect, is a database enthusiast with 15 years of experience. From deploying contact center infrastructure to falling in love with NoSQL, Esteban's journey led him to specialize in distributed computing. Today, he helps customers design massive-scale applications with single-digit millisecond latency using DynamoDB. Passionate about his work, Esteban loves nothing more than sharing his knowledge with others.
Like (2)(2)
Share
1 Comment
Log in to comment Log in
Sort by: Top
IG
Iván García
Mar 12, 2025
Great blog, thank you!
Like (0)
Reply (0)
Share
Resources
Getting Started
What's New
Blog Topics
Amazon Aurora
Amazon DocumentDB
Amazon DynamoDB
Amazon ElastiCache
Amazon Keyspaces (for Apache Cassandra)
Amazon Managed Blockchain
Amazon MemoryDB for Redis
Amazon Neptune
Amazon Quantum Ledger Database (Amazon QLDB)
Amazon RDS
Amazon Timestream
AWS Database Migration Service
AWS Schema Conversion Tool
Follow
Twitter
Facebook
LinkedIn
Twitch
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
