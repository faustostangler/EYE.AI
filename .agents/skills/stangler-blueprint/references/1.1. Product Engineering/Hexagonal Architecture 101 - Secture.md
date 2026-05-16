---
name: Hexagonal Architecture 101 - Secture
keywords: (placeholder)
metadata:
  url: https://secture.com/en/hexagonal-architecture-101/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Hexagonal Architecture 101 - Secture 
Cookie consent
To provide the best experiences, we use technologies such as cookies to store and/or access device information. Consenting to these technologies will allow us to process data such as browsing behavior or unique IDs on this site. Not consenting, or withdrawing consent, may adversely affect certain features and functions.
Functional [x] 1 Functional Always active
The storage or technical access is strictly necessary for the legitimate purpose of enabling the use of a specific service explicitly requested by the subscriber or user, or for the sole purpose of carrying out the transmission of a communication over an electronic communications network.
Preferences [-] 1 Preferences
The storage or technical access is necessary for the legitimate purpose of storing preferences not requested by the subscriber or user.
Statistics [-] 1 Statistics
Technical storage or access that is used exclusively for statistical purposes. Technical storage or access that is used for anonymous statistical purposes only. Without a request, voluntary compliance by your Internet Service Provider, or additional records from a third party, information stored or retrieved solely for this purpose cannot be used to identify you.
Marketing [-] 1 Marketing
The storage or technical access is necessary to create user profiles to send advertising, or to track the user on a website or multiple websites for similar marketing purposes.
Manage options
Manage services
Manage {vendor_count} vendors
Read more about these purposes
Accept Deny See preferences Save preferences See preferences
Cookie Policy
Privacy Statement
Impressum 
Home
Services
Projects
Blog & code
Contact 
Home
Services
Projects
Blog & code
Contact
secture & code
Hexagonal Architecture 101
Here's everything you need to know about Hexagonal Architecture: 
Hexagonal architecture scheme
The Hexagonal Architecture, defined by Alistair Cockburn, is an implementation of what we call a Clean Architecture. Its main motivation is to divide our application into different layers with their own responsibility. This separation by layers allows us to decouple our code from external dependencies, such as the framework or any other external library, or third party.
Ports and adapters
This architecture is also widely known as the ports and adapters architecture, or by its English name ports&adapters. And it is just because it makes intensive use of the “adapter” pattern ( Adapter Pattern) together with the principle of reversal of dependencies to obtain the decoupling we were talking about before.
Why hexagonal?
In almost all texts or documents that talk about this architecture, we usually see it represented in the shape of a hexagon. And why a hexagon and not a pentagon, or a triangle or any other polygon? There is no official answer to this question, simply may be because the hexagon is the most versatile polygon.. Be that as it may, the number of sides is not relevant, it is only a merely cosmetic arrangement to differentiate it from the rest of the clean architectures.
The fact is that each side represents an input/output port of the application, and a polygonal shape expresses this principle better than a circle.
These ports are the entry point for any of the external agents or mechanisms that can interact with our application, whether they are mobile or web clients through the port for REST API, Web browsers through the HTTP port or a queuing system through the HTTP port for Message Brokers.
Each of these ports has, in turn, one or more adapters assigned to it, depending on the diversity we want to support. For example, the port for MessageBrokers could very well have adapters for RabbitMQ, Redis, Beanstalk or AmazonSQS, if what we want is to support all this variety of providers.
Points in common with Clean Architecture
In the future, we will talk about Clean Architectures and its characteristics and we will see that the hexagonal architecture is one of the purest implementations that we can find of the Clean Architecture.
Both the distribution of the layers and their content or dependency rules are literally the same, but we will still see their characteristics.
The dependency rule
Each of the concentric hexagons represents a layer, and this layer in turn is a barrier that can only be crossed by its upper layers. Thus:
Infrastructure you can access Application and to Domain
Application you can access Domain
Domain can only access Domain
The further inward we penetrate into the layers, the deeper we get into the business logic, rules and policies. The further out we move, the closer we are to external agents or mechanisms (web or mobile clients, external services or APIs, infrastructure services such as databases, queuing systems, etc).
Directory structure and layer separation
We are going to see step by step the directory structure and how the code is distributed in the different layers. We will start with a basic example that we will iterate through.
First of all, the root of our project could be this: 
Root of the project
apps contains the applications, the installations of the different frameworks we use. This is where our controllers and routes will live.
src will contain our code, the business logic of our application. 
API Application
Here we can see the content of an application displayed. For reasons of space we have omitted all non-relevant folders, leaving in view only the entrypoint (index.php) and controllers. 
Context and API modules
We have opted for a distribution in contexts ( API y Shared). In this case we have only one functional context (API) and another shared (Shared), but we could have more, for example, backoffice, which could contain all the code to manage a content management application.
As can be seen, each module contains a triplet of folders, each corresponding to one of the layers of the architecture. 
Expanded User Module
Going into more detail, we can see the contents of each of the folders that make up the architecture:
Application. Use cases. In our case we apply CQRs, so they are usually composed of one query (reading action) or a command (writing action), a handler or handler and, optionally, a service that executes the action. In some cases this service may be shared by other use cases, as for example in the case of GetUser, We therefore promote the service of application service a domain service, by placing it in the folder Domain and making it accessible to the rest of the use cases.
Domain. This is where we host the domain objects, such as the entity User that represents a user, or the service contracts to be implemented in infrastructure, such as UserRepository. We also consider exceptions as domain objects, and some shared services such as the one mentioned above. GetUser.
Infrastructure. Finally we have the implementations of the domain contracts. In this case we only have one implementation of the repository and it would be for the database engine. MySQL, We could very well support more by simply implementing the contract. 
Expanded shared context
Earlier we talked about a shared environment, and this is where most of the contracts and implementations of elements that will be used throughout the application go, such as, for example, a EventDispatcher, or the buses of commands y queries. In this example, we have implemented a bus with two different suppliers: Symfony y Tactician. And, in addition, we have made two different implementations for each: the synchronous and the asynchronous version.
With this we intend to demonstrate the versatility that this architecture offers us and the ease of change that it brings to our code: we could change the way our code is handled. commands and our queries by simply altering some configuration parameters of the dependency container.
Hexagonal architecture and DDD
We will have seen a thousand and one times the term hexagonal architecture along with the term DDD, and they are undoubtedly a killer combo very useful.
DDD is a development methodology that advocates decoupling above all else, so the Hexagonal Architecture fits like a glove as the central core of its practice.
_ Bibliography
Hexagonal Architecture. Alistair Cockburn (2005)
Hexagonal Architecture Draft. Alistair Cockburn
Backend
Miguel Ángel Sánchez Chordi
Software engineer. I love it when plans come together. 
Miguel Ángel Sánchez Chordi
Software engineer. I love it when plans come together.
See more posts
GitHub
Twitter
Linkedin 
Events
SUGARFREE: tecnología aplicada, sin edulcorar
Raquel Perez 
Development
Ralph (Wiggum) Loop
David Luque Quintana 
Development
JavaScript, el objeto Intl y otros inventos «diabólicos» para comprendernos unos a otros.
Dani Cabal 
Development
ADR: La memoria arquitectónica que tu IA necesita
Miguel Ángel Sánchez Chordi 
Artificial Intelligence
APIs de IA en Chrome: qué son, cómo usarlas y si sirven para Node, NestJS o Next.js
David Perez Lopez 
Development
Cómo crear plugins de Framer: paso a paso
Ismael 
Development
Acoplamiento Temporal (Temporal Coupling)
Miguel Ángel Sánchez Chordi 
Events
Eventos Tecnológicos 2026: un calendario para desarrolladores y profesionales del sector
Carmela Alonso 
Design
Cómo crear tu primer plugin de Figma paso a paso
Ismael 
Development
Brecha de género en tecnología: 2025 suma, pero no iguala
Marta Gutierrez 
Development
Introduccion a GSAP
Ruben Zafra Traver 
Development
De Android a React Native: un reto lleno de ventajas
Natalia Alvarez 
Development
Cómo implementar reconocimiento de voz en tus apps web
Paula Sanz 
Development
Me tiré 3 días metiéndome en el rabbit hole de RL para agentes
Antonio Romero 
Development
Cómo hablarle a Claude para que haga el trabajo por ti
Marta Gutierrez 
Development
Mis prácticas de programación: de 'espabila, chaval' a programador funcional
Quique Muñoz 
Development
Introducción a Opensearch
David Luque Quintana 
Development
Semantic constructors in PHP: what they are, how to use them and why they improve your code
Miguel Ángel Sánchez Chordi 
Development
What your clients want to see (and what they don't) in pre-production.
Fernando Arenas 
Strategic consulting
The BCG Matrix in 2025: What It Is, How It Works and What You Can Do With It (With Real Examples)
Pedro Miguel Muñoz 
Development
Motion Activity Detection in iOS with Core Motion: 6 Types, Accuracy and Common Challenges.
Polina Demidova 
Development
Practical implementation of AI-first SEO: Tools, cases and strategies (Part 2)
Antonio Romero 
Development
Legacy Code Migration Strategies: Strangler Fig Application and Anticorruption Layer
Miguel Ángel Sánchez Chordi 
Development
Navigating the Post-Cursor Landscape: A Strategic Analysis of AI Tools for Developers in 2025
Pedro Miguel Muñoz 
Artificial Intelligence
From SEO to AI-first search: how to position your brand on AI-generated answers (Part 1)
Raquel Perez 
Artificial Intelligence
Guide to running ChatGPT on your PC without an Internet connection
Marius Serban 
Development
Location Optimization in iOS: How to Adjust Filter Distance, Monitor Significant Changes, and Take Advantage of Automatic Visitor Detection
Polina Demidova 
Artificial Intelligence
RAG done right: the difference between a chatbot and an AI agent
Antonio Perez 
Project management
How to do tech services marketing for B2B (and remote) without going mad
Raquel Perez 
Project management
Project management: 12 principles that work (at least for us)
Pedro Miguel Muñoz 
Design
Figma does not bite
Águeda Machado 
Design
5 strategies to design with waiting times without frustrating your users
Ismael 
Development
Drama-free frontend security: mistakes that are (still) made and how to avoid them
Javier Motos 
Development
5 Useful (and not so obvious) Tools for iOS Developers
Polina Demidova 
Artificial Intelligence
Generative Agents: When Artificial Intelligence Lives Among Us
Antonio Romero 
Development
Back to the Feature. Traveling to the future with Tailwind.
Fernando Arenas 
Development
Symfony Live Components. Why thousands of frontends are losing their jobs
Gonzalo Payo 
Development
iPad for development and prototyping: 3 tools that make a difference
Polina Demidova 
Development
Action-Domain-Responder
Miguel Ángel Sánchez Chordi 
Development
Knowledge bases with AI: a competitive advantage that your company is not yet taking advantage of.
Antonio Perez 
Development
How to improve your product sales through cognitive biases
Pedro Miguel Muñoz 
Development
Is software development sustainable?
Polina Demidova 
Development
Tailwind is to programming what the plague was to medieval Europe
Dani Cabal 
Design
Design events not to be missed in 2025
Ismael 
Development
How Cursor can help us in software development
David Luque Quintana 
Design
Live Activities for iPhone design guidelines and best practices: Case study with Wikiloc
Águeda Machado 
Development
Kotlin vs Java: Is it time to leave Java behind?
Natalia Alvarez 
Project management
How to work in a team (2/2)
Pedro Miguel Muñoz 
Project management
How to work in a team (1/2)
Pedro Miguel Muñoz 
Development
How to correctly store JWT tokens in the front end
Miguel Ángel Sánchez Chordi 
Project management
How to manage stress and burnout in web development
Samuel Sanchez 
Development
How to touch a legacy project without blowing everything up
Pedro Adame 
Project management
RASCI Matrix: How to keep your project and team organized
Alberto Aznar 
Development
Designing digital products that comply with accessibility legislation in Spain by 2025
Ismael 
Development
Playwright: The E2E Testing Framework That Leads the Race
Vicent Gisbert Soto 
Development
What is search intent
Pedro Miguel Muñoz 
Development
SwiftUI vs UIKit
Dani Moraleda 
Development
Boost your projects with ChatGPT: Make AI work for you!
Marius Serban 
Cybersecurity
Cybersecurity. Impact of Artificial Intelligence
Antonio Perez 
Development
Software Design Patterns
Miguel Ángel Sánchez Chordi     
Back to blog
We are HIRING!
Job Offers
What Can We Do
Discover why Secture
Stay in the loop
Subscribe to our Newsletter
X-twitter Instagram Linkedin
Empowering people, inspiring innovation. 2018 - 2025 ©Secture Labs, S.L.
Digital Kit
Kit Consulting
Newsletter
Legal Notice
Privacy Policy
Cookies Policy 
Spanish 
Spanish 
English 
Manage consent
