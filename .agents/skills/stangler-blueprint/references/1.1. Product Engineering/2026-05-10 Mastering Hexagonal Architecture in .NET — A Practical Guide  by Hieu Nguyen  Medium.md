---
name: 2026-05-10 Mastering Hexagonal Architecture in .NET — A Practical Guide | by Hieu Nguyen | Medium
keywords: (placeholder)
metadata:
  url: None
  source: SOURCE_TYPE_TEXT
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
WebSync metadata
title: Mastering Hexagonal Architecture in .NET — A Practical Guide | by Hieu Nguyen | Medium
url: https://medium.com/@hieunv/mastering-hexagonal-architecture-in-net-a-practical-guide-6651752e6baa
date: 2026-05-10T21:29:42.088Z
parsing method: defuddle
Sitemap
This is Part 2 of the.NET Architecture series.
Part 1 — Dependency Inversion Principle: The Foundation of Sustainable Architecture
Part 2 — Mastering Hexagonal Architecture in.NET: A Practical Guide (this post)
Part 3 — Dependency Injection: The Core Foundation for Implementing Dependency Inversion Principle
Not a Medium member? Keep reading for free by clicking here.
Introduction
Have you ever had to change your database and realized it required touching 10 different files — some of which had nothing to do with persistence? Or swapped an HTTP client and found business logic scattered throughout? These are symptoms of a tightly coupled architecture.
Hexagonal Architecture (also known as Ports and Adapters), introduced by Alistair Cockburn in 2005, solves exactly this problem. It enforces a clear separation between your core business logic and the technical details that surround it — databases, HTTP clients, UI frameworks — so that each can evolve independently.
This article walks through a practical.NET implementation using C#, showing how the architecture works in real code and why it makes your application more maintainable, testable, and adaptable.
What is Hexagonal Architecture?
Hexagonal Architecture separates the core business logic of an application from external technical details such as databases, user interfaces, or external services. It’s visualized as a hexagon with:
Core Domain at the center: containing business rules and logic
Ports: interfaces allowing communication with the application
Adapters: specific implementations of ports, connecting the domain with the outside world
The critical rule is dependency direction flows inward only. Outer layers know about inner layers, but the inner core never knows about the outside world:
App.Core has zero knowledge of databases, HTTP clients, or web frameworks. App.Data, App.Gateway, and App.Api all depend on App.Core — never the reverse.
Project Structure
Our sample.NET project organizes modules by architectural role, with each module further subdivided by feature (Poke, Todo):
Notice how App.Core is isolated at the center. HTTP APIs (App.Api), database access (App.Data), and HTTP clients (App.Gateway) are all adapters at the edges.
Detailed Analysis of Each Module
1. Core Module — The Heart of the Architecture
The Core module contains business logic and domain entities. It defines the Ports (interfaces) that all other layers must implement. Crucially, App.Core depends on no other project in the solution.
Let’s look at our base entity and the TodoEntity:
Next, we define the repository interface (Port). This interface only speaks in domain concepts — it has no idea whether the data comes from SQL, NoSQL, or a file:
2. Data Module — Secondary Adapter (Database)
The Data module implements the repository interfaces defined in App.Core. This is where EF Core, connection strings, and SQL specifics live — completely invisible to the domain.
By moving column name mappings out of App.Core entities and into AppDbContext.OnModelCreating via Fluent API, App.Core stays free of any infrastructure-specific knowledge:
The TodoRepository implementation is straightforward EF Core — all persistence details stay in App.Data:
If you wanted to swap EF Core for Dapper or move to a NoSQL store, you would only change files in App.Data. App.Core and App.Api remain completely untouched.
3. API Module — Primary Adapter (HTTP)
The API module handles HTTP requests and responses, acting as the primary adapter. It translates external HTTP calls into operations on the core domain. Notice it depends only on App.Core types — it has no reference to App.Data or App.Gateway.
The null-guard throws (?? throw new ArgumentNullException(...)) on the backing fields follow defensive programming best practices. This is a common pattern when using C# primary constructors where you want to validate dependencies at construction time.
4. Gateway Module — Secondary Adapter (External Services)
The Gateway module implements patterns for interacting with external services or APIs, acting as another secondary adapter.
First, the pure domain model and gateway interface in App.Core:
The gateway implementation in App.Gateway uses two kinds of internal DTOs that mirror the third-party PokeAPI's JSON shape:
PokeResponse<T> — a shared paginated wrapper in App.Gateway.Client, reused across different response types
PokemonItem and PokemonDetail — internal classes inside PokemonGateway for specific endpoint responses
These DTOs are purely implementation details of the App.Gateway module. The domain model only ever sees the clean Pokemon type defined in App.Core:
Data Flow in Hexagonal Architecture
Let’s follow the flow of an HTTP request from start to finish:
HTTP Request → Minimal API Endpoint in App.Api (Primary Adapter)
Endpoint validates the request, maps external DTOs, and calls the App.Core Service
Service in App.Core processes core business logic
Service calls a Repository or Gateway interface (Port) to interact with persistence or external APIs
Adapter Implementation (App.Data or App.Gateway) translates the core request to a database query or external HTTP call
Data flows back: Adapter → Service → Endpoint → HTTP Response
At no point does App.Core know which database, HTTP client, or web framework is in use.
Testability: The Core in Isolation
One of the biggest advantages is how cleanly the Core can be unit-tested. Because TodoService depends only on the ITodoRepository interface (a Port), you can mock it completely — no database required:
This test exercises real business logic in TodoService without any database connection, EF Core configuration, or HTTP infrastructure. The same pattern applies to PokemonService — mock IPokemonGateway and test pure domain behavior.
Benefits of Hexagonal Architecture
High Maintainability: Business logic is completely separated from technical implementations, making it simple to evolve either side independently.
Technology Agnosticism: You can swap your database ORM (e.g., from EF Core to Dapper) or replace an HTTP client without touching App.Core.
Excellent Testability: App.Core can be fully unit-tested without any external dependencies — just mock the Port interfaces.
Parallel Development: Frontend/API teams and database teams can work in parallel once the Core interfaces (Ports) are defined.
Conclusion
Hexagonal Architecture provides a strongly decoupled approach for complex application development. By defining clear boundaries (Ports) around the Domain (Core) and pushing infrastructure details to the edges (Adapters in Data, Gateway, and API), you produce robust, testable, and adaptable C# applications.
Our sample solution enforces this structurally using separate.NET class libraries (App.Core, App.Api, App.Data, App.Gateway). The compiler itself guarantees that App.Core can never accidentally import from App.Data — the architecture isn't just a convention, it's enforced by project references.
The result: when requirements change, you change in one place. When technology evolves, you swap one adapter. When bugs appear, you test in isolation. That’s the power of Ports and Adapters.
