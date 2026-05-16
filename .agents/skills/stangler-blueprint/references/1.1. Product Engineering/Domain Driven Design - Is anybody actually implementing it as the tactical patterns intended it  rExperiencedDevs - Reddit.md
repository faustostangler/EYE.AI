---
name: Domain Driven Design - Is anybody *actually* implementing it as the tactical patterns intended it? : r/ExperiencedDevs - Reddit
keywords: (placeholder)
metadata:
  url: https://www.reddit.com/r/ExperiencedDevs/comments/11ohfyn/domain_driven_design_is_anybody_actually/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Domain Driven Design - Is anybody actually implementing it as the tactical patterns intended it? : r/ExperiencedDevs
Skip to main content Domain Driven Design - Is anybody actually implementing it as the tactical patterns intended it? : r/ExperiencedDevs
Open menu
Open navigation 
Go to Reddit Home 
r/ExperiencedDevs
Sign Up
Sign up for Reddit
Log In
Log in to Reddit
Expand user menu
Open settings menu
Skip to Navigation Skip to Right Sidebar
Back
Go to ExperiencedDevs
r/ExperiencedDevs
•
3y ago
[deleted]
Locked post
Stickied post
Archived post
Report
Domain Driven Design - Is anybody actually implementing it as the tactical patterns intended it?
I've been at various shops that had people preach the greatness of DDD, and yet - I've never actually seen DDD being fully implemented as intended by Evans back then. Everybody seems to think that this is the holy grail of system design, yet I have not seen any team fully commit to it.
"Domain-centric architectures" (e.g. onions), bounded domain contexts (well designed microservices), sure, all of that works and I have seen several teams structure their systems that way on the "strategic" level.
But is anybody actually implementing DDD on the tactical code level as it was described in the original book? What I mean are, for example, aggregate objects that are always fully loaded and saved to / from repositories using the transactional patterns described by Evans. Or, heavy use of domain events and observers within a bounded context.
After reading the DDD book I just got the impression that you would quickly arrive at a DB bottleneck for anything nontrivial and that the heavy use of indirection through domain events within a bounded context would make systems really hard to follow and understand.
If you do work at a shop that strictly follow the code patterns of DDD, how do you like it?
Would you repeat it for your next greenfield project?
Upvote 99 Downvote 37 Go to comments Share
Sort by: Best
Open comment sort options
Best
Top
New
Controversial
Old
Q&A
Search Comments Expand comment search
Cancel
Comments Section
jhartikainen
•
3y ago
Good question. I like the ideas presented in the book as well, but I have the same concerns about "heavy" DDD design - it seems it has so many extra layers of abstraction for sake of having that abstraction that you end up having tons of extra work and complexity for little gain in the average project.
Perhaps it would make sense in some fairly large scale system, where you have multiple teams working on different modules, where having those abstractions could help with integrating the modules together with less friction... but hard to say as I've yet to work in such a way.
Personally I approach DDD the same way as design patterns and such in general - pick what seems reasonable, ignore the rest.
Upvote 52 Downvote Reply Award Share
Report
Award
Share
Atomfinger
•
3y ago
This is my reading as well: DDD being more like a toolbox rather than a recipe (where one presumably has to use all the ingredients).
Upvote 19 Downvote Reply Award Share
Report
Award
Share
g3t0nmyl3v3l
•
1y ago
This is a pretty old post, but for folks searching around Reddit in the future — DDD is intended to be used only as deep as you need it. You don't need to use the tactical patterns from DDD for every piece of code, in fact it's explicitly recommended that you don't!
If a concern is very simple, DDD encourages you to use an appropriately simplistic approach. DDD is intended to help when you reach higher complexity. Most healthy DDD projects of a decent scale likely have a good number of simplistic integrations/sub-systems driving it.
Upvote 7 Downvote Reply Award Share
Report
Award
Share 
[deleted]
•
3y ago
On the technical side, no. The main benefit I found is in getting to a common language between you and your (non-tech) stakeholder. And carrying that language through to the code.
Upvote 31 Downvote Reply Award Share
Report
Award
Share 
Main-Drag-4975
•
3y ago
• Edited 3y ago
Is that not how people program already? Seems like it'd be extra work to do anything else.
My paid coding experience has been almost exclusively web-adjacent for businesses though — maybe there's a flavor of programming where shared domain concepts are easier to lose sight of while building?
I started with full stack Rails, specialized into backend, cloud, and distributed stuff. Mostly building things for businesses, usually where someone else knows the business backwards and forwards and I'll have to learn to speak their language in order to effectively support it it in the systems I create.
I guess this miiiight be more naturally domain-y than building device drivers or databases or game engines or something.
Upvote 13 Downvote Reply Award Share
Report
Award
Share
More replies
MuNot
•
3y ago
I have. My first position out of college was at a startup in the growth phase that did DDD from the get go. That startup was acquired by a big tech company and I ended up being something of a DDD evangelist, I've literally traveled the world doing DDD workshops for a few companies.
The big thing to understand about " The Blue Book ", as much as that make it sounds like a cult, is that it isn't a deep technical book. If you watch lectures on DDD by Eric Evan's or pay attention to the book, you'll see he's a brilliant guy but operates on the theoretical level. Bringing those concepts down into code can be challenging.
When it comes to code implementations I've personally found that domain events intra-service can be overly complicated and confusing in most frameworks. However cross-service events is just the same as an event based architecture. Evaluate the tradeoffs between choreography (event based) and orchestration (flow-based).
The repository method can be stressful on a DB but I've seen this scale much more efficiently that the traditional approach. The big mistake I see people make is creating aggregates that combine master data (configurations) with transactional data. Iterating over the model to keep those two separate goes a long way, as does making the correct aggregates to reduce how much data you need to pull up: don't create a "CustomerTransactionHistory" aggregate that contains a list of CustomerTransactions as a child, that's too much data. You're probably much better off just having a 'CustomerTransaction" aggregate.
If you do the model first then create a schema based on that then you can easily just take your repository methods and ensure you have a compound index per method: that'd be 80% of the work to extremely fast queries.
The biggest issue with DDD is that it takes a few attempts before people learn it, and it's an up-front heavy design approach as you'll need to figure out your models before you can go hands on keyboard. All those layers of abstraction are there to ensure flexibility and agility on the large time scale, but companies are hesitant to trust that time spent without results now will lead to faster results in the long run. Add to that that DDD absolutely requires the buy-in of product and they're ability to deeply understand the problem domain and serve as domain experts, and you'll quickly see that the biggest obstacles to adaptation are organisational, not technical.
DDD is first my approach to software development and architecture. The only time I wouldn't advocate for it is if the problem space I'm operating has low business complexity but high technological complexity, or if what I'm developing truly is something that is not going to require major maintenance or extension once finished, and can be off on a server running without intervention for years.
Upvote 46 Downvote Reply Award Share
Report
Award
Share
5 more replies 
Main-Drag-4975
•
3y ago
Does anyone have a short explanation of what DDD even is? I've tried to get into the book a few times and so far it seems just like regular software design to me. The folks I know who swear by it simply tell me to go read the book 😔
Upvote 22 Downvote Reply Award Share
Report
Award
Share
KeisukiA
•
3y ago
A lot of the best insights are those that just seem like common sense, once you know them.
Upvote 8 Downvote Reply Award Share
Report
Award
Share
[deleted]
•
3y ago
Comment removed by moderator
More replies 
[deleted]
•
3y ago
Domain Driven Design made Functional is a great book. Makes my life easier.
Upvote 16 Downvote Reply Award Share
Report
Award
Share
2 more replies
[deleted]
•
3y ago
Comment deleted by user
4 more replies 
funbike
•
3y ago
DDD is not an all-or-nothing approach. There are many articles and videos with DDD experts explaining this. @CodeOpinion has several good articles about this.
I'd be afraid to go all-in on a long term DDD project with a mix of juniors and seniors. The conceptual integrity of the design would likely degrade. I wouldn't do it without a bunch of lint rules that prevent people from breaking the rules (e.g. inappropriate coupling or leaky abstractions).
Upvote 5 Downvote Reply Award Share
Report
Award
Share 
[deleted]
•
3y ago
• Edited 3y ago
I pick the strategic bits and the most impactful part for me is the ubiquitous language. (I recall Evans mentioning at one DDD EU conf that he wished he would have put that in an earlier chapter).
I tend to combine it with event sourcing and CQRS within the context and event driven messaging external to the context.
At a tactical level, I can't say I pay much attention to it and it tends to work against what other devs prefer for tooling. For example, my day-to-day is c# and entity framework already works well as a unit of work so trying to also be strict about repositories can feel a bit rough vs having well-isolated domain services. Some degree of mechanical sympathy is always worth keeping in mind.
edit: Also, value objects everywhere. I do love those.
Upvote 2 Downvote Reply Award Share
Report
Award
Share 
Inside_Dimension5308
•
3y ago
I am trying to get some good online examples for DDD. I don't want to read the book. If someone can help me, that would be great.
Personally after going through the educative course on DDD, I understood that it is a powerful tool for complex system designs. For simple systems, any approach works.
Upvote 2 Downvote Reply Award Share
Report
Award
Share
BrownCarter
•
2y ago
But with time simple systems become complex
Upvote 1 Downvote Reply Award Share
Report
Award
Share
More replies 
[deleted]
•
3y ago
Ive only ever worked at companies where the CTO/lead was into DDD and designed stuff according to it but none of the devs read the DD book and just wrote code, some code was written with aggregates/other DDD constructs by the leads and it was invariably the slowest, buggiest and most hard to understand part of the code by far, very simple things required a bunch of different classes and separations of data which made it impossible to do anything efficiently, if all the devs had been using that style the company would have collapsed
DDD has some good ideas but like always once it becomes a target to make your design look like the examples in the book you end up doing stuff that isn't right for your code
I'd tell a developer to read a distilled version of the book, take away some of the stuff about vocabulary and then use it if they actually need it, which for CRUD application #35345 you don't
Upvote 2 Downvote Reply Award Share
Report
Award
Share 
[deleted]
•
3y ago
• Edited 3y ago
I implement some ideas, but stray away from a dogmatic DDD. I found that there are concepts which didn't quite work.
For instance, in simpler domains the Value Objects were redundant and we ended up being happy with most checks done by Application Layer (i.e. Swagger). Other concepts simply didn't work-like Aggregate Root. Aggregate root looks great on paper but dogmatically loading your whole root that consists of thousands of results is no fun and people still try to wrestle with it to make it right. Vaughn Vernon proposes making your aggregates smaller, but this only works sometimes. Also, if you make them too small like entities, then there is no point as you loose the whole idea of consistency and transactional boundary. Vladik Khononov opts in for lazy loading entities (meaning partially) from aggregate, but then purists say it's anti-pattern. Not to mention consistency across aggregates, and you lose all of that. Since aggregate roots are objects loaded in memory it opens up doors to phantom reads, last write wins, lost update problems (etc etc). Optimization with more complex Database queries is also a problem here, because of in-memory nature of domain logic.
What works invaluably in my view are DDD's integration patterns between domains (i.e. Consumer/Supplier, Conformist) and the entire concept of Bounded Context.
Upvote 2 Downvote Reply Award Share
Report
Award
Share
tilutza
•
2y ago
DDD is a tactial choice just to put business in code. While I agree with the book itself, in real world you also have to work with other people, and it means you have to make compromises.
Since I have use it successfully these patterns in the past, I am building a real world SaaS using DDD and I describe all the process on YouTube: https://www.youtube.com/watch?v=zuOwzVWpo8I
Upvote 1 Downvote Reply Award Share
Report
Award
Share
Many_Particular_8618
•
2y ago
Ddd is nothing without event sourcing.
Upvote 1 Downvote Reply Award Share
Report
Award
Share 
Waksu
•
3y ago
I am working in a pretty mature and successful organization with strong emphasis on code quality and we use DDD in 5-10% of microservices, because the rest of them are CRUDs where you don't need to complicated stuff.
Upvote 1 Downvote Reply Award Share
Report
Award
Share
tomcizek
•
3y ago
I rarely saw that, my experience is that most of people saying they do DDD, but dont use tactical patterns. I did it in few projects, but I would not recommend building your core blueprints/abstractions without previous experience. But I would recommend to marry DDD with at least CQRS, optionally event sourcing and use some framework to have guidance and solved problems you dont want to be solving. I use axon framework I am very satisfied with. There is also Akka, thats actor model, but have good community and could be leveraged too for sure, but not sure if there is such strong guidance as with axon... Dont know about tools in other languages on same level, but would love to explore if anyone have a tip!
Upvote 1 Downvote Reply Award Share
Report
Award
Share
pookdeveloper
•
2y ago
I would like to know a real case example. When do you need to make a second implementation of something? It only occurs to me in the case of different types of login
Upvote 1 Downvote Reply Award Share
Report
Award
Share
New to Reddit?
Create your account and connect with a world of communities.
Continue with Email
Continue with Phone Number
By continuing, you agree to our User Agreement and acknowledge that you understand the Privacy Policy.
Related Answers Section
Related Answers
Alternatives to Domain Driven Design
Learning resources for Domain Driven Design
Relevance of Domain Driven Design today
Best practices for code reviews in teams
How to handle burnout as a developer
More posts you may like
Is there a more "lightweight" methodology/architecture than MagicGrid? r/systems_engineering • 3y ago [
Is there a more "lightweight" methodology/architecture than MagicGrid?
](https://www.reddit.com/r/systems_engineering/comments/11hl0s6/is_there_a_more_lightweight/) 7 upvotes · 8 comments
Happy DDD Devil Dany Day 😈 r/TheWarning • 8mo ago [
Happy DDD Devil Dany Day 😈
](https://www.reddit.com/r/TheWarning/comments/1n9mkjf/happy_ddd_devil_dany_day/)  youtube 49 upvotes · 3 comments
Managing User Stories/AC With Third Party Best Practice? r/agile • 3y ago [
Managing User Stories/AC With Third Party Best Practice?
](https://www.reddit.com/r/agile/comments/10hmvdz/managing_user_storiesac_with_third_party_best/) 3 upvotes · 8 comments
What are your thoughts on DDD r/csharp • 1y ago [
What are your thoughts on DDD
](https://www.reddit.com/r/csharp/comments/1jaq72n/what_are_your_thoughts_on_ddd/) 35 upvotes · 33 comments
What is the best and worst thing about this book? (if you have read it) r/DomainDrivenDesign • 2y ago [
What is the best and worst thing about this book? (if you have read it)
](https://www.reddit.com/r/DomainDrivenDesign/comments/192eias/what_is_the_best_and_worst_thing_about_this_book/) 4 upvotes · 8 comments
Domain Modeling Made Functional (or how Type Driven Design works) r/programming • 3y ago [
Domain Modeling Made Functional (or how Type Driven Design works)
](https://www.reddit.com/r/programming/comments/zsw6s7/domain_modeling_made_functional_or_how_type/)  youtube 12 upvotes · 2 comments
ELI5: What is Domain Driven Design really? r/programming • 10mo ago [
ELI5: What is Domain Driven Design really?
](https://www.reddit.com/r/programming/comments/1m2agkc/eli5_what_is_domain_driven_design_really/) 8 comments
Experienced devs in large orgs: has something like this ever happened to you? r/ExperiencedDevs • 3mo ago [
Experienced devs in large orgs: has something like this ever happened to you?
](https://www.reddit.com/r/ExperiencedDevs/comments/1qpse3v/experienced_devs_in_large_orgs_has_something_like/) 211 upvotes · 131 comments
My teammates are generating enormous test suites now r/ExperiencedDevs • 5mo ago [
My teammates are generating enormous test suites now
](https://www.reddit.com/r/ExperiencedDevs/comments/1po8uud/my_teammates_are_generating_enormous_test_suites/) 458 upvotes · 240 comments
DDD (Domain Driven Architecture) - Trop compliqué pour rien ? Pas assez optimisé côté SQL ? r/developpeurs • 2y ago [
DDD (Domain Driven Architecture) - Trop compliqué pour rien ? Pas assez optimisé côté SQL ?
](https://www.reddit.com/r/developpeurs/comments/1ggqdgz/ddd_domain_driven_architecture_trop_compliqu%C3%A9/) 30 upvotes · 22 comments
Spec Driven Development and other shitty stuff r/ExperiencedDevs • 2mo ago [
Spec Driven Development and other shitty stuff
](https://www.reddit.com/r/ExperiencedDevs/comments/1reiro1/spec_driven_development_and_other_shitty_stuff/) 39 comments
LS-Dyna or Explicit Dynamics? - Meshing and General Help Requested r/fea • 3y ago [
LS-Dyna or Explicit Dynamics? - Meshing and General Help Requested
](https://www.reddit.com/r/fea/comments/10ponu3/lsdyna_or_explicit_dynamics_meshing_and_general/) 9 upvotes · 12 comments
Open source DDD project, to learn DDD r/DomainDrivenDesign • 1y ago [
Open source DDD project, to learn DDD
](https://www.reddit.com/r/DomainDrivenDesign/comments/1kwrxy5/open_source_ddd_project_to_learn_ddd/) 36 upvotes · 8 comments
How do you validate domain? (DDD) r/dotnet • 4mo ago [
How do you validate domain? (DDD)
](https://www.reddit.com/r/dotnet/comments/1qke9vs/how_do_you_validate_domain_ddd/)  5 upvotes · 22 comments
Thoughts on Implementing Domain-Driven Design in Go? r/golang • 2y ago [
Thoughts on Implementing Domain-Driven Design in Go?
](https://www.reddit.com/r/golang/comments/1ex50kr/thoughts_on_implementing_domaindriven_design_in_go/) 34 upvotes · 12 comments
Refactoring UI? A good resource for getting more confident about frontend design and fixing that feeling of your app looking "off" without being able to tell exactly why? r/Frontend • 3y ago [
Refactoring UI? A good resource for getting more confident about frontend design and fixing that feeling of your app looking "off" without being able to tell exactly why?
](https://www.reddit.com/r/Frontend/comments/11cbih5/refactoring_ui_a_good_resource_for_getting_more/) 45 upvotes · 30 comments
A Hypothetical Proposal: Incorporation of a more robust algorithm for task prioritization. r/orgmode • 3y ago [
A Hypothetical Proposal: Incorporation of a more robust algorithm for task prioritization.
](https://www.reddit.com/r/orgmode/comments/10oxwgv/a_hypothetical_proposal_incorporation_of_a_more/) 13 upvotes · 5 comments
DDD Projections in microservices in application layer or domain modeling r/dotnet • 5mo ago [
DDD Projections in microservices in application layer or domain modeling
](https://www.reddit.com/r/dotnet/comments/1pj6bn9/ddd_projections_in_microservices_in_application/) 2 upvotes · 6 comments
Bringing up tools you never used in System Design Interviews r/ExperiencedDevs • 4mo ago [
Bringing up tools you never used in System Design Interviews
](https://www.reddit.com/r/ExperiencedDevs/comments/1ql8rz5/bringing_up_tools_you_never_used_in_system_design/) 57 upvotes · 32 comments
How to convince managers that developer-driven automated testing is valuable? r/ExperiencedDevs • 7mo ago [
How to convince managers that developer-driven automated testing is valuable?
](https://www.reddit.com/r/ExperiencedDevs/comments/1o7v94c/how_to_convince_managers_that_developerdriven/) 131 upvotes · 136 comments
How do you drive improvement in teams that are resistant to change? r/ExperiencedDevs • 1y ago [
How do you drive improvement in teams that are resistant to change?
](https://www.reddit.com/r/ExperiencedDevs/comments/1kts7ij/how_do_you_drive_improvement_in_teams_that_are/) 110 upvotes · 81 comments
How do you guys keep documentation up to date on your teams? r/ExperiencedDevs • 8mo ago [
How do you guys keep documentation up to date on your teams?
](https://www.reddit.com/r/ExperiencedDevs/comments/1nebg0u/how_do_you_guys_keep_documentation_up_to_date_on/) 25 upvotes · 56 comments
Other Teams Refuse Version Control r/ExperiencedDevs • 4mo ago [
Other Teams Refuse Version Control
](https://www.reddit.com/r/ExperiencedDevs/comments/1ql3nj9/other_teams_refuse_version_control/) 112 upvotes · 115 comments
Development before Agile r/ExperiencedDevs • 6mo ago [
Development before Agile
](https://www.reddit.com/r/ExperiencedDevs/comments/1p52mvd/development_before_agile/) 49 upvotes · 127 comments
Domain-Driven Design Explained by a Senior Backend Developer r/Backend • 4y ago [
Domain-Driven Design Explained by a Senior Backend Developer
](https://www.reddit.com/r/Backend/comments/y08bdm/domaindriven_design_explained_by_a_senior_backend/) 29 upvotes · 1 comment
View Post in
繁體中文
Français
简体中文
日本語
Русский
Português (Brasil)
See more See fewer
Srpski
Ελληνικά
한국어
Română
Bahasa Melayu
ไทย
Svenska
Suomi
Čeština
Norsk (Bokmål)
বাংলা
Community Info Section
r/ExperiencedDevs
Join
Experienced Devs
For experienced developers. This community should be specialized subreddit facilitating discussion amongst individuals who have gained some ground in the software engineering world. Any posts or comments that are made by inexperienced individuals (outside of the weekly Ask thread) should be reported. Anything not specifically related to development or career advice that is specific to Experienced Developers belongs elsewhere. Try /r/work, /r/AskHR, /r/careerguidance, or /r/OfficePolitics.
Show more
Public
Anyone can view, post, and comment to this community
Top Posts
Reddit reReddit: Top posts of March 11, 2023
Reddit reReddit: Top posts of March 2023
Reddit reReddit: Top posts of 2023
Reddit Rules Privacy Policy User Agreement Your Privacy Choices Accessibility Reddit, Inc. © 2026. All rights reserved.
Expand Navigation
Expand Navigation
Collapse Navigation
Collapse Navigation 
0cAFcWeA4IqG3Q5G4vkr6bnoYJ3CqR3vPRO6lc-GP-fsLsDeDmktLCLUD_aVedw9LEzzryIyfm7X5CbjIzagkRSipZb-qhM4iwta13JbhhJC_pCc9TI3ZlVOAq8dQjTYRXlSRu_r7c3DuhmiwmMEwfeoNcEuQ0yrT-893VYD6ezHbtnUaDy3ykiBuPE0snu6OW4Lum5E0Hes6GUGMfdMRY6Q-07r_NAwhz36qTTAixvmGd610VccJtqOuY_jBTF9BUTwX6yZOzI7qX9mVbYHCtTxeNAoJgUuicAKoq_SCIIv9w13pOQlWspLt_eZCW4mZKfnCb9xnGA4t3RZ7EOsp_VaZExCMjM2RCF49Nmxn0wZ4WRf98CR6zyJckyEBI-vsjm4BgNl9rBqRxeVcIcRZM9Id74vQlNEdObdt-4r_uO0T3OyXqCbVuGIUAD-7wVHg1GPKox6O8kGUNbuTPnmw9beUoqAID15XCnAxZ6XhqV0p3wUVs4GuJgej-WqFB_3z8Zq0mBGI1NvGIMyT4YH-h7HIKUJ344c5Xej8V4sDeDviJznb8hL7QGhWoOhIfyOTkHCarPTplaXdmQRBV9yePs4ReBepsAodn7wZZC6qCZxXFDGmLhAgNYaISL3d1kCSyasyvu47htfWzJIDOsm5tTWNAfrnBOvt7ic4wPdy5wTd4lHQ7q8GLJWp0i17WhfPhYJiB3Pi_x8kxzgtI4lKjr31UkI9sofsvfVHbd34qSOQY6FgwioMxIpqVBD3lS-vFYbtlRbesEjlOC0wLpyg2hLdMLMw03rIqSgy8arV-D7r9_SXY2EpS6pHg0eEpZZ0ohqeW65Bd00PiEYmfLXwVuxWlyebB1-onTMkmq5ipzE0t-u1OIdilaiBRiP67lhtZH86yYPL0x9Q43WsY3-AG4hW8RO5stMr1kbTcePBySuilVwffS0oEnPH8wz3QbuuvZlq8DDSl1RyuStuOo-OL71u0cYeiCsde8a2nx8S3rl8jiezf-MJoPYlANBbPMuq4M4ke92kYNY8GJsMrzvAJVeDLbaXZiPQ9VgNbyaY811VEUCkvCRvqedjODAofBu8kOjUxbqUwinlHkFh2AwDb-yPFSjbIH_AtE-t6cpwyEXeJ30DZSPphpp7suM54opgfxmKmDZvEVZtLpkPsAC6mI587V2YiCDKqhVi6e6ULsH8PS4H4HRQV3Wj72YeUmq2t_QZ0gan2DAMdKcA0qDPuHs_qWHyIn8WrVsFa9olOSXT0c5LlgveB7lRNQaambvDoyclTBn4ubfon9ZZ3kWcimWf6oVX_9kg38OsSOC1TpQYfHw9DToHLf_1nFgZ0dcXjBYRLKU0sLMDUue90TNf0-NJJwrVeUHsd7613Lu7kxhUBQZ152Pv-XBnFlF6FFi-w2VR-7taubxg5CJMoHFiouQ_-TksvEyKJpMuEk0wtlmO_O_1r_mr7HIlj80Bo_1qlsODOPDi6Kq9QbnbxV4a-XZN-0KV6xNl2YTOACW4hiN9i7TdgKQ0dIGIyJmnhzckeL5OcPxWJiipZIfBHtlX5sW9DeqDxAua4slcKX885FRsXmBGd3pYBVM0BZHJOF_NCWdpAv_EU9YKpiTPnPN_fe-9c2Tx2eux7dhJff4F-YZg1qdl7HNqkFl6WY2PlaMjaxcClLBNSRYoB__cF8xdxOYqNIhDAQW1gurI8xWCmQseDdDy3EzJy65aju9C1uflN95ham2qNzIopbFBnhYCiODwc2DuvDa_4Ukh0a4EoBL0NZSjtpNbQjRQDgoIYgyDRlgaMlriIIb3K1Ui30jqcnM_K-immStIhylM_pHX5qobWcG2r7xZu1ZNduyKbkxWt_2Q4aPwRQDGFvfLnhxPyv48D7mq9pjq9BIw8k4mJyWejeYcmKkTWHkXB9UQ1YlRxQw_JPH9O1zEmthXNYrCr5AUzneZcro0NGG22sC-ebp8nc1Vd5J6rS7nkV-VVRhi91MLO0-A7UWcEyM5pEWkuhKIKw0MKePACT_qjchWl4AzByJA2x_CnDDRM3-wLyDNgii7qC7fRIu_nkc4VMe7A5mQQVizGK4a3X7NaJbxnChSYy1ozuKHE9Z1EJqBFpJIqV3H2tR2FLE37wn0YISNIdrLGxpE943bApcPClQOAtyVfDN78PZsWkvKmTb2Op26R6Xkzd7VRwYtpxnsA60IO0CP4I_F5lP8GavF-6elVh8y19r-bxJvHik4
