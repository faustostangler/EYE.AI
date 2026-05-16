---
name: 2026-05-10 Hexagonal Architecture: Striking a Balance between Modularity and Efficiency | by Tom Bruyninx | Medium
keywords: (placeholder)
metadata:
  url: None
  source: SOURCE_TYPE_TEXT
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
WebSync metadata
title: Hexagonal Architecture: Striking a Balance between Modularity and Efficiency | by Tom Bruyninx | Medium
url: https://medium.com/@tom.bruyninx/hexagonal-architecture-striking-a-balance-between-modularity-and-efficiency-5f79ba3cf500
date: 2026-05-10T21:31:16.193Z
parsing method: defuddle
Sitemap
Photo by Markus Spiske on Unsplash
Introduction
I have been part of a software development team at a large media company in Belgium for over 3 years. During that time, we have made significant strides in maturing our development processes. We practiced Test-Driven Development, embraced Hexagonal Architecture and “Ports and Adapters,” and our projects are all set up with Continuous Integration and Continuous Deployment in mind. We were doing all the right things for all the right reasons. Despite all these efforts, our team’s understanding of Hexagonal Architecture may not be as solid as I had thought.
Recently, we had discussion in the team about where to put a piece of logic in our code. Some team members were of the opinion that the piece of logic was part of the domain, others suggested it should be part of the adapter implementation.
During the discussion I noticed that doing things this way had become a habit instead of a well thought through practice. I realized that our team’s understanding of Hexagonal Architecture had become more of a process than a well-informed decision.
This post aims to reevaluate the reasons why we chose to use Hexagonal Architecture, the benefits it brings, and the potential drawbacks of using it in our development process. By taking a step back and critically examining our approach, we can ensure that we are making the best decisions for our codebase as a team.
What is Hexagonal Architecture / Ports and Adapters
Hexagonal Architecture, also known as the “ports and adapters” pattern, is a widely researched and well-established architectural design pattern. It has a proven track record of success in many production systems around the world.
It is related to other architecture patterns like explicit architecture, clean architecture, onion architecture and it is closely aligned with Domain-Driven Design (DDD) and other best practices such as Test-Driven Development (TDD) and Behavior-Driven Development (BDD).
This summary aims to provide a brief overview of what Hexagonal Architecture is and its advantages and disadvantages. For a more in-depth understanding of this pattern, there are many excellent blog posts and resources available. (See below.)
So what is Hexagonal Architecture?
In essence, Hexagonal Architecture is an architectural pattern that improves the adaptability of code to changing circumstances through the decoupling of concerns. It emphasizes on separating the core business logic of a system from the various ways in which that system can be interacted with, such as through a web interface or a command line interface. This approach allows for a clean separation of concerns and makes it easier to test the system, making it more adaptable to changing requirements.
In short, Hexagonal Architecture means splitting our application into three parts: primary adapters, the application core, and secondary adapters, with the goal of minimizing the amount of coupling between boundaries.
Primary adapters are responsible for communicating with the application core and handling all incoming requests.
The application core is responsible for the application logic and wraps the domain logic inside. It also manages the communication between the application core and the secondary adapters.
Secondary adapters are responsible for communicating with other services and infrastructure that are needed to execute the business logic in the application core.
There are two important points to keep in mind:
The application core is completely separate from the adapters and defines its requirements through interfaces that are connected using dependency injection.
Ports are designed to meet the needs of the application core, and adapters are specific implementations of these needs.
This is very well described in a blog post by Herberto Graça: https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together/#connecting-the-tools-and-the-application-core
Advantages
Clear Separation of concerns: By isolating the core business logic from the various inputs and outputs, hexagonal architecture makes it easier to understand the system and how each component is responsible for specific functionality. (Single responsibility principle.)
Improved testability: By isolating the core of the system from the adapters, it is easier to test the business logic in isolation, making it easier to ensure the system is working correctly.
Increased flexibility: Hexagonal architecture makes it easy to add new inputs and outputs without affecting the core business logic, making it easy to adapt to changing requirements and reuse the business logic.
Enhanced maintainability: Hexagonal architecture is more modular, making it easier to understand, test and maintain. The well-defined dependencies between components make it easier to make changes to the system without introducing new bugs.
Disadvantages
Increased complexity: Hexagonal architecture introduces additional layers and abstractions. This can make the system more complex to understand and maintain.
Additional overhead: The additional layers and abstractions can add some overhead to the system, which can make it less efficient.
Extended development time: More layers and abstractions can make it more time-consuming to develop and test the system. This can increase the overall development time. However, it is important to note that with proper planning, documentation, and experienced team members, these challenges can be mitigated.
The team discussion
As with any approach, it is important to find a balance when applying Hexagonal Architecture principles. During the team discussion, it was pointed out that in our specific use case, the increased development time and added complexity outweighed the benefits of proper Hexagonal Architecture.
In situations where the application core is minimal or non-existent, it can be tempting to not establish proper boundaries between different pieces of code. However, this approach can become a slippery slope very fast. It can only be countered by discipline and a good understanding of when to separate logic and when not to.
We often use the existing codebase as a reference for further development. This habit encourages the use of the existing design over introducing a better separation of concerns. With every development we should strive to refactor towards a better architecture for our ever changing use case. “First make the change easy, then make the easy change.” this however is not always so straightforward to do.
During our discussion we looked at four different options. The goal was to evaluate the level of coupling between components in each design but also discuss the number of components we would need to write. Whether the separation between components actually added value or if they just added complexity.
Our use case
We need to develop an application that listens to an event. Based on the input provided in the event we need to retrieve data from an internal API, map the data to an internationally recognized standard format, save it to a file and then transfer it to a third-party FTP server.
Example 1: Direct coupling between adapters
In the first approach, we wired everything in the event listener. This method has a direct dependence on the internal API’s model. The event listener is responsible for handling the incoming event, retrieving data from the internal service, mapping it to the international standard format, and sending it to the FTP Adapter.
Example 1: Direct coupling between adapters
All components are highly coupled.
A change in one component will most likely require a change in all components.
Not possible to test logic in isolation.
Example 2: Introduction of application service
In the second approach, we introduced an application service. The event listener is responsible for directing the application service on what actions to take. The coordination of the logic is encapsulated within the application service inside the application core.
However, this approach still relies on the data models used by the primary and secondary adapters. Both the incoming DTO and the internal service DTO are owned by their respective adapters.
Example 2: Introduction of application service
Primary adapter is decoupled of the application logic and has a single responsibility.
Application core is responsible for orchestrating our functionality and accessing the secondary adapters.
A change in the model of one of the adapters will ripple through our application.
We can test logic in isolation, but our tests are dependent on external models.
Example 3: Decouple application core from external data models
In this third approach, we improved the coupling between components even further. By introducing new objects owned by the application core and mapping the adapter DTOs to these new objects, we prevent the models of the adapters from leaking into the application core.
This means that changes in the format of an adapter’s DTO will no longer affect the application core. But our application is still dependent on the international standard format for the outgoing data. A change in this format would require changes in the application core and possibly in the adapter implementation.
In this example, the application core is still closely tied to the adapter implementation. The issues may seem subtle, but they become more pronounced when considering future possibilities.
For example, if we need to change the format or support multiple formats for the same data, dependent on the type of adapter, it would be difficult to accommodate these changes in the current design without significant changes to the application core.
Example 3: Decouple application core from external data models
All the advantages of example 2.
A change in the model of one of the adapters will not ripple through our application anymore.
We can test logic in isolation our tests are independent
However this design is not future proof for additional formats.
Example 4: Decouple from external outgoing data formats
In the final example, we move the formatting logic to the secondary adapter and make the application core “pure.” This means that there are no longer any external dependencies that can cause changes to our application model. Only new functional requirements can drive changes in the application core.
This allows us to be more future-proof and implement new features more efficiently.
Example 4: Decouple from external outgoing data formats
All the advantages of example 3.
A change in data model of one of the adapters will not drive change in the application core.
Only new functional requirements can implicate change in the application core.
We can support new formats and multiple adapters without harm to our application core.
Conclusion
In my opinion we should always strive towards example four. The approach provides a strong foundation for future requirements and allows for easy expansion. I favour clear boundaries over a faster development time. The downside of a longer upfront development cost, added compelxity and overhead does not outweigh the advantages Hexagonal Architecture brings when optimizing for future changes.
It is important to remember that complexity should not be introduced for the sake of complexity, but all aspects should be evaluated when deciding in favour of or against Hexagonal Architecture. If the application is expected to grow and require changes to its functionality, it is best to aim for the least amount of coupling possible by implementing a pure application core for maximum flexibility. If no future changes are planned and the external data models are expected to be stable, a higher coupling in exchange for decreased development time can be considered.
We should, however, keep in mind that this is a slippery slope and if new features are added without a proper foundation of loosely coupled architecture, it can lead to trouble in the future.
Source material
https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together/
https://chat.openai.com/
I am a software developer. Passionate about Test-Driven Design and Clean Architecture. My main focus is on building web applications and API's.
