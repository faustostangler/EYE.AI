---
name: Hexagonal Architecture (Ports and Adapters) - DEV Community
keywords: (placeholder)
metadata:
  url: https://dev.to/godofgeeks/hexagonal-architecture-ports-and-adapters-3ljb
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Hexagonal Architecture (Ports and Adapters) - DEV Community
Skip to content
Powered by Algolia
Log in Create account
DEV Community
0 Add reaction 
0 Like  0 Unicorn  0 Exploding Head  0 Raised Hands  0 Fire
0 Jump to Comments 0 Save Boost
Copy link
Copied to Clipboard
Share to X Share to LinkedIn Share to Facebook Share to Mastodon
Report Abuse
Aviral Srivastava
Posted on May 7
Hexagonal Architecture (Ports and Adapters)
# architecture # backend # softwareengineering # tutorial
Taming the Code Kraken: Your Guide to Hexagonal Architecture (aka Ports and Adapters)
Ever felt like your codebase is a tangled mess of wires, where changing one tiny bit causes a domino effect of breakage? You're not alone. For years, developers have wrestled with monolithic applications, where the core business logic is inextricably linked to the UI, databases, and external services. It's like trying to untangle a plate of spaghetti with your eyes closed.
But fear not, brave coder! There's a superhero in town, and its name is Hexagonal Architecture, also affectionately known as Ports and Adapters. This architectural style is designed to rescue your sanity and make your applications more robust, testable, and adaptable to the ever-changing winds of technology.
So, grab a coffee (or your preferred potion of focus), and let's dive deep into this elegant solution.
The Problem We're Trying to Solve: The Monolithic Mire
Imagine a traditional layered architecture. You have your UI at the top, talking to your business logic in the middle, which in turn talks to your data access layer at the bottom. This sounds neat on paper, right?
The problem arises when the layers become too tightly coupled. Your business logic might be written with the assumption that it's always going to be a web UI calling it. What if you want to add a command-line interface (CLI) or integrate with a messaging queue? Suddenly, you're hacking at the core, introducing complexity and the dreaded "spaghetti code."
Furthermore, testing becomes a nightmare. To test your business logic, you often need to spin up the entire UI and database, which is slow, cumbersome, and prone to environmental issues.
Enter Hexagonal Architecture: The Elegant Alternative
Hexagonal Architecture, conceptualized by Alistair Cockburn, offers a brilliant way to decouple your core application logic from the "outside world." Instead of a strict layered approach, it focuses on a central "domain" or "core" that is blissfully unaware of how it's being interacted with or where its data is coming from.
The core idea is to create a clear boundary between your application's inner workings and its external concerns.
The "Hexagon" - Your Domain's Safe Haven
Think of your core business logic as residing within a hexagon. This hexagon represents the heart of your application – the rules, the workflows, the essential business operations. The beauty is that this hexagon is technology-agnostic. It doesn't know or care if it's being driven by a web browser, a mobile app, a scheduled job, or even a humble script.
Ports: The Application's "Contract"
Inside this hexagon, we define ports. Ports are essentially interfaces that define what your application can do and what information it needs from the outside world. They are the application's communication channels.
There are two main types of ports:
Primary Ports (Driving Ports): These are the entry points into your application. They represent the actions that external actors (like users, other systems, or scheduled tasks) can initiate. Think of them as "commands" or "queries" your application exposes.
Secondary Ports (Driven Ports): These are the interfaces that your application needs to interact with the outside world. They define the services or data sources your core logic relies on. Think of them as "requests" your application makes outward.
Adapters: The "Translators" to the Outside World
Now, how do these ports actually connect to the real world? That's where adapters come in. Adapters are responsible for translating between the abstract world of ports and the concrete realities of external systems.
Again, adapters come in two flavors, mirroring the ports:
Primary Adapters (Driving Adapters): These adapters drive your application by invoking its primary ports. Examples include:
Web Controllers/API Endpoints: Translate HTTP requests into calls to your application's primary ports.
CLI Commands: Translate command-line arguments into calls to your primary ports.
UI Components: Translate user interactions into calls to your primary ports.
Secondary Adapters (Driven Adapters): These adapters are driven by your application's secondary ports. They implement the interfaces defined by the secondary ports and handle the actual interaction with external systems. Examples include:
Database Repositories: Implement interfaces for saving and retrieving data from a database.
External API Clients: Implement interfaces for communicating with third-party services.
Message Queue Producers/Consumers: Implement interfaces for sending and receiving messages.
The Magic of Decoupling
The magic happens because the core domain only knows about the ports (interfaces), not the concrete implementations. It speaks in terms of "I need to save this user" (via a UserRepository secondary port), not "I need to execute an INSERT statement into the users table." Similarly, it exposes "Add New User" (a primary port) without knowing if it's being called by a web form or a mobile app.
This separation of concerns brings a boatload of benefits.
Advantages: Why Hexagons Rock
Testability, Glorious Testability! This is arguably the biggest win. Because your core domain is isolated, you can test it thoroughly without needing to set up databases, web servers, or external services. You can simply "mock" the secondary adapters to simulate their behavior. Imagine testing your complex business rules in milliseconds!
Adaptability and Flexibility: Want to switch from a SQL database to a NoSQL one? Need to integrate with a new payment gateway? No problem! You just create a new secondary adapter that implements the existing secondary port. Your core domain remains untouched. The same applies to front-end changes – swap out your web adapter for a mobile adapter.
Maintainability: With a clear separation of concerns, your codebase becomes much easier to understand and manage. Developers can focus on specific parts of the application without fear of breaking unrelated components.
Technology Independence: Your core business logic is no longer tied to specific frameworks or technologies. This future-proofs your application, allowing you to evolve with technological advancements without a massive rewrite.
Parallel Development: Different teams can work on different adapters (e.g., UI team, data team) simultaneously, as long as they adhere to the defined ports.
Disadvantages: It's Not All Sunshine and Rainbows
Initial Learning Curve: For developers accustomed to traditional layered architectures, understanding and implementing Hexagonal Architecture can take some getting used to. The concept of ports and adapters might seem abstract at first.
Boilerplate Code: You might find yourself writing more interface definitions (ports) and adapter classes initially. This can lead to a bit more "boilerplate" code, though modern frameworks can help mitigate this.
Overhead for Simple Applications: For very small and simple applications, the overhead of setting up ports and adapters might feel like overkill. The benefits become more pronounced as complexity grows.
Potential for Over-Abstraction: If not carefully designed, you could end up with too many small, granular ports and adapters, making the overall structure difficult to navigate. It's important to find the right balance.
Key Features and Concepts
Let's break down some of the core components you'll encounter:
The Core Domain (Application Layer)
This is where your business logic lives. It's a set of classes and interfaces that represent your application's business rules, entities, and use cases. It should be free of any external dependencies like frameworks or databases.
Ports (Interfaces)
Primary Ports: These define the "what" of your application's capabilities.
Example: An OrderServicePort interface with a method placeOrder(OrderDetails orderDetails) .
Secondary Ports: These define the "how" your application interacts with external services.
Example: An InventoryRepositoryPort interface with a method updateStock(String productId, int quantity) .
Adapters
Primary Adapters: These consume your primary ports.
Example: A WebOrderController that receives HTTP requests and calls orderServicePort.placeOrder(...) .
Example: A CliOrderHandler that parses command-line arguments and calls orderServicePort.placeOrder(...) .
Secondary Adapters: These implement your secondary ports.
Example: A DatabaseInventoryRepository that implements InventoryRepositoryPort and interacts with a database.
Example: An ApiPaymentGateway that implements PaymentGatewayPort and calls an external payment API.
Dependency Inversion Principle (DIP)
Hexagonal Architecture heavily relies on the Dependency Inversion Principle. Instead of high-level modules depending on low-level modules, both depend on abstractions (ports). This is what allows for easy swapping of implementations.
Inversion of Control (IoC)
IoC is often used to "wire up" the adapters to the ports. Dependency Injection frameworks are commonly used to manage the creation and injection of adapter instances into the core domain.
A Real-World Analogy: The Smart Home
Imagine a smart home system.
The Core Domain: The "brain" of your smart home, containing the rules for automating lights, setting thermostats, and triggering alarms. It doesn't care if you use Philips Hue bulbs or a Nest thermostat.
Primary Ports: The interfaces that allow you to interact with the smart home:
"Set Temperature" (command)
"Turn On Lights" (command)
"Get Room Status" (query)
Primary Adapters: The devices and interfaces that initiate actions:
Mobile App: Sends commands to the "Set Temperature" port.
Voice Assistant: Interprets "Turn on the living room lights" and calls the "Turn On Lights" port.
Web Dashboard: Displays room status by querying the "Get Room Status" port.
Secondary Ports: The interfaces that the smart home needs to perform its actions:
ThermostatControlPort (e.g., setTargetTemperature(int temperature) )
LightControlPort (e.g., turnOn(String lightId) )
SensorReaderPort (e.g., readTemperature(String roomId) )
Secondary Adapters: The actual hardware and services that the smart home interacts with:
Philips Hue Adapter: Implements LightControlPort to control Hue bulbs.
Nest Adapter: Implements ThermostatControlPort to control a Nest thermostat.
Temperature Sensor Driver: Implements SensorReaderPort to read data from a physical sensor.
This way, you can add new smart devices (adapters) without changing the core automation logic. If you decide to switch your lights to a different brand, you simply replace the Philips Hue adapter with a new one, and the smart home brain continues to function seamlessly.
Implementing Hexagonal Architecture: A Glimpse
Let's sketch out a very simple example in Java.
1. Domain Layer (The Hexagon)
2. Adapter Layer (The Outside World)
2.1. Primary Adapter (e.g., Web Controller)
2.2. Secondary Adapter (e.g., In-Memory UserRepository)
3. Composition Root (Wiring Everything Up)
This is where you instantiate your adapters and inject them into the core domain. This is typically done at the application's startup.
When to Consider Hexagonal Architecture
Medium to Large Applications: The benefits truly shine as your application grows in complexity.
Applications with Evolving Requirements: If you anticipate frequent changes in UI, data sources, or external integrations.
Microservices: Hexagonal Architecture is a natural fit for building self-contained microservices.
Applications Requiring High Testability: When robust and fast unit tests are a critical concern.
Conclusion: Building Resilient Systems
Hexagonal Architecture, or Ports and Adapters, is more than just a design pattern; it's a philosophy for building software that is resilient, adaptable, and a joy to work with. By creating a clear separation between your core business logic and its external concerns, you empower your application to withstand the inevitable changes of the technology landscape.
While it might require a slight shift in thinking initially, the rewards in terms of testability, maintainability, and flexibility are immense. So, the next time you feel the urge to untangle that code kraken, remember the hexagon – it's your ticket to a cleaner, more robust, and ultimately more enjoyable development experience. Embrace the ports, master the adapters, and build systems that stand the test of time!
 AWS
Promoted
What's a billboard?
Manage preferences
Report billboard
Power smarter decisions with the cloud
Join AWS experts and Partners to learn how cloud technology supports efficiency, agility, and growth. Watch live.
Register Now
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
 The DEV Team
Promoted
What's a billboard?
Manage preferences
Report billboard
Your Prompts are Legacy Code Now: The Google Cloud Next '26 Developer Breakdown
Google's showcase centered on a multi-agent system coordinating a full city-scale marathon simulation—Planner, Evaluator, and Simulator agents working in concert.
But the marathon wasn't the point. The architecture behind it is what you need to steal for your own systems to move from "vibes" to engineering rigor.
Read more →
Aviral Srivastava
Follow
Hi! I am a student currently pursuing my Undergraduate degree in Computer Science and Engineering in India.
Location Delhi, India
Joined Jan 23, 2021
More from Aviral Srivastava
Event Sourcing Pattern Details # architecture # database # softwareengineering # systemdesign
CQRS (Command Query Responsibility Segregation) # architecture # beginners # database # systemdesign
Onion Architecture vs Clean Architecture # architecture # backend # softwaredevelopment # softwareengineering
 AWS
Promoted
What's a billboard?
Manage preferences
Report billboard
Building industry breakthroughs together
Discover how the cloud helps businesses adapt, innovate, and grow in real time. Tune in live.
Register Now
DEV Community
What's a billboard?
Manage preferences
Edit billboard
Report billboard
Submissions close May 24. Don't leave $$$ on the table.
Build with Gemma 4 or write about it. Ten winners across two tracks.
Join Now
💎 DEV Diamond Sponsors
Thank you to our Diamond Sponsors for supporting the DEV Community
Google AI is the official AI Model and Platform Partner of DEV
Neon is the official database partner of DEV
Algolia is the official search partner of DEV
DEV Community — A space to discuss and keep up software development and manage your software career
Home
DEV++
Reading List
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
