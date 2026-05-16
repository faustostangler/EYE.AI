---
name: 2026-05-10 How we design our product organization with DDD and Team Topologies | by RETIERE Samuel | Peaksys Engineering | Medium
keywords: (placeholder)
metadata:
  url: None
  source: SOURCE_TYPE_TEXT
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
WebSync metadata
title: How we design our product organization with DDD and Team Topologies | by RETIERE Samuel | Peaksys Engineering | Medium
url: https://medium.com/peaksys-engineering/how-we-design-our-product-organization-with-ddd-and-team-topologies-9002bbcb70a6
date: 2026-05-10T20:35:00.041Z
parsing method: defuddle
Sitemap
Peaksys Engineering
Behind the code: learn about our Tech culture and product developments
puzzle by KD under CC BY-2.0
Short version
This is the story of an organization which is moving towards a more product-led approach, and needs to align its human and technical organization. As we believe that the human and technical dimensions are intimately linked, we have adopted a methodology based on Domain Driven Design and Team Topologies. In this article we focus more on how we did it than why we did it.
Target audience
This article is primarily concerned with the practical aspects of organization design using DDD/Team Topologies, giving you everything you need to get started. This is not the best place to start if you are looking for different approaches to organization design, or if you are keen on learning more about DDD and Team Topologies.
Long version
Once upon a time there was an organization which decided to make its teams autonomous and responsible for their own products, giving them the means to constantly improve their delivery speed and adapt to an ever-changing environment. The purpose of this article is not to offer a detailed explanation of why this paradigm shift occurred, but rather to look in detail at how we can design human organizations which effectively reconcile strategy and execution. Firstly, some context: our story takes place in the logistics sector, in an organization whose initial structure is primarily focused on expertise. If the organization succeeds in developing new services, it does so in a slow, layered manner. As for speed, it all depends on your frame of reference. Suffice to say that we were not as fast as we wanted to be. Hence the decision to sit down and rethink the way we organize our human resources, adopting the following approach:
1. The starting point. Objective: identifying the dependencies which slow us down and restrict our autonomy. We also talk in terms of inter-team relations, inter-asset relations and relations between teams and technical assets.
2. Our products. Objective: defining clear areas of responsibility in order to promote engagement and accelerate decision-making.
3. Choosing the right target and options. Objective: involving stakeholders in the change
4. Getting there
To give you an idea of the workload, it took a team of 4 a full day to complete the first 3 steps.
The starting point
What we are looking for at this stage is to identify the human, functional and technical dependencies which exist within our organisation. We will then analyse them in light of our strategy. One important point to note: as per Conway’s law, we do not have three discrete layers which coexist independently of one another (human organization, business domains and technical assets), what we have instead is a single socio-technical system in which human, business and technical dimensions are intimately linked.
To launch our analysis, we started with the layer which is most stable in the long term, namely the functional layer. We thus organized two event storming workshops, which allowed us to identify our business domains. We proceeded as follows:
· To begin with, we got a bunch of experts together in the same room — people capable of explaining in functional and operational terms what is going on.
· For our event storming, we only used the objects we really needed, namely business events and orders. This allowed us to define the contours of our business domains.
We used the bounded context canvas to describe our business domains, which enabled us to fine-tune our definition. This step allowed us to make sure that we fully respected the definition of what constitutes a business domain.
· We then positioned these domains on the core domain chart. This would be useful later on when defining our choice of target.
N.B.: While the names of the domains do not fall into the category “sensitive data”, the same is not true of the positioning of the domains. We fed a random model into Excel to create an example.
· We then colored the business domains with reference to our event storming. The less complex domains are shown in light colors, and the others are darker. The colors represent their differentiation.
The first point to note is than not all of our domains are classified as core domains, which is good because it means that they are not all regarded as differentiating, which is always interesting. Further analysis reveals that we have one domain which is highly complex but with a low differentiating factor. This is annoying, because it suggests that there is a degree of excess complexity in our system. Our analysis is now well under way, and it is time to take it to the next level.
The next step is to map our technical assets, domain by domain. When a technical asset is present in two fields, we duplicate the post-it and draw a line connecting the two of them.
Onto this visual map we superimposed our teams, regardless of their geographical location. The resulting 3D map looks like this:
The first thing that jumps out from this diagram is that we have just one technical asset which is shared between multiple domains. This means that our starting situation is pretty clear cut, without too many instances of technical overlap lurking beneath the hood. We do have a potential sticking point in two domains where the distribution of teams is dependent upon the age of the technical stack (legacy or new stack) rather than the functional fields. At this point no action is taken, but we make a note of this point.
Our products
A more accurate title for this section would be “Our Strategy.” It is called “Our Products” because our strategic goal is to move towards a product-oriented organization, where we define “product” as followed: “A product is a software program, a system, a service or a combination of the above which generates value for a client or partner.” To put it bluntly, we are not dealing with 18,000 different value chains in the logistical sector. It basically boils down to delivery requests and package preparation. Without getting sidetracked into a lecture on product management, we can consider the logistical value chain as the first element of our product breakdown, and our professional fields as the second defining factor of what constitutes a product. In practice, this leaves us with one product manager for each business domain, and potentially more product managers spanning multiple domains. At this stage, since we regard our business domains as akin to products, it is time to clarify our product vision and strategy. This serves to confirm our intuition that we are indeed dealing with a product, as per our own definition.
Choosing the right target and options
It is at this point that we turn to the concepts of Team Topologies regarding cognitive load management. No team should be left to manage more than one complex domain and a maximum of three simple domains. With rare exceptions, no domain should be the exclusive property of a single team. With these principles firmly established, and on the back of our 3D mapping exercise, it becomes clear that there are not 10,000 options available to us:
· First decision: to stop the legacy/new stack division of labor and create teams responsible for handling both within a given perimeter. This will undoubtedly accelerate technical convergence.
· Once the complex and/or differentiating domains have been shared out, it soon becomes clear that we have more options at our disposal in those fields which are not complex or differentiating. We can place them on the right or the left, it makes little difference. This gives us some room for manoeuvre to create stable teams, in terms of the minimum size of our teams as well as the skills represented in each team.
This leaves us with a target we can’t share in this article. As you can imagine, it wouldn’t be a great idea to publish a comprehensive list of all of our technical assets, business domains and teams. At this stage we felt it would be better to focus on a potential result.
Getting there
Since the purpose of this article is to explain how to establish a product-oriented organizational structure, we will save the “why” for another article. But rest assured: we have already put the structure described in this article into practice, and it is working. Can we stand up and say that we are already delivering faster thanks to this change? Not yet. We need to let the strategy bed in, and take the time to properly assess the impact of these changes on our time to market. Stay tuned.
Last published Feb 5, 2026
Behind the code: learn about our Tech culture and product developments
