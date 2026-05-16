---
name: Open Source Licenses: Types and Comparison - Snyk
keywords: (placeholder)
metadata:
  url: https://snyk.io/articles/open-source-licenses/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T19:00:57.430Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
Open Source Licenses: Types and Comparison | Snyk
You need to enable JavaScript to run this app.
Skip to main content 
Platform Platform
Snyk AI Security Platform Modern security in a single platform
Snyk AI Workflows AI-driven workflows to secure applications
DeepCode AI Purpose-built security AI
Integrations SDLC-spanning security
Snyk Learn Developer security education
Pricing Products
Snyk Code Secure your code as it's written
Snyk Open Source Avoid vulnerable dependencies
Snyk Container Keep your base images secure
Snyk IaC Fix IaC misconfigurations in-code
Snyk API & Web (DAST) Find and test APIs and web apps
Snyk Studio Fix and secure AI-generated code Solutions
Secure AI-Generated Code AI writes, Snyk secures
Application Security Build secure, stay secure
Software Supply Chain Security Mitigate supply chain risk
Zero-Day Vulnerabilities Fix the first day with Snyk
Security Intelligence Comprehensive vulnerability data
Code Checker Write better code for free
Risk-Based Prioritization Fix what matters most Discover, monitor, and secure AI agents Explore Evo by Snyk
Resources Our resources
Resource Library Browse our extensive database
Customer Resources The one stop shop for customers
Ethical Hacking How ethical hacking can help you
Snyk in 30 Resource Hub Live and on-demand sessions
Snyk Blog
Snyk's Podcasts
Snyk's YouTube
AI Glossary Knowledge & Docs
Snyk Labs Research on AI, vulnerabilities, and DevSecOps
Snyk Learn Security education from Snyk
Snyk User Docs Get started with Snyk
Snyk Support How can we help?
Snyk Vuln Database Find new vulnerabilities
Snyk Updates Stay in the loop
Snyk Partner Solutions Directory Explore Snyk Partner Integrations Our community & games
Events & Webinars
Ambassadors
AI Security Engineers Community
VulnVortex
AI Security University Program Audience
Snyk For Devs Dev-centric info on demand
Snyk For Government Mission-informed AppSec
Snyk For Security Leaders Insights from industry leaders Read the 2026 State of Agentic AI Adoption Download Now
Company Newsletter
Patched & Dispatched
Your monthly roundup of Snyk content – the latest insights patched in, dispatched straight to your inbox. No fluff. Just the good stuff. Subscribe to our newsletter
Our Services Maximize your AppSec ROI
Our Customers We help customers save time and money
Our Partners Bringing business class security with partners
Case Studies Check out our customer stories and stats
Newsroom See the latest press releases
Contact Us Get in touch with any feedback or questions
Careers Join Snyk today
Leadership Meet our leaders Snyk Embeds Anthropic's Claude Read Now
Pricing
Evo New
EN Select your language
English
Deutsch
Español
Français
日本語
Português
Login
Free and Team Plan Customers
Snyk app.snyk.io
Enterprise Plan Customers
🇺🇸 Snyk US - 1 app.snyk.io
🇺🇸 Snyk US - 2 app.us.snyk.io
🇪🇺 Snyk EU app.eu.snyk.io
🇦🇺 Snyk AU app.au.snyk.io
The region where your data is hosted follows local agreements, and it may not align with your own location. Find out more.
Snyk API & Web - All Customers
Snyk API & Web (DAST) plus.probely.app
Sign up Book a live demo
In this article
What are the different open source licenses?
Copyleft Licenses
Permissive licenses
Which Open Source License is Best?
Open Source License Control
Open Source Licenses: Types and Comparison
Written by 
Liran Tal
10 mins read
Many software buyers – even new developers – misunderstand the term “open source” to mean the software is available to use, copy, modify, and distribute as desired. This misunderstanding may arise from confusing open source with public domain or shareware, both of which are free to use and modify without specific permissions or licensing.
The truth is that, for the most part, open-source software is covered by one of several types of open source licenses and is not necessarily free of charge either.
In contrast to proprietary software where vendors typically make it impossible to access, copy or modify the source code, open source code permits the use, reuse, sharing, modification, and distribution of the code in other programs or applications. But just as with proprietary software licensing, open source software is subject to various legal terms and restrictions, depending on the type of open source license in force. Hence it is important to remain compliant with the open source software licenses terms. You should also be aware of the other risks associated with using open source software.
This article describes the different types of open source licenses and how they all seek to protect both the authors and users of the software by controlling the misuse and unauthorized use of open source code.
What is an Open Source License?
Open source software licenses govern how others – besides the originator – can use, modify, or distribute software code. They grant other users the permission and rights to use or repurpose the code for new applications or to include the code in other projects.
One of the main advantages of open source code is its visibility, which makes it easier to troubleshoot problems and to understand better how something works when the documentation is either lacking or incorrect.
Depending on the type of open source license, you may even be allowed to modify the original source code to tailor it to your needs or fix any issues you find. The license will determine whether this is possible, and under what terms. For example, you may be required to make any modifications publicly available.
Find out more about open source security with Snyk
Check out our 2023 State of Open Source Security report, or read about our top 10 open source vulnerabilities
Download the report
What are the different open source licenses?
There are over 80 variations of open-source licenses, but they generally fall into one of two primary categories: copyleft and permissive:
Copyleft license is a license type in which code derived from the original open source code inherits its license terms.
Permissive license is a license type that provides more freedom for reuse, modification, and distribution. 
Open source licenses comparison: popular copyleft licenses and permissive open source licenses.
Copyleft Licenses
The most popular copyleft open source licenses, in order of restrictiveness, are AGPL, GPL, LGPL, EPL, and Mozilla:
The GNU General Public License (GPL) preserves license notifications and copyright terms and is suitable for commercial, patent, and private use. Any software that uses GPL code must distribute all its source code under the same license. So if you use GPL code in your software (e.g., by using a GPL library), and distribute your application, all your source code must be made available under the same GPL license. This restriction makes the GPL a strong copyleft license.
The Affero GPL (AGPL) only adds only one clause, but an important one for some software. Because the GPL license is only triggered when software is distributed, there is a loophole for software that is made available over the network only, i.e., not explicitly “distributed”. The AGPL license closes this loophole by including a remote network interaction clause that triggers the GPL license for any software used over a network.
The Lesser General Public License (LGPL) provides the same level of terms as the AGPL and GPL copyleft open source licenses, including preserving copyright and license notifications. The prime variation is that smaller projects or objects accessed through larger licensed works do not require distribution of the larger project. Moreover, the modified source does not have to be distributed under the same terms that apply to the larger code project.
The Eclipse Public License (EPL) is commonly used for business software.With EPL, software developed using EPL, non-EPL, and even proprietary code can be combined and sub-licensed – provided any non-EPL elements reside independently as separate modules or objects. Modifications can be made under the EPL license, but they must be released under the same terms.
The Mozilla Public License (MPL) is the least restrictive copyleft open source software license. They make it easy to modify and use their code in closed-source and/or proprietary software, as long as any code licensed under the MPL is kept in separate files and these files are distributed with the software. The MPL also includes patent grants and enforces that copyright notices be retained.
Permissive licenses
The most popular permissive open source licenses are: Apache, MIT, BSD and Unlicense.
The Apache License requires license notifications and copyrights on the distributed code and/or as a notice in the software. However, derivative works, larger projects, or modifications are allowed to carry different licensing terms when distributed and are not required to provide source code. Apache licenses contain a patent grant.
The MIT License, which bears the name of the famous university where it originated, is perhaps the most used open source license in the world, perhaps because it is very short and clear and easy to understand. Iit allows anyone to do whatever they wish with the original code, as long as the original copyright and license notice is included either in the distributed source code or software. It removes any liability from authors and does not explicitly contain a patent grant.
The Berkeley Source Distribution (BSD) License is another permissive open source license that preserves license notices and copyrights but allows larger or licensed works to be distributed without source code and under different license terms. The 2- clause BSD License is very similar to the MIT open source license, while the 3-clause and 4-clause BSD licenses add more requirements or restrictions related to reuse and other terms.
Unlicense: As its name indicates, this is the least restrictive of open source licenses because it amounts to making the open source open to the public domain. No conditions apply, meaning these unlicensed works can be distributed without source code and under different terms.
Which Open Source License is Best?
Selecting an open source license type depends largely on the intention of the licensor or developer for use of the software. Here are some considerations to keep in mind during license comparison:
Care must be taken when choosing a copyleft license. If the original license is very permissive, the modified code is equally unrestricted, which may not be to the advantage of the author.
That having been said, copyleft licenses generally provide more restrictions – and possibly less liability – than permissive licenses.
When the intention is to make the code as reusable and shareable as possible, a level of permissive license is probably the best choice.
If you develop software that is used over a network, it can be highly advantageous to choose the AGPL. A common example of this are open source databases: by not licensing under the AGPL, any company (such as a major cloud provider) could improve on your product and monetize it without being required to distribute their modifications.
There are two main versions of the GPL license: GPLv2 and GPLv3. There are many differences in GPLv3, most of which address issues not covered in GPLv2 such as patents. GPLv3 also improves compatibility with other open source licenses such as the Apache License v2. However, take note that the two versions of GPL are not compatible with one another.
Because MIT licenses are so commonly used, there's the advantage that they are well recognized and commonly understood. When it comes to using software licensed under the MIT license, there are no restrictions regarding redistribution or monetization, which makes them very attractive for any sort of usage. It is also compatible with many other open source licenses, meaning that MIT licensed code can be used in other open source projects that use different licenses.
Open Source License Control
Many developers, businesses, and commercial software companies have a mix of several types of open source licenses. Maintaining control of those licenses can be increasingly complex as software is developed, purchased, and distributed:
Compliance with copyrights and patents
Maintaining derivative license types based on original software licenses
Awareness of effective dates and renewal requirements
Your browser does not support the video tag.
Snyk's license compliance solution
Snyk provides a complete license compliance solution to help you maintain the rapid development pace while remaining compliant with the open source software licenses in your projects.
“Because the Snyk tool identifies open source license issues, it allows our developers to generate a clean, manageable report that they can send off to the legal team, saving developers days and days of work.”
Scott Mitchell, Application Security Manager at Blue Prism.
Get a live Snyk demo for open source security
Chat with our security experts to see how Snyk can help you use open source securely
Book a live demo Or get started for free
Platform
Snyk AI Security Platform
Snyk AI Workflows
DeepCode AI
Integrations
Our Resources
Resource Library
Blog
Snyk's Podcasts
Knowledge & Docs
Snyk Labs
Snyk Learn
Snyk User Docs
Snyk Support
Snyk Vuln Database
Snyk Updates
Snyk Trust Center
Company & Community
About Snyk
Contact Us
Book A Demo
Careers
Events & Webinars
Ambassadors
Why Snyk
Snyk vs GitHub Advanced Security
Snyk vs Veracode
Snyk vs Checkmarx
Snyk vs Black Duck
Snyk vs Wiz
Snyk vs Aikido
Patched & Dispatched
Your monthly roundup of Snyk content – the latest insights patched in, dispatched straight to your inbox. No fluff. Just the good stuff.
Subscribe to our newsletter
© 2026 Snyk Limited
Registered in England and Wales
Legal terms
Privacy Notice
Terms of use
California residents: do not sell my information
English
Deutsch
Español
Français
日本語
Português (Brasil)
English
Deutsch
Español
Français
日本語
Português (Brasil)
Privacy Information
We use cookies to enhance our services, and improve our product and marketing efforts. We and our partners are using tracking technologies to process personal data in order to improve your experience. You may always exercise your consumer right to opt-out. For detailed information about personal information we collect and third parties having access to it, please select 'More Information' or refer to our privacy policy. Read More Read Less
Privacy Policy Terms of service More Information
OK
Powered by Usercentrics Consent Management
