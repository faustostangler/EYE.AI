---
name: Dependency Inversion & Ports/Adapters | Synapse Studios Standards
keywords: (placeholder)
metadata:
  url: https://docs.synapsestudios.com/concepts/architecture/dependency-inversion
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Dependency Inversion & Ports/Adapters | Synapse Studios Standards
Skip to content 
Search K
Main Navigation Home
Concepts
Overview
Architecture
UI
Patterns
Testing
CI/CD
Practices
Working with Legacy Code
Implementation
Frameworks
Testing
CI/CD
Infrastructure
Code Quality
Appearance
Menu
On this page
Sidebar Navigation
[
Architecture
](https://docs.synapsestudios.com/concepts/architecture/)
Domain Modeling
Coupling and Cohesion
Clean Architecture
Modular Monolith
Module Decomposition
Dependency Inversion & Ports/Adapters
Terraform Module Philosophy
[
UI
](https://docs.synapsestudios.com/concepts/ui/)
Compositional UI
[
Patterns
](https://docs.synapsestudios.com/concepts/patterns/)
Use Cases
Application Service
Domain Service
Repository
Page Object
Simulator
[
Testing
](https://docs.synapsestudios.com/concepts/testing/)
Unit Testing
Test-Driven Development
Backend Integration Testing
Frontend Testing
Acceptance Testing
[
CI/CD
](https://docs.synapsestudios.com/concepts/ci-cd/)
Continuous Integration
Continuous Delivery
[
Practices
](https://docs.synapsestudios.com/concepts/practices/)
Code Smells
[
Postmortems
](https://docs.synapsestudios.com/concepts/practices/postmortems/)
Formal Postmortem Template
[
Working with Legacy Code
](https://docs.synapsestudios.com/concepts/legacy/)
Modernizing Legacy Hapi Applications
On this page
The Dependency Rule
Understanding Dependency Inversion
The Problem
The Solution
Key Principles
1. High-level modules should not depend on low-level modules
2. Both should depend on abstractions
3. Abstractions should not depend on details
4. Details should depend on abstractions
Ports and Adapters
Ports: The Interfaces
Adapters: The Implementations
How It Works in Practice
Step 1: Define the Port (Interface)
Step 2: Use the Port
Step 3: Implement the Adapter
Step 4: Wire It Together
Benefits of This Approach
Testability
Flexibility
Parallel Development
Clear Boundaries
Common Patterns
Repository Pattern
Gateway Pattern
Presenter Pattern
Event Publisher Pattern
Anti-Patterns to Avoid
Leaky Abstractions
Interface Segregation Violation
Wrong Layer Definition
Practical Guidelines
Start Simple
Name Interfaces After Capabilities
Keep Interfaces Stable
Use Dependency Injection
Applied In
Related Concepts
Further Reading
Dependency Inversion & Ports/Adapters 
How to build flexible, testable systems by inverting dependencies and creating pluggable architectures
The Dependency Rule 
The Dependency Rule is the fundamental principle that makes Clean Architecture work:
Source code dependencies must point only inward, toward higher-level policies.
This simple rule has profound implications:
Business logic never depends on technical details
Core domain code remains stable and portable
Technical implementations can be swapped without affecting business rules
Testing becomes trivial when there are no external dependencies
But how do we achieve this when our use cases need databases, our domain events need message queues, and our entities need to be saved somewhere?
The answer: Dependency Inversion.
Understanding Dependency Inversion 
The Problem 
In traditional layered architectures, high-level components depend on low-level components:
This creates rigid systems where business logic is coupled to technical details. Want to switch from PostgreSQL to MongoDB? Rewrite your services. Want to test business logic? Set up a test database.
The Solution 
Dependency Inversion flips this relationship. Instead of high-level components depending on low-level ones, both depend on abstractions:
The high-level component defines the interface it needs, and the low-level component implements that interface. The dependency arrow has been inverted.
Key Principles 
1. High-level modules should not depend on low-level modules 
Your business logic (high-level) shouldn't know about databases, web frameworks, or external services (low-level).
2. Both should depend on abstractions 
Define interfaces that represent capabilities, not implementations.
3. Abstractions should not depend on details 
Interfaces should be defined in terms of business needs, not technical capabilities.
4. Details should depend on abstractions 
Implementations conform to interfaces, not the other way around.
Ports and Adapters 
The Ports and Adapters pattern (also called Hexagonal Architecture) is a practical application of dependency inversion that creates a pluggable architecture.
Ports: The Interfaces 
A Port is an interface that defines a boundary between your application and the outside world. Ports are defined by the application based on what it needs, not what the infrastructure provides.
Types of Ports:
Inbound Ports (Driving/Primary)
Define how the outside world can interact with your application
Implemented by use cases
Called by external actors (users, other systems)
Examples: CreateOrderUseCase , ProcessPaymentUseCase
Outbound Ports (Driven/Secondary)
Define what your application needs from the outside world
Defined as interfaces in the domain or use case layer
Implemented by infrastructure
Examples: OrderRepository , PaymentGateway , NotificationService
Adapters: The Implementations 
An Adapter is a concrete implementation that connects your application to the external world through a port.
Types of Adapters:
Inbound Adapters (Driving/Primary)
Translate external requests into application calls
Implement delivery mechanisms
Examples: REST controllers, GraphQL resolvers, CLI commands, Message queue consumers
Outbound Adapters (Driven/Secondary)
Implement outbound port interfaces
Handle technical details of external interactions
Examples: SQL repositories, HTTP API clients, SMTP email senders, File system accessors
How It Works in Practice 
Step 1: Define the Port (Interface) 
The use case layer defines what it needs:
typescript
Step 2: Use the Port 
The use case depends only on the interface:
typescript
Step 3: Implement the Adapter 
The infrastructure layer provides the implementation:
typescript
Step 4: Wire It Together 
The application's composition root connects ports to adapters:
typescript
Benefits of This Approach 
Testability 
Replace real implementations with test doubles:
typescript
Flexibility 
Swap implementations without changing business logic:
typescript
Parallel Development 
Teams can work independently:
Domain experts build use cases against interfaces
Infrastructure teams implement adapters
UI teams build against use case interfaces
Clear Boundaries 
The architecture makes boundaries explicit:
Ports define the contract
Adapters handle the technical details
Business logic remains pure
Common Patterns 
Repository Pattern 
Abstracts data persistence, allowing business logic to work with domain objects without knowing storage details.
Gateway Pattern 
Abstracts external service calls, hiding HTTP requests, authentication, and error handling from business logic.
Presenter Pattern 
Abstracts output formatting, allowing use cases to return raw data that different adapters can format appropriately.
Event Publisher Pattern 
Abstracts event publishing mechanisms, letting domain code emit events without knowing about message queues or event buses.
Anti-Patterns to Avoid 
Leaky Abstractions 
Don't let implementation details leak through interfaces:
typescript
Interface Segregation Violation 
Don't force clients to depend on methods they don't use:
typescript
Wrong Layer Definition 
Interfaces should be defined where they're used, not where they're implemented:
typescript
Practical Guidelines 
Start Simple 
Don't create interfaces for everything upfront. Start with concrete implementations and extract interfaces when you need flexibility or testing.
Name Interfaces After Capabilities 
Name interfaces after what they do, not how they're implemented:
Good: SaveOrder , NotifyUser , ValidatePayment
Bad: IPostgresDB , ISMTPService , IStripeAPI
Keep Interfaces Stable 
Interfaces should change less frequently than implementations. Design them around stable business concepts, not volatile technical details.
Use Dependency Injection 
Whether through a framework or manual wiring, use dependency injection to connect ports and adapters without creating coupling.
Applied In 
See how these principles are implemented in practice:
Clean Architecture in NestJS Modules - Dependency injection and layer boundaries
Repository Pattern in NestJS - Ports and adapters for data access
Modular Monolith in NestJS - Module boundaries and dependency management
Acceptance Testing Guidelines - Test doubles and adapter patterns in testing
React Design Guidelines (coming soon) - Props as ports, components as adapters
Related Concepts 
Clean Architecture - The architectural context for dependency inversion
Use Cases - Primary consumers of ports and adapters
SOLID Principles (coming soon) - Dependency Inversion Principle in detail
Further Reading 
Hexagonal Architecture - Original article by Alistair Cockburn
Ports and Adapters Pattern - Detailed explanation by Herberto Graça
Clean Architecture by Robert C. Martin - Chapters 11-12 on DIP and Boundaries
Dependency Inversion Principle - SOLID principle explanation
Pager
Previous page Module Decomposition
Next page Terraform Module Philosophy
