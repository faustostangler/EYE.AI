---
name: Hexagonal Architecture: A complete guide to robust and testable software design
keywords: (placeholder)
metadata:
  url: https://chakray.com/hexagonal-architecture-a-complete-guide-to-robust-and-testable-software-design/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Hexagonal Architecture: Overview and Implementation
Skip to Main Content 
Home
Initiatives Strategic
Integration Strategy
Digital Agility
Leveraging Data
Merger & Acquisition
Customer Experience
Reducing Integration TCO
Legacy Modernisation
Business Automation Technical
Migrate Systems & Services
Leveraging Cloud
API Management
API & Integration Security
Infrastructure Automation & DevOps
Identity & Access Management
Observability Process Automation
Joiners, Movers & Leavers
Quote to Cash
Source to Pay SaaS Integration
Salesforce
Workday
SAP Industry Specific
Banking and Finance
Healthcare
Telco
Retail
Expertise Expertise Explore the core integration capabilities Chakray can help provide to your organisation. View the page
API Management Tools and capability to control and govern your API estate and the lifecycle of those APIs.
DevOps & CI/CD Enables automated deployment, integration and infrastructure builds within an organisation.
iPaaS A low code cloud based service for integration of on-premise and cloud/SaaS technologies.
IAM Provides administrators with the ability to manage digital identities throughout their lifecycle.
Microservices Services built around business capabilities with minimum centralised management.
Integration as a service The provision of an integration or API solution as a complete end-to-end service.
Event Streaming The capture and persistence of data events in real-time from numerous event sources.
ESB/SOA Large implementations of service oriented enterprise integration patterns and services.
Technologies Technologies Choosing the right integration technology can be critical to your outcomes. We are integration specialists working with best of breed technologies covering Integration, API Management, DevOps and Identity Management All technologies
WSO2 Open source Integration, API and Identity Management technology
Gravitee Event-native API Management platform
Workato Enterprise IPaaS platform that unifies integration and automation
Confluent Data streaming platform
Anka All-in-One Observability Platform
Red Hat Enterprise open-source solutions: Middleware, IT automation, hybrid cloud infrastructure and more
Services
Implementation
More
Careers
About
Case Studies
Articles
EBooks
Webinars
Contact
en
English
Español
Home
Articles
Hexagonal Architecture: A complete guide to robust and testable software design
Hexagonal Architecture: A complete guide to robust and testable software design
Publication date: November 19, 2025 (Updated on: March 13, 2026)
Is there a way to develop software that doesn't directly depend on frameworks, databases, or external services, and yet remains easy to adapt and scale?
This is the premise of Hexagonal Architecture, also known as Ports and Adapters Architecture — a design pattern focused on creating a more flexible and adaptable software ecosystem by separating business logic from external dependencies.
In this article, we will answer in detail the questions: What is it? What are its benefits? and How can it be implemented? We will also discuss the challenges we may face and compare Hexagonal Architecture with other software design patterns.
Table of Contents
Toggle
What is Hexagonal Architecture?
What are the components of Hexagonal Architecture?
How is service testing made easier?
What are the benefits of Hexagonal Architecture?
Hexagonal Architecture vs. other architectural patterns
How to implement Hexagonal Architecture? (Step by step)
Common challenges in implementing Hexagonal Architecture
What is Hexagonal Architecture?
This development pattern, initially proposed by Alistair Cockburn around 2005, aims to make the core of the application (the domain) independent from external details. This means that the application can run without requiring a user interface or a database and can be tested in isolation through ports and adapters.
Although it is a relatively old concept, it remains relevant today thanks to its principle of decoupling frameworks and technology. In other words, it focuses on separating what changes quickly from what changes slowly — that is, the business logic.
What's the problem with the traditional layered approach?
Layered Architecture
Before the emergence of this and other architectural approaches, it was most common to design applications using a layered architecture. In this model, each layer depends on the one below it: the user interface depends on the business layer, which in turn depends on the data access layer.
Each “layer” can be understood as a package or library that exposes classes and methods to the layer above.
For example, we might have a library for data access:
// DataAccessLayer.dll
public class ProductDAO {
// Database access
}
And another library for business logic that directly depends on the previous one:
// BusinessLogicLayer.dll
using DataAccessLayer;
public class ProductBO {
private ProductDAO productDAO;
// Business logic that depends on data access
}
While this approach is easy to understand and has been widely adopted, it tends to create dependencies on external details. Ultimately, the domain becomes aware of or adapts to external elements or the technology in use. Moreover, technological changes become difficult, unit testing is more expensive (since it often requires setting up infrastructure or creating extensive mocks), and accidental coupling becomes a frequent consequence.
What does Hexagonal Architecture offer compared to the traditional layered approach?
Hexagonal Architecture, on the other hand, reverses the direction of dependencies: the domain knows nothing about external details — instead, the adapters know about the domain through ports (interfaces). This allows the following:
Replace the database without touching the business logic.
Change the user interface (for example, from a GUI to an API or CLI) without affecting the core.
Test the domain easily using simple mocks, without needing real infrastructure.
In short, this approach protects the business core and ensures that all interactions with the outside world occur through clear contracts. As a result, it reduces the cost of change, ensures quality, and extends the software's lifespan, even as surrounding technologies evolve.
The following article might interest you: Apache Apisix: The high-performance cloud-native API gateway for microservice architectures
What are the components of Hexagonal Architecture?
Hexagonal architecture
The essence of Hexagonal Architecture is clear: to isolate business logic from external sources — such as frameworks, databases, and third-party services — to make it easier to test and control through users and programs.
But how can we truly fulfill this promise? How is the architecture structured, and what components enable this isolation?
To understand this, we need to define three main concepts: the domain, the adapters, and the ports. Let's take a closer look at each of them and explore some of the fundamental ideas behind the model.
1. What is the domain?
The domain represents the core business logic — its processes, rules, and properties that define and regulate how it operates. The domain code must remain completely isolated from any external technology or dependency, acting as the heart of the application. This ensures a clean, coherent, and fully decoupled design, independent from the surrounding infrastructure.
2. What are ports?
Ports are responsible for transmitting information between the adapters and the core of the application, acting as intermediaries — much like a physical port on a computer that allows different devices to connect.
A port serves as a contract that defines the rules of communication between the external world and the domain.
There are two main types of ports:
Inbound Ports: These represent the operations that the domain offers to the outside world. They allow the application to receive requests or commands from other layers, such as the user interface or external services. In other words, they define what the domain can do when invoked from the outside.
Outbound Ports: These specify the operations that the domain needs to perform toward the outside — for example, to access databases, send messages, or consume external services. Outbound ports define the domain's dependencies on its environment so it can fulfill its responsibilities.
3. What are adapters?
Following the same principle, adapters are responsible for communicating external information with the core of the application through the ports, which act as intermediaries.
These adapters are part of the outer layer of the hexagon, which focuses on the infrastructure.
Thanks to this separation, it becomes possible to modify components or technologies without affecting the business logic.
There are also two types of adapters:
Inbound Adapters: These are responsible for receiving external requests (for example, from graphical interfaces or REST APIs) and translating them into a format that the domain can understand. Their main role is to invoke the corresponding inbound ports to execute the business logic.
Outbound Adapters: These allow the domain to interact with external resources, such as databases, third-party services, messaging systems, or file storage. They implement the outbound ports defined by the domain and serve as a “translation layer” between the business needs and the specific technologies used in the infrastructure.
Keep learning about enterprise architecture models: Enterprise Architecture vs Solution Architecture vs Technical Architecture: Key differences
4. What is dependency inversion and how is it related?
This concept corresponds to the fifth principle of the set of design guidelines in object-oriented programming known by the acronym SOLID.
The letter D stands for the Dependency Inversion Principle (DIP), whose original definition was proposed by software engineer Robert C. Martin, who expressed it as follows:
“High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.”
— Robert C. Martin
In other words, instead of having high-level modules (those containing the core business logic) depend directly on low-level modules (such as databases, controllers, or external services), both should rely on abstractions — that is, interfaces or contracts that define how they communicate with each other.
This way, changes in implementation details do not affect the overall functioning of the system.
For example, if a database or an external service is replaced, you only need to modify the component that implements the corresponding interface, without altering the business logic.
How is service testing made easier?
By depending on abstractions instead of concrete implementations, it becomes easy to replace real dependencies with simulated or “mock” versions during testing.
This means a service can be tested in isolation, without the need to connect to databases, external APIs, or other complex modules. As a result, unit tests become more predictable, faster, and safer, since the behavior of dependencies is completely controlled within the testing environment.
What are the benefits of Hexagonal Architecture?
Hexagonal Architecture promotes software designs that are adaptable and scalable to new technologies. Its benefits can be summarized in four key characteristics:
1. High maintainability
By clearly separating responsibilities between the domain, ports, and adapters, the code becomes more modular and easier to understand.
This separation simplifies bug detection and correction, as well as the implementation of improvements without affecting other parts of the system.
Independence between layers also reduces the risk of regressions and accelerates development cycles.
2. Advanced testability
Thanks to the low coupling between components, each module can be tested independently using mocks or simulated implementations.
This enables unit testing and controlled integrations without relying on real infrastructure, ensuring greater reliability and shorter validation times in enterprise environments.
3. Flexibility
Hexagonal Architecture allows new technologies or external services to be integrated without modifying the business core.
By defining connection points through interfaces (ports), you can replace or add adapters (for example, a database, messaging provider, or external API) without altering the system's core logic.
4. Adaptability
This architecture supports controlled system evolution. The domain remains stable while technological implementations can be updated or migrated with minimal friction. This results in greater resilience to change and a longer lifespan for the software.
The following article might interest you: DevOps: Monolithic architecture vs Microservices  
Talk to our experts!
Contact our team and discover the cutting-edge technologies that will empower your business.
contact us
Hexagonal Architecture vs. other architectural patterns
So far, we've discussed the characteristics and benefits of Hexagonal Architecture. However, how does it differ from other approaches? In this section, we'll focus on defining these differences.
Hexagonal Architecture vs. Clean Architecture
The clean architecture
Both Clean Architecture (proposed by Robert C. Martin) and Hexagonal Architecture share the same core principles — framework independence and a domain-centric design.
Their main goal is to ensure that the business rules remain isolated from external technologies.
Clean Architecture is based on the idea of structuring an application in concentric rings, each representing a different level of abstraction. These rings define clear boundaries and direction of dependencies — always pointing inward toward the domain.
It is typically composed of four main components:
Entities: Represent domain models containing specific business rules with long-term stability.
Use Cases / Interactors: Orchestrate the application rules, coordinate entities, and define input and output flows.
Interface Adapters: Act as translators between the external world and the use cases (e.g., controllers, presenters, mappers, and repositories defined as interfaces).
Frameworks & Drivers: Contain peripheral details such as databases, web frameworks, user interfaces, messaging systems, or devices. These components can be replaced without affecting the core domain.
Hexagonal Architecture vs. Onion Architecture
Onion Architecture This architecture, defined by Jeffrey Palermo in 2008, is based on the principle of decoupling business logic from infrastructure details such as the database or user interface (UI).
This model proposes structuring applications in layers, with the business domain as the central axis, and the following levels can be defined as:
Domain (Domain Model): Entities and value objects containing business rules.
Domain Services: Business logic that doesn't fit within a single entity; includes contracts such as repositories.
Application (Application Services): Orchestrates use cases, coordinates domains, and defines the necessary ports (interfaces).
Infrastructure: Implementations of the ports — ORM/database, messaging, file handling, email, external APIs.
In practice, the differences between this model and Clean Architecture are subtle, since both pursue the same principle: placing the domain at the center and isolating details to make testing, maintenance, and technology replacement easier.
Hexagonal Architecture and Domain-Driven Design (DDD)
Domain Driven Designs
This design, initially introduced by Eric Evans in his 2003 book Domain-Driven Design: Tackling Complexity in the Heart of Software, focuses on modeling the business core (for example, sales, logistics, and billing) so that the software reflects its real logic and rules.
To achieve this, it promotes continuous collaboration between domain experts and developers, using a shared language (ubiquitous language) that is directly translated into code. This ensures that the system not only solves technical problems but also aligns closely with business needs and processes, making it easier to evolve and maintain as requirements change.
Among its key components, we can mention:
Ubiquitous Language: A common vocabulary shared by business and development teams, also reflected in the code.
Bounded Contexts: Divide the system into distinct areas, each with its own model and language, to avoid ambiguity or overlap.
Entities and Value Objects: Represent important business concepts, with entities having identity and value objects describing characteristics or attributes.
Aggregates: Groups of entities and values treated as a coherent unit.
Services and Repositories: Services perform business actions, while repositories handle storing and retrieving domain data without exposing technical details.
Domain Events: Describe significant events that occur within the business domain.
Application Layer: Coordinates system actions but does not contain business logic itself.
Anti-Corruption Layer: Protects the domain model when interacting with external systems, ensuring that outside influences don't pollute internal business logic.
Role in microservices
Microservices architecture
A microservice is a small, independent service unit that performs specific tasks within a larger system. Each microservice operates autonomously and communicates with others through well-defined APIs.
In the context of Hexagonal Architecture, each microservice can internally implement this architectural style, structuring itself around its domain and clearly separating business logic from external details.
This means that within each microservice, you can define ports (interfaces) that represent the inputs and outputs of the system, as well as adapters that implement these interfaces to interact with databases, external APIs, or messaging queues.
In this way, each microservice maintains a high degree of independence, testability, and replaceability, aligning with the principles of low coupling and high cohesion that characterize Hexagonal Architecture and the best practices of distributed system design.
Want to learn more about how microservice architectures work? This resource might interest you: Migration to Microservices-based architectures: Success stories
Comparative table of architectures
Below is an overview of different architectures and how they relate to Hexagonal Architecture.
How to implement Hexagonal Architecture? (Step by step)
Define the core (domain + application)
Start by writing the domain model (entities/VOs) and the use cases/application services without any external library.
Goal: the core should compile and have tests without DB, web, or messaging.
Declare the ports as interfaces
Input ports: how a request enters the core (e.g., CreateOrder, GetBalance).
Output ports: what the core needs from the outside (e.g., Payments, Inventory, Clock, EventBus).
Ports live next to the use case and describe conversations with the external world, not technologies.
Implement adapters for each port
Input adapters: They translate the request into an input port call and format the response.
Output adapters: DB/external REST/Kafka/Email components that implement the output ports.
You may have multiple adapters per port (e.g., Postgres and Mongo for the same repository).
Dependency inversion and composition
The core does not know about frameworks. At the application edge (bootstrap), you assemble everything: create adapters, inject them into use cases, and expose controllers.
Keep dependencies pointing inward (details → ports → use cases → domain).
Suggested project structure (example)
/src
/domain # entities, VOs, domain rules
/application # use cases + ports (interfaces)
/adapters
/in/web # controllers/http -> input ports
/in/cli # batch commands
/out/db # database repositories -> output ports
/out/messaging # publishers/consumers -> output ports
/bootstrap # dependency composition/injection
The exact organization may vary by language, but it is important to respect the direction of dependencies and the isolation of the core.
Design stable contracts in the ports
Model operations and DTOs for the use case (do not expose DB models or external API models).
Ports must support contract tests to validate interchangeable adapters.
Layered testing (core first)
Unit tests for the domain and use cases (no frameworks).
Contract tests for output adapters (e.g., the repository must behave the same in memory and with Postgres).
Integration tests at the edge (HTTP controller ↔ use case ↔ real/double adapters).
Observability at the edges, not in the core
Metrics, tracing, and logging live in adapters or bootstrap; the core only uses ports to notify events when necessary.
Migration / evolution strategy
Start with a modular monolith in a hexagonal structure; later you can move adapters to separate processes without touching the core.
Useful when you want to modernize UI/DB without rewriting business logic.
Minimal flow example
POST /orders (HTTP adapter) → invokes CreateOrder (input port).
CreateOrder uses Inventory and Payments (output ports).
Concrete adapters: InventoryRestAdapter, PaymentsStripeAdapter, OrderRepositoryPostgres.
The bootstrap wires everything together and exposes the endpoint.
Implementation example
Hexagonal Architecture in Practice
To understand how the principles of Hexagonal Architecture materialize, let's analyze a concrete implementation of a reservation management system. This example follows the best practices from AWS's Prescriptive Guidance demonstrating the separation between the central domain and the external adapters.
Structure of the Core Domain
Recipient Entity: The Heart of the Business. The Recipient entity encapsulates the core business rules without any dependency on external frameworks or infrastructure:
python
class Recipient:
def init( self, recipient_id: str, email: str, first_name: str, last_name: str, age: int):
self. __recipient_id = recipient_id
self. __email = email
self. __first_name = first_name
self. __last_name = last_name
self. __age = age
self. __slots = []
@property
def recipient_id( self) -> str:
return self. __recipient_id
@property
def email( self) -> str:
return self. __email
def add_reserve_slot( self, slot: 'Slot') -> bool:
if self. are_slots_same_date( slot):
return False
self. __slots. append( slot)
return True
def are_slots_same_date( self, slot: 'Slot') -> bool:
for selfslot in self. __slots:
if selfslot. reservation_date == slot. reservation_date:
return True
return False
Ports: Communication Interfaces
Input Port: Reservation Management. The input port defines the contract for the operations that the system exposes to the outside world:
python
class IRecipientInputPort( ABC):
@abstractmethod
def make_reservation( self, recipient_id: str, slot_id: str) -> Status:
pass
Use Case Implementation
python
class RecipientInputPort( IRecipientInputPort):
def init( self, recipient_output_port: IRecipientOutputPort, slot_output_port: ISlotOutputPort):
self. __recipient_output_port = recipient_output_port
self. __slot_output_port = slot_output_port
def make_reservation( self, recipient_id: str, slot_id: str) -> Status:
# Retrieves the entities through the output ports
recipient = self. __recipient_output_port. get_recipient_by_id( recipient_id)
slot = self. __slot_output_port. get_slot_by_id( slot_id)
# Executes the domain logic
ret = recipient. add_reserve_slot( slot)
# Persists the changes through the output port
if ret == True:
ret = self. __recipient_output_port. add_reservation( recipient)
return Status. SUCCESS if ret else Status. FAILURE
Adapters: The connection to the outside world
DynamoDB Database Adapter
This adapter implements persistence specifically for DynamoDB, keeping the domain isolated from infrastructure details:
python
class DDBRecipientAdapter( IRecipientAdapter):
def init( self):
ddb = boto3. resource('dynamodb')
self. __table = ddb. Table( table_name)
def load( self, recipient_id: str) -> Recipient:
try:
response = self. __table. get_item( Key={'pk': 'RECIPIENT#' + recipient_id})
item = response['Item']
return Recipient(
recipient_id= item['recipient_id'],
email= item['email'],
first_name= item['first_name'],
last_name= item['last_name'],
age= int( item['age'])
)
except ClientError as err:
logging. error( err)
return None
def save( self, recipient: Recipient) -> bool:
try:
self. __table. put_item( Item={
'pk': 'RECIPIENT#' + recipient. recipient_id,
'recipient_id': recipient. recipient_id,
'email': recipient. email,
'first_name': recipient. first_name,
'last_name': recipient. last_name,
'age': recipient. age
})
return True
except ClientError as err:
logging. error( err)
return False
Configuration and dependency injection
Factory Pattern for Wiring
The factory is responsible for wiring all dependencies, creating a composition root where the ports are connected to their adapters:
python
def get_recipient_input_port():
return RecipientInputPort(
RecipientOutputPort( DDBRecipientAdapter()),
SlotOutputPort( DDBSlotAdapter())
)
Lambda handler as the entry point
In a serverless environment, the Lambda handler acts as the primary adapter, transforming events into calls to the input port:
python
def lambda_handler( event, context):
try:
recipient_id = event['pathParameters']['recipient_id']
slot_id = event['pathParameters']['slot_id']
recipient_input_port = get_recipient_input_port()
status = recipient_input_port. make_reservation( recipient_id, slot_id)
return {
'statusCode': 200 if status == Status. SUCCESS else 400,
'body': json. dumps({'status': status. name})
}
except Exception as e:
logging. error( f”Error processing request: { str( e)}“)
return {
'statusCode': 500,
'body': json. dumps({'error': 'Internal server error'})
}
Flow of a typical request
Input: An HTTP request arrives at the primary adapter (Lambda handler)
Transformation: The handler extracts the parameters and converts them into domain objects
Delegation: The corresponding input port is invoked with the parameters
Business Logic: The use case coordinates the entities and applies the business rules
Persistence: Through the output ports, the changes are persisted
Response: The result flows back through the layers until it reaches the primary adapter
Implementation considerations in different languages
Below are some examples using Java and Python:
Java
In pure Java, the implementation focuses on module separation and the use of interfaces to define contracts.
Module Structure: It is common to organize the project into at least two modules: core (or domain) and application. The core module contains the entities and the output port interfaces (such as UserRepository), with no external dependencies. The application module contains the adapters and depends on the core.
Pure Core: The core must be compilable and testable without the need for any framework. The only allowed dependencies are those of the language itself.
Example: Output Port in the Core This code defines an output port in the core module. The concrete implementation (adapter) will be provided externally.
java
// In the 'core' module
// Outbound Port
public interface UserRepository {
User findById( Long id);
void save( User user);
}
Spring Boot
Spring Boot is ideal for implementing this architecture thanks to its dependency injection system. The key is to prevent framework annotations from contaminating the core.
Configuration as “Glue”: Use @Configuration classes to connect the core beans with the Spring adapters, keeping the core free of annotations such as @Service.
REST and JPA Adapters: Spring MVC controllers act as primary (or input) adapters, while Spring Data JPA repositories serve as secondary (or output) adapters.
Example: Input Adapter (REST Controller) The controller receives HTTP requests and delegates the logic to the application service (input port).
java
// Primary Adapter
@RestController
@RequestMapping(“/api/users”)
public class UserController {
private final UserService userService; // Puerto de Entrada
public UserController( UserService userService) {
this. userService = userService;
}
@GetMapping(“/{id}”)
public ResponseEntity< UserDto> getUser(@PathVariable Long id) {
User user = userService. getUserById( id);
return ResponseEntity. ok( UserDto. fromDomain( user));
}
}
Example: Configuration to Connect the Core
This class creates the core service bean, injecting the repository adapter into it.
java
@Configuration
public class UserConfiguration {
@Bean
public UserService userService( UserRepository userRepository) {
return new UserServiceImpl( userRepository);
}
}
Python
You can use a manual dependency injection system or libraries such as dependency_injector.
Package Structure: Organize the project into packages such as domain, ports, adapters.
Dependency Inversion: Use-case functions must receive the adapters they need (for example, a repository) during initialization.
Example: Use Case and Port
python
# In domain/ports/user_repository.py (Outbound Port)
class UserRepository:
def find_by_id( self, user_id):
raise NotImplementedError
# In domain/services/user_service.py (Use Case / Entry Point)
class UserService:
def init( self, user_repository: UserRepository):
self. _user_repository = user_repository
def get_user( self, user_id):
return self. _user_repository. find_by_id( user_id)
# In adapters/orm/sqlalchemy_repository.py (Secondary Adapter)
class SqlAlchemyUserRepository( UserRepository):
def find_by_id( self, user_id):
# … lógica usando SQLAlchemy …
return user
# In adapters/api/flask_app.py (Primary Adapter)
app = Flask( name)
user_repository = SqlAlchemyUserRepository()
user_service = UserService( user_repository)
@app.route(“/users/<user_id>”)
def get_user( user_id):
user = user_service. get_user( user_id)
return jsonify( user. to_dict())
Other Languages & Frameworks
The concepts of Hexagonal Architecture are applicable to almost any ecosystem.
TypeScript/Node.js: It can be implemented very similarly to Java. Ports are defined as TypeScript interfaces, and adapters are classes that implement them. Frameworks such as Nest.js are very well suited for this pattern.
.NET: Just like Spring Boot, .NET includes a robust dependency injection container that makes it easy to connect core interfaces with their implementations in the infrastructure layer.
Common challenges in implementing Hexagonal Architecture
When implementing Hexagonal Architecture, teams often encounter several recurring challenges that go beyond the technical aspects. The following table summarizes these common obstacles to help you identify them and prepare to face them.
Hexagonal Architecture represents more than just a technical pattern: it is a design philosophy that prioritizes software longevity and maintainability. By clearly separating the business core from technological details, organizations can build systems that evolve with market demands without requiring costly rewrites.
The benefits in testability, flexibility, and maintenance are not just theoretical—they are visible to teams around the world adopting this approach.
However, successful implementation requires an initial learning curve, and the challenge of managing multiple adapters can become a significant obstacle without proper guidance.
If your team is considering this transition or needs to optimize an existing implementation, you don't have to do it alone. Contact us today and let's drive a structured and decoupled architecture together. 
Martín Mandujano
Digital Marketing   [](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fchakray.com%2Fhexagonal-architecture-a-complete-guide-to-robust-and-testable-software-design%2F&title=Hexagonal+Architecture%3A+A+complete+guide+to+robust+and+testable+software+design&summary= Is+there+a+way+to+develop+software+that+doesn%E2%80%99t+directly+depend+on+frameworks%2C+databases%2C+or+external+services%2C+and+yet+remains+easy+to+adapt+and+scale+This+is+the+premise+of+Hexagonal&source=) 
Subscribe to our newsletter
Enter your email address below to receive the latest articles, ebooks and newsletters from Chakray direct to your inbox!
Share   [](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fchakray.com%2Fhexagonal-architecture-a-complete-guide-to-robust-and-testable-software-design%2F&title=Hexagonal+Architecture%3A+A+complete+guide+to+robust+and+testable+software+design&summary= Is+there+a+way+to+develop+software+that+doesn%E2%80%99t+directly+depend+on+frameworks%2C+databases%2C+or+external+services%2C+and+yet+remains+easy+to+adapt+and+scale+This+is+the+premise+of+Hexagonal&source=) 
Contact our team to discuss your needs and find out how Chakray can help can help deliver your successful outcomes, talk to our experts!
Get in touch
Popular Articles
The four dimensions of a hybrid integration platform
Why All Organisations Must Prioritise Digital Agility In Response To Coronavirus
What are microservices? Definition, characteristics, advantages and disadvantages
5 main benefits of Identity Management
What are the differences between REST and SOAP?
[
Learn how to implement a microservice architecture with WSO2
Download Ebook](https://chakray.com/ebooks/learn-implement-architecture-microservices/)
Related Articles
Catch up on the latest news, articles, guides and opinions from Chakray. 
Artificial intelligence law in Spain: Technical requirements, risks, and adaptation for businesses
Martín Mandujano
Digital Marketing   [](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fchakray.com%2Fhexagonal-architecture-a-complete-guide-to-robust-and-testable-software-design%2F&title=Hexagonal+Architecture%3A+A+complete+guide+to+robust+and+testable+software+design&summary= Is+there+a+way+to+develop+software+that+doesn%E2%80%99t+directly+depend+on+frameworks%2C+databases%2C+or+external+services%2C+and+yet+remains+easy+to+adapt+and+scale+This+is+the+premise+of+Hexagonal&source=)  
Api Management
API First: what it is, benefits, and how to implement it with security, governance, and scalability
Martín Mandujano
Digital Marketing   [](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fchakray.com%2Fhexagonal-architecture-a-complete-guide-to-robust-and-testable-software-design%2F&title=Hexagonal+Architecture%3A+A+complete+guide+to+robust+and+testable+software+design&summary= Is+there+a+way+to+develop+software+that+doesn%E2%80%99t+directly+depend+on+frameworks%2C+databases%2C+or+external+services%2C+and+yet+remains+easy+to+adapt+and+scale+This+is+the+premise+of+Hexagonal&source=)  
Api Management
How AI is integrated into API management platforms
Martín Mandujano
Digital Marketing   [](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fchakray.com%2Fhexagonal-architecture-a-complete-guide-to-robust-and-testable-software-design%2F&title=Hexagonal+Architecture%3A+A+complete+guide+to+robust+and+testable+software+design&summary= Is+there+a+way+to+develop+software+that+doesn%E2%80%99t+directly+depend+on+frameworks%2C+databases%2C+or+external+services%2C+and+yet+remains+easy+to+adapt+and+scale+This+is+the+premise+of+Hexagonal&source=)  
How we can help
Initiatives
Expertise
Technologies
Services
Implementation
Chakray
Home
Careers
About
Contact
Learning
Articles
EBooks
Subscribe to our newsletter
Register to receive our monthly newsletter containing the latest articles, guides and opinions in the world of integration, delivered straight to your inbox.
Follow Us
  
Copyright 2026 © ISO 9001:2015 certified.
This site is protected by hCaptcha and its Privacy Policy, Policies and Procedures and Terms of Service apply.
Security Policy
Cookies Policy
Quality Policy
Privacy Policy
