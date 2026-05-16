---
name: Overview of Data Transfer Costs for Common Architectures - AWS
keywords: (placeholder)
metadata:
  url: https://aws.amazon.com/blogs/architecture/overview-of-data-transfer-costs-for-common-architectures/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Overview of Data Transfer Costs for Common Architectures | AWS Architecture Blog
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
AWS Architecture Blog
Overview of Data Transfer Costs for Common Architectures
by Birender Pal, Sebastian Gorczynski, and Dennis Schmidt on 30 JUN 2021 in Amazon EC2, Amazon RDS, Architecture, AWS Direct Connect, AWS Site-to-Site VPN, AWS Transit Gateway Permalink Share
 https://aws.amazon.com/blogs/architecture/overview-of-data-transfer-costs-for-common-architectures/
Data transfer charges are often overlooked while architecting a solution in AWS. Considering data transfer charges while making architectural decisions can help save costs. This blog post will help identify potential data transfer charges you may encounter while operating your workload on AWS. Service charges are out of scope for this blog, but should be carefully considered when designing any architecture.
Data transfer between AWS and internet
There is no charge for inbound data transfer across all services in all Regions. Data transfer from AWS to the internet is charged per service, with rates specific to the originating Region. Refer to the pricing pages for each service—for example, the pricing page for Amazon Elastic Compute Cloud (Amazon EC2)—for more details.
Data transfer within AWS
Data transfer within AWS could be from your workload to other AWS services, or it could be between different components of your workload.
Data transfer between your workload and other AWS services
When your workload accesses AWS services, you may incur data transfer charges.
Accessing services within the same AWS Region
If the internet gateway is used to access the public endpoint of the AWS services in the same Region (Figure 1 – Pattern 1), there are no data transfer charges. If a NAT gateway is used to access the same services (Figure 1 – Pattern 2), there is a data processing charge (per gigabyte (GB)) for data that passes through the gateway.
Figure 1. Accessing AWS services in same Region
Accessing services across AWS Regions
If your workload accesses services in different Regions (Figure 2), there is a charge for data transfer across Regions. The charge depends on the source and destination Region (as described on the Amazon EC2 Data Transfer pricing page).
Figure 2. Accessing AWS services in different Region
Data transfer within different components of your workload
Charges may apply if there is data transfer between different components of your workload. These charges vary depending on where the components are deployed.
Workload components in same AWS Region
Data transfer within the same Availability Zone is free. One way to achieve high availability for a workload is to deploy in multiple Availability Zones.
Consider a workload with two application servers running on Amazon EC2 and a database running on Amazon Relational Database Service (Amazon RDS) for MySQL (Figure 3). For high availability, each application server is deployed into a separate Availability Zone. Here, data transfer charges apply for cross-Availability Zone communication between the EC2 instances. Data transfer charges also apply between Amazon EC2 and Amazon RDS. Consult the Amazon RDS for MySQL pricing guide for more information.
Figure 3. Workload components across Availability Zones
To minimize impact of a database instance failure, enable a multi-Availability Zone configuration within Amazon RDS to deploy a standby instance in a different Availability Zone. Replication between the primary and standby instances does not incur additional data transfer charges. However, data transfer charges will apply from any consumers outside the current primary instance Availability Zone. Refer to the Amazon RDS pricing page for more detail.
A common pattern is to deploy workloads across multiple VPCs in your AWS network. Two approaches to enabling VPC-to-VPC communication are VPC peering connections and AWS Transit Gateway. Data transfer over a VPC peering connection that stays within an Availability Zone is free. Data transfer over a VPC peering connection that crosses Availability Zones will incur a data transfer charge for ingress/egress traffic (Figure 4).
Figure 4. VPC peering connection
Transit Gateway can interconnect hundreds or thousands of VPCs (Figure 5). Cost elements for Transit Gateway include an hourly charge for each attached VPC, AWS Direct Connect, or AWS Site-to-Site VPN. Data processing charges apply for each GB sent from a VPC, Direct Connect, or VPN to Transit Gateway.
Figure 5. VPC peering using Transit Gateway in same Region
Workload components in different AWS Regions
If workload components communicate across multiple Regions using VPC peering connections or Transit Gateway, additional data transfer charges apply. If the VPCs are peered across Regions, standard inter-Region data transfer charges will apply (Figure 6).
Figure 6. VPC peering across Regions
For peered Transit Gateways, you will incur data transfer charges on only one side of the peer. Data transfer charges do not apply for data sent from a peering attachment to a Transit Gateway. The data transfer for this cross-Region peering connection is in addition to the data transfer charges for the other attachments (Figure 7).
Figure 7. Transit Gateway peering across Regions
Data transfer between AWS and on-premises data centers
Data transfer will occur when your workload needs to access resources in your on-premises data center. There are two common options to help achieve this connectivity: Site-to-Site VPN and Direct Connect.
Data transfer over AWS Site-to-Site VPN
One option to connect workloads to an on-premises network is to use one or more Site-to-Site VPN connections (Figure 8 – Pattern 1). These charges include an hourly charge for the connection and a charge for data transferred from AWS. Refer to Site-to-Site VPN pricing for more details. Another option to connect multiple VPCs to an on-premises network is to use a Site-to-Site VPN connection to a Transit Gateway (Figure 8 – Pattern 2). The Site-to-Site VPN will be considered another attachment on the Transit Gateway. Standard Transit Gateway pricing applies.
Figure 8. Site-to-Site VPN patterns
Data transfer over AWS Direct Connect
Direct Connect can be used to connect workloads in AWS to on-premises networks. Direct Connect incurs a fee for each hour the connection port is used and data transfer charges for data flowing out of AWS. Data transfer into AWS is $0.00 per GB in all locations. The data transfer charges depend on the source Region and the Direct Connect provider location. Direct Connect can also connect to the Transit Gateway (via Direct Connect Gateway) if multiple VPCs need to be connected (Figure 9). Direct Connect is considered another attachment on the Transit Gateway and standard Transit Gateway pricing applies. Refer to the Direct Connect pricing page for more details.
Figure 9. Direct Connect patterns.jpg
A Direct Connect gateway can be used to share a Direct Connect across multiple Regions. When using a Direct Connect gateway, there will be outbound data charges based on the source Region and Direct Connect location (Figure 10).
Figure 10. Direct Connect gateway
General tips
Data transfer charges apply based on the source, destination, and amount of traffic. Here are some general tips for when you start planning your architecture:
Avoid routing traffic over the internet when connecting to AWS services from within AWS by using VPC endpoints:
VPC gateway endpoints allow communication to Amazon S3 and Amazon DynamoDB without incurring data transfer charges within the same Region.
VPC interface endpoints are available for some AWS services. This type of endpoint incurs hourly service charges and data transfer charges.
Use Direct Connect instead of the internet for sending data to on-premises networks.
Traffic that crosses an Availability Zone boundary typically incurs a data transfer charge. Use resources from the local Availability Zone whenever possible.
Traffic that crosses a Regional boundary will typically incur a data transfer charge. Avoid cross-Region data transfer unless your business case requires it.
Use the AWS Free Tier. Under certain circumstances, you may be able to test your workload free of charge.
Use the AWS Pricing Calculator to help estimate the data transfer costs for your solution.
Use a dashboard to better visualize data transfer charges – this workshop will show how.
Conclusion
AWS provides the ability to deploy across multiple Availability Zones and Regions. With a few clicks, you can create a distributed workload. As you increase your footprint across AWS, it helps to understand various data transfer charges that may apply. This blog post provided information to help you make an informed decision and explore different architectural patterns to save on data transfer costs.
Related posts
Exploring Data Transfer Costs for AWS Managed Databases 
Birender Pal
Birender is a Senior Solutions Architect at AWS, where he works with strategic enterprise users to design scalable, secure and resilient cloud architectures. He supports digital transformation initiatives with a focus on cloud-native modernization, machine learning, and generative AI. Outside of work, Birender enjoys experimenting with recipes from around the world. 
Sebastian Gorczynski
Sebastian Gorczynski is a Solutions Architect who works with enterprise companies. He is passionate about helping customers to innovate and design scalable, well-architected solutions on the AWS Cloud. Sebastian is based out of New York City and outside of work loves spending time with his family and friends. 
Dennis Schmidt
Dennis Schmidt is a Solutions Architect based in Rochester, New York. He works with Greenfield customers, helping them get started on their cloud journey with AWS, and is passionate about containers, serverless, and cost optimization. Outside of work, Dennis enjoys spending time with family and attending various sporting events.
Resources
AWS Architecture Center
AWS Well-Architected
AWS Architecture Monthly
AWS Whitepapers
AWS Training and Certification
This Is My Architecture
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
