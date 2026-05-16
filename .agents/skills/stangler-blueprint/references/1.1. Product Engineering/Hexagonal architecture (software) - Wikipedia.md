---
name: Hexagonal architecture (software) - Wikipedia
keywords: (placeholder)
metadata:
  url: https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Hexagonal architecture (software) - Wikipedia
Jump to content [-]
Main menu
Main menu
move to sidebar hide
Navigation
Main page
Contents
Current events
Random article
About Wikipedia
Contact us
Contribute
Help
Learn to edit
Community portal
Recent changes
Upload file
Special pages
Search
Search [-]
Appearance
Donate
Create account
Log in [-]
Personal tools
Donate
Create account
Log in
Contents
move to sidebar hide
(Top)
1 Origin
2 Principle
3 Criticism
4 Evolution
5 Variants
6 See also
7 References [-]
Toggle the table of contents
Hexagonal architecture (software)
[-]
8 languages
Català
Deutsch
Español
Français
日本語
मराठी
Русский
Українська
Edit links
Article
Talk [-]
English
Read
Edit
View history [-]
Tools
Tools
move to sidebar hide
Actions
Read
Edit
View history
General
What links here
Related changes
Upload file
Permanent link
Page information
Cite this page
Get shortened URL
Edit interlanguage links
Print/export
Download as PDF
Printable version
In other projects
Wikidata item
Appearance
move to sidebar hide
Text
[-] 0 Small [x] 1 Standard [-] 2 Large
This page always uses small font size
Width
[x] 1 Standard [-] 0 Wide
The content is as wide as possible for your browser window.
Color
[-] os Automatic [x] day Light [-] night Dark
This page is always in light mode.
From Wikipedia, the free encyclopedia
Software design pattern
The hexagonal architecture, or ports and adapters architecture, is an architectural pattern used in software design. It aims at creating loosely coupled application components that can be easily connected to their software environment by means of ports and adapters. This makes components exchangeable at any level and facilitates test automation. [1]
Origin
[ edit]
The hexagonal architecture was invented by Alistair Cockburn in an attempt to avoid known structural pitfalls in object-oriented software design, such as undesired dependencies between layers and contamination of user interface code with business logic. It was discussed at first on the Portland Pattern Repository wiki; [2] [3] in 2005 Cockburn renamed it "Ports and adapters". [1] In April 2024, Cockburn published a comprehensive book on the subject, coauthored with Juan Manuel Garrido de Paz. [4]
The term "hexagonal" comes from the graphical conventions that shows the application component like a hexagonal cell. The purpose was not to suggest that there would be six borders/ports, but to leave enough space to represent the different interfaces needed between the component and the external world. [1]
Principle
[ edit]
Example of hexagonal architecture
The hexagonal architecture divides a system into several loosely-coupled interchangeable components, such as the application core, the database, the user interface, test scripts and interfaces with other systems. This approach is an alternative to the traditional layered architecture.
Each component is connected to the others through a number of exposed "ports". Communication through these ports follow a given protocol depending on their purpose. Ports and protocols define an abstract API that can be implemented by any suitable technical means (e.g. method invocation in an object-oriented language, remote procedure calls, or web services).
The granularity of the ports and their number is not constrained:
a single port could in some case be sufficient (e.g. in the case of a simple service consumer);
typically, there are ports for event sources (user interface, automatic feeding), notifications (outgoing notifications), database (in order to interface the component with any suitable DBMS), and administration (for controlling the component);
in an extreme case, there could be a different port for every use case, if needed.
Adapters are the glue between components and the outside world. They tailor the exchanges between the external world and the ports that represent the requirements of the inside of the application component. There can be several adapters for one port, for example, data can be provided by a user through a GUI or a command-line interface, by an automated data source, or by test scripts.
Criticism
[ edit]
The term "hexagonal" implies that there are 6 parts to the concept, whereas there are only 4 key areas. The term's usage comes from the graphical conventions that shows the application component like a hexagonal cell. The purpose was not to suggest that there would be six borders/ports, but to leave enough space to represent the different interfaces needed between the component and the external world. [1]
According to Martin Fowler, the hexagonal architecture has the benefit of using similarities between presentation layer and data source layer to create symmetric components made of a core surrounded by interfaces, but with the drawback of hiding the inherent asymmetry between a service provider and a service consumer that would better be represented as layers. [5]
Evolution
[ edit]
According to some authors, the hexagonal architecture is at the origin of the microservices architecture. [6]
Variants
[ edit]
The onion architecture proposed by Jeffrey Palermo in 2008 is similar to the hexagonal architecture: it also externalizes the infrastructure with interfaces to ensure loose coupling between the application and the database. [7] It decomposes further the application core into several concentric rings using inversion of control. [8]
The clean architecture proposed by Robert C. Martin in 2012 combines the principles of the hexagonal architecture, the onion architecture and several other variants. It provides additional levels of detail of the component, which are presented as concentric rings. It isolates adapters and interfaces (user interface, databases, external systems, devices) in the outer rings of the architecture and leaves the inner rings for use cases and entities. [9] [10] The clean architecture uses the principle of dependency inversion with the strict rule that dependencies shall only exist between an outer ring to an inner ring and never the contrary.
See also
[ edit]
Architecture patterns
Layer (object-oriented design)
Composite structure diagram
Object-oriented analysis and design
References
[ edit]
^ Jump up to: a  b  c  d Cockburn, Alistair (2005-04-01). "Hexagonal architecture". alistair.cockburn.us. Retrieved 2020-11-18.
^ "Hexagonal Architecture in the C2 Wiki".
^ "Ports And Adapters Architecture in the C2 Wiki".
^ "Hexagonal Architecture Explained".
^ Fowler, Martin (2003). Patterns of enterprise application architecture. Addison-Wesley. p. 21. ISBN 0-321-12742-0 . OCLC 50292267.
^ Rajesh R. V. (2017). Spring 5.0 microservices : build scalable microservices with Reactive Streams, Spring Boot, Docker, and Mesos (Second ed.). Packt Publishing. pp. 13– 14. ISBN 978-1-78712-051-8 . OCLC 999610958.
^ Jeffrey, Palermo (2008-07-29). "The Onion Architecture : part 1". Programming with Palermo. Retrieved 2019-08-12.
^ Chatekar, Suhas (2015). Learning NHibernate 4 : explore the full potential of NHibernate to build robust data access code. Packt Publishing. pp. 249– 250. ISBN 978-1-78439-206-2 . OCLC 937787252.
^ Martin, Robert, C. (2012-08-12). "The Clean architecture | Clean Coder Blog". blog.cleancoder.com. Retrieved 2019-08-12. {{ [cite web](https://en.wikipedia.org/wiki/Template:Cite_web)}} : CS1 maint: multiple names: authors list ( link)
^ Martin, Robert C. (2017). Clean architecture : a craftsman's guide to software structure and design. Prentice Hall. ISBN 978-0-13-449416-6 . OCLC 1004983973. 
Retrieved from " https://en.wikipedia.org/w/index.php?title=Hexagonal_architecture_(software)&oldid=1318929549"
Categories:
Software design
Architectural pattern (computer science)
Object-oriented programming
Hidden categories:
CS1 maint: multiple names: authors list
Articles with short description
Short description matches Wikidata
This page was last edited on 26 October 2025, at 21:17 (UTC).
Text is available under the Creative Commons Attribution-ShareAlike 4.0 License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.
Privacy policy
About Wikipedia
Disclaimers
Contact Wikipedia
Legal & safety contacts
Code of Conduct
Developers
Statistics
Cookie statement
Mobile view
Search
Search [-]
Toggle the table of contents
Hexagonal architecture (software)
8 languages Add topic 
