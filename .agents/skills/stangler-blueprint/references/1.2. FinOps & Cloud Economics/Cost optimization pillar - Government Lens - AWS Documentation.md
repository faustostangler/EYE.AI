---
name: Cost optimization pillar - Government Lens - AWS Documentation
keywords: (placeholder)
metadata:
  url: https://docs.aws.amazon.com/wellarchitected/latest/government-lens/cost-optimization-pillar.html
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Cost optimization pillar - Government Lens
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
Government Lens
AWS Well-Architected Framework
Abstract and introduction
Service context checklist
Definitions
General design principles
Design with purpose
Design with end users (citizens, residents, businesses)
Make the service simple and intuitive
Iterate and improve frequently (with end user and staff feedback)
Collaborate and work in the open by default
Address security and privacy risks
Build inclusive services
Design trustworthy services
Measure, report, and take data-driven decisions
Consider composable architecture and reusability
Maintain service continuity
Scenarios
Artificial intelligence in the public sector
Classified information systems
Citizen engagement reference architecture
Regulatory reporting reference architecture
Distributed processing of sensitive documents reference architecture
Omni-channel public services
Open government methods, infrastructure, and tools
Verifiable credentials (claims) for government
Pillars of the Well-Architected Framework
Operational excellence pillar
Reshape the operating model
Organizational risk
Resources
Security pillar
Verifying privacy-by-design
Shifting to a real time security model
Resources
Reliability pillar
Performance efficiency pillar
Cost optimization pillar
Sustainability pillar
Climate action and technology
Resources
Enabling services outcomes for government
Conclusion
Contributors
Document history
Notices
AWS Glossary
Documentation
...
AWS Well-Architected
AWS Well-Architected Framework
Documentation
AWS Well-Architected
AWS Well-Architected Framework
Cost optimization pillar
PDF
RSS
Markdown [-]
Focus mode
On this page
Resources
Documentation AWS Well-Architected AWS Well-Architected Framework Resources The cost optimization pillar includes the ability to run services which deliver policy intent and user outcome at the best value. The following question and best practices are designed to complement the best practices in the Cost Optimization Pillar whitepaper. GL-COST-01: How do you demonstrate an understanding of “value for money” in the customer's context? Most government entities have clear rules around how they assess value for money, but this can be subtly different across jurisdictions. For some countries, value for money is considered whatever is the best functionality for the cost to deliver the desired policy outcome. Other countries take into account the best balance of social, public, and environmental benefits along with cost. These procurement rules translate to how cost optimization is perceived, with broader analysis of the public value or policy realization sometimes considered as pure cost efficiencies. For this reason, running services at the lowest price point to deliver policy outcomes may or may not be considered cost optimization for the government department, although it's still a generally useful goal. The following is a list of considerations and good practices to explore with the customer and to document to make sure that value for money is achieved in a government context.
Document the definition of value for money for the jurisdictional and portfolio context, and how this service meets that definition.
Improvement plan – Engage with the government organization to understand and document their value for money definition. Work with your AWS account team to optimise costs. If you're on AWS Enterprise Support, your Technical Account Manager (TAM) can help with this. The AWS Tools for Reporting and Cost Optimization whitepaper can provide guidance.
Define how the cost and value is reported to oversight and governance bodies (for example, parliament, and public scrutiny).
Improvement plan – Encourage the organization to automate and provide ease of cost/value reporting for the service. AWS provides several reporting and cost-optimization tools, including AWS Cost Explorer Service, AWS Budgets, and AWS Cost and Usage Report. Serverless applications running on services like AWS Lambda and Amazon DynamoDB can help by providing insight into costs per event.
Build in-house capability manage costs through training, tools, and equipping teams.
Improvement plan – Provide delivery teams with the services and tools that they need to be able to actively understand and manage their costs.
Leverage existing solutions and capabilities where possible. Support the reuse of platforms, panels, marketplaces, research, design systems, and existing solutions or components where possible.
Improvement plan – Encourage the organization to identify and leverage reusable tools, solutions, research and methods for the service. See the AWS Solutions Library .
Leverage professional networks and user groups. Identify and engage with cross-governmental networks, professional networks and relevant user groups to engage peer review and feedback on the solution.
Improvement plan – Encourage the organization to identify and leverage networks and communities of practice, and establish peer review sessions.
Optimize for speed of change.. It's sometimes necessary to optimize for speed to respond to a citizen need or department mandate rapidly. Government solutions might need to initially overcompensate on capacity to maintain service reliability during peak popularity, for example, at the time of a press release, to avoid breaking citizen trust. Fortunately, this necessary choice is temporary and works well with cloud economics. Service delivery teams can cost optimize and consider automatic scaling after release events, when utilization and popularity have normalized.
Improvement plan – Provide guidance and support on automated resource optimization.
Optimize for budget planning processes in the jurisdiction. Provide decision makers with the key metrics that they need to balance citizen needs with service costs. Support the organization to take into account funding cycles and ensure continuity of service. Often, there is low flexibility in these cycles, however, government customers can be supported to build more flexibility into the program, project, or product-based funding mechanisms.
Improvement plan – Encourage the organization to automate and provide ease of cost/value reporting for the service, especially for delivery teams and decision makers.
Resources
AWS Tools for Reporting and Cost Optimization whitepaper
AWS reusable solutions, patterns, and applications:
AWS Solutions Library
AWS Construct Library
AWS Serverless Application Repository
How cloud can help agencies enhance security, save costs, and improve mission delivery through the Technology Modernization Fund (TMF)
For Small Governments – The Cloud is Only as Big as You Want it to Be
Optimizing nonprofits' costs in the cloud Javascript is disabled or is unavailable in your browser. To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions. Document Conventions Performance efficiency pillar Sustainability pillar Did this page help you? - Yes Thanks for letting us know we're doing a good job! If you've got a moment, please tell us what we did right so we can do more of it. Did this page help you? - No Thanks for letting us know this page needs work. We're sorry we let you down. If you've got a moment, please tell us how we can make the documentation better.
Did this page help you? Yes No Provide feedback
Next topic:
Sustainability pillar
Previous topic:
Performance efficiency pillar
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
