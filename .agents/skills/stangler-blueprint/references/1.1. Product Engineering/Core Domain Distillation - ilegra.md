---
name: Core Domain Distillation - ilegra
keywords: (placeholder)
metadata:
  url: https://www.ilegra.com/pt/blog/core-domain-distillation
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Core Domain Distillation - ilegra
Utilizamos cookies para oferecer melhor experiência, melhorar o desempenho, analisar como você interage em nosso site e personalizar conteúdo. Saiba mais
RecusarCookiesAceitar  Cookies
PT EN 
Core Domain Distillation
escrito por Rafael Ritter
7 minutos de leitura
30/04/2021 
In software design, distillation translates to the partitioning of a larger system to make the core domain clearly visible and distinct.
A navigation map for strategic distillation, by Eric Evans
Strategic Distillation
When developing systems with complex domains, how do we tackle the central problem without being distracted by secondary issues? A layered architecture helps by separating domain concepts from technical logic, but in a large system even the isolated domain layer may be unmanageably complex.
One of the essential lessons to be learned from Domain-Driven Design (DDD) is defining and focusing on the core domain. This process is known as distillation. Distilling means separating the components of a mixture in order to extract its essence. In software design, this translates to the partitioning of a larger system to make the core domain clearly visible and distinct. In DDD, distillation is part of strategic design, which deals with the modularization of large software systems.
Strategic distillation does many things. It directs efforts to the vital parts of the domain; it makes the overview of the system clearer; it facilitates communication by identifying a core model of reduced size; it guides refactoring; and it guides outsourcing, use of off-the-shelf components and decisions about assignments. Multiple patterns assist in the achievement of these goals.
Core Domain
The core domain is what makes the company make money — it is its competitive advantage. It's what differentiates the application from the others, and what brings the most value to the users. Therefore, it is in the core domain that the focus should be. It should be crystal clear what is in the core domain and what is not. That will make the core domain — the real business asset — easier to understand and to change, which is everything the business wants. Because not all parts of the design will be equally refined, it is the definition of the core domain that should drive the priorities. When deciding where to refactor, the first place to consider should be the core domain.
Oftentimes, highly skilled developers gravitate to technical problems and lack domain knowledge. In such cases, the core will be developed by less skilled engineers, generally leading to a poor design or implementation of the main part of the system. This will likely create software that never does anything compelling for the users, no matter how well the technical infrastructure works or how nice the supporting features are.
Development in the core domain requires long-term commitment from the most skilled engineers. They must continuously learn about the business and acquire domain knowledge from the subject-matter experts, and apply their design skills to create the conceptual power in the model that will produce really useful and valuable software for users.
Generic Subdomains
There will be parts of the domain that are not core but that are still complex. Without an explicit distinction, these supporting complexities will make the core domain harder to understand.
Generic subdomains are subdomains that are not the motivation for the project. In order to make the core domain simpler, we should create generic models of these subdomains and place them in separate modules, leaving no trace of our specialties in them.
Identifying a generic subdomain gives us some options regarding the development of this subdomain:
Off-the-shelf solution: Because it is not part of our core domain, we can choose to buy an implementation or use open-source software. This leaves us with less code to develop and maintain, and a solution that is more mature and already used in multiple places. On the other hand, we still need to spend time evaluating it before deciding to use it, and integrating with it if we choose to use it.
Published design or model: A published design or model will also be more mature than a brand new solution, and will already come with documentation to assist us in its use. We just have to make sure it meets our needs and is not overengineered for them.
Outsourced implementation: Another option is to outsource the implementation of this subdomain. This choice will free the core team to work on the core domain, while also allowing more development to be done without increasing the size of the team and without dissipating core domain knowledge. Still, it will require time from the core team to design the interface and communicate their needs. In addition, this option will also generate the overhead of transferring ownership back inside, to understand the implemented code — which is still less overhead than in the case of specialized subdomains, which would require special background to understand.
In-house implementation: Finally, a homemade solution will provide just what we want and nothing more, as well as easy integration with the rest of the system. The cost will be, of course, the internal development and maintenance time for these modules.
Domain Vision Statement
There is a need to explain the value of the system concisely, be it at the beginning of the project, when a model does not yet exist, be it in the middle, for the sake of brevity. Besides that, the core domain may span multiple bounded contexts, in which different models with different concepts and rules apply. [2] Thus, these distinct models cannot be joined to show the goals they share.
The purpose of the domain vision statement is to describe the value of the core domain model. It should be short (about one page) and focused only on what differentiates that domain model from the rest. It can be used to guide resource allocation, to guide modeling choices, and to educate team members.
Highlighted Core
Since the domain vision statement has to be brief, it only identifies the core model in broad terms, and thus is too vague to identify core model elements. However, it is important that everyone in the project knows what is part of the core domain and what is not. The best way of achieving that is through the structure of the code, separating core from non-core elements logically or even physically. But it's hard to arrive at the correct code structure before even having a view of how it should look like in the first place.
As options to meet that need, there are two main techniques for highlighting the core domain:
The Distillation Document: This document consists of a few pages explaining the core domain and the primary interactions between its elements. It can be a set of diagrams containing the most essential conceptual objects. It can be a list of those objects. It can simply be textual descriptions of them and their relationships. As with any document, it may end up not being maintained or read. The best way of preventing such problems is to avoid details and focus on the central abstractions, which tend to be more stable. If changes to the code require changing the distillation document, then we know those changes are important and require more review, and we know we have to communicate the team about the new version of the document.
The Flagged Core: This is another form of highlighted core, in which we flag each core domain element within the primary repository of the model. It can be a UML stereotype identifying the core elements. It can be a set of Javadoc comments, if the team uses the code as the sole repository of the model. The important thing is that the core domain is clearly visible to the team.
Cohesive Mechanisms
Sometimes there is the necessity of implementing a complex algorithm in order to solve a problem in the domain. However, mixing it up with the design of the domain may end up obfuscating the expressiveness of the domain model.
A possible way of dealing with that challenge is separating that kind of cohesive mechanism into a framework responsible solely for processing the technical computations, without any knowledge of the domain. The domain then expresses the “what” through an intention-revealing interface and delegates the “how” to the framework. Doing that will avoid coupling the model to a particular solution, which would limit future options. An example of cohesive mechanism is graph manipulation.
Segregated Core
Separating generic subdomains from the core subdomains helps to simplify the core domain. However, it's not an easy task to identify all the generic subdomains and create models for them.
Segregating the core is basically attempting to do the same thing, but the other way around. Instead of worrying too much about the models of the subdomains that are not the motivation for the project, the segregation of the core focuses on the cohesion of the core domain, without immediately caring that much about defining and modeling the supporting subdomains, which is not irrelevant, but also not as important. The idea is to identify core subdomains and move them to new modules, leaving behind elements unrelated to the concept.
While this technique may make non-core parts of the system harder to work on, that cost is outweighed by the benefit of clarifying the core domain, since that's where the most value will be added to the business.
Conclusion
The core domain is the most important thing to the business and to the users. The distillation techniques described here aim either to clarify or to unburden the core domain, thus giving traction to the business. Learning about them, therefore, gives us the opportunity to create differentiated and remarkable software that draws the attention of users and stands out from the competition.
References
Evans, Eric. Domain-Driven Design: Tackling Complexity in the Heart of Software.
DDD Model Integrity Patterns
Fonte da imagem destaque deste post: Collaborative Modelling as a pillar of DDD (Source: Paul Rayner, Workshop at Explore DDD 2018, picture by Martin Schimak)
Compartilhe esse post:
Linkedin
Facebook
Whatsapp
Link
Posts relacionados
[
A importância dos filtros em relatórios de BI e como melhorar a experiência do usuário com CSS integrado ao Power BI
Giovanna Gadelha 28/04/2026 Como organizar segmentações de dados, evitar poluição visual e criar indicadores dinâmicos de filtros aplicados com CSS no Power BI](https://www.ilegra.com/blog/filtros-power-bi-css-usabilidade-relatorios)
[
Sucesso operacional vs. Integridade analítica: Quando o sucesso do pipeline não significa sucesso do processamento
Willian de Vargas 05/04/2026 Tornando falhas analíticas observáveis ao migrar do Azure Data Factory para o Databricks Lakeflow Jobs](https://www.ilegra.com/blog/sucesso-operacional-vs-integridade-analitica)
[
Editor de imagens automatizado com n8n, OpenAI e Gemini
Caio César Pereira de Souza 11/03/2026 A construção de um editor de imagens automatizado no n8n pode ir além de simples manipulações estáticas. Neste fluxo, uma arquitetura orientada a eventos integra Google Drive, OpenAI e Gemini para criar um pipeline inteligente de análise e transformação visual.](https://www.ilegra.com/blog/editor-imagens-automatizado-n8n-openai-gemini)
Sobre
Cases
Serviços
Parceiros
Blog
Carreira
Contato
 
    
Aviso de privacidade Relatório de Transparência MTE © 2026 ilegra 
