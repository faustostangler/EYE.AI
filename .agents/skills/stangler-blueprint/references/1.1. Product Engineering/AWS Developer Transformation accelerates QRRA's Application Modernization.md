---
name: AWS Developer Transformation accelerates QRRA's Application Modernization
keywords: (placeholder)
metadata:
  url: https://aws.amazon.com/blogs/migration-and-modernization/aws-developer-transformation-accelerates-qrras-application-modernization/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
AWS Developer Transformation accelerates QRRA's Application Modernization | Migration & Modernization
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
Migration & Modernization
AWS Developer Transformation accelerates QRRA's Application Modernization
by Derick Chen and Arun Surendran on 16 JUL 2025 in Amazon API Gateway, Amazon Elastic Container Registry, Amazon Q Developer, Asia Pacific, AWS Lambda, AWS Step Functions, Customer Solutions, Intermediate (200), Retail, Technical How-to Permalink Share
 https://aws.amazon.com/blogs/migration-and-modernization/aws-developer-transformation-accelerates-qrras-application-modernization/
Breaking free from a monolithic architecture is often a lengthy process, but with support from Amazon Web Services (AWS) through its Developer Transformation program, QRRA made significant progress in just three days. Legacy monolithic applications are commonly the biggest roadblock to digital transformation, with modernization efforts typically spanning months or even years. When QRRA, a leading retail solutions provider, encountered this challenge, they partnered with AWS to redefine their approach. Leveraging Domain-Driven Design and the AI capabilities of Amazon Q Developer's AI capabilities, QRRA successfully transformed key business-critical workloads into microservices within a short timeframe.
Introduction
QR Retail Automation (Asia) Sdn Bhd (QRRA) is a Malaysia-based retail enterprise solutions provider that has been serving medium to large retailers globally since 1992. A fully owned subsidiary of the Silverlake Group, QRRA specializes in retail consulting, system implementation, and ongoing maintenance and enhancement services with its proprietary software.
In today's rapidly evolving business landscape, QRRA helps companies remain competitive by streamlining business processes through automation and digitalization. Their comprehensive SaaS solution, the QR AgoraCloud suite, integrates modern technologies with robust merchandising functionalities, forming the foundation for digital transformation initiatives. By managing system upkeep and upgrades, QRRA allows businesses to focus on core operations without IT distractions.
With extensive industry expertise, QRRA positions itself as a strategic partner, offering innovative, cloud-enabled solutions. QRRA's proven track record in digital transformation makes it a trusted partner for companies aiming to achieve their current and future goals in the digital age.
Key challenges
QRRA's Merchandising & Material Management software, a monolithic application with tightly coupled modules built in Java with an Oracle database, has long been integral to the company's retail operations. As the business scaled, limitations of the monolithic architecture became increasingly apparent. During the year's biggest online retail sales event, known as the “11/11 sale”, QRRA's system degraded at peak load, when peak traffic reached 8,000 items sold across 2,000 sales orders per hour. This led to resource contention and performance challenges that impacted overall operations. QRRA subsequently implemented a queuing mechanism with controlled processing limits, effectively regulating load at 50 orders per batch and significantly improving stability at the cost of concurrent throughput. The system's large and intricate codebase further complicates maintenance and debugging efforts, extending release cycles, and delaying the timely rollout of critical features and updates. The absence of modularization constrains the adoption of innovative technologies and improvements, while inefficient resource allocation and elevated infrastructure costs place further strain on operational budgets.
Development teams also face substantial integration challenges due to intertwined code structures, impeding coordination, slowing down project timelines, and heightening the risk of downtime. By addressing these pain points through a modernization engagement with the AWS Prototyping and Cloud Engineering (PACE) Developer Transformation program, QRRA aims to transform its Merchandising and Material Management software into more agile, scalable, and maintainable systems, better suited to meet the dynamic needs of the retail industry.
Solution design mental model
The collaboration between QRRA and AWS improved the adaptability in the distributed system and brought about long-term benefits such as shorter time to market and more frequent deployments with higher predictability. Software adaptability measures the effort required for future changes, founded on high cohesion and loose coupling that mirror business reality. High cohesion groups similar functionalities within each service, while loose coupling minimizes inter-service dependencies, enabling independent deployments.
To design and implement a system with high adaptability, QRRA referenced the principles of Domain-Driven Design (DDD). DDD is a systems design philosophy that models a software system based on the inputs of domain experts from both the business and the technical teams. This closely resembles the Working Backwards principle at Amazon. Software design should begin from understanding the business processes and distilling the requirements.
Event Storming workshop
Event Storming is an interactive workshop that helps both the product and the development team to understand the business flow and extract requirements for a sound design of the microservice layout. The goal is to identify business functions and processes that are highly cohesive to be developed and deployed as independent services. This allows software teams to move faster with less dependencies in release management. In the Event Storming workshop, product and development teams collaborate to create a visual map of the entire business system. Using color-coded sticky notes, the team identifies:
Domain events (orange): significant system events (e.g., “order placed”, “payment received”)
Commands (blue): actions that trigger these events (e.g., “place order”, “process payment”)
Actors (yellow): users or systems that initiate commands (e.g., “customer”, “sales agent”)
External systems (pink): third-party services or legacy systems that interact with the system
Policies (purple): business rules and regulations that govern processes
Read models (green): views or projections of data that actors need to make decisions (e.g., “order summary dashboard”, “inventory status report”)
With the guidance from AWS software architects, the QRRA team then identified aggregates, clusters of related domain events, commands, and data managed together as a unit. For example, an “order” aggregate might include events like “order placed”, “order paid”, and “order shipped”, along with their associated commands and data.
Finally, the QRRA team drew bounded contexts, logical boundaries around groups of related aggregates, which naturally evolve into the microservice boundaries. All order-related aggregates might form an “order management” bounded context, while inventory-related aggregates form an “inventory management” bounded context. These boundaries ensure each future microservice has a clear, focused responsibility and minimal dependencies on other services.
Service boundaries closely mapped to the business reality helps reduce the model translation mental gap between the business and the technical solution. The identified bounded contexts and aggregates become important inputs for the microservice architecture design.
Microservices architecture
Using the bounded contexts and aggregates identified during Event Storming as a foundation, the QRRA team created an initial microservice design. This design was then refined to optimize integration points between services while maintaining alignment with actual business operations.
Through iterative discussions with AWS team, QRRA identified six distinct services for warehouse workflows: five core domains (Online Sales Order, Offline Sales Order, Inbound, Outbound, Warehouse Internal) and one domain service (Inventory) as shown in Figure 1. The domains primarily handle business logic specific to the business processes, while the domain service aims to provide utility functions and workflows with business logics that do not naturally fit into the above domains. 
Figure 1. Microservice boundary definition
The services are optimized for independent deployments with minimal dependency on other services. This allows QRRA to achieve adaptability with the least integration complexity and lowers the effort of future changes. Within each service, the amount of business scope and level of complexities to be included are designed to be proportional to the delivery capability of the team that will build and operate the service.
Performance design considerations and AWS architecture
To select the most appropriate set of AWS services to support this behavioral design, the QRRA considered the changes that the system must be able to adapt to.
Handling spiky traffic
The Online Sales Order and Offline Sales Order domains are critical entry points for customer orders. During peak sales periods, these services must handle sudden surges in order volume while maintaining data consistency. 
Figure 2. Online Sales Order service architectural design on AWS
AWS Lambda provides automatic scaling to handle unpredictable traffic loads while offering streamlined development and deployment processes. The incoming traffic amount of these two domains vary based on sales and seasonal shopping trends.
Amazon Simple Queue Service (SQS) provides a durable message buffer, complementing Lambda's scaling capabilities to ensure consistent request processing.
Amazon DocumentDB to store event records and maintain processing consistency. The solution implements the Event Sourcing pattern, with AWS Lambda functions publishing events to Amazon DocumentDB. DocumentDB Change Streams then propagate these events to downstream QRRA services like the “Outbound” service.
Amazon Simple Storage Service (Amazon S3) for any generation and storage of file-based assets required for downstream work.
Distributed multi-step workflows
Managing data consistency across distributed services becomes challenging when multi-step transactions can fail at any point. To address this, the QRRA team is moving toward adopting the Saga Orchestration pattern, a sequence of local transactions where each service performs its work and publishes an event to trigger the next step. As illustrated in Figures 3 and 4, if any step fails, the pattern runs compensating transactions to maintain data consistency across all services. 
Figure 3. Orchestrator design in Inventory domain service 
*Figure 4. Orchestration and compensation implementation with Amazon Step Function
and AWS Lambda*
Amazon Step Functions is chosen to be the orchestrator to control the flow of transaction and compensations depending on intermediate results. It has native integrations with both AWS Lambda and Amazon Elastic Container Service (Amazon ECS).
Domain services
The warehouse operation domains (Inbound, Outbound, Warehouse Internal) and Inventory domain service handle predictable day-to-day workflows with consistent traffic patterns. For these steady-state workloads, container-based deployment was chosen using Amazon ECS as shown in Figure 5. Containers provide efficient resource utilization and controlled scaling for these predictable workflows, while Amazon DocumentDB supports data persistence needs. The workflows are invoked either via a private API call or via an event driven system (such as the Amazon DocumentDB stream from Online Sales Order). 
Figure 5. Event driven consumer-producer design for Outbound service
Amazon ECS on AWS Fargate with automatic scaling policies that respond to both CPU and memory utilization. This ensures the services scale out when either resource approaches its defined threshold. Container images stored in Amazon Elastic Container Registry (Amazon ECR) provide consistent deployments across this elastic environment.
Amazon DocumentDB serves as our event store, maintaining a complete record of all warehouse operations in document format. This supports both audit requirements and operational analytics.
CI-CD / DevOps
According to the Global Code Time Report by software.com, software engineers typically spend only 55 minutes per day innovating and building new features. In a truly modern application, an organization needs to leverage managed services and infrastructure as code to minimize operational overhead to allow engineering teams to focus on innovation. With the help of Amazon Q Developer, the QRRA team was able to move from manual deployment operation to AWS Cloud Development Kit (AWS CDK) with infrastructure as code in just three days.
Amazon Q Developer helped DevOps engineers accelerate their AWS CDK development by removing common barriers like documentation comprehension and syntax challenges. As a result, DevOps engineers no longer depend on AWS management console access to deploy the latest updates and patches.
Conclusion
QRRA's modernization journey demonstrates how combining AWS services with domain-driven design principles creates adaptable, future-ready applications. Within three days, the team transformed a monolithic application into six independent microservices, implemented automated scaling to handle variable traffic loads, and simplified deployment processes using infrastructure as code. By using Amazon Q Developer to accelerate development, QRRA proved that rapid modernization is achievable without compromising architectural quality. While technology platforms evolve, the fundamental principles of this approach remain constant: understand the business domain, design for independence, and build for change. As a result, QRRA can now deploy updates faster, scale efficiently during peak sales events, and continue modernizing their applications incrementally.
To start your own application modernization journey with AWS Prototyping and Cloud Engineering (PACE), contact your AWS account team.
About the authors
Sim Meng Yang
Sim Meng Yang is the Senior Vice President of QRRA, overseeing product development, infrastructure, analytics, and product innovation. Sim successfully transitioned QRRA's products to a SaaS model and continues to drive innovation through cloud and AI technologies. With extensive experience supporting retailers on their digital transformation journey, Sim brings deep industry insight and a passion for enabling business agility through technology. 
Derick Chen
Derick Chen is a Developer Specialist Solutions Architect in Amazon Web Services (AWS), helping engineering organizations modernize applications in the cloud. Derick has transformed organizations by modernizing the software development process and principles, allowing developers to focus on innovation through rapid and high quality iteration cycles. 
Arun Surendran
Arun Surendran is a Senior Solutions Architect at Amazon Web Services, specializing in assisting ISV customers in building and operating secure workloads on AWS. He has over 13 years of experience in building and modernizing applications in production environments, with a focus on performance, reliability, scalability, and operational aspects.
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
