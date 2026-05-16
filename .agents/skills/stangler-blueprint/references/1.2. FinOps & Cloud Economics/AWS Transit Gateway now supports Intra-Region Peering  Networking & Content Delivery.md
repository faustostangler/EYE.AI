---
name: AWS Transit Gateway now supports Intra-Region Peering | Networking & Content Delivery
keywords: (placeholder)
metadata:
  url: https://aws.amazon.com/blogs/networking-and-content-delivery/aws-transit-gateway-now-supports-intra-region-peering/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
AWS Transit Gateway now supports Intra-Region Peering | Networking & Content Delivery
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
Networking & Content Delivery
AWS Transit Gateway now supports Intra-Region Peering
by Evgeny Vaganov and Shridhar Kulkarni on 01 DEC 2021 in Announcements, AWS Partner Network, AWS Transit Gateway, Networking & Content Delivery Permalink Share
 https://aws.amazon.com/blogs/networking-and-content-delivery/aws-transit-gateway-now-supports-intra-region-peering/
Update: Sep 9, 2024 – Expanded 'Things to know' section with additional cost considerations
Introduction
When we first released AWS Transit Gateway in 2018, it started with support for Amazon Virtual Private Cloud (Amazon VPC) and Site-to-Site VPN attachments. Customers loved the simplicity of deploying hub-and-spoke architectures, built-in resiliency and high availability, and the ability to scale to thousands of attachments using a single gateway. Thereafter we followed with additional connectivity options on Transit Gateway including AWS Direct Connect attachment, inter-region peering which enabled customers to build global networks on AWS, and Transit Gateway Connect which allowed Transit Gateways to natively peer with SD-WAN appliances and third-party virtual routers. One interesting deployment pattern that emerged with our customers was to deploy multiple Transit Gateways in the same AWS Region. These customers have been asking us to implement an easy way to interconnect and route traffic between these Transit Gateways in the same AWS Region. Today we are happy to announce the availability of Transit Gateway intra-region peering which enables customers to establish peering connections between Transit Gateways in the same AWS Region.
With intra-region peering capability, customers no longer need to create bridge VPCs between multiple transit gateways or attach a single VPC to multiple Transit Gateways for routing traffic between different Transit Gateways in the same AWS Region. Intra-region peering simplifies routing and inter-connectivity between VPCs and on-premises networks that are serviced and managed via separate Transit Gateways. This feature allows customers the flexibility to deploy multiple Transit Gateways with separate administrative domains, while providing an easy way to interconnect these Transit Gateways in a more native manner. Using intra-region peering, you can build flexible network topologies and easily integrate your network with a third-party or partner managed network in the same AWS Region. If you are already familiar with Transit Gateway inter-region peering, it works exactly the same way except that the peered Transit Gateways are in the same AWS Region.
Use cases
Following are some of the most typical use-cases for this feature.
Connectivity to partner managed networks. In this use-case, customers may want to connect their own Transit Gateway to another Transit Gateway that belongs to a third-party entity. This third-party entity could be a technology partner, a managed services provider or an Independent Software Vendor (ISV) who is operating their own Transit Gateway based network in AWS. A great example is VMware Transit Connect (VTC), a part of VMware Cloud on AWS (VMC) managed service offering that allows customers to deploy VMware's SDDC (Software-Defined Data Center) platform in AWS cloud. Customers can now use intra-region peering to connect their own Transit Gateway to VTC. Figure 1 below depicts a scenario where customers can directly peer their Transit Gateway to a third-party Transit Gateway and provide interconnectivity between the two networks in the same AWS Region. 
Figure 1: Intra-region Transit Gateway peering
Organizations with independent network teams. Many large organizations have teams with separate administrative domains managing their own independent networks in AWS (Teams owning Prod, Non-prod, Test and Staging environments, Independent Business Units, Mergers & Acquisitions etc). These teams operate in the same AWS Region but prefer to create their own Transit Gateways for administrative ease-of-use, segregate control plane operations and reduce human induced configuration errors. Intra-region peering enables these teams to easily peer their Transit Gateways with each other and provide connectivity between shared workloads within AWS.
Inter-divisional networks using AWS as a backbone. This use-case involves a large parent organization providing AWS backbone connectivity to multiple client divisions running their own separate networks. Such divisions can operate fairly independently in different geographies and AWS Regions. The parent organization builds an inter-divisional network (IDN) using Transit gateways and AWS as a backbone. Each client division will have its own Transit Gateway in AWS Regions where they operate along with their VPCs and security infrastructure. Intra-region peering allows direct connectivity between divisional Transit Gateways in every AWS Region to the IDN Transit Gateway owned by parent organization for global network connectivity.
AWS Managed Services (AMS) helps you operate your AWS infrastructure more efficiently and securely. AMS managed landing zone comes with a managed Transit Gateway for network integration of VPCs under AMS management. You may have both self-managed AWS environments and AMS managed AWS environments operating side by side. Intra-region peering helps you solve connectivity requirements between AMS and self-managed AWS networks.
Things to know
Configuration steps and requirements for intra-region Transit Gateway peering are exactly the same as for inter-region peering. You can create a 'peering' attachment between your Transit Gateway and another Transit Gateway in the same AWS Region. The peered Transit Gateway can be in your own AWS account or a different AWS account.
We recommend to give each AWS Transit Gateway a unique Autonomous System Number (ASN).
Peering attachment supports static routing. You can associate a route-table to the peering attachment or use the default Transit Gateway route-table. You can point routes in Transit Gateway route tables to the peering attachment for routing traffic between the peered Transit Gateways. You can also use customer-managed prefix lists to simplify IP management in Transit Gateway route-tables. As a best practice, only create routing entries for prefixes that you want to communicate within the peer network. Also, add blackhole routes in the peering attachment route table for prefixes you don't want the other side to be able to communicate to.
Transit Gateway peering does not support resolving public or private IPv4 DNS host names to private IPv4 addresses across VPCs on either side of the Transit Gateway peering attachment.
High Availability (HA) is not a valid use-case for Transit Gateway intra-region peering. Transit Gateway is built upon AWS Hyperplane, a highly reliable and horizontally scalable distributed switching fabric, and as such the service has built-in High Availability. Deploying multiple Transit Gateways in a AWS Region with intra-peering is neither required nor necessary for a better HA design.
While you can deploy flexible topologies to fit your use-case, we recommend setting up a full mesh architecture if you have multiple Transit Gateways as shown in Figure 2 below. 
Figure 2: Intra-region peering mesh when 3 or more Transit Gateways are peered
For some of the earlier mentioned use cases, the other side of peering connection may be semi-trusted or untrusted network. In this case, you may require a centralized network traffic inspection point which could be facilitated by either AWS Network Firewall or a AWS Gateway Load Balancer based inspection VPC pattern. Using static routes in the route-table associated with the intra-region peering attachment you can steer traffic coming from the third-party transit gateway to the security inspection VPC. Make sure to set appliance mode to “enable” on the inspection VPC's Transit Gateway attachment to keep traffic symmetry in both directions as shown in Figure 3 below. 
Figure 3: Traffic inspection point added to centrally protect the network
If you operate in multiple AWS Regions and also have multiple Transit Gateways in each AWS Region, you can build a full mesh of Transit Gateways. At scale, you may end up managing many peerings and our recommendation is to consider a hub approach as shown below in Figure 4. The hub approach allows you to control traffic between AWS Regions and potentially between different divisions from a single connectivity hub in each AWS Region. 
Figure 4: Inter-region peering mesh with multiple AWS Regions
You can view attachment-level AWS CloudWatch metrics such as BytesIn, BytesOut, PacketsIn, PacketsOut, PacketDropCountBlackhole, PacketDropCountNoRoute for monitoring traffic on both intra-region and inter-region peering attachments. Additionally, you can use AWS Network Manager for advanced visibility and monitoring of your Transit Gateway topology and global network deployments.
There is a Transit Gateway attachment-hour charge for peering attachments, and it is the same for both intra-region and inter-region peering attachments. Transit Gateway data processing charges apply to the sender attachment such as VPC, AWS Site-to-Site VPN, and AWS Direct Connect. There are no data processing charges for data sent from a peering attachment to a Transit Gateway. Data transfer charges for intra-region and inter-region traffic still apply and are covered on the EC2 Pricing Page.
Conclusion
With intra-region peering, you can now connect Transit Gateways created by different AWS accounts, and also in different AWS Organizations, within the same AWS Region. AWS Transit Gateway allows you to insert a network service, such as a network firewall, into a network path as required. You no longer need the workarounds for connectivity to multiple Transit Gateways and can create a more cost-efficient architecture. 
Shridhar Kulkarni
Shridhar is part of Amazon Virtual Private Cloud (VPC) team and leads Product Management for the AWS Transit Gateway service. Shridhar has a strong and diverse technology background with expertise in Cloud, SAAS, Mobile, SD-WAN, Virtualization, WAN Optimization, SDN, Data Networking (L1-L7), VoIP, Cable, FTTH, and x86 hardware platforms. Shridhar has a proven track record of launching cutting-edge high-tech products and services to Cloud, Enterprise, Service Provider and SMB customers worldwide. Shridhar has a Master's degree in Computer Science and MBA from UCLA Anderson School of Management. 
Evgeny Vaganov
Evgeny Vaganov is a Head of Networking SAs across Asia Pacific and Japan (APJ) region. Prior to this role, Evgeny supported customers across Australia and New Zealand adopting Cloud. Passionate about learning and experimenting, he has a goal of making Cloud networking simpler for everyone.
TAGS: Amazon VPC, AWS Transit Gateway, Networking
Resources
Networking Products
Getting Started
Amazon CloudFront
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
