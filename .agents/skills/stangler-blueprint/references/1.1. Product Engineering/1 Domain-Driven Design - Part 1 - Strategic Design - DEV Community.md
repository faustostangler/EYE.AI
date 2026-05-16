---
name: 1 Domain-Driven Design - Part 1 - Strategic Design - DEV Community
keywords: (placeholder)
metadata:
  url: https://dev.to/axeldlv/domain-driven-design-part-1-strategic-design-30b2
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Domain-Driven Design - Part 1 - Strategic Design - DEV Community
Skip to content
Powered by Algolia
Log in Create account
DEV Community
1 Add reaction 
1 Like  0 Unicorn  0 Exploding Head  0 Raised Hands  0 Fire
0 Jump to Comments 3 Save Boost
Copy link
Copied to Clipboard
Share to X Share to LinkedIn Share to Facebook Share to Mastodon
Report Abuse
Axel Dlv
Posted on May 29, 2024 
1    
Domain-Driven Design - Part 1 - Strategic Design
# ddd # architecture # productivity # learning
Domain-Driven Design (2 Part Series)
1 Domain-Driven Design - Part 1 - Strategic Design 2 Domain-Driven Design - Part 2 - Tactical Design
Introduction
Domain-Driven Design (DDD) is a well known concept of software design approach based on domain models explaining in the book Domain-Driven Design: Tackling Complexity in the Heart of Software in 2003 by Eric Evans and Implementing Domain-Driven Design in 2013 by Vaughn Vernon.
We are starting with the "theorical part" of the DDD concept, the Strategic Design.
Type of Subdomains
In DDD, a Business domain (the main area of focus for a company) typically comprises three types of subdomains:
Core subdomains - Specific/unique from other company These are specific and unique to a company, often involving new technologies or services that differentiate it from competitors. For example, AWS's core subdomains include e-commerce, cloud computing, and artificial intelligence.
Generic subdomains - Performing in the same way as other company These are areas where using existing solutions (off-the-shelf software) saves time compared to developing custom solutions. Examples include AWS IAM (Identity and Access Management) and online retail platforms.
Supporting subdomains - It does not provide any competitive impact These subdomains do not directly impact competitiveness but support the overall business domain. Examples include CRUD operations (Create, Read, Update, Delete) and ETL (Extract, Transform, Load) processes.
Ubiquitous Language
Communication between business stakeholders and developers can be challenging due to differing perspectives.
DDD introduces an Ubiquitous Language to facilitate efficient communication and active participation of domain experts.
This language can be documented using various methods such as wikis or word documents, ensuring clarity and consistency in communication.
Bounded Context
A Bounded Context divides the ubiquitous language into smaller, explicit contexts. For example, in a business model, contexts could include "shopping" and "accounting."
While these contexts can evolve independently, they must integrate with each other, often through contracts.
Patterns of Integration
Cooperation
Partnership : The integration between bounded contexts is coordinated in an ad hoc manner. The communication is two-way, teams cooperate during the work. Often, this process involves a collaboration between two software companies, or a software company and a hardware company, to integrate their respective products or services, thereby improving the experience for the end user.
Shared Kernel : This integration is used when two or more bounded contexts have to communicate with each other via a shared model (e.g: Shared JARs or Database schema). Each context can modify the share model and take effect on other bounded contexts.
Customer-Supplier
It is a upstream-downstream relationship where the supplier is the upstream and the customer the downstream.
Conformist : The client (downstream) has to be conform from what the supplier (upstream) sent to it. There is not translation of models.
Anticorruption layer It is the other side of conformist, the client (downstream) translates the data (bounded context's model) into a model tailored to it is own context/domain. The ACL acts as a translation layer, ensuring that the two systems can communicate without corrupting each other's design and functionality. The legacy system uses an old relational database model and communicates via SOAP web services, while your system uses a modern RESTful API architecture.
Open Host Service The supplier (upstream) is intended to expose a protocol convenient (translate the data before send the message) using a public language for the consumers (downstream). We can use web services or micro-services defined services using a API for your service to expose an interface openly accessible.
Separate Ways
Integration between contexts does not involve collaboration between teams.
Go further
The connections between the bounded contexts can be visualized on a context map. This tool provides understanding of the system's overarching structure, communication flow, and potential organizational challenges.
Now that you've gained insight into techniques of domain-driven design for examining and modeling business domains, we'll pivot our focus from strategic considerations to tactical approaches that you can find here.
Thank for reading
If you have any questions, feedback, or suggestions, please feel free to leave them in the comments below. I'm eager to hear from you and respond to your thoughts!
Domain-Driven Design (2 Part Series)
1 Domain-Driven Design - Part 1 - Strategic Design 2 Domain-Driven Design - Part 2 - Tactical Design
 The DEV Team
Promoted
What's a billboard?
Manage preferences
Report billboard
Observability at Scale: Mastering ADK Callbacks for Cost, Latency, and Auditability [GDE]
AI orchestrators receive significant attention; however, when deployments become latent and costly, developers often overlook a critical capability: ADK callback hooks. The design patterns and best practices of callback hooks enable developers to refactor logic from agents to callback hooks to add observability, reduce cost and latency, and modify session state dynamically.
Read more →
Read More
Top comments (0)
Subscribe 
Personal Trusted User
Create template
Templates let you quickly answer FAQs or store snippets for re-use.
Submit Preview Dismiss
Code of Conduct
• Report abuse
Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's permalink. [-] 1
Hide child comments as well
Confirm
For further actions, you may consider blocking this person and/or reporting abuse
 AWS
Promoted
What's a billboard?
Manage preferences
Report billboard
Building industry breakthroughs together
Discover how the cloud helps businesses adapt, innovate, and grow in real time. Tune in live.
Register Now
Axel Dlv
Follow
Senior Java Consultant, AWS Community Builder and Skyplanner of Cloud Solutions ☁
Location Belgium
Joined Jan 19, 2024
More from Axel Dlv
Traffic Shifting for AWS Lambda Deployments Using LocalStack and Terraform # aws # cloud # architecture # serverless
How to Build an Event-Driven Outbox Pattern with AWS, Terraform and LocalStack # aws # terraform # eventdriven # architecture
AWS Landing Zone - AWS Services # aws # architecture # landingzone # beginners
 Auth0
Promoted
What's a billboard?
Manage preferences
Report billboard
Stop hard-coding API keys for your AI agents.
Auth0's Token Vault securely stores and refreshes tokens for third-party apps, so you can build faster and safer.
Get started
👋 Kindness is contagious
What's a billboard?
Manage preferences
Report billboard
Dive into this insightful article, celebrated by the caring DEV Community. Programmers from all walks of life are invited to share and expand our collective wisdom.
A simple thank-you can make someone's day—drop your kudos in the comments!
On DEV, spreading knowledge paves the way and strengthens our community ties. If this piece helped you, a brief note of appreciation to the author truly counts.
Let's Go!
💎 DEV Diamond Sponsors
Thank you to our Diamond Sponsors for supporting the DEV Community
Google AI is the official AI Model and Platform Partner of DEV
Neon is the official database partner of DEV
Algolia is the official search partner of DEV
DEV Community — A space to discuss and keep up software development and manage your software career
Home
DEV++
Videos
DEV Education Tracks
DEV Challenges
DEV Help
Advertise on DEV
Organization Accounts
DEV Showcase
About
Contact
Free Postgres Database
DEV Shop
MLH
Code of Conduct
Privacy Policy
Terms of Use
Built on Forem — the open source software that powers DEV and other inclusive communities.
Made with love and Ruby on Rails. DEV Community © 2016 - 2026. 
We're a place where coders share, stay up-to-date and grow their careers.
Log in Create account     
