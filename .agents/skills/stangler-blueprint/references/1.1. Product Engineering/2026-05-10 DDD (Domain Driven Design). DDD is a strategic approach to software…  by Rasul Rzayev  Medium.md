---
name: 2026-05-10 DDD (Domain Driven Design). DDD is a strategic approach to software… | by Rasul Rzayev | Medium
keywords: (placeholder)
metadata:
  url: None
  source: SOURCE_TYPE_TEXT
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
WebSync metadata
title: DDD (Domain Driven Design). DDD is a strategic approach to software… | by Rasul Rzayev | Medium
url: https://rzaeeff.medium.com/ddd-domain-driven-design-69643f360b18
date: 2026-05-10T21:12:02.997Z
parsing method: defuddle
Sitemap
DDD is a strategic approach to software development that focuses on the core business domain. In short, DDD is first and foremost about modeling a bounded context with a Ubiquitous Language.
In DDD, if we don’t start with Strategic Design and understand it well, we can’t apply Tactical Design effectively.
Conway’s Law says software designs mirror the communication structures of the teams that build them. In DDD, this means your bounded contexts should align with team boundaries so each team owns one coherent model and language. The context map then reflects inter-team relationships (e.g., Customer/Supplier, ACL), turning social contracts into integration patterns.
If you ignore this, models fracture and coupling grows.
When need to use DDD?
D on’t try to apply DDD to everything. Draw a context map and decide on where you will make a push for DDD and where you will not. And then don’t worry about it outside those boundaries. Experiment a lot and expect to make lots of mistakes. Modelling is a creative process. — Eric Evans
In addition, DDD approaches should be applied only if you are implementing complex microservices with significant business rules. Simpler responsibilities, like a CRUD service, can be managed with simpler approaches.
DDD patterns help you understand the complexity in the domain. For the domain model for each Bounded Context, you identify and define the entities, value objects, and aggregates that model your domain.
Domains and subdomains appear in every phase: they frame user needs, describe today’s reality, and are reshaped by any solution. In DDD, Strategic Design belongs to the problem space, focusing on language, constraints, and boundaries without tech choices. Tactical Design moves the work into the solution space by refining models into code and architecture step by step. The Bounded Context links the two:
Ubiquitous Language
It establishes a shared, precise vocabulary between business and engineering. Business concepts and workflows are represented directly in the software — shaping design and showing up in the code.
In DDD, developers start with the business problem before tackling technical concerns. That focus lets each team’s Bounded Context develop its Ubiquitous Language organically and steadily over time.
Strategic Design
Strategic Design in DDD is about making deliberate, high-level choices for how the domain is carved up and governed. You identify the core domain, separate it from supporting and generic subdomains, and draw clear bounded contexts with explicit boundaries and responsibilities.
Apply rich DDD techniques only where the business complexity justifies them; don’t over-engineer areas with straightforward logic.
Start with a simple representation, then refine as your understanding deepens and requirements shift. Expect to revisit names, rules, and boundaries as the ubiquitous language matures.
Strategic Design depends on close partnership between domain experts (product, business, analysts) and engineers. Maintain a shared vocabulary and use it consistently — in conversations, documents, and code — so the model stays aligned with the business.
Bounded Contexts & Subdomain
A bounded context is a description of a boundary (typically a subsystem, or the work of a particular team) within which a particular model is defined and applicable. it’s the fence around a model and its Ubiquitous Language — inside the fence the terms/rules stay consistent; outside, other models may use the same words differently
Most of the time, a single Bounded Context would correspond to a single Subdomain. Subdomains carve the business into major capability areas (core, supporting, generic) and help partition legacy models into organizational units. Bounded contexts turn those conceptual areas into concrete software and team boundaries — owning code, data, and the local ubiquitous language.
Think of a subdomain as a conceptual bridge from today’s heterogeneous legacy models toward the new bounded contexts(each Bounded Context correlates to a microservice) you’ll implement with DDD.
Subdomain vs Bounded Context
Does this part make us stand out? → Core subdomain. Put most of your effort here. Aim for great.
Does the core need this to work? → Supporting subdomain. Do what’s needed so the core can run. Keep it lean.
Is this common, the same for most teams? → Generic subdomain. Reuse or buy (e.g., email sending, monitoring). Don’t build if you don’t have to.
Core: main value, heavy focus.
Supporting: helps the core, moderate effort.
Generic: commodity stuff, prefer reuse/buy.
Note: subdomains describe parts of the business and system — not your team structure.
A bounded context is a fence around one model. That fence might cover ideas from several subdomains. And the reverse is also true: one subdomain can be split into several bounded contexts.
Examples:
A Payments context might use concepts from Customer and Risk subdomains.
The Customer subdomain could be split into Profile, KYC, and Loyalty contexts.
Product in Two Bounded Contexts
Same name, different rules.
A Product can live in two contexts and mean different things.
In the Delivery Context, “product” might be a value object with only what delivery needs: weight, quantity, maybe size…
In the Product Context, it’s richer: categories, media, catalog rules, and its own business logic.
Do two contexts mean two microservices?
Not by default. Bounded Context ≠ service. Split into separate services only for clear technical reasons: scaling, team ownership, different release pace, or failure isolation. If those needs aren’t there, one service is fineCommunication between contexts
Communication Between Contexts
Keep coupling low. Common options:
Domain Events: ProductCreated, ProductRenamed.
Published Language: agreed event/DTO schema.
Anticorruption Layer: maps Product’s model into Delivery’s model.
Request/Response (sync) for occasional reads that must be fresh.
Anticorruption Layer (ACL)
When you must talk to a legacy system or an external service that uses a different model, add an Anticorruption Layer between them and your domain. This layer converts requests and data both ways so the outside model doesn’t leak into — or distort — your own.
Think of it as a translator: it maps their terms, structures, and rules to yours, and back again. By keeping this translation at the edge, your domain stays clean and consistent even when the other side changes or has a very different data shape.
This pattern is implementation agnostic, meaning it can be used regardless of whether your services communicate through events or with a request-response protocol. In both cases, there is typically a wire format (be it the schema used to return data from a REST endpoint or the schema used to describe an event, such as an Avro message stored in the Schema Registry).
The anti-corruption layer has two goals:
It insulates the domain model from change
It encapsulates the boundary between contexts, describing how they map both in a technical sense — field A in a message maps to field B in the model, but also in terms of DDD’s ubiquitous language — the counterparty in the event schema maps to the customer in the domain model
Context Mapping
Context mapping shows how two or more bounded contexts relate and talk to each other. It makes clear where each model starts and ends, how data moves, and who owns what.
Why it matters: With clear maps, changes in one context don’t break another. Teams know the contracts between contexts, the direction of flow, and the source of truth.How to do it (simple steps)
How to do it (simple steps):
List your bounded contexts and their goals.
Mark the touchpoints (events, APIs, files).
Pick an interaction style and contract.
Decide ownership: who publishes, who consumes.
Write down the terms (Published Language) and how you translate between models.
Context Mapping helps teams see the boundaries, the links between them, and the rules of communication — so data flows smoothly and surprises are rare.
Context Mapping helps teams see the boundaries, the links between them, and the rules of communication — so data flows smoothly and surprises are rare.
Upstream & Downstream
Upstream (u): owns the API/model/contracts. Changes here ripple outward. Downstream (d): consumes what upstream provides and must adjust.
This shows up in code (library → app), but also in process (release timing, how fast teams respond).
Example: A Personal Finance app calls an Online Banking API.
Online Banking = upstream (u) — it controls the API.
Personal Finance = downstream (d) — it relies on that API and follows its changes.
A clear map exposes power, risk, and dependencies early. You’ll see where delays might come from and whether the organizational setup quietly works against your project, before you lock in plans.
Separation of concerns
1) Start from the center: domain rules
This is the business logic in the ubiquitous language. It should not know about REST, gRPC, brokers, controllers, or DTOs. You can add/change interfaces (REST, gRPC, events) without touching these rules.
2) What comes in from other systems (upstream)
Example for a Cart service: it uses Catalog, Pricing, Profile, Orders. Those systems speak their own language. Convert their data into Cart’s terms. Do the conversion at the edge with adapters / an anticorruption layer. Goal: no foreign models leak into your core rules.
3) What goes out to clients (downstream)
Web and mobile apps (and others) call your Cart. Offer intention-revealing endpoints or events (REST, gRPC, pub/sub). Keep request handlers, DTO parsing, and input validation at the edge — not in the core. You can even put these edge parts in their own context to avoid tight coupling.
Tactical Design
Tactical design gives you simple building blocks to shape the domain model so it matches the business and stays easy to change.
1) Entities — things with identity
Have a stable ID and a lifecycle (they change over time). Defined by who they are, not just their attributes.
Example: in e-commerce, an Order (id=123) moves from Open → Confirmed → Shipped. Same order, changing state.
Objects that have a unique identity and possess a thread of continuity are called Entities. They are not defined solely by their attributes, but more by who they are.
2) Value Objects — no identity
No global ID; defined only by their values. Immutable: to “change” one, create a new instance.
Great for attributes you can reuse: e.g., Money, Quantity, Address. Must validate on creation (respect business rules). If data is invalid, don’t create the object
3) Aggregates — consistency boundaries
Aggregates are clusters of entities and value objects that are treated as a single unit. They define a consistency boundary, ensuring that changes to the domain are consistent and validated within the aggregate.
Key concepts:
Cluster that changes together: A small group of entities/value objects saved as one unit (e.g., Order + OrderLines).
Aggregate Root: One entry point that enforces rules; outside code talks only to the root’s methods.
Boundary: Clear inside vs. outside. No direct access to inner parts from other aggregates — use the root or IDs.
Consistency: Rules (invariants) must hold after every change. If a change breaks a rule, reject it.
Transactional unit: One aggregate = one transaction. For cross-aggregate work, use events/sagas (eventual consistency).
Example: Order (root) contains OrderLines (entities or value objects like Money/Quantity). Add/remove lines, apply discounts, and check totals through Order so invariants stay true.
4) Repositories — gateways to aggregates
Repositories provide an abstraction for accessing aggregates. They handle the persistence and retrieval of aggregates, allowing the domain model to remain focused on business logic rather than data access concerns.
Domain events
The image shows how domain events keep aggregates in sync. When a user starts an order, the Order aggregate publishes an OrderStarted event. The Buyer aggregate handles that event and creates or updates a Buyer record in the ordering service, using user data from the identity service (for example, user ID, name, and email). This keeps Order and Buyer aligned without a big cross-service transaction; the event is the handoff. With retries and idempotency, the system stays consistent even if messages are delayed.
Domain Events record facts that already happened in the business. Name them in the past tense — OrderPlaced, ProductCreated, PaymentFailed — because they describe completed actions.
One context publishes the event and others react to it. For example, when Order Processing emits OrderPlaced, the Inventory context listens and reduces stock. This can happen inside the same process or over a message bus.
Domain events facilitate loose coupling between different parts of the system. When an event occurs, it can be published to an event bus or messaging system, allowing other parts of the system to subscribe to and react to the event independently.
Using events makes side effects visible instead of hidden in code, reduces coupling between parts of the system, and helps keep several aggregates consistent without one big transaction. Keep each event’s data small and meaningful (IDs, amounts, timestamps), treat it as an immutable fact, and evolve the contract with versioning when needed.
A single domain event can trigger several follow-up actions. From one event, you might update other aggregates in the same domain and also kick off cross-service work by turning it into an integration event on your event bus.
Ensuring Reliability
To keep things reliable, write the changed aggregate and its domain event in the same transaction. With an ORM, that means saving the aggregate to its table and the event to an event-store table, then committing once.
If you use event sourcing, the aggregate’s state is fully represented by its events anyway. The usual way to guarantee this atomic write and later delivery is the Outbox Pattern: store the event with the aggregate, commit, then a background publisher reads the outbox/event table and publishes to subscribers.
Single transaction across aggregates versus eventual consistency across aggregates
In DDD, the usual rule is one transaction per aggregate. When a change touches other aggregates, you keep them in sync eventually, not in the same ACID transaction. Authors like Eric Evans and Vaughn Vernon promote this approach: update one aggregate, publish a domain event, and let other parts react asynchronously.
The reason is scale. Large, cross-aggregate transactions hold many locks and slow down a busy system. Fine-grained transactions keep throughput high, while background handlers bring the rest of the model up to date a bit later.
Not every business rule must be instantly consistent. Domain experts should determine which operations truly require atomic updates. If you discover an operation that always needs a multi-aggregate transaction, consider whether your aggregate boundaries are wrong — or whether those parts should be one larger aggregate.
In practice, you update one aggregate, record an event, and rely on mechanisms like outbox + message delivery, retries, and idempotent handlers to reach consistency without a big distributed transaction.
What is Event Sourcing?
Event Sourcing means you save every domain event that happened to an aggregate and treat those events as the source of truth. The current state isn’t stored as one row; you rebuild it by replaying the events in order.
An event store is just an append-only log/table where new events are added and past ones aren’t changed. This makes writes simple and fast, helps with audit/history, and can scale well. For reads, you often build projections/read models from the events to answer queries quickly. You can also use snapshots to avoid replaying a very long event stream.
What is Event Storming?
Event Storming is a fast, hands-on workshop that brings domain experts and developers together to understand the problem quickly. Instead of starting with database tables or class names, the group maps the business flow using past-tense events (e.g., Order Placed, Payment Failed).
In a session, everyone stands around a large surface and adds sticky notes for events, the actions that trigger them, the people/systems involved, and any rules or risks. As the picture grows, the team builds a shared language, spots bounded contexts, and uncovers gaps or tricky areas.
The result is a clear, shared view of how the business works and a starting point for the domain model and next design steps.
Steps and Rules
DDD/Hexagonal architecture implimentation part:
In Classic Layered → request flows through Controller → Service → Repository (where rules often leak into service or DB).
In DDD/Hexagonal → request flows through Controller → Application Service → Domain (business rules inside) → Repository Interface → Infrastructure implementation.
This ensures the Domain is always central and pure, unaffected by DB, frameworks, or delivery channels.
Classic layered:
Hexagonal/DDD
Classic Layered → Service depends directly on MongoRepository. If you switch DB (Mongo → PostgreSQL), you must change the service code.
DDD / Hexagonal → Domain defines its own repository interface. Infrastructure just plugs in the DB implementation. If you change DB, only Infra changes; Domain and Application remain the same.
