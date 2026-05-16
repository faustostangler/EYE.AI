---
name: Team Topologies - ralphmayr.com
keywords: (placeholder)
metadata:
  url: https://ralphmayr.com/posts/2020-02-22-team-topologies/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
ralphmayr.com :: Team Topologies
ralph mayr .com r m
Blog
Library
Contact
Saturday, February 22, 2020
Team Topologies
In many instances software architecture is less a product of deliberate design and more an accidental result of countless interactions between people. Or, as Eric Raymond put it more pointedly:
“If you have four groups working on a compiler, you'll get a 4-pass compiler.” 
How Do Committees Invent? by Mel Conway.
This idea was originally introduced by Mel Conway in his 1967 paper “How Do Committees Invent?” and has since turned into what is now known as Conway's Law:
“Organizations which design systems […] are constrained to produce designs which are copies of the communication structures of these organizations.” 
Team Topologies by Matthew Skelton and Manuel Pais.
It's easy to see Conway's Law as something inherently negative: It reminds us how limited large organizations really are, their ability to innovate and deliver value always hindered by their internal structures and processes. But in the 2019 book Team Topologies, Matthew Skelton and Manuel Pais assume a more positive outlook: They argue that we should see Conway's Law as an invitation to redesign our organizations so that they will—more or less automatically—produce the system architectures we want them to produce.
This approach has been called the Inverse Conway Maneuver and has been used for a while by companies wise enough to realize the implications of Conway's Law. Skelton and Pais take it as the basis for a framework for organizational design they call Team Topologies which, in their view, will help its users to avoid some of the design flaws still prevalent in many software systems today.
Team-first
The Team Topologies approach is based on a few assumptions that can be summed up under the umbrella term team first:
(1) Teams (not individuals) should be the fundamental building blocks of organizations. While great individual contributors can generate outstanding results at times, they also turn into single-points of failure easily. It is therefore essential to spread knowledge and responsibilities within the team and to make sure that the organization assigns work to the team and not to individual team members.
(2) Teams have limited cognitive capacity. The reason why we need more than one team in the first place is that specialization is what enables companies to scale. A single team can and should only work on a limited number of different tasks or types of tasks. If a team is spread too thin over a variety of seemingly unrelated assignments, team members easily get lost in the inefficiencies of task switching and may never develop a sense of purpose.
Note that this is not an invitation to create siloed teams along functional boundaries such as development, testing, database administration, and so on. Rather, those functions should all be present within a dedicated team that together works on a particular piece of functionality, rather than an unrelated set of issues.
(3) Not all communication between teams is helpful and desirable. People often assume that more communication between teams is always better, but Skelton and Pais argue that this is not necessarily the case. Instead, too much unstructured interaction can point out unintended dependencies, highlight badly designed APIs, and can distract teams from doing their primary work.
(4) Teams should have well-defined interfaces to other teams. The authors introduce the concept of the team API, a documented set of interactions with the outside world that the team finds helpful and productive. For example, some teams may prefer to have all requests funneled to them via tickets in an issue tracking system while others require a dedicated product owner or product manager to triage, prioritize, and negotiate incoming tasks. Some will want to be contacted via instant messaging tools, others via e-mail or phone. The point is: Teams should have the freedom—within limits, of course—to decide how they want to be accessible for other teams and the responsibility to communicate their preferences clearly. Just like each component in a distributed systems needs has to have a clear, consistent, and stable API that other components can interact with it, so should teams in a large organization.
Team types and interactions
Based on team-first thinking, the authors argue that organizations should limit themselves to having just four different types of teams which interact with each other using distinct interaction models, rather than unstructured ad-hoc communication. They acknowledge that in practice this isn't always possible but that it's nevertheless a goal worth aiming for.
Team type #1: Stream-Aligned
Joao Branco
A stream-aligned team is one that delivers value to the business. In a product organization, a stream-aligned team can own either an entire product, or a specific piece of functionality within a larger product. Important to note is that the stream-aligned team has to be in a position to deliver increments of value autonomously, without depending on other teams. Therefore, stream-aligned teams need to be staffed with cross-functional capabilities so that they can discover, build, test, and operate independently. The opposite of this setup would be the traditional frontend/backend/database silos that are still prevalent in some product organizations, or the development/testing/operations split.
The primary purpose of the other team types is to support the stream-aligned teams by removing impediments, making sure the stream-aligned teams can focus on value-generating work. According to Skelton and Pais, the vast majority of teams in an organization should be stream-aligned, going so far as to argue that not more than one in seven teams should be of any of the other types.
Team type #2: Platform
Tolu Olubode
Platform teams don't directly create business value, but provide services that the make the lives of stream-aligned teams easier. For example, a platform team can be responsible for providing infrastructure on top of which the stream-aligned teams run their products, or it can build a self-service system that the stream-aligned teams use to access build and test environments on demand.
Stream-aligned teams and platform teams should ideally not collaborate all the time, as collaboration binds resources and requires synchronization, and hence doesn't scale well. Instead, those teams should adopt an x-as-a-service interaction model whereby the platform team provides its services in a way that the stream-aligned teams can consume on demand without the need for explicit communication every time the service is used.
Of course, some collaboration is necessary and desired when a new service is introduced, but it's important in the authors' view that those times of close interaction are limited, and scoped to a particular outcome.
Team type #3: Enabling
Charles Deluvio
If stream-aligned teams are the one's working on end-to-end value creation, they should be freed from as many non value-generating tasks as possible. Therefore Skelton and Pais introduce the enabling team type to further assist stream-aligned teams by providing services such as trainings or specialized expertise.
Many organizations have already formed enabling teams when they introduced “Centers of Excellence” (CoE) around topics such as functional testing or user experience. A typical CoE for performance engineering for example has in-depth expertise around measuring and optimizing user experience by lowering latency and response times, which not every stream-aligned team requires all the time, but which it is still handy to have access to when the need arises.
Ideally, stream-aligned teams consult enabling teams occasionally, followed by a limited period of close collaboration during which the stream-aligned team adopts knowledge and learns new skills. After that, the stream-aligned team should no longer depend on the enabling team. The authors call this interaction model facilitating and point out that there are countless uses for it, ranging from sharing organizational best practices such as agile development, to spreading know-how in emerging technologies like machine learning or containerization.
Team type #4: Complicated-subsystem
Peter Gauster
The complicated-subsystem team type is a bit of an exception: The authors introduce it for the sole reason that sometimes specific areas of a product require such specialized expertise that no single stream-aligned team can take full ownership for them while at the same time delivering end-to-end value. Complicated-subsystem teams can help out here, taking on the role of a more traditional “component team”: A team that owns a complex part of the overall system which is not a self-sufficient driver for value creation. Think of a complex image recognition algorithm on top of which stream-aligned teams build customer-facing products for example, or a legacy system that requires highly specialized expertise.
The interaction between complicated-subsystem teams and others is… well, complicated. Stream-aligned teams will need to collaborate with complicated-subsystem teams regularly, but there will also be some facilitating going on. Ideally, organizations can turn their complicated subsystems into platforms over time, so that the stream-aligned teams can use them via the x-as-a-service interaction model rather than through ongoing collaboration. Of course, complicated-subsystem teams themselves can leverage the services provided by other teams of the enabling and platform team types.
Summary & opinion
The gist of Team Topologies can be summed up quite briefly: Four types of teams ( stream-aligned, platform, enabling, and complicated-subsystem), and three types of interactions ( collaboration, x-as-a-service, and facilitating) are all an organization needs to design, build and operate better software.
If that sounds too good to be true to you, I won't disagree. And probably, neither will the authors of Team Topologies. In my view it's important to take the book not as a literal recipe for how to build the perfect software delivery organization, but rather as a set of ideals organizations should aim to gravitate towards if they want to avoid some of the common pitfalls posed by Conway's Law.
It can definitely be helpful to question which types of teams one's organization currently has, how they interact, and which incremental changes would be desirable and feasible. Such a conscious review is only possible when one has the language to put the status quo and the envisioned end goal into words, and in this regard Skelton and Pais have done a great job.
The book furthermore is sprinkled with anecdotes from companies the authors have consulted with, and those highlight the advantages their approach has on the one hand, but also remind us that changing structures that have grown over time requires effort and dedication. Things are a lot messier in practice than in theory, but that doesn't mean that the theory in itself doesn't have value.
⟵ Home
Related content
On Tenuous Ground
Peak Mind
Product Roadmaps Relaunched
AI Superpowers
Empowered
The Right It
Designing Your Work Life
Guns, Germs, and Steel
Range
On Better Questions        
© Ralph Mayr 2026 · Impressum       
