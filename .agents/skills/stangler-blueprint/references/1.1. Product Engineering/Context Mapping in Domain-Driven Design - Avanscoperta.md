---
name: Context Mapping in Domain-Driven Design - Avanscoperta
keywords: (placeholder)
metadata:
  url: https://www.avanscoperta.it/en/context-mapping/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Context Mapping in Domain-Driven Design | Avanscoperta 
Avanscoperta
Training
Consulting
Books
About
Info – T&Cs
Blog
Avanscoperta
Training
Consulting
Books
About
Info – T&Cs
Blog
Italiano
Context Mapping
The Swiss Army knife of Strategic Domain-Driven Design
In Domain-Driven Design, Context Mapping is a tool for mapping relationships between Bounded Contexts in a software development scenario.
On the surface, it is just a drawing showing the relationships between different models. But the map is only the visible part of the story. Context Mapping is an investigation process that requires asking in-depth questions and highlighting strategic information that will be vital for our project outcome. 
When dealing with multiple models, a map becomes crucial for clearly separating their responsibilities and for their cooperation. It becomes a key source of information for splitting teams' ownership of models and minimising their coupling.
Eric Evans first described context maps in Domain-Driven Design: Tackling Complexity at the Heart of Software.
There, Context Maps weren't intended to be heavyweight diagrams that constrain evolution, but relatively quick sketches that guide teams in complex territory. However, the blue book only hinted at the power and versatility of Context Mapping. Field practice showed how they could be an incredibly versatile and powerful tool.
Greenfield vs Brownfield
A key distinction regarding the significance of context maps is their role in current software development initiatives. A greenfield context map focuses on the ideal decomposition of a future system into collaborating models. In contrast, a brownfield context map is more focused on understanding the current forces that constrain collaboration between models within the current system.
This is no minor difference. Envisioning the future is a design exercise in clean modelling, driven by design principles. Reading the current status quo is a full-blown sociotechnical discovery initiative. A brownfield context map is one of the few tools for displaying the political forces at work in your software ecosystem.
Brownfield and Greenfield typically explore the relationships among many models relevant to our current area of interest. When the map area is limited to a collaboration between two contexts, it can be referred to as a local context map or a translation map.
Brownfield Context Mapping
Typically, we draw a map as one of the initial steps for a software development initiative when our software needs to interact with other components.
The steps for drawing a context map differ significantly between greenfield and brownfield scenarios. Brownfield Context Mapping has a more straightforward recipe:
Detect models;
Make boundaries explicit;
Draw relationships between models;
Display the relationships' direction (upstream/downstream);
Categorise the relationships;
Decorate the map with annotations about the risk areas or other meaningful extra info.
The following picture will be more explicit.
Six steps to draw a Brownfield context map
1. Detecting Models
Graphically, this is the most straightforward step: we need to record the models we detect during our investigation. Since we are dealing with a legacy implementation, some design drivers may be blurred. The original purpose of a model may have been obscured by years of patches and uncontrolled evolution.
However, a separate software component might indicate at least one independent model. Code ownership can be another interesting signal: different teams typically mean different models.
We shouldn't aim for perfection at this stage. The reality won't be clean, and our map must be honest. The following steps may give us more information.
2. Make boundaries explicit
Do we have a clean separation between our models? If yes, then we can draw a bubble around our model. Bounded Contexts, by definition, are the limit of applicability of a model, so sharp boundaries are somewhat required.
However, when dealing with legacy code, clean boundaries are a lucky exception. Most of the time, we will discover a lack of clear boundaries, and we'll need a quick way to represent this mess. Clean boundaries can rely on the official representation, while more controversial interpretations can require a more explicit visualisation. 
A Big Ball of Mud is a quick way to highlight a portion of your system that has lost integrity long ago.
3. Draw relationships between models
Models are connected. They need to interact or to share information. A line between two bubbles indicates an ongoing relationship, such as an API call or a shared database table.
The number of existing relationships can already be a warning signal: systems where every model is connected with everything else are really hard to maintain. The number of relationships is an indicator of potential ripple effects and the associated fear of modifying the code.
4. Visualise direction
Drawing relationships may look trivial at first. Models are connected, tables are shared, events are published, APIs are exposed. But a Brownfield Context Map shifts the exploration in a different direction. It forces us to examine the collaboration between models and teams in a way that isn't purely technical, but also political.
This mostly happens by focusing on the upstream-downstream relationships between the models.
Upstream and downstream
The upstream and downstream labels show which side of the relationship has more influence over the other, constraining the available collaboration patterns.
For example, we'll typically be downstream to external service providers, such as a payment gateway, which may not accommodate our requests for an additional field in their API. Here, we might choose to be Conformist in our first implementation and then upgrade to a safer Anti-Corruption Layer.
In other scenarios, we might be in a dominant upstream position, offering a standard entry point to our services without much room for customisation, maybe with an Open Host.
The upstream-downstream relationship captures the political relationship between the two models, not the technical one.
Emphasising Communication Bandwidth
Connectors between bounded contexts can convey extra information: thickness can represent the available communication bandwidth between two models.
Communication bandwidth is a scarce resource in many organisations, and a common source of friction and misunderstanding. It represents the available space for information exchange between the teams responsible for Bounded Contexts. It can be the time we reserve for meetings, cross-team coordination, and other tasks.
Two colocated teams could share modelling space and discuss topics in a simplified way without calling structured meetings. We can leverage this proximity to enable highly engaging collaboration patterns, such as Partnerships. 
Two teams in different time zones, or perhaps part of other departments or even companies, may not have the same privileges. It would be great to build a shared mindset and foster continuous collaboration, but it won't happen. With little available communication bandwidth, both teams would be better off with a clear definition of the boundaries. Maybe writing a little more code will compensate for the missing conversation space.
While apparently discussing software models, we are taking a peek into organisational constraints. The bandwidth we need and the one we have can be really different. Mapping the communication bandwidth is a great way to highlight the existing constraints.
5. Categorising relationships
A Brownfield Context Map focuses on the collaboration between models. This often mirrors the collaboration between the responsible teams.
After collecting information on the possible types of collaboration, we can attempt to categorise the relationship between the models.
We need to keep in mind that we are examining the models in the making: we are looking at the forces that constrain their evolution, not at how the code behaves. It's organisation boundaries and team collaboration, more than clean interfaces.
Collaboration patterns
Eric Evans describes some patterns that categorise these relationships.
A Partnership describes a collaboration in which two models can evolve harmoniously, as in the early days of a small company, where a single team can juggle with multiple models, or easily call a joint modelling session with the other team.
A Customer/Supplier describes a more structured co-dependency, where one side needs the other more than the other does. Collaboration is possible, but it requires coordination.
In a Conformist, the downstream model adapts to the upstream one with minimal adjustment and trading flexibility for short-term development speed.
An Anti-Corruption Layer will protect the downstream model from variations from the upstream one. This is particularly useful when integrating with third-party components.
An Open Host highlights the different responsibilities that stem from the upstream role of being a service provider. This will mean more work on documentation, robustness, and backward compatibility.
A Shared Kernel highlights the need for robustness and expertise to maintain a shared model in which a small change can have massive ripple effects.
Separate Ways describes the deliberate choice to move on with minimal integration between two distinct systems.
Published Language refers to the use of a shared, official language for model-to-model communication, often allowing more parties to participate.
The Big Ball of Mud describes the dynamics of a system that has lost its conceptual integrity and becomes progressively harder to change.
Visualising the sociotechnical complexity
These patterns describe different trade-offs in the sociotechnical stack.
An Anti-Corruption Layer implies writing more code to compensate for the team's limited communication bandwidth. A Partnership goes in the opposite direction.
Similarly, an Open Host may be the more bureaucratic version of a Customer/Supplier, becoming too demanding as more models started connecting.
Relationships between models result more from spontaneous evolution than a deliberate act of design. A Brownfield Context Map is typically a short-lived tactical tool to assess the current reality and highlight the most constraining concerns.
6. Decorate the map
If you're aiming for perfection and clean diagrams, drawing a Brownfield Context Map can be excruciating. Clarity, not beauty, is not the goal of the mapping effort.
But all the little inconsistencies, questions, and doubts that haunted us while attempting to draw the map can find their way into our drawing. Warning signs, question marks, red notes, and any other necessary elements to convey the message can be added to the map.
The map is a tool to deliver a message. Make it speak!
How to use a Brownfield Context Map
Drawing a Brownfield Context Map is a detective job: it implies asking the right questions about the surroundings of our area of interest.
Ideally, when kicking off a new project, drawing a brownfield map should take less than an hour, provided we can obtain the necessary answers from the experts. Greenfield maps will take longer because different interpretations may clash, but we don't need diplomacy in Brownfield; only transparency. 
If obtaining answers about integrations and collaborations with other teams is challenging or inconclusive, we may have already gathered crucial information about the risks associated with a project.
“We should integrate with team X, but we couldn't get any answers from anybody about how to perform this integration.”
For a software development team on an ambitious project, the perfect storm may be a combination of fixed deadlines and unreliable external dependencies. Here, estimations tend to capture only the risk associated with doing without considering the time spent waiting for unresponsive partners.
A Brownfield Context Map helps detect these risks very early by forcing you to ask the right questions and meet the right people before committing to a hopeless death-march project.
Greenfield Context Mapping
Greenfield context mapping is a different sport. We need to detect domain hints that may signal the presence or the need for independent models. This would allow us to optimise models for their specific purpose.
A single-purpose model can be sharpened and distilled to excel at one thing, while trade-off models (such as those built on top of a shared database schema) tend to lose flexibility over time.
Unfortunately, while purpose is the most powerful force shaping our need for a dedicated model, it doesn't provide immediate guidance for drawing our map. We can't ask business stakeholders to provide us with a purpose with the sharp precision needed to define model boundaries.
Finding boundaries is a software architect's job and can't be delegated.
Detecting Bounded Context with EventStorming
Luckily, collaborative workshops like Big Picture EventStorming can provide valuable hints about partitioning a large enterprise model, especially when organised around a business flow.
Different stakeholders, especially those from different offices, will have distinct needs; therefore, they will likely require separate models.
Pivotal Events, which separate distinct phases, serve as natural landmarks between the model(s) to the left and the model(s) to the right.
Swimlanes typically represent independent processes, often with a clear and specific purpose.
While none of these indicators is bulletproof, observing the emergent model and the people's behaviour together provides incredible information about how to split a large enterprise model.
While a Big Picture EventStorming effectively detects domain signals, we must remember that Bounded Contexts are not a business concern.
Despite the invaluable contribution during the workshop, drawing the map with our business stakeholders isn't always a good idea.
Going below the surface
Not every bounded context can be detected with signals from the business flow. Shared components may provide services or technical capabilities independently from the business flow. Often, logical layers are a better way to detect boundaries between models below the business flow surface.
Usually, we'd use a Local Context Map for that.
What about the collaboration patterns?
Collaboration patterns are somewhat premature for Greenfield Context Maps. The collaboration is not in place, and perhaps there is no organisation to investigate yet, and no organisational politics.
In general, collaboration patterns are a way to categorise existing collaborations, so we'll need more field information to recognise them.
However, some relationships are easily recognisable even before the start, so it's not uncommon to add Anti-Corruption Layers between our model and an external vendor. But when it comes to finding a distinction between a partnership and a customer-supplier relationship before development is in place, then it could quickly become pointless
Local Context Mapping
When working on the boundary between Bounded Contexts, concepts that may span different models require special attention.
This is where a Local Context Map may be helpful. It can visualise the current agreement and support the discussion when deciding which concepts belong to which model.
Cooperating models
In the following example, three models are cooperating in a space where the same data is used for different purposes. The emphasis on purpose helps preserve the integrity of the local model and provides a more robust foundation for future evolutions. 
Refining the local Ubiquitous Language helps sharpen the model, keeping the involved Bounded Contexts sharp and clean. Interestingly, the same data can be presented under different names (such as Balance and Liquidity in the example above) or lead to more precise concepts when translating the Due Date concept in Billing to the Expected Date in Forecast.
Stacked Models
Drawing the boundaries can become tricky in a layered model scenario, especially when the modellers trying to draw the line are also experts in the underlying layers.
In this example, we can see two models that are logically layered: a Content Design bounded context that sits on top of a more generic Text Editing bounded context. Content Design offers a more sophisticated perspective on content, enabling us to manage the different logical components of a piece of web content. The Text Editing model, on the other hand, is unaware of this sophistication and focuses solely on the editing experience. 
The objection “At the end of the day, it's all text” is valid and wrong at the same time. While everything can be text, and we'll be using some text-editing capabilities, designing content for the web occurs at a different level of abstraction, with a more purpose-oriented semantic approach.
Context Mapping Applicability
Context Maps are a versatile tool, not strictly limited to Domain-Driven Design.
A Brownfield Context Map can be a very effective tool for capturing vital information about an initiative about to start. Moreover, the collaboration patterns can be applied beyond the software world, making the map a useful tool for any transformation initiative involving multiple teams.
A Greenfield Context Map is more of a design artefact for envisioning complex model collaboration, and then providing modelling guidelines for the future evolution of the model. Clean boundaries coming from your map can also provide robust guidelines for AI-assisted development.
Local Context Maps can be vital when working on two adjacent models simultaneously. A single team will need safeguards to avoid injecting coupling into a young, growing system.
But local Context Maps can also be vital in complex negotiation scenarios. Words may have different meanings and significance to the two negotiating parties; an explicit context map can prevent misunderstandings from escalating.
F.A.Q.
Should we map everything?
Not really. The map is a tool, not a duty. When starting a project, it's a good idea to sketch a map of the surrounding bounded contexts and categorise their relationships. But gathering information beyond the neighboring models may not be relevant at this stage.
More ambitious large-scale initiatives, such as architectural modernisation, can leverage discovery workshops, such as Big Picture EventStorming, to gather information and map the entire business line.
Avanscoperta has deep field experience in leveraging Domain-Driven Design
to solve complex challenges for teams and organizations around the world.
Need our help about it?
Contact us
TOP
Avanscoperta S.r.l - Società unipersonale - Via S.Silvestro 168 – 48018 Faenza (RA) - ITALY ~ C.F. / P. IVA: 02352720391
Via S.Silvestro 168 - 48018 Faenza (RA) - ITALY C.F. / P. IVA: 02352720391 T: +39.0546.646007 - E: info@avanscoperta.it        Search 
NEWSLETTER
Get exclusive content from experts in software development, technology, business and design!
SUBSCRIBE TO OUR NEWSLETTER! :-)
Subscribe to our newsletter!
×
Notice
We and selected third parties collect personal information as specified in the privacy policy and use cookies or similar technologies for technical purposes and, with your consent, for experience, measurement and “marketing (personalized ads)” as specified in the cookie policy.
You can freely give, deny, or withdraw your consent at any time by accessing the preferences panel. Denying consent may make related features unavailable.
Use the “Accept all” button to consent. Use the “Reject all” button or close this notice to continue without accepting. [x] true
Necessary [-] false
Experience [-] false
Measurement [-] false
Marketing [x] true
Sale of my personal information [x] true
Sharing of my personal information [x] true
Processing of my personal information for targeted advertising
Press again to continue 0/1
Learn more
Reject all Save and continue
