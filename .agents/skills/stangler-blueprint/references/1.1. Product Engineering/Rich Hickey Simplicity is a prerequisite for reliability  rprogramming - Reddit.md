---
name: Rich Hickey: Simplicity is a prerequisite for reliability : r/programming - Reddit
keywords: (placeholder)
metadata:
  url: https://www.reddit.com/r/programming/comments/1pzfo4r/rich_hickey_simplicity_is_a_prerequisite_for/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Rich Hickey: Simplicity is a prerequisite for reliability : r/programming
Skip to main content Rich Hickey: Simplicity is a prerequisite for reliability : r/programming
Open menu
Open navigation 
Go to Reddit Home 
r/programming
Sign Up
Sign up for Reddit
Log In
Log in to Reddit
Expand user menu
Open settings menu
Skip to Navigation Skip to Right Sidebar
Back
Go to programming
r/programming
•
4mo ago
Digitalunicon
Locked post
Stickied post
Archived post
Report
Rich Hickey: Simplicity is a prerequisite for reliability
 
infoq.com Open
Rewatched this recently. Still one of the clearest explanations of why systems fail as complexity accumulates. would like to know how people here apply this in real projects.
Upvote 414 Downvote 100 Go to comments Share
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
awitod
•
4mo ago
The paradox is that simplicity is much harder to achieve because it requires a lot of design and architecture.
Complexity and chaos is the normal default state. Order takes time and effort.
I offer this as a caution - people often use expediency as an excuse to avoid the complicated work required to achieve simplicity
Upvote 231 Downvote Reply Award Share
Report
Award
Share 
Sharlinator
•
4mo ago
Only the best programmers can devise simple solutions to complex problems. Unfortunately many more programmers like to create complex solutions to simple problems.
Upvote 58 Downvote Reply Award Share
Report
Award
Share
More replies
19 more replies 
shared_ptr
•
4mo ago
This is so important it's one of our guiding principles in the engineering team at incident.
We have a few rules that help us keep to this:
Fewer tools done well: we try to use as few tools across our stack as possible and invest in them fully.
Keep developer environments close to production: as much as possible keeping the two aligned reduces surprises when you go to production
Clear purpose, strong boundaries: when a system grows larger you should identify logical separations and make them clear in code, sharing as little as you can between them.
Having guidelines like this has stopped us adding all sorts of infrastructure since the company began and allowed us to grow over the last five years without having to ditch a simple monolithic Go application with Postgres as the primary store and a developer environment people can setup in half a day.
Upvote 31 Downvote Reply Award Share
Report
Award
Share
TrustInNumbers
•
4mo ago
nah, lets just preemptively create 50 microservices because our architect told us that proper separation improves scalability
Upvote 15 Downvote Reply Award Share
Report
Award
Share
More replies
2 more replies
fj2010
•
4mo ago
Always find Rich's talks thought provoking
Upvote 37 Downvote Reply Award Share
Report
Award
Share
2 more replies
Saint_Nitouche
•
4mo ago
Defining simplicity in a system as components only doing one thing is a perfectly good way to think about it. But in my experience that means you then have to orchestrate those do-one-thing components to actually achieve the true goal you care about.
If you are lucky you can compose them into a linear pipeline where everything just feeds results forward. Even then though, there is often complexity hidden in the boundary between components. RPC, REST, carrier pigeon. The microservices problem.
The transcript makes it clear he is talking more about things on a code-level, I think, where that applies less. But still something I find myself running into.
I also had to laugh at this: "Information is simple. Keep it simple..."
Information is many things, but I would not call it simple.
Upvote 34 Downvote Reply Award Share
Report
Award
Share
Krackor
•
4mo ago
Adding behavior and state (i.e. mutable objects with methods) is one way to make information complex.
Upvote 15 Downvote Reply Award Share
Report
Award
Share
More replies 
awitod
•
4mo ago
Information is simple. Making it flow simply through a system is complicated.
In terms of components and services - when you find that a low level operation needs information from some other low level operation that your design has on the other side of some system boundary you feel this truth like a punch in the gut
Upvote 6 Downvote Reply Award Share
Report
Award
Share
fiah84
•
4mo ago
Information is many things, but I would not call it simple.
and I would argue that's one of the main points to start: simplify the input as much as possible. I've been so lucky in that with my projects I've been able to push back on some of the most complexity inducing requirements, and one of the main methods was to reduce the user input and the complexity of it to the bare minimum. The result was that they've been much more successful than previous projects where I didn't yet have the goodwill / perceived authority to push back like that. And although the users may have had to compromise slightly because of me being a jerk who wouldn't implement what they wished for, they're still very happy with the result
Upvote 5 Downvote Reply Award Share
Report
Award
Share 
[deleted]
•
4mo ago
Comment deleted by user
Upvote Downvote Reply Share
bring_back_the_v10s
•
4mo ago
But in my experience that means you then have to orchestrate those do-one-thing components to actually achieve the true goal you care about.
I'm not an electronics expert but aren't many things in electronics just like that? You have many small components that have a single responsibility, you orchestrate them to a goal. Then you have composition, eg. a microcontroller which is made of many small focused components.
Upvote 3 Downvote Reply Award Share
Report
Award
Share
More replies
VictoryMotel
•
4mo ago
The title says simplicity, you extrapolated it to doing only one thing per component. That's ideal but there are probably times when the straight forward and simple way isn't the same path. Big libraries like ffmpeg for example would do a lot of different things.
Upvote 3 Downvote Reply Award Share
Report
Award
Share
More replies
14 more replies
civildisobedient
•
4mo ago
A lot of the complexity that I have seen comes from minor, well-intentioned deviations that someone promised a Big Client in order to close a deal. Your only guideposts to the sprawling tangled web of conditionals and branching logic are (maybe) some old comments or git commit messages with references to decisions made in meetings long ago that mean nothing to you now - if you're lucky.
Upvote 7 Downvote Reply Award Share
Report
Award
Share
1 more reply 
jax024
•
4mo ago
simplicity isn't simple.
Upvote 4 Downvote Reply Award Share
Report
Award
Share 
beders
•
4mo ago
We've built a fintech on Clojure/ClojureScript and while a few of Javaisms sneaked into the initial code (many Clojure devs have Java background) we never had to do large refactoring efforts. We can still make significant changes with confidence.
This is due to a few things I would attribute to simplicity:
Most of our functions are simple - they take data and return data. We keep data models simple: they are maps, vectors, sets, lists with well defined keys and spec checks at system boundaries (that go beyond static type checks)
So most reasoning about a piece of code is local. Devs aware of what it means to break a contract set up by a function definition.
Data is immutable by default: no quirky effects because state changed unexpectedly. No issues with multi-threading at all.
Fast feedback loop thru REPL based dev: There's no wait time for changes. You can test changes interactively in your app with great tool/IDE support.
Also the front-end hot reloading story of ClojureScript w/ re-frame is still excellent and has been for many years - unchanged.
Upvote 4 Downvote Reply Award Share
Report
Award
Share
5 more replies
devraj7
•
4mo ago
"I apologize for the length of this letter, I didn't have time to make it shorter"
Upvote 3 Downvote Reply Award Share
Report
Award
Share
CurtainDog
•
4mo ago
The challenge of simplicity is not design - that's just a matter of git gud. The real challenge is convincing people to pay for it. The trick is in adding just enough gold plating to convince customers (both internal and/or external) that it's worth the spend while not compromising the core architecture.
Upvote 2 Downvote Reply Award Share
Report
Award
Share 
TheFaithfulStone
•
4mo ago
This is a good, classic talk but Rich is only talking about a single kind of simplicity - and “simplicity” is a multi-dimensional vector. Off hand, I can think of three dimensions on which we like to say things are “simple”
Abstract -> Concrete
The best example of this is 2+2. Infix addition is very abstract, but it's broadly shared, so we don't need to understand all the leaks or how to make an adder circuit. Broadly shared and understood abstractions are “simple” (files, processes, functions) while detailed concrete implementations are “complex” - (file SYSTEMs, process managers, VMs)
Single-ness -> Multiplicity
The one that Rich is mostly talking about: a single thing does a single thing, there isn't state threaded through the whole call, the function takes some arguments, returns a value, the function has a single observable side effect. Your data holds data not data AND behavior.
Straightforward -> Toilsome
How much bullshit typing to do I have to do to do the thing? Like one-to-many relations in databases are sort of obnoxious, you have to specify / type the same-ish thing a whole bunch. Rails has “belongs_to” which is straightforward as hell and also fronts an enormous amount of “magic”
Like a lot of things it's a three-way tradeoff - and how making one dimension “better” necessarily makes another dimension “worse”
Upvote 3 Downvote Reply Award Share
Report
Award
Share 
Substantial_Ice_311
•
4mo ago
• Edited 4mo ago
The best example of this is 2+2. Infix addition is very abstract, but it's broadly shared, so we don't need to understand all the leaks or how to make an adder circuit.
What? I don't understand what you are trying to say.
Upvote 3 Downvote Reply Award Share
Report
Award
Share
More replies
xthecharacter
•
4mo ago
One of the best talks of all time.
Upvote 1 Downvote Reply Award Share
Report
Award
Share 
seweso
•
4mo ago 
Top 1% Commenter
Kiss and refactoring basically. And that's only doable if you have requirements and automated tests.
Upvote -3 Downvote Reply Award Share
Report
Award
Share 
Substantial_Ice_311
•
4mo ago
• Edited 4mo ago
Saying that KISS is simplicity is a circular definition. Also, simplicity has nothing to do with tests or even requirements.
Upvote 7 Downvote Reply Award Share
Report
Award
Share
More replies
Krackor
•
4mo ago
The K in KISS is misleading. Simplicity requires hard work and careful design.
Upvote 3 Downvote Reply Award Share
Report
Award
Share
More replies
New to Reddit?
Create your account and connect with a world of communities.
Continue with Email
Continue with Phone Number
By continuing, you agree to our User Agreement and acknowledge that you understand the Privacy Policy.
Related Answers Section
Related Answers
Best talks by Rich Hickey on programming
Best practices for writing clean code
Top resources for mastering algorithms
Common mistakes new programmers make
Essential tools for software development
More posts you may like
The Simple Path to Wealth book critique r/Bogleheads • 5mo ago [
The Simple Path to Wealth book critique
](https://www.reddit.com/r/Bogleheads/comments/1pg972d/the_simple_path_to_wealth_book_critique/) 23 upvotes · 79 comments
Nobody Gets Promoted for Simplicity r/programming • 2mo ago [
Nobody Gets Promoted for Simplicity
](https://www.reddit.com/r/programming/comments/1rjo0w2/nobody_gets_promoted_for_simplicity/)  terriblesoftware 610 upvotes · 165 comments
Simple made easy? r/Clojure • 6y ago [
Simple made easy?
](https://www.reddit.com/r/Clojure/comments/g88q8y/simple_made_easy/) 15 upvotes · 30 comments
Random Rich Hickey comment on E-ink note-taking devices! r/lisp • 1y ago [
Random Rich Hickey comment on E-ink note-taking devices!
](https://www.reddit.com/r/lisp/comments/1l2dyyp/random_rich_hickey_comment_on_eink_notetaking/)  11 upvotes · 23 comments
From Chaos and 1.5 Failures to Full-time Simplicity (A 7-Year Reflection) r/RealDayTrading • 5mo ago [
From Chaos and 1.5 Failures to Full-time Simplicity (A 7-Year Reflection)
](https://www.reddit.com/r/RealDayTrading/comments/1pk7t6p/from_chaos_and_15_failures_to_fulltime_simplicity/)  116 upvotes · 69 comments
"Simplicity is prerequisite for reliability." Edsger W. Dijkstra r/quotes • 5y ago [
"Simplicity is prerequisite for reliability." Edsger W. Dijkstra
](https://www.reddit.com/r/quotes/comments/qsdr4q/simplicity_is_prerequisite_for_reliability_edsger/) 4 upvotes · 3 comments
Thanks AI! - Rich Hickey, creator of Clojure, about AI r/programming • 4mo ago [
Thanks AI! - Rich Hickey, creator of Clojure, about AI
](https://www.reddit.com/r/programming/comments/1qa0ujk/thanks_ai_rich_hickey_creator_of_clojure_about_ai/)  github 824 upvotes · 127 comments
Simple Made Easy - Prime Reacts r/Clojure • 1y ago [
Simple Made Easy - Prime Reacts
](https://www.reddit.com/r/Clojure/comments/1k6us5f/simple_made_easy_prime_reacts/)  youtu 76 upvotes · 39 comments
"Simplicity is the ultimate sophistication." r/minimalism • 5y ago [
"Simplicity is the ultimate sophistication."
](https://www.reddit.com/r/minimalism/comments/l0hda8/simplicity_is_the_ultimate_sophistication/) 15 upvotes · 6 comments
How to cope with being “Rich Hickey”-Pilled r/Clojure • 2y ago [
How to cope with being “Rich Hickey”-Pilled
](https://www.reddit.com/r/Clojure/comments/1eoipjr/how_to_cope_with_being_rich_hickeypilled/) 157 upvotes · 72 comments
Use Protocols, Not Services r/programming • 3d ago [
Use Protocols, Not Services
](https://www.reddit.com/r/programming/comments/1t6fx7a/use_protocols_not_services/) 111 upvotes · 47 comments
"Simple Made Easy" - Rich Hickey (2011) r/Clojure • 5y ago [
"Simple Made Easy" - Rich Hickey (2011)
](https://www.reddit.com/r/Clojure/comments/pgqk28/simple_made_easy_rich_hickey_2011/)  youtube 104 upvotes · 6 comments
"Simple Made Easy" by Rich Hickey [video] r/programming • 15y ago [
"Simple Made Easy" by Rich Hickey [video]
](https://www.reddit.com/r/programming/comments/lirke/simple_made_easy_by_rich_hickey_video/)  infoq 123 upvotes · 73 comments
The silent death of Good Code r/programming • 3mo ago [
The silent death of Good Code
](https://www.reddit.com/r/programming/comments/1qyytvj/the_silent_death_of_good_code/) 478 upvotes · 159 comments
"Simplicity is the ultimate sophistication." - Leonardo da Vinci r/Frugal • 15y ago [
"Simplicity is the ultimate sophistication." - Leonardo da Vinci
](https://www.reddit.com/r/Frugal/comments/ma8da/simplicity_is_the_ultimate_sophistication/) 169 upvotes · 40 comments
A couple of Edsger Dijkstra quotes i thought this sub might appreciate r/compsci • 7y ago [
A couple of Edsger Dijkstra quotes i thought this sub might appreciate
](https://www.reddit.com/r/compsci/comments/apnfnk/a_couple_of_edsger_dijkstra_quotes_i_thought_this/) 181 upvotes · 25 comments
The Root Cause Fallacy: Systems fail for multiple reasons, not one r/programming • 6mo ago [
The Root Cause Fallacy: Systems fail for multiple reasons, not one
](https://www.reddit.com/r/programming/comments/1ots577/the_root_cause_fallacy_systems_fail_for_multiple/)  perspectiveship 366 upvotes · 76 comments
"Simplicity is prerequisite for reliability." - Edsger W. Dijkstra r/quotes • 13y ago [
"Simplicity is prerequisite for reliability." - Edsger W. Dijkstra
](https://www.reddit.com/r/quotes/comments/1m1lr1/simplicity_is_prerequisite_for_reliability_edsger/) 16 upvotes · 1 comment
On sabotaging projects by overthinking r/programming • 16d ago [
On sabotaging projects by overthinking
](https://www.reddit.com/r/programming/comments/1sumkeu/on_sabotaging_projects_by_overthinking/) 62 upvotes · 16 comments
anthropic bet everything on coding reliability and it actually worked r/Verdent • 4mo ago [
anthropic bet everything on coding reliability and it actually worked
](https://www.reddit.com/r/Verdent/comments/1q841lf/anthropic_bet_everything_on_coding_reliability/) 31 upvotes · 11 comments
Clojure Documentary Q&A (with Rich Hickey and others) - April 17 r/Clojure • 1mo ago [
Clojure Documentary Q&A (with Rich Hickey and others) - April 17
](https://www.reddit.com/r/Clojure/comments/1shsvi0/clojure_documentary_qa_with_rich_hickey_and/)  zoom 74 upvotes · 3 comments
Ask HN: Is Clojure Dead? r/Clojure • 4y ago [
Ask HN: Is Clojure Dead?
](https://www.reddit.com/r/Clojure/comments/xr7n6g/ask_hn_is_clojure_dead/) 47 upvotes · 58 comments
Rich Hickey's opening remarks from Clojure/Conj 2025 r/Clojure • 4mo ago [
Rich Hickey's opening remarks from Clojure/Conj 2025
](https://www.reddit.com/r/Clojure/comments/1pyql7a/rich_hickeys_opening_remarks_from_clojureconj_2025/)  youtube 130 upvotes · 4 comments
Genuine caution to avoid taking SI110 r/uofm • 7mo ago [
Genuine caution to avoid taking SI110
](https://www.reddit.com/r/uofm/comments/1o9mh53/genuine_caution_to_avoid_taking_si110/) 62 upvotes · 20 comments
Rich Hickey (Clojure Creator) radically changed the way I think about my Java code. This talk is one of his gems. r/java • 8y ago [
Rich Hickey (Clojure Creator) radically changed the way I think about my Java code. This talk is one of his gems.
](https://www.reddit.com/r/java/comments/87fcaw/rich_hickey_clojure_creator_radically_changed_the/)  youtube 133 upvotes · 37 comments
View Post in
日本語
Français
简体中文
Português (Brasil)
हिन्दी
See more See fewer
Deutsch
Polski
ไทย
Svenska
Español (Latinoamérica)
Community Info Section
r/programming
Join
programming
Computer Programming
Show more
Public
Anyone can view, post, and comment to this community
Reddit Rules Privacy Policy User Agreement Your Privacy Choices Accessibility Reddit, Inc. © 2026. All rights reserved.
Expand Navigation
Expand Navigation
Collapse Navigation
Collapse Navigation 
0cAFcWeA4O_6aeRq9mlRSVFp26erdYJcGx_4K9ZjtSOj6dexBBLw-yx9m8Bvjz4L5zOCcKFmF21f7YPF4DAsXV5ZRktT4PDl6nY2Y6xIfee1lQEwyuEXfJFKSi0Ic9V0ArLaiwKAYgePTEs28nRamrTOhKm6UsH3a5kuDgccOZic43xAUxzg1-_TrOfIvJAnApX2I1cIUcnEI8xTfvGDA4DhICb-QJ1Q1nObwkxsoKIMRIoMR_Nm3GBhYIOoF2F4Tk5qnzyFVnAPMLzmCkAay5JC4Mgs_s8cJ6pjiTonoNwW5Qkia-y0-tJlhJzs0BhR5m45RZqZD3M4rH0ZaPkaciBcVnnZXPJXVqKKKebLCLW1GHF8SgPK_cyPxEWDXpNGGqA-QcuyFzL0y6fnQf8MWA_d9fqpBJ-7HMs1z_KbWsaqrLDsUazlHdaLy16WlTgvgSXJdaorjFdJDHxg8am2GSUCcpd1gGK4UPXx9_yHRJkeT2Maw6vzMpZ9Tf0Ew6PWDAyuPVbaZf7ipAIVD8ppqNY-iUe9x4m6bV2nHGZv0JJ69rCMdCcu_8lbYF4mgAjFo2aRdQ7DRA3V5sANIuxdqSIz_GhosurqAs_xsIJagFeHwsSL0Y1ZJFi02bUOzMXcpKH8bIQvxYBexIye_tfmQa-vOd87rvu2pIHm4wvo1GwIaXd2Kwaa0ipr1IZ0ehu6y2euXSvm5afMsnvNxRa70d-GdKAN-DvlGp0IVsogH7U6BhJBHXcW-CkxMfxyBLApvgNXFYlKt5Iht8JQeGKZNeLtJo3LghxTBaq9hd1niBqP06cA3s12SO1qU7CCDXKexWwhUaEaDSYcxzFFK-oSjqhVoM7WU89aW3Qs-QRsC_MLlcHdbjBTikl-1LiK6Tz6NxmsBUzhGEXZgZ32Va7DXF4z7f9mZtXhgzeRKfcenpCtWmjBeY-me_LbldmklnYRneDFk4LysYEW2--NAEYARTGsPYBM8AHmM4JBMEy7vneIYNfVdMeXSZa_uYrpczz1z50BXbNY3-FDBCLZUTIvNeW0yu_OVrBTJwKp31yORxV4g7zIP9hgUNx2_G2_jpvLXjmo8iHwK6egTc7Mm83BqmW2lc3VjbzdqWX6oGrA_FN6zqqwThSiGnMnLJt5sGyh7Vfux-0f7uEi6gZTrNju1_aM8L6wGVzb6gaiXQP3JMGPGxA2WTAO4PojbTkKZD8w0jY1-YjxMysJ79vZ7hWvUh77Hmrud4rTlILne5zg3V8ttxuuGFx6sm00K93hx_PMHob79Gc6hshNHSMwH8HbP8qatkWcs1WFd6DLfGjSHNKm-o0oFdO84JY2HusyxyimBxjEnvv2HMoa55w1UkX1l8lYSnvflLJi2gmK8e4OsDvFHBtjG6a_RKxJ2jXu9MQjLi2HC77YrPJTp1-Ws39vdT9qmlc_mzbZO7ken9soATA2MqRnWGcyvGvlJ0gKQNlN1SYudgXW9mTPmYaIOMqoWVQKvPXWjzFWELSY8NOHf7pWNU8O4EipQWGbLGU7O0XrkwRS4sINC117zvc5ydm4WnL5V16ysj-TGa7i1ZD0Pmo_gioN8tCzsRQIghGcRd7mZXj_73Lv1VuAOa8embD_6gKMg2NRMYtSy2tltKDwMV2AWfdLUIjv65vRRes-S6n9hqVJVxYSEwRRkHH_M250Vjnj8rOxz3DA11fsY7gR43FgiLFwHiknFaR-H0R_RCJgocY0krcRrCfZwFLQQaVHRbd9AQ46fZL1GuEsmfhUEAGZyw7c2ffNwpHcrwvLuuPhCgiDCo38pLs87A1zuAYNv8KyF0XujMF-o0XrxanS855zm1q9Blv_YpqHb0IQ517D0iuMoJDKFYlMc4ODkegwyCJTOetUSDzTipdUOMuJaTRFwJEPa131Rsj2OlScfO3jr0d_rJci_HwuACD5B9bByr_Vb3pG2Bu_JRll0PYcqqGaNnbVy8mxeanVKTihgmomfEavN7hA8Fke6EKOH0AaFMh9-tZHEe1cyfkwqCso3j-sfyymbMG3ecxbT3KzJGsTJv8mYYSuoFftJrs8CjgLrKlsBSR3tlqa3CoQHructJ-rNJyGSbZpoytIXvwQyYwY3sWN7kej8n64co1gjmVAAAlS63aRw77YyfdpsH5pJ7TwbyrDtDy_jJlW4k-1-JpYndVTT83V6F2WqZG2YB6eEDo6c0BF0iS13kBg
