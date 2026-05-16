---
name: Hexagonal architecture pattern - AWS Prescriptive Guidance
keywords: (placeholder)
metadata:
  url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Hexagonal architecture pattern - AWS Prescriptive Guidance
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
AWS Prescriptive Guidance
Cloud design patterns, architectures, and implementations
Introduction
Anti-corruption layer pattern
API routing patterns
Hostname routing
Path routing
HTTP header routing
Circuit breaker pattern
Event sourcing pattern
Hexagonal architecture pattern
Publish-subscribe pattern
Retry with backoff pattern
Saga patterns
Saga choreography
Saga orchestration
Scatter-gather pattern
Strangler fig pattern
Transactional outbox pattern
Resources
Document history
Glossary
Documentation
...
AWS Prescriptive Guidance
Cloud design patterns, architectures, and implementations
Documentation
AWS Prescriptive Guidance
Cloud design patterns, architectures, and implementations
Hexagonal architecture pattern
PDF
RSS
Markdown [-]
Focus mode
On this page
Intent
Motivation
Applicability
Issues and considerations
Implementation
Related content
Videos
Documentation AWS Prescriptive Guidance Cloud design patterns, architectures, and implementations Intent Motivation Applicability Issues and considerations Implementation Related content Videos
Intent
The hexagonal architecture pattern, which is also known as the ports and adapters pattern, was proposed by Dr. Alistair Cockburn in 2005. It aims to create loosely coupled architectures where application components can be tested independently, with no dependencies on data stores or user interfaces (UIs). This pattern helps prevent technology lock-in of data stores and UIs. This makes it easier to change the technology stack over time, with limited or no impact to business logic. In this loosely coupled architecture, the application communicates with external components over interfaces called ports, and uses adapters to translate the technical exchanges with these components.
Motivation
The hexagonal architecture pattern is used to isolate business logic (domain logic) from related infrastructure code, such as code to access a database or external APIs. This pattern is useful for creating loosely coupled business logic and infrastructure code for AWS Lambda functions that require integration with external services. In traditional architectures, a common practice is to embed business logic in the database layer as stored procedures and in the user interface. This practice, along with using UI-specific constructs within business logic, leads to closely coupled architectures that cause bottlenecks in database migrations and user experience (UX) modernization efforts. The hexagonal architecture pattern enables you to design your systems and applications by purpose rather than by technology. This strategy results in easily exchangeable application components such as databases, UX, and service components.
Applicability
Use the hexagonal architecture pattern when:
You want to decouple your application architecture to create components that can be fully tested.
Multiple types of clients can use the same domain logic.
Your UI and database components require periodical technology refreshes that don't affect application logic.
Your application requires multiple input providers and output consumers, and customizing the application logic leads to code complexity and lack of extensibility.
Issues and considerations
Domain-driven design: Hexagonal architecture works especially well with domain-driven design (DDD). Each application component represents a sub-domain in DDD, and hexagonal architectures can be used to achieve loose coupling among application components.
Testability: By design, a hexagonal architecture uses abstractions for inputs and outputs. Therefore, writing unit tests and testing in isolation become easier because of the inherent loose coupling.
Complexity: The complexity of separating business logic from infrastructure code, when handled carefully, can bring great benefits such as agility, test coverage, and technology adaptability. Otherwise, issues can become complex to solve.
Maintenance overhead: The additional adapter code that makes the architecture pluggable is justified only if the application component requires several input sources and output destinations to write to, or when the inputs and output data store has to change over time. Otherwise, the adapter becomes another additional layer to maintain, which introduces maintenance overhead.
Latency issues: Using ports and adapters adds another layer, which might result in latency.
Implementation
Hexagonal architectures support the isolation of application and business logic from infrastructure code and from code that integrates the application with UIs, external APIs, databases, and message brokers. You can easily connect business logic components to other components (such as databases) in the application architecture through ports and adapters. Ports are technology-agnostic entry points into an application component. These custom interfaces determine the interface that allows external actors to communicate with the application component, regardless of who or what implements the interface. This is similar to how a USB port allows many different types of devices to communicate with a computer, as long as they use a USB adapter. Adapters interact with the application through a port by using a specific technology. Adapters plug into these ports, receive data from or provide data to the ports, and transform the data for further processing. For example, a REST adapter enables actors to communicate with the application component through a REST API. A port can have multiple adapters without any risk to the port or to the application component. To extend the previous example, adding a GraphQL adapter to the same port provides an additional means for actors to interact with the application through a GraphQL API without affecting the REST API, the port, or the application. Ports connect to the application, and adapters serve as a connection to the outside world. You can use ports to create loosely coupled application components, and exchange dependent components by changing the adapter. This enables the application component to interact with external input and outputs without needing to have any contextual awareness. Components are exchangeable at any level, which facilitates automated testing. You can test components independently without any dependencies on the infrastructure code instead of provisioning an entire environment to conduct testing. The application logic doesn't depend on external factors, so testing is simplified and it becomes easier to mock dependencies. For example, in a loosely coupled architecture, an application component should be able to read and write data without knowing the details of the data store. The responsibility of the application component is to supply data to an interface (port). An adapter defines the logic of writing to a data store, which can be a database, a file system, or an object storage system such as Amazon S3, depending on the application's needs.
High-level architecture
The application or application component contains the core business logic. It receives commands or queries from the ports, and sends requests out through the ports to external actors, which are implemented through adapters, as illustrated in the following diagram.
Implementation using AWS services
AWS Lambda functions often contain both business logic and database integration code, which are tightly coupled to meet an objective. You can use the hexagonal architecture pattern to separate business logic from infrastructure code. This separation enables unit testing of the business logic without any dependencies on the database code, and improves the agility of the development process. In the following architecture, a Lambda function implements the hexagonal architecture pattern. The Lambda function is initiated by the Amazon API Gateway REST API. The function implements business logic and writes data to DynamoDB tables.
Sample code
The sample code in this section shows how to implement the domain model by using Lambda, separate it from infrastructure code (such as the code to access DynamoDB), and implement unit testing for the function.
Domain model
The domain model class has no knowledge of external components or dependencies—it only implements the business logic. In the following example, the class Recipient is a domain model class that checks for overlaps in the reservation date.
Input port
The RecipientInputPort class connects to the recipient class and runs the domain logic.
DynamoDB adapter class
The DDBRecipientAdapter class implements access to the DynamoDB tables.
The Lambda function get_recipient_input_port is a factory for instances of the RecipientInputPort class. It constructs instances of output port classes with related adapter instances.
Unit testing
You can test the business logic for domain model classes by injecting mock classes. The following example provides the unit test for the domain model Recipent class.
GitHub repository
For a complete implementation of the sample architecture for this pattern, see the GitHub repository at https://github.com/aws-samples/aws-lambda-domain-model-sample .
Related content
Hexagonal architecture , article by Alistair Cockburn
Developing evolutionary architectures with AWS Lambda (AWS blog post in Japanese)
Videos
The following video (in Japanese) discusses the use of hexagonal architecture in the implementation of a domain model by using a Lambda function. Tap to unmute Your browser can't play this video. Learn more  1x
An error occurred.
Try watching this video on www.youtube.com, or enable JavaScript if it is disabled in your browser. Javascript is disabled or is unavailable in your browser. To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions. Document Conventions Event sourcing pattern Publish-subscribe pattern Did this page help you? - Yes Thanks for letting us know we're doing a good job! If you've got a moment, please tell us what we did right so we can do more of it. Did this page help you? - No Thanks for letting us know this page needs work. We're sorry we let you down. If you've got a moment, please tell us how we can make the documentation better.
Did this page help you? Yes No Provide feedback
Next topic:
Publish-subscribe pattern
Previous topic:
Event sourcing pattern
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
Hexagonal architecture pattern
Close
Implementing the hexagonal architecture pattern on AWS
Close
