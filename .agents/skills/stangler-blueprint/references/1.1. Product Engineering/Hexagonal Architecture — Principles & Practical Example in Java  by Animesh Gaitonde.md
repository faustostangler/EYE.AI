---
name: Hexagonal Architecture — Principles & Practical Example in Java | by Animesh Gaitonde
keywords: (placeholder)
metadata:
  url: https://itnext.io/hexagonal-architecture-principles-practical-example-in-java-364bb2e50075
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Hexagonal Architecture — Principles & Practical Example in Java | by Animesh Gaitonde | ITNEXT
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
ITNEXT
](https://itnext.io/?source=post_page---publication_nav-5b301f10ddcd-364bb2e50075---------------------------------------)
·
Follow publication
ITNEXT is a platform for IT developers & software engineers to share knowledge, connect, collaborate, learn and experience next-gen technologies.
Follow publication
Hexagonal Architecture — Principles & Practical Example in Java
Animesh Gaitonde
Follow
6 min read
·
Jan 13, 2020 
331
3 
Listen
Share
Implementation of Hexagonal Architecture or Ports & Adapter Architecture
Press enter or click to view image in full size 
Background
As developers, at some or the other point, you have worked on legacy software that is not well maintained. You understand the pain to comprehend simple logic written in complex blocks of code. Further, introducing an enhancement or a new feature gives nightmares to developers.
Maintainability is at the heart of good software design. Codebases that are not well maintained become difficult to manage. Not only they become difficult to scale but also give a hard time to a new developer to onboard & hit the ground running.
In the Tech world, everything moves at a rapid pace. Assume that you are owning a legacy project. If the business asks you to ship a new feature A.S.A.P or you want to move from RDBMS to NoSQL, what would be your first reaction? 
Thrash your machine?
High test coverage boosts a developer's confidence to deploy a new release seamlessly. However, if your application & infrastructure logic is intertwined, would it possible to test your business logic in isolation? That will just aggravate your frustration. 
Why me?
That's enough of ranting, let's have a tour of Hexagonal Architecture along with an illustration. Adopting this pattern will help you improve the maintainability, testability of codebase along with many other benefits.
Introduction to Hexagonal Architecture
In 2006, Alistair Cockburn coined the term Hexagonal Architecture. This architecture is also known as the Ports And Adapters Architecture. In simple words, the idea is to expose multiple endpoints in software for communication. As long as you have the right adapter for your port, your request will always get handled.
It's analogous to exposing multiple USB ports on a Machine. If you have the right adapter (mobile charger, or Pendrive) that fits into your Machine's port, you'll be able to meet your goal. 
Adapter
Software is diagrammatically represented in the form of a hexagon & application business logic forms it's core. It's surrounded by entities with which it communicates & components that drive it by providing inputs.
In real-world, different entities such as user actions, API calls, automated scripts & unit tests interact with your software and provide various inputs. In case your business logic becomes entangled with user interface code, you'll observer multiple difficulties. For eg:- It will become cumbersome to switch from user-driven input to a unit test-driven input.
Similarly, an application interacts with external entities such as Databases, message queues, web servers through HTTP API calls, etc. If you want to migrate database or dump data to a file system instead, you should be able to achieve this without touching your business logic.
As the name ' Ports And Adapter' suggests, it defines ports which are means through which communication takes place. Adapters are components that handle user input and convert it into language-specific message call in the core. Likewise, adapters encapsulate the logic to interact with external systems such as databases, message queues, etc and facilitate communication between core and external objects.
Working
Let's go through a deep walkthrough of the pattern. The below diagram shows the different layers in which the application is divided:-
Press enter or click to view image in full size 
Hexagonal Architecture
Hexagonal architecture divides the application into three layers — Domain, Application & Framework. Following is a brief description of the three layers
Domain — This layer contains the core business logic. It's not supposed to know the implementation details of the outer layers
Application — This layer acts as a glue between the domain and the framework
Framework — It implements how domain interacts with the external world. Inner layers act as a black box for this layer
According to the architecture, two actors — Primary & Secondary interact with the application. The Primary actors send request or drive the application. For example — Users or automated test suite. Secondary actors provide infrastructure to the domain to communicate with external entities. For example — Database adapters, TCP or HTTP client.
Let's represent the actors in the below diagram:-
Press enter or click to view image in full size 
Hexagonal Architecture
The left side of the Hexagon consists of drivers (which provide input to the core) while the right side represents all the components that are driven by our application.
Illustration
Let's design an Application that stores movie reviews. The user can query the application with a movie name. The app returns random five reviews for the given movie.
For simplicity, let's assume it's a console app. Movie reviews data is stored in memory. The user response is printed on the console.
We have the User which sends the request to the app. Thus, the User becomes a driver. The app can fetch data from any data store. The application can either write the response on the console or a file. So, data fetcher and response printer becomes the driven entities.
The driver and driven components are explained in the below figure:-
Press enter or click to view image in full size 
Hexagonal Architecture of Movie Review App
On the left, we have the driver which provides input to the app. Driven components are on the right which enables the App to communicate with Database and console.
Get Animesh Gaitonde's stories in your inbox
Join Medium for free to get updates from this writer.
Subscribe
Subscribe [x]
Remember me for faster sign in
Let's have a quick Code walkthrough of the above App.
Driver Port
Driver Port
Driven Ports
Driven Ports
Driven Port Adapter
The movie fetcher will extract movies from the movies repo. We will have a console printer which will print movie reviews on the console. Let's implement the above two interfaces.
ConsolePrinter and MovieReviewsRepo
Domain
Our core domain handles user requests. The core will fetch movies, process them and pass the results to the printer. For now, we only have one request i.e search for Movies. We will use the standard Java Consumer interface to handle user requests.
Let's have a look at our core domain class i.e MovieApp.
Movie App
We will now define a Command mapper which will map the commands with specific handlers.
Command Mapper
Driver Adapter
The user will interact with our system through the IUserInput interface. Let's implement this interface. The implementation will build a use case model. It will use the model runner and delegate the action.
Primary Actor
We will now take a look at our primary actor the user which will use the above interface for communication.
Movie User
Movie application
We will now create the console application. We will add the driven adapters as a dependency in our application. The user will be creating and sending the request to the application. The application will fetch the data, process and print the response on console.
Movie Application
New features/Changes
In the above example, you could easily switch from one datastore to another with minimal change. Datastore dependency can be injected into the code without altering the existing business logic. For instance, you can move the in-memory data to a database, write & inject a database adapter into the application
Similarly, instead of a Console Printer, you could have a Printer that would write to a file system. It becomes simple to introduce new features and fix bugs in such a layered application
You can write comprehensive tests to test your business logic. Adapters can be tested in isolation. Thus, the overall test coverage of the application can be improved
Conclusion
We have learned the following benefits of adopting hexagonal architecture:-
Maintainability — We build layers that are loosely coupled and independent. It becomes easy to add new features in one layer without affecting other layers.
Testability — Unit tests are cheap to write and fast to run. We can write tests for each layer. We can mock the dependencies while testing. For example:- We can mock a database dependency by adding an in-memory datastore.
Adaptability — Our core domain becomes independent of changes in external entities. For eg:- If we plan to use a different database, we don't need to change the domain. We can introduce the appropriate database adapter.
References
Hexagonal Architecture by Alistair Cockburn
Hexagonal Architecture-Wiki
Ports And Adapters Architecture
Giphy 
331
3 
Software Architecture
Best Practices
Software Development
Software Engineering
Java 
331 
331
3 
Follow
[
Published in ITNEXT
](https://itnext.io/?source=post_page---post_publication_info--364bb2e50075---------------------------------------)
81K followers
·
Last published 11 hours ago
ITNEXT is a platform for IT developers & software engineers to share knowledge, connect, collaborate, learn and experience next-gen technologies.
Follow
Follow
[
Written by Animesh Gaitonde
](https://animeshgaitonde.medium.com/?source=post_page---post_author_info--364bb2e50075---------------------------------------)
4K followers
·
58 following
SDE-3/Tech Lead @ Amazon| ex-Airbnb | ex-Microsoft. Writes about Distributed Systems, Programming Languages & Tech Interviews
Follow
Responses (3)
 
Write a response
What are your thoughts?
Cancel
Respond
Alexander Kriegisch
Jul 17, 2020
11
Reply
Emre Kizildas
Jan 16, 2020
4
Reply
Serguei Cambour
Aug 3, 2022 (edited)
Reply
More from Animesh Gaitonde and ITNEXT
In
ITNEXT
by
Animesh Gaitonde
[
Rate Limiting System Design: Algorithms, Trade-offs and Best Practices
A deep dive into token bucket, leaky bucket, and sliding window techniques with real-world system design applications
](https://itnext.io/rate-limiting-system-design-algorithms-trade-offs-and-best-practices-c6019cb2dd85?source=post_page---author_recirc--364bb2e50075----0---------------------c3c38797_cba8_4955_9202_e4f6bb6f4a52--------------)
Mar 29
A clap icon 150 A response icon 5   
In
ITNEXT
by
Denys Poltorak
[
The Map of System Topologies
This article explores a map of common software architectures based on the amount of their partitioning into layers and subdomains.
](https://itnext.io/the-map-of-system-topologies-e2d3d0b89618?source=post_page---author_recirc--364bb2e50075----1---------------------c3c38797_cba8_4955_9202_e4f6bb6f4a52--------------)
5d ago
A clap icon 70 A response icon 1   
In
ITNEXT
by
Jacob Ferus
[
Cursor Is Dying
Cursor is a great product. It was one of the first great applications of AI in coding, moving past copy-pasting code from chats. But the AI…
](https://itnext.io/cursor-is-dying-0ed76b4a38b3?source=post_page---author_recirc--364bb2e50075----2---------------------c3c38797_cba8_4955_9202_e4f6bb6f4a52--------------)
Feb 11
A clap icon 622 A response icon 37   
In
ITNEXT
by
Animesh Gaitonde
[
From Cron to Distributed Schedulers: Scaling Job Execution to Thousands of Jobs per Second
Designing a Distributed Job Scheduler for High-Throughput and Correctness at Scale
](https://itnext.io/from-cron-to-distributed-schedulers-scaling-job-execution-to-thousands-of-jobs-per-second-ef05955bf3d9?source=post_page---author_recirc--364bb2e50075----3---------------------c3c38797_cba8_4955_9202_e4f6bb6f4a52--------------)
Feb 17
A clap icon 570 A response icon 5  
See all from Animesh Gaitonde
See all from ITNEXT
Recommended from Medium
In
Javarevisited
by
Arvind Kumar
[
HashMap Deep Dive: Internal Working, Collision Handling & Treeification (Java 8+)
If you've used Java for even a short time, you've used HashMap. But most developers stop at “O(1) lookup” — which is only half the story.
](https://medium.com/javarevisited/hashmap-deep-dive-internal-working-collision-handling-treeification-java-8-7dfc93abff6d?source=post_page---read_next_recirc--364bb2e50075----0---------------------f245aba7_332e_4cc9_a554_84b80839e4c4--------------)
Apr 22
A clap icon 134   
In
Women in Technology
by
Alina Kovtun✨
[
Stop Memorizing Design Patterns: Use This Decision Tree Instead
Choose design patterns based on pain points: apply the right pattern with minimal over-engineering in any OO language.
](https://medium.com/womenintechnology/stop-memorizing-design-patterns-use-this-decision-tree-instead-e84f22fca9fa?source=post_page---read_next_recirc--364bb2e50075----1---------------------f245aba7_332e_4cc9_a554_84b80839e4c4--------------)
Jan 29
A clap icon 7.9K A response icon 85   
Java Interview
[
If You're a Java Developer Ignoring Spring AI, You're Already Falling Behind
A few years ago, being a solid Java developer meant knowing Spring Boot, REST APIs, microservices, and maybe some Kafka on the side.
](https://medium.com/@kaurharjeet122/if-youre-a-java-developer-ignoring-spring-ai-you-re-already-falling-behind-2fc816d43ab7?source=post_page---read_next_recirc--364bb2e50075----0---------------------f245aba7_332e_4cc9_a554_84b80839e4c4--------------)
Apr 25
A clap icon 25   
Jaydeep Karale
[
The Bloom Filter: How Big Tech Avoids Expensive Database Lookups
The Brilliant Data Structure That Intentionally Lies (And Why Your Favorite Apps Depend On It)
](https://medium.com/@_jaydeepkarale/the-bloom-filter-how-big-tech-avoids-expensive-database-lookups-1a109d05bc2f?source=post_page---read_next_recirc--364bb2e50075----1---------------------f245aba7_332e_4cc9_a554_84b80839e4c4--------------)
Dec 13, 2025
A clap icon 374 A response icon 10   
In
@Override
by
Ahmet Emre DEMİRŞEN
[
Handling 100k Requests with Java Virtual Threads
Have you ever wondered how your Java application would fare under a sudden surge of 100,000 concurrent requests? The thought alone can send…
](https://medium.com/but-it-works-on-my-machine/handling-100k-requests-with-java-virtual-threads-898233c2184b?source=post_page---read_next_recirc--364bb2e50075----2---------------------f245aba7_332e_4cc9_a554_84b80839e4c4--------------)
Jan 25
A clap icon 209 A response icon 3   
Leo Godin
[
Claude Code is Great
You Just Need to Learn How to Use It
](https://leo-godin.medium.com/claude-code-is-great-6db35d8685f0?source=post_page---read_next_recirc--364bb2e50075----3---------------------f245aba7_332e_4cc9_a554_84b80839e4c4--------------)
Mar 2
A clap icon 3.5K A response icon 99  
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
