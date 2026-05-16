---
name: 2026-05-10 The Fallacy of the Speed / Cost / Quality Trade-off | by Jeff Kolesky | Medium
keywords: (placeholder)
metadata:
  url: None
  source: SOURCE_TYPE_TEXT
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
WebSync metadata
title: The Fallacy of the Speed / Cost / Quality Trade-off | by Jeff Kolesky | Medium
url: https://medium.com/@jeffkole/the-fallacy-of-the-speed-cost-quality-trade-off-fdcd83b1c2a5
date: 2026-05-10T21:35:13.505Z
parsing method: defuddle
Sitemap
Making trade-offs is a mandatory part of engineering. Our job is a discipline of delivering the best possible solution to the problem, as defined, within the constraints set.
Engineer emeritus, Billy Koen, put it best in his “Definition of the Engineering Method”:
[The engineering method is] the strategy for causing the best change in a poorly understood or uncertain situation within the available resources.
This is why engineering is more than a purely technical job — it actually demands quite a bit of creativity. You can never get everything you want, at least not all at once.
There is this “theory” that has been in the project management world for a while that of speed, cost, and quality, we can only have two. People who believe this think that if you want a project to be delivered quickly and cheaply, then it must be of low quality. Or, if you want a very high quality product and you want it delivered fast, then it is going to cost a lot. Or, if… well, you get the point.
A small amount of very shallow research (i.e., skimming a couple pages on Wikipedia) reveals that the common knowledge is actually a misrepresentation of the original concepts of Quality, Cost, Delivery and the Project Management Triangle. In the QCD model, if one of the three dimensions is sacrificed, the others will be as well. The project management triangle actually has speed, cost, and scope as the vertices of the triangle with quality filling in the area; if you change the speed, cost, or scope, you will affect quality. Neither of these original models says that you can maximize two at the expense of the other, and both are tied into old fashioned industrial manufacturing that may still apply to that realm but should not be used as a metaphor for modern creative technical work.
How can we have it all?
The answer is quite easy — focus on quality first. DevOps Research & Assessment have been doing research since 2014 to understand what makes high performing engineering teams. What they have found may sound counterintuitive, but, since it is research and not just theory, I’m inclined to believe it.
The teams that focused on quality are the ones that gained speed.
The research used a proxy for quality based on how much rework and unplanned work was being done, but let’s think about this from the day-to-day point of view of a line engineer.
I’m writing some code. I write some tests to make sure that code works. I have an easy and quick way of verifying that code works correctly with the rest of the code in the system. I get another engineer to review my code and my tests. Once that’s done, I merge the code, and it goes through an automated system to check it for correctness, security, performance. If all goes well, it gets pushed to production and metrics are checked automatically, triggering a rollback if something is wrong. With that level of process, I have full confidence that I can quickly deliver a high-quality change and react to it if needed.
But that is only quality delivered as part of the development process. What does quality look like from the perspective of a product manager, a CEO, or any other partner of the engineering team? The focus for all should be on delivering value to the customer. Quality here may be something as tactical as building in the ability to do A/B testing to test a feature’s value. Or it may be more high level like setting priorities and keeping a steady hand at the helm. It may be a focus on simple solutions to customers’ problems. Or it may be putting in place process to communicate clearly across the org and push decision making out to the edges. All of these quality practices enable faster delivery of value to customers.
The speed depends on quality, and the quality depends on speed. It is a virtuous cycle.
How do we lower costs then?
Cost comes in two clear forms and many less clear forms. The most obvious form, and often the biggest line item on a budget, is people. But, we also pay for compute, storage, memory, network, and other things I will happily classify as resources. If we are building iteratively and have confidence in each small change we push out, then everyone can make changes quickly. That leads to each person being able to contribute more, and if each is contributing more, you need fewer people to achieve the same thing. That’s cost reduction. On the other side of the coin are the resources. If we can ship quickly and iterate, we can build a first version that works and then focus on optimizing resources once we know where the pain points are. That’s cost reduction.
There is another set of costs that are much more nebulous — the communication overhead costs, feature carrying costs, tech debt friction. Those are not addressed as directly, but they certainly can be addressed one by one if a high quality process is kept up.
Is quality always important to focus on first?
There are certainly times when you don’t even know if what you are building is worth being built. In those cases, you should focus on doing whatever the smallest thing is possible to figure that out. It may mean that you do not write an abundance of end-to-end tests or maybe even not that many integration tests. But you probably are writing unit tests, since those should be fairly quick to write and run. You maybe choose to not put a lot of time into having a fully automated continuous delivery system, and that is fine. You can certainly sink time into building up processes that are not good investments. So, build a prototype with “lower quality” in order to get speed to market to test out if your product is worthwhile. If you figure that out, and you have an understanding of your market and your product, then focus on building up those habits of quality and all will fall out from there.
There are plenty of examples of other industries following this model. Automobile design builds clay models before production vehicles. Architects put together cardboard models before final blueprints. Hardware development tests out designs on breadboards before committing to etch silicon. I’d venture to say that if we started talking about these as being “lower fidelity” rather than “lower quality,” we could build prototypes fast and still keep the levels of quality that give us the confidence we need.
Nah, just get me my features fast and cheap!
I’ve made the argument so far that focusing on quality first gets you speed, and from that you can get the right features built at the lowest cost. But, what if you absolutely positively have to have it the next day… every day? This is often the pressure that “the business” puts on an engineering team — to deliver product to market now! The 2017 edition of the State of DevOps report actually shows that the lower performing teams improved their speed relative to the high performing teams, but by focusing on speed, their quality measures decreased.
I’ve seen this in the wild. A team will neglect doing technical design, or working to understand the intricacies of the users’ needs, or writing unit tests. They will stop “wasting time” doing code reviews, or writing comments in code, or making the code more modular through iterative refactorings. They will focus all of their attention on getting code out the door. And in doing so, they will make it harder and harder and harder to change anything in the future. The code will be confusing for the next engineers who need to maintain it. The functionality will be so poorly understood that no one will be able to write tests for it after the fact.
Eventually, the entire organization will slow down. Because it is so difficult to get any new feature built, the product team will think they must design every feature upfront — they get only one shot. The engineers will build that feature and move on to the next big feature without spending time iterating and maintaining the prior one. The execs will think that hiring more engineers will increase speed (and we all know that once “hire more people” is the answer to every problem, you are up a creek), which in turn distracts everyone from building product. And since the engineers think they too only get one shot before moving on, they will overengineer the solution with the hope that it can just live forever as is.
This is speed that kills quality; and the low quality then kills the speed. And everything costs more. It is a vicious cycle.
Conclusion
While it seems counterintuitive, personal experience and years of research agree: cost reduction comes from speed; speed comes from confidence; confidence comes from quality. Rinse, repeat, profit.
References
The Code Quality Versus Speed Fallacy
State of DevOps 2016 Report
Definition of the Engineering Method
Special thanks to Jeff Barrett and Brad Henrickson for review and feedback.
Writer of software. Otherwise unsummarizable.
