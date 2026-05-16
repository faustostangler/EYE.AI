---
name: What happens if you violate the terms of an open source license? - Reddit
keywords: (placeholder)
metadata:
  url: https://www.reddit.com/r/opensource/comments/1ns4gr8/what_happens_if_you_violate_the_terms_of_an_open/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T23:03:23.186Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
What happens if you violate the terms of an open source license? : r/opensource
Skip to main content What happens if you violate the terms of an open source license? : r/opensource
Open menu
Open navigation 
Go to Reddit Home 
r/opensource
Sign Up
Sign up for Reddit
Log In
Log in to Reddit
Expand user menu
Open settings menu
Skip to Navigation Skip to Right Sidebar
Back
Go to opensource
r/opensource
•
8mo ago
oz1sej
Locked post
Stickied post
Archived post
Report
What happens if you violate the terms of an open source license?
Discussion
(Probably very) hypothetical - but honest! - question: If I open source some software under the condition, that anyone can use it as long as they credit me, nothing prevents others from removing my name from it and putting their own in. I'd probably never discover it, and even if I did, what could I do? I don't suppose the average open source software developer has any interest in paying a lawyer to start a court case, when you've explicitly said you didn't want to make money off it. What would be the purpose?
So if anyone can violate the terms of an open source license without any consequences (other than you can boo at them on social media) - what's the point of having licenses in the first place?
Upvote 304 Downvote 85 Go to comments Share
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
cyb3rofficial
•
8mo ago
I just slap AGPLv3 on all my works. It's incredibly defensible and flexible for several reasons, also I'm sorry for the text wall, but I will try to explain,
First, the AGPL has real teeth - it's designed to be enforceable. Unlike permissive licenses where proving damages can be tricky (since you're giving the code away anyway), AGPL violations create clear legal remedies. If someone uses your AGPL code in their proprietary service without releasing their modifications, they're in copyright violation, and you can seek injunctive relief to shut them down until they comply.
Second, the enforcement landscape is much stronger than people realize. Organizations like the Software Freedom Conservancy actively enforce copyleft licenses and have won numerous cases. Even individual developers have successfully enforced GPL/AGPL - the legal precedent is solid and courts understand these licenses now.
Third, the 'network copyleft' aspect of AGPL is brilliant for modern software. Companies can't just run your code on their servers and avoid the copyleft requirements like they could with regular GPL. If they use your AGPL code in a web service, they must release their entire codebase under AGPL too. This creates a strong incentive for compliance. The flexibility comes from dual licensing - if a company really wants to use your code proprietarily, they can approach you for a commercial license. This actually gives you monetization options you wouldn't have with permissive licenses.
You're right that enforcement requires effort, but AGPL's design makes violations costly enough that most companies either comply immediately or seek commercial licensing rather than risk it. The license essentially enforces itself through economic pressure.
To directly answer your question about 'what's the point of licenses' - the premise is actually incorrect. License violations absolutely do have real consequences beyond social media shaming. Copyright law gives you automatic legal rights the moment you create code. When someone violates your license terms, they lose their license to use your copyrighted work entirely - meaning they're now engaged in straight copyright infringement . This isn't some toothless academic concept; it's the same legal framework that protects Disney, Microsoft, and every other copyright holder.
The consequences include:
Immediate cease-and-desist orders that can shut down their entire product
Statutory damages up to $150,000 per work infringed (even if you can't prove monetary harm)
Seizure of infringing products and equipment
Attorney fees (in many cases, they pay your legal costs if you win)
You don't need deep pockets to enforce this. Organizations like Software Freedom Conservancy will enforce on your behalf for free if your project meets their criteria. There are also lawyers who take GPL cases on contingency because the law is so favorable to copyright holders. The real power of licenses isn't punishment - it's prevention. Most companies have legal teams that won't touch license violations because the risk/reward is terrible. A proper copyleft license, like for example AGPL, makes your code legally 'radioactive' to proprietary use, which forces either compliance or commercial licensing discussions. Without licenses, your code would be under full copyright protection anyway - meaning nobody could legally use it at all without your permission. Licenses don't weaken your position; they create a controlled way for others to use your work while preserving your rights.
Upvote 143 Downvote Reply Award Share
Report
Award
Share 
newz2000
•
8mo ago
You are partly correct and partly wrong on the enforcement. I am an open source attorney formerly from an ospo at a big company. I now do copyright and other such law.
If someone violates the terms of the license then they don't have a license. That means they are using unlicensed software.
You can use the courts to help enforce your rights, but the statutory damages are not available unless you registered the copyright, which people rarely do for software. You can file an injunction though. You can try to sue for other types of money damages and probably get them to settle. Hopefully they have E&O insurance.
Upvote 53 Downvote Reply Award Share
Report
Award
Share
More replies
12 more replies 
serverhorror
•
8mo ago
Open source license litigation - Wikipedia https://en.m.wikipedia.org/wiki/Open_source_license_litigation
Upvote 20 Downvote Reply Award Share
Report
Award
Share 
Huge_Leader_6605
•
8mo ago
It mostly matters with businesses. They can absolutely get sued by for example free software foundation, for violating a license.
Or by some other company who releases some project under open source license.
Upvote 15 Downvote Reply Award Share
Report
Award
Share 
oz1sej
OP
• 8mo ago
But if the business uses an open source component in their closed source code, who will ever find out?
Upvote 5 Downvote Reply Award Share
Report
Award
Share
1 more reply 
DotGroundbreaking50
•
8mo ago
Pay a lawyer and at least send cease and desist letter. You can also send DMCA noticed if they are hosting the project on github or similar.
Upvote 19 Downvote Reply Award Share
Report
Award
Share
2 more replies 
WolfOfDoorStreet
•
8mo ago
It's not just to protect individuals, but corporations that open source their code. And they will most certainly sue for infringement. Oracle has sued many companies in the past, most notably Google for claiming they copied a portion of the Java source code. Additionally, the license protects you as an author, absolving you of any damage that your code may inadvertently cause.
Upvote 4 Downvote Reply Award Share
Report
Award
Share 
cgoldberg
•
8mo ago
There are consequences of violating an open source license. If you don't want to pursue legal action yourself, groups like the FSF will help enforce compliance.
Upvote 4 Downvote Reply Award Share
Report
Award
Share 
Left_Sundae_4418
•
8mo ago
The most effective weapon against this kind of behavior is to keep updating your codebase. This will ensure that if someone is using your work uncredited, they will use an old version or in worse case knowingly violate the license multiple times by taking your code as their own again and again. Also other people might do the hard work for you. Many people check software code wherever they can and actually might spot your code being used.
Upvote 4 Downvote Reply Award Share
Report
Award
Share 
pyeri
•
8mo ago
• Edited 8mo ago
Firstly, open source contributors also rely on the "general goodness of human behavior" just like most businesses. Many shops don't have any CCTV or digital surveillance, they rely on the fact that over 99% humans aren't sadistic shop lifters but will gladly pay for what they pick from stores. Similarly, most users of a project will try to comply with a license by providing attribution, having a LICENSE file, etc.
For those who are somewhat cynical or worry about others stealing their work, you can either hire a lawyer and pursue lawsuits against violations - or if you can't afford that, join a foundation like Apache or FSF which does that on your behalf. At least Apache is known to chase other open source projects on github, etc. where they failed to include a LICENSE file or performed some other violation. They even have legal resources to back their positions (as happened in the famous Google vs Oracle lawsuit wrt Apache Harmony).
Upvote 4 Downvote Reply Award Share
Report
Award
Share
Spare-Builder-355
•
8mo ago
• Edited 8mo ago
I see 2 questions in your post.
How can I "enforce" conditions of my license e.g. they attribute my name
What is the purpose of open source licenses.
Let me start with point 2. I haven't checked all possible licenses ever but I think each and every public license I've seen starts with "use this software at your own risk" clause. I'd say this is the main purpose of attaching a license to a software your release for a public use - safeguard yourself.
Regarding point 1 - how you "ensure they mention my name" or similar license conditions? In the world of proprietary software it is nearly impossible to track uses of your opensource code.
In other words the purpose of a license is to setup a legal framework around your software.
Upvote 3 Downvote Reply Award Share
Report
Award
Share 
thatdevilyouknow
•
8mo ago
I worked for a company that Sun accused of violating the GPL for Java. They used our product for the Sun Java developer chatrooms of which I was one of the people who was admin for them. They required us to run Sun servers at our expense on our network to host the software but the whole time we were secretly running Slackware instead in an attempt to distance ourselves from their licensing agreement. If they had problems with the product they would send us 10 point response plans as if we were part of Sun. So they took the product and used it heavily themselves at no cost while the company I worked for was still allowed to charge money for it. This was all because it was made from Sun Java initially but they went under shortly after that and no longer held any claim to that application which was bringing in millions of dollars in revenue.
Things are different now and the GPL can no longer be interpreted like this as far I know but this sort of reared it's head with GCC a while back before they back pedaled hard on the whole linking thing. So if you go to the wiki article for GCC linking exception you see Sun mentioned there, hmm 🤔 why might that be? I'm explaining what it was like before 2007 obviously. I don't know every little detail of if any money changed hands this was just what I personally experienced with Sun.
So to answer the question directly what happens if you violate those terms? Your shit belongs to them is what it means if you are making money from it and they have retained the rights and associated trademarks/IP from a legal standpoint. And yes, if money like that is on the line lawyers will see dollar signs. There are public licenses that require properly attributing credit to the original creators and just that but those are the more permissive licenses not typical of the business of open source like the GPL.
Upvote 3 Downvote Reply Award Share
Report
Award
Share 
xTakk
•
8mo ago
For a company it's one thing to follow the licenses. It's easy to get a company to comply with something if there's a legit legal basis there. Lawyers aren't hugely prohibitively expensive if you just want to send a letter and have them correct their usage.
On your level though, you should look at the license for just indicating how you expect the code to be used. It's cool if you want to start a project and have people expand it and move forks forward and all of that... Or I'll just use MIT or unlicense to poop some stuff out there that id expect people to "steal" from freely.
You can't always control people at an individual level. My thoughts here are, I wrote it so my dev branch will always be better than theirs and that will filter up to better repo numbers and them going away. I figure if the situation comes up where I need to defend one, it would stand out as being worth the money to defend it.
Upvote 2 Downvote Reply Award Share
Report
Award
Share
Fear_The_Creeper
•
8mo ago 
Top 1% Poster
Let's look at a real-world example:
I foolishly bought a Nokia 2780 phone because it advertised itself as having a Linux-based OS. I figured "hey, Apple and Android based their OSs on BSD because you can't base a completely locked down closed source OS on Linux, right? RIGHT??"
https://en.wikipedia.org/wiki/KaiOS
https://wiki.bananahackers.net/en/devices/nokia/nokia-weeknd
How is this not a violation of the GPL?
Upvote 2 Downvote Reply Award Share
Report
Award
Share
dkopgerpgdolfg
•
8mo ago
I foolishly
because you can't base a completely locked down closed source OS on Linux, right? RIGHT??"
How is this not a violation of the GPL?
Yeah, this assumption is indeed foolish. They do release kernel changes with the GPL, and that's it.
Anything outside (userland, external driver blobs, bootloader, even some types of kernel modules, ...) are not in scope of the kernel license. This is true for KaiOS, Android, Debian on a Lenovo PC, and anything else too.
Upvote 4 Downvote Reply Award Share
Report
Award
Share
More replies
Fr0gm4n
•
8mo ago
• Edited 8mo ago
https://www.kaiostech.com/help-center/source-code-2/
https://github.com/kaiostech
Despite the common business scare tactic, the GPL does not "infect" everything that runs on the Linux kernel. You can still write, sell, and distribute proprietary software that is under a non-FOSS license that runs on a Linux system. Also, just because they give you the source code, they don't have to give you root access to the OS.
Upvote 2 Downvote Reply Award Share
Report
Award
Share
1 more reply
Timely-Degree7739
•
8mo ago
Then it's isn't compliant with that license anymore.
Upvote 2 Downvote Reply Award Share
Report
Award
Share 
daronhudson
•
8mo ago
You basically instantly explode into a giant blaze of fire.
Upvote 2 Downvote Reply Award Share
Report
Award
Share
3v1n0
•
8mo ago
Me and others are actually currently affected by a clear violation of a quite used library in the Linux world, but I'm still seeking for help in how to proceed.
As I'm unsure what to do given that the violator is a Chinese company and most of us are based in Europe
Upvote 2 Downvote Reply Award Share
Report
Award
Share 
maskedredstonerproz1
•
8mo ago
The FSF sometimes tends to step in, especially in the case of something like the GPL being violated
Upvote 1 Downvote Reply Award Share
Report
Award
Share
1 more reply
PurpleYoshiEgg
•
8mo ago
In addition to what other people have said, copyright violations have statutory damages in the US if you've registered the copyright under 17 U.S.C. § 412.
Tangentially, many countries (notably, not the US) also recognize moral rights of the sort that cannot be given up, which can mean attribution can't be scrubbed even if the license or any other agreement would state you'd give such rights up.
Upvote 1 Downvote Reply Award Share
Report
Award
Share
12 more replies
cdhowie
•
8mo ago
All an open source license does is say "I give you permission to use my copyrighted code as long as you follow these terms." You still retain copyright of your work.
Unless you have made another agreement with them, nothing else gives them the legal right to use your code. Therefore, it simply becomes a copyright violation in the eyes of the law, and you can pursue appropriate legal action as you would any other copyright violation.
Upvote 1 Downvote Reply Award Share
Report
Award
Share
ignorantpisswalker
•
8mo ago
If you create a bsd licensed package and one of the files is borrowed from a gplv3 library the community is going to make lots of noise. But in reality, that's it.
Unless you start selling it. Then, depending on the revenue, you will get sued.
Upvote 1 Downvote Reply Award Share
Report
Award
Share 
JVNHIM
•
8mo ago
You go to open source jail
Upvote 1 Downvote Reply Award Share
Report
Award
Share
View more comments
New to Reddit?
Create your account and connect with a world of communities.
Continue with Email
Continue with Phone Number
By continuing, you agree to our User Agreement and acknowledge that you understand the Privacy Policy.
Related Answers Section
Related Answers
Tools for software license compliance
Understanding open source software law
Most restrictive open source licenses
Top open source projects to watch in 2024
Best open source tools for developers
Why are you still open source your code? r/opensource • 17d ago [
Why are you still open source your code?
](https://www.reddit.com/r/opensource/comments/1sxfww8/why_are_you_still_open_source_your_code/) 19 comments
I'm new to open source. What open source license would you recommend? r/opensource • 9mo ago [
I'm new to open source. What open source license would you recommend?
](https://www.reddit.com/r/opensource/comments/1mm7wp1/im_new_to_open_source_what_open_source_license/) 34 upvotes · 46 comments
Why GPL violations are bad - Gary explains r/linux • 8y ago [
Why GPL violations are bad - Gary explains
](https://www.reddit.com/r/linux/comments/7wj8ci/why_gpl_violations_are_bad_gary_explains/)  youtube 78 upvotes · 12 comments
What does the Supreme Court really have to say about "traveling?" r/Sovereigncitizen • 3y ago [
What does the Supreme Court really have to say about "traveling?"
](https://www.reddit.com/r/Sovereigncitizen/comments/11f5icp/what_does_the_supreme_court_really_have_to_say/) 28 upvotes · 381 comments
Do large enterprises really avoid open source in production? r/opensource • 1y ago [
Do large enterprises really avoid open source in production?
](https://www.reddit.com/r/opensource/comments/1lkdx1u/do_large_enterprises_really_avoid_open_source_in/) 99 upvotes · 149 comments
Open source publication policies? r/ExperiencedDevs • 5mo ago [
Open source publication policies?
](https://www.reddit.com/r/ExperiencedDevs/comments/1pnm0tp/open_source_publication_policies/) 13 upvotes · 2 comments
Looking for U.S. or common-law jurisprudence on implied licensing of bundled assets r/COPYRIGHT • 4y ago [
Looking for U.S. or common-law jurisprudence on implied licensing of bundled assets
](https://www.reddit.com/r/COPYRIGHT/comments/t6jr2z/looking_for_us_or_commonlaw_jurisprudence_on/) 2 upvotes · 5 comments
What They Don't Tell You About Maintaining an Open Source Project r/opensource • 6mo ago [
What They Don't Tell You About Maintaining an Open Source Project
](https://www.reddit.com/r/opensource/comments/1p6q7mr/what_they_dont_tell_you_about_maintaining_an_open/) 84 upvotes · 14 comments
What license should I use to prevent commercialization? r/opensource • 10mo ago [
What license should I use to prevent commercialization?
](https://www.reddit.com/r/opensource/comments/1m7gpbu/what_license_should_i_use_to_prevent/) 22 upvotes · 30 comments
Reasons open source is NOT good? r/opensource • 5mo ago [
Reasons open source is NOT good?
](https://www.reddit.com/r/opensource/comments/1pu9t2u/reasons_open_source_is_not_good/) 48 upvotes · 132 comments
What do you do to make sure your opensource project doesn't end up being stolen ? r/opensource • 10mo ago [
What do you do to make sure your opensource project doesn't end up being stolen ?
](https://www.reddit.com/r/opensource/comments/1m5cvw4/what_do_you_do_to_make_sure_your_opensource/) 18 upvotes · 75 comments
How do you manage open source security vulnerabilities and license compliance? r/opensource • 6y ago [
How do you manage open source security vulnerabilities and license compliance?
](https://www.reddit.com/r/opensource/comments/im9wo9/how_do_you_manage_open_source_security/) 10 upvotes · 11 comments
what is stopping you from contributing to large open source projects? r/opensource • 7mo ago [
what is stopping you from contributing to large open source projects?
](https://www.reddit.com/r/opensource/comments/1nzqz9h/what_is_stopping_you_from_contributing_to_large/) 44 upvotes · 98 comments
Why not just fund open source projects? r/opensource • 4mo ago [
Why not just fund open source projects?
](https://www.reddit.com/r/opensource/comments/1qn8mbn/why_not_just_fund_open_source_projects/)  youtube 132 upvotes · 27 comments
How to open source license a patent? r/opensource • 4y ago [
How to open source license a patent?
](https://www.reddit.com/r/opensource/comments/vef4cj/how_to_open_source_license_a_patent/) 6 upvotes · 15 comments
French Appeal Court affirms decision that copyright claims on GPL are invalid; must be enforced via contractual dispute r/linux • 5y ago [
French Appeal Court affirms decision that copyright claims on GPL are invalid; must be enforced via contractual dispute
](https://www.reddit.com/r/linux/comments/pejmou/french_appeal_court_affirms_decision_that/)  thehftguy 820 upvotes · 200 comments
Why you should get involved in open source - a personal story r/opensource • 3mo ago [
Why you should get involved in open source - a personal story
](https://www.reddit.com/r/opensource/comments/1rbgx0p/why_you_should_get_involved_in_open_source_a/) 102 upvotes · 19 comments
I endorse open source projects and I like to share my works that way too. But here's the dilemma I'm facing. r/opensource • 6mo ago [
I endorse open source projects and I like to share my works that way too. But here's the dilemma I'm facing.
](https://www.reddit.com/r/opensource/comments/1p13hkv/i_endorse_open_source_projects_and_i_like_to/) 35 upvotes · 17 comments
Has anybody ever faced consequences for violating the GPL? r/linuxquestions • 8y ago [
Has anybody ever faced consequences for violating the GPL?
](https://www.reddit.com/r/linuxquestions/comments/7vo1n1/has_anybody_ever_faced_consequences_for_violating/) 61 upvotes · 25 comments
How to verify open source? r/opensource • 5mo ago [
How to verify open source?
](https://www.reddit.com/r/opensource/comments/1pw4xxw/how_to_verify_open_source/) 41 upvotes · 25 comments
i contributed to open source for the first time last month and the maintainers were shockingly nice r/opensource • 6d ago [
i contributed to open source for the first time last month and the maintainers were shockingly nice
](https://www.reddit.com/r/opensource/comments/1t7fx4d/i_contributed_to_open_source_for_the_first_time/) 135 upvotes · 23 comments
Does anyone actually enforce the GPL of the Linux kernel? r/linux • 6y ago [
Does anyone actually enforce the GPL of the Linux kernel?
](https://www.reddit.com/r/linux/comments/iz0h5p/does_anyone_actually_enforce_the_gpl_of_the_linux/) 818 upvotes · 244 comments
Where do you discover open-source projects? r/opensource • 4mo ago [
Where do you discover open-source projects?
](https://www.reddit.com/r/opensource/comments/1q8ni6o/where_do_you_discover_opensource_projects/) 20 upvotes · 23 comments
Contacted about licence violation r/sysadmin • 2y ago [
Contacted about licence violation
](https://www.reddit.com/r/sysadmin/comments/1bif95f/contacted_about_licence_violation/) 175 upvotes · 99 comments
This AI Tool Rips Off Open Source Software Without Violating Copyright | Malus, which is a piece of satire but also fully functional, performs a "clean room" clone of open source software, meaning users could then sell software without crediting the original developers r/technology • 23d ago [
This AI Tool Rips Off Open Source Software Without Violating Copyright | Malus, which is a piece of satire but also fully functional, performs a "clean room" clone of open source software, meaning users could then sell software without crediting the original developers
](https://www.reddit.com/r/technology/comments/1ss47dz/this_ai_tool_rips_off_open_source_software/)  404media 187 upvotes · 48 comments
View Post in
日本語
Français
हिन्दी
简体中文
Português (Brasil)
Русский
See more See fewer
Polski
Dansk
العربية
Čeština
Български
Deutsch
Italiano
Srpski
Community Info Section
r/opensource
Join
Open Source on Reddit
A subreddit for everything open source related (for this context, we go off the definition of open source here http://en.wikipedia.org/wiki/Open_source)
Show more
Public
Anyone can view, post, and comment to this community
Top Posts
Reddit reReddit: Top posts of September 27, 2025
Reddit reReddit: Top posts of September 2025
Reddit reReddit: Top posts of 2025
Reddit Rules Privacy Policy User Agreement Your Privacy Choices Accessibility Reddit, Inc. © 2026. All rights reserved.
Expand Navigation
Expand Navigation
Collapse Navigation
Collapse Navigation 
0cAFcWeA6XyGSlALgY_rQuJSl-9Qt4VXkTE2hPsr0oav2UXfbo1MNor59B57wgJ3zUU3iQtLkBWQuqN2mPHfRY0rs5Zwv605ZjBRC6y-C4mPVERJmsRV5bIbs0-j4ooevY9gkancWsIlAeY98PHpePkVo_kokWcfxb0wheYRx2yCUH_ziWOOV5HHnOgaDc2eala_6eWXM1zsPwI3tev1Cjipkf6MBevVcRsge51wjvdX1p7LxYn3myLWFx_c3vC3OwNEWHiH1jdvgoPzRezB0XfI7aMR85w1ofvnE4PmTQfKx9vB9eajeKTNFkrm2PTJ9gVKyKPLJ8mmv44Ho1vFYAU2Uisw-IrW6NIiLVJ1DzWVMqv4WIrtnmYtl9kk4KmmIj9xaEpzORGV52fawTVk-tC1iqlKJWVo9PWUsvJC1KYfxHZY6-kgu1v3tkq7UEJ96197pKDpqt43zRcl5nUv2XVzqYevJrYypEqy4W11duRN3UIPqmkoOWP05TJ5R2kKBouC7OEUgHv_Knlve2-A7GnTGo0zp65hmPQlReRUMCqHvMZq74aenfXhYb_KoaSxUUpepQb6xGYU75tppt1xc_TsE8s0sofcQ4ayNROmq_47ZBHuo8eHLdoKiZ3wSlHCW1OBFpZoLRRN3_X3BkpBbw6Rmsn6CFEi_acVx9ob2dxwziKcd6KMqP-WbbGGFPUPW-m5SgljaELrj7AXiq1bdCoiTmAmzH0i_ZSYoO1zmMIeE2QOmDYYfYywQpW-bZ1jb9UHUkg4g2NYjLvAhlC-w7YxOASjF_gvsPuXBJ30olSUQ4ehvr_YMVdznAk5F3X-UfxF4tuApYh2Cyxoxi66G57PPD_jJ3Q7XfDf2KQX0uzbp6PVxby3tuUILueO65OxUVthnkiYkK7awjF5rkG5Dtp4cVE48aVG1eVjTU14QbGLZjqT4DhUMmF_M9rW1vKLNE4btpb2fpPzWmpXojpVwVJiS9q-iy994R88Zyzx-4dMmWoj_avRaDySHTdfPm2tRRHAtyNr0diCJh8FyJpSsuXr02Kj2JVKC1Pg5h6qEGBe43rOkkCkXa35ZLxIjMlYJazSWmi1sBtpeRsqpr03q6whvib_7VWbJe0YLGa_aIeBVjvFNdbAzLZo0_zl6xL1Pma-ls3lYSSGekf2FgcmLHmSPZ5OxInJO8ekzprUb1FHATTEPLJQEiTRpssiksvutCFYBDVyb3o9LTpt7QDCrjXqN5PAh1s0J8-lvkajxOMdMsiQhsuzdnWwGL_GzLA3czuCHVgAUynn3fCBrvw5JBSCrhBg9CC1ME5yOb8n0entNscb41usAxjxFeYHzYgsNHogeEjI_sqbQMWjkQibD4an_eYrYzDrR6aq5rvVsPN1lh-MWNsIfh29yy379kwzSToMyBWNOXeM3k8Naw-UeksTE14GnQOVfhnNZvs06uSWZjqswUd9z6G3oi0vBc1GtgnJcZN-ELXF4LT_AF7HLT94JP-ADat2y6Ue_hclrqHrQ9ALx4qy40Ir_RuXTH2esqTjBj_j_0-RVQaiMDLG5S0XA41pqOx7qdLbEgnjv8_1tCl26nuXQ1G2CcQb_yuqiRUj9HuhDZo0LysqWvn4YDD--Bb4XSdHiFmQt2CUzoUU4vxN44GMxjyy511fT8TdIGvmNHa1vMtmWeiRxgtVbSe2GGFanHN2S3n1X0NyhX-TcJaYN-cQDM4JwPkLxInLHV3A8jlwvZSIN_5Ds7jU7Eu0JIHCsKUljkKSexOLbbpu2EfhmC8w6BRSxtzSP4SkELRrIc2nThsL00lKjQgVZk6Uku-x66GTDcLxVVBzq_ieboOZyyPJiwOlMMDcftp9ZQZNDYvUwwcqidvydrLT-PzjZ47-NU0C24sMg8brTMzzHGAVYYCUF2vtpXqZX0O6IU6jP5f8dhywN-i3_GRP-X1LLQtWMuQfLWu25kI9NjEZ6mbBJ8YJiErWxwDdbdc_2TmT8pyB3fFoXUfELQSNGgglugDDrH0PxHHtYOvYKAlDYUV3txjTwkZvW0Cdw3_IBe6b5k_11Yk1t4364m9hKYcGLwTR3vG_-EQayU3H8sE0vesc5Oam-9cET5Et8j017eMTq29KplVVnWk74oAWB3Wx9hHTr4qxfUqQ
