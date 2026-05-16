---
name: What is Team Topologies? How to Structure Engineering Teams - DEV Community
keywords: (placeholder)
metadata:
  url: https://dev.to/bmf_san/what-is-team-topologies-how-to-structure-engineering-teams-5854
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
What is Team Topologies? How to Structure Engineering Teams - DEV Community
Skip to content
Powered by Algolia
Log in Create account
DEV Community
0 Add reaction 
0 Like  0 Unicorn  0 Exploding Head  0 Raised Hands  0 Fire
0 Jump to Comments 0 Save Boost
Copy link
Copied to Clipboard
Share to X Share to LinkedIn Share to Facebook Share to Mastodon
Report Abuse
Kenta Takeuchi
Posted on Mar 15
• Originally published at bmf-tech.com
What is Team Topologies? How to Structure Engineering Teams
# teamtopologies # teammanagement # organizationaldesign
This article was originally published on bmf-tech.com.
What is Team Topologies?
Team Topologies is an "adaptive organizational design model to maximize the flow of business value."
It fundamentally differs from traditional organizational design (hierarchical organizational charts) by prioritizing the following:
Emphasizing dynamic "flow" over static "hierarchy"
Considering "cognitive load" as a design constraint
Thinking of software architecture and organizational structure as a set
The goal is to create a state where each team can operate autonomously by organizing inter-team dependencies and reducing unnecessary communication (coordination costs).
Why Team Topologies?
Why do traditional function-based organizations (frontend, backend, infrastructure, etc.) not work well? Two powerful laws are at play here.
Conway's Law and the "Reverse Conway Maneuver"
The law proposed by Melvin Conway in 1968 is still valid today.
"Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations."
In other words, if an organization is siloed, the system will also be fragmented, making integration difficult. Conversely, if you want to create loosely coupled microservices, you must first divide the organization into loosely coupled independent teams. This is called the "Reverse Conway Maneuver."
Cognitive Load Theory: The Limits of Teams
Another important concept is "cognitive load." There is a limit to the complexity that the human brain (working memory) can handle at one time. Team Topologies classifies this load into three types and aims to reduce "extraneous load."
Intrinsic Load: Essential load for work, such as how to write Java or business logic.
Extraneous Load: Non-value-adding load, such as overly complex deployment procedures, difficult-to-use test environments, and unclear internal procedures.
Germane Load: Load for seeking better solutions. More resources should be allocated here.
Cognitive Load and "Lack of Ownership"
What happens when cognitive load exceeds a team's capacity?
The team can no longer fully understand the entire system. Then, anxiety like "I don't want to touch the working parts" or "What if it breaks when deployed?" begins to dominate. As a result, there is a "lack of ownership (sense of ownership and responsibility)" towards the system.
The attitude of "I don't know anything outside my responsibility" spreads, incident response is passed around, and delivery speed dramatically decreases.
The aim of Team Topologies is to restore healthy ownership by setting appropriate team sizes and responsibility scopes.
Four Team Types
To avoid chaotic team formation and manage cognitive load appropriately, Team Topologies recommends classifying the organization into the following four types only.
Stream-aligned Team
Role: Teams aligned with the main value stream of the business.
Characteristics: They have end-to-end responsibility (ownership) for the entire flow, from planning, development, testing, to operations. They minimize "waiting for requests" from other teams and are the main actors in delivering value autonomously. In a healthy organization, 80-90% of all teams are of this type.
Platform Team
Role: Teams that provide infrastructure and tools as "self-service" so that stream-aligned teams can operate autonomously.
Characteristics: They view internal developers as "customers" and provide an easy-to-use, low-cognitive-load platform (Thinnest Viable Platform). They are not mere "infrastructure operators" but teams that create "products" to increase the productivity of product teams.
Enabling Team
Role: Specialist teams to fill gaps in specific technical areas (security, test automation, AI, etc.).
Characteristics: Instead of doing the work for them, they temporarily join stream-aligned teams to provide technical guidance and coaching, thereby improving the team's capabilities. They are teams that "teach how to fish rather than give fish."
Complicated Subsystem Team
Role: Teams that handle only parts that are too specialized for normal teams to handle due to high cognitive load, such as advanced mathematical models or image processing engines.
Characteristics: They are set up as an exceptional measure to reduce cognitive load. They should not be increased easily.
Three Interaction Modes
Not only the "shape" of the team but also the "way of interaction" needs to be intentionally designed.
The important thing is that these modes are not fixed but should be used differently depending on the time. Dynamic changes, such as starting with "Collaboration" to build together and then transitioning to "X-as-a-Service" once stable, are required.
Conclusion
Team Topologies is not a "new organizational chart" that ends once implemented.
As the product phase changes, the necessary team shape and optimal interaction also change. Regularly questioning "Are the current team boundaries appropriate?" and "Is cognitive load becoming too high?" and continuously refactoring the organization (organizational sensing) is the key to maintaining a fast flow.
Starting by discussing with your team which type they fit into and whether "cognitive load" is undermining ownership might lead to valuable discoveries.
References
teamtopologies.com
チームトポロジー 価値あるソフトウェアをすばやく届ける適応型組織設計
 The DEV Team
Promoted
What's a billboard?
Manage preferences
Report billboard
Build the Future of Data Privacy on Midnight
This is your opportunity to build on a fully launched network designed to solve the internet's biggest privacy challenges. You'll get hands-on experience with cutting-edge data protection tech to create applications that give users true control over their digital lives.
Start building →
Read More
Top comments (0)
Subscribe 
Personal Trusted User
Create template
Templates let you quickly answer FAQs or store snippets for re-use.
Submit Preview Dismiss
Code of Conduct
• Report abuse
Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's permalink. [-] 1
Hide child comments as well
Confirm
For further actions, you may consider blocking this person and/or reporting abuse
 AWS
Promoted
What's a billboard?
Manage preferences
Report billboard
Building industry breakthroughs together
Discover how the cloud helps businesses adapt, innovate, and grow in real time. Tune in live.
Register Now
Kenta Takeuchi
Follow
Software engineer.
Location Kanagawa, Japan
Work Software engineer
Joined Dec 17, 2020
Trending on DEV Community
 5 types of engineers I met as a Technical Writer # watercooler # technicalwriting # discuss # jokes
 AI vs Non-AI: Building the Same Project Twice # ai # softwareengineering # discuss # programming
 What is your WPM (Words per Minute)? #2 # discuss # watercooler # challenge # community
 AWS
Promoted
What's a billboard?
Manage preferences
Report billboard
Building industry breakthroughs together
Discover how the cloud helps businesses adapt, innovate, and grow in real time. Tune in live.
Register Now
👋 Kindness is contagious
What's a billboard?
Manage preferences
Report billboard
Explore this insightful piece, celebrated by the caring DEV Community. Programmers from all walks of life are invited to contribute and expand our shared wisdom.
A simple "thank you" can make someone's day—leave your kudos in the comments below!
On DEV, spreading knowledge paves the way and fortifies our camaraderie. Found this helpful? A brief note of appreciation to the author truly matters.
Let's Go!
💎 DEV Diamond Sponsors
Thank you to our Diamond Sponsors for supporting the DEV Community
Google AI is the official AI Model and Platform Partner of DEV
Neon is the official database partner of DEV
Algolia is the official search partner of DEV
DEV Community — A space to discuss and keep up software development and manage your software career
Home
DEV++
Reading List
Videos
DEV Education Tracks
DEV Challenges
DEV Help
Advertise on DEV
Organization Accounts
DEV Showcase
About
Contact
Free Postgres Database
DEV Shop
MLH
Code of Conduct
Privacy Policy
Terms of Use
Built on Forem — the open source software that powers DEV and other inclusive communities.
Made with love and Ruby on Rails. DEV Community © 2016 - 2026. 
We're a place where coders share, stay up-to-date and grow their careers.
Log in Create account     
