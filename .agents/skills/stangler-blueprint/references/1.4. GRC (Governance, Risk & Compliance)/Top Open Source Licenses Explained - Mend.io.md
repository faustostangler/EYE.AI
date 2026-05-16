---
name: Top Open Source Licenses Explained - Mend.io
keywords: (placeholder)
metadata:
  url: https://www.mend.io/blog/top-open-source-licenses-explained/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T23:03:23.186Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
Platform Mend AI   Secure AI powered applications  Mend AppSec   Secure your code  Mend SCA   Decrease open source risk  Mend SAST   Secure proprietary code 10x faster  Mend Renovate   Automate dependency updates Expand AppSec coverage   DAST  API security  EOL support Platform Benefits   Repo integration  Scalability  Reachability 
Solutions AI app security   Manage risks in AI models and agents  AI red teaming   Test and secure conversational AI  AI based remediation workflows   Automate remediation with AI  System prompt hardening   Prevent prompt injection and misuse  AI-BOM   AI component inventory  SBOM   Move from static to effective SBOMs  AI gen code security   Real-time AI code security  Dynamic testing   Test for risks in running applications  Compliance   Security compliance coverage  Code scanning   Find and fix known vulnerabilities  Open source security   Prevent. Prioritize. Automate.  Open source compliance   Risk management for OSS licenses  Dependency updates   Reduced risk, better code  Software supply chain security   Ensure build integrity  Container security   Container security, simplified 
Why Mend
Pricing
Company About us   Who we are  Careers   Join our team  Partners   Meet our partners  Events   Upcoming events  Newsroom   The latest Mend.io news  Contact us   Connect with us 
Resources Resource center   View our latest resources  Blog   The latest AppSec news and insights  Podcast   Insights from leading experts  Customers   View our customer case studies  Integrations   Find your integration  Languages   Find your language  Vulnerability database   Mend.io's OSS vulnerability database  Documentation   Product and feature documentation FEATURED   AI Security Governance: A Practical Framework for Security and Development Teams  The Complete Guide to Open Source & AI Licensing 2026  ROI of Automated Dependency Management with Mend Renovate Enterprise  AI Red Teaming Practical Guide 
Guides
 AI security 
Protect AI models, data, and systems
 AI red teaming 
Test for behavioral risks in conversational AI
 LLM security 
Mitigating risks and future trends
 Application security 
AppSec types, tools, and best practices
 Dependency management 
Automating dependency updates
 SCA 
Manage open source code
 SAST 
Keep source code safe
 Software bill of materials 
Improve transparency, security, and compliance
 Application security testing 
Pre-production scanning and runtime protection
 Container security 
Secure containerized applications
 See all guides 
 Schedule a DemoTable of contents
Related resources
Open Source Licenses Trends and Predictions
Top 9 GPL With The Classpath Exception Questions Answered
Top 10 Questions About the Apache License
The Top 10 Questions about the GPL License – Answered!
Top 10 Eclipse Public License Questions Answered
The SaaS Loophole in GPL Open Source Licenses
 Top Open Source Licenses Explained 
Tiffany Jennings October 9, 2025  6 min read  Share article   License Compliance Table of contents
What is an open source license?
An open-source license is a legal agreement between a software author and its users. It defines how the software can be used, modified, and redistributed. This license is what turns regular software into open source, granting developers the right to build on top of others’ work—as long as they comply with specific conditions.
Open-source licenses play a vital role in both community-driven and commercial software development. They dictate how companies can integrate open-source components into proprietary products without facing legal or compliance risks.
Today, there are over 200 open-source licenses, but in practice, most open-source projects fall under a small number of popular ones. Let’s unpack how these licenses differ and what they mean for your codebase.
Learn more about open source.
Types of software license: Copyleft and permissive
Open-source licenses generally fall into two broad categories:
Copyleft licenses
A copyleft license requires that any derivative work built from the original open-source code remains open source. If you use or modify code under one of these licenses and distribute your software, you must make your source code available under the same terms.
For example, the GNU General Public License (GPL) enforces this rule strictly, ensuring that open-source code—and everything derived from it—stays open.
However, copyleft licenses vary in strength:
Strong copyleft (e.g., GPL): Any combined or derivative work must remain open source.
Weak copyleft (e.g., LGPL, EPL): Only modified files must remain open source, while the rest of your application can use another license.
Learn more about the nuances in our guide on Open Source Copyleft Licenses.
Permissive licenses
Permissive licenses are far more flexible. They allow you to use, modify, and redistribute open-source code—even within proprietary software—without the obligation to open source your own code.
The MIT License, BSD Licenses, and Apache License are the most popular examples. They’re designed for ease of adoption, minimal legal risk, and commercial compatibility.
Open source license comparison: Main differences
Below is a visual comparison of how common open-source licenses differ in terms of freedom, reciprocity, and restrictions.
Top open source licenses explained
There’s no single “best” open-source license—only the one that fits your project’s goals and compliance needs. The Open Source Initiative (OSI) currently approves around 80 licenses, but only a handful dominate modern software development.
Here’s a breakdown of the major ones you’ll encounter:
GNU general public license (GPL)
The GPL is the most widely used strong copyleft license. Created by Richard Stallman, it ensures that software using GPL components must also be released under the GPL.
This extends even to linked libraries—meaning you generally can’t mix GPL code with code under other restrictive licenses. However, there’s a key nuance: the copyleft obligation is triggered only upon distribution.
That’s why SaaS providers can use GPL software without releasing their source code—a loophole addressed by the Affero GPL (AGPL), which considers network access a form of distribution.
Weaker variants include:
Lesser GPL (LGPL): Allows linking with proprietary code.
GPL with Classpath Exception: Clarifies use of unmodified libraries without enforcing copyleft.
The Apache license (version 2.0)
The Apache License is one of the most permissive open-source licenses. It allows modification, redistribution, and even commercial use, provided you:
Include a copy of the license and attribution,
Note any modifications made,
Avoid implying endorsement by the Apache Software Foundation.
Apache 2.0 stands out because it includes explicit patent rights, protecting developers and users alike. This balance of openness and legal clarity makes it a favorite for enterprise use.
Microsoft public license (Ms-PL)
The Ms-PL is a simple, permissive license from Microsoft. It allows free use, modification, and distribution—with a few caveats:
You cannot use contributors’ names, logos, or trademarks.
The software comes without warranties.
If distributing in source form, it must remain under the Ms-PL.
Berkeley software distribution (BSD) licenses
The BSD family includes several permissive variants:
4-clause BSD: Requires attribution in advertising (rare today).
3-clause BSD: Removes the advertising clause.
2-clause BSD (FreeBSD): Removes both advertising and non-endorsement clauses.
BSD licenses are minimalistic and highly business-friendly, allowing virtually unrestricted reuse.
Common development and distribution license (CDDL)
Created by Sun Microsystems, the CDDL is a weak copyleft license modeled after the MPL. It requires that source code files containing CDDL-licensed code remain open source, but other files in the same project can be under different licenses.
You must:
Retain copyright and attribution notices,
Identify yourself as a modifier, and
Include the license in all redistributions.
This structure enables collaborative reuse without forcing full project openness.
Eclipse public license (EPL)
The EPL is another weak copyleft license that applies per file.
If you modify EPL code and distribute it, that modified file must stay under EPL. However, your proprietary code can remain closed if kept separate.
Version 2.0 clarified this per-file rule and added an explicit patent grant. The EPL is popular in enterprise software ecosystems, such as the Eclipse IDE.
MIT license
The MIT License is one of the most popular and permissive licenses in existence. It allows almost total freedom:
Use, modify, and distribute freely,
Include the license text in copies or substantial portions,
No warranty or liability from the author.
At under 200 words, the MIT License is concise, legally sound, and perfect for proprietary integration. It accounts for nearly one-third of all open-source license usage worldwide.
Open source licensing in 2026 is complex
Most teams don’t know where their exposure lives until it’s a legal problem. This guide shows you exactly where to look.
 Get the guideKnow your open source licenses, or explain it to the judge
Nearly all modern applications rely on open-source components. Ignoring license compliance isn’t just risky—it’s reckless. The wrong license choice (or the wrong use of it) can expose your organization to legal, financial, and reputational damage.
That’s why open-source license management tools are essential. They:
Identify and track licenses in your codebase,
Ensure compliance across dependencies,
Reduce legal exposure for your organization,
Reinforce trust and security in your software supply chain.
Learn more about evolving license trends in our analysis of Open Source Licenses: Trends and Predictions and how dual licensing can offer flexibility for developers and enterprises alike.
Additional guides on open source topics
Together with our content partners, we have authored in-depth guides on several other topics that can also be useful as you explore the world of open source:
Open source licenses
Authored by Mend
Dual Licensing for Open Source Components: Yeah or Meh?
Top 9 GPL With The Classpath Exception Questions Answered
The SaaS Loophole in GPL Open Source Licenses
Open Source Licenses Trends and Predictions
Open source audit
Authored by Mend
When’s The Right Time For An Open Source Audit?
Tips And Tools For Open Source Compliance
Manage Open Source Appsec Risk
Dependency management
Authored by Mend
Maven Update Dependencies Automatically
Dependency Management: Protecting Your Code
What Is Patch Management & How To Get It Right
Apache Kafka
Authored by Instaclustr
Apache Kafka on AWS: Features, pricing, tutorial and best practices
Apache Kafka: Architecture, deployment and ecosystem [2025 guide]
Apache Kafka tutorial: Get started with Kafka in 5 simple steps
Stay up to date on open source licenses
 Read the reportAbout the author
Tiffany Jennings
Head of Content
Tiffany Jennings is Head of Content at Mend.io. She oversees editorial strategy and thought leadership across Mend.io’s digital channels, bringing complex AppSec topics to life through creative storytelling, expert insights, and helping technology find its human voice.
Related Posts
Open Source Copyleft Licenses: All You Need to Know
Open Source Licenses Trends and Predictions
Dual Licensing for Open Source Components: Yeah or Meh?
Top 9 GPL With The Classpath Exception Questions Answered
Top 10 Questions About the Apache License
The Top 10 Questions about the GPL License – Answered!
Recent resources
Best Software Composition Analysis (SCA) Tools: Top Solutions in 2026
Tiffany JenningsApr 14, 2026    Software Composition Analysis 
Learn what SCA tools do and how they help secure your open source dependencies.
 Read more What is Software Composition Analysis (SCA)?
Tiffany JenningsJul 8, 2025    Software Composition Analysis 
Learn about Software Composition Analysis (SCA) and how it helps manage open source code to reduce security risks.
 Read more The Top 10 Questions about the GPL License – Answered!
Tiffany JenningsJun 8, 2025    Open Source Licenses 
Learn about the GPL License and its compliance requirements. 
 Read more 
Mend.io is the security platform built for every risk, across application security and AI security — securing the code layer, the AI layer, and the attack surface between them. Continuous protection across the full AI application lifecycle.
Legal
Privacy Policy
© 2026 Mend.io (White Source Ltd.) All rights reserved.
