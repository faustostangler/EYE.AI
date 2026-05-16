---
name: How do you account for dependency risk in modern software architecture? - Reddit
keywords: (placeholder)
metadata:
  url: https://www.reddit.com/r/softwarearchitecture/comments/1sluj1n/how_do_you_account_for_dependency_risk_in_modern/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T19:00:57.430Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
How do you account for dependency risk in modern software architecture? : r/softwarearchitecture
Skip to main content How do you account for dependency risk in modern software architecture? : r/softwarearchitecture
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
1mo ago
MDiffenbakh
Locked post
Stickied post
Archived post
Report
How do you account for dependency risk in modern software architecture?
Discussion/Advice
One thing I've been thinking about recently is how much of modern system design relies on external dependencies that sit outside the core architecture we define.
In most systems today, very little is truly self-contained. We rely on shared libraries, frameworks, and external modules to handle everything from security to data handling and integration. This makes development faster and systems more modular, but it also introduces a layer of hidden complexity that's easy to underestimate.
At an architectural level, each dependency might look stable and well-defined. But when you look at the full dependency graph, the real system behavior becomes harder to reason about - especially when you include transitive dependencies and updates from external sources.
We recently explored this idea by mapping out a full dependency tree for a project instead of only focusing on first-party components.
As part of that process, we used a broad scanning approach (including guardix) to get visibility into both direct and indirect dependencies. One of the findings pointed to an issue in a third-party library we had integrated earlier. It wasn't visible from the main system design itself, but after manual review, the issue turned out to be valid.
It raised a broader architectural question for me: where do you actually draw the boundary of responsibility when so much of the system is composed of external components?
Upvote 8 Downvote 11 Go to comments Share
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
UnreasonableEconomy
•
1mo ago
where do you actually draw the boundary of responsibility when so much of the system is composed of external components?
This is ultimately a non-functional requirement that can be tracked and kept visible. It's a form of technical debt , and it depends on your or your customer's attitude to security. What is or isn't reasonable depends heavily on context.
Would I sign off on someone importing 'isNumber'? unlikely. Rx? Right now, improbable. Would I have allowed axios two years ago? Depends on the situation and other cross cutting concerns.
At the end of the day it's just another build or buy decision.
Upvote 5 Downvote Reply Award Share
Report
Award
Share
enterprisedatalead
•
1mo ago
This is one of those risks that tends to stay invisible until something breaks or becomes a security issue.
In practice, I've seen teams handle this at a few different levels rather than relying on a single control. At the architecture level, reducing unnecessary dependencies and being intentional about what gets introduced makes a big difference. Every dependency is effectively a piece of external risk you're accepting.
From an operational side, things like dependency scanning, version pinning, and having a clear upgrade strategy help manage the day to day risk. But what often gets overlooked is ownership. If no one is explicitly responsible for tracking and reviewing dependencies, they tend to drift over time.
Another useful approach is thinking in terms of blast radius. Even if a dependency fails or becomes compromised, how much of your system does it actually impact? Designing boundaries and isolation can limit the damage significantly.
Curious how others are balancing speed vs control here, are you leaning more on automation tools, or architectural constraints to manage dependency risk?
Upvote 4 Downvote Reply Award Share
Report
Award
Share 
nitkonigdje
•
1mo ago
• Edited 1mo ago
If you think about software architecture as common patterns of design to achive functional goal, your architecture is than x86 running hypervisor running linux running libc running kubernetes running linux running jvm running spring with dependencies running few customized lines of code.
Why then you care so much about externalizing lines od code, when 99,95% of instructions in stack trace in any given time aren't writen in any shape or form by you? Your app is literally just tip of extremely deep environment and nothing in it is made by you.
Unless you have specific need, stick to good dependecy management system and don't overthink it. Just make rational choices.
And even disasters like log4j exploit, meltdown and spectre etc. were net gain.
Upvote 2 Downvote Reply Award Share
Report
Award
Share 
shufflepoint
•
1mo ago
Have as few dependencies as possible and stick with tried and true.
Upvote 1 Downvote Reply Award Share
Report
Award
Share
sfboots
•
1mo ago
We handle as part of upgrading dependencies once per year. All versions are pinned during the year
But you can still have issue come up. We are in react 18 and bootstrap 3 which is not compatible with react 19. 200 screens to be updated and reviewed so we can upgrade bootstrap 5 and then react. And one major library has major api changes for the R19 version. So it wi be a big effort
Upvote 1 Downvote Reply Award Share
Report
Award
Share 
f0CUS
•
28d ago
The same basic concept as always. You abstract it away.
If you deem it a risk to your application, then you make a abstraction and use whatever it is through that.
It doesn't matter if it is a library, or if it is an other system. The technique you use might be different, but the concept remains the same.
Edit: wait, I got the question wrong. I'm gonna leave this as I still think it is useful advice :)
Upvote 1 Downvote Reply Award Share
Report
Award
Share
thejuniormintt
•
28d ago
This is exactly why most teams treat dependencies as part of the attack surface, not just “external tools.” In practice you can't own everything, so the boundary of responsibility usually becomes: you own selection, version pinning, monitoring, and rapid replacement—not the upstream code itself.
Upvote 1 Downvote Reply Award Share
Report
Award
Share
kvorythix
•
28d ago
transitive dependencies kill you way more than your direct ones - lock versions and keep auditing, that's where the risk actually is
Upvote 1 Downvote Reply Award Share
Report
Award
Share
TomOwens
•
28d ago
Control over third-party dependencies is something that is often missing:
An informed decision to "buy" (including obtaining FOSS) instead of building capabilities. Lightweight decision records can help capture the outcome and rationale.
After a decision to buy, a review of the product and the provider should be conducted. In my experience, organizations have controls for managing vendors, but nothing similar for FOSS products. Understanding things like contributor guidelines and policies, release cadence, community support, responsiveness to security findings (including in downstream dependencies), etc., can help determine the risk with a particular component.
To help reduce supply chain risks, mirror approved third-party components in an internal repository and pull from there. Based on risk level of the component, there may be different levels or types of review before adding a new version of a component to the repository.
Using a source composition analysis tool can help detect embedded code and manage dependency files. Some of these tools will flag out-of-date and/or vulnerable dependencies, as well as cases where the dependency has not been updated recently and may be unsupported. This can help flag and prioritize work to update or change dependencies.
Taking steps to isolate dev/test dependencies from production dependencies can reduce the system's footprint when deployed.
Regular vulnerability scanning of the application, including human-driven penetration testing, can help find vulnerabilities. For high-risk open-source components, also consider performing static and dynamic testing of the package directly. Issues can be raised directly with the provider.
Upvote 1 Downvote Reply Award Share
Report
Award
Share
Chunky_cold_mandala
•
28d ago
https://github.com/squid-protocol/gitgalaxy/blob/main/gitgalaxy/tools/supply_chain_firewall.py for direct external import monitoring.
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
Tips for dependency vulnerability scanning
Understanding dependencies in programming
Open source dependency security strategies
Best practices for microservices architecture
Common pitfalls in software design
More posts you may like
Why is software architecture so influenced by money? r/softwarearchitecture • 14d ago [
Why is software architecture so influenced by money?
](https://www.reddit.com/r/softwarearchitecture/comments/1syuw9y/why_is_software_architecture_so_influenced_by/) 117 upvotes · 91 comments
How do you become a software architect without already having broad experience? r/softwarearchitecture • 19d ago [
How do you become a software architect without already having broad experience?
](https://www.reddit.com/r/softwarearchitecture/comments/1sv30ag/how_do_you_become_a_software_architect_without/) 70 upvotes · 70 comments
How do you approach correlating data from different sources in a security tool? r/webdev • 1mo ago [
How do you approach correlating data from different sources in a security tool?
](https://www.reddit.com/r/webdev/comments/1sec7uz/how_do_you_approach_correlating_data_from/) 3 upvotes · 5 comments
What is most important in software architecture? r/softwarearchitecture • 1mo ago [
What is most important in software architecture?
](https://www.reddit.com/r/softwarearchitecture/comments/1schn2g/what_is_most_important_in_software_architecture/) 86 upvotes · 61 comments
Literature about software architecture r/softwarearchitecture • 3mo ago [
Literature about software architecture
](https://www.reddit.com/r/softwarearchitecture/comments/1re95ew/literature_about_software_architecture/) 46 upvotes · 16 comments
How do you structure UI event handling in Unity when projects grow in size? r/Unity3D • 4mo ago [
How do you structure UI event handling in Unity when projects grow in size?
](https://www.reddit.com/r/Unity3D/comments/1qidway/how_do_you_structure_ui_event_handling_in_unity/)  1 upvote · 3 comments
How do you keep software architecture documentation in sync with reality? r/softwarearchitecture • 3mo ago [
How do you keep software architecture documentation in sync with reality?
](https://www.reddit.com/r/softwarearchitecture/comments/1r124hz/how_do_you_keep_software_architecture/) 52 upvotes · 29 comments
How do you effectively manage technical debt in ongoing web development projects? r/webdev • 4mo ago [
How do you effectively manage technical debt in ongoing web development projects?
](https://www.reddit.com/r/webdev/comments/1q9fri9/how_do_you_effectively_manage_technical_debt_in/) 2 upvotes · 14 comments
System arch r/softwarearchitecture • 9d ago [
System arch
](https://www.reddit.com/r/softwarearchitecture/comments/1t3gdde/system_arch/) 26 upvotes · 15 comments
What types of software still feel brutally hard to build and even impossible to build well? r/softwarearchitecture • 1mo ago [
What types of software still feel brutally hard to build and even impossible to build well?
](https://www.reddit.com/r/softwarearchitecture/comments/1shg00x/what_types_of_software_still_feel_brutally_hard/) 155 upvotes · 110 comments
Do people really not care about code, system design, specs, etc anymore? r/softwarearchitecture • 6mo ago [
Do people really not care about code, system design, specs, etc anymore?
](https://www.reddit.com/r/softwarearchitecture/comments/1ougyjf/do_people_really_not_care_about_code_system/) 116 upvotes · 86 comments
falling for distributed systems r/softwarearchitecture • 3mo ago [
falling for distributed systems
](https://www.reddit.com/r/softwarearchitecture/comments/1r9z650/falling_for_distributed_systems/) 4 upvotes · 15 comments
Methodology from requirements to software architecture r/softwarearchitecture • 6mo ago [
Methodology from requirements to software architecture
](https://www.reddit.com/r/softwarearchitecture/comments/1ox815b/methodology_from_requirements_to_software/) 28 upvotes · 8 comments
How do you prevent complexity from growing in a system over time? r/softwarearchitecture • 1mo ago [
How do you prevent complexity from growing in a system over time?
](https://www.reddit.com/r/softwarearchitecture/comments/1slioz8/how_do_you_prevent_complexity_from_growing_in_a/) 32 upvotes · 39 comments
Software Architecture Diagram r/softwarearchitecture • 2mo ago [
Software Architecture Diagram
](https://www.reddit.com/r/softwarearchitecture/comments/1s0cmno/software_architecture_diagram/) 102 upvotes · 58 comments
Senior Developer going for first Software Architecture role r/softwarearchitecture • 8mo ago [
Senior Developer going for first Software Architecture role
](https://www.reddit.com/r/softwarearchitecture/comments/1nk1sjq/senior_developer_going_for_first_software/) 75 upvotes · 29 comments
What are the biggest problems when searching for and implementing components? r/diyelectronics • 4mo ago [
What are the biggest problems when searching for and implementing components?
](https://www.reddit.com/r/diyelectronics/comments/1qjcp7n/what_are_the_biggest_problems_when_searching_for/) 3 upvotes · 4 comments
HELP with software architecture r/learnprogramming • 22d ago [
HELP with software architecture
](https://www.reddit.com/r/learnprogramming/comments/1srnnxj/help_with_software_architecture/) 5 upvotes · 9 comments
What math actually helped you reason about system design? r/softwarearchitecture • 4mo ago [
What math actually helped you reason about system design?
](https://www.reddit.com/r/softwarearchitecture/comments/1qif3i2/what_math_actually_helped_you_reason_about_system/) 41 upvotes · 22 comments
How do you work with AI as a long-term architect (docs + decisions + staying up-to-date)? r/softwarearchitecture • 5mo ago [
How do you work with AI as a long-term architect (docs + decisions + staying up-to-date)?
](https://www.reddit.com/r/softwarearchitecture/comments/1pyimcw/how_do_you_work_with_ai_as_a_longterm_architect/) 32 upvotes · 10 comments
What about dedicated database engineers? r/softwarearchitecture • 7mo ago [
What about dedicated database engineers?
](https://www.reddit.com/r/softwarearchitecture/comments/1oc3cp4/what_about_dedicated_database_engineers/) 35 upvotes · 38 comments
Junior dev trying to learn system design — need real resources, not AI answers r/softwarearchitecture • 2mo ago [
Junior dev trying to learn system design — need real resources, not AI answers
](https://www.reddit.com/r/softwarearchitecture/comments/1s0g81o/junior_dev_trying_to_learn_system_design_need/) 49 upvotes · 22 comments
Best practices for System Design r/softwarearchitecture • 6mo ago [
Best practices for System Design
](https://www.reddit.com/r/softwarearchitecture/comments/1p49rkp/best_practices_for_system_design/) 65 upvotes · 23 comments
[AskJS] In production JavaScript apps, how do you decide when abstraction becomes overengineering? r/javascript • 3mo ago [
[AskJS] In production JavaScript apps, how do you decide when abstraction becomes overengineering?
](https://www.reddit.com/r/javascript/comments/1qrv2u1/askjs_in_production_javascript_apps_how_do_you/) 7 upvotes · 23 comments
Why do some tech lead/software architects tend to make architecture more complicated while the development team is given tight deadlines? r/softwarearchitecture • 1y ago [
Why do some tech lead/software architects tend to make architecture more complicated while the development team is given tight deadlines?
](https://www.reddit.com/r/softwarearchitecture/comments/1kqd1tf/why_do_some_tech_leadsoftware_architects_tend_to/) 163 upvotes · 131 comments
View Post in
Français
Português (Brasil)
See more See fewer
Español (Latinoamérica)
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
0cAFcWeA5buAI4cxvvQjdkz-2bUTW_BUwFmVEBB9uXOIaaYHNEamLSjoWMgiO9VSzJ0JyWuzcpDGAUT7qmYbJXwxF06BSmSqMro5sqKa58kZqcjwkTTr-CpQPvF6Brye4o8OFdxb7vaQNDoO4kAUbmhzd60kVP3-wMKtbdegvGFElVy28jmYF4l44MogyrufEChNwYJIyZbM3J9Udl1HCVV8vE_EmLkmlTRalC6R99Zdv8Qi_V8_3o2UbF48tSigdZbmFP0AcDkqneeZK95omGpxJ7ClV9Jv16rZCNffrUPPqSmtkZiUp1MEPlwFjvibnbFWxeuCaAZNMotLcRnXgnn2iAi9gC_frBI3y5U59tYUyBCakNsm3ALAXpGe1bnKULnt1nov8cF3mc5eJkXccLgYw4m5eb-1J0hLXAJIaHhqXzgl3VxlBBgaeHsAKRoHlbMURUBywI33AUtukNeiqN2mPJoGoNjVNnA3tihEhPG-pPivmt1StGSsfwOrrK9VYk36dZ1Q2Bf8ZCbe06FNu_i3bbRhgtAN376VfBsl8Z6hTbf6k0jS9Ztrpq-M9apnGjZpt5hlRRjOdn3No0ZS4DLsGRoq_Msjj6m9F8McDBY943E-mkIkihuq3BRWA1MmJ4t5Lb42unGj71DzP3ld6RnRrtIoQ-BkGg6VPgTGEc2rpp2nqcEOd4ilG5gfk4uQIf57S8-0hNByLIhfYmk9huMHuZq1rkU0FMDRW2v2x-iiV3QjoUmYBPngcbl6qMGVjI7yTEY_4OUthwexGMC22tPPjj5lLY3YTdFhx5sESAlsUOCiWqhdcgNWh4jrx_CGCGLVKjOb-_xBsIqa2U_oaHD-xkCX5qVamfiOk7WxK0PgVjVI6ccVBaBD1sQTHZ5xa2YY0W-7hEqrnSIGHdGQq0_Ht1K9zsXqQ9_JMmpWFry6DohPuoN2jx9bh3YHecWcfTdDopvWpQPYa6WTbVp-iuNnDYmlGEgZ9ux59dLPvkC-AS0UeQJBeEorRzQ6UE2VEqjzD9fhsNepTHhHp2QLRWo-SKFZtteGOMUrKE_RXhQRSDPLTOJx5CktsEvMJBJPZqHs6KlCkx84LzPkCzss7l7fJKudpEOGG7HSbgx2xdmruK-eHgcO4yZmUPIwi8VmmKMA71NdvAtdkvaEqcAngs8SDJf0yf-VCM-LIYEL-ChV5immryCEFOwgrBPr4IQoTx_i8s9G3ID9vFMt5ppzcRPgTDpzYC7rfchekHV81kFkI0WSBvUKBxsGayQWYJG3LFMBUX0-hAXXDVuCaZ3cj3aN1YcHVzsueDw0uIZCoyugCJG8PJYbVXvZrcxvwhmOXBNk-T9kg7AOcbGjSxdAq1Z1LR4O7xZ7AUUDSw1XfEQhq5AI2rn2d2nf3Jr-2-65Qo8PAXRG_ZvhVpJ9NAIxjww2d_YI5gNPuMLU9umaCUEShkhUhnog9Kd5ta4nUAc49cs5jpB_y3tUc_5df5lzKoSGV4RXu56B5cLLGcW09Mtj3Xk1qHhmY97iXBLIo99DlhJZkqywJBPnX9lE_9WlMiHKRWmFmPSwG3w6266wCFKiLiINm5GewJat95u4LeAy9QS9uMdhs1DIRul_uQJMgJMva2KKBL512C8ApetluTG1v7wEo4dtpKzQ_zZwfmn36TNbDsGcoJh4NafqjuhXjBJsJYbdzsiJ_vUNf5DycrYnE4Fnq6xJZ2Qt4oZIMzLS0PAoqvbivc-kl8RnXCCvwYJ2LPKDyaZxXCOlyFxA0I8wTjoBDSru7wORra7aPEuUrSE6R92bKCB8Wr8Ebmkds2X6xRtbXfRHmXZ_6CI6y77UBd6S-IyvgAMoxHUjykerDa0otDu45KARYjagP2bTTmnxbaRWq-04LfwNM111bFBGiz8D4-98XcRlW2glaH6yaHEOMHksbIIxNKl-L9urixN5ApTXpkeQOGncNgFYSxLPD-E5l2qFyDtYoyPHur7Yf68uKQhBSCHhoIF2PRrvB-f-V5-l-6taDtyfyFevmCuz9_WfuqQ6cKMYeV_jYEFKxisQdfFf1vZq6zs7nbkdvA7QO0jLKjpVjJ07wchsdENTzBN6aXKohf2rxP1oTPzQs9kwqFk-eAzOC9vwxj-WlwcAlSx9oPaYY0u9wpmYz89FEtRNOwsw8WEdY
