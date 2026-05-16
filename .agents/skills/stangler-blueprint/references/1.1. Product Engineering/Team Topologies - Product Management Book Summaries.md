---
name: Team Topologies - Product Management Book Summaries
keywords: (placeholder)
metadata:
  url: https://andrewclark.co.uk/product-book-summaries/team-topologies
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Team Topologies
 
Team Topologies
Author
Manuel Pais and Matthew Skelton
Year
2019 
Review
This book is essential reading if you need or want to learn a little more about organisational design. The model in this book is a simplification of a messier reality, but it's a useful frame of reference. It establishes a limited number of team types and interaction types between teams. The authors then explain how fracture planes and sensing/triggers can help you identify the best team topologies.
You Might Also Like
Curious about how are these recommendations generated? Learn more.
[
Project to Product
I'm not sure if the 'Flow Framework' is the golden goose of transformation. I found the theory intriguing, but I have reservations about implementing it within a large organisation. There was a lack of practical implementation advice, and based on my experience, I believe it would be challenging to implement without a team of consultants. Nevertheless, there are plenty of interesting nuggets and principles in this book. It has certainly influenced my perspective on team topologies, and managing those zero-sum tradeoffs between features, quality and risk. andrewclark.co.uk](https://andrewclark.co.uk/all-media/project-to-product)
[
Articulating Design Decisions
Master the art of communicating design decisions with this insightful summary of Tom Greever's "Articulating Design Decisions". Learn how to effectively present your work, foster agreement, and gain support from stakeholders. Discover key strategies for building relationships, preparing for meetings, responding to feedback, and navigating challenging situations. Enhance your ability to articulate the problem-solving, user-centric, and business-oriented aspects of your design choices. A must-read for designers and product managers looking to improve their communication skills and drive successful outcomes. andrewclark.co.uk](https://andrewclark.co.uk/product-book-summaries/articulating-design-decisions)
[
ReOrg
There's so much more to a reorg than choosing a shape or a model. This book does a great job of sketching out a sensible 4 step process that'll help you avoid disaster. andrewclark.co.uk](https://andrewclark.co.uk/all-media/reorg) 
Key Takeaways
The 20% that gave me 80% of the value.
The Problem with Org Charts, Conways Law and Why it Matters, Team First Thinking
Two problems with traditional org charts:
They're often out of date (office politics make them hard to update and issue) and based on past projects and legacy systems
They don't show the interactions and communication between teams. If they did - we might be better able to assess them
Evaluate your org design through the lens of systems thinking:
Optimising for the whole
Understanding flow and bottlenecks
Organisations are complex adaptive systems
expect to review and iterate over time
structures should be able to flex and adapt to new conditions
‣
The key to successful knowledge work is interactions between people and teams
The three different organisation structures in every organisation:
Formal - facilitates compliance (org chart)
Informal - the realm of influence between individuals (people)
Value Creation - how work gets done based on inter-personal and inter-team reputation (teams)
Explicitly agree interaction models modes with other teams - set clear expectations and build trust
Team Topologies clarify team purpose and responsibilities, increasing the effectiveness of their interrelationships.
‣
Four Fundamental Team Types (covered later)
Stream-aligned
Platfrom
Enabling
Complicated-Subsystem
Design Software Architecture and Org Structures together to take into account Conway's law
Clean Conways Law (by Ruth Malan): If the architecture of the system and the architecture of the organisation are at odds, the architecture of the organisation wins
Reverse/ Inverse Conway Maneuver: change your team and org structure to achieve the desired software architecture you want (as opposed to mandating the architecture design)
You need to understand what software architecture is needed before you organise teams. Technology leaders need to lead or be involved in team design
Goal: architecture to support teams to get work done, without requiring high-bandwidth communication between teams
Restrict unnecessary communication
Does the structure minimise the number of communication paths between teams?
Low-bandwidth or Zero-Bandwidth communication between teams is desirable
Use fracture plane patters to split up software into smaller chunks
Limiting communication paths to well-defined team interactions produces modular, decoupled systems.
Tool choices can drive communication patterns. Collaborative teams should have shared tools
Design Team APIs and Facilitate team interactions. A team API is a description and specification for how to interact with the team. Teams should define, advertise, test and evolve their team API to ensure it's fit for other consumers
Restrict the cognitive load of each team until it's manageable.
Instead of designing a system in the abstract - design the system and it's boundaries to fit the cognitive load within teams. Restrict team responsibilities to match cognitive load
Dan Pink's 3 elements of intrinsic motivation (autonomy, mastery and purpose) are challenged when a team has too many domains or responsibilities.
Do you feel like you're effective and able to respond in a timely fashion to the work you're asked to do?
‣
Identify the domains a team has to deal with, then classify them by difficulty, divide appropriately
Assign each domain to a single team
A single team should be able to accommodate 2-3 simple domains
A team responsible for a complex domain - shouldn't have any more domains assigned to them
Avoid a single team responsible for two complicated domains
When in doubt - prioritise how the team feels about it
Optimise for flow of change, bottlenecks and feedback from running systems
Fast flow requires restricting communication between teams
The fewer dependencies the better
Steam-aligned teams are the preferred option
The speed of software delivery is strongly affected by how many team dependencies the org design instills
Team-First: take a humanistic approach to system and org design
Use small long-lived teams as the standard
The ideal size of teams, groups and divisions depends on the level of trust in the organisation. High trust organisations can have larger collections at each level
Single Teams - 5-15 max
Groups of teams - 50-150 max (tribes, families)
P&L / Division - 150-200 max
Make work flow to long-lived teams
Teams take time to be effective (2-12 weeks)
Keep stability around and within a team so they can reach a high level of effectiveness
Establish clear boundaries of responsibility for teams.
Every part of the system needs to be owned by exactly one team. There should be no shared ownership of components, libraries or code
Team-first mindset = putting the needs of the team above their own
Reward the whole team, not individuals (allocate a training budget to the team)
Facilitate Team Interactions to build trust, awareness and learning. Time, space and money
Static Team Topologies, The Four Fundamental Topologies, Choose Team-First Boundaries
Consciously design your teams into Team Topologies. Teams should be deliberately placed into organisations
Shape Team Intercommunication to enable flow and sensing
Considerations when selecting a topology:
Technical Maturity
Cultural Maturity
Organisational size, software scale and engineering maturity
Remove or lessen dependencies on specific teams by breaking down their set of responsibilities and empowering other teams to take some of them on
It is essential to detect and track dependencies and wait times between teams
The Four Fundamental Team Topologies
All teams should move toward one of these types (if not clear cut today)
Simplifying teams to just these 4 types helps reduce ambiguity within the organisation
1) Stream-Aligned Teams
A continuous flow of work aligned to a business domain or org capability
Aligned to a single product, service or feature, persona, or user journey
From idea to deployment, as independently as possible
Primary team type of the org
Other team types are there to reduce the burden on steam-aligned teams
2) Enabling Teams (technical consulting teams)
Composed of specialists in a given technical or product domain
Help bridge the capability gap of stream aligned teams to give them more capacity
Goal is to increase the autonomy of the stream-aligned teams - by growing their capabilities
Often focused on one of: build engineering, continuous delivery, deployments, test automation
Set up a skeleton → initial examples → work with teams to advise on implementation
Knowledge transfer is likely to be temporary when a new technology is adopted (teams will pair closely in this moment
3) Complicated Sub System Teams
Building and maintaining a sub-system tat depends heavily on specialist knowledge
Goal: reduce cognitive load of stream-aligned teams
Wouldn't be feasible, cost-effective for a stream-aligned team to own that system
Decision driven by cognitive load - not opportunity of a shared component
4) Platform Teams
Enable stream aligned teams to deliver work with autonomy
Stream-aligned teams maintain ownership of building, running and fixing their tech
Platform: self-service APIs, tools, services, knowledge and support which are arranged as a compelling internal product.
Platforms team value is measured by the value of the services they provide to product teams
Don't group functional expertise like UX, Architecture, Data Processing, Database Administration or Testing. That model doesn't work for safe and rapid change.
Move to mostly stream-aligned teams for longevity and flexibility
6/7 or 9/10 teams should be stream-aligned teams
Software boundaries or Fracture Planes
Fracture Plane is a natural seam in the system that allows it to be split easily into multiple parts
Try to align boundaries with business domain areas -
Helps with prioritisation, flow and user experience
Most fracture planes should map to a business-domain bounded context
Aligning technology to business context - reduces mismatches in terminology, everyone is speaking the same language
Types of fracture plane: regulatory compliance, team location, change cadence, risk, performance isolation, technology, user personas
Team interaction modes, evolve team structures with organisational sensing
Most org design team is done as at a 'point in time' - we should be thinking about how we want them to evolve and change over time
Three core team interaction modes:
Simplifies interactions between teams
Avoid all teams communicating with all other teams to achieve their goals
What type of interaction should we be having with this other team? Should we be collaborating closely? Should we be expecting or providing a service? Or should we be expecting or providing facilitation?
1) Collaboration
Driver of innovation and rapid discovery but boundary blurring
Good for rapid discovery - requires good alignment and high appetite and ability for working together between teams. Bringing together different skill sets to solve a challenge.
Overlap between teams can be small or almost total
Teams must take joint responsibility for overall outcomes of their collaboration
Hit in productivity - so should be for something high value, and on a temporary basis
Only do it with one team at a time
Increases innovation and reduces hand-offs
Context sharing, responsibility challenges, reduced output
2) X-as-a-service: Clear responsibilities with predictable delivery but needs good product management
Best when teams need to use a code library, component, API, or Platform that just works without much effort → where that can be effectively provided as a service by another team
Consuming or providing something with minimal collaboration
Requires a high standard of XaaS teams - need to adapt to changing team needs, they need to make the DevEx compelling.
Clarity of ownership and responsibility
Reduced detail/context sharing between teams
Danger of reduced flow if the boundary or API is not effective - the service boundary needs to be well chosen
3) Facilitating: Sense and reduce gaps in capabilities
Where one or more teams would benefit from the active help of another team facilitating or coaching some aspect of their work
Goal: enable other teams to be more effective, learn more quickly and understand new technology
Goal: to discover and remove common problems or impediments across the teams
Typically interact with many teams - not building but focusing on quality of interactions between other teams that are building and running software
Unblocks stream-aligned teams to increase flow
Requires experienced staff (to not work on building or running things)
The interaction may be unfamiliar or strange to one or both teams involved in facilitation
Associate behaviours to the different interaction modes:
Collaboration mode: high interaction and mutual respect
X-as-a-service: emphasise the user experience
Facilitating mode: help and be helped
How to choose:
Use awkwardness in team interactions to sense missing capabilities and misplaced boundaries
Triggers for evolution of team topologies
Software has grown too large for one team
Delivery cadence is becoming slower
Multiple business services rely on a large set of underlying services
Things to sense:
Have we misunderstood how users need/want to behave?
Do we need to change interaction modes to enhance how the org is working?
Build or by discussions about x thing?
Is the collaboration between two teams still effective? Should we shift modes?
If the flow as smooth as it could be? What hampers flow?
Are the promises between the two teams still valid and achievable?
3 ways of DevOps from (the DevOps Handbook)
Systems thinking: optimise for fast flow across the whole organisation, not just parts
Feedback loops: development informed and guided by operations
Culture of continual experimentation and learning: sensing and feedback for every team interaction 
Deep Summary
Longer form notes, typically condensed, reworded and de-duplicated.
Part 1: Teams as the Means of Delivery
The Problem with Org Charts, Conways Law and Why it Matters, Team First Thinking
Two problems with traditional org charts:
They're often out of date (office politics make them hard to update and issue) and based on past projects and legacy systems
They don't show the interactions and communication between teams. If they did - we might be better able to assess them
Evaluate your org design through the lens of systems thinking:
Optimising for the whole
Understanding flow and bottlenecks
Organisations are complex adaptive systems
expect to review and iterate over time
structures should be able to flex and adapt to new conditions
‣
The key to successful knowledge work is interactions between people and teams
The three different organisation structures in every organisation:
Formal - facilitates compliance (org chart)
Informal - the realm of influence between individuals (people)
Value Creation - how work gets done based on inter-personal and inter-team reputation (teams)
Empower teams - treat them as the fundamental building blocks
Explicitly agree interaction models modes with other teams - set clear expectations and build trust
Org Structure shouldn't be static - needs to be adaptable
‣
5 rules of thumb for org design (from Naomi Stanford)
Design when there is a compelling reason
Develop options for deciding on a design
Choose the right time to design
Look for clues that things are out of alignment
Stay alert to the future
Team Topologies clarify team purpose and responsibilities, increasing the effectiveness of their interrelationships.
Team Topologies are a consistent and actionable guide for evolving your team design
Four Fundamental Team Types
Stream-aligned
Platfrom
Enabling
Complicated-Subsystem
Take into account Conway's law, cognitive load and flow
Effective and humanistic approach
The team is the indivisible element of software delivery - people have a finite cognitive capacity
Design Software Architecture and Org Structures together to take into account Conway's law
Conway's Law: Organisations which design systems are constrained to produce designs which are copies of the communication structures of these organisations
Clean Conways Law (by Ruth Malan): If the architecture of the system and the architecture of the organisation are at odds, the architecture of the organisation wins
If your org design doesn't compliment your system design - then change one of the two
Organisations are constrained to produce designs that reflect communication paths.
An organisation that is arranged in functional silos is unlikely to produce software that is well architected for end-to-end flow
The design of the organisation constrains the “solution search space,” limiting possible software designs. For any given org structure - there are system designs that can't be pursued because the communication paths don't exist
Monoliths need to be broken down, while keeping a team focus.
To adapt system designs and make them more amenable to flow → reshape the organisation
Reverse/ Inverse Conway Maneuver: change your team and org structure to achieve the desired software architecture you want (as opposed to mandating the architecture design)
You need to understand what software architecture is needed before you organise teams.
Team assignments are the first draft of your software architecture
Technology leaders need to lead or be involved in team design
‣
Best Practices for software architecture
Loose coupling → components don't have strong dependencies on others
High cohesion → components have clear bounded responsibilities, their internal elements are strongly related
Clear and appropriate version compatibility
Clear and appropriate cross-team testing
Goal: architecture to support teams to get work done, without requiring high-bandwidth communication between teams
Software architecture should reflect the flows of change they enable
Keep things team sized (for ease of understanding)
Team-first software architecture
Exploit architecture as an enabler of change. Partition the architecture to absorb change.
Restrict unnecessary communication
Requiring everyone to communicate with everyone else is a recipe for a mess. Not all communication and collaboration is good.
Goal: focused communication between specific teams.
Notice unaddressed design interfaces and unpredicted team interactions
Does the structure minimise the number of communication paths between teams?
Low-bandwidth or Zero-Bandwidth communication between teams is desirable (if you can still build and release great software)
Communication within teams = high bandwidth
Communication between two paired teams = mid bandwidth
Communication between most teams (should be) = low bandwidth
Use fracture plane patters to split up software into smaller chunks
Limiting communication paths to well-defined team interactions produces modular, decoupled systems.
Everyone doesn't need to communicate with everyone - else systems become monolithic, tangled and highly coupled.
Tool choices can drive communication patterns.
Collaborative teams should have shared tools
Independent teams can have separate tools
But make information visible
Design Team APIs and Facilitate team interactions
Team API: description and specification for how to interact with the team. It includes:
Code, versioning, wiki and documentation, practices and principles, communication, work information (priorities backlog etc)
Team API should consider the usability of other teams - Will they find it easy to interact with us?
Teams should define, advertise, test and evolve their team API to ensure it's fit for other consumers
Restrict the cognitive load of each team until it's manageable.
Put the team first, consider their cognitive load and restrict it until it's manageable.
You don't want any team to have an excessive amount of responsibilities and domains. Else they won't be able to pursue mastery
Dan Pink's 3 elements of intrinsic motivation (autonomy, mastery and purpose) are challenged when a team has too many domains or responsibilities.
Make sure the cognitive load on a team isn't too high!
Restrict team responsibilities to match cognitive load
True for both coding and implementation tasks
Domains, applications, tools, deployments etc
Definition of cognitive load;
Intrinsic: aspects of the task fundamental to the problem space
reduce through training, tech choices, hiring, pair programming
Extraneous: environment in which the task is being done
remove boring or superfluous tasks with reduction and automation
Germane - aspects of the task that need special attention for learning or high performance
Create more space for this
Limit the size of the subsystem or area on which the team works
Do you feel like you're effective and able to respond in a timely fashion to the work you're asked to do?
How to limit the number and type of domains per team:
When in doubt - prioritise how the team feels about it
Identify the domains a team has to deal with
Classify them by difficulty:
Simple: most of the work has a clear path of action
Complicated: changes need to be analysed and might require a few iterations on the solution to get it right
Complex: solutions require a lot of experimentation and discovery
Compare pairs of domains to fine tune your classification
Important Heuristics:
Assign each domain to a single team
A single team should be able to accommodate 2-3 simple domains
A team responsible for a complex domain - shouldn't have any more domains assigned to them
Avoid a single team responsible for two complicated domains
Instead of designing a system in the abstract - design the system and it's boundaries to fit the cognitive load within teams
Choose somewhere between monolithic and micro-services based to fit the maximum team cognitive load
A team first approach will favour small decoupled services
To increase the size of the domain a team looks after:
provide a team-first working environment
minimise distractions in the working week
change the management style by communicating goals and outcomes (eyes on, hands off)
Minimise the cognitive load for others → heuristic for software development
Optimise for flow of change, bottlenecks and feedback from running systems
Choose software architectures that encourage team-scoped flow.
Fast flow requires restricting communication between teams
Design the intercommunications between teams - the fewer dependencies the better
Optimise for flow → steam-aligned teams are preferred
Occasionally you'll need a complicated-subsystem team
The speed of software delivery is strongly affected by how many team dependencies the org design instills
Team collaboration is important if you're doing discovery
Agile, Lean IT and DevOps all demonstrated the value of small autonomous teams aligned to the flow of
Team-First: take a humanistic approach to system and org design
Start with the team for effective software delivery
Make small autonomous teams that are aligned to the flow of the business (Agile, Lean IT and DevOps all agree)
Teams outperform the equivalent number of individuals for knowledge rich, problem solving tasks
Teams are essential for modern software development (due to the complexity)
Who is on the team matters less than the actual team dynamics
Things to consider: lifespan, size, relationships and cognition
Use small long-lived teams as the standard
Stable grouping of 5-9 people
The team is the smallest unit within an organisation
In larger teams - trust can erode. You need to design for high trust. Smaller size teams foster trust
‣
Dunbars Number's / relationship limits
5 people - for personal relationships and working memory
15 people - for deep trust
50 people - for mutual trust
150 people - whose capabilities you can remember
The ideal size of teams, groups and divisions depends on the level of trust in the organisation. High trust organisations can have larger collections at each level
Single Teams - 5-15 max
Groups of teams - 50-150 max (tribes, families)
P&L / Division - 150-200 max
Make work flow to long-lived teams
Teams take time to be effective (2-12 weeks)
Keep stability around and within a team so they can reach a high level of effectiveness
Teams reach a state when they're much more effective than a group of individuals
Flow the work to the team
Teal Performance Model: Forming, Storming, Norming, Performing
Establish clear boundaries of responsibility for teams.
The Team Owns the software
Team ownership brings continuity of care
Teams can think multiple horizons out (H1: immediate, H2 few periods, H3 beyond that)
Every part of the system needs to be owned by exactly one team
There should be no shared ownership of components, libraries or code
Team Members need a team-first mindset
The team is the fundamental means of delivery, not the individual
Team members should put the needs of the team above their own:
Arrive for stand-ups on time
Keep discussions and investigations on track
Encourage a focus on team goals
Help unblock others before starting new work
Mentor new or less experienced team members
Don't aim to win arguments - agree to explore options
Remove 'team toxic' people before the damage is done
Embrace Diversity in Teams
Diverse mix of people fosters better results
Variety of viewpoints and experiences helps a team traverse landscape of solutions faster
Reward the whole team, not individuals (allocate a training budget to the team)
Facilitate Team Interactions to build trust, awareness and learning
Ultimately makes teams go faster.
Time, space and money are required for people to develop their professional competencies
Make learning and trust building part of the rhythm that facilitates effective team interactions
working environment (enable interaction) - Red Hat put everything on wheels!
time away from that in guilds, or communities of practice
‣
Part 1: Book Recommendations
Mik Kersten : Project to Product
Niels Pflaeging: Organise for Complexity
Naomi Stanford: Guide to organisation design
McChrystal: Team of Teams
Tuckman: Teal
Frédéric Laloux: Reinventing Organisations:
Part 2: Team Topologies that Work for Flow
Static Team Topologies, The Four Fundamental Topologies, Choose Team-First Boundaries
Consciously design your teams into Team Topologies
Teams should be deliberately placed into organisations
Don't do Team Design Ad Hoc
Don't shuffle team members often
Questions you should try and answer…
Given out skills, constraints, cultural and engineering maturity, desired software architecture, and business goals, which team topology will help us deliver results faster or safer?
How can we reduce or avoid handovers between teams in the main flow of change?
Where should the boundaries be in the software system in order to reserve viability and encourage rapid flow? How can our teams align to that?
Design for the flow of change → from concept to working software
the old model: functional silos between departments, outsourcing and hand-offs
Shape Team Intercommunication to enable flow and sensing
Software development isn't a one way process - we need to act quickly on feedback from live systems
Functional silo's (Dev, Test, Transition, BAU) with hand-offs aren't as good for flow
Avoid hand-offs by keeping work within the stream-aligned team.
Make sure operational information flows back to the team
There is no one-size-fits-all approach to structuring teams for DevOps success
BUT there are several known bad topologies
Feature teams require high engineering maturity and trust
Feature Team: cross-functional, cross-component team that can take a feature from idea to production
Feature teams need to be self-sufficient - they need to get to production without the help of other teams
You might need to add communication conduits between feature teams to help with coordination (system architects, integration leads etc)
Product teams need a support system to be independent (infrastructure, platform, test environments, delivery pipelines)
The key to making a team autonomous is making sure that any external dependencies are non-blocking
That often requires self-service capabilities - things built and maintained by other teams
The SRE model makes sense at scale - relationship changes throughout the lifecycle.
Considerations when selecting a topology:
Technical Maturity
Cultural Maturity
Organisational size, software scale and engineering maturity
Low maturity orgs need time to acquire capabilities before going to autonomous E2E teams
Meanwhile more specialised teams are an acceptable trade-off as long as they collaborate closely
Remove or lessen dependencies on specific teams by breaking down their set of responsibilities and empowering other teams to take some of them on
think about how team's capabilities cause dependencies within teams
It is essential to detect and track dependencies and wait times between teams
Book Recommendation: Making Work Visible → use a physical dependency matrix or dependency tags.
The Four Fundamental Team Topologies
Stream-aligned
Platfrom
Enabling
Complicated-Subsystem
All teams should move toward one of these types (if not clear cut today)
Simplifying teams to just these 4 types helps reduce ambiguity within the organisation
1) Stream-Aligned Teams
A continuous flow of work aligned to a business domain or org capability
Clarity of purpose and clear responsibilities between teams is key
Aligned to a single product, service or feature, persona, or user journey
From idea to deployment, as independently as possible
Primary team type of the org
Other team types are there to reduce the burden on steam-aligned teams
Close to the customer, quick to act on feedback
The flow of work is clear and steady
‣
8 Capabilities of a stream aligned team:
Why not a feature team or product team?
Aligning to a stream focuses on flow
Customers interact with brands in many different ways
It can be hard to understand what the responsibilities of a product team are
‣
8 Expected Behaviours
2) Enabling Teams
Composed of specialists in a given technical or product domain
Help bride the capability gap of stream aligned teams to give them more capacity
Enabling teams have the bandwidth to research tools, practices and frameworks
Strongly collaborative - they want to understand and solve problems of stream-aligned teams
Alternative Name: technical consulting teams
Help other teams understand technology constraints in the org
Goal is to increase the autonomy of the stream-aligned teams - by growing their capabilities
Often focused on one of: build engineering, continuous delivery, deployments, test automation
Set up a skeleton → initial examples → work with teams to advise on implementation
Knowledge transfer is likely to be temporary when a new technology is adopted (teams will pair closely in this moment
‣
5 Expected Behaviours
understand needs of stream-aligned teams through regular checkpoints
research and experimentation with new tooling and practices
helps teams understand best practice and avoid mistakes
act as a proxy for any internal or external services which are too difficult for stream-aligned teams to use
curator that facilitates appropriate knowledge sharing
Not a community of practice, but does some of the same things. They work on enabling activities full time
3) Complicated Sub System Teams
Building and maintaining a sub-system tat depends heavily on specialist knowledge
Goal: reduce cognitive load of stream-aligned teams
Capabilities / expertise that is hard to find or grow
Wouldn't be feasible, cost-effective for a stream-aligned team to own that system
Decision driven by cognitive load - not opportunity of a shared component
Expected behaviours
high collaboration with stream-aligned teams
delivery speed and quality is clearly higher that if done by stream-aligned team
Prioritised and delivers work respecting the needs of stream-aligned teams
4) Platform Teams
Enable stream aligned teams to deliver work with autonomy
Stream-aligned teams maintain ownership of building, running and fixing their tech
Provide internal services (reducing cognitive load of stream-aligned teams)
Platform: self-service APIs, tools, services, knowledge and support which are arranged as a compelling internal product.
Autonomous delivery teams can make use of the platform to deliver product features at a higher pace, with reduced coordination
Ease of use is fundamental for platform adoption
Reliable, usable, and fit for purpose
Platforms team value is measured by the value of the services they provide to product teams
Can agree different levels of service for services
Expected Behaviours
Strong collaboration with stream-aligned teams to understand their needs
fast prototyping, fast feedback from other teams
focus on usability and reliability
leads by example, dogfoods
encourages adoption (expects to follow adoption curve)
A platform team can have multiple nested platform teams within it if needed
Don't group functional expertise like UX, Architecture, Data Processing, Database Administration or Testing
That model doesn't work for safe and rapid change.
A good platform is just big enough
Make sure platform teams are serving the needs of their internal customers
Make it easy for internal teams to do things the right way
Thinnest viable platform - can start with a wiki
Platforms generally succeed by reducing the complexity of underlying systems while exposing enough functionality to be useful
Platform teams need to focus on UX and Developer Experience (DevEx)
Should get out of the way of the dev teams
Think about the experience of an new developer in a customer team
Treat the platform as a live production experience
Use Product Management and Service management techniques within platform teams
Have user persona's etc
Move to mostly stream-aligned teams for longevity and flexibility
6/7 or 9/10 teams should be stream-aligned teams
Infrastructure teams → platform teams
Change old component teams to platform teas
Component teams → platform or complicated-subsystem team
Align support teams to streams of change → keeps streams independent, rapid sharing within streams
‣
Types of undesirable systems
Application monolith (single large application with many dependencies and responsibilities)
Joined at the database monolith (single schema - making them hard to change)
Monolithic builds (gigantic continuous integration component to get a new change live)
Monolithic coupled releases (test a shared static environment, QA tests everything as one)
Monolithic Model - enforcing a single domain language across many concepts
Monolithic thinking - one size fits all thinking for teams on technology implementation with a view to minimising variation
Software boundaries or Fracture Planes
Fracture Plane is a natural seam in the system that allows it to be split easily into multiple parts
Try to align boundaries with business domain areas -
Helps with prioritisation, flow and user experience
Most fracture planes should map to a business-domain bounded context (a unit for partitioning a larger system into smaller parts, each of which represents an internally consistent business domain area)
Also known as Domain Driven Design
Aligning technology to business context - reduces mismatches in terminology, everyone is speaking the same language
Types of fracture plane: regulatory compliance, team location, change cadence, risk, performance isolation, technology, user personas/
Part 3: Evolving Team Interactions for Innovation and Rapid Delivery
Team interaction modes, evolve team structures with organisational sensing
Most org design team is done as at a 'point in time' - we should be thinking about how we want them to evolve and change over time
Three core team interaction modes:
Collaboration: working closely together with another team
X-as-a-service: consuming or providing something with minimal collaboration
Facilitating: helping another team(s) to clear impediments
Simplifies interactions between teams
Well-defined interactions are key to effective teams. Helps us assess effectiveness between teams, in turn interfaces are likely to be reflected in software systems too
We want to avoid all teams communicating with all other teams to achieve their goals
What type of interaction should we be having with this other team? Should we be collaborating closely? Should we be expecting or providing a service? Or should we be expecting or providing facilitation?
1) Collaboration
Driver of innovation and rapid discovery but boundary blurring
Suitable when high adaptability or discovery is needed - e.g. exploring new technologies or new techniques
Good for rapid discovery - requires good alignment and high appetite and ability for working together between teams
Bringing together different skill sets to solve a challenge
Overlap between teams can be small or almost total
Teams must take joint responsibility for overall outcomes of their collaboration
Hit in productivity - so should be for something high value, and on a temporary basis
Only do it with one team at a time
Increases innovation and reduces hand-offs
Context sharing, responsibility challenges, reduced output
2) X-as-a-service: Clear responsibilities with predictable delivery but needs good product management
Best when teams need to use a code library, component, API, or Platform that just works without much effort → where that can be effectively provided as a service by another team
Consuming or providing something with minimal collaboration
Requires a high standard of XaaS teams - need to adapt to changing team needs, they need to make the DevEx compelling.
Clarity of ownership and responsibility
Reduced detail/context sharing between teams
Slower innovation of the boundary or API
Danger of reduced flow if the boundary or API is not effective - the service boundary needs to be well chosen
3) Facilitating: Sense and reduce gaps in capabilities
Where one or more teams would benefit from the active help of another team facilitating or coaching some aspect of their work
Facilitating interaction mode is the main interaction mode of enabling teams → providing support and capability to many other teams → helping to enhance the productivity of these other teams
Goal: enable other teams to be more effective, learn more quickly and understand new technology
Goal: to discover and remove common problems or impediments across the teams
Typically interact with many teams - not building but focusing on quality of interactions between other teams that are building and running software
Unblocks stream-aligned teams to increase flow
Requires experienced staff (to not work on building or running things)
The interaction may be unfamiliar or strange to one or both teams involved in facilitation
Associate behaviours to the different interaction modes:
Collaboration mode: high interaction and mutual respect
X-as-a-service: emphasise the user experience
Facilitating mode: help and be helped
How to choose:
Common pairings
Use the reverse Conway maneuver with collaboration and facilitating interactions
Discover effective APIs between teams by deliberate evolution of team topologies
Choose team interaction modes to reduce uncertainty
Choose team interaction modes that enhance flow
Use the collaboration mode to discover viable x-as-a-service interactions
Change the team interaction temporarily to help a team grow experience
Use awkwardness in team interactions to sense missing capabilities and misplaced boundaries
Triggers for evolution of team topologies
Software has grown too large for one team
Delivery cadence is becoming slower
Multiple business services rely on a large set of underlying services
Things to sense:
Have we misunderstood how users need/want to behave?
Do we need to change interaction modes to enhance how the org is working?
Build or by discussions about x thing?
Is the collaboration between two teams still effective? Should we shift modes?
If the flow as smooth as it could be? What hampers flow?
Are the promises between the two teams still valid and achievable?
3 ways of DevOps from (the DevOps Handbook)
Systems thinking: optimise for fast flow across the whole organisation, not just parts
Feedback loops: development informed and guided by operations
Culture of continual experimentation and learning: sensing and feedback for every team interaction
