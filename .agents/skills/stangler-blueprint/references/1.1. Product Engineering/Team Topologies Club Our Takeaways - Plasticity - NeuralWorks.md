---
name: Team Topologies Club: Our Takeaways - Plasticity - NeuralWorks
keywords: (placeholder)
metadata:
  url: https://plasticity.neuralworks.cl/team-topologies-club-our-takeaways/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Team Topologies Club: Our Takeaways
Plasticity
Search Sign In 
Subscribe
Send
Success! Now Check Your Email
To complete Subscribe, click the confirmation link in your inbox. If it doesn't arrive within 3 minutes, check your spam folder.
NeuralWorks LinkedIn Careers
Sign In
NeuralWorks LinkedIn Careers 
Subscribe
Send
Success! Now Check Your Email
To complete Subscribe, click the confirmation link in your inbox. If it doesn't arrive within 3 minutes, check your spam folder.
Team Topologies Club: Our Takeaways
Apr 15, 2025
by
Santiago Allamand Agustín Krebs
Team Topologies Club: Our Takeaways
At NeuralWorks, we explored the book Team Topologies. Turns out, team structure plays a bigger role in software architecture than we thought. 
This post is co-authored by me (Agustín) and Santiago Allamand. Over the past few months, we ran a book club at work where we read and discussed Team Topologies. I'll walk you through why we picked it and what came out of those sessions — while Santiago prepared a full chapter-by-chapter summary, which you'll find at the end in case you want to dive deeper.
From November (2024) to February (2025), we met every Thursday around the end of the workday to talk about the book. As my colleagues (current and past) already know, I'm a big fan of book clubs at work—mostly because they're a low-effort way to build shared knowledge and vocabulary.
More than that, I think reading and discussing together builds long-term critical thinking. After a few technical books, you start noticing how different authors approach similar problems in distinct (sometimes, opposing) ways. That contrast is where the value lives.
A former manager of mine once worried that if a team of junior devs all read the same book, they'd start blindly following its "rules" — even if the industry hasn't reached consensus on them. But I've always seen these books differently: not as dogmas, but as toolkits. If one book says problem X is best solved with approach A and another suggests B, I'd rather know both exist — and choose based on context.
That mindset becomes especially valuable for those of us still building experience. It lets you make decisions with a clearer awareness of alternatives and trade-offs, instead of just copying whatever's popular at the moment.
In short, book clubs help develop judgment — without relying entirely on 1:1 mentorship from more senior staff.
Why this book?
I don't remember exactly how I came across Team Topologies (I think it was briefly mentioned in a client's meeting), but the promise was worth exploring: how to think about team structures in tech environments. In my experience, team setups have always felt like something that just "happens"—people added or removed based on who's available and how urgent a project is. Rarely has it felt like a conscious design decision backed by research or proven practice.
That's why I suggested we read it. Especially since we regularly advise clients not just on the technical side, but on the organizational one too. This felt like a good chance to ground some of those conversations in a bit more evidence—what's worked for other companies, what hasn't.
To be honest, this was the first book I've read that really dives into the impact of team structures on software architecture. Sure, the microservices' philosophy touches on this—small teams per service, etc.—but Team Topologies digs deeper.
The book
Compared to other technical books we've read (e.g., Implementing Domain-Driven Design, by Vernon), Team Topologies is short and manageable: just 8 chapters, and none of them too dense.
That said, it can feel a bit repetitive at times. Some chapters don't add a whole lot beyond what earlier ones already covered. If you're trying to get the core ideas without reading cover to cover, I'd recommend focusing on chapters 1, 5, and 7.
And if you're short on time, here's a summary of the ideas that sparked the most discussion in our sessions—or that we thought were especially worth knowing.
Before continuing: is this book for every tech-team?
No. Team Topologies becomes useful once you're past the early-stage chaos —when your org is no longer just one or two teams doing a bit of everything.
To me, the book starts to make real sense when you have at least:
3 or more delivery teams (ideally stream-aligned, but not necessarily called that yet),
and enough complexity that it becomes useful to separate platform concerns into a dedicated team (tooling, infra, observability, etc.).
At that point, coordination starts to hurt, ownership gets blurry, and you probably have competing priorities across teams. That's when this framework helps — not by prescribing structure, but by giving you a language to navigate and evolve it.
Highlighted topics
Conway's Law
This one pops up right away and stays central to everything that follows. Conway's Law basically says that the way your teams are structured — and how they communicate — ends up shaping your software architecture. That sounds abstract, but it has real consequences. If your communication is messy, your architecture probably will be too.
We liked how the book framed this not just as a warning, but as a tool: you can actually flip Conway's Law around. Want a more modular architecture? Reorganize your teams to reflect that. It's not magic, but it's a useful lever.
One important thing to call out: this whole book only makes sense if you buy into Conway's Law — or at least find it mostly true in your own experience. For us, it checks out. We've seen team structure ripple into code structure more times than we can count. So if you're not on board with that idea, the rest of the book might not land as strongly.
Collaboration Isn't Always a Good Thing
One of the more controversial — but useful — ideas in the book is that collaboration isn't always the answer. It's easy to assume that the more teams work together, the better. But strong collaboration comes at a cost: more meetings, more alignment, more shared ownership… and often, more confusion.
The book argues that collaboration is great during the early discovery phase of a project — when teams are still figuring things out, exploring new ideas, or building shared context. But once the path is clearer, it's usually better to tighten responsibilities and reduce collaboration. That means defining clearer boundaries, limiting coordination, and letting each team move faster on its own.
To us, it's a bit like inviting people to a meeting: at the beginning, you might want lots of voices in the room. Later, you want only the people who'll actually make the call.
In other words, too much collaboration can slow you down — especially if no one's sure who's actually in charge of what.
Think in team-sized units
Team Topologies puts a big emphasis on what they call "team-first thinking." The core idea is that teams should be the basic building blocks of your org — not just individuals floating around.
They reference Dunbar's number to explain why: people can only maintain so many close relationships. So when your team size balloons past a certain point, things start to break down. The book suggests keeping core delivery teams to around 5–9 people, and being mindful of how many people are grouped together across the org.
The Four Team Types
One of the most memorable ideas in the book is its four team "topologies" — essentially, templates for how teams can be structured and interact.
Here's the short version:
Stream-aligned teams focus on a specific area of value (like a product or service). They're meant to be autonomous and fast-moving, and usually include a mix of technical roles.
Platform teams exist to support stream-aligned teams with tools, infrastructure, and shared capabilities — so they don't have to reinvent the wheel. Their users are not the business, but the internal teams.
Enabling teams act as internal coaches or consultants, helping stream-aligned teams adopt new technologies or practices of the platform teams. They usually engage for a limited time, unblock a capability, and move on.
Complicated-subsystem teams handle highly specialized parts of the system that require deep expertise — things like algorithmic trading engines, video encoding, or pricing optimizers.
The book doesn't hedge here: it claims that every team in a tech org should fall into one of these four types. It's a strong statement — but as we read it, we couldn't come up with quick counterexamples.
It was helpful for us to map the teams we've worked with (ours and our clients') against this model. In cases where a team didn't clearly fit one of the types, it often pointed to a deeper issue — like unclear ownership, duplicated responsibilities, or under-defined scope.
Watch out for hidden monoliths
We also spent time on what the book calls "hidden monoliths" — systems that look modular on the surface, but are so tightly coupled underneath that any change requires updates across the board. We've definitely seen this in the wild.
The takeaway was: designing good boundaries isn't just about code — it's about who owns what, and whether teams can actually move independently.
Fracture Planes: More Than Just Domain Boundaries
This was a new term for most of us, but the idea felt intuitive: fracture planes are natural places to split your system so teams can take clear ownership. What's interesting is that the book goes way beyond the usual suspects like product or domain boundaries (which you often see in microservices or DDD discussions).
Instead, it offers a wider range of options — from technical layers to compliance needs, performance constraints, even team geography. The goal is to reduce friction, not to obsess over some “perfect” design.
A quick note here on terminology: the book talks a lot about stream-aligned teams. A “stream” refers to a flow of change — like a product, feature set, user journey, or business capability. So a stream-aligned team is one that's aligned with delivering that flow end-to-end, with the focus on not depending too much on others.
Fracture planes help you design boundaries so these teams can actually operate that way — independently, with clear scope and ownership.
Three Ways Teams Can Interact
Once you've mapped your teams and decided on their type, the book introduces three default interaction modes between them:
Collaboration — when two teams work closely together to figure something out. This is common in the early phase of a project, when there's still a lot of uncertainty.
X-as-a-Service — when one team provides something (like a tool, API, or platform) that others can use with minimal back-and-forth. This tends to come later, once things are more stable.
Facilitating — when one team helps another learn, unblock something, or adopt a new practice.
This is one of those things you don't usually think about when designing software architecture: not just who owns what, but how teams should work together. The default approach tends to be: "let them figure it out." But that often leads to fuzzy responsibilities and slow delivery.
The authors argue it's better to be explicit: define the mode of interaction up front, and don't be afraid to switch modes as the work evolves.
When to rethink your team structure
Finally, the book lists some signs that it might be time to change how teams are organized. These felt very familiar:
Your product has grown too big for one team to manage.
One team becomes a bottleneck for others.
Changes take longer than they used to.
People complain about unclear ownership or poor documentation.
Everyone's always waiting on the same few people.
We realized during our sessions that we'd seen most of these play out in our past projects — and hadn't always recognized them as signals.
Detailed Chapter-by-Chapter Summary
If you're curious to go deeper, Santiago put together a full chapter-by-chapter breakdown — summarized below, with just enough detail to get the gist (or decide what to read first).
Chapter 1. The Problem of Organizational Mapping
Key Ideas of the Chapter
Conway's Law suggests great benefits when designing software architectures and team interactions together, as they are similar forces.
Team Topologies clarifies the purpose and responsibilities of teams, increasing the effectiveness of their interrelationships.
Team Topologies takes a humanistic approach to building software systems while preparing organizations for strategic adaptability.
Detailed Summary
Software development with rapid delivery for modern interconnected systems and services requires organizations to consider multiple dimensions. Historically, many companies have approached software development as a manufacturing process, assigning tasks to individuals in specialized roles (reflected in an organizational map or matrix), with large projects planned from the outset and little attention to communication dynamics.
This has resulted in them failing to create the necessary conditions for innovation while at the same time making rapid delivery.
Part of the problem is that organizational maps tend to imply that communication goes in a vertical direction, in circumstances where people do not really limit their communication only upward or downward.
Main Idea
Team Topologies brings a new perspective on how to effectively structure teams for enterprise software delivery. It provides a coherent and practical guide to evolve the design of teams, helping them to continuously adapt to changes in technology, people, and business. This includes aspects such as:
size
shape
location
responsibilities
boundaries
interactions
of the teams that build and operate modern software systems.
Four Fundamental Types of Teams (explored in the rest of the book)
Stream-aligned — focused on a specific workflow
Platform — providing reusable services
Enabling — helping other teams to improve their capabilities
Complicated-subsystem — handling highly specialized or complex areas
Three Main Modes of Interaction Between Teams
Collaboration
X-as-a-Service (services offered as a product)
Facilitation
Combining these elements with an understanding of:
Conway's Law
Cognitive load of teams
How to become a sensing organization
Team Topologies proposes an effective and humanistic approach to building and operating modern software systems.
Conway's Law (Origin)
In 1968, Mel Conway published in a magazine called Datamation a paper titled "How do Committees Invent?", where this sentence became known as Conway's Law:
"Organizations that design systems... are limited to produce designs that are copies of the communication structures of these organizations."
Cognitive Load
When we talk about cognitive load, it is easy to understand that any person has a limit on the amount of information they can process at any given time.
The same is true for teams, simply by adding up the cognitive capacities of all team members.
If cognitive load is not considered, teams are overburdened by trying to cover an excessive amount of responsibilities and domains.
A team in this situation lacks the ability to focus on achieving mastery in its area and faces difficulties due to the costs associated with constant context switching.
Chapter 2. Conway's Law and Why It Matters
Key Ideas of the Chapter
Organizations are limited to producing designs that reflect existing communication paths.
The organization's design restricts the "solution search space," limiting the possible software designs.
Demanding that everyone communicate with everyone is a recipe for chaos.
It is better to opt for software architectures that encourage a team-focused flow.
Restricting communication paths to well-defined interactions between teams results in modular and decoupled systems.
Detailed Summary
This quote from Ruth Malan provides what could be considered the modern version of Conway's Law:"If the system architecture and the organization architecture are in conflict, the organization architecture prevails."
In particular, an organization structured in functional silos (where teams specialize in a specific function, such as QA, DBA, or security) is unlikely to succeed in producing well-designed software systems for end-to-end flow. Similarly, an organization organized primarily around sales channels for different geographic regions is unlikely to produce an effective software architecture that delivers multiple software services to all global regions.
Why? Because the communication pathways (whether through formal reporting lines or not) within an organization effectively restrict the types of solutions the organization can develop.
Main Idea: The Reverse Conway Maneuver
The Reverse Conway Maneuver gained popularity in the technology world around 2015 and has since been applied in many organizations. The book Accelerate: The Science of DevOps by Nicole Forsgren, PhD, Jez Humble, and Gene Kim supports the importance of this strategy for high-performing organizations:"Our research supports what is sometimes called the 'reverse Conway maneuver,' which states that organizations should evolve their team and organizational structure to achieve the desired architecture. The goal is for your architecture to support the ability of teams to do their work, from design to deployment, without requiring high-intensity communication between teams."
Example: Suppose we want to implement a microservices architecture for a new cloud-based software system, where each service is independent and has its own data store.
By applying Conway's reverse maneuver, we can design our teams to align with the required software architecture. This is achieved by assigning separate developers for client applications and APIs, and integrating a database developer within the team rather than keeping it as a separate role (see Figure 2.4, page 22).
To achieve a safe and fast flow of change, it is essential to consider team-focused flow and design the software architecture to match it. The team is the fundamental delivery medium (see more in Chapter 3), so the system architecture must enable and encourage fast flow within each team.
Fortunately, in practice, this involves following proven software architecture best practices:
Weak coupling: components must not have strong dependencies with each other.
High cohesion: components must have clearly delimited responsibilities, and their internal elements must be closely related.
Clear and adequate version compatibility: ensure that changes to one component do not disrupt other components.
Clear and adequate inter-team testing: ensure that interactions between teams are tested in an effective and controlled manner.
Focused Communication Over Communication Overload
Main idea: A key implication of Conway's Law is that not all communication and collaboration is beneficial.
It is critical to define "team interfaces" to set clear expectations about what type of work requires close collaboration and what does not.
Many organizations assume that more communication is always better, but this is not really the case.
What is needed is focused communication between specific teams, ensuring that interactions are efficient and productive rather than becoming unnecessary overload.
This can be achieved by restricting communication through simple interventions such as:
Moving teams to different physical locations
Limiting messaging applications
If everyone talks to everyone, you end up creating monolithic systems that are undesirable.
Common Errors in the Application of Conway's Law
Mismatch between the responsibility limits of the teams or departments and the responsibility limits of the tools.
Too many different component kits
Frequent reorganizations that create fiefdoms or reduce the number of people
Chapter 3. Team-First Thinking
Key Ideas of the Chapter
The team is the most effective medium for software delivery, not individuals.
Limit the size of multiple team groupings within the organization, based on Dunbar's number.
Restrict team responsibilities to match the maximum cognitive load they can handle.
Establish clear boundaries of responsibility for each team.
Modify the team's work environment to facilitate its success.
Detailed Summary
The team is the most effective means of software delivery, not individuals.An ideal group has between 5 to 9 people who share a common goal as a unit.For example, Amazon talks about the 2-pizza team (7 to 9 people).
Main Idea: Dunbar's Number and Group Size Limits
This limit, recommended by popular frameworks like Scrum, stems from evolutionary limits on recognition and trust within a group, known as Dunbar's number (named after anthropologist Robin Dunbar).
Dunbar determined that 15 is the maximum number of people a person can deeply trust, and of those, only about 5 can be trusted closely.
Teams need trust to operate effectively. If the group size grows too large, that trust is harder to maintain, which leads to reduced effectiveness.
Therefore, to ensure predictable behavior and interactions, team groupings should be sized as follows:
A single team: ~5 to 8 people (depending on experience)
In high-trust organizations: no more than 15 people
Families ("tribes"): groupings of teams with a maximum of 50 people
In high-trust organizations: groupings of no more than 150 people
Divisions / work streams / P&L lines: no more than 150–500 people
When these limits are reached, groupings should be split into semi-independent units to maintain trust and efficiency.
It typically takes 2 weeks to 3 months for a team to become cohesive.
Main Idea: Exclusive Software Ownership
Each team should own the software:Each part of the system must be the exclusive property of a single team.
There should be no shared ownership of components, libraries, or code.
Teams may use shared services at runtime, but:
Each running service, application, or subsystem must be owned by a single team.
External teams may submit pull requests or suggestions, but not modify code directly.
Main Idea: Prioritize the Team over the Individual
For teams to work effectively, team members must prioritize the team's needs over their own.
They should:
Arrive on time for meetings
Keep discussions and research focused and aligned with objectives
Encourage focus on team goals
Help unblock teammates before starting new work
Mentor newer or less experienced members
Avoid "winning" discussions — be open to exploring alternatives
Organizations should also:
Seek diversity in teams
Reward whole teams, not individuals
Create clear boundaries to reduce cognitive load
Measure cognitive load using relative domain complexity:
Limit one complex domain per team
Or 2–3 simple domains
Main Idea: Design "Team APIs" to Facilitate Interaction
Stable, long-term teams with clear responsibilities can define a "Team API" — a structured way for other teams to interact with them. This includes:
Code: runtime access points, libraries, clients, UIs, etc.
Versioning: e.g., using SemVer to communicate changes and maintain compatibility
Wiki and documentation: guides and docs for the software
Practices and principles: the team's preferred ways of working
Communication: norms for remote tools like chat or video
Work information: what the team is doing now, next, and their current priorities
Other aspects: anything needed to interact effectively with the team
The usability of the team's API should be an explicit priority to enable smooth collaboration.
Office Design for Effective Software Delivery
Effective workspace design supports different work modes:
Focused individual work: quiet spaces for deep work
Collaborative work within the team: small meeting rooms or team tables
Collaborative work between teams: flexible open spaces for inter-team interaction
A balanced design should support smooth transitions between modes, encouraging both individual productivity and effective collaboration.
Chapter 4. Static Team Topologies
Key Ideas of the Chapter
Improvised or constantly changing team design slows down software delivery.
There is no single definitive team topology, but there are several topologies that are inappropriate for an organization.
Key aspects in choosing a topology include technical and cultural maturity, organizational scale, and engineering discipline.
The pattern of feature- or product-focused teams is powerful — but only with the right support environment.
Dividing a team's responsibilities can dismantle silos and empower other teams.
Detailed Summary
Some patterns that go against Conway's Law include:
Designing ad hoc teams without considering communication
Frequently "switching and mixing" team members without stability
Main Idea: Design for the Flow of Change
Spotify is an excellent example of intentional organizational design to improve effectiveness in software delivery and operations.As described by Henrik Kniberg and Anders Ivarsson in their 2012 blog post "Scaling Agile @ Spotify", this approach includes:
Squads: Small, autonomous, cross-functional teams of ~5 to 9 people with long-term missions
Tribes: Affinity groupings of squads working in similar areas
Chapters: Groups of people with similar skills (e.g., all testers across squads), sharing practices and managed by a chapter lead who is also hands-on in day-to-day work
Guilds: Communities of practice that span across squads, chapters, and tribes, helping maintain shared knowledge and culture
"Chapters and guilds are the glue that holds the company together, providing economies of scale without sacrificing too much autonomy."
However, many organizations have blindly copied Spotify's model without understanding its underlying culture and purpose, leading to poor results.
Instead of moving from "Dev" → "Test" → "Transition" → "Live", organizations should organize around workflows.
Main Idea: Avoid the "Wall of Confusion"
The classic anti-pattern in team design was to completely separate development (Dev) and operations (Ops).
Dev teams would "throw software over the wall" to Ops teams, who had minimal context and limited communication (typically via tickets).
This created inefficiencies and frustration, known in the DevOps world as the "wall of confusion."
The DevOps movement emerged around 2009 to address this friction, driven by:
The rise of Agile
Increased deployment pressure on Ops teams
A need for collaboration, automation, and alignment between Dev and Ops
DevOps Topologies Catalog
Originally created by Matthew Skelton in 2013 and expanded by Manuel Pais, this catalog is a helpful online resource of:
Patterns and anti-patterns for team design and interactions
A great starting point for conversations around team responsibilities, interfaces, and collaboration
Patterns of Successful Teams
Feature or functionality teams require high engineering maturity and confidence
Product teams need a robust support system
Cloud teams should not create infrastructure per application — they should build self-service platforms
Anti-Pattern: The "DevOps Team"
In theory, having a DevOps team with automation expertise makes sense.
In practice, this often becomes a rigid bottleneck if the team ends up manually executing delivery steps for each application.
Instead, they should focus on enabling self-service capabilities for application teams.
Main Idea: SRE Only Makes Sense When You're Already Big
Site Reliability Engineering (SRE) — pioneered by Google — is:
A distinct approach to operating and improving large-scale applications
Based on concepts like error budgets (acceptable levels of downtime)
Involves SRE teams having the authority to reject poor quality software
SRE is not a good fit for smaller or immature organizations.
Main Idea: Considerations When Selecting a Topology
Key factors to evaluate include:
Technical and cultural maturity of the organization
Size and scale of the org and its software
Engineering maturity
Dividing responsibilities to break down silos
Dependencies and waiting times between teams
Chapter 5. The 4 Fundamental "Team Topologies"
Key Ideas of the Chapter
The four fundamental team topologies simplify interactions in modern software organizations.
Mapping common industry team types to these fundamental topologies helps eliminate gray areas and prevent overloaded or underutilized teams.
The 4 topologies are:
The main topology is stream-aligned — all others support it.
Enabling teams
Complicated-subsystem teams
Platform teams
Topologies are often fractal: teams within teams.
Main Idea: The 4 Fundamental Typologies
This chapter introduces the four fundamental team types (or “topologies”) that should form the building blocks of a modern software organization. The authors argue that clearly defining these types helps reduce friction, misalignment, and inefficiencies caused by ambiguous or overly general team structures.
Stream-Aligned Team A stream (or business flow) is the continuous flow of work aligned to a business domain or capability. A stream-aligned team is aligned to a single, valuable workflow, which could be:
A product or service
A set of functionalities
A user journey
A user persona
Enabling Team Specialists in a specific technical or product domain, enabling teams:
Help close capability gaps
Operate transversally to stream-aligned teams
Have bandwidth to research, test, and recommend tools, practices, and frameworks
Aim to increase the autonomy of stream-aligned teams by focusing first on their problems
Complicated-Subsystem Team Responsible for parts of the system that require deep specialized knowledge. Most team members are experts in the area. Example subsystems:
Video processing codecs
Mathematical models
Real-time transaction algorithms
Financial reporting systems
Facial recognition engines
Platform Team Helps stream-aligned teams deliver with high autonomy by providing:
Internal services
Reduced cognitive load
Programmable APIs or web portalsThese services allow teams to build, operate, and remediate their applications independently.
Within platforms, nested teams or "inner topologies" may exist. As James Womak and Daniel Jones describe, a product line manager may coordinate multiple value stream managers at different levels.
Main Idea: Capabilities and Behaviors by Team Type
A. Stream-Aligned Team
Continuous delivery of features or functionality
Rapid correction based on feedback
Experimental approach to product evolution
Minimal work handoffs
Evaluated on sustainable flow, support, and team health
Dedicated time to improve code quality ("technical debt")
Proactive interaction with support topology teams
A sense of autonomy, mastery, and purpose (Daniel Pink)
B. Enabling Team
Proactively understands needs of stream-aligned teams
Stays ahead on tools, practices, and approaches
Acts as a messenger for both good and bad tech news
Acts as a proxy for complex external/internal services
Promotes learning and acts as a knowledge curator
C. Complicated-Subsystem Team
Adapts collaboration based on subsystem development stage:
High collaboration during exploration
Lower interaction after stabilization
Improves speed and quality compared to stream-aligned teams
Prioritizes needs of dependent teams appropriately
D. Platform Team
Strong collaboration with stream-aligned teams
Uses rapid prototyping and agile feedback loops
Prioritizes usability and reliability — treats platform as a product
Leads by example and uses internal services where applicable
Understands adoption evolves along a curve
Transforming Common Teams to Fundamental Topologies
The authors suggest reframing traditional team types as one of the fundamental Team Topologies:
Infrastructure teams → Platform teams
Tool teams → Enabling teams or part of the Platform
Support teams → Embedded in Stream-Aligned teams
Chapter 6. Choosing Boundaries "Team First"
Key Ideas of the Chapter
Select software boundaries using a team-centric approach.
Beware of hidden monoliths and coupling in the software delivery chain.
Define software boundaries according to the bounded contexts of the business domain.
Consider alternative boundaries where necessary and appropriate.
Detailed Summary
To achieve a rapid flow of change in software systems, it's necessary to:
Eliminate inter-team handoffs
Align most teams with major change flows in the organization
Main Idea: The Problem of Unclear Boundaries
Many software delivery problems arise from unclear team boundaries and responsibilities.This often results in architectures with high coupling, even when designed to be modular — a phenomenon explained by Conway's Law.
Such systems are commonly known as "monoliths".
Hidden Monoliths to Avoid
Monolith Application
Joined-at-the-Database Monolith
Monolithic Builds (rebuild everything)
Monolithic (Coupled) Releases
Monolithic Model (single view of the world)
Monolithic Thinking (over-standardization)
Monolithic Workplace (open-plan office without functional separation)
Main Idea: Software Boundaries as "Fracture Planes"
While monoliths have downsides, there are also risks in how we split software between teams.The concept of a fracture plane helps guide natural and effective software division.
A fracture plane is a natural seam in the system that allows it to be cleanly split into separate parts — especially useful when breaking down monolithic systems.
Whenever possible, align fracture planes with domain boundaries in the business.
Key Fracture Planes to Consider
Bounded Contexts of the Business Domain Divide the system by distinct business areas and capabilities.
Regulatory Compliance Separate components to meet specific compliance requirements.
Rate of Change Isolate parts of the system that evolve at different speeds.
Team Location Align software divisions with the geographical distribution of responsible teams.
Risk Exposure Separate components based on criticality and risk levels.
Performance Isolation Prevent performance issues in one part from degrading others.
Technology Stack Divide components by the different technologies used (e.g., Java vs. Python).
User Personas Align boundaries with distinct user groups and their specific needs.
Chapter 7. Modes of Interaction Between Teams
Key Ideas of the Chapter
Choose specific modes of interaction between teams to improve software delivery.
Select from three modes: collaboration, X-as-a-Service, and facilitation — each helps teams provide and evolve services for others.
Collaboration drives innovation but can slow delivery.
X-as-a-Service enables speed but requires clear boundaries.
Facilitation helps detect and solve challenges across teams.
Detailed Summary
In many organizations, poorly defined team interactions and responsibilities are a major source of friction and inefficiency.
Main Idea: The Three Essential Modes of Team Interaction
Taking into account team-centered dynamics and Conway's Law, teams should interact through one of the following clearly defined modes:
Collaboration Teams work closely together toward a shared goal. Ideal when adaptability or discovery is needed — such as exploring new tech or experimenting with design ideas. Helps avoid costly handoffs and speeds up innovation.
X-as-a-Service A team provides or consumes a service with minimal interaction, typically via a defined API, library, or tool. Ensures low cognitive load and clear responsibility boundaries.
Facilitation One team helps another team solve problems or unlock capabilities. Common for enabling teams that help stream-aligned or platform teams gain skills or adopt new practices.
A combination of all three modes is typically required in medium to large organizations — and even smaller companies can benefit from introducing these patterns early.
Collaboration Mode
Advantages:
Enables rapid innovation and discovery
Reduces handoffs between teams
Disadvantages:
Shared responsibilities increase cognitive load
Requires more context and coordination
May lead to reduced productivity during collaboration
Restriction:
A team should collaborate with only one other team at a time
Typical Uses:
Stream-aligned teams working with complicated-subsystem teams
Stream-aligned teams working with platform teams
Complicated-subsystem teams working with platform teams
X-as-a-Service Mode
Advantages:
Clear ownership and defined service boundaries
Lower cognitive overhead — minimal context sharing required
Disadvantages:
Slower innovation at API/service boundaries
Risk of reduced delivery speed if APIs are poorly designed
Restriction:
A team must be ready to consume or provide services to many other teams simultaneously
Typical Uses:
Stream-aligned or complicated-subsystem teams consuming services from a platform team
Any team consuming a library or component from a complicated-subsystem team
Facilitation Mode
Advantages:
Helps unblock teams, enabling better flow
Identifies misaligned capabilities and component gaps
Disadvantages:
Requires experienced people not focused on day-to-day delivery
Interaction may feel foreign or unusual to some teams
Restriction:
A team should facilitate only a small number of teams at once
Typical Uses:
An enabling team helping a stream-aligned, platform, or complicated-subsystem team
A stream-aligned or platform team helping another stream-aligned team
Chapter 8. Evolve Team Structures Using "Organizational Sensing"
Key Ideas of the Chapter
Use different team topologies simultaneously for strategic advantage.
Evolve team topologies and interactions to accelerate the adoption of new approaches.
Differentiate between explore, exploit, sustain, and withdraw phases using team topologies.
Expect multiple team topologies to coexist to meet diverse needs.
Recognize triggers for organizational change.
Treat operations as high-fidelity sensory input for self-management.
Detailed Summary
Collaboration is ideal for rapid discovery and avoiding handoffs or delays, but comes at the cost of increased cognitive load.In contrast, X-as-a-Service offers clarity of responsibility, reducing the need for coordination.
Main Idea: Modes of Interaction Should Evolve Over Time
The modes of team interaction — collaboration, X-as-a-Service, and facilitation— are not static. They should evolve based on the goals and current phase of team work.
When a team needs to explore new parts of the tech stack or domain:
Use collaboration mode with the owning team, for a defined period.
Once new approaches have been discovered and stability is needed:
Shift to X-as-a-Service mode to formalize the interface and responsibilities between teams.
Organizations should aim to move from discovery to predictable delivery as services and platforms mature and become commoditized.
Main Idea: Organizational Triggers for Restructuring Teams
Certain events or trends in software delivery indicate the need to rethink team structures:
Trigger: The software has become too big for a single team to manage.
Trigger: The pace of delivery is slowing down — signaling too much cognitive load, unclear responsibilities, or inefficient workflows.
Trigger: Multiple business services depend on a large, entangled set of underlying services — requiring clearer ownership and modularization.
By treating operations as sensory input, organizations can use these signals to self-manage and adapt, ensuring the team structures and interaction modes remain aligned with current delivery needs and strategic direction.
Chapter 9. Conclusion: The Next Generation Digital Operating Model
Key Ideas of the Chapter
This chapter synthesizes the core ideas of the book into a coherent, next-generation digital operating model, grounded in a team-centric philosophy and built upon the following principles and tools:
A team-focused approach to software delivery and operations
Application of Conway's Law to align communication and architecture
Use of the four fundamental team topologies
Explicit modes of interaction between teams
Evolution of team topologies over time
Leveraging an organizational sensory system to adapt and self-manage
Where to Start: A Practical Approach
Start with the teams Focus on shaping the right team structures and responsibilities.
Identify workflows Understand and map the flow of work that delivers value across the organization.
Define the thinnest minimum viable platform Provide just enough platform to support stream-aligned teams while avoiding unnecessary complexity.
Identify capability gaps Recognize where teams lack the expertise or resources needed and introduce enabling or platform teams to fill those gaps.
Practice interactions between teams Foster the right modes of collaboration, service consumption, and facilitation to strengthen team effectiveness and autonomy.
By combining these elements, organizations can create a flexible, resilient, and adaptive operating model that empowers teams, accelerates delivery, and supports sustainable software development at scale.
by
Santiago Allamand Agustín Krebs
Published Apr 15, 2025    
Plasticity Direct to Your Inbox
Subscribe (zero spam, we promise). Fresh takes on Tech, data, and AI.
Send
Success! Now Check Your Email
To complete Subscribe, click the confirmation link in your inbox. If it doesn't arrive within 3 minutes, check your spam folder.
Read Next
The End of Apps: Why AI Agents Will Replace Software Interfaces
AI is pushing software away from interface-first navigation and toward outcome-driven execution. The shift is not just about chatting with machines. It is about delegating work to systems that can reason, coordinate, and act.
Mar 30, 2026
by Hermon Alfaro
No API? No Problem: A Framework for Extracting Data from Any Website.
Most tutorials show you how to scrape public pages. This one covers the hard kind — login portals, bot detection, cross-origin iframes, and modal nightmares — with a Playwright framework that actually runs in production.
Mar 06, 2026
by Santiago Maass Gangler
Building Data Governance from Zero: A Practical Journey in Large Organizations
Centralized processes, federated ownership, scalable solutions
Jan 29, 2026
by Vicente Vega
Plasticity
The NeuralWorks Blog — Thoughts, stories and ideas.
NeuralWorks LinkedIn Careers
Copyright © 2026 Plasticity . Published with Ghost and Plasticity .
