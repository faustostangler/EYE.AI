---
name: How to Implement a Hexagonal Architecture - freeCodeCamp
keywords: (placeholder)
metadata:
  url: https://www.freecodecamp.org/news/implementing-a-hexagonal-architecture/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
How to Implement a Hexagonal Architecture
Menu Menu
Forum
Curriculum
Donate
Learn to code — free 3,000-hour curriculum
June 19, 2019 / #Clean Architecture
How to Implement a Hexagonal Architecture
By Bertil Muth
A hexagonal architecture simplifies deferring or changing technology decisions. You want to change to a different framework? Write a new adapter. You want to use a database, instead of storing data in files? Again, write an adapter for it.
Draw a boundary around the business logic. The hexagon. Anything inside the hexagon must be free from technology concerns.
The outside of the hexagon talks with the inside only by using interfaces, called ports. Same the other way around. By changing the implementation of a port, you change the technology.
Isolating business logic inside the hexagon has another benefit. It enables writing fast, stable tests for the business logic. They do not depend on web technology to drive them, for example.
Here's an example diagram. It shows Spring MVC technology as boxes with dotted lines, ports and adapters as solid boxes, and the hexagon without its internals: 
An adapter translates between a specific technology and a technology free port. The PoemController adapter on the left receives requests and sends commands to the IReactToCommands port. The PoemController is a regular Spring MVC Controller. Because it actively uses the port, it's called a driver adapter. IReactToCommands is called a driver port. Its implementation is inside the hexagon. It's not shown on the diagram.
On the right side, the SpringMvcPublisher adapter implements the IWriteLines port. This time, the hexagon calls the adapter through the port. That's why SpringMvcPublisher is called a driven adapter. And IWriteLines is called a driven port.
I show you how to implement that application. We go all the way from a user story to a domain model inside the hexagon. We start with a simple version of the application that prints to the console. Then we switch to Spring Boot and Spring MVC.
From a user story to ports & adapters
The company FooBars.io decides to build a Poetry App. The product owner and the developers agree on the following user story:
As a reader
I want to read at least one poem each day
So that I thrive as a human being
As acceptance criteria, the team agrees on:
When the user asks for a poem in a specific language, the system displays a random poem in that language in the console
It's ok to "simulate" the user at first, i.e. no real user interaction. (This will change in future versions.)
Supported languages: English, German
The developers meet and draw the following diagram: 
So the SimulatedUser sends commands to the IReactToCommands port. It asks for poems in English and German. Here's the code, it's available on Github.
poem/simple/driver_adapter/ SimulatedUser.java
The IReactToCommands port has only one method to receive any kind of command.
poem/boundary/driver_port/ IReactToCommands.java
AskForPoem is the command. Instances are simple, immutable POJOs. They carry the language of the requested poem.
poem/command/ AskForPoem.java
And that's it for the left, driver side of the hexagon. On to the right, driven side. 
When the SimulatedUser asks the IReactToCommands port for a poem, the hexagon:
Contacts the IObtainPoems port for a collection of poems
Picks a random poem from the collection
Tells the IWriteLines port to write the poem to the output device
You can't see Step 2 yet. It happens inside the hexagon, in the domain model. That's the business logic of the example. So we focus on Step 1 and Step 3 first.
In Step 1, the collection of poems is a language dependent, hard coded array. It's provided by the HardcodedPoemLibrary adapter that implements the IObtainPoems port.
poem/boundary/driven_port/ IObtainPoems.java
poem/simple/driven_adapter/ HardcodedPoemLibrary.java
In Step 3, the ConsoleWriter adapter writes the lines of the poems to the output device, i.e. the console.
poem/boundary/driven_port/ IWriteLines.java
poem/simple/driven_adapter/ ConsoleWriter.java
We have created all the ports, and a simple implementation of all the adapters. So far, the inside of the hexagon remained a mystery. It's up next. 
Command handlers (inside the hexagon)
When a user asks for a poem, the system displays a random poem.
Similar in the code: when the IReactToCommands port receives an AskForPoem command, the hexagon calls a DisplayRandomPoem command handler.
The DisplayRandomPoem command handler obtains a list of poems, picks a random one and writes it to the output device. This is exactly the list of steps we talked about in the last clause.
poem/boundary/internal/command_handler/ DisplayRandomPoem.java
It's also the job of the command handler to translate between the domain model data and the data used in the port interfaces.
Tying commands to command handlers
In my implementation of a hexagonal architecture, there is only a single driver port, IReactToCommands . It reacts to all types of commands.
The Boundary class is the implementation of the IReactToCommands port. It creates a behavior model using a library. The behavior model maps each command type to a command handler. Then, a behavior dispatches the commands based on the behavior model.
poem/boundary/ Boundary.java
The domain model
The domain model of the example doesn't have very interesting functionality. The RandomPoemPicker picks a random poem from a list.
A Poem has a constructor that takes a String containing line separators, and splits it into verses.
The really interesting bit about the example domain model: it doesn't refer to a database or any other technology, not even by interface!
That means that you can test the domain model with plain unit tests. You don't need to mock anything.
Such a pure domain model is not a necessary property of an application implementing a hexagonal architecture. But I like the decoupling and testability it provides.
Plug adapters into ports, and that's it
A final step remains to make the application work. The application needs a main class that creates the driven adapters. It injects them into the boundary.
It then creates the driver adapter, for the boundary, and runs it.
poem/simple/ Main.java
And that's it! The team shows the result to the product owner. And she's happy with the progress. Time for a little celebration. 
Switching to Spring
The team decides to turn the poem app into a web application. And to store poems in a real database. They agree to use the Spring framework to implement it.
Before they start coding, the team meets and draws the following diagram: 
Instead of a SimulatedUser , there is a PoemController now, that sends commands to the hexagon.
poem/springboot/driver_adapter/ PoemController.java
When receiving a command, the PoemController calls springMvcBoundary.basedOn(webModel) . This creates a new Boundary instance, based on the webModel of the request:
poem/springboot/boundary/ SpringMvcBoundary.java
The call to reactTo() sends the command to the boundary, as before. On the right side of the hexagon, the SpringMvcPublisher adds an attribute lines to the Spring MVC model. That's the value Thymeleaf uses to insert the lines into the web page.
poem/springboot/driven_adapter/ SpringMvcPublisher.java
The team also implements a PoemRepositoryAdapter to access the PoemRepository . The adapter gets the Poem objects from the database. It returns the texts of all poems as a String array.
poem/springboot/driven_adapter/ PoemRepositoryAdapter.java
Finally, the team implements the Application class that sets up an example repository and plugs the adapters into the ports.
And that's it. The switch to Spring is complete.
Conclusion
There are many ways to implement a hexagonal architecture. I showed you a straightforward approach that provides an easy to use, command driven API for the hexagon. It reduces the number of interfaces you need to implement. And it leads to a pure domain model.
If you want to get more information on the topic, read Alistair Cockburn's original article on the subject.
The example in this article is inspired by a three part series of talks by Alistair Cockburn on the subject.
Last updated on 30 July 2021.__. If you want to keep up with what I'm doing or drop me a note, follow me on dev.to, LinkedIn or Twitter. Or visit my GitHub project. To learn about agile software development, visit my online course.
If you read this far, thank the author to show them you care. Say Thanks
Learn to code for free. freeCodeCamp's open source curriculum has helped more than 40,000 people get jobs as developers. Get started
ADVERTISEMENT
freeCodeCamp is a donor-supported tax-exempt 501(c)(3) charity organization (United States Federal Tax Identification Number: 82-0779546)
Our mission: to help people learn to code for free. We accomplish this by creating thousands of videos, articles, and interactive coding lessons - all freely available to the public.
Donations to freeCodeCamp go toward our education initiatives, and help pay for servers, services, and staff.
You can make a tax-deductible donation here.
Trending Books and Handbooks
REST APIs
Clean Code
TypeScript
JavaScript
AI Chatbots
Command Line
GraphQL APIs
CSS Transforms
Access Control
REST API Design
PHP
Java
Linux
React
CI/CD
Docker
Golang
Python
Node.js
Todo APIs
JavaScript Classes
Front-End Libraries
Express and Node.js
Python Code Examples
Clustering in Python
Software Architecture
Programming Fundamentals
Coding Career Preparation
Full-Stack Developer Guide
Python for JavaScript Devs
Mobile App
Our Charity
Publication powered by Hashnode About Alumni Network Open Source Shop Support Sponsors Academic Honesty Code of Conduct Privacy Policy Terms of Service Copyright Policy
