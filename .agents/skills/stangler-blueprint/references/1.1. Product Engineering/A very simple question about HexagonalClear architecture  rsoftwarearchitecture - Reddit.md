---
name: A very simple question about Hexagonal/Clear architecture : r/softwarearchitecture - Reddit
keywords: (placeholder)
metadata:
  url: https://www.reddit.com/r/softwarearchitecture/comments/1brqh4t/a_very_simple_question_about_hexagonalclear/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
A very simple question about Hexagonal/Clear architecture : r/softwarearchitecture
Skip to main content A very simple question about Hexagonal/Clear architecture : r/softwarearchitecture
Open menu
Open navigation 
Go to Reddit Home 
r/softwarearchitecture
Get App
Get the Reddit app
Log In
Log in to Reddit
Expand user menu
Open settings menu
Skip to Navigation Skip to Right Sidebar
Back
Go to softwarearchitecture
r/softwarearchitecture
•
2y ago
ipcock
Locked post
Stickied post
Archived post
Report
A very simple question about Hexagonal/Clear architecture
Discussion/Advice
So, in my mind there are following layers:
Domain - domain entities representing things existing in the real world, which are directly connected to the business domain. It depends on nothing but itself and...
Application - Use Cases / Services (I don't really get the difference), which orchestrate actions going on with domain entities. For example, creating a user: usecases depends on an interface of a repository, which has a method for creating a said user. I'm not sure if this layer should check the validness of a DTO (e.g. we shouldn't create a user with negative ID).
Presentation layer - here we have implementations of interfaces, declared in the application layer. It is also used to connect the program with real world: it takes input from a user and presents info to him.
So my general question is: what should domain entities actually do? Do they just validate themselves? Also, If they don't have an access to a database (and therefore don't break dependency direction), it can't even check if the ID is unique.
Also, is my view of hexagonal architecture somewhat correct? Thanks for any answers in advance
Upvote 13 Downvote 20 Go to comments Share
Sort by: Best
Open comment sort options
Best
Top
New
Controversial
Old
Q&A
Search Comments Expand comment search
Cancel
Comments Section
gnu_morning_wood
•
2y ago
• Edited 2y ago
I think it's easiest to start from the beginning.
Layered architecture is the idea that there are layers within an application that are specialised.
Probably the most famous of the early layered architecture is MVC, Model, View, Controller.
Model speaks about the way the data/knowledged is stored
View speaks the way that the data is presented
Controller speaks about the way that the data is processed
Now, if you change the names of those you will see a more current layered architecture.
Model - Datastore
View - API
Controller - Business logic
The idea of Hexagonal architecture, aka Ports and Adapters, is to focus on the Business logic, and have everything depend on that, and not the other way around. That is, the business layer should not import the datastore layer libraries, the business layer should not know that there is any such thing.
To achieve this, the business layer defines and uses interfaces to communicate to the datastorage layer, and the datastorage layer provides code that satisfies those interfaces allowing the business layer to talk to a postgres, or mysql, or mongo, or whatever, and never know what that data store is.
This is called the Dependency Inversion Principle.
This leads us to why Hexagonal or Ports and Adapters gets its name - the business logic is at the centre of the hexagon, and all services that it makes use of sit around it.
The second part of the communication between the business logic and the data storage is the fact that you don't want the business logic to know how the data is represented in the datastore. You most definitely don't want the business logic to use a mySQL specific field type, because your code is then coupled to mysql, and it's then a major breaking change to - say - move some of the data into a Redis cache.
This is where the Data Transfer Object (DTO) comes into play - the business logic says "here's some data, ints, strings, whatever", and passes it to the data storage layer. The data storage layer says "oh, ok I will translate that into a representation that works for me - a Data Access object (DAO)", and then save it, retrieve it etc.
Retrieval is the Datastorage layer getting the data, as a DAO, translating it back into a DTO and passing the DTO back to the Business logic.
As for validation of the DTO - each layer has its own validation rules - the business layer might say that a user ID cannot be negative (although there's no reason that it couldn't be), but the Data storage layer will have different rules, it might say that the User ID must be a string (I cannot think why it might be that, but it's possible).
This means that each layer will validate that the data is valid for that layer - the data storage layer will additionally validate that the DTO translates to a DAO and that DAO translates exactly back (no data loss).
The rest of your comment/question is heavily swayed toward Domain Driven Design :)
Upvote 24 Downvote Reply Award Share
Report
Award
Share 
Blackgarion
•
2y ago
Your answer is amazingly well writen and believe me I'm just saying this in case somebody wants to Google the terms you used but the Its the dependency inversion principle, not reversal, but again I don't want to be an "aktually guy", just in case somebody wants to dive deep into what you explained.
Upvote 4 Downvote Reply Award Share
Report
Award
Share
More replies
TinnedCarrots
•
2y ago
I wouldn't say DAOs are part of hexagonal architecture although I'm sure many people combine them and there's nothing wrong with what you wrote.
Upvote 2 Downvote Reply Award Share
Report
Award
Share
bobaduk
•
2y ago
• Edited 2y ago
what should domain entities actually do?
What does your system do? One of the problems people have with this is that they can't wrap their minds around the idea of a domain model that solves a problem, instead of a data model that just represents a fact.
Whatever problem you have that your software solves, that's what the domain model does. If you don't have a problem to solve, if you're just storing data, then don't worry about it, but then why can't your users just use a spreadsheet?
In cosmic python we gave an example of a simple, real world, domain model that came up when we were selling furniture. https://www.cosmicpython.com/book/chapter_01_domain_model.html#_what_is_a_domain_model
We had lots of interesting domain models at MADE, and a lot at Cazoo, though in my current job, my problems are data centric, so I'm not applying those patterns.
Also, If they don't have an access to a database (and therefore don't break dependency direction), it can't even check if the ID is unique.
Why would that matter? "ID" is a database concept. What's your use case for a unique value? Your application services/use cases are responsible for orchestration. In most cases you can enforce a uniqueness constraint in the database, and handle the exceptional case of collision at that layer
Also, is my view of hexagonal architecture somewhat correct?
Close enough for you to grok. "Presentation layer" is the wrong term of art. I'd call those things adapters: they connect our application to the outside world by adapting it to different protocols.
The application services layer is generally responsible for syntax checking commands, if that's what you mean by DTOs. For example, if the incoming request has a negative user id, that's a syntax error. That's different to a semantic error, like trying to, I dunno, change the password of a deleted user. Those semantic cases are about the state of an entity, not the shape of incoming requests. Does that make sense?
Edit: domain models, btw, don't have to represent real world objects. They represent concepts, nouns, that describe our problem space. "Cancellation workflow" is a noun that doesn't correspond to a physical object. So is "purchase order amendment" , or "sensor failure prediction", but they might be useful in software, and have their own complex life cycles, even though they're not real world objects. Most good domain objects aren't physical things, they're state machines that describe a process m
Upvote 4 Downvote Reply Award Share
Report
Award
Share 
ipcock
OP
• 2y ago
Thanks for the answer!
While it did answer some of my questions, it did raise even more :)
Speaking of a "what should a domain model do" question, I think I've expressed my thoughts incorrectly. I understand that they should do the problem solving of a business. Now, for example, a domain entity named user has a method to create itself (I'm not sure if this is acceptable though) or to send an email. For the first one, the question is: in the use case interactor i've used User's method to create itself. And now I need to persist these changes anyway (it also shouldn't rely on repository, as it is in the outer layer), or in the second case, use a library to actually send an email.
I think the problem is that I don't really understand how domain layer interacts with anything outside of it when it's being called in the application layer. Does it store some data and then calculate something based on it, then returns result to the controller? Does jt mutate itself according to business rules and give infinite about the changes to save it using database?
p.s. Also, speaking of good domain entities usually being not a representation of some physical object, but rather a concept of some sort which helps solving a business problem. I think I get what you mean, however a lot of examples use the opposite :(
Upvote 3 Downvote Reply Award Share
Report
Award
Share
More replies 
[deleted]
•
2y ago
• Edited 8mo ago
coherent live friendly attempt sugar attraction sable frame chop afterthought
This post was mass deleted and anonymized with Redact
Upvote 2 Downvote Reply Award Share
Report
Award
Share 
Drevicar
•
2y ago
• Edited 2y ago
What you described is closer to clean architecture, which is complicated to learn and too complicated to use on most projects.
Hexagonal architecture on the other hand scales down really well and I like to use it even on small hobby projects.
For any given language, you should have the ability to create, build, and publish packages or modules. While you don't always have to do this literally, pretend like you are for the sake of this example.
I am creating an application that allows me to control IOT lightbulbs. My business logic loves in its own package and has aggressive unit testing and the success of my business relies on this being correct. This package has no concept of auth-n or auth-z, just pure business logic and nothing else. The problem with this module is that to keep it pure it can't interact with the outside world, which means it can't call external things like the filesystem, the current time, random numbers, network sockets, http, or databases. Nor can it be talked to by any of those things. This by definition means my code is not only perfect, but perfectly useless. We can solve this in two halves. I can make everything I've done so far private and add a public interface for how to use my code in a domain specific way and only in the correct way. This is where the use case or services comes in. Instead of a collection of functions that could be called in the wrong order, it forces you to use a well defined interface when interacting with this module from the outside world. This is the port on the left side of the hex. The next issue is now that my code can be driven, it can't itself talk to the outside world, which means I can now be told to turn on a lightbulb, but I can't go turn it on. To solve this we create an abstract interface for "something" for us to drive to interact with the outside world. This can fall into one of several patterns such as RPC, pub / sub, request / response, or whatever abstraction you feel like you need here. Because it is in the core package I only create the interface, not the implementation of it. The left port we just created assumes the concrete implementation of this interface will be passed in at runtime. This is your right port.
Whew! With all that out of the way let's create some adapters.
Our lightbulb service likely needs a few right adapters. We likely need some RPC mechanism to interact with the lightbulbs, or the controller device that interacts with the light bulbs. We also need a database to store state such as the desired state of each lightbulb be that on or off, brightness, or color. Maybe even a listing of which capabilities each bulb has and where it is located in the building. If we want to send notification we need another service. A couple examples of a concrete implementation of a notification service can be email or SNS. Which we use if determined at runtime, but the core package would define whether a service needs a notification adapter. For storing state I could use a postgres adapter, a redis adapter, mongo adapter, or just an in memory data structure adapter. All these adapters conform to the interface exposed by the core package. Doesn't matter if the concrete implementation is using raw SQL, a query builder, an ORM, or a third party service that gives us SQL as a service with a custom library. These are all choices made at runtime. You can create integration tests here such that the in memory adapter is tested with a whole bunch of tests and proven to work. You then repeat all the tests again for each adapter that matches that in memory mock to prove it got the same result. And we aren't just testing methods and such, this is a living stateful system. So you want some huge complex test that proves after hundreds or even millions of state modifications that every adapter gets the same results as the in memory mock which was heavily unit tested.
Now we can work on the left adapters. I know for a fact we need at least 2 of them. I want to expose this application to the world using a web application, so I need a web server left adapter. But I also want to do integration tests here so I'll create a mock left adapter that is my new primary end to end test suite. When you combine multiple core services or use cases along with all their left and right adapters into a single bundle of code, this is now called an application. For testing purposes I want my test case left adapter along with all my core services and all their mock right adapters that only use in memory data structures. This is the single largest unit of code we can unit test, and so we do so heavily, everything after this will be integration tests where we compare the results to this. For the web left adapter we need to create an application that takes in all the core services and all the right adapters to use and stitches them into some web framework stuff that calls into the core services. We can still test this using browser automation, but now we are including a real network, a real browser, and a real database in our tests. Meaning this is both more expensive and slower to run, but might provide much more confidence in the correctness of our application.
I mentioned earlier you almost never want auth-n and auth-z in your core package. Instead it would be implemented as a left or right adapter depending on where it needs to happen. Maybe it is standalone, maybe it is baked into the web left adapter as JWTs or into the SQL right adapter as part of your queries. Maybe it is some middleware you wrap these adapters with to do something else. Doesn't really matter too much.
So, now we have 2 applications. One for testing and one for production. Each application contains 1 left adapter each and 1 service that relies on 2 right adapters each. As your application grows you will likely have multiple bounded contexts. Meaning we are solving a giant complex network of problems that each can be solved in a smaller isolated package. Maybe we are building a hotel management system where the light manager is just one small service in it. This is where all these fancy architectures really start to shine. Because now I can compile my hotel manager by combining my light manager with my guest manager and my staff scheduling manager. If all of the various services each used a SQL based right adapter I could establish a single database connection and pass it to each adapter. If all 3 services are exposed as a web API I can instead create them as sub routes and now the combination of all 3 of them are the web app. Now I have a highly modular monolith, which is an very desirable thing. Or I can go the microservices route and deploy each core package as its own unique web service with its own deployed SQL server that they don't share anymore. I can test each service in isolation, or I can test all 3 in aggregation. In most real world cases you won't have a system that can be deployed as either a modular monolith or microservices, only one at a time. But if you follow those architecture practices you can switch from a modular monolith to microservices very quickly and cheaply without having to throw away too much code or change how things build and test.
Once you have adopted this pattern you can just keep adding more services, more left adapters, and more right adapters will keeping the complexity of your overall application closer to linear growth rather than exponential growth, but at the cost of increased effort upfront to build out the architecture and the effort put in to decouple code that may not have needed to be decoupled in the long run.
Upvote 3 Downvote Reply Award Share
Report
Award
Share 
Drevicar
•
2y ago
Note that in my examples I talk a lot about testing at different levels of abstraction. You may or may not actually benefit from that, and a single end to end browser based test with a real DB may be all you need. Make your own choices, but make sure to leave yourself room to make future choices as you learn more about the problems you are solving.
Upvote 2 Downvote Reply Award Share
Report
Award
Share 
ipcock
OP
• 2y ago
Wow, that sure was a long read haha, thanks for the answer!
I think I've got most of it. Now I understand that the biggest problem I have is with this RPC thing. I need a way for my domain entities to tell the outside world that they demand a change based on their calculations, but I'm not sure about what should I do to implement this mechanism
Upvote 0 Downvote Reply Award Share
Report
Award
Share
More replies 
flavius-as
•
2y ago
• Edited 2y ago
Use Cases are inside the domain model, but at the edge.
Through the use case you interact with the domain model.
It's like a controller from MVC, except its purpose is to document the business logic at a high level, and to make the model testable.
The use case also depends on nothing outside of the model.
Regarding uniqueness: that's not the model's job. The model is not concerned with anything technical. No DB, nothing.
The uniqueness is a job for the storage adapter.
Regarding validation: there are various levels of validations. The syntactic simple ones are done in the domain model's classes constructors. There you throw an exception, thus enforcing class invariants.
Other semantic validations can only be done when a method of the model is called, the point at which you have all data and where you can check that the puzzle pieces fit together.
The model has access to the database, but it doesn't know it's a database.
From the model's perspective, the data comes from a pure fabrication (see GRASP) that the model itself specifies.
A common pattern for this is the repository pattern.
You make a ProductRepository interface inside the model, which you implement in the storage adapter and inject into the model (dependency inversion).
Upvote 3 Downvote Reply Award Share
Report
Award
Share
shenku
•
2y ago
Let's clear that up.
Domain entities encapsulate the rules and business processes of your domain.
Repositories load the data into the entity (or save the entity data to the db)
And the services/application layer orchestrates the whole thing.
In other words, the request comes through your controller to the service, the service uses the repository to load the entity, and the service invokes the appropriate business logic on the entity.
Example: a customer wants to withdraw money from their bank account.
The request comes in to the account controller, the account controller calls the account service, the service uses the account repository to load the correct account from the db: 'accountRepo.getAccountForCustomer(customerID)'
now we have the account we can do: 'customerAccount.withdraw(amount)'
The withdraw function has some rules in it:
it checks the amount is a positive value
it checks the current account balance is greater than the amount requested
if it is it subtracts the withdrawal amount from the balance
if it's not it throws and error indicating you can't exceed your balance
Of course this is a simple example. it can be as complex as it needs to be and use as much data as is needed usually from the entity but you can pass in through the function call as well.
Then the service that called the '.withdraw' function will again call the accountRepo to save the entity with the new balance: accountRepo.save(customeraccount).
Effectively no 'business logic' should live in your services. They only orchestrate the use case by loading and invoking the functions on your domain entities.
Upvote 3 Downvote Reply Award Share
Report
Award
Share 
addys
•
2y ago
u/gnu_morning_wood explained it well, so I'll just add a few minor nuances to what they said:
Even (especially) before MFC, the common architecture model was 3-tiered- "Data layer" then "business layer" then "presentation layer". In practical terms, the "data layer" usually included a ton of business logic in the form of SQL stored procedures. And also, the "presentation layer" usually also quite a bit of business logic as related to formatting, validation etc. So the business layer was typically fairly hollow since it's responsibilities were scattered all over.
Data integrity was usually considered a data layer concern and was enforced via database constraints and logic. But since data integrity is basically another way of saying "business rules", the end effect was that DBAs were often the gatekeepers for much of the key business logic.
hexagon architecture (I prefer the term "onion architecture") has two simple tenets:
A) the "domain" is at the center of the model and everything else wraps it.
B) dependencies flow outwards, meaning outer layers depend on the inner layers, inner layers do not depend on outer layers.
What is the "domain" in (A)? One possible answer is the definition given by DDD. But that's not the only answer. I would define the domain as your "special sauce", ie the way you solve/approach the business problem which justifies the existence of your company/service, which in turn is the thing you are attempting to codify into a running software system.
You should be able to write a pure C#/Java/Python/whatever application, running single-threaded in a single process, which contains the entirety of your business concepts and behaviors. Ignore anything which isn't related to the core business challenges (ie use an in-memory collection instead of a database). Obviously this isn't what you are going to eventually ship to production, but it's a good starting exercise. If you can't do it, then you aren't ready to continue to the next steps. So at this point you have solved all the known business complexities, running in a console app or unit test, etc.
Once you can do that, then what's left is extending your domain code into an actual software system- scale, reliability, concurrency, UX, security, privacy etc. The idea is to wrap additional layers around your business logic. For example, swap out the in-memory collection with a database. ORM layers are meant to do exactly that- present persistence capabilities with the same interface and behavior as in-memory lists. Replace in-memory calls with messaging features (queues, pub/sub etc).
So to summarize, the responsibility of the outer wrapper layers is to serve the core, which is the business logic. This approach has quite a few drawbacks, but also significant advantages, especially in complex business domains where getting the "business" right is the primary success condition.
Upvote 1 Downvote Reply Award Share
Report
Award
Share 
linjusDev
•
2y ago
Hexadiagonal Architecture is basically, service container pattern and injects services based on context and app configurations limited by type hinted interface. Somewhere in application lifecycle, usually using Service Providers or application configuration, you register services and tag them to either specific interfaces or keywords, if its not an empty interface service must adhere to its required methods and expected parameters and returned value if defined, otherwise it is just a tag to build a collection upon. And what you get depends on conditions you either set for specific class that uses that service or how specific service for given tag is selected based on context. But usually at the end of the day it ends up getting hundreds if not thousands of services that are almost carbon copy replicas, but have few lines changed, because context have no conditions to make it reusable. :D
Upvote 1 Downvote Reply Award Share
Report
Award
Share
New to Reddit?
Create your account and connect with a world of communities.
Continue with Email
Continue with Phone Number
By continuing, you agree to our User Agreement and acknowledge that you understand the Privacy Policy.
Related Answers Section
Related Answers
Hexagonal architecture best practices
Hexagonal architecture vs clean architecture
Ports and adapters architecture explained
Onion architecture vs hexagonal architecture
Best practices for microservices architecture
More posts you may like
Noob question: How to enable code navigation for Nuxt.js project? r/vuejs • 2y ago [
Noob question: How to enable code navigation for Nuxt.js project?
](https://www.reddit.com/r/vuejs/comments/1b52xu1/noob_question_how_to_enable_code_navigation_for/) 2 upvotes · 3 comments
Understanding role of React Query in my basic project r/reactjs • 2y ago [
Understanding role of React Query in my basic project
](https://www.reddit.com/r/reactjs/comments/1bph2ym/understanding_role_of_react_query_in_my_basic/) 13 upvotes · 8 comments
Is There a Standard for Hexagonal Architecture r/softwarearchitecture • 5mo ago [
Is There a Standard for Hexagonal Architecture
](https://www.reddit.com/r/softwarearchitecture/comments/1po2ofq/is_there_a_standard_for_hexagonal_architecture/) 30 upvotes · 18 comments
A well-structured layered architecture is already almost hexagonal. I'll prove it with code. r/softwarearchitecture • 2mo ago [
A well-structured layered architecture is already almost hexagonal. I'll prove it with code.
](https://www.reddit.com/r/softwarearchitecture/comments/1rr1r80/a_wellstructured_layered_architecture_is_already/)  34 upvotes · 38 comments
Hexagonal vs. Clean Architecture: Same Thing Different Name? r/softwarearchitecture • 1y ago [
Hexagonal vs. Clean Architecture: Same Thing Different Name?
](https://www.reddit.com/r/softwarearchitecture/comments/1l7u2wx/hexagonal_vs_clean_architecture_same_thing/) 44 upvotes · 40 comments
I finally understood Hexagonal Architecture after mapping it to working code r/softwarearchitecture • 5mo ago [
I finally understood Hexagonal Architecture after mapping it to working code
](https://www.reddit.com/r/softwarearchitecture/comments/1pb9zge/i_finally_understood_hexagonal_architecture_after/)  56 upvotes · 53 comments
Hexagonal Architecture - Ports r/softwarearchitecture • 22d ago [
Hexagonal Architecture - Ports
](https://www.reddit.com/r/softwarearchitecture/comments/1spess7/hexagonal_architecture_ports/) 37 upvotes · 14 comments
Hexagonal vs Clean vs Onion Architecture — Which Is Truly the Most Solid? r/softwarearchitecture • 6mo ago [
Hexagonal vs Clean vs Onion Architecture — Which Is Truly the Most Solid?
](https://www.reddit.com/r/softwarearchitecture/comments/1otdz3g/hexagonal_vs_clean_vs_onion_architecture_which_is/)  155 upvotes · 77 comments
where to define dto in hexagonal architecture r/softwarearchitecture • 2mo ago [
where to define dto in hexagonal architecture
](https://www.reddit.com/r/softwarearchitecture/comments/1s2wmpd/where_to_define_dto_in_hexagonal_architecture/) 22 upvotes · 20 comments
Layered Architecture != Hexagonale, Onion and Clean Architecture r/softwarearchitecture • 5mo ago [
Layered Architecture != Hexagonale, Onion and Clean Architecture
](https://www.reddit.com/r/softwarearchitecture/comments/1paq2d7/layered_architecture_hexagonale_onion_and_clean/) 43 upvotes · 19 comments
[Question] How to run gauge R&R with small subsets-rl problem NOT class r/statistics • 2y ago [
[Question] How to run gauge R&R with small subsets-rl problem NOT class
](https://www.reddit.com/r/statistics/comments/1bhpnca/question_how_to_run_gauge_rr_with_small_subsetsrl/) 3 upvotes · 6 comments
Modularity vs Hexagonal Architecute r/softwarearchitecture • 6mo ago [
Modularity vs Hexagonal Architecute
](https://www.reddit.com/r/softwarearchitecture/comments/1okdefo/modularity_vs_hexagonal_architecute/) 32 upvotes · 17 comments
How doe modules interact each other in Hexagonal Architecture? r/softwarearchitecture • 7mo ago [
How doe modules interact each other in Hexagonal Architecture?
](https://www.reddit.com/r/softwarearchitecture/comments/1o8vqzr/how_doe_modules_interact_each_other_in_hexagonal/) 24 upvotes · 24 comments
Advice needed for transitioning from software engineer to architecture r/softwarearchitecture • 1mo ago [
Advice needed for transitioning from software engineer to architecture
](https://www.reddit.com/r/softwarearchitecture/comments/1seoxmv/advice_needed_for_transitioning_from_software/) 52 upvotes · 24 comments
AI + human readable architecture diagrams? r/softwarearchitecture • 3mo ago [
AI + human readable architecture diagrams?
](https://www.reddit.com/r/softwarearchitecture/comments/1rdb1c1/ai_human_readable_architecture_diagrams/) 13 upvotes · 30 comments
How to Make Architecture Decisions: RFCs, ADRs, and Getting Everyone Aligned r/softwarearchitecture • 3mo ago [
How to Make Architecture Decisions: RFCs, ADRs, and Getting Everyone Aligned
](https://www.reddit.com/r/softwarearchitecture/comments/1r22ddq/how_to_make_architecture_decisions_rfcs_adrs_and/) 88 upvotes · 6 comments
Need advice on solutions architect path r/softwarearchitecture • 2mo ago [
Need advice on solutions architect path
](https://www.reddit.com/r/softwarearchitecture/comments/1rzmxi4/need_advice_on_solutions_architect_path/) 6 upvotes · 16 comments
Anyone actually keep initial architecture docs up to date and not abandoned after few months? Ours always rot r/softwarearchitecture • 4mo ago [
Anyone actually keep initial architecture docs up to date and not abandoned after few months? Ours always rot
](https://www.reddit.com/r/softwarearchitecture/comments/1qa83h4/anyone_actually_keep_initial_architecture_docs_up/) 40 upvotes · 32 comments
A Better (Beyond CRUD) Architecture r/softwarearchitecture • 25d ago [
A Better (Beyond CRUD) Architecture
](https://www.reddit.com/r/softwarearchitecture/comments/1smdhsj/a_better_beyond_crud_architecture/)  233 upvotes · 65 comments
Architectural Question about Serilog and Microsoft Logging r/dotnet • 2y ago [
Architectural Question about Serilog and Microsoft Logging
](https://www.reddit.com/r/dotnet/comments/1bg92ti/architectural_question_about_serilog_and/) 37 upvotes · 15 comments
How do you become a software architect without already having broad experience? r/softwarearchitecture • 16d ago [
How do you become a software architect without already having broad experience?
](https://www.reddit.com/r/softwarearchitecture/comments/1sv30ag/how_do_you_become_a_software_architect_without/) 70 upvotes · 70 comments
What types of software still feel brutally hard to build and even impossible to build well? r/softwarearchitecture • 1mo ago [
What types of software still feel brutally hard to build and even impossible to build well?
](https://www.reddit.com/r/softwarearchitecture/comments/1shg00x/what_types_of_software_still_feel_brutally_hard/) 155 upvotes · 109 comments
How to setup Architecture Governance | Learnings and Practices r/softwarearchitecture • 4mo ago [
How to setup Architecture Governance | Learnings and Practices
](https://www.reddit.com/r/softwarearchitecture/comments/1qbkxof/how_to_setup_architecture_governance_learnings/) 30 upvotes · 10 comments
How do you enforce architecture governance? r/softwarearchitecture • 1mo ago [
How do you enforce architecture governance?
](https://www.reddit.com/r/softwarearchitecture/comments/1siwx5l/how_do_you_enforce_architecture_governance/) 23 upvotes · 24 comments
Event-first architecture r/softwarearchitecture • 23d ago [
Event-first architecture
](https://www.reddit.com/r/softwarearchitecture/comments/1snypjo/eventfirst_architecture/) 57 upvotes · 49 comments
View Post in
Русский
简体中文
Português (Brasil)
繁體中文
Tiếng Việt
Français
See more See fewer
Čeština
Español (Latinoamérica)
Polski
Bahasa Melayu
Community Info Section
r/softwarearchitecture  
The Incident, a CTF-style Production Outage contest, is starting soon! Cash prize is $100. See highlighted post for more details!
Join
Software Architecture
Dive into discussions on designing, structuring, and optimizing software systems. Share insights on architectural patterns, best practices, and real-world experiences.
Show more
Public
Anyone can view, post, and comment to this community
Top Posts
Reddit reReddit: Top posts of March 30, 2024
Reddit reReddit: Top posts of March 2024
Reddit reReddit: Top posts of 2024
Reddit Rules Privacy Policy User Agreement Your Privacy Choices Accessibility Reddit, Inc. © 2026. All rights reserved.
Expand Navigation
Expand Navigation
Collapse Navigation
Collapse Navigation 
0cAFcWeA7MDOZ66WyrqgfIww79oDfycTFrhYl4ZFfgkNB7eUmAfDt09UeaVxFZ3FoqoDlne-gvB0h_J_QgEfpgB8dp_ymlHeDHssKFbDETJZTAizfK_gP0x8HIC02oSYWRmgcBUaJjl6qfq7cbMecMWcBLpfpsIvnOV4hwf3hAk2XdHJaNRIH_g569K8kRkNaesFoVN3qpUXvp949DPC6BGdO9oxtMne_SWXwGel632SohAeRi8vxHjubUQOoV5BMXvQGSgAV02Hvhe970JyjhfI4cG2_JnpcHR6VN9-3pRL7hrcnrRugdjc0FzHyDylW2TzqZoRtNADe4VTEgF-3l7UXqIIwmEi5GNMFaI1G58IvALtZevbL_uOIj9DLAWe39N_MlargOgNyfF0Ps-8nkkwF_mQwtUk8jykMX6tTT8bl_GuRjsVwj_6_I0XLDZmHMtpuKGWgOSxqyL8fW5Y1231t_vQRgVCM0ZqMTrLVRkglt-oxIvtWcKDzrO8UBeztRbw6L22TWBM1OEg59Wol_5fI5a2I-xv8ry4VQM_NwHgUoSGOou8WZyPOl1qiGX_vj2qe3x-JY6u2dRl5upim-RkpVlIm9PvqlmPpVpgWmD7lblEim9SiyBpdHrhCb_22QoMcFQZGNymUMCF6CWZGtiY-PjrClKU2f-Q5GX4VtR9ObjYujxDRPxVXIKpYl9TdNBidJKcRh6S_ke5cKeAN5GfeXN3d2YyCNJWVIzcJEJM4nCysWewCy6GGC_TbnwzZgFS90eRlMbOA6ftXAtH99hMQzF4jD0DbCJSpuPTuaospXuJgF9yzyJURB3RHlv0ORDfk6Fs0GunejPhk6cklicd-DAuAUbt1ut6BK7yasKbip3Y3JK5DeFvnDUbi63IhqW3K9JoMjgN-wCWOGt65P9dZ_xi7OTA5OK275BXgfPyMJ25Nq1n8L8mCzRnb8iTs4o7dGpdgaKsz_yj-04bitTCrFg6aoZ573QDvxiAreRn8Wd_j1AOGUULKLEgVI5E-weB3p9Ao2wmokGyoVnxtZEL6jaCZXIvPIp4WIya23Zzpd7_J0gJCnQs3rXjdgGb8hDgEcw_kD6xMdi7WHQ2sBnE5KnuxjVW8uiN2OO50G8euvFRyGBvn0PrXZ7ujZNIToxzu3kKasG_LK_9u6exNqv1_3SiVZg7uW-JCK1DoarhHRc4c50rT9GoEs82gqlbWy6QpRVWVSf-VTqsi3zYlO3zmeuPNnz3Y7m4WGx83tcSBbLcmN_NNCS5U9q73T5yEVcOgur9rVnrshd4uXa73P04TSLMk9pnGQtqAPTHtHaItu22pja-Ep4fAKR5dVJ7DLbXe7TljqEH95WJDS8XOpo-2-3rZ5wLUBHoXeZQivXIISnY4V0dnHTFXb6r57L6SeMG1idxVb6YmQKc2pKSUnyPb812yFGngOspr7tK81sdHRNPCVTyD1lKM_5MgVgq0Ce6smGx3yA1MgRTAOl99GTIt8SMAUdovs8DgsIKh6oBY-b8kGIRD0h4Ytz1plDgP5FGPl22cBX3_n1HGOxr0nV3LG02ijMHFqwGFraUGkTu94smzbScuzHXIGkEnJrL8JtW-5ptf11zXW2UBPpHEGsb6QcT6NqKSH7tQ0RjCVPdBaStMlrsVdso2PrR320M4B64ELlFUXCT49fWNCdSe7Q2fi1uZ4A9FDwPE_dhTDy6i4AW3_xPRy2c1TOm3m2ks-EnpZ0ul3CKuEGOIzH9HiLldxjIR3f0pa3Aw7KvyebGfP71FGEKGz9yNipmlCc3P6QL6j39zmkMbqhp_q0THAbrVn_-nvUgU6Aqy-sPWlmIxDbz57ODBzBlBsmhY8QbrnlhxSufLBK7T1YZjvR3yvNeLpSHAfb2y3UGXQ7JaXrmWqv0xiNSEzBWhlUObIONh9UAQGSFw3xDN6FW8dus-MkjGJb_L84J-9TpYaCucgPhQefWaGU2Xrc7YGq3KPtYpXs8J-v7nJPzsd6odLo1zfMe5l-G6qJ-LbT3ppuFloFGjfwLSCP10NyMhJyvW4GjDCPbeDpdapp7jjnBAPMzqO77UmjYO7oxehR-E6DIRe6JE1rMbF2bDrVd05VDeI7clTgIyuM2475i2W5kfiQSv_ixsRXCm3grL__58_ULxrCWjuIsojyZ5mC3EbuojuQ3bGMaOB6gIB3sUX
