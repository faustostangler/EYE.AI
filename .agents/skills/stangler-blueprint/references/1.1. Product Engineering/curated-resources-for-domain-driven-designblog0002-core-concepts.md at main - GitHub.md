---
name: curated-resources-for-domain-driven-design/blog/0002-core-concepts.md at main - GitHub
keywords: (placeholder)
metadata:
  url: https://github.com/SAP/curated-resources-for-domain-driven-design/blob/main/blog/0002-core-concepts.md
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
curated-resources-for-domain-driven-design/blog/0002-core-concepts.md at main · SAP/curated-resources-for-domain-driven-design · GitHub
Skip to content
Navigation Menu
Toggle navigation 
Sign in
Appearance settings
Platform
AI CODE CREATION
GitHub Copilot Write better code with AI
GitHub Spark Build and deploy intelligent apps
GitHub Models Manage and compare prompts
MCP Registry New Integrate external tools
DEVELOPER WORKFLOWS
Actions Automate any workflow
Codespaces Instant dev environments
Issues Plan and track work
Code Review Manage code changes
APPLICATION SECURITY
GitHub Advanced Security Find and fix vulnerabilities
Code security Secure your code as you build
Secret protection Stop leaks before they start
EXPLORE
Why GitHub
Documentation
Blog
Changelog
Marketplace View all features
Solutions
BY COMPANY SIZE
Enterprises
Small and medium teams
Startups
Nonprofits
BY USE CASE
App Modernization
DevSecOps
DevOps
CI/CD
View all use cases
BY INDUSTRY
Healthcare
Financial services
Manufacturing
Government
View all industries View all solutions
Resources
EXPLORE BY TOPIC
AI
Software Development
DevOps
Security
View all topics
EXPLORE BY TYPE
Customer stories
Events & webinars
Ebooks & reports
Business insights
GitHub Skills
SUPPORT & SERVICES
Documentation
Customer support
Community forum
Trust center
Partners View all resources
Open Source
COMMUNITY
GitHub Sponsors Fund open source developers
PROGRAMS
Security Lab
Maintainer Community
Accelerator
GitHub Stars
Archive Program
REPOSITORIES
Topics
Trending
Collections
Enterprise
ENTERPRISE SOLUTIONS
Enterprise platform AI-powered developer platform
AVAILABLE ADD-ONS
GitHub Advanced Security Enterprise-grade security features
Copilot for Business Enterprise-grade AI features
Premium Support Enterprise-grade 24/7 support
Pricing
Search or jump to...
Search code, repositories, users, issues, pull requests...
Search
Clear
Search syntax tips
Provide feedback
We read every piece of feedback, and take your input very seriously. [-]
Include my email address so I can be contacted
Cancel Submit feedback
Saved searches
Use saved searches to filter your results more quickly
Name
Query
To see all available qualifiers, see our documentation.
Cancel Create saved search
Sign in
Sign up
Appearance settings
Resetting focus
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert
SAP / curated-resources-for-domain-driven-design Public
Notifications You must be signed in to change notification settings
Fork 43
Star 363
Code
Issues 0
Pull requests 0
Discussions
Actions
Projects
Security and quality 0
Insights
Additional navigation options
Code
Issues
Pull requests
Discussions
Actions
Projects
Security and quality
Insights 
Files Expand file tree
main
Breadcrumbs
curated-resources-for-domain-driven-design
/ blog
/
0002-core-concepts.md
Copy path
Blame
More file actions
Blame
More file actions
Latest commit
neolytian
Update 0002-core-concepts.md (#107)
last year
d90df49
· last year
History
History
Open commit details 
History
143 lines (82 loc) · 14.9 KB
main
Breadcrumbs
curated-resources-for-domain-driven-design
/ blog
/
0002-core-concepts.md
Top
File metadata and controls
Preview
Code
Blame
143 lines (82 loc) · 14.9 KB
Raw
Copy raw file
Download raw file
Outline
Edit and raw actions
The Core Concepts of Domain-Driven Design
We all want to create better code as software development teams, and Domain-Driven Design (DDD) is one collaborative approach that can assist us in doing so. DDD, at its heart, is a methodology to software development that emphasizes the business area and the issues we're attempting to resolve rather than just the technical execution.
The ability to establish a shared language between business experts and team members with a technical background like developers is one of the main advantages of DDD. We can communicate and work together more effectively if we use words and ideas that everyone engaged in the endeavor is familiar with. This shared understanding plays a vital role in making sure that everyone is pursuing the same objectives and prevents misunderstandings.
Modular design is promoted by DDD, which is an additional advantage. By dividing a system down into smaller, more manageable components, we can think about it more readily and make changes without affecting other portions of the software. Long term, this should result in a more adaptable and manageable system.
Testing and feedback processes are also emphasized in DDD. We can make sure that we are creating the correct thing and moving closer to our objectives by regularly verifying our ideas and getting input from business users, domain experts, and technical peers.
At the heart of DDD are several core concepts, including:
Strategic Design
Strategic design is a pillar of Domain-Driven Design (DDD) that focuses on defining the Bounded Contexts, Ubiquitous Language, and Context Maps of a project. It involves collaboration between domain experts and the technical team to ensure that the software model accurately reflects the business domain.
Bounded Context is one of the most important concepts of DDD. It represents a conceptual boundary within which a domain model is applicable. As you try to model a large domain, you may encounter difficulties because different groups of people may use subtly different terms and sentences. A Bounded Context helps to mitigate this issue by providing a linguistic delimitation where any use of vocabulary outside of that limit will probably mean something different.
Ubiquitous Language is another key concept in DDD. It is modeled within a Bounded Context and represents the terms and concepts of the business domain where there should be no ambiguity. The development of an efficient Ubiquitous Language requires an understanding of the business and should be developed in agreement with the entire project team.
Context Maps help to understand the relationships between different Bounded Contexts. There are several ways to relate Bounded Contexts, including Shared Kernel, Customer/Supplier, Conformist, Partner, and Anti-Corruption Layer.
In summary, strategic design in DDD involves defining the Bounded Contexts, Ubiquitous Language, and Context Maps of a project in collaboration with domain experts and the technical team. This helps to ensure that the software model accurately reflects the business domain.
Tactical design
Tactical design in Domain-Driven Design (DDD) involves refining the domain model to a stage where it can be converted into working code. It is a set of design patterns and building blocks that can be used to design domain-driven systems.
Compared to strategic domain-driven design, tactical design is much more hands-on and closer to the actual code. It deals with classes and modules rather than abstract wholes.
One of the most important concepts in tactical DDD is the value object. A value object is an object whose value is of importance. This means that two value objects with the same value might be deemed the same and hence interchangeable. As a result, value objects should always be immutable.
Value objects are not only containers of data - they can also contain business logic. The fact that the value objects are also immutable makes the business operations both thread-safe and side-effect free.
Another important concept in tactical DDD is the aggregate. An aggregate defines a consistency boundary around one or more entities. Exactly one entity in an aggregate is the root. Lookup is done using the root entity's identifier. Any other entities in the aggregate are children of the root, and are referenced by following pointers from the root. As such, a very important correlate of this is that during communication between Bounded Contexts one context never explicitly references ids below the aggregate root's id.
Ubiquitous language
Ubiquitous Language is a key concept of Domain-Driven Design (DDD). It is a common and consistent way of naming and describing the domain entities, rules, and scenarios.
The purpose of Ubiquitous Language is to build a language shared by the team, developers, domain experts, and other participants. It is modeled within a Bounded Context, where the terms and concepts of the business domain are identified, and there should be no ambiguity ².
Ubiquitous Language must be expressed in the Domain Model. It unites the people of the project team and eliminates inaccuracies and contradictions from domain experts.
Developing a clear Ubiquitous Language requires an understanding of the business. It evolves over time and is not defined entirely in a single meeting. Concepts that are not part of the Ubiquitous Language should be rejected.
Domains and subdomains
Domains and Subdomains in Domain-Driven Design
In Domain-Driven Design (DDD), a domain is the most vital concept. It refers to the space of the problem for which we are acting, its aggregates and entities, its behavior and rules.
A domain can have several meanings within DDD. It can refer to the totality of the company's domain, an area, sector or process of the company, or a domain that serves as support for the business.
DDD necessitates the division of the domain into subdomains, which aids human comprehension. In this method, we can distinguish what actually provides value and financial return for the organization.
A subdomain is a domain division. Every domain, regardless of company size, can be subdivided. We separate the total complexity of the company's domain into smaller segments by doing so.
There are three types of subdomains: Core, Supporting, Generic. The Core subdomain is where we must put our best efforts. The Supporting subdomain complements the main domain. The Generic subdomain typically can be supported by ready-made commercial or open-source software or services.
Core Domain
The core domain is where we want to excel as a business and our specific skills here really differentiate us from the rest of the market. It is so critical and fundamental to the business that it gives you a competitive advantage and is a foundational concept behind the business.
DDD advocates modeling based on the reality of business as relevant to your use cases. It describes independent problem areas as Bounded Contexts (each Bounded Context usually correlates to a microservice or a module within a well-structured monolith), and emphasizes a common language to talk about these problems.
The core domain gives you a competitive advantage and is a foundational concept behind the business.
Supporting Domain
The supporting domain is key to providing value in the core domain. These types of pieces help perform ancillary or supporting functions related directly to what the business does.
In these cases, high-quality code and perfectly designed structure are not necessary. You could get by with assigning more inexperienced developers or even outsourcing these pieces. Just be sure that these concepts do not bleed into your core domain—you want to maintain a rigid separation with a context map to keep separate things separate.
Note that even if you assign less experienced teams or outsource this work, it can be very advantageous to have automated test cases written by your core teams to ensure that any implementation of the subdomain fulfills the explicit business needs. This provides confidence in the correctness of the behavior and allows for future refactoring to improve the code quality or performance while retaining comfidence in its behavioral correctness.
Generic Domain
The generic domain is an area where the market has expertise that we can exploit. When developing or redeveloping an enterprise application, there will be parts of the system that aid the business but are not critical to the operation.
Most businesses, for example, have a concept of invoicing—sending bills to customers. While this is a critical business concept, it is not "core" to the organization. In general, these elements can be acquired from a vendor or outsourced and then packaged in such a way that they can connect with the rest of the organization as needed.
The generic domain leverages expertise in the market for areas that facilitate the business but are not core to it.
Events and commands
Domain events and commands are two key concepts in domain-driven design (DDD), a software development approach that focuses on the core business domain and its logic.
Domain events are facts that have happened in the past and affect the state of the domain, such as an order placed or a payment received. An important benefit of domain events is that side effects can be expressed explicitly.
A command is a message that is sent to the domain expressing an intention to change state or invoke some behavior. A command is processed by a dedicated command handler. A command should be named with a verb in an imperative mood plus the aggregate name which it operates on. A command request can be rejected due to the data the command holds being invalid/inconsistent. There should be exactly 1 handler for each command.
Events and commands express side effects explicitly and handling state changes in the domain.
Bounded Contexts
Bounded Context is a central pattern in Domain-Driven Design (DDD). It is the focus of DDD's strategic design section which is all about dealing with large models and teams.
DDD deals with large models by dividing them into different Bounded Contexts and being explicit about their interrelationships. A Bounded Context is primarily a linguistic delimitation, that is to say that terms and sentences can mean different things, according to the context in which they are employed.
This linguistic delimitation refers to ubiquitous language, which is another essential element in DDD. It is also important to understand that Bounded Context is where the Model is implemented, that is, a Bounded Context is the solution implementation in a technical way.
Bounded Contexts divide large models into different contexts and being explicit about their interrelationships.
Aggregates
A DDD aggregate is a cluster of domain objects that can be treated as a single unit.
An example may be an order and its line-items, these will be separate objects, but it's useful to treat the order (together with its line items) as a single aggregate. An aggregate will have one of its component objects be the aggregate root ¹.
Any references from outside the aggregate should only go to the aggregate root. The root can thus ensure the integrity of the aggregate as a whole. Aggregates are the basic element of transfer of data storage - you request to load or save whole aggregates. Transactions should not cross aggregate boundaries ¹.
Aggregates treat a cluster of domain objects as a single unit.
Conclusion
We can begin to implement DDD principles to our own projects and enjoy the advantages that come with it once we have a solid grasp of these ideas and how they work together. Finally, Domain-Driven Design is a potent method of software development that can aid groups in producing better, more enduring code. We can build a more collaborative and adaptable development process by concentrating on the business area and employing a shared language. The first step to implementing DDD in our own initiatives and gaining these advantages is comprehending its fundamental ideas.
Resources
DDD Part 1: Strategic Domain-Driven Design | Vaadin
I. Strategic Design - Learning Domain-Driven Design [Book]
Strategic Domain-Driven Design - Medium..
Using tactical DDD to design microservices - Azure Architecture Center
DDD Part 2: Tactical Domain-Driven Design | Vaadin
Domain-Driven Design Part II: Tactical Design | by Can Güt | Medium
Ubiquitous Language: Documenting and Communicating Tips - LinkedIn
UbiquitousLanguage - Martin Fowler
Domain-driven design - Wikipedia
Domain, Subdomain, Bounded Context, Problem/Solution Space in ... - Medium
Domain-Driven Design for Microservice Decomposition - LinkedIn
Domain Driven Design (DDD): Core concepts and Enterprise Architecture
DDD: Strategic Design: Core, Supporting, and Generic Subdomains
Designing a DDD-oriented microservice | Microsoft Learn
Domain Event vs Command: Versioning and Evolution in DDD - LinkedIn
Domain events: Design and implementation | Microsoft Learn
Command vs. Event in Domain Driven Design - Medium
BoundedContext - Martin Fowler.
Balancing Consistency and Autonomy in Bounded Contexts - LinkedIn.
DDD_Aggregate - Martin Fowler
What Are Aggregates In Domain-Driven Design? - James Hickey
Understanding Aggregates in Domain-Driven Design - DZone
Footer
© 2026 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Community
Docs
Contact
Manage cookies
Do not share my personal information
You can't perform that action at this time.
