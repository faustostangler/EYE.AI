---
name: 2026-05-10 Dependency Injection: The Core Foundation for Implementing Dependency Inversion Principle | by Hieu Nguyen | Medium
keywords: (placeholder)
metadata:
  url: None
  source: SOURCE_TYPE_TEXT
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
WebSync metadata
title: Dependency Injection: The Core Foundation for Implementing Dependency Inversion Principle | by Hieu Nguyen | Medium
url: https://medium.com/@hieunv/dependency-injection-the-core-foundation-for-implementing-dependency-inversion-principle-8a2ef14cb82a
date: 2026-05-10T21:30:10.654Z
parsing method: defuddle
Sitemap
This is Part 3 of the.NET Architecture series.
Part 1 — Dependency Inversion Principle: The Foundation of Sustainable Architecture
Part 2 — Mastering Hexagonal Architecture in.NET: A Practical Guide
Part 3 — Dependency Injection: The Core Foundation for Implementing Dependency Inversion Principle (this post)
Not a Medium member? Keep reading for free by clicking here.
Introduction
Dependency Injection (DI) is not merely a design pattern or framework feature — it is the fundamental mechanism that makes the Dependency Inversion Principle (DIP) practically implementable in real-world software systems. While DIP provides the theoretical foundation for building flexible, maintainable architectures, DI serves as the concrete implementation strategy that transforms this principle from concept into working code.
Understanding this relationship is crucial: DIP defines the “what” and “why” of proper dependency management, while DI provides the “how”. Without DI, attempting to follow DIP leads to complex, manual dependency management that becomes unwieldy as systems grow. With DI, DIP becomes an elegant, automated solution that scales naturally.
The Fundamental Problem: Why DIP Exists
The Dependency Problem
This code violates DIP because:
High-level policy (order processing) depends on low-level details (MySQL, SMTP, Stripe)
Abstractions (business logic) depend on concretions (specific implementations)
Changes to infrastructure force changes to business logic
Testing requires real databases, email servers, and payment systems
The Dependency Inversion Principle Solution
But here’s the critical question: How do we ensure that OrderService gets the correct implementations of these abstractions at runtime? This is where Dependency Injection becomes essential.
Dependency Injection: The Implementation Foundation of DIP
The Manual Approach: Why It Doesn’t Scale
DI: Automating DIP Implementation with ASP.NET Core
ASP.NET Core ships with a built-in DI container (IServiceCollection). All you need to do is register your abstractions and their concrete implementations — the framework handles object creation and injection automatically.
Now OrderService is resolved with its dependencies injected automatically:
Key Insight: DI doesn’t just make DIP possible — it makes DIP practical and maintainable. Without DI, manually managing dependencies according to DIP principles becomes a maintenance nightmare.
How DI Enables DIP: The Core Mechanisms
1. Inversion of Control (IoC)
DI implements IoC by taking away the responsibility of creating dependencies from the consuming class:
2. Lifetime Management
ASP.NET Core DI gives you fine-grained control over object lifetimes, which reinforces DIP boundaries:
LifetimeRegistrationWhen to UseTransient AddTransient<I, T>() Lightweight, stateless servicesScoped AddScoped<I, T>() Per-request state (e.g., DB contexts, repositories)Singleton AddSingleton<I, T>() Shared, thread-safe state (e.g., caches, clients)
3. The Captive Dependency Pitfall
While DI gives you powerful tools to manage object lifetimes, it also introduces a dangerous pitfall known as a Captive Dependency. This occurs when a service with a longer lifetime “captures” and holds a reference to a service with a shorter lifetime.
To fix this, a long-lived service should never depend directly on a shorter-lived service. Instead, if a Singleton needs a Scoped service, it should inject an IServiceScopeFactory to create the scope dynamically:
Note: ASP.NET Core throws an _InvalidOperationException_   by default in the Development environment if it detects a scoped service injected into a singleton.
4. Dependency Graph Resolution
DI automatically resolves complex dependency graphs, ensuring proper DIP implementation throughout the system:
DI as the Enabler of Testability in DIP
The Testing Challenge Without DI
DI Enables True Unit Testing
With DI, your tests can inject mock implementations — without modifying a single line of production code:
Key Point: DI makes it trivial to substitute mock implementations for real ones, enabling fast, isolated unit tests that still respect DIP boundaries.
DI Configuration Patterns That Reinforce DIP
1. Extension Method Pattern (the.NET Way)
In.NET, the idiomatic approach is to use extension methods on IServiceCollection to group related registrations by layer. This keeps Program.cs clean and enforces architectural boundaries:
And in Program.cs, composition is clean and intentional:
2. Environment-Based Implementation Selection
DI enables runtime selection of implementations without any code changes — a direct expression of DIP:
Or use configuration to drive the decision:
Dependency Injection in Hexagonal Architecture
In Hexagonal Architecture, DI is not optional — it is the wiring mechanism that connects the domain core to the adapters. Without DI, you can define ports and adapters, but you cannot connect them at runtime while keeping the domain isolated.
The Three Layers and Their DI Roles
Ports as Interfaces, Adapters as Implementations
A port is an interface defined in the domain layer. An adapter is a concrete class in the infrastructure layer that implements that port. DI is what connects them:
The DI + Hexagonal Flow
When an HTTP request comes in, DI orchestrates the full dependency chain invisibly:
The domain core (App.Core) has zero knowledge of SQLite, EF Core, or HTTP. DI enforces this separation at the composition root.
The Strategic Value: Why DI as DIP Foundation Matters
1. Architectural Integrity
DI makes DIP violations visible. When you wire dependencies in Program.cs, the wrong dependency immediately stands out:
Note: Unlike some static analysis tools, the.NET DI container won’t prevent you from injecting a concrete type at compile time — but code review and architectural conventions should enforce this. Tools like NetArchTest or ArchUnitNET can add automated enforcement.
2. Evolution and Maintenance
Adding new capabilities never requires touching existing domain code:
3. Team Productivity and Code Quality
DI with DIP yields compounding benefits as teams and codebases grow:
No manual wiring — the container handles the entire dependency graph
Consistent architecture — ports and adapters have a clear home in each layer
Easy testing — swap any adapter with a mock or in-memory alternative
Clear boundaries — Program.cs is the single composition root; everyone knows where wiring lives
Reduced coupling — replacing a database or external API requires only a new adapter and one registration change
Conclusion
Dependency Injection is not just a helpful pattern — it is the foundational technology that makes the Dependency Inversion Principle practical and maintainable in real-world.NET applications. The relationship is symbiotic:
DIP provides the architectural principle: High-level modules should not depend on low-level modules; both should depend on abstractions
DI provides the implementation mechanism: Automatic resolution and injection of dependencies based on interfaces
Hexagonal Architecture ties them together: Ports define the abstractions, adapters provide the implementations, and DI wires them at the composition root
Without DI, following DIP leads to complex manual dependency management that doesn’t scale. With DI, DIP becomes an elegant, automated solution that grows naturally with your system.
Key Takeaway: When you write builder.Services.AddScoped<ITodoRepository, TodoRepository>(), you're not just registering a service — you're expressing an architectural decision. You're declaring that the domain will never know about SQLite, EF Core, or any specific persistence technology. That single line of code is DIP made real.
References
Martin, Robert C. — “Clean Architecture: A Craftsman’s Guide to Software Structure and Design”
Seemann, Mark — “Dependency Injection Principles, Practices, and Patterns”
Evans, Eric — “Domain-Driven Design: Tackling Complexity in the Heart of Software”
Microsoft — Dependency injection in ASP.NET Core
