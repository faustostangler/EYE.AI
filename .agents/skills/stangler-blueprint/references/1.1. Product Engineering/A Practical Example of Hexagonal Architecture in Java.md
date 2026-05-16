---
name: A Practical Example of Hexagonal Architecture in Java
keywords: (placeholder)
metadata:
  url: https://www.dineshonjava.com/a-practical-example-of-hexagonal-architecture-in-java/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
A Practical Example of Hexagonal Architecture in Java - Dinesh on Java
Core Java
Core Java
Java 8 Certification
Interview Q/A
Spring Boot
Spring
Spring Core
Spring AOP
Spring MVC
Spring Security
Microservices
Spring 4
Spring 5
Spring Batch
Spring Mobile
Spring HATEOAS
Hibernate
Hibernate Search
Tutorials
Design Patterns
Web Services
WS Interview Questions
JAX-WS (SOAP)
JAX-RS (REST)
WSDL
SOAP
Cloud Computing
Struts 2 Tutorial
J2EE Tutorial
Servlet Tutorial
JSP Tutorial
JSTL Tutorial
JDBC Tutorial
JAX B Tutorial
Java Mail API
Hadoop Tutorial
AJAX Tutorial
Build Tools
Maven
Gradle
ANT
Mongo DB
Thymeleaf
Git
Linux
Interview Q/A
Spring Interview
AOP Interview
MVC Interview
Spring Boot Interview
Microservices Interview
Spring Security Interview
Web Service Interview
Training
Who I Am
Privacy Policy
Home
Design Pattern
A Practical Example of Hexagonal Architecture in Java
February 14, 2020
No Comments
A Practical Example of Hexagonal Architecture in Java
Hexagonal architecture is an application design pattern. It solves some problems of the layered architecture by introducing ports-and-adapter for the dependencies between our components of the application toward our domain objects. The domain objects are the core part of the application and it is the part of inside a hexagon. And other parts such as web interface, DB, messaging systems, etc are outside of a hexagon.
Hexagonal Architecture Diagram
Let's discuss in details each of the stereotypes in this architecture style.
Core application part
Domain Objects are the core parts of an application. These have business rules and validations and also have state and behaviour. This core application part doesn't have any outward dependency. These are pure core business logic services. Domain objects will be changed when the business requirement will be changed otherwise they never affect the changes in other layers.
Let's see the following domain class Account of the core application, it has account-related information and business validations.
Inbound and outbound ports
In the Hexagonal architecture pattern, the ports provide the flow to the application from outside and inside.
Inbound ports
An inbound port provides the flow and the application functionality to the outside. An inbound port is a service interface that exposes the core logic and can be called by outside components. You can see the following example of an inbound port:
Outbound ports
An outbound port provides the outside functionality or interface. The core application calls this output port as per requirement such as external database call etc. For example, a simple repository interface AccountRepository that provides a port to enable communication from the core application to a database. This simple repository interface is an outbound port. Let's see the following example of an outbound port:
Adapters
Adapters are nothing but these are the implementation of inbound and outbound ports. The adapters from the outside of the hexagonal architecture and they are not part of the core application. They only interact with the core application from outside by using inbound and outbound ports.
Input adapters
The input adapters are also known as primary or driving adapters. These drive the application by invoking actions on the application using the inbound ports of application.
For example, the AccountController provides REST APIs or web interfaces as the input adapters. The REST controllers use the service interfaces (inbound ports) to interact with the core part of the business logic of the application.
Output adapters
The output adapters are also known as secondary or driven adapters. These are the implementation of the outbound ports. These are driven by the core application using the outbound ports to find the connections to the database and external APIs.
For example, the AccountRepositoryImpl provides an interface to the core application to communicate to external dependency such as the database.
Use cases of a core application
In the Hexagonal architecture, the use cases and business domain objects are inside of the hexagonal. The use cases are nothing but it is specific use case implementation of the inbound port to communication from the core to the downstream system. Let's see the following use case implementation AccountServiceImpl provides a use case for a specific requirement:
Conclusion
In the article, we have discussed the Hexagonal application architecture with a quick example in Java. This architecture focuses to simplify application design with external and internal dependencies.
Previous
Share this:
Click to share on Facebook (Opens in new window)
Click to share on Twitter (Opens in new window)
Click to share on LinkedIn (Opens in new window)
Click to share on WhatsApp (Opens in new window)
Click to share on Telegram (Opens in new window)
9 Click to share on Pinterest (Opens in new window) 9
Design Pattern Java
Related Posts
Best Practices in Programming to Decide Name of Variables, Methods, Classes and Packages
Service to Worker Pattern – Core J2EE Patterns
Builder Design Pattern – Creational Patterns
How to remove duplicate items from ArrayList in Java?
Composite Pattern – Structural Design Patterns in Java
Data Access Object (DAO) – Core J2EE Patterns
About The Author
Dinesh Rajput
Dinesh Rajput is the chief editor of a website Dineshonjava, a technical blog dedicated to the Spring and Java technologies. It has a series of articles related to Java technologies. Dinesh has been a Spring enthusiast since 2008 and is a Pivotal Certified Spring Professional, an author of a book Spring 5 Design Pattern, and a blogger. He has more than 10 years of experience with different aspects of Spring and Java design and development. His core expertise lies in the latest version of Spring Framework, Spring Boot, Spring Security, creating REST APIs, Microservice Architecture, Reactive Pattern, Spring AOP, Design Patterns, Struts, Hibernate, Web Services, Spring Batch, Cassandra, MongoDB, and Web Application Design and Architecture. He is currently working as a technology manager at a leading product and web development company. He worked as a developer and tech lead at the Bennett, Coleman & Co. Ltd and was the first developer in his previous company, Paytm. Dinesh is passionate about the latest Java technologies and loves to write technical blogs related to it. He is a very active member of the Java and Spring community on different forums. When it comes to the Spring Framework and Java, Dinesh tops the list!
Learn various design patterns and best practices and use them to solve common design problems.
Learn Spring Boot 2.0 and Spring Cloud Application Microservices Architecture to solve common cloud native problems.
Designing Applications with Spring Boot 2.2 and React JS: Let us full stack development with Spring Boot and React JS.
Hands-On Microservices - Monitoring and Testing: A performance engineer's guide to the continuous testing and monitoring of microservices.  
Dinesh on Java Copyright © 2026.
Core Java
Core Java
Java 8 Certification
Interview Q/A
Spring Boot
Spring
Spring Core
Spring AOP
Spring MVC
Spring Security
Microservices
Spring 4
Spring 5
Spring Batch
Spring Mobile
Spring HATEOAS
Hibernate
Hibernate Search
Tutorials
Design Patterns
Web Services
WS Interview Questions
JAX-WS (SOAP)
JAX-RS (REST)
WSDL
SOAP
Cloud Computing
Struts 2 Tutorial
J2EE Tutorial
Servlet Tutorial
JSP Tutorial
JSTL Tutorial
JDBC Tutorial
JAX B Tutorial
Java Mail API
Hadoop Tutorial
AJAX Tutorial
Build Tools
Maven
Gradle
ANT
Mongo DB
Thymeleaf
Git
Linux
Interview Q/A
Spring Interview
AOP Interview
MVC Interview
Spring Boot Interview
Microservices Interview
Spring Security Interview
Web Service Interview
Training
Who I Am
Privacy Policy 
