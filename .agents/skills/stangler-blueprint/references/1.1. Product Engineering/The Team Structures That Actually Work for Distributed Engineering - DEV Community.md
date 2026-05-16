---
name: The Team Structures That Actually Work for Distributed Engineering - DEV Community
keywords: (placeholder)
metadata:
  url: https://dev.to/tom_emmanuelogunmokun_24/the-team-structures-that-actually-work-fordistributed-engineering-f00
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
The Team Structures That Actually Work for Distributed Engineering - DEV Community
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
Tom Emmanuel Ogunmokun
Posted on Mar 30
The Team Structures That Actually Work for Distributed Engineering
# softwareengineering # software # development
Here is something most engineering leaders eventually discover, usually after the damage is done: the structure of your distributed team is not just a management decision. It is an architectural decision. Get the structure wrong and your codebase will mirror that mistake. Every unclear boundary in your org chart will show up as an unclear boundary in your code. Every ambiguous handoff between your internal team and your outsourced team will produce an ambiguous, poorly-defined handoff in the system itself.
This is not a theory. It is a law Conway's Law and it has been operating quietly in your engineering organization whether or not you have been paying attention to it.
This article makes three arguments. First: most distributed team structures fail not because of communication but because of cognitive overload a different problem with a different solution. Second: Team Topologies, applied correctly at startup and scale-up stage, gives you a practical model for fixing it. Third: Conway's Law tells you why the team structure decision and the architectural decision have to be made together, and what happens when they are not.
At the end, there is a diagnostic you can run on your current setup today.
The Real Problem Is Not Communication. It Is Cognitive Overload.
Every article about distributed team management tells you the problem is communication. The solution is always some combination of better tools, more check-ins, and clearer escalation paths. None of it is wrong exactly. But it is treating a symptom while the actual disease goes undiagnosed.
At the 2024 Enterprise Technology Leadership Summit, organisational psychologist Dr. Laura Weis and Team Topologies co-author Manuel Pais presented research showing that cognitive overload costs engineering organisations $322 billion annually in lost productivity — and that most organisations are measuring system performance metrics while being entirely blind to the overload that is slowing their teams down.
The reason cognitive overload is the right diagnosis is precise. In a co-located team, a bad structure gets patched with hallway conversations and shoulder taps. People fill the gaps with informal communication that is not planned, not documented, and not visible. It works, imperfectly but well enough. In a distributed team, those informal patches do not exist. The gaps that bad structure creates become genuine bottlenecks, and they compound with every sprint.
There are three types of cognitive load, and understanding the distinction is what separates a team structure that works from one that slowly grinds its people down 
The structural implication is direct: a well-designed distributed team minimizes extraneous load and maximizes germane load. A poorly designed one does the opposite. And the mechanism by which poor structure creates extraneous load in a distributed team is not communication frequency, it is domain boundary ambiguity. When it is unclear which team owns which part of the problem, engineers carry the mental burden of that ambiguity constantly. They spend cognitive capacity figuring out whose responsibility it is before they can spend cognitive capacity actually doing the work.
Team Topologies at Startup Scale: The Framework Nobody Is Applying Correctly
Team Topologies, the framework developed by Matthew Skelton and Manuel Pais, defines four fundamental team types and three interaction modes. Every serious article about distributed engineering mentions it. Almost none of them apply it at the stage where most of this article's readers actually are — startup and scale-up, with a small distributed team that includes outsourced engineers.
Team Topologies identifies four team types. As Atlassian's Team Topologies overview describes them: Stream-Aligned teams focus on a single valuable stream of work and are empowered to build and deliver independently. Platform teams provide internal services that reduce cognitive load on stream-aligned teams. Enabling teams are specialists who help stream-aligned teams build capabilities they are currently missing. Complicated Subsystem teams own parts of the system requiring deep specialist knowledge, so stream-aligned teams do not have to carry that complexity themselves.
The critical insight, as Martin Fowler notes on his bliki, is that the primary benefit of every supporting team type — Platform, Enabling, Complicated Subsystem is cognitive load reduction for stream-aligned teams. That is not a secondary benefit. It is the entire point. Every team design decision in Team Topologies is a cognitive load decision.
The Stage-Structure Match: Applying Team Topologies Where You Actually Are
Here is the original framework that most Team Topologies discussions skip entirely — how to apply the model at each funding stage, specifically when one or more of your teams is outsourced. 
At pre-seed and seed stage: one stream-aligned team
At this stage, complexity is a choice you are making, not an inevitability. One team, one product stream, clear ownership from frontend to backend to deployment. Your outsourced engineers are part of this team — not a separate external vendor — and their domain boundaries need to be defined before the first sprint begins, not after the first miscommunication.
The most common mistake at this stage is structuring by technical layer: a frontend team, a backend team, a DevOps function. This produces exactly the architecture Conway's Law predicts — a system with sharp, hard-to-cross boundaries between layers, where every feature requires coordination across all three groups. Restructure by product domain instead. One team owns the entire user journey for one feature set. Slower to feel natural at the start. Faster in every sprint thereafter.
At Series A: stream-aligned pods by product domain
By Series A, product complexity has usually outgrown a single team's cognitive capacity. The right structural move is to split into pods by business domain, not by technical function. Each pod owns its domain end-to-end: frontend, backend, data, and deployment within its scope.
One specific rule worth making explicit: Team Topologies' own guidance on platform team misuse is clear that platform teams are frequently created too early, before there is genuine shared infrastructure to manage. At Series A, if you are spinning up a platform team, it should be internal. The cognitive overhead of outsourcing platform infrastructure — the shared tooling and foundational services that every other team depends on — is almost always higher than the cost saving justifies.
At Series B and beyond: the full model becomes viable
At this scale, all four team types are genuinely useful. Outsourced teams continue to work best in stream-aligned roles where domain expertise and delivery autonomy are the primary requirements. Complicated subsystem teams owning deeply specialized components like a payment processing engine or a machine learning inference layer can be outsourced successfully, but only with a rigorously defined Team API that makes the subsystem's interface explicit and stable.
Conway's Law Is Already Running Your Distributed Team. Here Is How to Use It Deliberately
Conway's Law was first described by Melvin Conway in 1968 and later named by Fred Brooks in The Mythical Man-Month. As Martin Fowler states on his bliki, Conway's observation has been validated consistently across software organizations of every size: systems are constrained to follow the communication patterns of their designers.
The modern restatement, from architect Ruth Malan, makes the strategic implication explicit: if the architecture of the system and the architecture of the organization are at odds, the architecture of the organization wins. Every time
What Conway's Law Means Specifically for Outsourced Teams
Every Conway's Law article applies the principle to internal org design. Here is the application that is missing from the entire content landscape: Conway's Law is even more consequential when the organizational boundary is between two separate companies.
When your internal product team and your outsourced engineering team have an ambiguous, poorly-defined boundary, your codebase will develop an ambiguous, poorly-defined boundary in the exact same place. Not as a metaphor. As a technical reality. The module that nobody quite owns across the two teams will become the module that nobody quite owns in the architecture. The handoff that is unclear in your sprint planning will produce a handoff that is unclear between your services.
This is confirmed by research on distributed teams and monolith emergence: when distributed teams with unclear boundaries work on a shared system, they stop communicating about the parts that require cross-team coordination. Each group makes local decisions to optimise their piece. The architecture fragments along the informal team boundaries whether or not the design acknowledged it — producing what engineers call a distributed monolith. The worst of both worlds: the complexity of a distributed system with the tight coupling of a monolith.
The Inverse Conway Maneuver for Outsourced Teams
The Inverse Conway Maneuver, coined by Jonny LeRoy and Matt Simons and later developed in the Accelerate research, states that organizations should deliberately design their team structure to produce the architecture they want — not let team structure emerge and then be surprised by the architecture that results.
Applied to an outsourced team relationship, the Inverse Conway Maneuver looks like this: before you define the team structure, define the architecture. Specifically, define the boundary between what your internal team owns and what your outsourced team owns at the code level. Then structure the teams to match that boundary. Not the other way around.
As the Accelerate research puts it: the goal is for your architecture to support the ability of teams to get their work done from design through to deployment without requiring high-bandwidth communication between teams. In an outsourced relationship, that means the outsourced team should be able to deliver their scope without requiring constant coordination with your internal team. If they cannot, the team boundary and the architectural boundary are misaligned, and Conway's Law will make you pay for that misalignment in every sprint.
The Team API: Making the Boundary Explicit
The practical instrument for executing the Inverse Conway Maneuver with an outsourced team is the Team API — a one-page document that makes the team's boundary explicit before a line of code is written. It is not a legal contract and not a project scope document. It is a technical and operational agreement about where one team ends and another begins.
A well-defined Team API between your internal team and your outsourced team covers:
What the outsourced team owns end-to-end: the services, features, or domains for which they have full delivery responsibility.
What they consume as a service: the internal infrastructure, APIs, or shared services they depend on but do not own.
The interaction mode: X-as-a-Service for stable, ongoing dependencies. Collaboration for short-period joint discovery. Facilitation for knowledge transfer.
The change protocol: how does the outsourced team signal when a boundary needs to change? How do they flag a dependency that is blocking them?
The communication surface: what gets communicated between teams, at what frequency, through what channel, and to whom?
_ The most expensive architectural decision most companies make is not a technical one. It is the decision to start an outsourced engagement without a defined Team API. The resulting codebase will faithfully mirror that absence of definition. Fixing it later costs more than defining it upfront by an order of magnitude.
_
The Diagnostic: Five Questions to Run on Your Current Setup
Here is the practical instrument the article has been building toward. Run these five questions on your current distributed team structure. Honest answers will tell you where you have a cognitive load problem, a Conway's Law problem, or both.
Question 1: How many domains does your outsourced team own?
Team Topologies domain guidance is specific: teams can handle two to three simple domains at most. Complex domain teams should not take on extra domains, even simple ones. No team should manage two complicated domains simultaneously.
If your outsourced team owns more than two distinct product or business domains, the structure is generating cognitive overload regardless of team quality. The fix is a boundary redefinition, not a performance conversation.
Question 2: How many other teams does your outsourced team coordinate with regularly?
Count the number of regular, required coordination points between your outsourced team and any other team internal or external. Each coordination point is a cognitive load cost. More than two regular cross-team dependencies means the team is operating in permanent collaboration mode, which is expensive by design and unsustainable long-term.
The target: your outsourced team should be able to deliver a complete sprint's worth of value with one primary coordination point your internal product or technical lead and no more than one secondary coordination point with another team.
Question 3: Can an engineer on your outsourced team describe the architectural boundary of their work?
Ask an engineer — not the team lead but describe what they own in the system, what they consume, and where their responsibility ends. If the answer requires clarification, hedging, or is different from what the team lead would say, your Team API is either undefined or not understood by the people it applies to. A Team API that exists only in a document nobody reads is not a Team API.
Question 4: Does your team structure match your stage?
Refer to the Stage-Structure Match table above. If your current topology does not match your funding stage, the mismatch itself is a structural cost. The most common mismatch: a seed-stage company that has structured by technical layer (frontend, backend, DevOps) rather than by product domain. The second most common: a Series A company that has outsourced its platform function, creating a high-dependency, high-cognitive-load relationship between the outsourced platform team and every internal stream-aligned team.
Question 5: If the outsourced team left tomorrow, what would happen to the codebase?
This is the Conway's Law question. The honest answer reveals the true state of your architectural boundary. If the answer is 'we would lose the entire payment module' or 'nobody else understands that service,' the boundary is not defined it is just an accident of who happened to build what. A well-defined boundary means the outsourced team's departure would leave a clean, documented, well-interfaced component that another team could adopt. A poorly defined boundary means it would leave an undocumented tangle that is effectively owned by nobody.
The Bottom Line: Structure Is Architecture
The distributed teams that work are not the ones with the best communication tools. They are the ones whose structure was designed deliberately — where cognitive load was considered before team size, where the Team API was defined before the first sprint, and where someone understood that the team boundary and the architectural boundary are the same decision.
Conway's Law will run your distributed team whether or not you use it deliberately. The Inverse Conway Maneuver gives you the option to use it on purpose. Team Topologies gives you the model. The cognitive load framework gives you the diagnostic.
None of this requires a large team or a mature engineering organisation. It requires a single afternoon before the engagement starts, a one-page Team API document, and a clear answer to the question: what does this team own, completely and end-to-end?
That answer is the foundation everything else is built on. Get it right before you write a line of code.
Need a Team Structure That Actually Works?
At Tribesquare, we structure every engagement around these principles — defined Team APIs, explicit cognitive load boundaries, and a topology that matches your stage. We build with you, not just for you.
Start the conversation at tribesquare.co
 The DEV Team
Promoted
What's a billboard?
Manage preferences
Report billboard
What is an LLM actually doing when it's "thinking"?
Ever wondered what an LLM is doing when it's "thinking"?
In this episode of Release Notes Explained, we cover the fundamentals of how thinking and reasoning models work including concepts like:
Scaling laws
Test-time compute
Reinforcement learning from verifiable rewardsHope you enjoy! 🩵
Watch the video 🎥
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
 AWS
Promoted
What's a billboard?
Manage preferences
Report billboard
Building industry breakthroughs together
Discover how the cloud helps businesses adapt, innovate, and grow in real time. Tune in live.
Register Now
Tom Emmanuel Ogunmokun
Follow
Joined Mar 30, 2026
Trending on DEV Community
 Welcome to the DEVengers Organization! A group of Extraordinary Individuals that Influenced Dev.to the platform has ever seen! 🚀 # discuss # community # meta # programming
 AI vs Non-AI: Building the Same Project Twice # ai # softwareengineering # discuss # programming
 I Didn't Stop Building. I Just Left My Laptop. # career # learning # development # workplace
 AWS
Promoted
What's a billboard?
Manage preferences
Report billboard
Building industry breakthroughs together
Discover how the cloud helps businesses adapt, innovate, and grow in real time. Tune in live.
Register Now
👋 Kindness is contagious
What's a billboard?
Manage preferences
Report billboard
Take a moment to explore this thoughtful article, beloved by the supportive DEV Community. Coders of every background are invited to share and elevate our collective know-how.
A heartfelt "thank you" can brighten someone's day—leave your appreciation below!
On DEV, sharing knowledge smooths our journey and tightens our community bonds. Enjoyed this? A quick thank you to the author is hugely appreciated.
Okay
💎 DEV Diamond Sponsors
Thank you to our Diamond Sponsors for supporting the DEV Community
Google AI is the official AI Model and Platform Partner of DEV
Neon is the official database partner of DEV
Algolia is the official search partner of DEV
DEV Community — A space to discuss and keep up software development and manage your software career
Home
About
Contact
MLH
Code of Conduct
Privacy Policy
Terms of Use
Built on Forem — the open source software that powers DEV and other inclusive communities.
Made with love and Ruby on Rails. DEV Community © 2016 - 2026. 
We're a place where coders share, stay up-to-date and grow their careers.
Log in Create account     
