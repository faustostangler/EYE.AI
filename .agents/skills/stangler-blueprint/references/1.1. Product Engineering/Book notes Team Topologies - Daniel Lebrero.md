---
name: Book notes: Team Topologies - Daniel Lebrero
keywords: (placeholder)
metadata:
  url: https://danlebrero.com/2021/01/20/team-topologies-summary/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Book notes: Team Topologies
Menu
Home.
Archives.
@DanLebrero.
software, simply
Book notes: Team Topologies
Wed, 20 Jan 2021
Book notes on Matthew Skelton and Manuel Pais "Team Topologies" 
These are my notes on Matthew Skelton and Manuel Pais's Team Topologies.
The shortest summary: this book is like learning about Conway's law for the first time, but on steroids. Really enjoyed it.
You might also be interested in Remote Team Interactions Workbook: Using Team Topologies Patterns for Remote Working by the same authors.
Key Insights
Teams are always work in progress.
An org chart is always out of sync with reality.
Empowering is the way of moving from group of people to a team.
There are 3 org structures within each org: formal, informal and value creation
Key to success in knowledge work is in the interactions between the informal and value creation.
Team Topologies == 4 fundamental team types + 3 core interactions + Conway's law + Team Cognitive Load + Sensing Organisation + evolution If the architecture of the system and the architecture of the org are at odds, the architecture of the org wins. Ruth Malan
Implication of Conway's law:
Technical leaders must have a say on the organisation design.
Not all collaboration/communication is good.
Who is on the team matters less than the team dynamics.
Stable teams, not static.
Forming a team takes from 2 weeks to 3 months.
Each part owned exactly by one team.
Put the needs of your team above your own.
Minimise intrinsic cognitive load, eliminate extraneous cognitive load to leave room to germane cognitive load.
DevOps Topologies
Emphasize flow of change from concept to working SW.
Types of dependencies: knowledge, task, resource.
Four types of teams:
Stream-aligned: deliver values with minimal hands-offs.
Enabling: Grow capabilities of stream-aligned teams.
Complicated-subsystem: reduce cognitive load of stream-aligned teams.
Platform: make stream-aligned teams autonomous.
The purpose of the other types is to reduce the burden of stream-aligned teams.
Ratio stream-aligned vs others: 6:1 to 9:1.
Cross-functional teams build simpler solutions because solutions that require deep expertise in one area are likely to lose against easier-to-comprehend solutions that work for all team members.
Test for breaking a monolith: Does the resulting architecture support more autonomous teams with reduced cognitive load?
Intermittent collaboration gives better results than constant interaction.
Existing SW architecture will initially “push back” against the new team structures.
The most important thing is not the shape of the org, but the decision rules used to adapt and change it.
Collaboration is expensive, so it must be planned and justified.
Operations is not the output of design, but an input.
Team owning a product needs to have some responsibility for its commercial viability.
TOC
Preface
Part I: Teams As the Means of Delivery
Chapter 1 - The Problem with Org Charts
Chapter 2 - Conway's Law and Why It Matters
Chapter 3 - Team-First Thinking
Part II: Team Topologies that Work for Flow
Chapter 4 - Static Team Topologies
Chapter 5 - The Four Fundamental Team Topologies
Chapter 6 - Choose Team-First Boundaries
Part III: Evolving Team Interactions for Innovation and Rapid Delivery
Chapter 7 - Team Interaction Modes
Chapter 8 - Evolve Team Structures with Organizational Sensing
Chapter 9 - Conclusion
Preface
Teams are always work in progress.
Ideally teams should be:
Long-lived.
Autonomous.
Not isolated.
With engaged team members.
Part I: Teams As the Means of Delivery
Chapter 1 - The Problem with Org Charts
Team Topologies focuses on how to set up dynamic team structures and interaction modes that can help teams adapt quickly to new conditions, and achieve fast and safe software delivery.
An org chart is always out of sync with reality.
3 organizational structures in each org ( Niels Pflaeging):
Formal:
The org chart.
Facilitates compliance.
Informal:
“Real of influence” between individuals. 3. Value creation:
How work actually gets done based on inter-personal and inter-team reputation.
Pflaeging: Key to success in knowledge work is in the interactions between the informal and value creation structures.
2 key concepts:
Empowered teams as fundamental building block:
Empowering is the way of moving from group of people to a team. 2. Interaction modes: build trust between teams.
Naomi Stanford five rules for designing org:
Design when there is a compelling reason.
Develop options for deciding on design.
Chose the right time for design.
Look for clues that things are out of alignment.
Stay alert to the future.
Team Topologies == 4 fundamental team types + 3 core interactions + Conway's law + Team Cognitive Load + Sensing Organisation + evolution.
Teams are indivisible elements of SW delivery.
Dan Pink's three elements of intrinsic motivation:
Autonomy.
Mastery.
Purpose.
Teams have finite cognitive capacity:
If exceeded, team struggles to achieve mastery.
Delays, quality issues, decrease in motivation.
Conway's law.
SW consultancy:
No autonomy: constant juggling of requests from customers.
No mastery: “jack of all trades, master of none”.
No purpose: too many domains of responsibility.
Obstacles to flow:
Disengaged teams.
Pushing against Conway's law.
SW too big for team.
Confusing org design.
Team pulled in many directions.
Painful re-org every few years.
Flow is blocked.
Too many surprised.
Chapter 2 - Conway's Law and Why It Matters
Communication paths within an org effectively restrict the kinds of solutions that the organization can devise.
If the architecture of the system and the architecture of the org are at odds, the architecture of the org wins. Ruth Malan
We should be designing flows on top of an underlying platform.
Implication of Conway's law:
Technical leaders must have a say on the organisation design.
Not all collaboration/communication is good.
Communication tools have a strong influence on communication patterns.
Team assignments are the first draft of the architecture Michael Nygard
Chapter 3 - Team-First Thinking
Disbanding high-performing teams is worse than vandalism: it is corporate psychopathy. Allan Kelly
Driskell and Salas:
Teams working as a cohesive unit perform far better than a collection of individuals for knowledge-rich, problem-solving tasks that require high amounts of information.
Google found that: Who is in the team matters less than the team dynamics.
When measuring performance, teams matter more than individuals.
Team = stable group of 5-9 who work towards a shared goals as a unit.
Dunbar numbers.
Scaling by Dunbar.
Forming a team takes from 2 weeks to 3 months.
Stable teams, not static.
In high trust orgs, it is ok to change teams once a year.
In a typical org, 2 years.
Every part of the SW system needs to be owned by exactly one team.
Team members need a team first mindset:
Put the needs of the team above your own.
Embrace diversity.
Reward the whole team, not individuals.
Assign training budgets to the whole team and let them decide.
Cognitive load is the total amount of mental effort being used in the working memory ( John Sweller).
3 Types of cognitive load:
Intrinsic:
Fundamentals of the problem space.
Example: programming language.
Extraneous:
Environment related.
Example: how to deploy.
Germane:
Special attention is required.
Value adding.
Example: business domain.
Minimize intrinsic, eliminate extraneous to leave room for germane.
To measure cognitive load, ask the team: Do you feel like you are effective and able to respond in a timely fashion to the work you are asked to do?
Heuristics:
3 types of domain:
Simple.
Complicated.
Complex.
Each domain to one team
If domain is too big, split into subdomains. 2. One team, either:
2-3 simple domains.
1 complex domain.
Avoid 2 complicated domains, better split the team.
Define a Team API:
Code: endpoints, libraries, clients, …
Versioning.
Documentation.
Practices and principles.
Communication tools.
Work information: what is working on now, next and future.
Consider the TEam API for usability point of other teams.
Provide team, space, and money for guilds and communities of practice.
Design Physical and Virtual environment for:
Focused individual work.
Collaborative intra-team.
Collaborative inter-team.
Part II: Team Topologies that Work for Flow
Chapter 4 - Static Team Topologies
Instead of structuring teams according to know-how or activities, organize teams according to business domain areas. ( Jutta Eckstein)
Most common team anti-patterns:
Adhoc team design.
Shuffling team members.
Emphasize the flow of change from concept to working software.
DevOps Topologies.
Success of topology depends both on team members and surrounding environment, teams and interactions.
Examples:
Feature teams require high engineering maturity and trust.
Product teams require a support system.
Cloud teams provide self-service tools.
SRE makes sense at scale.
Good team topology depends on org size/SW scale and engineering maturity: 
Split responsibilities to breakdown silos.
Types of dependencies ( Diana Strode and Sid Huff):
Knowledge.
Task.
Resource.
Track dependencies and establish thresholds for alerts.
Chapter 5 - The Four Fundamental Team Topologies
Four types of teams:
Stream-aligned (SA):
Requires clarity of purpose and responsibility.
Single value stream.
Ideal: deliver values with 0 hands-offs.
Primary type: the purpose of the other types is to reduce the burden of SA teams.
Expected behaviours:
Steady flow of features.
Team measured by this.
Course correct based on feedback.
Proactive reaches supporting teams.
Enabling:
Goal: grow capabilities of SA teams.
Research, suggest tooling and practices to SA teams.
Expected behaviours:
Proactively seek to understand the needs of SA teams.
Stay ahead of the curve.
Management of technology lifecycle.
Knowledge sharing across SA teams.
Complicated-subsystem:
Goal: reduce cognitive load of SA teams.
Most team members require specialist knowledge on the subsystem their work on that is very hard to acquired.
Main difference with typical component teams.
Expected behaviours:
Delivery and quality higher than if SA team was developing the subsystem.
Prioritizes work according to all SA teams.
Platform:
Goal: make stream-aligned teams autonomous.
Digital platform: Self-service APIs, tools, services, knowledge and support.
Use internal pricing to regulate demand.
Thinnest Viable Platform.
Expected behaviours:
Platform as a product for SA teams.
Uses its own platform.
Builds on top of other platform teams.
Traditional work allocation:
Large request by a single customer is translated into a project, then several teams are involved and be required to fit the new work into their existing backlog.
Capabilities within a SA team (non-exhaustive):
App security.
Commercial and operational visibility.
Design and architecture.
Development and coding.
Infrastructure and operability.
Metrics and monitoring.
Product management and ownership.
Testing and QA.
UX.
Value stream examples:
Single product.
Single set of features.
Single user journey.
Single user persona.
Geography.
Compliance stream.
Business area.
Ratio stream-aligned vs others: 6:1 to 9:1.
Nested or “fractal” teams: In a big enough Platform, the Platform itself will contain several of the fundamental types of teams, incluing a platform team.
Cross-functional teams build simpler solutions because solutions that require deep expertise in one area are likely to lose against easier-to-comprehend solutions that work for all members.
Mapping existing teams to the fundamental types will clarify purpose and expected behaviours.
Examples in page 104.
Chapter 6 - Choose Team-First Boundaries
Align most teams with the streams of change in the org.
When considering a new architecture, take into account how it affects the teams:
Cognitive load.
Their location.
Their interest in the new service.
Types of monoliths:
Application monoliths.
Shared DB monolith.
Monolithic builds.
Couple releases.
Monolithic model - Shared domain.
Monolithic thinking - Standardization.
Monolithic workplace - Open-plan office.
Fracture plan is a natural seam in the SW system that allows the system to be split easily into two or more parts. Examples:
Business Domain Bounded Context.
Preferred fracture plane.
Expect iteration as you understand the context better.
Regulatory compliance.
Change cadence.
Team location:
Different time zone.
Either:
Full collocation.
Remote first.
Split team.
Risk
Depending on appetite for failure.
Performance isolation.
Technology.
Particularly old or less automatable tech.
User personas.
Org specific.
Test for breaking a monolith: Does the resulting architecture support more autonomous teams with reduced cognitive load?
Part III: Evolving Team Interactions for Innovation and Rapid Delivery
Chapter 7 - Team Interaction Modes
Team interactions as the sensing mechanism for innovation and self-steering.
Intermittent collaboration gives better results/solutions than constant interaction (Bernstein)
3 essential Team Interaction modes:
Collaboration:
Work closely between teams with different skill sets.
Insights should be shared with other teams.
When a high degree of adaptability or discovery is needed.
Example: early phases of new system.
Joint responsibility.
Need of ongoing collaboration suggest incorrect:
Domain boundaries, or
Team responsibilities, or
Mix of skills within a team.
Expect reduced output:
Higher cognitive load.
Extra coordination.
Can collaborate with at most one team.
X-as-a-Service:
Natural interaction model after collaboration.
Clearer ownership, smaller cognitive load.
Slower innovation across boundaries.
Must provide good Developer Experience.
Manage it as a product.
Facilitation:
Helping to clear impediments.
Main operating model of enabling teams.
Facilitators also help to discover gaps or inconsistencies in existing components and services used by other teams.
Focus on quality of interaction between other teams.
Interaction modes should become team habits:
Increase clarity of purpose.
Improve team engagement.
Reduce frustration with other teams.
Typical interaction modes:
Existing SW architecture will initially push back against the new team structures.
A small group of architects can be hugely effective when the remit of architecture is to discover, adjust, and reshape the interactions between teams, and therefore, the architecture of the system.
Collaborate on ambiguous interfaces until they are stable and functional.
Consider deliberate temporal re-teaming to revitalize interaction between teams, refresh and grow experience and build empathy.
Chapter 8 - Evolve Team Structures with Organizational Sensing
The most important thing is not the shape of the org, but the decision rules used to adapt and change it.
Collaboration is expensive, so it must be planned and justified.
Collaboration for:
Rapid learning.
Adoption of new practices.
Evolve different team topologies for different parts of the org at different times to match the team purpose and context.
Triggers for evolutions of Team Topologies:
SW has grown too large for one team.
Work queued in a team.
Specialization in components with in the team.
Complains about lack of documentation.
Delivery cadence is becoming slower.
Multiple Business services rely on a large set of underlying services.
Operations is not the output of design, but an input. Jeff Sussna
Team owning a product needs to have some responsibility for its commercial viability.
IT-ops service desk should be staffed with some of the most experienced engineers in the org.
Chapter 9 - Conclusion
Team Topologies is not enough:
Healthy org culture.
Good engineering practices.
Healthy funding and financial practices:
Avoid CapEx/OpEx split in IT.
Project driven deadlines.
Large-batch budgeting.
Clarity of business vision.
How to get started:
Start with the team:
Answer: what does the need in order to:
Act and operate as an effective team?
Own part of the SW effectively?
Focus on user needs?
Reduce unnecessary cognitive load?
Consume and provide SW and information to other teams?
Identify suitable streams of change.
Identify the Thinnest Viable Platform.
Identify capability gaps in team coaching, mentoring, service management and documentation.
Share and practice different interaction modes and explain principles behind new ways of working.
Did you enjoy it?
or share!
share
tweet
share
share
mail
Tagged in : book notes
We were unable to load Disqus Recommendations. If you are a moderator please see our troubleshooting guide.
Also on danlebrero.com
❮ 
Book notes: Deming's Journey to …
2 years ago
1 comment
Book notes on "Deming's Journey to Profound Knowledge" by John Willis 
Book notes: Building …
3 years ago
2 comments
Book notes on "Building Microservices: Designing Fine-Grained Systems" by Sam Newman 
Book notes: Unbundling the Enterprise
2 years ago
2 comments
Book notes on "Unbundling the Enterprise: APIs, Optionality, & the Science of Happy Accidents" by Stephen Fishman and Matt McLarty 
My personal path to Senior developer ... …
4 years ago
2 comments
Yet another "how to become a senior developer" blog post 
Book notes: Never split the difference
3 years ago
2 comments
Book notes on "Never Split the Difference" by Chris Voss and Tahl Raz 
Book notes: Flow Engineering
2 years ago
5 comments
Book notes on "Flow Engineering: From Value Stream Mapping to Effective Action" by Steve Pereira and Andrew Davis 
Schrödinger's functions: not the pure …
4 years ago
1 comment
What make a pure function pure? What make a stable system stable? 
Client-side good practices when …
3 years ago
5 comments
Good practices, pains and other considerations from a client's perspective when building third party integrations
❯
We were unable to load Disqus. If you are a moderator please see our troubleshooting guide.
What do you think?
9 Responses 
Upvote 
Funny 
Love 
Surprised 
Angry 
Sad
0 comments
1
Login
Disqus
Facebook
X (Twitter)
Google
Microsoft
Apple
G
Start the discussion…
Comment
Log in with
or sign up with Disqus or pick a name
Disqus is a discussion network
Don't be a jerk or do anything illegal. Everything is easier that way.
Read full terms and conditions
This comment platform is hosted by Disqus, Inc. I authorize Disqus and its affiliates to:
Use, sell, and share my information to enable me to use its comment services and for marketing purposes, including cross-context behavioral advertising, as described in our Terms of Service and Privacy Policy, including supplementing that information with other data about me, such as my browsing and location data.
Contact me or enable others to contact me by email with offers for goods or services
Process any sensitive personal information that I submit in a comment. See our Privacy Policy for more information [-]
Acknowledge I am 18 or older [-]
I'd rather post as a guest
4
Discussion Favorited!
Favoriting means this is a discussion worth sharing. It gets shared to your followers' Disqus feeds, and gives the creator kudos! Find More Discussions Share
Tweet this discussion
Share this discussion on Facebook
Share this discussion via email
Copy link to discussion
Best
Newest
Oldest
Be the first to comment.
Load more comments
Subscribe Subscribed
Privacy
Do Not Sell My Data
Powered by Disqus   Go
About me
Daniel Lebrero is a baby CTO, a teen remote worker, a mature Clojurian, an elder Architect, an ancient TDDer and an antediluvian Java dev.
With more than 20 years of software development experience, he has worked on monolithic websites, embedded applications, low latency systems, micro services, streaming applications and big data.
Right now, SVP of Engineering at LifeCheq. Maybe we are hiring.
Need help? Reach me at  , drop me an  or connect with .
Archives
RSS feed: 
Subscribe by email:
Subscribe
Categories
Architecture (42)
CTO diary (9)
Career (11)
Clojure (37)
Humour (12)
Java (7)
Kafka (8)
Kubernetes (5)
Talks (12)
book notes (54)
good practices (27)
resilience (7)
testing (10)
© Copyright 2016 Daniel Lebrero. Design by Styleshout.
Top
