---
name: Software Engineering Trade-Offs - Why We Cannot Build Perfect
keywords: (placeholder)
metadata:
  url: https://pasksoftware.com/software-engineering-trade-offs/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Software Engineering Trade-Offs - Why We Cannot Build Perfect
Skip to content
Pask Software
Designing Systems and Crafting Code
Menu
Blog
About
Newsletter
Limitless System Design – January
Limitless System Design – February
Limitless System Design – March
Limitless System Design – April
Limitless System Design – May
Limitless System Design – June
Series
Talks 
Software Engineering Trade-Offs
August 14, 2025 June 14, 2025 by Bartłomiej Żyliński
X LinkedIn Facebook Mastodon Copy Link Share
In a couple of my last articles, I emphasize the importance of different software engineering trade-offs, for example here. I have been trying to point out that focusing on maxing out just one trait can cause problems in others. I believe that main part of our job as software engineers should be to min-max different software engineering trade-offs and even the trade-offs of different combinations of trade-offs.
Table of Contents
Toggle
We Cannot Build Perfect
Software Engineering Trade-Offs
Complexity vs Everything
Simplicity vs Flexibility
Time-to-Market vs Technical Debt
Horizontal vs Vertical Scaling
Latency vs Throughput
Stateful vs Stateless
Sync (Blocking) vs Async (Non Blocking)
Coupling and Cohesion
Other
Navigating Software Engineering Trade-Offs
Evaluate the short-term and long-term impact of decisions
Identify key stakeholders, their needs and act accordingly.
Research — clarify goals and hard constraints
Document trade-offs, and their rationale (ADR)
Prototype or spike the extreme options to expose hidden pitfalls early.
Focus on simple solutions then optimize for the future.
Summary
Software engineering is an art of constantly balancing all these things. Below you can find eight trade-offs, plus their pros and cons. I will also share a very simple framework for navigating software engineering trade-offs.
First, a reality check: perfection is impossible — min-maxing is the way.
We Cannot Build Perfect
In the perfect case we could build a system that matches each and every requirement. It could also handle all the possible edge-cases and yet be simple and easy to maintain. Well, reality is often disappointing: each new case our the system can handle increasing its complexity. Each new fancy tech, tool or concept we introduce, will do the same.
If we are choosing data transfer format, we can pick one of the few—but not all of them. Of course, can decide to add support for all the formats, but again the complexity increases.
If we want our system to be based only on stateful operations, we cannot expect that the system will be easily scalable. We can then off-load part of stateful processing to other services or tools, but again complexity follows.
Unfortunately, the software engineering is far from perfect. Same as in life—each action/decision has a consequence, either short or long-lasting. We cannot run away from that fact. Luckily for us, in software engineering the boundaries are much more flexible, and the consequences are not as dire as in personal life.
In the worse case, we can always build something from scratch. It will not be cheap, easily or even fast, but it is always a possibility.
Software Engineering Trade-Offs
Let's start with my favourite trade-off: Complexity vs Everything.
Complexity vs Everything
This one is as simple as it can. I wrote a lot about this one in the paragraph above, and I do not want to repeat myself. Almost every decision we make increases complexity, that's it.
With time, the complexity grows, and the growth speed only increases. The system is complex enough to begin with, and we want it to support newer and newer use cases.
As software engineers, we have to keep complexity as low as possible. In ideal case we should also leave some margin for future changes and requirements.
Cons of high complexity:
Increase RTB (Run the Business) costs
Increase onboarding cost
Increase costs of new change
Chance the system will become either unmaintainable or unreplaceable (at least without huge investment of time and money)
If you discover any real benefit of increased complexity, I owe you a coffee.
To be 100 % clear, complexity is not something we can fully run away from. It is a trait of every system. We just should be aware of it and balance our choices accordingly.
Simplicity vs Flexibility
Simplicity is a key always and everywhere.
I guess that most of us will prefer to work with easy to grasp and easy to maintained systems. I also guess that most of us prefer to design systems that are just like that. However, we must not oversimply our architectures. We should always leave some design margin for future changes.
Yet, making the system too flexible is also a no-go, at least in my opinion. There is no point in making your system capable of handling all possible future scenarios from the start. Half of what you expected will not ever occur, and the other half will be significantly different from what you expected. I will quote a proverb No big design up front.
Time-to-Market vs Technical Debt
Time to market vs. Technical Debt is probably the most crucial when it comes to actually delivering software.
Even the most beautiful and perfect code, does not matter if competitors are already there, and they are stealing away our to-be customers. In more corporate cases—we continuously fail to meet our deadlines and deliver on time.
Time to Market itself does not bring any value. I know that everyone want to be viral since day one but cascading software failure is probably not the desired way to achieve it. Our code has to actuality work and meet customer expectations. Also, the code itself is not the only source of tech debt. Things like observability, security, tests are among other sources.
Maybe, polishing the code for yet another time is not the best usage of time left. Instead, it may be better to focus on building a good observability pipeline or doing some performance tests.
Horizontal vs Vertical Scaling
If you are not sure as what any of them means, I recommend reading my text on Scalability.
Picking the way of how we can scale our application is probably one of the most crucial choices we can make while designing our application. It shapes all core design choices we make in our system and has long-lasting consequences.
This choice is not a set in stone; you can change the approach later down the road. However, all the architecture changes required to make application horizontally scalable will probably make the whole undertaking long, painful and expensive.
Same is true in the other way around — if we are migrating from horizontal to vertical. In both case, it will probably end with rewriting the system from scratch, or similar level of changes.
Horizontal scaling also has drawbacks. This approach also has drawbacks. You can achieve great performance with vertical scaling only.
Latency vs Throughput
This trade-off may seem strange. One would think that optimization of latency—single request processing time would impact the overall throughput—number of requests we can handle per unit of time.
Surprise, surprise after a certain point it seems not to be the case.
Optimizing and fine-tuning for latency tends to concentrate extra CPU cycles, cache space, or memory bandwidth on a single request. While it may yield great results initially, after a certain, non-arbitrary, threshold this results tends to diminish. After that point achieving any measurable gains can even require hardware or architectural changes.
In the case of Throughput we tend to split the resources proportionally. Focusing on optimizing average processing time across multiple requests. Instead of aiming at absolute latency of any one request.
As this trade-off can be somewhat tricky I recommend deciding based on what your use case needs. If you have some type of mixed use case, or focus point is not clear then I would recommend using or slightly optimizing your SLO (e.g. p99 latency). Only then focusing on throughput subjected to that SLO.
Stateful vs Stateless
To be honest, we cannot truly run away from stateful processing. Unless we have a very specific use case, we would need some form of state. The real trade-off here is to either store state in our service, close to our logic, or we want to offload it to some 3rd party tool or platform.
As some of the other software engineering trade-offs this one will also have a major impact on our system final design. Among other, it will impact areas like scalability, load balancing and overall complexity of the system. I will dive deeper into this topic in separate text.
Sync (Blocking) vs Async (Non Blocking)
Every network call, disk seek, and every RPC is happening asynchronously, in the background, at hardware level. This is the fact we cannot run away from.
The real trade-off is whether we expose that fact. Make our stack non-blocking (async) or hide this fact behind blocking (sync) API.
Opposite to the other trade-offs here this one has, relatively small impact on the overall architecture. However, it has a more significant impact on our codebase, and how our code works.
While non-blocking may seem to be the clear winner here, it is not that simple. Complexity introduced by async may not seem so bad. Nonetheless, it is a totally different programming model than what we used to. In most cases it will require a completely new mindset.
Beware, the tricky part, async models do not always outperform sync models for CPU-bound tasks.
I think that a good approach is to use a sync model in the core of the code base. Then using an async model in the edges when you need to handle I/O tasks. I believe this mix will get most of the pros of both approaches. Besides, it will also leave our core/domain pure, and play very nice with hexagonal arch.
Coupling and Cohesion
Though we used to think of them when talking about microservices. These two metrics in fact can be used to describe any type of architecture. No matter its size. We can even use it to describe relations between classes in the source code of a particular service.
In short:
Coupling describes the interdependence between two modules.
Cohesion describes how well the elements of a module belong together.
It is not the trade-off per se more like a target we should aim to. No matter where we apply both of the concepts the relation between them should be the same. Our entities should have: High Cohesion and Low (Loose) Coupling. Any other relation between the concepts is unhealthy and will cause problems.
Our job is to correctly adjust the levels of Coupling and Cohesion not to overdo any of them.
Other
These are not the only software engineering trade-offs out there — there are many more other ones. In fact, most if not all the decisions we make while designing the system are trade-offs.
Below a few examples:
Consistency vs Availability — probably the most famous. Microservice vs Monolith
3rd Tools vs In-house Cloud vs On-premise
Security vs Usability
Read vs Write Optimize
Navigating Software Engineering Trade-Offs
While they are not complex, long, and covers all possible edge cases, below rules are simple, cohesive, and easy to follow.
Evaluate the short-term and long-term impact of decisions
First and the most important rule — aim for the long-term.
Short-term gains are tempting — however they may have hidden costs and cause a lot of pain later on.
Estimate lifetime — services/modules/systems may not live long enough to see long-term at all.
Use data whenever you have them — without data you are just another person with an opinion.
Identify key stakeholders, their needs and act accordingly.
If you ever worked on any project with more than average complexity then you probably know that there are multiple people interested in its success (or failure). It is impossible to meet everyone's expectations.
Thus:
Map all interested parties
Prioritize the critical few who will approve or reject the outcome.
Capture their expectations and success criteria
Try to favor the side of trade-offs in such a way to meet their expectations.
Research — clarify goals and hard constraints
Requirements are not always clear, verify them.
When you have high level requirements, try to come up with an initial design.
Show you design to stakeholders and reiterate the requirements
Attempt to quantify metrics like: latency, throughput, storage whenever possible.
If you can, try doing Event Storming session. Crucial info has the tendency to show up in the most unexpected of times and places.
Remember: the more knowledge you will gather the easier it will be for you to navigate your landscape of trade-offs.
Document trade-offs, and their rationale (ADR)
Document, document and once again DOCUMENT. While it may sound trivial and repetitive it is probably the single most important thing you can do for your future coworkers.
Leaving behind even the simplest Architecture Decision Record (ADR), with:
What you chose
Why you did it
Pros and cons (optionally)
Alternatives considered and rejected
Such a document will ease up many, many things. Not to mention building your team reputation among whoever comes next to the project.
In the worst case, it spares future engineers from head-scratching, and from muttering unspeakables at 2 a.m. Which is probably the best measure of code quality.
Prototype or spike the extreme options to expose hidden pitfalls early.
If you think that you are lacking knowledge in some particular topic, or you are unsure as to how solutions would work. Try to spend some time and prepare a POC or do some spiking around the topic.
Better to drop some approaches sooner than later. It will cost less and be less painful. Just remember no to spend too much time on this, it should be POC not a fully working system, keep it simple.
Focus on simple solutions then optimize for the future.
As a final piece of advice:
Start from the simplest solution that meets current requirements
Optimize and make it more extensible only after completing the previous step.
In this way, you should end up with a well min-maxed system. It should meet all the requirements, be slightly optimized and had some free design space.
Summary
All of these may seem complex, hard or even overwhelming. Yes it is complex, there are a lot of software engineering trade-offs. However, there are multiple guides and best practices on how to navigate the problems of system design. I have even shared my own.
As with a many other things — practice makes perfect. There are multiple case-studies, books and articles on how to approach design challenges in different types of systems. I mention one of them here.
I believe that after some practice, all the problems here will sound significantly less scary.
Thank you for your time.
X LinkedIn Facebook Mastodon Copy Link Share
Categories Software Engineering
Best Software Engineer Books: Build Your Personal Library
Lock-Free Programming – From Primitives To Working Structures 
Bartłomiej Żyliński
Senior Software Engineer
🌐 Distributed Systems
🧠 System Design
🛠 Simplicity at Scale
Follow me:
LinkedIn
GitHub
X
Categories:
Distributed Systems (6)
Java (12)
Security (6)
Soft Skills (4)
Software Engineering (13)
Like what you read here - b uy me ☕
© 2026 Pask Software
• Built with GeneratePress
Table of Contents
×
We Cannot Build Perfect
Software Engineering Trade-Offs
Complexity vs Everything
Simplicity vs Flexibility
Time-to-Market vs Technical Debt
Horizontal vs Vertical Scaling
Latency vs Throughput
Stateful vs Stateless
Sync (Blocking) vs Async (Non Blocking)
Coupling and Cohesion
Other
Navigating Software Engineering Trade-Offs
Evaluate the short-term and long-term impact of decisions
Identify key stakeholders, their needs and act accordingly.
Research — clarify goals and hard constraints
Document trade-offs, and their rationale (ADR)
Prototype or spike the extreme options to expose hidden pitfalls early.
Focus on simple solutions then optimize for the future.
Summary
→ Table of Contents
✓
Thanks for sharing!
AddToAny
More…
