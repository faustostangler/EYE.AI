---
name: Specification-driven Prototyping with Domain Storytelling - codecentric AG
keywords: (placeholder)
metadata:
  url: https://www.codecentric.de/en/knowledge-hub/blog/from-domain-story-to-prototype
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Specification-driven Prototyping with Domain Storytelling
Popular searches Cloud native DevOps IT-Security Agile methods Java
About us
News
Contact us
DE EN
Services
How we work
References
Locations
Knowledge Hub
Careers  
About us
News
Contact us
DE EN
Services
Data Effectiveness
Digital Products & Solutions
Digital sovereignty
IT Security
Artificial intelligence
Software Modernization
Services from A to Z ...
How we work
References
Locations
Knowledge Hub
Blog
Careers
HOME
KNOWLEDGE-HUB
BLOG
//
From Domain Story to Prototype - Specification-driven Prototyping in DDD Workshops
DDD 
Annegret Junker
2.4.2026 | 8 minutes reading time 
You've just run a great Domain Storytelling workshop. The Miro board is covered in pictograms, numbered arrows, and work objects — stickies everywhere, connections between everything, the whole board alive with the domain's logic. Frames hold the Domain Stories, actors moving through a sequence of activities. Another frame holds the Visual Glossary, sticky notes mapping out the terms and relationships the domain experts actually use. Everyone nodded. The right questions were asked. The session was a success.
Then Monday arrives. The Miro board gets a bookmark. The export lands in a shared folder. And nothing has changed.
This is the classic gap between discovery and delivery. Domain Storytelling helps you understand a domain. But understanding alone doesn't mean validating — and there's a crucial difference between the two. This post is about closing that gap, fast, using the very artefacts your workshop already produced.
Domain Storytelling in a nutshell
If you're new to the method, Domain Storytelling is a collaborative modelling technique where domain experts narrate how their work actually happens or should happen, while a moderator captures the story using a simple visual language. The result is a Domain Story: a diagram showing who does what with which objects — in a clear, numbered sequence.
The cast of every Domain Story consists of three types of elements:
Actors — the people or systems doing the work (e.g. commuter, mechanic, app)
Work objects — the things being worked with (e.g. bicycle, code, monthly fee)
Activities — what actors do with or to those objects (e.g. books, unlocks, returns)
In parallel, a Visual Glossary takes shape. It doesn't define terms in isolation — instead, it captures how concepts relate to each other through strong verbs: a commuter uses a code, a code unlocks a lock, a rack contains locks, a rack stores bicycles. The meaning of each term emerges from these relationships, not from a dictionary entry. By the end of the session, you have two complementary artefacts: a story that shows the flow, and a glossary that explains the vocabulary.
Most teams treat the glossary as a reference artefact — nice to have, but nothing more. This post argues that with both artefacts in hand, you already have everything you need to build a working prototype — and show it back to the domain experts before the session ends.
A prototype hiding in plain sight
Here's the insight that changes the dynamic: the Visual Glossary and the Domain Story together map almost directly onto the building blocks of a software prototype.
When you look at the Visual Glossary and the Domain Story through this lens, you don't see sticky notes anymore — you see a list of screens to build and entities to model. The domain experts have already told you what matters. They've named the things, described the flows, and drawn the shapes. You just need to render it.
The prototype doesn't need to be complete. It doesn't need a database, error handling, or production-ready code. It needs to speak the domain's language well enough that the people who live in that domain can point at it and say: yes, exactly — or no, that's not how it works.
A real example: the bike-sharing system
A few days ago, I ran a Domain Storytelling workshop with a team building a bike-sharing system for urban commuters. The goal was to understand how the system would work in practice, from a mechanic provisioning bikes all the way to a commuter unlocking one at a public transport station and returning it near home.
The Domain Story captured ten numbered activities across two actors. A mechanic brings a bicycle to a rack. A commuter registers in the app, pays a monthly fee, searches for a bicycle at a public transport station, books it via the app, receives a code, and unlocks the bicycle with that code at the rack. Then the commuter drives home, returns the bicycle to a rack near home, and confirms the return via code. 
In parallel, the Visual Glossary took shape alongside the story, capturing six terms and the relationships between them: a commuter uses a code, a code unlocks a lock, a rack contains locks, a rack stores bicycles, and a commuter pays a monthly fee. The meaning of each term came from those relationships, not from descriptions. 
At the end of the session, I took both artefacts — the Domain Story and the Visual Glossary — and handed them to an AI, together with an example web page to define the visual style and formatting. And had it built a working prototype. 
Ten minutes later, we had a running HTML prototype. The screens followed directly from the Domain Story — one for finding an available bicycle at a rack, one for booking and receiving a code, one showing the active ride, and one for returning the bicycle. The story had drawn the navigation for us.
Every label, every field name, and every button used the exact vocabulary from the glossary. Not "vehicle" — bicycle. Not "station" — rack. Not "PIN" — code. Not "end trip" — return bicycle. The AI had no reason to invent its own terminology — the glossary was right there.
![Picture: Prototype screenshot — the resulting HTML prototype showing one or more screens with the domain vocabulary clearly visible]]( https://eu-central-1.graphassets.com/AiE4QoWSSiIQO3k152ugkz/cmnaa14ixi8b806uprsfuf78j)
I showed this back to the team before the workshop ended.
What happened in the room
The reaction was immediate — and instructive.
Within two minutes, one of the domain experts pointed at the Available Bicycles screen and asked: "What happens if a commuter gets to the rack and the bicycle is already gone — does the code still work?" Nothing in the Domain Story had covered the window between booking and arrival. It was a real race condition nobody had named yet.
Another participant looked at the Return screen and said: "The commuter confirms return via code — but the system should also verify the lock is actually closed. Those are two different things." Again: not in the story, not in the glossary, but immediately visible once there was something to react to.
A developer asked: "Is a code single-use? Can I unlock, re-lock, and unlock again on the same ride?" A question that turned out to have a genuine business rule behind it — and one that would have caused a subtle bug if left unresolved.
Questions like these also surface during the Domain Storytelling workshop. But the prototype activates a different mode of thinking — that of the user rather than the narrator. And that's what brings the additional insights to light.
The key advantage is the AI: the prototype is ready while the workshop is still running — not one or two weeks later, when the energy has long faded.
How to do it yourself
The method is simpler than you might expect. You need three things:
The Domain Story — exported or screenshotted from your Miro board
The Visual Glossary — the sticky-note relationship map from the same board
An example web page — a screenshot of any existing interface whose visual style and formatting you want the prototype to follow
Hand all three to an AI and use this prompt:
"Create a clickable webapp prototype out of a provided Domain Story for the process and a Visual Glossary for the domain language. For formatting, use the provided screenshot."
That's it. The Domain Story tells the AI what screens to build and in what order. The Visual Glossary tells it what to call everything. The example page tells it how to make it look. There is nothing left to specify — because the workshop already did the work.
Why does this change the conversation
Something happens when domain experts see their vocabulary in a working interface. They stop being narrators and start being critics — in the best sense of the word.
A Domain Story asks: What do you want to do? A prototype asks: Is this what you meant? These are different questions, and they surface different information. The first elicits description. The second elicits correction.
The gaps, edge cases, and unstated assumptions that did not surface in the workshop will surface in five minutes of clicking through a prototype. Not because the experts were holding back — but because software makes implicit knowledge visible in a way that conversation and diagrams cannot.
Domain Storytelling already gives you all the raw material. The Visual Glossary provides the terms and their relationships. The Domain Story and the Visual Glossary aren't just workshop outputs — they are the specification. And the prototype follows directly from them. With an AI to do the rendering, it happens fast enough to build the prototype during the workshop itself — not days later.
A prototype built from the Domain Story and the Visual Glossary isn't a deliverable — it's a question, asked in a language that gets an honest answer.
Have you used Domain Storytelling in your projects? I'd love to hear how you bridge the gap from workshop to validation — feel free to reach out or share your experience.
Was this post helpful?
share post
Blog author
Annegret Junker
Do you still have questions? Just send me a message.
Get in contact
Do you still have questions? Just send me a message.
Get in contact
//
More articles in this subject area
Discover exciting further topics and let the codecentric world inspire you.
[
The Synergetic Blueprint Revisited — and Why AI Changes Everything
From Workshop to Working Software — the Gap Nobody Talks About Most teams that adopt Domain-Driven Design invest heavily in workshops. Domain Storytelling sessions, EventStorming boards, context mapping exercises — the collaboration is real, and the ...
DDD
LLM 28.4.2026 | 8 minutes reading time](https://www.codecentric.de/en/knowledge-hub/blog/the-synergetic-blueprint-revisited-and-why-ai-changes-everything)
[
From Stories to Code: How Domain Storytelling and EventStorming Give LLMs...
The Broken Promise of AI-Assisted Development By now, most development teams have tried using an LLM to generate code. The results are familiar: syntactically correct, superficially plausible, and frequently wrong in ways that take hours to diagnose...
DDD
AI 4.3.2026 | 15 minutes reading time](https://www.codecentric.de/en/knowledge-hub/blog/from-stories-to-code-how-domain-storytelling-and-eventstorming-give-llms-the-context-they-need)
[
When Business Meets Technology: From Data Product to Data Architecture...
Abstract The Data Product Canvas (DPC) is a tool for the lightweight and iterative definition of data products. It increases the efficiency of product definition by clearly presenting the key impact areas on data products. Additionally, the DPC motivates...
Software architecture
Data
DDD
Digital product developement 5.8.2024 | 24 minutes reading time Dr. Florian Rademacher](https://www.codecentric.de/en/knowledge-hub/blog/when-business-meets-technology-from-data-product-to-data-architecture-with-domain-driven-design)
[
Axon Framework 102: Taking advantage of Metadata
Welcome to Axon Framework 102, where we will be deep diving into many interesting challenges you will encounter when working with Axon Framework. We will be diving into asynchronous projections and letting the front-end know new data. We will take a ...
DDD
Kotlin 30.5.2021 | 6 minutes reading time](https://www.codecentric.de/en/knowledge-hub/blog/axon-framework-102-taking-advantage-of-metadata)
[
Axon Framework 102: Dealing with personal data
Welcome to Axon Framework 102, where we will be deep diving into many interesting challenges you will encounter when working with Axon Framework. We will be diving into asynchronous projections and letting the front-end know new data. We will take a ...
DDD
Framework
Pattern
Event Sourcing
Compliance
Java
Kotlin 10.5.2021 | 5 minutes reading time](https://www.codecentric.de/en/knowledge-hub/blog/axon-framework-102-dealing-with-personal-data)
[
Organising a remote workshop EventStorming
Recently we have been busy organizing an Eventstorming workshop. It was a bit different than normal though since the goal of the workshop was to show the participants what an EventStorming workshop is and how they can apply it. We organized this workshop...
Remote Work
Agile
DDD 21.4.2021 | 5 minutes reading time](https://www.codecentric.de/en/knowledge-hub/blog/organising-a-remote-workshop-eventstorming)
[
Hexagon, Schmexagon? – Part 2
Exploring Variations of Implementing Domain Driven Design With The “Ports and Adapters” Pattern, Part 2Hexagonal Architecture is a key design pattern to use when implementing Domain Driven Design. It enables evolutionary changes, helps to keep test suites...
DDD
Software architecture
Microservices
Software development 30.7.2020 | 8 minutes reading time](https://www.codecentric.de/en/knowledge-hub/blog/hexagon-schmexagon-2)
[
Hexagon, Schmexagon? – Part 1
Exploring Variations of Implementing Domain Driven Design With The “Ports and Adapters” Pattern, Part 1 Hexagonal Architecture is a key design pattern to use when implementing Domain Driven Design. It enables evolutionary changes, helps to keep test ...
DDD
Software architecture
Microservices
Software development 28.7.2020 | 17 minutes reading time](https://www.codecentric.de/en/knowledge-hub/blog/hexagon-schmexagon-1)
[
“I open Pandora's box” – An interview with Alberto Brandolini on Domain...
EventStorming Creator, author of Introducing EventStorming – An act of deliberate collective learning and founder of Avanscoperta , Alberto Brandolini is a 360° consultant in the Information Technology field. Asserting that problems cannot be solved...
Agile
DDD 14.10.2019 | 13 minutes reading time Corinna Kern](https://www.codecentric.de/en/knowledge-hub/blog/alberto-brandolini-domain-driven-design-eventstorming)
[
DDD vs. Anemic Domain Models (Martin Fowler)
During a discussion about how to best implement our domain objects when applying DDD, which has recently become more and more popular, a colleague pointed me to Martin Fowler's article about Anemic Domain Models (2003). Martin is one of my heroes; I ...
Software architecture
DDD 14.10.2019 | 10 minutes reading time Rüdiger zu Dohna](https://www.codecentric.de/en/knowledge-hub/blog/ddd-vs-anemic-domain-models)
[
EventStorming meets Domain-Driven Design with Alberto Brandolini: A workshop...
Domain-Driven Design (DDD) is an approach to software development for complex scenarios: scenarios where we cannot get to the right implementation at first attempt. This is far more common than one might think. Often, what we experience in software ...
Agile
DDD
Product management 1.10.2019 | 7 minutes reading time](https://www.codecentric.de/en/knowledge-hub/blog/eventstorming-meets-domain-driven-design-with-alberto-brandolini)
[
Why do you write accessor methods?
Erik PetzoldRaimar Falke .We all know the getXxx() and setXxx() methods in languages like Java. They appear in almost every project and everybody uses them. But why do we cling to these methods? Do we need them? What about just making the fields public...
DDD
Java
Software development 22.2.2016 | 11 minutes reading time](https://www.codecentric.de/en/knowledge-hub/blog/write-accessor-methods)
[
Demystified CQRS
…and why it should be a fundamental principle of application designSome incredibly useful principles or patterns for software design are ignored because of the misconceptions around them, e.g. that they are not useful, too theoretical or their implementation...
Software architecture
Pattern
DDD
Database
Software development 25.5.2015 | 9 minutes reading time](https://www.codecentric.de/en/knowledge-hub/blog/demystified-cqrs)
The company
About us
News
Contact us
codecentric for you
Softwerker (DE)
Blog
RSS-Feed (blog)
Sitemap
Services
How we work
References
Careers
Locations
Media
Legal matters
Imprint
Privacy policy
       
Selecting an option will immediately change the language
Cookie banner: We need your consent
For codecentric AG, it is important to us that you can use our website without any concerns. We protect your data and pay attention to how it is used.
In order to tailor our website to your needs, we use tracking technologies from selected partners. These technologies are deactivated by default and we require your consent to use them. If you give us your consent, we may optionally use additional tracking technologies to analyze your user behavior, for marketing purposes and to integrate external content.
By clicking on "Accept all" you agree to all options. However, if you only want to allow certain services, you can select them individually under "Settings", change them or withdraw your consent at any time. With your consent, your data can also be transferred to third countries outside the EEA in accordance with Art. 49 Para. 1 Clause 1 a GDPR, which may not have the same level of data protection as the EU. You can find more information about your options in our data protection information and at any time under "Settings".
Privacy notice Imprint
Accept All Deny all Settings
Powered by Usercentrics Consent Management
