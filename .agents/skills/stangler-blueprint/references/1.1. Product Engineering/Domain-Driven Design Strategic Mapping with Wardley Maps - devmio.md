---
name: Domain-Driven Design: Strategic Mapping with Wardley Maps - devmio
keywords: (placeholder)
metadata:
  url: https://devm.io/ddd/wardley-maps-169761-001
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Domain-Driven Design: Strategic Mapping with Wardley Maps
Search
X
Agile
Android
Angular
API
ASP.NET
AWS
Azure
Blockchain
Cloud
Containers
Continuous Delivery
C#
Databases
DDD
Delphi
DevOps
Digital Transformation
Docker
.NET
Eclipse
Game Development
Go
iOS
IoT
Java
JavaScript
Careers
Kubernetes
Machine Learning
Microservices
Mobile
Node.js
Online Marketing
Open Source
PHP
Programming
Python
React
Law & Net Culture
Ruby
Rust
Security
SEO
Serverless
Sharepoint
Software Architecture
Spring
Swift
Testing
TypeScript
UX
Visual Studio
Vue.js
Web Design
Web Development
Windows
WordPress
Xamarin
Skip to content
devmio – Software Know-How
Test now 
×
Products
For Individuals
For Teams
Download app
Products
Live Events
Conferences
Magazines and Specials
Features & Services
devintelligence
FAQ
Our App
Contact
Blog
Logout
Login
Login
Test now
Reactivate Subscription
Test now
Login
Test now
devmio – Software Know-How
Communities
Java, Agile & Software Architecture
DevOps, CI/CD & Platform Engineering
JavaScript, React & Node.Js
AI & Machine Learning
API Development, Design & DDD
PHP & Web Development
Conference Weeks
London | May 11 – 15, 2026
San Diego | June 1 – 5, 2026
New York | September 28 – October 2, 2026
Products
Magazines and Specials
Live Events
Conferences – Add-on
Solutions
For Individuals – Fullstack Access
For Teams – Fullstack Elevate
For Partners – Event Support
Features & Services
devintelligence
Experts
Insights
Mobile App
Blog
Login
Test now
Reactivate Subscription
Test now
Login
Test now
Strategic mapping with Wardley Maps
Domain-Driven Design: Strategic Mapping with Wardley Maps
DDD
Issues: Volume 9 
Strategic mapping with Wardley Maps
Domain-Driven Design: Strategic Mapping with Wardley Maps
DDD
Issues: Volume 9
Tom Asel
Only when we know the landscape around us, we can plan our way through rough terrain in a sensible way. Maps help us avoid obstacles, recognize chances on the way and find favourable starting positions for coming stages. So let's draw a map...
Strategic decisions should not be made from the gut, that much is clear. We need reliable information to plan our strategy. But how can we put this information together in a meaningful way so that a reliable picture emerges? Wardley Maps are a method of visually arranging existing assumptions to produce a picture that is not dissimilar to maps. The very act of creating a map, i.e., arranging components that are related to each other, can help us gain new insights. The method visualizes existing assumptions and makes them tangible for discussion. By checking (implicit) assumptions, a common understanding can be developed. Maps are very well suited as a means of communication for the presentation of complex issues and thus form a basis for the actual strategy development, but let us start at the beginning:
SEE ALSO: Using Siren to increase personal productivity and enable quick insights
We consider an exemplary scenario, which is based on a real use case. In this scenario a company offers its customers an overview of contracts and services via a web-based customer portal. The customer portal accesses a cloud-based CRM system and an internal system for contract management. The latter is connected to a standard SAP solution to handle deposit and withdrawal transactions. The customer portal, contract management and SAP are operated in-house in the company's own computer center, while the CRM is used as a software-as-a-service offering. The organization is also developing an app for customers which is connected to the customer portal via a backend. The app will offer the portals functions for mobile use. The development of the app and backend has just begun.
Fig. 1: A map of the example scenario
Figure 1 shows a Wardley Map of our scenario consisting of a reference point ( Anchor) and interconnected things of importance ( Components). The Anchor is the north arrow of our map, and positions are noted on the map relative to this reference point. On our map, the customer is the Anchor, so all components are aligned with the customer. Directly linked to the Anchor are components that represent requirements ( Needs). In our case the map expresses that the customer interacts with the components “App” and “Customer Portal”.
Components represent all things of importance in the context of our strategic consideration. They are abstractions, maximum simplifications of complex relationships. Software systems can appear in a map as a component just as services, knowledge or physical forces. Rule of thumb: If it is strategically important, it becomes part of the map as a component.
The vertical alignment of the components depends on the visibility of the Value to the customer (our Anchor). Components with which the customers interact directly are also directly perceptible to them and are therefore placed higher up. Components further down are less visible – but no less important – relative to the customer's reference point. The Value of a component and its visibility from the reference point are two different characteristics. The connections between the components result in a Value chain in which components build on each other.
About the method
Named after Simon Wardley, former CEO of Fotango and later Vice President Cloud at Canonical. In his book, he describes how dissatisfaction with current methods (SWOT analyses, 2×2 charts, …), unreliable advice from business consultants and management decisions made from the gut inspired him to seek new approaches to strategic planning. The method he called “Topographical Intelligence in Business Strategy” has established itself in many different application areas, also below the CEO level, under the name of Wardley Mapping.
The higher up a component is located, the more recognizable its Value to the customer. The further to the right it is located, the higher and more mature it is developed. The horizontal axis describes the degree of development ( Evolution). This says something about the character of the respective component: If we depict a software system as a component on the left edge of the map, we are saying that the system is at the beginning of its evolutionary development. The same applies to components that represent knowledge or methods. If a component is far left, this can mean, for example, that technologies or concepts have been used for which little knowledge is available within the organization. This gives the component an experimental character in the context under consideration. This also creates opportunities for new ideas and thus future potential for both competitive advantages and risks. On the left edge of the Evolution axis, the uncertainties are high. The further a component moves along this axis, the more mature it becomes, i.e. the lower the imponderability and the better the chances and risks can be identified and evaluated. The division of the axis into 4 segments illustrates this: In the first segment ( Genesis) the “creation” takes place. The focus is on research and exploration and the original creation of something new. The 2nd segment is about specific, tailor-made ( Custom Built) solutions. In the 3rd segment, a component receives the characteristics of a product in terms of its development and maturity. Components in the 4th segment are so far developed that they are ubiquitous and easily available ( Commodity + utility), comparable to electricity, radio reception or, thanks to cloud computing, processing power. Not all components reach the highest level of development, but they develop along the axis in this direction – of course at different speeds.
Now we have got to know all the building blocks to draw a map of a certain Landscape: We have a reference point ( Anchor) and can position strategically relevant elements ( Components) relative to it ( Value). Distances between the elements are distinguishable and significant for us ( Evolution). We can show this map to others to discuss the Landscape. The best way to create a map is to do this directly in a group, together with the respective experts. This will lead to valuable discussions: “Why is this so far down?”, “Why is 'X' shown further developed than 'Y'?”, “Is 'A' really part of the Landscape? Why is 'B' not shown? Where is my 'C'?”. Through critical examination, assumptions are challenged, and insights are shared – a common understanding is built and further promoted. If you think of DDD and the Ubiquitous Language, you are exactly right. As soon as we have a common understanding of the Landscape, we can turn our attention to the climatic conditions and transfer these to our map as well.
Climatic influences
Surface weather maps contain, in addition to the geographical representation of the Landscape, further information, e.g.: about high and low-pressure areas, wind conditions, precipitation and temperatures. The climatic conditions have an impact on the Landscape and influence the prevailing conditions. The more relevant details our map contains, the better we can see that the “best” way from A to B is not necessarily a straight line. Depending on the climatic conditions, a steep ascent on a rock face ( Landscape) marked on the map is exhausting but doable or even a life-threatening risk. This information advantage is crucial and, according to Simon Wardley, represents the difference between maps and classical methods of strategic planning (see box “About the method”). In order to develop a successful strategy, we must explicitly and consciously deal with those things over which we have little or no influence. While we take advantage of the Landscape and can change it to some extent, climatic influences elude our will: We cannot control them, but we can discover them and also use these insights to our advantage. Movements in markets, strategic decisions by competitors, technological or social change are climatic influences that we can and want to depict on our maps.
Fig. 2: Wardley maps with climatic influences
In Figure 2, climatic conditions are used to develop a strategy. App and backend are developed in parallel by the same team. The common context is made visible by the outline, as it plays a role for the strategic development. Both systems are still in an early experimental state and not ready for production. The UI has to be optimized and performance problems have to be eliminated to enable a positive customer experience and thus acceptance in the market. The red arrow expresses the desired movement along the Evolution axis. The software should lose its experimental character over time and maintain the characteristics of a mature product. The strategic decision is shown together with the hurdle to be taken: In our case there is a lack of knowledge and capacity, which is shown as a black bar. The bar describes the inertia to be overcome. Only if this hurdle can be overcome is the way clear for the Evolution from a custom-built system to a mature and competitive system with product character.
Cloud computing enables not only the use of SaaS but also alternative operating concepts for in-house developments, which has an impact on provisioning. The red arrow describes the step away from data center-based operation of standardized VM's ( Product) to container-as-a-service in a public cloud ( Commodity). However, this step cannot be taken without further ado, because resistance through inertia exists here as well. The know-how has to be built up, deployment and operations require new infrastructural measures, the organizations internet connection has to be redimensioned. If these challenges are mastered, new opportunities arise for other components on the map, so they can evolve. The backend benefits from moving to container-based provisioning and can be operated on a cloud-based model once the operating model is ready. The red line describes this connection of the components in the future. It is worth taking a closer look at the concept of Evolution for this purpose.
Evolution
Fig. 3: Evolution from the Uncharted to the * Industrialized Domain*
Evolution begins with the appearance of a component on the left-hand side, the so-called “ Uncharted Domain“. Its characteristics are marked by terms such as “experimental”, “chaotic”, “insufficiently understood”. We can hardly or not at all predict how things in the Uncharted Domain will develop, which results in a high potential in the future, but also in high risk due to this very uncertainty. The further a component develops, the more the uncertainty turns into certainty and allows for planning at industrial scale. Looking back at history we see the first laboratory tests with transistor-based CPUs. Later specialized small series were produced, which reached product maturity later on and could finally be produced cost-effectively in mass production processes in sufficient quantities, available for everyone. The further we move to the right edge of the map, the more we enter the Industrialised Domain. The ability to differentiate between products is decreasing, but they are well understood and can be produced and provided efficiently. Availability increases rapidly, the costs per unit drop. The more developed a component is, the more likely it is to be the starting point for new developments, which in turn can be used in the Uncharted Domain. CPUs manufactured in large numbers at low cost have been turned into server farms and finally into cloud computing, where computing power (not hardware) is ubiquitously available. In our example, the Evolution of the operating model from an in-house data center to cloud-based container services is the basis for the technological development of the backend. The app experiment develops into a mature product the further it advances into the Industrialised Domain.
Some hints on working with Wardley Maps
User Needs are above all. Users may be customers, stakeholders, …
Accept uncertainties. Use the map to identify them.
Assumptions should be clearly communicated. Questioning them should be appreciated.
All concepts must be designed for constant Evolution.
Proceed iteratively, apply what you have learned.
SEE ALSO: Controlled Chaos: Managing your Microservice Ecosystem for Business Agility
Making strategic decisions
So far, the purely visual properties of Wardley Maps have been discussed. With knowledge of the Landscape and the forces acting on it, we can now focus on the strategic decision-making process. Knowing the Landscape and the climatic influences we can derive individual actions and apply universal principles that apply in any context. Patterns help us to recognize and apply them. Simon Wardley describes this with the concepts of Doctrine and Leadership and provides pattern catalogues and stratagems to help with development of own strategies. These concepts are beyond the scope of this article, but they should not be left completely unmentioned. Together with the concept of the Strategy Cycle they form the true core of strategic mapping.
To illustrate this, we apply the collected knowledge and pick out the pattern “ No Single Method fits all“. It means that there is no method that can be applied universally to all components of a map. If we relate this to the different approaches to software development and transfer them to the concept of Uncharted and Industrialised Domain, the following picture emerges:
Fig 4: Different methods are more suitable depending on the degree of Evolution
Both app and backend are in the Uncharted Domain. This means that frequent changes can be expected, so to speak “by design”. It is an essential property of components in the Genesis phase of Evolution and thus of the Uncharted Domain. In this case, it makes sense to embrace constant change with agile methods in order to keep the resulting costs under control. Elements at the right end of the map are less subject to this change. Their characteristics are well known and therefore calculable. For in-house developments that make it to this stage, outsourcing could (not must! Avoid any dogmatism!) be an option. CRM, for example, is used as SaaS from the very beginning and is not an individual in-house development.
Conclusion, possible applications and outlook
We have briefly touched on the most striking features of Wardley Maps and illustrated them with simple examples. For more advanced topics such as Doctrine, gameplay, and the pattern catalogues, please refer to the freely available work by Simon Wardley, licensed under CC-BY-SA, as this article cannot provide enough space for all of this.
The development of a map in a team can be done in a workshop. The result may easily fill an entire wall. The next step is crucial here: Reduce to the essentials, e.g. by splitting a map into several. In this way, new insights into existing assumptions are constantly collected.
In the context of DDD Wardley Maps can be used to make strategic decisions about bounded contexts. What changes are emerging? Which team and which method is suitable for which region of the map? In which bounded context (not system!) is it worthwhile to invest in order to make use of new opportunities? Wardley Maps are another tool in our design toolbox that we can access when needed.
Although Wardley Maps were originally developed for strategic decisions at CEO level, we can use them wherever we need to get a picture of complex situations in order to make informed decisions. This applies to strategic architecture management for the enterprise architect, as well as for project managers and system owners who want to do forward (i.e. strategic) planning. Finally, the question can be taken up whether it is possible to represent complex real world scenarios with Wardley Maps. There is also a more than apt quotation from George Box, which Simon Wardley likes to take up:
All models are wrong but some are useful.
Links & further literature
Ebook by Simon Wardley freely available as a series of blog posts, licensed under CC-BY-SA:
https://medium.com/wardleymaps
Project page with reference and articles to get you started:
https://learnwardleymapping.com/
Tom Asel
Tom Asel is the co-founder of tangible concepts, a Java expert, and a specialist in software architecture. As a former Head of Software Engineering and Enterprise Architect, he understands every level of the software development process. In his work as a software architect, he empowers teams to work independently and efficiently while developing sustainable solutions. For him, long-term success lies in strengthening the collaboration of the entire team rather than relying on individuals. His extensive experience in architecture evaluation and analysis, along with his active membership in the iSAQB, distinguishes him as an experienced trainer and consultant who contributes to the advancement of modern software architecture.
More articles on this topic
[
Part 1: DDD, testing, and, modularity in Spring Boot
Introducing the Apache Causeway Java Framework: Your Next Modular Monolith
Dan Haywood](https://devm.io/ddd/apache-causeway-introduction)
[
What's it all about?
Domain-Driven Design: The Only “Sensible” Software Development?
Eberhard Wolff](https://devm.io/ddd/domain-driven-design-ddd-development)
[
Scenario casting lessons from a veggie subscription box
Harvesting Success with Domain-Driven Design
Jörn Koch](https://devm.io/ddd/harvesting-success-domain-driven-design)
[
Stream the live event: September 27, 2022 | 02:00 - 05:30 PM CEST
Join Our Live Event: Event Storming
devmio Editorial Team](https://devm.io/ddd/workshop-event-storming)
Start Your Journey to Software Know-How:
The Fullstack Experience
Experience our online live events, exclusive and interactive.
Thousands technical articles, magazines, cheatsheet and more.
Up to 25% discount for more than 30 conferences a year with international experts.
Exclusive content from over 30+ renowned software brands.
GET STARTED
More articles on this topic
[
Part 1: DDD, testing, and, modularity in Spring Boot
Introducing the Apache Causeway Java Framework: Your Next Modular Monolith
Dan Haywood](https://devm.io/ddd/apache-causeway-introduction)
[
What's it all about?
Domain-Driven Design: The Only “Sensible” Software Development?
Eberhard Wolff](https://devm.io/ddd/domain-driven-design-ddd-development)
[
Scenario casting lessons from a veggie subscription box
Harvesting Success with Domain-Driven Design
Jörn Koch](https://devm.io/ddd/harvesting-success-domain-driven-design)
[
Stream the live event: September 27, 2022 | 02:00 - 05:30 PM CEST
Join Our Live Event: Event Storming
devmio Editorial Team](https://devm.io/ddd/workshop-event-storming)
Social
Follow us on social media for more news and content from our experts and events. Share your personal experience with us!    
App
Access your digital knowledge base everywhere with our mobile apps.  
Check Out Our Offers!
Not convinced yet? Check out our training portfolio for free!
Learn more
Privacy
Terms and Conditions
Contact
FAQ
Imprint
iOS
Android
iOS
Android     
Gen AI Engineering Days 2024
Live on 29 & 30. October 2024 | 13:00 – 16:30 CEST
Register here
Subscribe our Newsletter
×
Sign Up: Submit
[mc4wp-simple-turnstile]
Leave this field empty if you're human:
