---
name: Team Topologies Book Summary – Part 1 of 3: Key Concepts | Mark ...
keywords: (placeholder)
metadata:
  url: https://markosrendell.wordpress.com/2020/02/04/team-topologies-book-summary-part-1-of-3-key-concepts/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Team Topologies Book Summary – Part 1 of 3: Key Concepts | Mark Rendell
Mark Rendell
Data Platforms, SRE, DevOps, Developer Experience, Continuous Delivery, PaaS, Cloud meet tenuous musical references
Menu
Skip to content
Home
About Mark Rendell
Team Topologies Book Summary – Part 1 of 3: Key Concepts
Posted on February 4, 2020 by markosrendell
Team Topologies is one of the latest books published by IT Revolution (the excellent company created by Gene Kim the co-author of The Phoenix Project and author of The Unicorn Project). Team Topologies was written by Matthew Skelton and Manuel Pais (the people behind the DevOps Topologies website) but it is far more than an 'extended dance remix' of that. The book takes a much wider view on team designs that make companies successful and considers the full socio-technical problem space.
This blog series is a set of highlights from the book followed by some suggestions of what to do with the information. I hope it will also inspire you to read the book and have some fresh thoughts about improving your organisation.
Conway's Law Demonstrates Team structures are incredibly important
Conway's Law is the famous observation that the structure of teams (or more specifically the structure of information flow between groups of people) impacts the design of a system. For example, if you take a 4-team organisation and ask them to build a compiler, you will most likely get a compiler that has 4 stages to it. This is important because of the implication that the structure of Teams doesn't just impact governance, efficiency, and agility, it also impacts the actual architecture of the products that get built. The architecture of products is vitally important because of the heavy bearing it has on the agility and reliability of not just systems, but the businesses driven by them.
Advertisement
So Conway's law teaches us two things:
Team designs are very important because good team designs lead to good software design and good software design leads to better more effective teams (or if you get it wrong the cycle goes the other way).
The factors that influence both a good architecture as well as good teams need to be considered when designing teams, team boundaries, and the planned communication required between teams.
General guidance for great teams
The book doesn't overlook covering general factors that influence high performing people and teams. For example:
Team sizing – Dunbar's number is highlighted for its recommendation about the limits of how many people can successfully collaborate in different ways:
The strongest form of communication happens in an individual team working closely together with a very consistent shared context and specific purpose. In software this number is supposed to be 8 people.
The limit of people who can all deeply trust each other is 15 and there is also significance of the dynamics of 50 and 150 people. So this can provide useful constraints when thinking about the design of teams of teams.
The importance of having long lived teams that are given enough time to get to a state of high performance and then stick together and capitalise on it. Research shows teams can take 3 months to get to a point where a team is many times more effective than the sum of the individual members. The better the overall company culture is, the easier changing teams can be, but even in the best cases the research recommends no less than a year. The book also highlights that the well-known Tuckman team performance model (Forming, Storming, Norming, Performing) has been proven to be less linear than it sounds. The storming stage has been found to restart every time there is a personnel or major change to the team.
Some aspects of office design are important.
Putting other team members first and generally investing in relationships and making the team an inclusive place to work is vital.
Defining effective team scope, boundaries, and approaches to communication. This is the broadly the topic of the rest of the book (and this blog).
Advertisement
Team Design Consideration: Minimising Team Handoffs, Queues, and Communication Overhead
The book talks about the importance of organising for flow of change to software products. In order to do that you need to consider team responsibilities and to minimise and optimise communication. The book presents a case study from Amazon as exponents of “you build it, you run it” approaches.
You also need what the book calls “sensing” which is where an organisation possesses enough feedback mechanisms to ensure software and service quality is understood as early and clearly as possible.
Whilst teams may communicate and prioritise effectively within the boundary of their team, external communication across team boundaries is always much more costly and much less effective. When teams have demands upon other teams, this can:
Advertisement
be disruptive and lead to context switching
lead to queues, delays, and prioritisation problems
create a large communication and management overhead.
I found the point about communication thought provoking because it's often a popular idea that the more collaboration within an organisation, the better. As the book states, in practice all communication is expensive and should be considered in terms of cost versus benefit. A friend of mine Tom Burgess pointed out a nice similarity to memory hierarchy in Computer Science. This also got me thinking about the parallels of people and the Fallacies of Distributed computing!
Team Design Consideration: Cognitive load
The book introduces a very helpful concept from psychology (created by John Sweller) called Cognitive Load. This describes how much 'thinking effort' a particular 'thing' needs in order to be done effectively. It observes that not all types of thinking effort are the same in nature:
Advertisement
Different tasks require different types of thinking
There are different causes of the need to think
There are different strategies for managing and reducing the effort required for the different types of thinking.
The types are:
Intrinsic Cognitive Load – this relates to the skill of how to do a task e.g. which buttons to press according to the specific information available and scenario.
Extraneous Cognitive Load – this relates to broader environmental knowledge, not related to the specific skill of the task, but still necessary, e.g. what are the surrounding process admin steps that must be done after this task
Germane Cognitive Load – this relates to thinking about how to make the work as effective as possible e.g. what should the design be, how will things integrate.
The strategies for managing each type of cognitive load are as follows:
Intrinsic Cognitive Load – can be reduced by training people or finding people experienced at a task. The greater their relevant skill levels, the lower the load required to do the task.
Extraneous Cognitive Load – can be reduced by automation or good process design and discoverability.
Germane Cognitive Load – is really the type of work you want people focusing on. However, the amount required is a factor of how much scope someone has to worry about.
Advertisement
This is all very interesting and applicable to individuals, but you might be wondering: how does this relate to organisational team design? The book presents a very useful idea here: cognitive load should be considered in terms of the total amount required by whole teams.
Putting this in plainer terms, when you are thinking about team design and organisational structure, you need to consider how much collectively you are expecting the team to:
know
be able to perform
be able to make effective decisions about
be able to make brilliant.
The reason I found this so powerful is because it gives you a logical way to reason with the current fairly fashionable idea that end-to-end / DevOps / BusDevSecOps(!) teams are the utopia (or worse: the meme that if there are separate teams in the value stream you are not doing DevOps and you are doing it wrong). Sure, giving as much ownership of a product or service as possible to one team avoids team boundaries, but it also increases the cognitive load on the team and potentially the minimum number of people needed in a team.
Advertisement
Decomposing and fracture planes
So a simplified summary so far:
Amazon have helped highlight the benefit of minimising handoffs, queues, and communication
Sweller has taught us to avoid giving a team too much Cognitive load
Dunbar has taught us to keep teams at around 8 people.
At this point we have to consider the amount of scope assigned to a team as our way to satisfy the above constraints. If we can keep it small enough, perhaps we can still give them end-to-end autonomy whilst keeping team sizes down and cognitive load manageable.
This is where the book starts talking about a concept of Fracture Plains. The name is a metaphor about how when stonemasons break rocks, they focus on the natural characteristics of the structure of the rock in order to break them up cleanly and efficiently. The theory is that software systems also naturally have characteristics that create more effective places to divide things up. The metaphor is especially poetic considering large tightly coupled software systems are often likened to monolithic rocks.
Advertisement
The book provides a useful discussion of different types of fracture plane to explore including:
Business domains (i.e. where the whole domain driven development and bounded contexts design techniques come into play)
Change cadence i.e. things that need to change at the same pace
Risk i.e. things with similar risk profiles
(Most important of all) separation of platform and application (more on that to come).
Ideally all of these can help decompose systems whilst minimising cognitive load and keeping team sizes small enough.
In Part 2 I'll share the reusable patterns the book proposes for doing this.
Advertisement
Share this:
Share on X (Opens in new window) X
Share on Facebook (Opens in new window) Facebook
Like Loading...
This entry was posted in agile, agile development, cloud, continuous deployment, continuousdelivery, continuousintegration, devops, enterpriseit, it, PaaS, Uncategorized and tagged Agile, Agile software development, Configuration management, Continuous delivery, DevOps, Release management. Bookmark the permalink.
Post navigation
← SRE Certification – Free Self Test
Team Topologies Book Summary – Part 2 of 3: Topologies and Interaction Modes →
5 thoughts on “ Team Topologies Book Summary – Part 1 of 3: Key Concepts”
 Brahm Srivastav says: February 7, 2020 at 16:26 Really great piece of work Mark… You continue to inspire hundreds like me! Reply
 markosrendell says: February 7, 2020 at 17:47 Thanks Brahm, but there is only one like you. Total legend! Lovely to hear from you 🙂 Reply
 Peter Friedwagner says: February 9, 2020 at 19:49 Hi Mark – Thanks for the great summary. Reply
Pingback: The Importance of Developer Experience in the PaaS Age | Mark Rendell
Pingback: Finding your path with Site Reliability Engineering (SRE) | Mark Rendell
Leave a comment Cancel reply
Write a comment...
Log in or provide your name and email to leave a comment. [-]
Email me new posts [x] instantly
Instantly [-] daily Daily [-] weekly Weekly [-]
Email me new comments [-]
Save my name, email, and website in this browser for the next time I comment.
Comment
Δ
Search Search
Recent Posts
Day 2 of the 'AI for the rest of us' Conference
Finding your path with Site Reliability Engineering (SRE)
Defining an enterprise PaaS strategy – Part 3 of 3: Re-use versus Coupling
Defining an enterprise PaaS strategy – Part 2 of 3: As a Service
Defining an enterprise PaaS strategy – Part 1 of 3: Introduction
Top Posts & Pages
AWS Certified Solutions Architect - Sample Questions Answered and Discussed
The Importance of Developer Experience in the PaaS Age
Archives
October 2024
July 2021
July 2020
May 2020
February 2020
November 2019
October 2019
August 2019
June 2019
May 2017
April 2017
February 2017
November 2016
July 2016
May 2016
April 2016
March 2016
February 2016
November 2015
October 2015
September 2015
August 2015
November 2014
October 2014
September 2014
August 2014
July 2014
June 2014
May 2014
March 2014
February 2014
December 2013
November 2013
October 2013
September 2013
Create a website or blog at WordPress.com
Comment
Reblog
Subscribe Subscribed
Mark Rendell Join 66 other subscribers Sign me up
Already have a WordPress.com account? Log in now.
Mark Rendell
Subscribe Subscribed
Sign up
Log in
Copy shortlink
Report this content
View post in Reader
Manage subscriptions
Collapse this bar Close and accept
Privacy & Cookies: This site uses cookies. By continuing to use this website, you agree to their use.
To find out more, including how to control cookies, see here: Cookie Policy
%d 
Design a site like this with WordPress.com
Get started 
Advertisement 
