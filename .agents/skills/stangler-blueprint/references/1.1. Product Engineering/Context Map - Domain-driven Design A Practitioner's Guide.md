---
name: Context Map - Domain-driven Design: A Practitioner's Guide
keywords: (placeholder)
metadata:
  url: https://ddd-practitioners.com/home/glossary/context-map/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Context Map – Domain-driven Design: A Practitioner's Guide
Skip to content
For practitioners by practitioners
Search 
Domain-driven Design: A Practitioner's Guide
Menu
FAQs
Glossary
About Us
Our Book!
FAQs
Glossary
About Us
Our Book!
Home Home Glossary Context Map
Context Map
In Domain-Driven Design, a Context Map is a visualization tool used to show the relationships between different bounded contexts within a domain. It is essentially a map that displays how the various contexts in a domain interact with each other, including their boundaries, their dependencies, and their communication patterns.
Bounded contexts are important in DDD because they help to identify and manage the complexity of large domains by breaking them down into smaller, more manageable parts. By understanding the relationships between different contexts, development teams can collaborate more effectively and ensure that each context is designed in a way that is consistent with the overall goals of the domain. Context Maps also help to highlight areas of potential conflict or overlap between contexts, which can be addressed early on to avoid issues down the line.
A context map typically includes the following constituents:
Context: A specific domain or subdomain that has a bounded context with explicit boundaries and a well-defined ubiquitous language.
Bounded Contexts: A boundary that defines a specific domain or subdomain in which the terms and concepts have a specific meaning.
Relationships: The relationships between bounded contexts. At a broad level, relationships are are of two types: symmetric or asymmetric. In a symmetric relationship, both sides have a more or less equal say in how the relationship evolves. In an asymmetric relationship, one of the sides acts as a clear power center
Teams: Teams responsible for the development and maintenance of a bounded context or subdomain.
Strategic Goals: The strategic goals that each bounded context aims to achieve.
A context map provides a high-level view of the domain and how different bounded contexts are related to each other, helping stakeholders to identify the system's architecture, dependencies, and risks.
There are several relationship types that can be depicted on a context map, including:
Partnership: A relationship between two bounded contexts where they collaborate as equal partners to achieve a common goal.
Shared Kernel: A relationship where two bounded contexts share a portion of the domain model or a data source.
Customer-Supplier: A relationship between two bounded contexts where one context provides functionality or data to another context, which consumes it.
Conformist: A relationship where one context is aligned with another context and conforms to its rules, standards, or policies.
Anticorruption Layer: A relationship where a layer of translation is used to isolate one context from another context with an incompatible model or technology.
Open Host Service: A relationship where a bounded context provides a public API that can be used by external clients or other bounded contexts.
Published Language: A relationship where two bounded contexts agree on a shared language or vocabulary to communicate with each other.
Separate Ways: A relationship where two bounded contexts are completely independent and have no interaction with each other.
Example
Here is simplified context map for a fictitious ** XYZ bank**. This visual depicts the various bounded contexts, their relationships. In the case of asymmetric relationships, it also indicates which side is upstream versus downstream. Looking at this visual should give onlookers a clear idea of the overall big picture of the software real estate at XYZ Bank. 
Comparison to the C4 model
The C4 model offers an alternate way to describe the architecture of your solution. Specifically, the system context diagram is very similar in nature to the context map in that they are both used to visualize the architecture of a software system. However, there are some key differences between the two approaches.
The DDD context map is a high-level diagram that shows the different bounded contexts within a system. Each bounded context is a self-contained domain that has its own language, models, and services. The DDD context map is a useful tool for understanding the overall architecture of a system and how the different bounded contexts interact.
The C4 model's system context diagram is a more detailed diagram that shows the different containers and components within a system. Each container is a grouping of components that share a common infrastructure. The C4 model's system context diagram is a useful tool for understanding the internal architecture of a system and how the different containers and components interact.
Here is a table that summarizes the key differences between the two approaches:
Categories
analysis
basics
ddd
design
faq
leadership
patterns
Blog at WordPress.com.
Subscribe Subscribed
Domain-driven Design: A Practitioner's Guide Sign me up
Already have a WordPress.com account? Log in now.
Domain-driven Design: A Practitioner's Guide
Subscribe Subscribed
Sign up
Log in
Copy shortlink
Report this content
View post in Reader
Manage subscriptions
Collapse this bar
Loading Comments...
Write a Comment...
Email (Required) Name (Required) Website Post Comment
 
