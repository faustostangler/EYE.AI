---
name: AWS Direct Connect - Amazon Virtual Private Cloud Connectivity Options
keywords: (placeholder)
metadata:
  url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect.html
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
AWS Direct Connect - Amazon Virtual Private Cloud Connectivity Options
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
Unable to save cookie preferences
We will only store essential cookies at this time, because we were unable to save your cookie preferences.
If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.
Dismiss
Skip to main content
English
Preferences
Contact Us
Feedback
Get started
Service guides
Developer tools
AI resources
Create an AWS Account
Amazon Virtual Private Cloud Connectivity Options
AWS Whitepaper
Abstract
Introduction
Network-to-Amazon VPC connectivity options
AWS Site-to-Site VPN
AWS Transit Gateway + Site-to-Site VPN
AWS Direct Connect
AWS Direct Connect + AWS Transit Gateway
AWS Direct Connect + AWS Site-to-Site VPN
AWS Direct Connect + AWS Transit Gateway + AWS Site-to-Site VPN
Site-to-Site VPN CloudHub
AWS Transit Gateway + SD-WAN solutions
Software VPN
Amazon VPC-to-Amazon VPC connectivity options
VPC peering
AWS Transit Gateway
AWS PrivateLink
Software VPN
Software VPN-to-AWS Site-to-Site VPN
Software remote access-to-Amazon VPC connectivity options
AWS Client VPN
Software client VPN
Transit VPC
AWS Cloud WAN
Conclusion
Appendix A: High-Level HA architecture for software VPN instances
Contributors
Document revisions
Notices
Documentation
...
AWS Whitepapers
AWS Whitepaper
Documentation
AWS Whitepapers
AWS Whitepaper
AWS Direct Connect
PDF
RSS
Markdown [-]
Focus mode
On this page
Additional resources
Documentation AWS Whitepapers AWS Whitepaper Additional resources AWS Direct Connect makes it easy to establish a dedicated connection from an on-premises network to one or more VPCs. Direct Connect can reduce network costs, increase bandwidth throughput, and provide a more consistent network experience than internet-based connections. It uses industry-standard 802.1Q VLANs to connect to Amazon VPC using private IP addresses. The VLANs are configured using virtual interfaces (VIFs), and you can configure three different types of VIFs:
Public virtual interface - Establish connectivity between AWS public endpoints and your data center, office, or colocation environment.
Transit virtual interface - Establish private connectivity between AWS Transit Gateway and your data center, office, or colocation environment. This connectivity option is covered in the section AWS Direct Connect + AWS Transit Gateway.
Private virtual interface - Establish private connectivity between Amazon VPC resources and your data center, office, or colocation environment. The use of private VIFs is shown in the following figure. AWS Direct Connect You can establish connectivity to the AWS backbone using AWS Direct Connect by establishing a cross-connect to AWS devices in a Direct Connect location . You can access any AWS Region from any of our Direct Connect locations (except China). If you don't have equipment at a location, you can choose from an ecosystem of WAN service providers for integrating your AWS Direct Connect endpoint in an AWS Direct Connect location with your remote networks. With AWS Direct Connect, you have two types of connection:
Dedicated connections, where a physical ethernet connection is associated with a single customer. You can order port speeds of 1, 10, or 100 Gbps. You might need to work with a partner in the AWS Direct Connect Partner Program to help you establish network circuits between an AWS Direct Connect connection and your data center, office, or colocation environment.
Hosted connections, where a physical ethernet connection is provisioned by an AWS Direct Connect Partner and shared with you. You can order port speeds between 50 Mbps and 10 Gbps. Your work with the Partner in both the Direct Connect connection they established and the network circuits between an AWS Direct Connect connection and your data center, office, or colocation environment. For dedicated connections, you can also use a link aggregation group (LAG) to aggregate multiple connections at a single AWS Direct Connect endpoint. You treat them as a single, managed connection. You can aggregate up to four 1- or 10-Gbps connections, and up to two 100-Gbps connections. When discussing high availability in AWS Direct Connect, we recommend using additional Direct Connect connections. The Direct Connect Resiliency Toolkit offers guidance in building highly resilient network connections between AWS and your data center, office, or colocation environment. The following figure shows you an example of a high-resiliency connectivity option, with two Direct Connect connections terminated in two different Direct Connect locations. Redundant AWS Direct Connect AWS Direct Connect is not encrypted by default. For dedicated connections of 10 or 100 Gbps, you can use MAC security (MACsec) as an encryption option. For connections of 1 Gbps or less, you can create VPN tunnels on top of the connection – this option is covered in AWS Direct Connect + AWS Site-to-Site VPN and AWS Direct Connect + AWS Transit Gateway + AWS Site-to-Site VPN sections. One important resource in AWS Direct Connect is the Direct Connect gateway, which is a globally available resource to enable connections to multiple Amazon VPCs or Transit Gateways across different Regions or AWS accounts. This resource also allows you to connect to any participating VPC or Transit Gateway from one private VIF or transit VIF, reducing AWS Direct Connect management, as shown in the following figure. AWS Direct Connect Gateway Regarding IP addressing, AWS Direct Connect virtual interfaces support both IPv4 and IPv6 BGP sessions for dual-stack operation.
Private and transit VIFs IPv4 configuration make use of either AWS-generated IPv4 addresses or addresses configured by you. For public VIFs IPv4 BGP peering, you must specify an unique public /31 IPv4 CIDR that you own (or submit a request to have a CIDR block assigned).
For all types of VIFs IPv6 BGP peering, AWS assigns a /125 CIDR, which is not configurable.
Additional resources
AWS Direct Connect User Guide
AWS Direct Connect virtual interfaces
AWS Direct Connect gateways
AWS Direct Connect Resiliency Toolkit
AWS Direct Connect MAC Security
AWS Direct Connect locations
AWS Direct Connect Delivery Partners Javascript is disabled or is unavailable in your browser. To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions. Document Conventions AWS Transit Gateway + Site-to-Site VPN AWS Direct Connect + AWS Transit Gateway Did this page help you? - Yes Thanks for letting us know we're doing a good job! If you've got a moment, please tell us what we did right so we can do more of it. Did this page help you? - No Thanks for letting us know this page needs work. We're sorry we let you down. If you've got a moment, please tell us how we can make the documentation better.
Did this page help you? Yes No Provide feedback
Next topic:
AWS Direct Connect + AWS Transit Gateway
Previous topic:
AWS Transit Gateway + Site-to-Site VPN
Get Started
AWS Hands-On Tutorials
AWS Solutions Library
AWS Decision Guides
Service Guides
Choosing a generative AI service
AWS service guides
AWS CLI Tutorials on GitHub
Developer Tools
AWS Code Example Library
AWS CLI
AWS Builder Center
AWS Developer Tools Blog
Helpful Links
Download the AWS Docs MCP Server
Sign into the AWS Console
AWS re:Post
Privacy
Site terms
Cookie preferences
© 2026, Amazon Web Services, Inc. or its affiliates. All rights reserved.
English
Language selector
Top
A diagram example that shows a high-resiliency connectivity option.
Close
Diagram that shows connecting to any participating VPC or Transit Gateway from one private VIF or transit VIF.
Close
Diagram showing AWS Direct Connect.
Close
