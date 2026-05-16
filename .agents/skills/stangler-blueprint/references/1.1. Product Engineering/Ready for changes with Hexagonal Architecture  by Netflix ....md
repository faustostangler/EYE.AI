---
name: Ready for changes with Hexagonal Architecture | by Netflix ...
keywords: (placeholder)
metadata:
  url: https://netflixtechblog.com/ready-for-changes-with-hexagonal-architecture-b315ec967749
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Ready for changes with Hexagonal Architecture | by Netflix Technology Blog | Netflix TechBlog
Sitemap
Open in app
Sign up
Sign in
Medium Logo
Get app
Write
Search
Sign up
Sign in 
[
Netflix TechBlog
](https://netflixtechblog.com/?source=post_page---publication_nav-2615bd06b42e-b315ec967749---------------------------------------)
·
Follow publication
Learn about Netflix's world class engineering efforts, company culture, product developments and more.
Follow publication
Top highlight
1
1
1
1
1
1
1
Ready for changes with Hexagonal Architecture
Netflix Technology Blog
Follow
9 min read
·
Mar 10, 2020 
8K
33 
Listen
Share
by Damir Svrtan and Sergii Makagon
As the production of Netflix Originals grows each year, so does our need to build apps that enable efficiency throughout the entire creative process. Our wider Studio Engineering Organization has built numerous apps that help content progress from pitch (aka screenplay) to playback: ranging from script content acquisition, deal negotiations and vendor management to scheduling, streamlining production workflows, and so on.
Highly integrated from the start
About a year ago, our Studio Workflows team started working on a new app that crosses multiple domains of the business. We had an interesting challenge on our hands: we needed to build the core of our app from scratch, but we also needed data that existed in many different systems.
Some of the data points we needed, such as data about movies, production dates, employees, and shooting locations, were distributed across many services implementing various protocols: gRPC, JSON API, GraphQL and more. Existing data was crucial to the behavior and business logic of our application. We needed to be highly integrated from the start.
Swappable data sources
One of the early applications for bringing visibility into our productions was built as a monolith. The monolith allowed for rapid development and quick changes while the knowledge of the space was non-existent. At one point, more than 30 developers were working on it, and it had well over 300 database tables.
Over time applications evolved from broad service offerings towards being highly specialized. This resulted in a decision to decompose the monolith to specific services. This decision was not geared by performance issues — but with setting boundaries around all of these different domains and enabling dedicated teams to develop domain-specific services independently.
Large amounts of the data we needed for the new app were still provided by the monolith, but we knew that the monolith would be broken up at some point. We were not sure about the timing of the breakup, but we knew that it was inevitable, and we needed to be prepared.
Thus, we could leverage some of the data from the monolith at first as it was still the source of truth, but be prepared to swap those data sources to new microservices as soon as they came online.
Leveraging Hexagonal Architecture
We needed to support the ability to swap data sources without impacting business logic, so we knew we needed to keep them decoupled. We decided to build our app based on principles behind Hexagonal Architecture.
The idea of Hexagonal Architecture is to put inputs and outputs at the edges of our design. Business logic should not depend on whether we expose a REST or a GraphQL API, and it should not depend on where we get data from — a database, a microservice API exposed via gRPC or REST, or just a simple CSV file.
The pattern allows us to isolate the core logic of our application from outside concerns. Having our core logic isolated means we can easily change data source details without a significant impact or major code rewrites to the codebase.
One of the main advantages we also saw in having an app with clear boundaries is our testing strategy — the majority of our tests can verify our business logic without relying on protocols that can easily change.
Defining the core concepts
Leveraged from the Hexagonal Architecture, the three main concepts that define our business logic are Entities, Repositories, and Interactors.
Entities are the domain objects (e.g., a Movie or a Shooting Location) — they have no knowledge of where they're stored (unlike Active Record in Ruby on Rails or the Java Persistence API).
Repositories are the interfaces to getting entities as well as creating and changing them. They keep a list of methods that are used to communicate with data sources and return a single entity or a list of entities. (e.g. UserRepository)
Interactors are classes that orchestrate and perform domain actions — think of Service Objects or Use Case Objects. They implement complex business rules and validation logic specific to a domain action (e.g., onboarding a production)
With these three main types of objects, we are able to define business logic without any knowledge or care where the data is kept and how business logic is triggered. Outside of the business logic are the Data Sources and the Transport Layer:
Data Sources are adapters to different storage implementations. A data source might be an adapter to a SQL database (an Active Record class in Rails or JPA in Java), an elastic search adapter, REST API, or even an adapter to something simple such as a CSV file or a Hash. A data source implements methods defined on the repository and stores the implementation of fetching and pushing the data.
Transport Layer can trigger an interactor to perform business logic. We treat it as an input for our system. The most common transport layer for microservices is the HTTP API Layer and a set of controllers that handle requests. By having business logic extracted into interactors, we are not coupled to a particular transport layer or controller implementation. Interactors can be triggered not only by a controller, but also by an event, a cron job, or from the command line.
Press enter or click to view image in full size 
The dependency graph in Hexagonal Architecture goes inward.
With a traditional layered architecture, we would have all of our dependencies point in one direction, each layer above depending on the layer below. The transport layer would depend on the interactors, the interactors would depend on the persistence layer.
In Hexagonal Architecture all dependencies point inward — our core business logic does not know anything about the transport layer or the data sources. Still, the transport layer knows how to use interactors, and the data sources know how to conform to the repository interface.
Get Netflix Technology Blog's stories in your inbox
Join Medium for free to get updates from this writer.
Subscribe
Subscribe [x]
Remember me for faster sign in
With this, we are prepared for the inevitable changes to other Studio systems, and whenever that needs to happen, the task of swapping data sources is easy to accomplish.
Swapping data sources
The need to swap data sources came earlier than we expected — we suddenly hit a read constraint with the monolith and needed to switch a certain read for one entity to a newer microservice exposed over a GraphQL aggregation layer. Both the microservice and the monolith were kept in sync and had the same data, reading from one service or the other produced the same results.
We managed to transfer reads from a JSON API to a GraphQL data source within 2 hours.
The main reason we were able to pull it off so fast was due to the Hexagonal architecture. We didn't let any persistence specifics leak into our business logic. We created a GraphQL data source that implemented the repository interface. A simple one-line change was all we needed to start reading from a different data source.
Press enter or click to view image in full size 
With a proper abstraction it was easy to change data sources
At that point, we knew that Hexagonal Architecture worked for us.
The great part about a one-line change is that it mitigates risks to the release. It is very easy to rollback in the case that a downstream microservice failed on initial deployment. This as well enables us to decouple deployment and activation, as we can decide which data source to use through configuration.
Hiding data source details
One of the great advantages of this architecture is that we are able to encapsulate data source implementation details. We ran into a case where we needed an API call that did not yet exist — a service had an API to fetch a single resource but did not have bulk fetch implemented. After talking with the team providing the API, we realized this endpoint would take some time to deliver. So we decided to move forward with another solution to solve the problem while this endpoint was being built.
We defined a repository method that would grab multiple resources given multiple record identifiers — and the initial implementation of that method on the data source sent multiple concurrent calls to the downstream service. We knew this was a temporary solution and that the second take at the data source implementation was to use the bulk API once implemented.
Press enter or click to view image in full size 
Our business logic doesn't need to be aware of specific data source limitations.
A design like this enabled us to move forward with meeting the business needs without accruing much technical debt or the need to change any business logic afterward.
Testing strategy
When we started experimenting with Hexagonal Architecture, we knew we needed to come up with a testing strategy. We knew that a prerequisite to great development velocity was to have a test suite that is reliable and super fast. We didn't think of it as a nice to have, but a must-have.
We decided to test our app at three different layers:
We test our interactors, where the core of our business logic lives but is independent of any type of persistence or transportation. We leverage dependency injection and mock any kind of repository interaction. This is where our business logic is tested in detail, and these are the tests we strive to have most of.
Press enter or click to view image in full size 
We test our data sources to determine if they integrate correctly with other services, whether they conform to the repository interface, and check how they behave upon errors. We try to minimize the amount of these tests.
Press enter or click to view image in full size 
We have integration specs that go through the whole stack, from our Transport / API layer, through the interactors, repositories, data sources, and hit downstream services. These specs test whether we “wired” everything correctly. If a data source is an external API, we hit that endpoint and record the responses (and store them in git), allowing our test suite to run fast on every subsequent invocation. We don't do extensive test coverage on this layer — usually just one success scenario and one failure scenario per domain action.
Press enter or click to view image in full size 
We don't test our repositories as they are simple interfaces that data sources implement, and we rarely test our entities as they are plain objects with attributes defined. We test entities if they have additional methods (without touching the persistence layer).
We have room for improvement, such as not pinging any of the services we rely on but relying 100% on contract testing . With a test suite written in the above manner, we manage to run around 3000 specs in 100 seconds on a single process.
It's lovely to work with a test suite that can easily be run on any machine, and our development team can work on their daily features without disruption.
Delaying decisions
We are in a great position when it comes to swapping data sources to different microservices. One of the key benefits is that we can delay some of the decisions about whether and how we want to store data internal to our application. Based on the feature's use case, we even have the flexibility to determine the type of data store — whether it be Relational or Documents.
At the beginning of a project, we have the least amount of information about the system we are building. We should not lock ourselves into an architecture with uninformed decisions leading to a project paradox.
The decisions we made make sense for our needs now and have enabled us to move fast. The best part of Hexagonal Architecture is that it keeps our application flexible for future requirements to come. 
8K
33 
Hexagonal Architecture
Software Architecture
API
Api Integration 
8K 
8K
33 
Follow
[
Published in Netflix TechBlog
](https://netflixtechblog.com/?source=post_page---post_publication_info--b315ec967749---------------------------------------)
184K followers
·
Last published 2 days ago
Learn about Netflix's world class engineering efforts, company culture, product developments and more.
Follow
Follow
[
Written by Netflix Technology Blog
](https://netflixtechblog.medium.com/?source=post_page---post_author_info--b315ec967749---------------------------------------)
456K followers
·
1 following
Learn more about how Netflix designs, builds, and operates our systems and engineering organizations
Follow
Responses (33)
 
Write a response
What are your thoughts?
Cancel
Respond
stickperson
Mar 10, 2020
39
Reply
Shekhar Gulati
Mar 13, 2020
27
2 replies
Reply
Luca Marzi
Mar 16, 2020
13
Reply
See all responses
More from Netflix Technology Blog and Netflix TechBlog
In
Netflix TechBlog
by
Netflix Technology Blog
[
The Human Infrastructure: How Netflix Built the Operations Layer Behind Live at Scale
By: Brett Axler, Casper Choffat, and Alo Lowry
](https://netflixtechblog.com/the-human-infrastructure-how-netflix-built-the-operations-layer-behind-live-at-scale-33e2a311c597?source=post_page---author_recirc--b315ec967749----0---------------------47219011_0142_4d1c_a2a8_0b20c5079962--------------)
Apr 17
A clap icon 305 A response icon 8   
In
Netflix TechBlog
by
Netflix Technology Blog
[
Evaluating Netflix Show Synopses with LLM-as-a-Judge
by Gabriela Alessio, Cameron Taylor, and Cameron R. Wolfe
](https://netflixtechblog.com/evaluating-netflix-show-synopses-with-llm-as-a-judge-6269251e6f28?source=post_page---author_recirc--b315ec967749----1---------------------47219011_0142_4d1c_a2a8_0b20c5079962--------------)
Apr 10
A clap icon 337 A response icon 4   
In
Netflix TechBlog
by
Netflix Technology Blog
[
Foundation Model for Personalized Recommendation
By Ko-Jen Hsiao, Yesu Feng and Sudarshan Lamkhede
](https://netflixtechblog.com/foundation-model-for-personalized-recommendation-1a0bd8e02d39?source=post_page---author_recirc--b315ec967749----2---------------------47219011_0142_4d1c_a2a8_0b20c5079962--------------)
Mar 21, 2025
A clap icon 2K A response icon 42   
In
Netflix TechBlog
by
Netflix Technology Blog
[
State of Routing in Model Serving
By Nipun Kumar, Rajat Shah, Peter Chng
](https://netflixtechblog.com/state-of-routing-in-model-serving-16e22fe18741?source=post_page---author_recirc--b315ec967749----3---------------------47219011_0142_4d1c_a2a8_0b20c5079962--------------)
May 1
A clap icon 357 A response icon 6  
See all from Netflix Technology Blog
See all from Netflix TechBlog
Recommended from Medium
In
UX Planet
by
Nick Babich
[
CLAUDE.md Best Practices
10 Sections to Include in your CLAUDE.md
](https://uxplanet.org/claude-md-best-practices-1ef4f861ce7c?source=post_page---read_next_recirc--b315ec967749----0---------------------dcec2d38_1c97_41ff_9fc9_e503cdfa87f9--------------)
Mar 6
A clap icon 1.3K A response icon 25   
In
Women in Technology
by
Alina Kovtun✨
[
Stop Memorizing Design Patterns: Use This Decision Tree Instead
Choose design patterns based on pain points: apply the right pattern with minimal over-engineering in any OO language.
](https://medium.com/womenintechnology/stop-memorizing-design-patterns-use-this-decision-tree-instead-e84f22fca9fa?source=post_page---read_next_recirc--b315ec967749----1---------------------dcec2d38_1c97_41ff_9fc9_e503cdfa87f9--------------)
Jan 29
A clap icon 7.9K A response icon 85   
Emily
[
I Failed Uber's System Design Interview Last Month. Here's Every Question They Asked.
It was much harder and the rejection email taught me more than any LeetCode grind ever could.
](https://medium.com/@emilyhustlenyc/i-failed-ubers-system-design-interview-last-month-here-s-every-question-they-asked-bdaf1bd6e64b?source=post_page---read_next_recirc--b315ec967749----0---------------------dcec2d38_1c97_41ff_9fc9_e503cdfa87f9--------------)
Feb 20
A clap icon 2.3K A response icon 50   
In
ExpoComputing
by
Cloud With Azeem
[
The Day a Google L7 Engineer Tore My System Design to Shreds
If you are not medium member read here for free
](https://medium.com/expocomputing/google-l7-system-design-interview-lessons-0b3834fded07?source=post_page---read_next_recirc--b315ec967749----1---------------------dcec2d38_1c97_41ff_9fc9_e503cdfa87f9--------------)
Feb 16
A clap icon 1.6K A response icon 37   
Jaydeep Karale
[
The Bloom Filter: How Big Tech Avoids Expensive Database Lookups
The Brilliant Data Structure That Intentionally Lies (And Why Your Favorite Apps Depend On It)
](https://medium.com/@_jaydeepkarale/the-bloom-filter-how-big-tech-avoids-expensive-database-lookups-1a109d05bc2f?source=post_page---read_next_recirc--b315ec967749----2---------------------dcec2d38_1c97_41ff_9fc9_e503cdfa87f9--------------)
Dec 13, 2025
A clap icon 374 A response icon 10   
Lucas Didier
[
How to Write Product Specs in 2025 (Spoiler: It Takes 10 Minutes Now)
There's a particular kind of irony that only product managers truly appreciate: I used to spend hours writing specifications about features…
](https://medium.com/@lucdid/how-to-write-product-specs-in-2025-spoiler-it-takes-10-minutes-now-d249c43a7c95?source=post_page---read_next_recirc--b315ec967749----3---------------------dcec2d38_1c97_41ff_9fc9_e503cdfa87f9--------------)
Dec 10, 2025
A clap icon 7 A response icon 2  
See more recommendations
Help
Status
About
Careers
Press
Blog
Privacy
Rules
Terms
Text to speech
