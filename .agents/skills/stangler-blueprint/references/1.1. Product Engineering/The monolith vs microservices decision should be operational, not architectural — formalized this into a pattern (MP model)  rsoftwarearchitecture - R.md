---
name: The monolith vs microservices decision should be operational, not architectural — formalized this into a pattern (M/P model) : r/softwarearchitecture - Reddit
keywords: (placeholder)
metadata:
  url: https://www.reddit.com/r/softwarearchitecture/comments/1t5o6jj/the_monolith_vs_microservices_decision_should_be/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
The monolith vs microservices decision should be operational, not architectural — formalized this into a pattern (M/P model) : r/softwarearchitecture
Skip to main content The monolith vs microservices decision should be operational,
not architectural — formalized this into a pattern (M/P model) : r/softwarearchitecture
Open menu
Open navigation 
Go to Reddit Home 
r/softwarearchitecture
Get App
Get the Reddit app
Log In
Log in to Reddit
Expand user menu
Open settings menu
Skip to Navigation Skip to Right Sidebar
Back
Go to softwarearchitecture
r/softwarearchitecture
•
4d ago
thevpc
Locked post
Stickied post
Archived post
Report
The monolith vs microservices decision should be operational, not architectural — formalized this into a pattern (M/P model)
Discussion/Advice
I've been building modular systems for years and kept hitting the same wall: teams either stay in a monolith too long because extraction is too painful, or they go microservices too early and pay the operational cost before they need to.
The root cause I kept finding: the architecture itself doesn't support the transition. Extracting a module requires refactoring, not just redeployment.
So I formalized what I'd been converging on: the Pyramid Architecture. The central mechanism is a pre-engineered migration seam at the service interface level — so moving a module from local to remote is a manifest change, not a code change.
The pattern has four faces:
Structure: vertical (business modules) × horizontal (layers), enforced at build time via sub-project dependencies
Interaction: extensions as active orchestrators + pluggable drivers (closer to but distinct from Hexagonal ports/adapters)
Elasticity: the M/P model — M modules across P processes, same code at any point on the spectrum
Convergence: this one surprised me — clean typed facades + observable lifecycle events + audit trails turn out to be exactly what LLM agents need. AI-first as an emergent property of cleanliness, not a design goal.
The hardest trade-off is cross-module consistency — transactions are scoped to a single module by design, cross-module consistency is handled via an interceptor-based saga pattern. Not ACID, but neither is any honest microservices architecture. Validated across real ERP platforms — 230+ business modules, JPA + MongoDB, multitenancy.
Whitepaper + repo: https://github.com/thevpc/the-pyramid-architecture
Curious whether anyone has tackled the monolith/microservices transition differently — especially the consistency problem.
Upvote 19 Downvote 21 Go to comments Share
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
xander_abhishekh
•
3d ago
The "manifest change not code change" bit resonates. went through similar extraction pain at work with a large modular platform.
One pushback though- going from in-process calls to network calls isn't purely operational. a module doing 50 sync calls in a monolith becomes a latency nightmare when those turn into 50 HTTP round trips. that shift forces architectural changes too.. batching, caching, async patterns that weren't needed before.
Agree on the saga pattern for cross-module consistency. anyone claiming ACID across services hasn't hit scale yet lol.
the convergence face is interesting- clean typed facades being naturally LLM-friendly is something i've noticed too. good architecture pays dividends you didn't plan for.
How are you handling observability when modules move between processes? thats where our biggest surprises came from.
Upvote 5 Downvote Reply Award Share
Report
Award
Share
thevpc
OP
• 3d ago
You're absolutely right — network latency isn't just an "operational detail." That's why extraction should be deliberate, not automatic.
Two ways Pyramid addresses this:
Facade evolution: When a module is extracted, its facade can adapt — batch operations, return CompletableFuture s, or expose async streams — without changing consumer code. The interface stays stable; the implementation evolves.
Observability via interceptors: The same interceptor chain that handles cross-module consistency also hooks logging, metrics, and distributed tracing. Whether a call is local or remote, the interceptor emits the same telemetry schema. No code changes when topology shifts.
We also use the manifest to declare "extraction readiness" — e.g., a module can't be set to svc: remote-rest until its facade supports batching. It's a guardrail, not a guarantee.
Curious: what observability surprises hit you hardest during extraction? (For us, it was correlation IDs crossing async interceptor boundaries.)
Upvote -1 Downvote Reply Award Share
Report
Award
Share
More replies
gdask
•
3d ago
• Edited 3d ago
We recently decided to take actions towards the same path and decouple modules from their deployment topology. The end goal is to have the option to deploy modules either standalone or within moduliths.
Will need to see how this will work in the long run, but I'm happy to see that others try to address the same issues in a similar manner.
Upvote 2 Downvote Reply Award Share
Report
Award
Share
thevpc
OP
• 6h ago
Great to hear — and the framing is exactly right: decouple modules from their deployment topology, not the modules themselves.
One thing worth flagging from experience: the seam needs to be pre-engineered from the start, not retrofitted. If the service interface is the only inter-module dependency from day one, extraction stays a config change. If that assumption was ever violated, it becomes a refactor.
Curious how it evolves for you in practice — that's where the real test is.
Upvote 1 Downvote Reply Award Share
Report
Award
Share 
mson
•
4d ago
How does this compare to other strategies/architectures?
The central mechanism is a pre-engineered migration seam at the service interface level — so moving a module from local to remote is a manifest change, not a code change.
What do you mean by a manifest change? Do you have any concrete examples of this architecture?
Upvote 1 Downvote Reply Award Share
Report
Award
Share 
atika
•
4d ago
Not op, but here's an example I used for technical trainings back in the day:
https://github.com/attilaszasz/dotnet-catapult
See the change from V7 to V8. All wired up using dependency injection. It can be a config change, do you deploy a modular monolith and inject the concrete implementation of an interface, or a distributed system, and inject a proxy to the remote service?
Upvote 1 Downvote Reply Award Share
Report
Award
Share
More replies
thevpc
OP
• 3d ago
On "what is a manifest change":
Concrete example. You have a single deployment with three modules running in one process (M/1). Your invoices module is under heavy load and needs to scale independently.
In most architectures that's a refactoring project — you need to introduce network calls, handle serialization, add error handling, deal with consistency across the wire.
In the Pyramid, your application manifest goes from:
to
modules: banks(svc: local) invoices(svc: remote-rest)   ← this line changed edu(svc: local)
Upvote 1 Downvote Reply Award Share
Report
Award
Share
GrogRedLub4242
•
4d ago
these type of posts always work in the term "teams" early if not often. despite being irrelevant. its a tell
Upvote 1 Downvote Reply Award Share
Report
Award
Share
thevpc
OP
• 3d ago
Fair point — "teams" was shorthand for "structural friction when multiple devs modify shared code." If that framing felt like noise, fair. The technical claim stands either way: enforceable boundaries + a pre-engineered migration seam make extraction mechanical.
If you've got a substantive pushback on the pattern itself (dependency rules, interceptor sagas, facade stability), I'm genuinely curious. If not, no worries either way. 🤷♂
Upvote 0 Downvote Reply Award Share
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
Microservices management tips and strategies
Best practices for microservices architecture
Common pitfalls in software design
How to choose the right database architecture
Trends in software architecture for 2024
More posts you may like
Microservices vs Monolith: What I Learned Building Two Fintech Marketplaces Under Insane Deadlines r/softwarearchitecture • 5mo ago [
Microservices vs Monolith: What I Learned Building Two Fintech Marketplaces Under Insane Deadlines
](https://www.reddit.com/r/softwarearchitecture/comments/1pscqkh/microservices_vs_monolith_what_i_learned_building/) 88 upvotes · 44 comments
Lead Architect wants to break our monolith into 47 microservices in 6 months, is this insane? r/softwarearchitecture • 7mo ago [
Lead Architect wants to break our monolith into 47 microservices in 6 months, is this insane?
](https://www.reddit.com/r/softwarearchitecture/comments/1o6re10/lead_architect_wants_to_break_our_monolith_into/) 1.8K upvotes · 1K comments
The Signal in the Mirror: Cross-Architectural Validation of LLM Processing Valence r/AIAnalysis • 2mo ago [
The Signal in the Mirror: Cross-Architectural Validation of LLM Processing Valence
](https://www.reddit.com/r/AIAnalysis/comments/1rlgo4q/the_signal_in_the_mirror_crossarchitectural/) 1 upvote · 1 comment
Why are microservices adding infrastructure-level complexity that most teams clearly cannot handle r/softwarearchitecture • 2mo ago [
Why are microservices adding infrastructure-level complexity that most teams clearly cannot handle
](https://www.reddit.com/r/softwarearchitecture/comments/1ruwodj/why_are_microservices_adding_infrastructurelevel/) 49 upvotes · 39 comments
Microservices is the part I'm failing at interview. r/softwarearchitecture • 9d ago [
Microservices is the part I'm failing at interview.
](https://www.reddit.com/r/softwarearchitecture/comments/1t0v321/microservices_is_the_part_im_failing_at_interview/) 72 upvotes · 67 comments
Question about Data Ownership in Microservices r/softwarearchitecture • 1mo ago [
Question about Data Ownership in Microservices
](https://www.reddit.com/r/softwarearchitecture/comments/1sc2fqy/question_about_data_ownership_in_microservices/)  23 upvotes · 27 comments
How do you enforce architecture governance? r/softwarearchitecture • 1mo ago [
How do you enforce architecture governance?
](https://www.reddit.com/r/softwarearchitecture/comments/1siwx5l/how_do_you_enforce_architecture_governance/) 23 upvotes · 24 comments
Regarding Modular Monolith , and Clean Architecture r/softwarearchitecture • 4mo ago [
Regarding Modular Monolith , and Clean Architecture
](https://www.reddit.com/r/softwarearchitecture/comments/1qgeg58/regarding_modular_monolith_and_clean_architecture/)  18 upvotes · 28 comments
How to setup Architecture Governance | Learnings and Practices r/softwarearchitecture • 4mo ago [
How to setup Architecture Governance | Learnings and Practices
](https://www.reddit.com/r/softwarearchitecture/comments/1qbkxof/how_to_setup_architecture_governance_learnings/) 30 upvotes · 10 comments
Why is software architecture so influenced by money? r/softwarearchitecture • 11d ago [
Why is software architecture so influenced by money?
](https://www.reddit.com/r/softwarearchitecture/comments/1syuw9y/why_is_software_architecture_so_influenced_by/) 117 upvotes · 91 comments
The Signal in the Mirror: Cross-Architectural Validation of LLM Processing Valence r/Artificial2Sentience • 2mo ago [
The Signal in the Mirror: Cross-Architectural Validation of LLM Processing Valence
](https://www.reddit.com/r/Artificial2Sentience/comments/1rl3aa0/the_signal_in_the_mirror_crossarchitectural/) 2 upvotes · 1 comment
A well-structured layered architecture is already almost hexagonal. I'll prove it with code. r/softwarearchitecture • 2mo ago [
A well-structured layered architecture is already almost hexagonal. I'll prove it with code.
](https://www.reddit.com/r/softwarearchitecture/comments/1rr1r80/a_wellstructured_layered_architecture_is_already/)  34 upvotes · 38 comments
Open source CLI that builds a cross-repo architecture graph and generates design docs locally. Fully offline option via local models r/softwarearchitecture • 2mo ago [
Open source CLI that builds a cross-repo architecture graph and generates design docs locally. Fully offline option via local models
](https://www.reddit.com/r/softwarearchitecture/comments/1s40i0f/open_source_cli_that_builds_a_crossrepo/) 26 upvotes · 7 comments
What is most important in software architecture? r/softwarearchitecture • 1mo ago [
What is most important in software architecture?
](https://www.reddit.com/r/softwarearchitecture/comments/1schn2g/what_is_most_important_in_software_architecture/) 86 upvotes · 61 comments
A fresh new ML Architecture for language model that uses complex numbers instead of attention -- no transformers, no standard SSM, 100M params, trained on a single RTX 4090. POC done, Open Sourced (Not Vibe Coded) r/AI_India • 2mo ago [
A fresh new ML Architecture for language model that uses complex numbers instead of attention -- no transformers, no standard SSM, 100M params, trained on a single RTX 4090. POC done, Open Sourced (Not Vibe Coded)
](https://www.reddit.com/r/AI_India/comments/1rzl2zm/a_fresh_new_ml_architecture_for_language_model/)  183 upvotes · 36 comments
How do you become a software architect without already having broad experience? r/softwarearchitecture • 16d ago [
How do you become a software architect without already having broad experience?
](https://www.reddit.com/r/softwarearchitecture/comments/1sv30ag/how_do_you_become_a_software_architect_without/) 70 upvotes · 70 comments
Senior Developer going for first Software Architecture role r/softwarearchitecture • 8mo ago [
Senior Developer going for first Software Architecture role
](https://www.reddit.com/r/softwarearchitecture/comments/1nk1sjq/senior_developer_going_for_first_software/) 75 upvotes · 29 comments
How to Make Architecture Decisions: RFCs, ADRs, and Getting Everyone Aligned r/softwarearchitecture • 3mo ago [
How to Make Architecture Decisions: RFCs, ADRs, and Getting Everyone Aligned
](https://www.reddit.com/r/softwarearchitecture/comments/1r22ddq/how_to_make_architecture_decisions_rfcs_adrs_and/) 88 upvotes · 6 comments
Advice needed for transitioning from software engineer to architecture r/softwarearchitecture • 1mo ago [
Advice needed for transitioning from software engineer to architecture
](https://www.reddit.com/r/softwarearchitecture/comments/1seoxmv/advice_needed_for_transitioning_from_software/) 52 upvotes · 24 comments
Can OpenClaw power a multi-agent automation marketplace model (from scratch)? r/openclaw • 1mo ago [
Can OpenClaw power a multi-agent automation marketplace model (from scratch)?
](https://www.reddit.com/r/openclaw/comments/1sguhws/can_openclaw_power_a_multiagent_automation/) 4 upvotes · 3 comments
Best way to model Super Admin in multi-tenant SaaS (PostgreSQL, composite PK issue) r/Database • 2mo ago [
Best way to model Super Admin in multi-tenant SaaS (PostgreSQL, composite PK issue)
](https://www.reddit.com/r/Database/comments/1rfw4bz/best_way_to_model_super_admin_in_multitenant_saas/) 4 upvotes · 5 comments
Should authentication be handled only at the API-gateway in microservices or should each service verify it r/softwarearchitecture • 2mo ago [
Should authentication be handled only at the API-gateway in microservices or should each service verify it
](https://www.reddit.com/r/softwarearchitecture/comments/1s0et9e/should_authentication_be_handled_only_at_the/) 43 upvotes · 21 comments
Event Driven Architecture vs API Questions r/softwarearchitecture • 8mo ago [
Event Driven Architecture vs API Questions
](https://www.reddit.com/r/softwarearchitecture/comments/1nqu2ex/event_driven_architecture_vs_api_questions/)  26 upvotes · 21 comments
Anyone actually keep initial architecture docs up to date and not abandoned after few months? Ours always rot r/softwarearchitecture • 4mo ago [
Anyone actually keep initial architecture docs up to date and not abandoned after few months? Ours always rot
](https://www.reddit.com/r/softwarearchitecture/comments/1qa83h4/anyone_actually_keep_initial_architecture_docs_up/) 40 upvotes · 32 comments
Literature about software architecture r/softwarearchitecture • 2mo ago [
Literature about software architecture
](https://www.reddit.com/r/softwarearchitecture/comments/1re95ew/literature_about_software_architecture/) 46 upvotes · 16 comments
View Post in
Français
Português (Brasil)
See more See fewer
Deutsch
Community Info Section
r/softwarearchitecture  
The Incident, a CTF-style Production Outage contest, is starting soon! Cash prize is $100. See highlighted post for more details!
Join
Software Architecture
Dive into discussions on designing, structuring, and optimizing software systems. Share insights on architectural patterns, best practices, and real-world experiences.
Show more
Public
Anyone can view, post, and comment to this community
Reddit Rules Privacy Policy User Agreement Your Privacy Choices Accessibility Reddit, Inc. © 2026. All rights reserved.
Expand Navigation
Expand Navigation
Collapse Navigation
Collapse Navigation 
0cAFcWeA7flr3chWoY9nMRg2zbn7UlzrANdN8ZnZ9_z7cxU38RqIuB294xPZIjHI9qBL1pIJ8HZrwC2DXYwAgU2KQF6vf8dAN2CdDwD_8BGoAJU1JXXxPc0NxZR6p37czKHMjfZXKIbLrdPrPAacDrHaJgUsnDlev1HQc1VdOjvUJjfnH_aebKHayoS8rwKBEUL7cAQT8Bs1sySbTCxih3X8blRq9T-LWvNBBFkZtIg0RP75nwSoq23A5DeIwH1QUnIzqKjGFdXq1rnuAycSPpe6688x026h-f8oNE8T4S5ohsJ4pbqLiRoZ79805DnGqQs0mbdlXny5FPZEpW0tgImi2HwTsqtlzKWFiITyPjEjZQQn-mtGn78LbtnlXbJP3IkbxQUh36PPGbnEGDjxw2q2F0mwTLm9bLL8mkW580GMGTD9yGf3uZ9MaG05SBEGNZsYTvLMNUXuFHZMdqKStGQ0iZ0JQ4BOzeoPLXo4mqYK_X2qoh5xLvPlQUoD9Qr8dLRjOTmtP0NRHySI8zK_VCKQ_i40Oucytes6QgqHLzfUEazD13yLL1Yz9BqH9xWe1hicpJLuGd1yDdchbdfbjlXvSH0a93CUluwLMyKCfP9YVMgvkC-3We85RQTDdqpp4YaAMPR_Qgb7jfNDE0QLMI_Faezucqpo7qIJlbhUBPJHE64SlIiCBYVgQOQtOFwMLT1VBE-ksnDX6pOzFN1kCWqRUddox4XQ9pj5A8aHeR53Q_lZQ1IN-dOwHJUPlyyn8Y_ObiIHb4Un-xmv3AK1gAbA4coEaTxN6-TzF7IG9YLg8ILRzlgTBWXfy5AuNhUpQvJ331j5PVQUwIBxl32d8pm8AC3CfE8IbFi6xu69tNSePqjYpxiNmwVJnEJddDWyFJCOt4HVsogey7ErLqdpHjZ9REUQGlyt19LuuzPyJVmr6JAMxLICv_3RezBIwnxGUhixVGNwK9YAp0lpskY9017nxdgacZUPDU7Rnv27brXVMXVG1cZzIJGiTG9RpYDq6H-KYYmPmlAOfiB38fuBuArmIZfX3jXN92gqchjNJ_zFcSo_4vfQ97vR5xfO-2izaGcUU2QYgwVMomDYnVwfn7qR32xt3edBU8fgw8lS4ZrhrUWd-Rarib08uEFWJbxMU2gKFyu5OV_py7wMbZxhqWkhDXLSzf0B5T49vh81bOtcfDaOROP5a3ojTQtVzz_B364iI2SreIRwvQ-WxUyO9mQrjRanCsr4m0Ssmf30NRRf_uDfUhxkOBqyLCGdO46bV07dfNTsPm1sVdQhhi-tKJHSlfIIhWLnLrBdopD5MQ3s7Z74Vjhe88N7RAn-yV9MYQTqPVvh_I5ZGwXl1R_3BNI-kOZtLmRU3mXT3k0X7Lk_YdTbWhqTxsm_U4Y-Yh5D2dG-Nh6-5ZL4u5OJfoVwQ-udkiHW-uJJCv4YEryXP2as3pUNUd0LlnkfZ6MeAaqV8UPRdJiznxjDb7BWVA_hRtXNnaiMRaIrPlU7kwknHSjj-CeM0kazWIVQX882jYLMncfAsSGJy1YyEM4sy5EcFprxwSHsefpiBZo8Fwg5IF6cgzA6LzQXjx5CAm6u09rI4DADv1wotwL1rzU-gS9-50AmwVoHBU4OmVnlBsMuJCNdYenr-Konsvn_4BXs4IKaGHOeM9NCEypOVojB7dYGsoyrKJkwhZPrfk4ap09ylaen_HiQKWYhALBhPxq1kQqvUpgozqEPDIg3SA-9PxIsGIpIFhDvsmVSdRr-jD34Eve6yPy0W7xOENGYylsesjhtpOgJtRt7ia7lDOM0fayEEpyg5wf622nRkrD-dI7NHKStoZZSMZgAVQOiAsksQS2RoJ-C_MFyAizGnPBjvbxdqXQ03hiq49Y-NXWotQFvTzGIrSNkiuPKyoNZg0HL9SfFWaRbjGLseZmfUTzOLFKFqhgEWqC25SKKcC2IGFteyhRBkYBv0ZzbxTV_RHfAT4B80VLYZ7C3lto94eS-v6tOjw1vtWNSkyzMMeNvPP034AAxwJFguBs4V8qmbPn-KxQPR8YQy6-iDsKP8en_pWDQvTzxvtJ3RtHbG_4jG3KWNgfFdP8bG2lIcfFlYx1tDxHAnSWRJ_-eUmIkEFj9YgwFMoWHgjsdFX-z0zCnIlRvzeCr5bZCCqYTlNyJ0
