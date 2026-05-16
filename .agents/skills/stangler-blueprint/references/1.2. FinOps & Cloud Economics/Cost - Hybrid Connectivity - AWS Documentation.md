---
name: Cost - Hybrid Connectivity - AWS Documentation
keywords: (placeholder)
metadata:
  url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/cost.html
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Cost - Hybrid Connectivity
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
Hybrid Connectivity
AWS Whitepaper
Abstract and introduction
AWS hybrid connectivity building blocks
Hybrid network connections
AWS hybrid connectivity services
Hybrid connectivity type and design considerations
Connectivity type selection
Time to deploy
Security
Service level agreement
Performance
Cost
Connectivity design selection
Scalability
Connectivity models
AWS Accelerated Site-to-Site VPN – AWS Transit Gateway, Single AWS Region
AWS DX – DXGW with VGW, Single Region
AWS DX – DXGW with VGW, Multi-Regions, and AWS Public Peering
AWS DX – DXGW with AWS Transit Gateway, Multi-Regions, and AWS Public Peering
AWS DX – DXGW with AWS Transit Gateway, Multi-Regions (more than 3)
Reliability
Customer-managed VPN and SD-WAN
Example Corp. Automotive use case
Architecture selected
Conclusion
Contributors
Further reading
Document revisions
Notices
AWS Glossary
Documentation
...
AWS Whitepapers
AWS Whitepaper
Documentation
AWS Whitepapers
AWS Whitepaper
Cost
PDF
RSS
Markdown [-]
Focus mode
On this page
Definition
Key questions
Capabilities to consider
Decision matrix
Documentation AWS Whitepapers AWS Whitepaper Definition Key questions Capabilities to consider Decision matrix This whitepaper is for historical reference only. Some content might be outdated and some links might not be available. This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.
Definition
In the cloud, the cost of hybrid connectivity includes the cost of provisioned resources and usage. Cost of provisioned resources is measured in units of time, usually hourly. Usage is for data transfer and processing usually measured to in gigabytes (GB). Other costs include the cost of connectivity to the AWS network point of presence. If your network is within the same colocation facility, it might be as little as the cost of a cross connect. If your network is in a different location, there will be a service provider or APN Direct Connect partner costs involved.
Key questions
How much data do you anticipate sending into AWS per month from your facility and from the internet?
How much data do you anticipate sending from AWS per month to your facility and to the internet?
How often will these amounts change?
What changes in a failure scenario?
Capabilities to consider
If you have bandwidth-heavy workloads that you wish to run on AWS, AWS Direct Connect can reduce your network costs into and out of AWS in two ways. First, by transferring data to and from AWS directly, you can reduce your bandwidth costs paid to your internet service provider. Second, all data transferred over your dedicated connection is charged at the reduced AWS Direct Connect data transfer rate, rather than internet data transfer rates – see the Direct Connect pricing page for details. AWS Direct Connect allows the use of AWS Direct Connect SiteLink to interconnect your sites using the AWS backbone – see the SiteLink launch blog for more information. Leveraging this capability incurs normal Direct Connect data transfer costs, along with a charge per hour SiteLink is enabled. You can enable and disable SiteLink on-demand, and it may be a good option for failure scenarios involving the internet or private network connectivity. If you are using a network service provider for connectivity between on-premises and a Direct Connect location, your ability and the time needed to change your bandwidth commitments is based on your contract with the service provider. The AWS backbone can deliver your traffic to any AWS Region except China from any AWS network point of presence. This capability has many technical benefits over using the internet to access remote AWS Regions, but has a cost – see the EC2 Data Transfer pricing page for details. If there is an AWS Transit Gateway in the traffic path, it adds data processing cost per GB, however if using inter-region peering between two Transit Gateways, you are only billed once for the Transit Gateway data processing. Optimal application design keeps data processing within AWS and minimizes unnecessary data egress charges. Data ingress to AWS is free.
Note
As part of the overall connectivity solution, in addition to the AWS connection cost, you should also consider cost of the end-to-end connectivity including service provider cost, cross connects, racks, and equipment within DX location (if required). If you are not sure if you should use the internet or a private connection, calculate a breakeven point where AWS Direct Connect becomes less expensive than using the internet. If the volume of data means that AWS Direct Connect is less expensive, and you require permanent connectivity, AWS Direct Connect is the optimal connectivity choice. If the connectivity is temporary and the internet meets other requirements, it can be cheaper to use AWS S2S VPN over the internet due to the elasticity of the internet. Note this requires that you have sufficient internet connectivity from your on-premises network. If you are within a facility which has AWS Direct Connect (the list is available on the Direct Connect website ), you can establish a cross-connect to AWS. This means using dedicated connections at 1,10, or 100Gbps. AWS Direct Connect partners offer more bandwidth options and smaller capacities, which may optimize your connectivity cost. For example, you can start at a 50 Mbps Hosted Connection versus a 1 Gbps Dedicated Connection. With AWS Transit Gateway, you can share your VPN and Direct Connect connections with many VPCs. While you are charged for the number of connections that you make to the AWS Transit Gateway per hour and the amount of traffic that flows through AWS Transit Gateway, it simplifies management and reduces the number of VPN connections and VIFs required. The benefits and cost savings of lower operational overhead can easily outweigh the additional cost of data processing. Optionally, you can consider a design where AWS Transit Gateway is in the traffic path to most VPCs, but not all. This approach avoids the AWS Transit Gateway data processing fees for use cases where you need to transfer large amounts of data into AWS. Refer to the Connectivity Models section for further details on this design. Another approach is to combine AWS Direct Connect as a primary path with AWS S2S VPN over the internet as backup/failover path. While technically feasible and very cost effective, this solution has technical downsides (discussed in the Reliability section of this whitepaper) and can be more difficult to manage. AWS doesn't recommend this for highly critical or critical workloads . The final approach is a customer-managed VPN or SD-WAN deployed in Amazon EC2 instance(s). This can be cheaper at scale if there are tens to hundreds of site when compared to AWS S2S VPN. However, there is management overhead, licensing costs, and EC2 resource cost for each virtual appliance to consider.
Decision matrix
Table 3 – Example Corp. Automotive connectivity design inputs
Did this page help you? Yes No Provide feedback
Next topic:
Connectivity design selection
Previous topic:
Performance
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
