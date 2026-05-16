---
name: 2026-05-10 Self-documenting Architecture. One of the biggest time costs in… | by Nick Tune | Nick Tune’s weird ideas | Medium
keywords: (placeholder)
metadata:
  url: None
  source: SOURCE_TYPE_TEXT
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
WebSync metadata
title: Self-documenting Architecture. One of the biggest time costs in… | by Nick Tune | Nick Tune’s weird ideas | Medium
url: https://medium.com/nick-tune-tech-strategy-blog/self-documenting-architecture-80c8c2429cb8
date: 2026-05-10T21:11:45.267Z
parsing method: defuddle
Sitemap
Nick Tune’s weird ideas
Domain-Driven Design, Organization Design, Continuous Delivery
One of the biggest time costs in software development is understanding how a system works. And the problem may be growing. Systems are getting more complex yet our ability to understand them doesn’t seem to be growing at the same rate.
As we continuously develop software systems, the complexity slowly increases and we don’t fully realise it. Nobody sets out to create a Big Ball of Mud, but many codebases end up that way due to the cumulative effect of the thousands of small changes we make.
Complex systems are harder to learn and harder for newcomers to be productive in. I’ve heard the opinion from many technical leaders that it is reasonable to expect a new hire to take upto 6 months to learn about the code, the domain, and the architecture before they become fully productive.
I believe that self-documenting architecture would dramatically reduce one of the big costs in software development. Everybody talks about self-documenting code, but that only applies in the small. Why not self-documenting architecture?
A codebase is more than text files. It is a database of domain, business, and architectural information. We should be able to click a few buttons and get 100% accurate visualisations of the domain model, business processes, and architecture.
A self-documenting architecture would reduce the learning curve. It would accentuate poor design choices and help us to make better ones. It would help us to see the complexity we are adding to the big picture as we make changes in the small and help us to keep complexity lower. And it would save us from messy whiteboard diagrams that explain how one person incorrectly thinks the system works.
Accelerating the Learning Curve
Self-documenting code helps us to quickly learn what a method does, or a few classes. But self-documenting code alone doesn’t accentuate the big picture; architecture, domain, and business processes.
The benefits of self-documenting architecture apply well beyond the scope of just onboarding newcomers. With a reduced learning curve everybody can have a larger understanding of the system and make broader contribution.
One of the reasons we have long-lived teams is due to the costs of learning a new codebase and domain. If those costs are reduced, our whole approach to organising teams could change, enabling greater organisational fluidity
Improving System Design
As software systems gradually evolve on a continual basis, individual decisions may appear to make sense in isolation, but from a big picture architectural perspective those changes may add unnecessary complexity to the system.
With a self-documenting architecture, everybody who makes changes to the system can easily zoom out to the bigger picture and consider the wider implications of their changes.
One of the reasons I use the Bounded Context Canvas is because it visualises all of the key design decisions for an individual service. Problems with inconsistent naming, poorly-defined boundaries, or highly-coupled public interfaces jump out at you. When these decisions are made in isolation they seem OK, it is only when considered in the bigger picture that the overall design appears sub-optimal.
The Bounded Context Canvas
Unfortunately, populating the canvas is a manual process. It is my belief that we should get the Bounded Context Canvas for free. The information is in our systems so it should be easy to extract. As part of our development process, we could then review each small change we make in the context of the bigger picture.
Living Documentation
The concept of self-documenting architecture is in the space that Cyrille Martraire calls living documentation. As the system evolves, the documentation evolves with it, it is alive.
In the book, Cyrille outlines a number of ways that documentation can play a greater role in improving our ability to understand systems. Not just their current state, but the rationale for decisions and additional domain information that cannot easily be expressed in code.
As you read through the book you start to see what the future of software development looks like. It’s going to be less about programmers taking requirements and squeezing them into a messy codebase, and more of an information-rich experience where software developers will understand the business context the system operates in and the history of changes to the system.
I hope that this book inspires a generation of developers and architects to solve the genuinely hard and worthwhile problems in software development.
New Primitives
One of the challenges I noticed with Cyrille’s book is that the building blocks aren’t quite there yet. Some of the domain and architectural information we care about is hard to extract from a codebase.
In Domain-Driven Design, domain concepts are represented using concepts like Domain Events, Entities, Aggregates, and Policies. But in most programming languages, all of these concepts are represented using classes.
How can we build tooling that can auto-visualise our domain model if all we have are classes to extract from the code? We can look at the names of those classes, or try to infer their behaviours. In Cyrille’s book he uses annotations or marker interfaces.
I have no objection to annotations and marker interfaces if they enable self-documenting architecture. However, it’s not the optimal developer experience and it can be error-prone. Discipline and rigour is required.
What if instead we all agreed on some architectural or domain model building block conventions? Maybe they will become native concepts in future programming languages. We will then get self-documenting architecture for free (because tools can easily extract domain concepts from a codebase).
I know there will be pushback to standards and it could be a number of years before we converge. However, the benefits are so great that it feels inevitable. As programming languages abstract away more accidental complexity, I can see a space opening up for them to include higher level domain primitives.
Existing Tooling
What about the tools out there at the moment in the self-documenting architecture space? What should we be getting excited about?
Structurizr by Simon Brown is one of the tools I watch with interest. Structurizr provides a language/DSL for describing architectural concepts using C4 nomenclature. In effect, it is similar to adding annotations or marker interfaces. It still requires effort from developers to identify concepts in code.
The future of Structurizr is what I find interesting. What if there is a way to bake Structurizr into frameworks and platforms so that we get self-documenting architecture for free? Spoiler: I already know of multiple efforts underway.
The other tool I’m paying special attention to is Contexture by Softwarepark. Contexture differs to Structurizr by focusing more on domain concepts and less on technical concepts.
One of the Contexture features is the Bounded Context Canvas. As with Structurizr, the current iteration still requires manual steps, but it’s not hard to envision future iterations of the tool which almost fully automate the process and extracting domain knowledge from a system.
I’ve also been impressed with OpenApi-Specification (formerly Swagger). The ability to view the public interface of a service is a great example of reducing the learning curve and making complexity visible.
The Future….
The future of software development will involve self-documenting architectures that are easier to learn, easier to evolve, and maybe will even partially design themselves. They will document their evolution over time, allowing us to gain long-term feedback on our design choices and better understand why decisions made. We might no longer have the problem of “everybody who worked on that part of the system has left”.
I can’t predict the timescale of these changes, but it is encouraging to see tools like Structurizr and Contexture, and the exceptional work of Cyrille Martraire.
Let me know your thoughts on this topic. Leave a comment or contact me directly.
Last published Mar 1, 2026
Domain-Driven Design, Organization Design, Continuous Delivery
Author of Architecture Modernization (Manning) and legacy-modernization.io. Find me on BlueSky: nick-tune.me and LinkedIn: /in/nick-tune
