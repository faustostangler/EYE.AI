---
name: Advanced large-scale DDD | by Michał Grabowski | SoftwareMill Tech Blog
keywords: (placeholder)
metadata:
  url: https://blog.softwaremill.com/advanced-large-scale-ddd-72eafc8d6050
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Advanced large-scale DDD | by Michał Grabowski | SoftwareMill Tech Blog | SoftwareMill Tech Blog
Sitemap
Open in app
Sign up
Sign in
Medium Logo
Get app
Write
Search
Sign up
Sign in 
[
SoftwareMill Tech Blog
](https://blog.softwaremill.com/?source=post_page---publication_nav-185e254afb32-72eafc8d6050---------------------------------------)
·
Follow publication
Custom software development: Scala, Akka, Kafka, ML consulting. Distributed systems & backends, APIs. Tech partner to execute your idea! ➡ www.softwaremill.com
Follow publication
Advanced large-scale DDD
Michał Grabowski
Follow
8 min read
·
Dec 12, 2023 
27 
Listen
Share
Introduction
The most complex domains require tools to model larger structures and concepts. Developers need to understand the model to evolve it effectively. It's easy to lose track of where things belong. It becomes difficult to reveal the meaning and relationships between distinct system parts. We may quickly lose the most remarkable advantages of DDD. There is a need to structurize the model and introduce particular architecture on the model level.
Architecture imposes certain constraints that make the model more explicit and clear. Relevant aspects of the business must be carefully separated from each other to keep them meaningful and easy to understand. The goal is a system that is easy to reason about and develop. Tools that allow us to describe the system as a whole are a necessity.
Press enter or click to view image in full size 
Responsibility Layers
This approach employs a layered model, which assumes the division of a system into layers. Each layer has a narrowly defined responsibility and does not know what is above it, while the higher layers can use the functions of the layers below.
Here, we have two main approaches. A more radical one that assumes the use of only the direct underlying layer. A more flexible one that allows the use of any lower layer.
By definition, the “ Responsibility Layers” model is based on the second, more relaxed approach so that each layer can use domain functions from any layers below.
The layered model, used at the system or application level, delineates its responsibilities based on technical aspects. This model's decisions are rooted in purely business considerations, aiming to divide the model into smaller parts. We are focused on emphasizing business responsibilities and the relationships between them. The layers will also form an essential part of the ubiquitous language.
Every business has its natural stratification. Therefore, the selection of specific layers will depend on the particular case. It would be difficult to predetermine such layers; instead, it results from the model's evolution. Over time, as we better understand our domain, we will notice that certain concepts are based on others, lower down.
Several proven heuristics allow for the recognition of the layered nature of a model.
Linguistic Context — We cannot speak of sales without having a product or service. The concept of sales is based on the product/service. We can model a product without knowing about the existence of sales.
Evolutionary Context — Some model elements will change at a different pace and for various reasons than others. We will change the concept of price less frequently than the discount model based on it.
The storytelling context of layers communicates priorities and the realities of the domain. The choice of layers is a purely business decision.
Let's describe an exemplary layered model based on a transport company. Similar layers can be observed in many other domains. In particular, the first two layers tend to occur almost everywhere.
Capabilities — the actual possibilities we have. In a logistics company, these would be trucks, railway wagons, agreements with airports or ports, and access to traffic density data — all the resources that allow for the transportation of goods from point A to point B. Our resources do not know what we use them for; they model the capabilities. Not all possibilities will be utilized by our business. We can discuss transport schedules without considering the actual loads these units transport.
Operations — here, we talk about the current and actual activities of the business. A logistics company picks up a package from one location and commits to delivering it to another. Of course, to make this possible, this layer must use trucks, cars, or trains. However, the execution of the entire process will require various means of transportation so that the package ultimately reaches the recipient. If we want to track our shipment, we must be aware of the unit transporting it — here, we depend on the layer below and coordinate its work.
Policies — this is where we describe what we want to achieve or aim to optimize. We might optimize for the security of the shipment, the cost of delivery, or the time it takes. These will be certain specifications that determine the behavior of operations.
Commitments — all kinds of agreements and contracts. Namely, things that obligate us to specific behaviors. For example, to deliver a package within three days.
Decision Support — the layer responsible for selecting the appropriate policy. A decision may arise from legal regulations in a contract with a client and may vary depending on the period or even a specific client. If this is our essential customer, we might focus on building the relationship and delivering the package faster, sometimes even at the expense of individual profit.
Press enter or click to view image in full size 
Each of these layers may constitute its independent context or parts of it. We could use strategies or machine learning, rely on existing data warehousing mechanisms, or utilize an existing rule engine in the decision layer. It's worth noting that such a division may not be limited to a single bounded context.
The benefits of this approach indeed come to the fore within highly complex systems. By deliberately delineating our business's objectives and capabilities, we can prevent the conflation of concepts. It can also help us avoid introducing confusion into our shipping organization's management model, such as blending in the minutiae of specific transportation means usage, the intricacies of process optimization, or decision-making methodologies. We address these considerations on three distinct levels:
Usage — focus on what resources we utilize and how they are coordinated.
Optimization and Prioritization — define what aspects of our operation we aim to refine and elevate in importance.
Rationale — clarify why we adopt certain strategies under specific conditions.
With planning, it's easier for these distinct responsibilities to become entangled, leading to a challenging model to read, understand, and develop further. Our objective is to consciously delineate dependencies and awareness within our operations. This separation not only clarifies roles and responsibilities but also enhances the stability of our model.
Guidance
When making changes such as shifting focus from cost to customer relations and aiming for shorter delivery times — we must ensure that our modifications do not inadvertently affect unrelated system components. For example, suppose we decide to dispatch trucks earlier to improve delivery times, even when they aren't fully loaded. In that case, we must ensure this doesn't result in unforeseen issues like GPS malfunctions in our vehicles. This level of careful change management ensures that improvements in one area do not cause disruptions in another.
Get Michał Grabowski's stories in your inbox
Join Medium for free to get updates from this writer.
Subscribe
Subscribe [x]
Remember me for faster sign in
The layers form an outline of the story that our system tells. The division imposed by bounded contexts prevents the blurring and contamination of models. However, it does not help to see the system as a coherent whole. In an extensive system, people will work independently at various levels.
Without guidance, different teams will create separate solutions, which leads to difficulties in understanding how the individual parts fit together. The large-scale structure must evolve as part of the domain model. An ill-chosen structure is worse than no structure at all. A proper structure can be found only through a deep understanding of the domain and the problem. The practical route to that understanding is an iterative development process.
Sometimes, it is criticized that at the capability layer, we deal with aspects that the business did not request — potential abilities that we have but that the business does not use. However, having such a division often makes adding new functionalities simpler and faster. By modeling the capability layer in complete isolation, we do not contaminate it with artificial limitations. It is just that the operational layer only uses a portion of the available capabilities.
Knowledge Level
Relationships between objects can be very complex. They may even change dynamically and result from configuration. For example, organizations are composed of people and smaller organizations, each with defined roles and relationships with other units. Such structures can be very complex and, more importantly, may look different in each organization, using various departments, names, permissions, or policies.
The Knowledge Level is a particular case of the reflection pattern, which allows capturing changing needs by making the system self-aware. We divide a given concept into two levels. The Base Level carries out operational responsibilities. Meta Level represents knowledge about behavior and structure.
The meta-model describes how various employees and their relationships are organized and what rules govern them. It enables the organization of data from the base model. It defines how we can organize and manipulate that data. The meta-model describes the blueprint for organizing the base model.
Thus, it answers questions like:
A department can contain many positions.
A manager oversees the employees within their department.
An employee is assigned to one department.
These are not rigid rules; they may depend on many different factors. The meta-model can be derived from configuration.
Press enter or click to view image in full size 
It sounds very similar to the layers described above, yet these are not the same layers. The difference here lies in the flow of dependencies. The Knowledge Level is based on the bidirectional dependency of the base and meta-models.
This method is apparent in the Party Archetype. The structure's model is complex, and managing the relationships separately is helpful. This way, each part can evolve without affecting the other. It also makes it easier to reuse parts of the system. Our goal isn't to create a one-size-fits-all solution, though. We want to keep our system flexible while still focusing on the critical aspects of our domain.
Conclusion
These aren't the only model architectures out there, but they serve as great examples to appreciate their power. Along with bounded context and distillation, these structures are techniques for shaping models. However, this is an optional technique.
Each model architecture has its strengths. These examples highlight how effective they can be when applied correctly. When we talk about bounded context, we refer to setting clear boundaries within which a particular model is defined and relevant. Distillation, conversely, is about refining and simplifying a model to its essence.
Adding structures, such as new layers or components, can enhance a system's capabilities, but it also brings additional complexity that may not be necessary. The key is to balance the benefits of these structures against their cost in complexity. They should only be introduced when they add clear value and align with the goals of the domain. It is essential to remember that adding more structures to a system can make it more complex, and in most cases, it is just not worth the effort.
By treating these structures as optional, we maintain flexibility in our design, ensuring we can adapt to changes without being locked into an overly rigid model framework.
Further reads
Domain Driven Design Tackling Complexity in the Heart of Software — (Section 16: Large Scale Level) Eric Evans 2014
Enterprise Patterns and MDA — (Party Archetype, Party Relations Archetype) Jim Arlow 2003
[PL] Better Software Design — (O modelowaniu w wielkiej skali) Mariusz Gil, Jakub Pilimon 2020
Pattern Languages of Program Design — (Reflection Pattern) Frank Buschmann 1995
Dealing with Properties — Martin Fowler 1997 
27 
Domain Driven Design
System Architecture
Software Development
Design Patterns
Bounded Context 
27 
27 
Follow
[
Published in SoftwareMill Tech Blog
](https://blog.softwaremill.com/?source=post_page---post_publication_info--72eafc8d6050---------------------------------------)
5K followers
·
Last published Nov 25, 2024
Custom software development: Scala, Akka, Kafka, ML consulting. Distributed systems & backends, APIs. Tech partner to execute your idea! ➡ www.softwaremill.com
Follow
Follow
[
Written by Michał Grabowski
](https://ayeo.medium.com/?source=post_page---post_author_info--72eafc8d6050---------------------------------------)
84 followers
·
211 following
Software Developer at softwaremill.com
Follow
No responses yet
 
Write a response
What are your thoughts?
Cancel
Respond
More from Michał Grabowski and SoftwareMill Tech Blog
Michał Grabowski
[
CQRS and transactions in DDD world
One day you may need to dispatch few commands and you want all of them to succeed or none. To put it other words you want an transaction…
](https://ayeo.medium.com/cqrs-and-transactions-in-ddd-world-10419440a09c?source=post_page---author_recirc--72eafc8d6050----0---------------------a6117408_fdfa_4569_adaf_9a386a3eab54--------------)
Feb 22, 2021
A clap icon 110   
In
SoftwareMill Tech Blog
by
Maciek Opała
[
Editing files in a docker container
bash: <EDITOR_NAME>: command not found— if you've ever encountered this shell message after logging into a docker container with an…
](https://blog.softwaremill.com/editing-files-in-a-docker-container-f36d76b9613c?source=post_page---author_recirc--72eafc8d6050----1---------------------a6117408_fdfa_4569_adaf_9a386a3eab54--------------)
Dec 14, 2018
A clap icon 1.2K A response icon 12   
In
SoftwareMill Tech Blog
by
Bartek Andrzejczak
[
Who am I? Keycloak Impersonation API
](https://blog.softwaremill.com/who-am-i-keycloak-impersonation-api-bfe7acaf051a?source=post_page---author_recirc--72eafc8d6050----2---------------------a6117408_fdfa_4569_adaf_9a386a3eab54--------------)
Feb 12, 2018
A clap icon 188 A response icon 9   
In
Level Up Coding
by
Michał Grabowski
[
Exception in Domain-Driven Design
Exceptions have been introduced to handle errors on the function level. The intention was to avoid returning error codes and remove return…
](https://levelup.gitconnected.com/exception-in-domain-driven-design-832c92fb04f4?source=post_page---author_recirc--72eafc8d6050----3---------------------a6117408_fdfa_4569_adaf_9a386a3eab54--------------)
Jul 4, 2022
A clap icon 254 A response icon 4  
See all from Michał Grabowski
See all from SoftwareMill Tech Blog
Recommended from Medium
In
Women in Technology
by
Alina Kovtun✨
[
Stop Memorizing Design Patterns: Use This Decision Tree Instead
Choose design patterns based on pain points: apply the right pattern with minimal over-engineering in any OO language.
](https://medium.com/womenintechnology/stop-memorizing-design-patterns-use-this-decision-tree-instead-e84f22fca9fa?source=post_page---read_next_recirc--72eafc8d6050----0---------------------542345cf_b7f3_4267_ba55_2501f5c0c5fe--------------)
Jan 29
A clap icon 7.9K A response icon 85   
WhyPratiik
[
Stop Memorizing Design Patterns: Use This Decision Tree Instead
A practical, story-driven guide to choosing the right pattern without memorizing 23 definitions.
](https://medium.com/@pratikchaudhariworks/stop-memorizing-design-patterns-use-this-decision-tree-instead-2e2633a5a225?source=post_page---read_next_recirc--72eafc8d6050----1---------------------542345cf_b7f3_4267_ba55_2501f5c0c5fe--------------)
Feb 19
A clap icon 127   
Michal Malewicz
[
The End of Dashboards and Design Systems
Design is becoming quietly human again.
](https://michalmalewicz.medium.com/the-end-of-dashboards-and-design-systems-5d98ec9de627?source=post_page---read_next_recirc--72eafc8d6050----0---------------------542345cf_b7f3_4267_ba55_2501f5c0c5fe--------------)
Nov 26, 2025
A clap icon 7.3K A response icon 303   
Natan Schons
[
Using Classic Design Patterns to Build Scalable AI Systems
The Wild West of AI Engineering
](https://medium.com/@natanschons/using-classic-design-patterns-to-build-scalable-ai-systems-e4c812224aaa?source=post_page---read_next_recirc--72eafc8d6050----1---------------------542345cf_b7f3_4267_ba55_2501f5c0c5fe--------------)
Feb 25
A clap icon 3   
#hope
[
CQRS: Command Query Responsibility Segregation — Inside Out
The Core Idea
](https://todayamerican.medium.com/cqrs-command-query-responsibility-segregation-inside-out-63099885a0f2?source=post_page---read_next_recirc--72eafc8d6050----2---------------------542345cf_b7f3_4267_ba55_2501f5c0c5fe--------------)
5d ago
A clap icon 38   
slice engineering
[
How We Solved a Kafka Freeze, 5x-ed Throughput, and Right-Sized Our Partitions — Lessons from…
At Slice, we run a high-throughput event-driven backend. Kafka is at the center of it, processing payments, order lifecycle events, and…
](https://engineering.slice.bank.in/how-we-solved-a-kafka-freeze-5x-ed-throughput-and-right-sized-our-partitions-lessons-from-d9b0e20c3cc2?source=post_page---read_next_recirc--72eafc8d6050----3---------------------542345cf_b7f3_4267_ba55_2501f5c0c5fe--------------)
Apr 8
A clap icon 30 A response icon 1  
See more recommendations
Help
Status
About
Careers
Press
Blog
Privacy
Rules
Terms
Text to speech
