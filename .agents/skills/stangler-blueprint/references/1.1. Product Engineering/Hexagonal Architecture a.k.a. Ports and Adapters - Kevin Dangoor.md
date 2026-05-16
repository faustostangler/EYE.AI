---
name: Hexagonal Architecture a.k.a. Ports and Adapters - Kevin Dangoor
keywords: (placeholder)
metadata:
  url: https://www.kevindangoor.com/posts/hexagonalarchitecture
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Hexagonal Architecture a.k.a. Ports and Adapters
Kevin Dangoor
Search
Recent Writing
Ranked Choice Voting
May 05, 2026
2026-19
May 04, 2026
2026-18
Apr 29, 2026
2026-16
Apr 19, 2026
See 355 more →
Home
❯
posts
❯
Hexagonal Architecture a.k.a. Ports and Adapters
Hexagonal Architecture a.k.a. Ports and Adapters
Dec 29, 2018 10 min read
Architecture
Gary Bernhardt's Boundaries talk is one of my favorites. In it, he talks about a “functional core” of pure, easily-testable code, surrounded by an “imperative shell” which deals with the messy world outside.
It can be delightful to write code in this way:
Part of the time, you're focused on the real problem you set out to solve
The other part of the time, you're dealing with the technology mess required to make it work
Haskell's IO Monad or the Effect Python library provide systematic ways to get this kind of architecture. Your pure code can describe its messy side effects, which will get executed elsewhere.
The Ports and Adapters Architecture
Alistair Cockburn described the “Hexagonal Architecture” back in 2005, later deciding that Ports and Adapters was a better name.
Alistair Cockburn's website isn't responding for me as I write this (October 2018), so I won't link to his original explanations. The C2 wiki has the link. I'll summarize the key bits of the architecture:
Within a “hexagon”, all of the code I write is pure business logic.
It knows nothing about the technology used to work with the outside world.
Any time the code in the hexagon needs to deal with outside concerns, it uses a port
Interfaces to the user and database are obvious examples
But, there can be other systems as well, depending on the application
Adapters sit at each port, converting between the real “outside world” API and the API defined at the port
I could draw a diagram like the many other hexagonal diagrams you can find out there, but there's no point. It's the ports and adapters that are important, not the hexagon.
Isn't that extra abstraction a bunch of work?
As with anything, Hexagonal Architecture doesn't apply to everything. Creating ports and adapters is extra overhead. If I've got a long-lasting system that needs to change over time, and especially if I have a need for multiple implementations to attach to those ports, this architecture could be a good fit.
What if there is only one implementation? If I want to be able to write simple, fast-running tests for my business logic, each of the ports will likely have two adapters:
A test adapter
The real adapter
One nice thing about this architecture is that my tests don't need to put mocks in all over the place. I only need to provide adapters that take the place of the real implementations.
Aside: are you really going to change adapters at some point?
When I started at Khan Academy, we had a substantial REST API. Over the past year or so, we've been making a move toward GraphQL. I have no doubt that the ports would have required some changes to deal with this move, but I also think that certain aspects of the move would have been cleaner.
Additionally, we've been using Google App Engine's Data Store since the beginning. We were recently talking about whether a relational database would be a better fit for some of our data, and we'd be able to more easily test that out if we could simply write another adapter. Again, the port would probably need to change a bit, but there would be less change.
There are many more options for storage of data today than there were 10-15 years ago, so I can see having ports and adapters on the data storage side useful for things other than testing. Again, this applies to systems that are intended to last and change over time.
Lasting and changing over time vs. throw it away
This is actually a better question than will adapters change at some point: is it better to have adapters that you change out for new technology, or to have small, well-defined subsystems that you can throw away and rebuild as needs dictate. My intuition is that the testing benefits of ports and adapters will make them worthwhile, but I do think the right answer is going to depend a lot on the kind of change that is occurring.
I will say this: Khan Academy has a lot of code that has lived longer than folks would probably have expected. I wish that code was as easy to work with as a well-bounded hexagon.
Hexagons and DDD
There seems to be a nice connection between Domain Driven Design and hexagonal architecture. The idea with DDD is to create bounded contexts which are responsible for a certain business domain. Those bounded contexts need to have their connections to other bounded contexts clearly defined. DDD also has the notion of an “anti-corruption layer”, which is responsible for ensuring that the code and terminology used within a single bounded context stays consistent.
Bounded contexts map nicely to the hexagons, and adapters serve the function of the anti-corruption layer.
“Functional core” (from Boundaries), IO monad, Effects, DDD, and hexagonal architecture all share similarities because many systems have the problems that these techniques try to solve.
Hexagonal architecture in Python
Ports and Adapters with Command Handler pattern in Python
Bob Gregory wrote Ports and Adapter with Command Handler pattern in Python . One thing I appreciate about this article is how he brought DDD and domain language into the example. I do think the ubiqitous language is a useful idea from DDD.
He started with these three principles:
We will always define where our use-cases begin and end. We won't have business processes that are strewn all over the codebase.
We will depend on abstractions, and not on concrete implementations.
We will treat glue code as distinct from business logic, and put it in an appropriate place.
Rather than “ports and adapters”, he expressed his architecture with a layer of “services” around the domain. Those services interact with the ports, in line with principle #3.
In part 2 , he introduces the Repository and Unit of Work patterns, which are ways to consistently manage data independently of how it's stored.
He creates Unit of Work Manager, which is a port that handles management of a database transaction. His command handler objects are then responsible for running the use case (as desired in principle #1 above), starting a transaction, gathering the data, calling into the hexagon, and committing the transaction at the end. I appreciate that he calls this glue code “painfully boring”, because I've always felt that you want that difficult-to-test code to be super obvious to read and understand.
The ORM code depends on the domain model, not the other way around. In other words, the adapter knows how to interpret the domain data, but the domain data knows nothing about the adapter's (ORM) working, which is what the hexagonal architecture dictates.
Part 3 starts with a discussion of Command Query Separation , which apparently goes back to Bertrand Meyer in the late eighties and seems remarkably similar to Command Query Responsibility Segregation (CQRS) which is much more recent. I think this point is key:
if commands and queries are clearly distinguished, then I can read through a code base and understand all the ways in which state can change.
He continues to make a good point about the value of using an ORM for your commands (writes), but just using straight SQL for your reads. Your writes need to deal with all sorts of business rules, but your reads are mostly about getting the data to the user as quickly as possible.
His approach to IDs is interesting and one I've seen elsewhere: IDs for new entities can be assigned anywhere (potentially even at the client). He does mention that you should still use integer primary keys in the database, for the sake of the database. In his example, his Flask route handler assigned a UUID and passed it in to the command handler. That way, his endpoint could return the ID without his command returning anything (as dictated by CQS).
Part 4 gets into domain events, using an example of an action that is taken and then, as a side effect, an email notification is sent. Bob points out that the “and” is a good sign that this command is violating single responsibility principle. So, he splits the action and the email into separate handlers, and then uses events as the way to invoke the email handler.
He put the raising of the event into the domain model, because sometimes, as in his example, the event doesn't need to be raised. One thing that felt a bit off in this example was his use of self.events.add on the business object. I'll see where this goes, but it seems like the message bus should really be another port.
Next, he flushes the events via the Unit of Work, which is indeed an established port. events is just a list on the model objects and is defined simply, with no magic , so I'm fine with where this stands.
The final (as of October 2018) part of the series covers dependency injection . Dependency injection (DI) is actually quite straightforward, as the first part of the article states. It doesn't require fancy frameworks or code.
I have been a Python user since 1995, but have spent more time with JavaScript in the past decade. Thus, I haven't been following much of Python 3.x's evolution or current solutions for DI. Bob introduces the inject library. He's not a fan of the use of decorators there, but it seems okay to me.
He has a DI framework built on Python 3.6 typehints. I agree that this is nicer than decorators, but decorators at least work with Python 2.
His section on Nested Services explains more about why he likes his DI implementation. Pretty cool stuff.
Abstracting databases
Some of my Khan Academy colleagues had feedback about a hexagonal architecture experiment. At Khan Academy, we're storing our data in Google Cloud Datastore, and I wanted to see if a hexagonal architecture would help make moving some code to a relational database easier. Datastore is not a relational database, and has different performance characteristics and ways to work with it. We could try to hide those differences behind the repository pattern, but it seems as though we'd end up with a lowest common denominator of both when the reality is that our application has enough traffic that we really need to write code that uses the technology available to it (the strengths of either the Datastore or a relational database).
With two repository implementations needing to be “production grade” and also needing to hide very different implementations, this pattern just doesn't seem like a good fit.
Conclusions
While I like the overall approach in Bob's series and think that hexagonal architecture can be a win in some circumstances, I do think, as with anything, it makes sense to use architecture to solve specific problems. If the problems you're trying to solve need this level of indirection and are not harmed by it, then go for it.
I am left with one additional question: if a command fails, but is not allowed to return any values, how does the user know that their operation failed? If commands are invoked via the message bus, would exceptions even get through to the adapter that is interfacing with the user? I'm curious to know what Bob thinks of this and have filed an issue asking this very question .
Clean Architecture
This pattern also goes by a variety of different names:
Clean Architecture — Bob Martin
Onion Architecture — Jeffrey Palermo
Bob Martin also lists DCE and a couple of others, but DCE seemed a bit different to me.
I like Bob Martin's description of this architecture. It's succinct and the rules are clear. It's not as concrete as Bob Gregory's example, but it's clearly expressing the same idea.
Changelog
2018/12/29: Update to include notes about different repository implementations.
Recent Writing
Ranked Choice Voting
May 05, 2026
2026-19
May 04, 2026
2026-18
Apr 29, 2026
2026-16
Apr 19, 2026
See 355 more →
Graph View
Table of Contents
The Ports and Adapters Architecture
Isn't that extra abstraction a bunch of work?
Aside: are you really going to change adapters at some point?
Lasting and changing over time vs. throw it away
Hexagons and DDD
Hexagonal architecture in Python
Ports and Adapters with Command Handler pattern in Python
Abstracting databases
Conclusions
Clean Architecture
Changelog
Created with Quartz v4.5.2 © 2026
GitHub
BlueSky
Twitter
LinkedIn
