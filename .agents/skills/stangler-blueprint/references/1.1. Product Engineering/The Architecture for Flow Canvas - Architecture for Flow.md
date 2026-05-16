---
name: The Architecture for Flow Canvas - Architecture for Flow
keywords: (placeholder)
metadata:
  url: https://architectureforflow.com/canvas/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
The Architecture for Flow Canvas - Architecture for Flow
Skip to content
Architecture for Flow
Home
Order
Contact
The Architecture for Flow Canvas
How can Wardley Mapping, Domain-Driven Design, and Team Topologies be brought together in a structured way?
I developed an opinionated structured approach and visualized it in an Architecture for Flow Canvas, offering guidance in designing adaptive, socio-technical systems optimized for a fast flow of change and feedback. This canvas aims to seamlessly combine Wardley Mapping, Domain-Driven Design, and Team Topologies. I also introduced the canvas in my talk at Fast Flow Conf (2024) in London.
The Architecture for Flow Canvas enables assessing the current (“as-is”) situation while also facilitating the design of the envisioned (“to-be”) situation. It is not a rigid framework but rather provides as little structure as possible (just enough to be helpful) while still allowing for being complemented with other tools as needed. It typically begins with analyzing the teams of today and envisions the teams of tomorrow.
The Architecture for Flow Canvas is typically applied in collaborative sessions with the affected teams involved in the optimization process. These sessions can begin with defining the desired outcomes, e.g. by collecting hopes and fears from each participant.
Assessing The As-Is Situation
Describing the Current Teams and Their Way of Working
Starting with the teams of today provides a clear understanding of the current team structure, their team sizes, their interactions and dependencies, and their current responsibilities within the system, as Figure 1 schematically illustrates. 
Figure 1) Describing current team structure, sizes, responsibilities, interactions and dependencies
These insights can be used as a foundational starting point when transitioning to the envisioned to-be situation.
Assessing the Current Flow of Change
Optimizing for fast flow involves assessing the current flow of change to identify potential blockers to flow. Teams often know what slows down their work. Meeting teams where they are and interviewing them about what currently blocks their flow of work helps to identify potential impediments that should be minimized, as Figure 2 depicts. 
Figure 2) Collecting current blockers and supporters to flow within team interviews
During the team interviews, not only are blockers collected, but also elements that currently support the flow to understand what should be preserved in the future to-be state.
The collaboratively collected pain points can be addressed later for cross-checking. In the envisioned to-be state, these pain points can be revisited to determine which of these flow impediments have been mitigated, which still need attention, and whether any new challenges have emerged.
Visualizing the Current Business Landscape
After addressing the teams and their blockers to flow, the next step is to understand and visualize the current business landscape using Wardley Maps. This can start with identifying a set of potential user or customer types. The scope of the Wardley Map can initially focus on one of these user types and later expand to include others, each with its own Wardley Map. Depending on the desired outcome and participants of the collaborative sessions, the addressed users can be external (e.g., external customers, business partners, etc.) and/or internal, e.g., teams.
Figure 3 summarizes the steps that are involved in creating a Wardley Map. 
Figure 3) Steps to create a Wardley Map
As a reminder, a Wardley Map is not meant to be a perfect representation but rather a useful abstraction. The maps can start simple, with just a few components, and be expanded over time.
A great value comes from creating a Wardley Map collaboratively within a group of people, fostering a shared understanding of the business landscape. Another significant value lies in starting from the user perspective by identifying users and user needs as the anchor of the map. It encourages a conversation that is focused on delivering value aligned with user needs, ensuring that the problem space is understood before moving on to building a solution.
The map helps to identify areas for investment and innovation, as well as what to evolve or outsource to gain a competitive advantage.
I use the Wardley Map as a visual tool to guide the optimization process, integrating patterns and practices from Domain-Driven Design and Team Topologies.
Categorizing the Problem Space
Transitioning from the current (as-is) situation to the designed (to-be) situation involves categorizing the problem space into subdomain types. Categorizing the problem space bridges the status quo and the future landscape.
The users and user needs not only represent the anchor of a Wardley Map but also reflect the problem space or problem domain, which can be categorized into core, supporting, and generic subdomain types – as Figure 4 illustrates. 
Figure 4) Categorizing the problem space into subdomain types
Those subdomain types help prioritize strategic investments and support build-buy-outsource decisions regarding the subdomains' solutions.
Designing the Envisioned To-Be Situation
Modularizing the Solution Space
After partitioning the problem space into subdomains, the next step is to achieve modularity in the solution space. Bounded contexts from Domain-Driven Design (DDD) promote high cohesion and modularity from a business behavior point of view. Bounded contexts provide good seams to split a system into smaller, modular, and well-encapsulated parts. Several modeling techniques can be used to define and design bounded contexts, such as EventStorming (see Figure 5). 
Figure 5) Identifying bounded contexts candidates with EventStorming
Visualizing the Future Landscape
After categorizing the problem space into subdomain types and modularizing the solution space into bounded contexts, next is to integrate these subdomain types and bounded into a Wardley Map to visualize the future landscape, as Figure 6 simplifies. 
Figure 6) The future business landscape with subdomain types and bounded contexts
The previously discovered subdomain types and designed modular bounded context help to better target future strategic investments. Major development efforts should prioritize core domain-related bounded contexts that provide a competitive advantage, which should be built in-house. For generic, non-differentiating subdomain-related bounded contexts, it's essential to evaluate whether existing solutions can be leveraged.
The decision of whether to build or buy is more nuanced for supporting subdomain-related bounded contexts that are non-differentiating but specialized. If highly customizable products are available, the decision tends to be to buy or use them. However, if off-the-shelf products or open-source solutions cannot easily address the required level of specialization, custom-built solutions are necessary.
Figure 7 highlights that not only the bounded contexts but also the entire value chain needs to be considered when targeting future strategic investments and assessing efficiency gaps. Can further evolved components not belonging to our core domain be leveraged to increase efficiency? 
Figure 7) Increasing efficiency by leveraging further evolved components for the future business landscape
The future business landscape visualized in one or multiple Wardley Maps can also be used to address the future team organization.
Deriving the Future Team Organization
Considering the socio-technical aspect of systems, the next step is to address the future team organization, where Team Topologies can help to optimize a system for fast flow with their well-defined team types and interaction modes.
Optimizing for fast flow involves analyzing the key drivers of value and change within an organization. That requires identifying the areas where the most important changes occur – the streams of changes. The user needs of a Wardley Map are strong candidates for customer-driven streams of change. To ensure a fast flow of change where it matters most, teams and systems should be structured around these customer-driven streams of change.
Deriving the future team organization involves finding suitable team boundaries aligned with customer-facing streams of change. As mentioned previously, bounded contexts provide well-defined ownership boundaries, making them not only good modularity boundaries but also good candidates for stream-aligned teams.
To maintain a fast flow of change, stream-aligned teams depend on other teams to support them in delivering their work, such as platform teams that provide easily consumable platforms. This requires identifying services that support a reliable flow of change and can be delivered as platforms providing self-service capabilities. Figure 8 illustrates a simplified future team constellation, where the bounded contexts are owned by stream-aligned teams and a platform team owns foundational platform related components of the value chain. 
Figure 8) A simplified future team constellation
A Wardley Map visualizing the future business landscape for external users or customers can be complemented by additional Wardley Maps that reflect the internal customer or team perspective. When shifting the focus from external customers to internal teams, stream-aligned teams and their user needs become the anchor of the map. This shift involves identifying self-service platform candidates that fulfill the user needs of the stream-aligned teams, helping them become more self-sufficient and reducing their cognitive load.
Simply organizing teams into different team types is not enough to ensure effectiveness. How these teams interact with each other and when to change and evolve the team interaction is crucial for achieving high effectiveness. Figure 9 depicts a simple example of an X-as-a-service (XaaS) interaction between the platform team and stream-aligned teams while also showing how stream-aligned teams can collaborate with each other over a limited period of time. 
Figure 9) Snapshot of interaction modes between teams
If teams lack certain skills, enabling teams can engage as internal coaches to help upskill the other teams. It may not be necessary to form a dedicated enabling team right from the start. For example, a platform team can initially facilitate other teams in using their platform, with a dedicated enabling team potential emerging later.
At this stage, the initially identified blockers to flow can be revisited to assess which of them have been minimized, which still need addressing, and whether any new obstacles have emerged.
Summary
This article introduces the Architecture for Flow Canvas, a structured yet flexible approach to integrating Wardley Mapping, Domain-Driven Design (DDD), and Team Topologies. The canvas helps to design adaptive, socio-technical systems optimized for a fast flow of change and feedback. It guides both assessing the current state („as-is“) and designing the future state („to-be“) in a collaborative, iterative way. It is structured enough to provide direction but remains open to being complemented with other tools.
Links
The Miro board template
My talk at Fast Flow Conf, London (2024)
© 2026 Architecture for Flow
Published by Pearson/Addison-Wesley – Part of Vaughn Vernon's Signature Series
hello@architectureforflow.com
Imprint
· Privacy Policy
· Cookies
