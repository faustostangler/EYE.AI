---
name: Managing intermodule communication in a transition from a Monolith to Hexagonal Architecture : r/softwarearchitecture - Reddit
keywords: (placeholder)
metadata:
  url: https://www.reddit.com/r/softwarearchitecture/comments/1ith7gc/managing_intermodule_communication_in_a/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Managing intermodule communication in a transition from a Monolith to Hexagonal Architecture : r/softwarearchitecture
Skip to main content Managing intermodule communication in a transition from a Monolith to Hexagonal Architecture : r/softwarearchitecture
Open menu
Open navigation 
Go to Reddit Home 
r/softwarearchitecture
Sign Up
Sign up for Reddit
Log In
Log in to Reddit
Expand user menu
Open settings menu
Skip to Navigation Skip to Right Sidebar
Back
Go to softwarearchitecture
r/softwarearchitecture
•
1y ago
AttitudeImpossible85
Locked post
Stickied post
Archived post
Report
Managing intermodule communication in a transition from a Monolith to Hexagonal Architecture
Discussion/Advice
I've started to decouple a "big ball of mud" and am working on creating domain modules (modulith) using hexagonal architecture. Since the system is live and the old architecture is still in place, I'm taking an incremental approach.
In the first iteration, I still need to allow some function calls between the new domain module and the old layered architecture. However, I want to manage intermodule communication using the orchestration pattern. Initially, this orchestration will be implemented through direct function calls.
My question is: Should I use the infrastructure incoming adapters of my new domain modules, or can I use application incoming ports in the orchestration services?
Choice infrastructure incoming adapters:
I would be able to hide some cross-cutting concerns relating to the domain.
I would be able to place feature flags here.
A downside is that I might need to create interfaces to hide the underlying incoming ports of application services, which could add an extra level of complexity.
What's your take on?
Upvote 8 Downvote 14 Go to comments Share
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
SilverSurfer1127
•
1y ago
Hexagonal architecture is also called ports and adapters and relies heavily on dependency inversion. So using adapters directly is a detour back to a big ball of mud. IMO interfaces are not an extra level of complexity but rather a clean way to have healthy contracts and therefore clean boundaries. The result of such design is flexibility and better testability.
Upvote 5 Downvote Reply Award Share
Report
Award
Share
AttitudeImpossible85
OP
• 1y ago
I'm sorry I meant if I expose the domain logic through incoming adapters I have to use interfaces for those adapters because the use case interfaces should be visible outside and it doesn't make sense to expose the domain logic via two interfaces.
Upvote 1 Downvote Reply Award Share
Report
Award
Share
More replies 
edgmnt_net
•
1y ago
healthy contracts and therefore clean boundaries
Sounds good in theory, but a large part of software just can't have clean, stable and robust boundaries given the usual constraints without serious side-effects. Not at the level of small components anyway. (E.g. a general video encoding solution is doable, provided you take the time to analyze codecs and their parameters so the contracts actually mean something and don't change every day, but a lot of software is way more ad-hoc than that and needs to do something very specific.)
Flexibility is also tricky. Indirection does provide some, but it's often not the kind of flexibility you want, e.g. overridable getters and setters more often invite spaghetti code and hacks, when even refactoring may be a better (and often easier) solution.
Upvote 1 Downvote Reply Award Share
Report
Award
Share
More replies 
flavius-as
•
1y ago
Let's go through top down. Some of these points might need clarification from you
Transition from monoliths to hexagonal: these are not at all opposing - a hexagonal modulith is still deployed as a monolith
doing it gradually is the right thing to do
" some function calls between the new domain module and the old layered architecture" the direction of dependencies matters here. You want the legacy to call the new thing and not the other way around. The reason is that you plan to eliminate legacy eventually, and if you call legacy from your new thing, when you explain to management why you might have a delay, it will sound more often like your new thing is the problem
i recommend starting with a new feature in the new system. It allows you to create the required infrastructure and connect it to business value, instead of a purely technical endeavor
continue implementing and refining your approach with 2-4 more new clean-slate features. Legacy calls hexagon.
Upvote 2 Downvote Reply Award Share
Report
Award
Share
Orbs
•
1y ago
What is the problem you're trying to solve? This reads like you want to apply some patterns rather than fix something.
Splitting things into a domain module is a great idea for separating business logic. If you need the domain to be able to call into non-domain code, you typically do this by defining an interface in the domain and having the non-domain code implement that interface.
Upvote 2 Downvote Reply Award Share
Report
Award
Share
AttitudeImpossible85
OP
• 1y ago
I'm restructuring the code base which has extreme cognitive load because it violates the separation of concerns. Defining an interface in the domain to call into non-domain code is something I would like to avoid because it assumes a choreography that is hard to track across domains and not domain switches.
Simplifying my question: What's wrong with having incoming infrastructure adapters to make available domain use cases for non-domain code? Is it an anti-pattern in hexagonal architecture if I don't have a real infrastructure-related adapter like a controller for rest endpoints?
Upvote 1 Downvote Reply Award Share
Report
Award
Share
More replies
cantaimtosavehislife
•
1y ago
I'm also very interested in this question.
I've got a 'modular' monolith. The modules can be quite coupled in parts though. For instance I'd have a Customers module and an Orders module, the Orders module makes reference to the Customers module domain.
I can't see an elegant way around this at the moment without creating a copy of all the necessary customer parts within the Order domain and using some sort of anti corruption layer to translate Customer domain into the Order domains customer entities.
I'd be interested to hear how others have tackled this.
Upvote 1 Downvote Reply Award Share
Report
Award
Share 
flavius-as
•
1y ago
• Edited 1y ago
The modules should be aligned to bounded contexts.
Yes that duplication is just duplication of code, but it's not duplication of semantics.
Customer in the front-end means prospective customer, the one on which you want to gather data for further analytics etc.
Customer in an order module means other things based on business model and what other modules might be.
If your business model is clearly defined, the edges of the bounded contexts are easier to see.
You evaluate if you've cut the boundaries right if, when making a change, you need to touch only one module, more often than not.
If that's not the case, in 90% of cases the root cause is approaching the design too much as a programmer and too little as a business modeller.
Upvote 3 Downvote Reply Award Share
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
Best practices for microservices architecture
Common pitfalls in software design
How to choose the right database architecture
Trends in software architecture for 2024
Key principles of clean architecture
More posts you may like
Geometric B1 r/EDHBrews • 5d ago [
Geometric B1
](https://www.reddit.com/r/EDHBrews/comments/1t4ehgw/geometric_b1/)  85 upvotes · 27 comments
Is a hexaconsonantal root system feasible for an alien language? r/conlangs • 8d ago [
Is a hexaconsonantal root system feasible for an alien language?
](https://www.reddit.com/r/conlangs/comments/1t1z7d3/is_a_hexaconsonantal_root_system_feasible_for_an/) 42 upvotes · 19 comments
IBM partners with Signal to develop quantum-safe messaging encryption r/signal • 2mo ago [
IBM partners with Signal to develop quantum-safe messaging encryption
](https://www.reddit.com/r/signal/comments/1rpp7dh/ibm_partners_with_signal_to_develop_quantumsafe/)  cyberinsider 842 upvotes · 27 comments
Interstellocaster r/warmoth • 10mo ago [
Interstellocaster
](https://www.reddit.com/r/warmoth/comments/1lolw5q/interstellocaster/)  2 49 upvotes · 10 comments
I hope they never add reactivity for Heinrix's callous route to his romance because it's way funnier this way r/RogueTraderCRPG • 9mo ago [SPOILER
I hope they never add reactivity for Heinrix's callous route to his romance because it's way funnier this way
](https://www.reddit.com/r/RogueTraderCRPG/comments/1n287bt/i_hope_they_never_add_reactivity_for_heinrixs/)  519 upvotes · 74 comments
Geometric Tessellations r/creativecoding • 6mo ago [
Geometric Tessellations
](https://www.reddit.com/r/creativecoding/comments/1p5xaop/geometric_tessellations/)  0:47 392 upvotes · 9 comments
Why does Heinrix always look so tired ? r/RogueTraderCRPG • 4mo ago [
Why does Heinrix always look so tired ?
](https://www.reddit.com/r/RogueTraderCRPG/comments/1qh6nl7/why_does_heinrix_always_look_so_tired/)  3 346 upvotes · 52 comments
Inter-Dimensional Beings r/ExistentialJourney • 4mo ago [
Inter-Dimensional Beings
](https://www.reddit.com/r/ExistentialJourney/comments/1q015zt/interdimensional_beings/) 109 upvotes · 31 comments
Does this count as a series or parallel circuit? r/shittyaskelectronics • 4mo ago [
Does this count as a series or parallel circuit?
](https://www.reddit.com/r/shittyaskelectronics/comments/1qm0694/does_this_count_as_a_series_or_parallel_circuit/)  185 upvotes · 45 comments
Heinrix tolerated way more of my xeno-fraternizing bullshit than I could have imagined. r/RogueTraderCRPG • 10mo ago [SPOILER
Heinrix tolerated way more of my xeno-fraternizing bullshit than I could have imagined.
](https://www.reddit.com/r/RogueTraderCRPG/comments/1m4ns0t/heinrix_tolerated_way_more_of_my_xenofraternizing/)  765 upvotes · 43 comments
What do folks mean by inter-dimensional ? r/UFOs • 2mo ago [
What do folks mean by inter-dimensional ?
](https://www.reddit.com/r/UFOs/comments/1rh9tdp/what_do_folks_mean_by_interdimensional/) 33 upvotes · 107 comments
Discussion on possible communication r/Experiencers • 10mo ago [
Discussion on possible communication
](https://www.reddit.com/r/Experiencers/comments/1lvhu29/discussion_on_possible_communication/) 46 upvotes · 34 comments
Why can we not give THE THING to Heinrix? r/RogueTraderCRPG • 9mo ago [
Why can we not give THE THING to Heinrix?
](https://www.reddit.com/r/RogueTraderCRPG/comments/1munrqg/why_can_we_not_give_the_thing_to_heinrix/) 114 upvotes · 48 comments
Need help regarding deployment of IPSec tunnels in a multicloud hybrid environment. r/networking • 1y ago [
Need help regarding deployment of IPSec tunnels in a multicloud hybrid environment.
](https://www.reddit.com/r/networking/comments/1in0oix/need_help_regarding_deployment_of_ipsec_tunnels/) 27 upvotes · 17 comments
Clean-sheet architecture for a startup: integration orchestration and minimizing infrastructure management r/softwarearchitecture • 1y ago [
Clean-sheet architecture for a startup: integration orchestration and minimizing infrastructure management
](https://www.reddit.com/r/softwarearchitecture/comments/1isf65e/cleansheet_architecture_for_a_startup_integration/) 17 upvotes · 4 comments
How can I design a scalable LLM middleware to handle indefinite conversations while retaining context? r/LocalLLaMA • 1y ago [
How can I design a scalable LLM middleware to handle indefinite conversations while retaining context?
](https://www.reddit.com/r/LocalLLaMA/comments/1hku5z6/how_can_i_design_a_scalable_llm_middleware_to/) 13 upvotes · 6 comments
Apparently intuitionistic logic is paraconsistent r/badmathematics • 20d ago [
Apparently intuitionistic logic is paraconsistent
](https://www.reddit.com/r/badmathematics/comments/1sr6ebk/apparently_intuitionistic_logic_is_paraconsistent/) 37 upvotes · 13 comments
How to get rid of these inter dimensional beings? r/Experiencers • 9mo ago [
How to get rid of these inter dimensional beings?
](https://www.reddit.com/r/Experiencers/comments/1mpd7v9/how_to_get_rid_of_these_inter_dimensional_beings/) 95 upvotes · 128 comments
Quantum Thermodynamic Emergence: A Derivation-Driven Theory of Abiogenesis as a Phase Transition r/CoherencePhysics • 1mo ago [
Quantum Thermodynamic Emergence: A Derivation-Driven Theory of Abiogenesis as a Phase Transition
](https://www.reddit.com/r/CoherencePhysics/comments/1seb98x/quantum_thermodynamic_emergence_a/)  15 30 upvotes · 18 comments
Heinrix is so bad at his job r/RogueTraderCRPG • 2mo ago [
Heinrix is so bad at his job
](https://www.reddit.com/r/RogueTraderCRPG/comments/1rjokgq/heinrix_is_so_bad_at_his_job/)  294 upvotes · 30 comments
Just got Heinrix, and he's literally my MC 😭 r/RogueTraderCRPG • 27d ago [
Just got Heinrix, and he's literally my MC 😭
](https://www.reddit.com/r/RogueTraderCRPG/comments/1sk79si/just_got_heinrix_and_hes_literally_my_mc/) 85 upvotes · 38 comments
A New Quantum Model Proposes Your Brain Rewrites Reality Before You Know You've Seen It r/abovethenormnews • 26d ago [
A New Quantum Model Proposes Your Brain Rewrites Reality Before You Know You've Seen It
](https://www.reddit.com/r/abovethenormnews/comments/1slojgt/a_new_quantum_model_proposes_your_brain_rewrites/)  abovethenormnews 64 upvotes · 14 comments
Quantum Realms [OC] r/fractals • 6mo ago [
Quantum Realms [OC]
](https://www.reddit.com/r/fractals/comments/1om7wk7/quantum_realms_oc/)  0:20 64 upvotes · 8 comments
I'm not understanding Heinrix. r/RogueTraderCRPG • 2mo ago [SPOILER
I'm not understanding Heinrix.
](https://www.reddit.com/r/RogueTraderCRPG/comments/1rq6afh/im_not_understanding_heinrix/) 103 upvotes · 50 comments
Modular vs. Monolithic Approaches in LLM-Driven System Design r/LLMDevs • 1y ago [
Modular vs. Monolithic Approaches in LLM-Driven System Design
](https://www.reddit.com/r/LLMDevs/comments/1hy1uy7/modular_vs_monolithic_approaches_in_llmdriven/) 5 upvotes · 3 comments
View Post in
Português (Brasil)
简体中文
日本語
See more See fewer
Deutsch
Filipino
Community Info Section
r/softwarearchitecture  
The Incident, a CTF-style Production Outage contest, is starting soon! Cash prize is $100. See highlighted post for more details!
Join
Software Architecture
Dive into discussions on designing, structuring, and optimizing software systems. Share insights on architectural patterns, best practices, and real-world experiences.
Show more
Public
Anyone can view, post, and comment to this community
Top Posts
Reddit reReddit: Top posts of February 19, 2025
Reddit reReddit: Top posts of February 2025
Reddit reReddit: Top posts of 2025
Reddit Rules Privacy Policy User Agreement Your Privacy Choices Accessibility Reddit, Inc. © 2026. All rights reserved.
Expand Navigation
Expand Navigation
Collapse Navigation
Collapse Navigation 
0cAFcWeA4rIKqqeZDcW8YgdGF5rFM3jyc601aoAxzBvyTDU_aie3s0V7-SZjTDYys3Cw0ZYY5O2GNIcyegB0nY6z_E_prqj25Xg5pL_5XoBqNCl5lLx9NAEhyVMozI1bLSK_yQgEkw62EyQDPTnVIE1dx4OH6aUtdUnfSkxVxWrxbww305UECZU789_OW6IqKEjOR6-zl-oUMO3RFTeLITMc7yePx0ggbUm09gaz6Vgo1zbSDPWjcujkiCzlxsi52BNiqU8qsU8_09P7FWstE_IyFgCpgEuRl6Mig3H7K5GWUFH7rfN9v6szB4E86qq6UEfAI_dr31c07NwnZN8y5RtYec6w5pO1Q89jl5Axn7xwSy4rBq_sYprgFL6Psb0ozMRfDqsPZVuWGsYnpqM6pgY6ctDAZ-xdKuKiL-TP_BaszSskccKuafVQai74i8RZT7m2wo7BSLJYik4kIY79gCutPi0bGux0amJpSf5FheVYI_sEXh7cDTuMzP69CEN8C4PJvS1dVy37b_qNTECoi3fF_qOTUuAjveIXPeSIB_lgxjkd9JIy0HrpdIURZ4SqUgt-kwAvd3UTSX1VNNEjCO-684JHBNh9XgkjauywVtyqLcj7LDHVUyJ4EI-HaOTJEVw4WihGT84ofZIZHBexmVEr0IU0w2aIsrY1IYR86qL2RU41Mo4dCwhyPoxwp2CON7egBsD5KHzS1QjRiQprIDkHBqxlNVfHTIXtFupjWgyyR_2qdNGXKXab1ekKC2Lb_kIkVGgtEM7p7Jth_UNuSuxfGifTCbl2EZJ-r9hmOAaHjbIdnruZmHC7B3yu_vxGM4d9wWHwJfj5o4eRGmDKF5c3cz1R9l--esDZwaHjEH2u_CsmTgOFDCCD9vDfCFqxWrhyBliTmSHnaz22v3IoZnovDVwrdB870E8BYjBYKge3aQhOwwj_S7E7Reh4clAj5aT5IXrZyphnw-EZBph6vNKKqz_ohJqEaI_G5cIYPD_yncEGxqiF3ZQ9urW5FnL54_Tpbuk6TEzembrU7g-9Z2SYeUy84xdmlHti73q4uaq99HUl6zXPYV-JaJkUrHI7F65Sq7HziXp0a9gDFl_TtbRbYRvEkOiBSbz7tCQrGoqoU-27Crn5a0nSj3Op6O_rQeBhK9fs1ZyS_F9nLDZJtFUZFnHGJMEGbEmVDefgNuHUkFPXBn6ktPcrAHwSdXA2NputD2LjzendmB560pmnS5gfNPbOObP9318F_N7g1NYaTPjWlyYEJJ5DWbZwXumc30TF0YcJNnRRngt2dkHanCIV_P6U_ADpBjVJlZsD3UwFhMq9OnDxgc3c0uzAGiw4bV5kRCQAj5FceAPBgkdYhw4Y_ILuioY5nESpnPrJJE6baCBkd396vSGW-i8rd6EpFiwvaHpCWHcAuIDGEBHy4d3VBYVx229khl9Jmoro11dGT1IFBBp7vHwEHIEnArNya6kKPIz_DZeOT3n_GMoPHSxt-oweY43xOAy9K74ZAOUjDF5sh2rhoMMSnMAmyHOt11Xrpuv0O0o9Qn4A44y7x1U80ylR_csNJpr-tsnBJE5Mw5NT4bKJ70PA6sM_KFQbnuyD66y5eqMXYgxdhN2zDF2AvnZhbYV957JR0FYoNCNI9M2eDph1l8I3BSjO79FcWDyphOGaqMTakinEvDWGJnyPnXiLexENk9GJ1OApeHkJla2hbcud3GOMevQiot6FUVUJF8OPs58hXT9jeBNDDWYvxIkIfvJ0ZjODn7pUbbd_xIjIvooTMGoPczrwJKCrUq8TAuYFw6xaztEKO525anXMgI3jLYdk6uG4jXmegCi37mdOWvRIpaSnXwAfpHz_hztXhyjO6UH_1uF2yDARInNQaQdR-h_CeVjRVgT7cORLOlKtjP5I2w9scTvsQcNAJfAFtJW4VAA81_s7YsodaSl6Zg4Ncyj2JrfFlauVvca2utmUKaqQ4fNA0csC6DrjN4gkaeawHmIRDVxX72m0ELatAZtRLKGJpbxvhurQmI-CeWnrdW6oEbJPUA_AmDj4EG4CdNo-BU5VuAlf840idycDgMo7uolh_vzVt231tybaFYxzeNDGS2yHPfBBwXsCZf31H9cDN-0_bxUgmYf87jozvWhOc_DyqS3xYGEcqmkdx39pwmbAfWPGlrJR4bZRYm9RcIOdyxFYkkD8Xl81FWCmEWR5EIuyi7Zw
