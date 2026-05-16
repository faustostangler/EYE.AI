---
name: Open Source Licenses: Which One Should You Pick? MIT, GPL, Apache, AGPL and More (2026 Guide) - DEV Community
keywords: (placeholder)
metadata:
  url: https://dev.to/juanisidoro/open-source-licenses-which-one-should-you-pick-mit-gpl-apache-agpl-and-more-2026-guide-p90
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T19:00:57.430Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
Open Source Licenses: Which One Should You Pick? MIT, GPL, Apache, AGPL and More (2026 Guide) - DEV Community
Skip to content
Powered by Algolia
Log in Create account
DEV Community
3 Add reaction 
3 Like  0 Unicorn  0 Exploding Head  0 Raised Hands  0 Fire
0 Jump to Comments 1 Save Boost
Copy link
Copied to Clipboard
Share to X Share to LinkedIn Share to Facebook Share to Mastodon
Report Abuse
Juan Isidoro García Cifuentes
Posted on Feb 27 
3    
Open Source Licenses: Which One Should You Pick? MIT, GPL, Apache, AGPL and More (2026 Guide)
# opensource # licensing # beginners # webdev
You just finished your side project. You push it to GitHub, hit "Create repository" and there it is — that dropdown you always skip:
Choose a license.
MIT, GPL, Apache, BSD... does it really matter?
Short answer: yes, a lot. Pick the wrong one and a big company can take your work and never give anything back. Pick none and technically nobody can legally use your code at all — even if it's sitting there in a public repo.
This isn't a theoretical problem. Let me give you a real example that shook the industry.
HashiCorp is a company behind some of the most widely used tools in cloud infrastructure. One of their flagship products is Terraform — a tool that thousands of companies (from startups to Fortune 500) use to manage their servers, databases, and cloud resources. Think of it as the "remote control" for your entire cloud infrastructure. It was open source for years, with a massive community building plugins, writing tutorials, and integrating it into their workflows.
In August 2023, HashiCorp changed Terraform's license from MPL (a permissive open source license) to the Business Source License (BSL) — which, as we'll see later, is not open source. Overnight, companies that had built their entire infrastructure around Terraform had to ask themselves: can we still use this the way we do?
The community's response? They forked the entire project — took a copy of the code from before the license change — and created OpenTofu, a fully open source alternative backed by the Linux Foundation. Thousands of contributors, millions of lines of code, infrastructure teams across the world scrambling to evaluate their options. All because of a license change.
That's how much this stuff matters. A single license decision can split a community, create competing projects, and force entire organizations to rethink their tech stack.
As someone who builds SaaS products and works as a freelance developer, I've learned to check licenses before adding any dependency to my stack. It's one of those things you ignore until it bites you. This guide is everything I wish someone had explained to me when I started — the most common licenses with real use cases, no legal jargon, no fluff.
Here's what we'll cover:
Key concepts you need before diving in
Quick comparison table
Each license explained with real use cases
Dual licensing explained
License compatibility rules
Common licensing mistakes
AI tools and code licensing
FAQ for solo developers
Decision tree to pick your license
Key Concepts Before Diving In
If you already know what copyleft means and why distribution matters, skip ahead to the comparison table. If not, spend 2 minutes here — everything else will make a lot more sense.
What Is a Software License?
A license is just a document that tells people what they can and can't do with your code. Think of it as the "house rules": you decide whether others can copy, modify, sell, or redistribute your work.
Without a license, nobody has permission to do anything with your code — even if it's public on GitHub. Public does not mean free to use. It just means visible.
What Does "Open Source" Actually Mean?
It means the source code is available and anyone can view, use, modify, and distribute it under certain conditions (defined by the license). It doesn't mean "free" and it doesn't mean "no rules."
For a license to be officially considered open source, it must be approved by the OSI (Open Source Initiative) — they're the ones who set the standard.
Open Source vs. Source-Available: What's the Difference?
"Source-available" is a newer term. It means you can see the code (it's transparent), but you can't do whatever you want with it. There are restrictions, usually around commercial use. The BSL (Business Source License) is a good example — we'll cover it later.
The key difference: open source lets you use the code freely. Source-available lets you look at it, but with limits on usage.
Permissive vs. Copyleft Licenses: The Big Split
Every open source license falls into one of two families. Understanding this is the single most important thing in this entire post:
🟢 Permissive licenses (MIT, Apache, BSD)
The relaxed ones. They basically say: "Do whatever you want with my code. Use it in your commercial app, modify it, sell it. Just give me credit."
Your code can end up inside closed-source proprietary software, and that's totally fine. The author gives up control over what happens with the code once it's shared.
🟠 Copyleft licenses (GPL, AGPL, LGPL)
The protective ones. They say: "You can use and modify my code, but if you distribute your work, you must share it under the same conditions."
The term copyleft started as a wordplay on "copyright." While copyright restricts copying, copyleft flips copyright on its head: instead of preventing copies, it forces you to keep things open. If you use copyleft code, your derived work must be open too.
This creates what people call a "viral" effect — the license spreads to everything it touches. If you include GPL code in your project, your entire project becomes GPL. It's not literally a virus, but the practical effect is similar.
Why would anyone choose copyleft? Because it protects the community's work. Without it, a big company could take your open source project, improve it, close it, and sell it without giving anything back. With copyleft, that can't happen.
What Does "Distribute" Mean in Software Licensing?
This concept comes up everywhere in licensing and it's not always obvious. Distributing means delivering a copy of the software to someone else. This includes:
Publishing an app on a store (App Store, Google Play)
Sending a binary or installer to a client
Uploading a package to npm, PyPI, or any public registry
Not considered distribution:
Using the software internally at your company
Running the software as a web service (SaaS) — this is where the AGPL comes in, and we'll get to that
This distinction is critical: if you use GPL code only internally and never distribute anything, you're not required to open your code.
Why Do Software Patents Matter for Licensing?
Some companies patent specific techniques or algorithms. If a license doesn't mention patents, someone could contribute code to your project and later sue you for using a technique they've patented. Licenses like Apache 2.0 include a patent grant that protects you from this.
If you're a solo developer working on small projects, this probably won't affect you. But if your code will be used by larger companies or receive external contributions, it's worth thinking about.
Quick Comparison Table
Here's the full spectrum at a glance — from most permissive to most restrictive:
MIT License
What Is the MIT License and When Should You Use It?
The world's most popular open source license. Use it, modify it, sell it, distribute it. The only requirement: keep the copyright notice.
📦 Used by: React, Node.js, Meilisearch, jQuery, VS Code
💡 Real-world scenario
You build a React component library. You want every company and developer out there to use it in their commercial projects with zero friction. The more people use it, the more contributions you get and the more your reputation grows.
You don't mind if someone puts it in a closed-source product — your goal is maximum adoption.
Pick MIT when: you want your code to spread everywhere and you don't care who makes money from it.
Apache 2.0 License
What Is the Apache 2.0 License and How Does It Differ From MIT?
Very similar to MIT but with one key difference: patent protection. If someone contributes code to your project, they automatically grant you a license to any related patents. If they later sue you over those patents, they lose their rights to the project.
📦 Used by: Kubernetes, TensorFlow, Apache Kafka, Android (AOSP)
💡 Real-world scenario
Your startup is building a machine learning framework. You know big companies will contribute code. You need the legal guarantee that they won't sue you later over patents covering the features they contributed themselves.
With MIT, that protection doesn't exist. With Apache 2.0, every contributor automatically grants you a patent license.
Pick Apache 2.0 when: you're in an enterprise environment where patents are a real risk.
BSD License (2-Clause and 3-Clause)
What Is the BSD License?
Almost identical to MIT. The 3-clause version adds one extra rule: you can't use the author's name or the project's name to promote a derivative product without permission.
📦 Used by: Nginx, FreeBSD, Flask, PostgreSQL (similar variant)
💡 Real-world scenario
You publish a high-performance networking tool. You're fine with others using or modifying it commercially. But you don't want a company to fork it and market it saying:
"Built on the work of [your name]" or "From the creator of [your project]"
...to gain credibility at your expense without your consent.
Pick BSD 3-clause when: you want MIT-level freedom but with brand protection.
GPL v3 (GNU General Public License)
What Is the GPL License and What Does Copyleft Mean in Practice?
Strong copyleft. If you distribute software that includes GPL code, your software must also be GPL and open source. That means publishing your full source code under the same terms.
Remember: distributing means handing a copy to someone (publishing an app, sending a binary, uploading a package). If you use GPL code only internally and never distribute it, you're not required to open your code.
📦 Used by: Linux kernel, WordPress, GIMP, GCC
💡 Real-world scenario
You're building a content management system. You want to make sure that if a company takes it, improves it, and distributes it, those improvements must come back to the community. Nobody can "close" your work.
WordPress works exactly like this. That's why its ecosystem is massive: every theme and plugin that gets distributed must keep the GPL license.
Pick GPL when: you want to guarantee your code and all its derivatives stay free forever.
⚠ Keep in mind
GPL is "viral" (as we explained earlier): if you include GPL code in your project, your entire project becomes GPL. This scares away many companies working with closed source. That's not a bug — it's the whole point.
AGPL v3 (Affero General Public License)
What Is the AGPL and Why Does It Matter for SaaS?
Just like GPL but with one crucial addition. The GPL has a loophole: offering software as a web service (SaaS) is not considered "distribution." So a company can take your GPL code, run it on their servers, charge customers for it, and never share a single line of their modifications.
The AGPL closes that gap. If you make the software available over a network, you must also publish the source code, including your changes.
📦 Used by: Grafana, Nextcloud, Mastodon, MongoDB (before switching to SSPL)
💡 Real-world scenario
You create a self-hosted analytics platform. Without the AGPL, Amazon could take your code, launch it as a managed service on AWS, charge money for it, and give nothing back.
With AGPL, if they offer it as SaaS, they're required to publish their modifications.
This is the anti-cloud-giant shield. MongoDB eventually moved from AGPL to the even more restrictive SSPL — the AGPL wasn't enough to hold off AWS.
Pick AGPL when: your software will be offered as a web service and you want anyone monetizing it to contribute back.
LGPL (Lesser General Public License)
What Is the LGPL and When Should You Use It for Libraries?
A softer version of GPL. It allows proprietary software to use your library (by linking to it dynamically) without becoming GPL themselves. But if someone modifies your library directly, those modifications must be open source.
The difference from full GPL: with GPL, if you use the library, your whole project becomes GPL. With LGPL, only direct modifications to the library itself must be opened — the rest of your application can stay closed.
📦 Used by: FFmpeg (partially), Qt (community edition), GNU C Library (glibc)
💡 Real-world scenario
You build a video processing library. You want every app — including closed-source commercial ones — to be able to use it. But if someone improves your compression algorithm, that specific improvement must come back to the community.
The rest of their application can stay proprietary. Only the direct changes to your library need to be shared.
Pick LGPL when: you're building a library you want everyone to use, while protecting direct improvements to it.
BSL (Business Source License)
What Is the BSL and Is It Open Source?
No, the BSL is not open source — it's "source-available" (as we discussed earlier). The code is visible and auditable, but production or commercial use is restricted for a set period (usually 3–4 years). After that period, it automatically converts to a fully open source license (typically Apache 2.0).
Remember the HashiCorp/Terraform story from the intro? This is the license they switched to — and the reason the community forked the project.
📦 Used by: MariaDB, Sentry, CockroachDB, HashiCorp (Terraform, Vault), Elastic
💡 Real-world scenario
You're launching a database as a SaaS product. You want developers to see your code, audit it, learn from it, and use it in development. But you don't want AWS to clone your product and compete against you using your own code.
BSL gives you a window of commercial exclusivity. Once the period expires, the code becomes fully open.
Pick BSL when: you want transparency and trust without handing your business model to the hyperscalers.
Dual Licensing: How Some Projects Offer Two Licenses
Some projects don't pick just one license — they offer two (or more) and let you choose. This is called dual licensing, and it's more common than you might think.
How does dual licensing work?
The project is available under a copyleft license (usually GPL or AGPL) for free. But if the copyleft terms don't work for you — say, you're building a closed-source product and can't go GPL — you can buy a commercial license that lets you use the code without copyleft obligations.
📦 Real examples:
Qt — Free under LGPL/GPL. Need to keep your code closed? Buy a commercial license from The Qt Company.
MySQL — Free under GPL. Don't want your project to be GPL? Oracle sells a commercial license.
MongoDB (before SSPL) — Used this model with AGPL + commercial option.
FFmpeg — Parts are LGPL, parts are GPL. If you need the GPL parts in a closed-source product, you need a separate agreement.
💡 When does this matter to you?
If you're using a dual-licensed library and the free license is copyleft, ask yourself: "Am I okay with my project being copyleft too?"
Yes → Use the free license. No problem.
No → You'll need to buy the commercial license. Budget for it.
As a freelancer, I've had to factor this into project estimates more than once. A "free" library isn't always free if your client needs a closed-source product.
Consider dual licensing for your own projects if: you want to keep the code open for the community but also generate revenue from companies that need proprietary terms.
License Compatibility: Can You Mix MIT and GPL?
This is where most developers mess up — and I'll be honest, I had to learn some of these the hard way while auditing dependencies in my own projects. Not all licenses play well together. Mix incompatible ones and you've got a legal problem.
The basic compatibility rules
Permissive → Copyleft = ✅ Generally OK
You can use MIT or Apache code inside a GPL project. The result will be GPL.
Copyleft → Permissive = ❌ Nope
You can't take GPL code and put it in an MIT project. Copyleft propagates upward.
GPL + AGPL = ⚠ Careful
GPL v3 and AGPL v3 are compatible with each other. GPL v2 (without the "or later" clause) is not compatible with AGPL.
Apache 2.0 + GPL v2 = ❌ Incompatible
Apache 2.0 has patent clauses that clash with GPL v2. It is compatible with GPL v3 though.
How copyleft propagation actually works
Think of it like mixing paint. If you pour a drop of red paint (copyleft) into a bucket of blue paint (permissive), the entire bucket changes. You can't take the red out.
That second scenario catches a lot of people off guard. You didn't write the GPL code, you just used it as a dependency — but the copyleft still propagates to your whole project.
💡 Real example
You're building a commercial app. You pick 15 libraries, all MIT. Then you add one small utility library that happens to be GPL. Your entire app must now be GPL — meaning you have to publish your source code. If your business model depends on keeping the code closed, that one dependency just blew it up.
I've seen this happen in freelance projects. The fix is almost always painful: find an alternative library with a permissive license, or rewrite the functionality yourself.
Tip: check the license before adding any dependency. Tools like FOSSA, license-checker (npm), or pnpm licenses can audit your project for you. Make it a habit — future you will thank you.
5 Open Source Licensing Mistakes Developers Make
1. Not adding a license to your GitHub repo
"It's on a public GitHub repo, so it's open source."
Wrong. Without an explicit license, nobody has legal permission to use, copy, or modify your code. Public ≠ free to use. I've reviewed GitHub repos that had hundreds of stars but no license file — technically, none of those stargazers could legally use the code in their projects.
2. Using GPL code in a closed-source product
If you distribute software that includes a GPL dependency, your entire project must be GPL. This isn't hypothetical — it has real consequences. In 2008, Cisco had to release the source code for their Linksys router firmware after the Free Software Foundation found they were using GPL-licensed code (from the Linux kernel and other projects) without complying with the license terms. They settled the case and had to make the code available. A multi-billion dollar company, caught by a license they didn't take seriously.
3. Confusing source-available with open source
BSL, SSPL, and similar licenses are not open source according to the OSI. You can see the code, but you can't do whatever you want with it. If your README says "open source" and your license is BSL, that's misleading. This distinction matters — especially if your users or contributors care about open source principles.
4. Ignoring transitive dependencies and their licenses
Your project is MIT. But you use a library that depends on another library that's GPL. That chain of dependencies can change the rules without you even noticing. This is why automated license auditing tools aren't optional — they're essential. One npm install can pull in hundreds of transitive dependencies, each with its own license.
5. Assuming "non-commercial" means open source
Creative Commons licenses with an NC (Non-Commercial) clause are not open source. They're designed for content (text, images, music), not software. If you see a project on GitHub with a CC BY-NC license, you cannot use it in any commercial context — and it's not considered open source by the OSI definition.
AI Tools, GitHub Copilot, Claude Code, and Open Source Licenses
This deserves its own section because it's reshaping how we think about code ownership. If you use GitHub Copilot, Claude Code, ChatGPT, Cursor, or any other AI-powered coding tool, you need to understand what's happening under the hood.
Who owns AI-generated code?
This is genuinely uncharted territory. Current copyright law in most countries requires a human author for something to be copyrightable. If an AI generates a block of code, there's no clear human author — which means it might not be copyrightable at all.
What does that mean in practice? It's still being debated. Courts in different countries are reaching different conclusions. The safest approach for now: treat AI-generated code as if you wrote it yourself, and take full responsibility for it.
The training data problem
Here's where it gets tricky. Tools like GitHub Copilot were trained on publicly available code — including code under GPL, AGPL, MIT, and every other license. When Copilot suggests a code snippet, it might be reproducing (or closely paraphrasing) code from a GPL-licensed project.
If you accept that suggestion and put it in your closed-source app, are you violating the GPL? Nobody knows for certain yet. There are active lawsuits on exactly this question. In 2022, a class-action lawsuit was filed against GitHub, Microsoft, and OpenAI arguing that Copilot violates open source licenses by reproducing licensed code without attribution or license compliance.
What about AI coding agents like Claude Code?
AI coding agents (Claude Code, Copilot Workspace, Cursor Agent, etc.) can write entire files, modules, or even full applications. The license question gets more complex here because:
The tool's license — Claude Code itself is licensed under Apache 2.0. This means the tool is open source, but it doesn't say anything about the code it generates for you.
The generated code — Code that these tools write for you is generally considered yours. Anthropic's terms (and similar terms from other providers) typically grant you ownership of the output. But "ownership" doesn't resolve the question of whether the generated code might accidentally reproduce GPL-licensed patterns from the training data.
Your responsibility — Regardless of how the code was generated, you are responsible for the licenses in your project. If an AI tool writes code that looks suspiciously like a well-known open source library, you should verify the original license and comply with it.
Practical advice for developers using AI coding tools
Don't blindly accept large code blocks from AI tools without reviewing them. If a suggestion looks like it could be copied from a specific project, check.
Run license auditing tools on your project regularly — they won't catch AI-reproduced code directly, but they'll catch any dependencies you add.
Be especially careful with unique or distinctive code patterns. Generic patterns (a for loop, a REST endpoint) are fine. But if the AI outputs a complex algorithm that feels very specific, it might be reproducing someone's copyrighted work.
Check the terms of service of your AI tool. Most providers (Anthropic, OpenAI, GitHub) include clauses about code ownership and liability. Know what you're agreeing to.
When in doubt, rewrite. If you're unsure whether a generated block might have license implications, rewrite it in your own style. It's safer and you'll understand the code better anyway.
This whole area will keep evolving as courts rule on pending cases and as AI tools mature. Stay informed — the rules might be very different a year from now.
FAQ: Open Source Licensing for Solo Developers and Small Teams
If you work alone, build your own apps, and rely on third-party libraries and services, this section is for you. These are the real questions that come up day to day — answered without the legal jargon.
Can I use React (MIT) in my closed-source commercial app?
Yes, completely. MIT lets you use, modify, and distribute the code in commercial and closed-source projects. You just need to keep the copyright notice somewhere (usually a LICENSES file or an "about" section in your app). You don't need to open your code or pay anyone.
If I install a GPL library via npm, does my whole project become GPL?
It depends on whether you distribute your project. If your app is a SaaS running on a server and you never deliver the code to anyone, you're technically not "distributing" — so the GPL doesn't force you to open your code. But heads up: if it were AGPL instead, you would have to.
If you do distribute your app (upload to a store, package as a binary, ship to clients), then yes — your project becomes GPL.
Practical advice: if your project is closed-source, avoid GPL dependencies and look for MIT or Apache alternatives. In my experience, there's almost always a permissively licensed alternative for whatever you need.
Can I use code from Stack Overflow in my project?
Technically, you should give credit. All content on Stack Overflow is published under CC BY-SA 4.0 (Creative Commons Attribution-ShareAlike). If you copy a code block, you should attribute it. For small snippets (a few lines), the real-world risk is minimal, but for substantial blocks, good practice is to credit the source.
Can I change my project's license from MIT to GPL?
Yes, with caveats. If you're the sole author, you can change the license whenever you want. Older versions you published under MIT stay MIT (anyone who already downloaded them keeps those rights), but new versions can be GPL.
If you have external contributors, you need consent from every single one of them to change the license — unless you set up a CLA (Contributor License Agreement) upfront that grants you those rights. That's why many large projects require a CLA before accepting contributions. It's also why the HashiCorp situation was possible — they owned the copyright, so they could change the license unilaterally.
Do Firebase, Supabase, Stripe, or AWS SDKs impose license obligations?
Client SDKs and libraries from these services are usually permissively licensed (MIT or Apache 2.0), so you can use them freely in closed-source projects. But always verify: go to the SDK's GitHub repo and check the LICENSE file. Don't assume the license based on the service name.
The Terms of Service (ToS) of the service itself are a separate thing — they define how you can use the platform, not the SDK code. I make it a habit to check both when integrating any third-party service into a project.
Can I charge money for software that uses open source libraries?
Absolutely. "Open source" does not mean "free of charge." You can charge for your software even if it uses open source libraries. What matters is respecting each license's conditions:
MIT / Apache / BSD libraries: Charge freely. Just give credit.
LGPL libraries: You can charge, but if you modify the library itself, those modifications must be open.
GPL libraries: If you distribute your software, the whole project must be GPL — meaning your code must be accessible. You can still charge, but anyone who gets your software has the right to see and redistribute the source.
Can I change the license if I fork an open source project?
Depends on the original license:
MIT / BSD / Apache: Yes. You can fork and relicense (even as closed-source), as long as you keep the original copyright notices.
GPL / AGPL: No. Your fork must keep the same GPL/AGPL license. That's the entire point of copyleft — and that's exactly what happened with OpenTofu. They could fork Terraform because the code was still under MPL at the time, but they couldn't have forked it if the code had always been BSL.
LGPL: Direct modifications to the library must stay LGPL, but the project using it can be closed.
Which open source license matters when building a SaaS?
This is the million-dollar question, and as someone who builds SaaS products, it's the first thing I check before picking any open source tool as a base. It depends on the project's license:
MIT / Apache / BSD: Full freedom. Run it as SaaS, modify it, keep everything closed.
GPL: As long as it's purely SaaS and you don't distribute the code, you're technically not required to open it. But this is a gray area that generates a lot of debate.
AGPL: You must publish your source code, including any modifications. This license was specifically designed for this scenario.
BSL: Check the specific terms. Usually you can't use it in commercial production during the restriction period without a separate commercial license.
Do open source licenses apply if I don't distribute my app?
Barely. If the software is for personal or internal use and you don't distribute it or offer it as a service, most open source licenses don't impose obligations beyond keeping copyright notices. Even the GPL won't force you to publish code if you never distribute the software.
The exception: if you run a network-accessible service (a website, an API, a backend) and use AGPL code, you must publish the source even though you're not "distributing" anything in the traditional sense.
Who is responsible for licenses in AI-generated code (Copilot, Claude Code, Cursor)?
This is the question everyone's asking right now. Short answer: you're responsible. The code the AI generates is considered yours (check your tool's ToS to confirm), but if that code happens to reproduce patterns from a GPL-licensed project in the training data, you could theoretically be on the hook.
Practical advice: use AI tools freely, but review the output. If something looks like it was lifted from a specific library, check the source. And always run your usual license auditing tools on the final project — AI-generated code isn't exempt from license compliance.
Which Open Source License Should You Pick? Decision Tree
Useful Resources
choosealicense.com — GitHub's interactive guide for picking a license
tl;drLegal — License summaries in human-readable language
FOSSA — Automated license auditing for your dependencies
OSI Approved Licenses — The official list of approved open source licenses
OpenTofu — The Terraform fork born from a license change (a cautionary tale)
Wrapping Up
Remember that Terraform story from the beginning? HashiCorp built an incredible tool, grew a massive community, and then changed the license. The result: a split community, a competing fork, and years of trust gone in a single announcement.
Licenses aren't an afterthought. They're a promise to your users and your community. They define the relationship between your code and everyone who touches it.
Whether you're pushing your first repo or maintaining a project with thousands of users, take 5 minutes to understand the license you're choosing. It's one of the few decisions in software that's genuinely hard to undo.
What license do you use in your projects and why? Have you ever run into a licensing issue that caught you off guard? I'd love to hear your stories in the comments. 👇
If you found this useful, hit ❤ and share it with someone about to push their first repo without a license.
 The DEV Team
Promoted
What's a billboard?
Manage preferences
Report billboard
Building Capabilities for a Multi-Agent System with Google ADK, MCP, and Cloud Run
My team's mission is to accelerate the developer journey from writing code to running secure AI workloads on Google Cloud. To help developers succeed, we focus on identifying their most pressing questions and building demos that provide straightforward, easy-to-implement solutions.
Read more →
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
Multimodal RAG with the Gemini API File Search Tool: A Developer Guide 🗺
The File Search tool in the Gemini API now supports multimodal retrieval by adding support for Gemini Embedding 2. This update allows images, such as charts, product photos, and diagrams, to be natively indexed and searched in the same store as your text-based documents.
Read more →
Juan Isidoro García Cifuentes
Follow
Full-stack dev building MAKO (AI-agent readable web, -93% tokens) & CTY (e-commerce sync, Event Sourcing). Node.js, TypeScript, Clean Architecture.
Location Cadiz, Spain
Education Self-taught
Work Full-stack developer & open source builder
Joined Feb 18, 2026
More from Juan Isidoro García Cifuentes
Hexagonal Architecture in Plain JavaScript: Why I Use Objects as Interfaces (And Validate Them at Startup) # architecture # node # webdev # javascript
How I Ended Up Doing CQRS in a Node.js Monolith (Without Planning It) # node # javascript # architecture # webdev
AI agents are wasting 90% of tokens on your navbar — I built a protocol to fix it # ai # opensource # webdev # llm
 MongoDB
Promoted
What's a billboard?
Manage preferences
Report billboard
3 reasons why developers scale faster on MongoDB Atlas.
A flexible schema, integrated search, and automated global distribution so you can innovate and innovate with speed and agility. Build gen AI apps that run anywhere and scale everywhere.
Start Free
👋 Kindness is contagious
What's a billboard?
Manage preferences
Report billboard
Sign in to DEV to enjoy its full potential.
Unlock a customized interface with dark mode, personal reading preferences, and more.
Okay
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
