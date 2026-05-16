---
name: Talk Notes: "Simple Made Easy" by Rich Hickey (2011) - DEV Community
keywords: (placeholder)
metadata:
  url: https://dev.to/sylwiavargas/talk-notes-simple-made-easy-by-rich-hickey-2011-39oo
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Talk Notes: "Simple Made Easy" by Rich Hickey (2011) - DEV Community
Skip to content
Powered by Algolia
Log in Create account
DEV Community
10 Add reaction 
8 Like  1 Unicorn  0 Exploding Head  1 Raised Hands  0 Fire
0 Jump to Comments 2 Save Boost
Copy link
Copied to Clipboard
Share to X Share to LinkedIn Share to Facebook Share to Mastodon
Report Abuse
Sylwia Vargas
Posted on Mar 28, 2023 
8  1   1 
Talk Notes: "Simple Made Easy" by Rich Hickey (2011)
# techtalks
Talk Notes (16 Part Series)
1 Talk Notes: "DocOps: engineering great documentation" by Adam Butler 2 Talk Notes: "Fight, Flight, or Freeze - Releasing Organizational Trauma" by Matt Stratton ... 12 more parts... 3 Tech Notes: "Accessibility is a Requirement" (RailsConf 2021) 4 Talk Notes: "'Junior' Devs are the Solution to Many of Your Problems" (RailsConf 2021) 5 Talk Notes: "Self-Care on Rails" (RailsConf 2021) 6 Talk Notes: "Designing APIs: Less Data is More" (RailsFonc 2021) 7 Talk Notes: 'Talmudic Gems For Rails Developers' (RailsConf 2021) 8 Talk Notes: "Implicit to Explicit: Decoding Ruby's Magical Syntax" (RailsConf 2021) 9 Talk Notes: "Secrets of Successful Mentors" (RailsConf 2021) 10 Talk Notes: 'The Rising Storm of Ethics in Open Source' (RailsConf 2021) 11 Tech Talks: "A Day in the Life of a Ruby Object" (RailsConf 2021) 12 Talk Notes: "Growing Software From Seed" (railsConf 2021) 13 Tech Talk: 'Debugging: Techniques for Uncertain Times' (RailsConf 2021) 14 Talk Talk: 'One AWS team's move to docs as code: what worked, what didn't, what's next' (Write the Docs 2022) 15 Tech Talk: 'Unit Test the Docs: Why You Should Test Your Code Examples' (Write the Docs 2022) 16 Talk Notes: "Simple Made Easy" by Rich Hickey (2011)
✨ What is this post about: As a part of my professional growth, I make time to watch tech talks. Previously, I'd just watch them but now I take and publish notes for future reference.
✨ Talk: "Simple Made Easy" by Rich Hickey
✨ One-paragraph summary: Rich Hickey, the author of Clojure and designer of Datomic, is a software developer with over 30 years of experience in various domains. Rich has worked on scheduling systems, broadcast automation, audio analysis and fingerprinting, database design, yield management, exit poll systems, and machine listening, in a variety of languages. This keynote was given at Strange Loop 2011, and is perhaps the best known and most highly regarded of Rich's many excellent talks, ushering in a new way to think about the problems of software design and the constant fight against complexity.
✨ Impression: I loved this talk. Plenty of food for thought, both with regards to my engineering work and Developer Relations. Even though the talk was delivered over a decade ago, most points are still very much relevant - and many discussions are still ongoing. That is a testament to how well-planned this talk was, but also to that some themes in the tech community discourse are universal.
Introduction
"We need to build simple systems if we want to build good systems."
Word origins
simple - roots are 'sim' and 'plex', which means 'one fold' or 'one braid'
complex - at roots, it means 'braided together'
easy - at roots, it means 'lie near' (adjacent)
hard - at roots, means 'strong'
"Simple"
Simple things are like one fold: they have one role, one task, one objective, one concept; it is focused
There might be many instances of the same simple thing - and it remains simple as long as these instances are not mingled
The simplicity can be objectively stated
my side note: simple is a language of fairy tales
"Easy"
Easy things are near, at hand, easy to obtain, they are at reach; in software, that would be an easy reach like on our hard drive, tool set, IDE
Easy things are near to our understanding, our skillset, they are familiar
my side note: easy is Swedish because to me it looks like English and German
Easy things are near our capabilities
Easy is relative, it depends on the context an individual has
Construct vs Artifact
Construct: "We program with constructs. We have programming languages. We use particular libraries, and those things, in and of themselves, when we look at them, like when we look at the code we write, have certain characteristics in and of themselves."
Artifacts: "But we're in a business of artifacts. We don't ship source code, and the user doesn't look at our source code and say, "Ah, that's so pleasant." They run our software, and they run it for a long period of time. (...) All of that stuff, the running of it, the performance of it, the ability to change it all is an attribute of the artifact, not the original construct."
We focus too much on the construct (the programming languages)
Even though the users are infatuated with the artifact (say, the UI), the developers focus on the construct (the library)
Our employers are infatuated with the "easiness" of the contruct, too - it's "easy" to replace a programmer and this programmer will know how to move around the codebase and use the tools because they are "easy" - near their context and familiar (though it's not necessarily easy in the sense of whether the person has the capabilities to actually code in this codebase)
We should focus on the long-term results of the use of the artifact
Does the software do what it's supposed to do?
Is it of high quality?
Can we rely on it doing what it's supposed to do?
Can we fix problems when they arise?
And if we're given a new requirement, can we change it?
Conclusion: We must assess constructs by their artifacts
my side note: this is a really interesting framing; to me, it's really helpful because I have been thinking a lot about how much talk there is about some libraries (say, React) and so little talk about how inaccessible the resulting UI is
Working with limitations
Only the things we can understand we can make reliable
The more extensible, flexible, and dynamic stuff is, the more tradeoff there is in our ability to understand it
We can only consider a few things at a time; this is a limited number
my side note: some research suggests that we can't focus on more than one thing at a time and other that we can keep track of limited number of things, like 2-4, at the same time
"If things are intertwined together, we lose the the ability to take them in isolation."
Every intertwining is adding more burden - and the intertwining (braiding things together) is going to limit our ability to understand systems
Conclusion: complexity undermines understanding
Changing things
"What is the impact of this potential change?": if you're going to change software, you're going to need to analyze what it does and make decisions about what it ought to do
"And what parts of the software do I need to go to to effect the change?": if you can't reason about your program, you can't make these decisions without fear
Once we have software, we do two things: add capabilities, and debug what doesn't work
Good joke about debugging at 15:43 mark
Tests are useless if we can't understand our program; they may eventually fail us
Another good joke, this time about agile, at 17:27, and I'm going to quote it here: > What kind of runner can run as fast as they possibly can from the very start of a race? Sprinter, only somebody who runs really short races, okay? But of course, we are programmers, and we are smarter than runners, apparently, because we know how to fix that problem, right? We just fire the starting pistol every hundred yards and call it a new sprint.
If you ignore the complexity, you will slow down over the long haul
if you focus on ease, you will be able to go as fast as possible from the beginning of the race but the complexity will eventually get you, and you will accomplish less with every next sprint, and you will end up redoing things you've already done, "and the net effect is you're not moving forward in any significant way."
Easy but complex
Some things that are easy are actually complex
they are succinctly described
they are familiar
they are available
easy to use
Users don't care about the underlying complexity, they care about what the program does
Is the outcome of your work drowning in complexity?
The benefits of simplicity:
ease of understanding
ease of change
ease of debugging
increased flexibility (change things around) - modularity
Is it easier to change a knitted castle or a LEGO castle?
Making Things Easy
Make it reachable - easy to install, easy to approve
Make it familiar - it's a learning exercise
Make it simple so it's easy to understand, we are limited in our ability to understand complexity
Good point about parens in Clojure: there are some things you can solve (get more familiar, start using the tool) and some that you cannot (the tool is complex)
Developers know the value of everything and the cost of nothing (rephrased from: "LISP programmers know the value of everything and the cost of nothing" from Alan Perlis) - we talk a lot about benefits but not the tradeoffs
Avoid complexity (don't complect/braid together)
Instead, compose (place together)
composing simple components is the key to robust systems
it's not only about modularization
State is never simple but it is easy (familiar, at hand)
You don't need all this complexity. You can make a sophisticated system with simple tools - you can focus on the system, what it's supposed to do, instead of the constructs.
If a decision needs to be made by a person who has better context, that system is not simple.
Main points of complexity
These can be replaced with the following simpler stuff:
Data is actually really simple. There are not a tremendous number of variations in the essential nature of data: there are maps, there are sets, there are linear, sequential things. There are not a lot of other conceptual categories of data. We create hundreds of thousands of variations that have nothing to do with the essence of this stuff and make it hard to write programs that manipulate the essence of the stuff. We should just manipulate the essence of the stuff. It's not hard. It's simpler.
Abstraction for simplicity
abstract (meaning drawn away from its physical nature)
"abstraction" sometimes is used in a sense of hiding complexity but that's not what it is about
If you want to take stuff apart, look at a concept and ask who, what, when, where, why, how
What
What is the operation? What is what we want to accomplish?
If you separate "what" from "how", you can make "how" someone else's problem
Who
Data or entities - these are the things that our abstractions are going to be connected to eventually depending on how your technology works.
Pursue many subcomponents so you work with small interfaces
How
How the work happens - the implementation logic
connect to abstractions and entities via polymorphism
prefer abstractions that don't dictate how (declarative are good)
When, where
don't complect with design (if A causes B, you're complectin - use queues instead)
Why
the policy and rules of the application
often strewn everywhere
Information is simple
Don't ruin it
Simplify the problem space or some code that somebody else wrote by disentangling:
identifying individual threads/roles/dimensions
following through the user story
Simplicity is a choice - it's your fault if you don't have a simple system
You need vigilance, sensibilities, and care
Easy is not simple. Simple is something that's not entangled.
Simplicity made easy
Choose simple constructs over complexity-generating constructs
It's the artifacts, not's the authoring
Create simple abstractions
Simplify the problem space before you start
Simplifying means making more things, not fewer
Talk Notes (16 Part Series)
1 Talk Notes: "DocOps: engineering great documentation" by Adam Butler 2 Talk Notes: "Fight, Flight, or Freeze - Releasing Organizational Trauma" by Matt Stratton ... 12 more parts... 3 Tech Notes: "Accessibility is a Requirement" (RailsConf 2021) 4 Talk Notes: "'Junior' Devs are the Solution to Many of Your Problems" (RailsConf 2021) 5 Talk Notes: "Self-Care on Rails" (RailsConf 2021) 6 Talk Notes: "Designing APIs: Less Data is More" (RailsFonc 2021) 7 Talk Notes: 'Talmudic Gems For Rails Developers' (RailsConf 2021) 8 Talk Notes: "Implicit to Explicit: Decoding Ruby's Magical Syntax" (RailsConf 2021) 9 Talk Notes: "Secrets of Successful Mentors" (RailsConf 2021) 10 Talk Notes: 'The Rising Storm of Ethics in Open Source' (RailsConf 2021) 11 Tech Talks: "A Day in the Life of a Ruby Object" (RailsConf 2021) 12 Talk Notes: "Growing Software From Seed" (railsConf 2021) 13 Tech Talk: 'Debugging: Techniques for Uncertain Times' (RailsConf 2021) 14 Talk Talk: 'One AWS team's move to docs as code: what worked, what didn't, what's next' (Write the Docs 2022) 15 Tech Talk: 'Unit Test the Docs: Why You Should Test Your Code Examples' (Write the Docs 2022) 16 Talk Notes: "Simple Made Easy" by Rich Hickey (2011)
 AWS
Promoted
What's a billboard?
Manage preferences
Report billboard
Power smarter decisions with the cloud
Join AWS experts and Partners to learn how cloud technology supports efficiency, agility, and growth. Watch live.
Register Now
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
 The DEV Team
Promoted
What's a billboard?
Manage preferences
Report billboard
How to prompt Gemini 3.1's new text to speech model
Gemini 3.1 Flash text to speech (TTS) is a new model that you can direct to get the precise audio performance you want. In this blog post I'll share some tips on how to guide the model with prompts, and share some examples of its strengths.
See more 🎥
Sylwia Vargas
Follow
I'm a tech writer and educator advocating for code newbies ✨ I'm also a Developer Relations Lead + front-end dev at @inngest
Location New York
Pronouns she/her
Joined Nov 30, 2019
More from Sylwia Vargas
Tech Talk: 'Debugging: Techniques for Uncertain Times' (RailsConf 2021) # techtalks
Talk Notes: "Growing Software From Seed" (railsConf 2021) # techtalks
Tech Talks: "A Day in the Life of a Ruby Object" (RailsConf 2021) # rails # techtalks
 AWS
Promoted
What's a billboard?
Manage preferences
Report billboard
Building industry breakthroughs together
Discover how the cloud helps businesses adapt, innovate, and grow in real time. Tune in live.
Register Now
DEV Education Tracks
What's a billboard?
Manage preferences
Report billboard
Announcing the First DEV Education Track: "Build Apps with Google AI Studio"
The moment is here! We recently announced DEV Education Tracks, our new initiative to bring you structured learning paths directly from industry experts.
Dive in and Learn
DEV is bringing Education Tracks to the community. Dismiss if you're not interested. ❤ 
💎 DEV Diamond Sponsors
Thank you to our Diamond Sponsors for supporting the DEV Community
Google AI is the official AI Model and Platform Partner of DEV
Neon is the official database partner of DEV
Algolia is the official search partner of DEV
DEV Community — A space to discuss and keep up software development and manage your software career
Home
About
Contact
MLH
Code of Conduct
Privacy Policy
Terms of Use
Built on Forem — the open source software that powers DEV and other inclusive communities.
Made with love and Ruby on Rails. DEV Community © 2016 - 2026. 
We're a place where coders share, stay up-to-date and grow their careers.
Log in Create account     
