---
name: Transitive Dependency Vulnerabilities: The 95% Blind Spot | Kusari®
keywords: (placeholder)
metadata:
  url: https://www.kusari.dev/blog/why-transitive-dependencies-biggest-software-supply-chain-blind-spot-2026
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T23:03:23.186Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
Transitive Dependency Vulnerabilities: The 95% Blind Spot | Kusari®
NEW! AppSec in Practice Research
Get the Report
Product
Product
Kusari Inspector Kusari Platform Integrations
Industries
Medical Devices Blog Introducing the Kusari Platform—know your software
Developers
Resources
Resources
All Resources Case Studies Coffee with Kusari videos Docs Events Guides Newsletters Product Tour Solution Briefs Free webinar The New Frontline in DevSecOps: Security at the Pull Request
Blog
Learning Center
Company
Company
About Open Source Partners Newsroom Contact us Newsroom CNCF and Kusari Partner to Strengthen Software Supply Chain Security across Cloud-Native Projects
Docs
Get a Demo
Log In
The 95% Problem: Why Transitive Dependencies Are Your Biggest Software Supply Chain Blind Spot in 2026
Your security team just finished a vulnerability scan. The dashboard looks clean, but there's a catch: that scan only covered about 5% of your actual risk surface. 
Tim Miller  
March 4, 2026 
Your security team just finished a vulnerability scan. The dashboard looks clean—direct dependencies patched, known CVEs addressed, compliance boxes checked. But there's a catch: that scan only covered about 5% of your actual risk surface.
Key Insights
The 95% Transitive Dependency Problem: The overwhelming majority (approximately 95% of open-source vulnerabilities) do not reside in a project's direct dependencies, but in the transitive dependencies (indirect components) they pull in. This creates the single largest software supply chain blind spot for organizations relying on surface-level scanning.
Visibility Gap is the Core Risk: Traditional Software Composition Analysis (SCA) tools often fail to provide adequate visibility into deeper dependency layers. A typical enterprise application may have only dozens of direct dependencies but hundreds or thousands of invisible transitive components, drastically expanding the attack surface and leading to remediation efforts described as a "whack-a-mole" scenario.
Complete SBOMs are Non-Negotiable: Effective transitive dependency vulnerability management must start with generating a complete, recursive Software Bill of Materials (SBOM). An accurate SBOM must capture every component in the full dependency graph, not just the top-level packages, to prevent compliance gaps and untracked inherited risk.
Contextual Analysis for Prioritization: To overcome alert fatigue, security teams must move beyond raw SCA output and implement reachability analysis. This capability determines if a vulnerable function is actually invoked by the application's code, allowing for contextual risk assessment and helping teams prioritize remediation based on blast radius and exploit probability (leveraging data like EPSS and KEV) rather than just a high CVSS score.
Shift to Proactive Governance: Mature software supply chain security requires continuous, automated monitoring of the dependency graph and clear ownership across DevSecOps teams. This proactive approach shifts the security posture from simply firefighting inherited risks to informed governance, enabling organizations to catch newly disclosed transitive dependency vulnerabilities closer to the point of introduction.
Kusari's Solution for Deep Visibility: Platforms like Kusari, which maintain the GUAC (Graph for Understanding Artifact Composition), are essential for gaining actionable visibility into deeply nested dependencies. They automatically map complex relationships, apply reachability analysis, and provide the business context needed to effectively remediate exposure within the modern software supply chain.
Transitive dependency vulnerabilities are security flaws that live in the indirect components your software inherits through its direct dependencies. They sit two, three, or ten layers deep in your dependency graph, and most organizations have almost no visibility into them. According to research from Endor Labs, roughly 95% of open-source vulnerabilities reside in these transitive components—not in the packages your developers deliberately selected.
This article explains what transitive dependency vulnerabilities are, why they represent the single largest blind spot in modern software supply chains, how to detect and prioritize them, and what practical steps DevSecOps teams can take to close the gap. It is written for CISOs, security engineers, and DevSecOps leads at mid-sized organizations who need to move beyond surface-level scanning and build real supply chain visibility.
What Are Transitive Dependencies, and Why Do They Create Security Blind Spots?
A transitive dependency is any software component that your application inherits indirectly. When your project depends on Library A, and Library A depends on Library B, which in turn depends on Library C—Libraries B and C are transitive dependencies. Your developers never chose them. They may not even know they exist.
This distinction matters because modern applications are mostly assembled rather than written from scratch. A typical enterprise project might declare 20 or 30 direct dependencies, but the full dependency graph can easily contain hundreds or even thousands of transitive components. One Kusari customer, for example, discovered over 18,000 components in their dependency tree after tracking only direct dependencies.
The problem compounds quickly. Each transitive layer inherits its own dependencies, creating a deeply nested structure that expands your attack surface in ways traditional scanning tools rarely capture. This is what the industry calls indirect dependency security—and it's where most hidden vulnerabilities actually live.
The Visibility Gap: Most Teams Can't See Their Real Attack Surface
Survey data from Kusari's Application Security in Practice report paints a stark picture. Only 28% of respondents said they had strong insight into their deeper transitive dependency layers. Meanwhile, 56% reported being "highly aware" of their direct dependencies. That's a massive awareness gap between what teams think they control and what actually runs in production.
This gap creates what practitioners often describe as a "whack-a-mole" scenario. A team remediates a vulnerability in one component, only to discover that the same flaw (or a related one) surfaces again through a different transitive path they didn't know about. Without a complete dependency graph, remediation becomes an endless game of chasing symptoms instead of root causes.
The consequences are measurable. According to the same report, nearly half of teams (47%) spend more than five hours per week responding to and remediating software supply chain security issues. That's developer time diverted from building features—spent instead on firefighting problems that could have been prevented with better visibility.
Source: Kusari, Application Security in Practice Report (2026)
Why Traditional SCA Tools Miss Transitive Dependency Vulnerabilities
Software Composition Analysis (SCA) tools have been the default approach to dependency security for years. They scan your project manifest files, cross-reference known vulnerabilities in databases like the CVE or National Vulnerability Database (NVD), and flag matches.
The limitation? Most SCA tools focus primarily on direct dependencies—the packages explicitly declared in your package.json, pom.xml, or requirements.txt. They may list transitive components, but they rarely provide the context needed to act on them. Which transitive paths actually lead to your application's runtime? Is a flagged vulnerability even reachable through your code? What's the blast radius if it's exploited?
Without reachability analysis, SCA tools generate noise. They report vulnerabilities that may exist in your dependency tree but can't tell you whether those flaws are actually exploitable in your specific context. This leads to alert fatigue—security teams drowning in findings they can't prioritize, and developers losing trust in the tooling altogether.
What organizations need is not just detection but a remediation workflow that accounts for the full dependency graph, assesses actual exposure, and helps teams focus on what matters. That shift—from raw scanning to contextual risk analysis—is where transitive dependency vulnerability management starts to mature.
How Supply Chain Blind Spots Turn Into Real-World Breaches
The Log4Shell vulnerability (CVE-2021-44228) remains the textbook case for transitive dependency risk. Log4j, a widely used Java logging library, was rarely declared as a direct dependency. Instead, it was pulled in transitively through frameworks like Apache Struts, Spring Boot, and dozens of other libraries. When the critical flaw was disclosed in December 2021, organizations scrambled to determine whether they were even exposed—many couldn't answer that question for days or weeks.
More recently, the xz Utils backdoor (CVE-2024-3094) revealed how a compromised maintainer could inject malicious code into a deeply nested component. The attack targeted a compression library that most developers would never interact with directly but that sat in the transitive dependency chain of critical Linux distributions.
These aren't isolated events. The pattern is consistent: attackers target components that are widely used but poorly monitored. Transitive dependencies are ideal targets precisely because they exist in the supply chain blind spots that most organizations haven't addressed.
Legacy systems compound this risk. Kusari's report found that 59% of respondents cited legacy systems as the most significant source of inherited risk in their software supply chain. Healthcare organizations were particularly exposed, with 84% flagging legacy systems as their biggest concern. Older codebases tend to have longer, less maintained dependency chains where transitive vulnerability accumulation goes unchecked.
Direct vs. Transitive Dependencies: A Comparison
Understanding the difference between direct and transitive dependencies is foundational to closing the visibility gap.
This table highlights why relying solely on direct dependency management leaves the majority of your SBOM accuracy unverified. A complete picture requires mapping the entire dependency tree, including every transitive path.
Five Steps to Improve Transitive Dependency Visibility
Closing the transitive dependency visibility gap doesn't require ripping out existing tooling overnight. It does require a deliberate, layered approach.
Step 1: Generate a complete, recursive SBOM. Your Software Bill of Materials should capture every component in your dependency graph—not just the top layer. Tools that perform recursive resolution across package managers like npm, Maven, PyPI, and NuGet are essential.
Step 2: Map the full dependency graph. A flat list of components isn't enough. You need to understand the relationships between them—which packages pull in which, through what paths, and at what versions. Dependency graph visualization makes it possible to trace transitive dependency vulnerabilities back to their source.
Step 3: Apply reachability analysis. Not every vulnerability in your dependency tree is exploitable. Reachability analysis determines whether a vulnerable function is actually called by your application code, dramatically reducing false positives and helping your team focus on risks that matter.
Step 4: Prioritize using blast radius, not just CVSS scores. A critical-severity CVE in a deeply nested, unreachable library is less urgent than a moderate-severity flaw in a transitive component that's actively invoked at runtime. Combine CVSS with EPSS (Exploit Prediction Scoring System) and KEV (Known Exploited Vulnerabilities) data for smarter vulnerability prioritization.
Step 5: Automate continuous monitoring. Dependencies change constantly. New versions are released, maintainers shift, and previously safe components get compromised. Continuous monitoring of your dependency graph ensures that newly disclosed transitive dependency vulnerabilities are caught early—not weeks later during a scheduled scan.
When Transitive Dependency Monitoring Falls Short
No approach works universally, and it's worth being upfront about the limitations.
Transitive dependency analysis is less effective when applied to vendored code—projects where dependencies are copied directly into the repository rather than resolved through a package manager. Without a manifest file to parse, automated tools can't reconstruct the dependency tree reliably.
Polyglot environments present another challenge. An application that spans three or four programming languages (say, a Java backend with a Python ML service and a Node.js frontend) requires different dependency resolution strategies for each ecosystem. Most tools handle one or two ecosystems well; few handle all of them equally.
Organizations with very large monorepos may also face performance constraints. Mapping the complete dependency graph for a monorepo with millions of lines of code and thousands of packages takes compute time and can generate dependency trees so large they're difficult to interpret without purpose-built tooling.
Finally, transitive dependency visibility doesn't replace other security practices. It's one layer in a defense-in-depth strategy that should also include code review, build integrity verification (via frameworks like SLSA and in-toto), and runtime monitoring.
What Mature Transitive Dependency Management Looks Like
Organizations in the top quartile of Kusari's survey—those that understand their transitive dependencies "to a great extent"—consistently report better security outcomes. They check their security posture more frequently, respond to vulnerabilities faster, and experience fewer unexpected incidents.
These teams share a few common characteristics. They treat transitive dependency visibility as a foundational capability, not an advanced add-on. They run automated SCA and SBOM generation on every pull request, not just at release milestones. And they've established clear ownership of dependency hygiene across development and security teams—avoiding the fragmented responsibility that slows remediation at most organizations.
The data also shows a correlation between checking frequency and outcomes. Organizations that assess security daily (19% of respondents) report 40% fewer monthly vulnerability discoveries than those that check only at release milestones. Earlier, more frequent checks catch issues closer to the point of introduction, reducing downstream remediation costs.
Transitive dependency vulnerability management, done well, shifts the security posture from reactive to proactive—from firefighting inherited risks to understanding and governing them before they reach production.
Closing the Gap with Kusari
Kusari helps organizations gain actionable visibility into both direct and transitive dependencies across the software supply chain. Our data and analysis go deeper to automatically maps nested dependency relationships, identifies inherited risk, and provides the context needed for effective remediation—without manual configuration or guesswork about dependencies. We're not reverse engineering to get to a solution, we've done the hard work to provide source information about the software you have now to the new libraries and AI-generated code that's being pulled into your enterprise.
Rather than generating another flood of alerts, Kusari surfaces findings with business context: which transitive paths are reachable, what the blast radius of a vulnerability looks like, and where to focus remediation efforts. This approach helps DevSecOps teams move from reactive scanning to informed, continuous supply chain security.
Request a demo to see how Kusari closes the visibility gap for transitive dependencies.
Frequently Asked Questions
What are transitive dependency vulnerabilities? Transitive dependency vulnerabilities are security flaws found in indirect software components—the packages your application inherits through its declared dependencies rather than ones your developers explicitly selected. Because these components are pulled in automatically during dependency resolution, they often escape routine security scans and create hidden risk in the software supply chain.
Why are transitive dependencies harder to detect than direct dependencies? Transitive dependencies are harder to detect because they don't appear in standard manifest files and can sit multiple layers deep in the dependency graph. Traditional SCA tools primarily focus on direct dependencies, and without recursive resolution and reachability analysis, security teams may not know these components exist—let alone whether they contain exploitable flaws.
What percentage of open-source vulnerabilities are found in transitive dependencies? According to research published by Endor Labs, approximately 95% of open-source vulnerabilities reside in transitive dependencies rather than in directly declared packages. This statistic underscores why organizations that only scan direct dependencies are missing the vast majority of their actual risk surface.
How can organizations improve visibility into transitive dependency vulnerabilities? Organizations can improve visibility into transitive dependencies by generating recursive SBOMs that capture the full dependency tree, mapping dependency graphs to understand component relationships, applying reachability analysis to assess exploitability, and implementing continuous monitoring to catch newly disclosed flaws. Prioritization should combine CVSS, EPSS, and KEV data rather than relying solely on severity scores.
What is the difference between a direct and a transitive dependency? A direct dependency is a software package that developers explicitly include in their project configuration. A transitive dependency is inherited indirectly—it's a dependency of a dependency. For example, if your project uses Library A, which requires Library B, then Library B is a transitive dependency. Most applications contain far more transitive dependencies than direct ones.
How does SBOM accuracy relate to transitive dependency security? SBOM accuracy depends directly on whether the Software Bill of Materials captures transitive components. An SBOM that lists only direct dependencies misrepresents the software's true composition, creating compliance gaps and leaving hidden vulnerabilities untracked. A complete, recursive SBOM is the foundation for effective transitive dependency vulnerability management.
What tools help with managing transitive dependency vulnerabilities? Transitive dependency vulnerability management typically requires advanced SCA tools with recursive dependency resolution, SBOM generation platforms, dependency graph visualization, and reachability analysis capabilities. Platforms like Kusari combine these capabilities with continuous monitoring and contextual risk assessment to help teams prioritize remediation based on actual exposure rather than raw severity scores.
Like what you read? Share it with others.
  
Other blog posts
The latest industry news, interviews, technologies, and resources.
View all posts
[
Open Source Summit 2022
 Takeaways & Learnings June 23, 2022 Tim Miller](https://www.kusari.dev/blog/open-source-summit-2022)
[
SPIFFE/SPIRE CSI Driver
 Overview of the SPIFFE/SPIRE CSI Driver June 27, 2022 Parth Patel](https://www.kusari.dev/blog/spiffe-spire-csi-driver)
[
Not Just Third Party Risk
 There's a misconception in Cybersecurity among some that Software Supply Chain Security is just Third Party Risk Mana... July 20, 2022 Michael Lieberman](https://www.kusari.dev/blog/not-just-third-party-risk)
[
Government Memo for Enhancing the Security of the Software Supply Chain
 Executive Order (EO) 14028, Improving the Nation's Cybersecurity was released last year in May. September 19, 2022 Parth Patel](https://www.kusari.dev/blog/government-memo-for-enhancing-the-security-of-the-software-supply-chain)
[
A High Fidelity View of Software Supply Chain
 Understanding and maintaining your software supply chain can be a task that needs 24/7 vigilance. October 20, 2022 Michael Lieberman](https://www.kusari.dev/blog/a-high-fidelity-view-of-software-supply-chain)
[
Kusari presenting at KubeCon and Cloud Native SecurityCon NA 2022
 KubeCon + CloudNativeCon is right around the corner and we are excited to be attending in person! October 21, 2022 Parth Patel](https://www.kusari.dev/blog/kusari-presenting-at-kubecon-and-cloud-native-securitycon-na-2022)
[
The Next Heartbleed?
 Heartbleed (CVE-2014-0160) in 2014 left the industry in a scramble... October 31, 2022 Parth Patel](https://www.kusari.dev/blog/the-next-heartbleed)
[
Kusari's Software Supply Chain Security Overview
 What is Software Supply Chain security, and why should I care? March 14, 2023 Michael Lieberman](https://www.kusari.dev/blog/kusaris-software-supply-chain-security-overview)
[
Applying Zero Trust to the Software Supply Chain
 Understanding Zero Trust and Its Benefits March 28, 2023 Michael Lieberman](https://www.kusari.dev/blog/applying-zero-trust-to-the-software-supply-chain)
[
Figure Out Who's Lurking in Your Supply Chain With Signatures and Attestations
 A Story of Software and Cats April 4, 2023 Michael Lieberman](https://www.kusari.dev/blog/figure-out-whos-lurking-in-your-supply-chain-with-signatures-and-attestations)
[
Kusari Open-Sources Spector
 We're excited to announce the open-sourcing of Spector. April 26, 2023 Michael Lieberman](https://www.kusari.dev/blog/kusari-open-sources-spector)
[
GUAC v0.1 Beta Release
 Kusari is excited to announce the v0.1 beta release of GUAC — Graph for Understanding Artifact Composition. May 23, 2023 Tim Miller](https://www.kusari.dev/blog/guac-v0-1-beta-release)
[
Quest to determine the 'G' in GUAC
 Working towards determining a persistent database for GUAC June 27, 2023 Parth Patel](https://www.kusari.dev/blog/quest-to-determine-the-g-in-guac)
[
daBOM Podcast with Tim & DJ
 Tim appeared as a guest on the daBOM podcast. July 5, 2023 Tim Miller](https://www.kusari.dev/blog/dabom-podcast-with-tim-dj)
[
Announcing Helm Chart for GUAC
 Helm Chart for GUAC July 12, 2023 Tim Miller](https://www.kusari.dev/blog/announcing-helm-chart-for-guac)
[
Case Study: A discussion with Guidewire on GUAC
 A look into Guidewire's software supply chain security use case and why they are using GUAC August 2, 2023 Michael Lieberman](https://www.kusari.dev/blog/case-study-a-discussion-with-guidewire-on-guac)
[
Announcing the Kusari YouTube Channel and GUACademy
 Kusari have just launched a YouTube Channel! August 23, 2023 Jeff Mendoza](https://www.kusari.dev/blog/youtube-channel-and-guacademy)
[
Terror of cURL - Preparation is Half the Battle
 CVE-2023-38545 - HIGH Severity Vulnerability October 16, 2023 Parth Patel](https://www.kusari.dev/blog/terror-of-curl)
[
Spooky Enhancements: Unveiling GUAC's OpenVEX Feature
 GUAC's OpenVEX Integration October 31, 2023 Nathan Naveen](https://www.kusari.dev/blog/spooky-enhancements-unveiling-guacs-openvex-feature)
[
What the NSA Missed in its SBOM Management Recommendations
 The missing first step that most organizations are still struggling with December 22, 2023 Parth Patel](https://www.kusari.dev/blog/what-the-nsa-missed-in-its-sbom-management-recommendations)
[
Contributor to Leader: Securing Open Source Software at OpenSSF
 Kusari elected to OpenSSF leadership roles January 16, 2024 Michael Lieberman](https://www.kusari.dev/blog/contributor-to-leader-securing-open-source-software-at-openssf)
[
Our $8M Funding Round Fuels our Mission to Make the Software Supply Chain Transparent and Secure
 Kusari raises seed funding January 18, 2024 Tim Miller](https://www.kusari.dev/blog/seed-funding)
[
Kusari Soaks up Community at FOSDEM and Beyond
 Kusari speaking at FOSDEM and other EU community venues January 26, 2024 Jeff Mendoza](https://www.kusari.dev/blog/kusari-soaks-up-community-at-fosdem-and-beyond)
[
From Open Source Community to Joining a Start-up – while in High School
 Nathan Naveen, a 17-year-old high schooler, shares his journey to becoming an intern at Kusari February 8, 2024 Nathan Naveen](https://www.kusari.dev/blog/intern-at-kusari)
[
Unveiling GUAC as an OpenSSF Incubating Project for Software Dependency Management
 Today, we find ourselves in a moment akin to proud parents, as we witness a significant milestone in the journey of Graph for Understanding Artifact Composition (GUAC). March 7, 2024 Parth Patel Michael Lieberman](https://www.kusari.dev/blog/unveiling-guac-as-an-openssf-incubating-project-for-software-dependency-management)
[
Graph for Understanding Artifact Composition (GUAC) Joins OpenSSF as Incubating Project
 The GUAC maintainers are pleased to announce the project has joined the Open Source Security Foundation (OpenSSF) as an Incubating Project. March 7, 2024 Michael Lieberman Brandon Lum](https://www.kusari.dev/blog/graph-for-understanding-artifact-composition-guac-joins-openssf-as-incubating-project)
[
XZ Backdoor: Software Security Lessons
 The recent incident involving the XZ backdoor brings to light the critical importance of vigilance and proactive security measures, while not losing sight of the human element. April 5, 2024 Michael Lieberman](https://www.kusari.dev/blog/xz-backdoor-software-security-lessons)
[
Proactive Security in the Post-Log4j Era
 Gone are the days when signing containers and running vulnerability scans through CI processes provided a sense of security. April 23, 2024 Tim Miller](https://www.kusari.dev/blog/proactive-security-in-the-post-log4j-era)
[
Graph for Understanding Artifact Composition (GUAC) adds persistent storage in v0.6.0 release
 Open source supply chain observability tool standardizes on PostgreSQL May 6, 2024 Jeff Mendoza Dejan Bosanac](https://www.kusari.dev/blog/graph-for-understanding-artifact-composition-guac-adds-persistent-storage-in-v0-6-0-release)
[
Another Turn of the Page: GUAC v0.7.0 Released
 Improving performance with pagination and more June 4, 2024 Parth Patel](https://www.kusari.dev/blog/another-turn-of-the-page-guac-v0-7-0-released)
[
Counting CVEs Was Never Enough
 CVE IDs don't tell you much, but somehow we started using them as a proxy for security June 6, 2024 Ben Cotton](https://www.kusari.dev/blog/counting-cves-was-never-enough)
[
Kusari Signs the Secure by Design Pledge
 The Secure By Design Pledge is a great starting point, but it can't be the end. June 12, 2024 Tim Miller](https://www.kusari.dev/blog/secure-design-pledge)
[
To Fork or Not to Fork
 How you handle your dependencies will change how you secure your software supply chain June 27, 2024 Ben Cotton](https://www.kusari.dev/blog/to-fork-or-not-to-fork)
[
Meeting Federal Software Supply Chain Mandates
 Only two months left until the Secure Software Development Attestation Form deadline July 11, 2024 Parth Patel](https://www.kusari.dev/blog/meeting-federal-software-supply-chain-mandates)
[
Achieving Wisdom with GUAC Visualizer
 It's not enough to just have the data, you need to be able to see it. July 23, 2024 Ben Cotton](https://www.kusari.dev/blog/achieving-wisdom-with-guac-visualizer)
[
Announcing GUAC v0.8.0 Enhancements
 GUAC v0.8.0 brings support for license information, running vuln scans upon SBOM ingestion, node deletion, and many other improvements. July 25, 2024 Parth Patel](https://www.kusari.dev/blog/announcing-guac-v0-8-0-license-data-integration-immediate-vuln-scans-and-streamlined-node-deletion)
[
Why Software Cannot Be Secured by SBOMs Alone
 Actionable insights come from SBOMs plus additional information July 31, 2024 Tim Miller](https://www.kusari.dev/blog/why-software-cannot-be-secured-by-sboms-alone)
[
Hack-Proof Artificial Intelligence Supply Chains Using Open Source Security
 Practical ways to protect against AI software attacks August 5, 2024 Tim Miller Michael Lieberman](https://www.kusari.dev/blog/hack-proof-ai-supply-chains-using-open-source-security)
[
GUAC Boosts License Transparency
 v0.8.0 features new integration with ClearlyDefined August 8, 2024 Ben Cotton](https://www.kusari.dev/blog/guac-boosts-license-transparency)
[
Understanding Prevalence is the First Step
 The White House commits $11 million to enhance our collective understanding of the challenges surrounding open source software. August 26, 2024 Ben Cotton](https://www.kusari.dev/blog/understanding-prevalence-is-the-first-step)
[
You Can't Fix Issues if You Can't Find Them
 Organizations often struggle to identify vulnerabilities and risks hidden within the layers of dependencies. Address it by using a holistic approach to software security. October 18, 2024 Ben Cotton Parth Patel](https://www.kusari.dev/blog/you-cant-fix-issues-if-you-cant-find-them)
[
Introducing the Kusari Platform—know your software
 Navigating modern software development is a complex challenge. Kusari's aim is to make it easier. October 22, 2024 Parth Patel](https://www.kusari.dev/blog/introducing-the-kusari-platform--know-your-software)
[
Is Your Supply Chain Haunted by CVEs?
 Secure development starts with developers: bring forth the code masters October 31, 2024 Michael Lieberman](https://www.kusari.dev/blog/is-your-supply-chain-haunted-by-cves)
[
The Path to Zero CVEs: Vanquishing Cyber Threats
 Addressing Common Vulnerabilities and Exposures (CVEs) is no longer optional—aiming to eliminate them is a critical priority for securing modern systems. November 8, 2024 Michael Lieberman Andrew Martin, CEO of ControlPlane](https://www.kusari.dev/blog/the-path-to-zero-cves-vanquishing-cyber-threats)
[
Is the Internet on Fire? The State of Open Source Security
 Amid the flurry of innovation and collaboration at last week's KubeCon North America, a critical theme emerged: the precarious state of open source security. November 26, 2024 Michael Lieberman Andrew Martin, CEO of ControlPlane](https://www.kusari.dev/blog/is-the-internet-on-fire-the-state-of-open-source-security)
[
The Best Way to Secure Your Open Source Supply Chain is to Participate
 Open source software powers 96% of modern applications, but it comes with challenges. Companies can secure their supply chains by actively participating in the open source projects they rely on. December 5, 2024 Ben Cotton](https://www.kusari.dev/blog/the-best-way-to-secure-your-open-source-supply-chain-is-to-participate)
[
Rust Won't Fix Everything: Moving Toward a Memory-Safe Future
 Rust is promising for addressing memory safety issues. Improving existing C/C++ toolchains will take time, but these steps help set a realistic path forward. December 9, 2024 Ben Cotton Michael Lieberman](https://www.kusari.dev/blog/rust-wont-fix-everything-moving-toward-a-memory-safe-future)
[
Threat Modeling in the Software Development Life Cycle
 What are you defending against? From upstream dependencies to code repositories, threat modeling ensures you're prepared to mitigate risks, reduce vulnerabilities, and avoid costly compromises. December 17, 2024 Parth Patel](https://www.kusari.dev/blog/threat-modeling-in-the-software-development-life-cycle)
[
Solving the “Bottom Turtle” Problem in Supply Chain Security
 Software supply chain security is like a stack of turtles—each layer depends on the integrity of the one below it. Continuous vigilance is key to maintaining security all the way down. December 18, 2024 Michael Lieberman](https://www.kusari.dev/blog/solving-the-bottom-turtle-problem-in-supply-chain-security)
[
Software Supply Chain Security Predictions: Hits & Misses from 2024
 As 2025 approaches, it's time to revisit our 2024 software supply chain security predictions to see how they held up. December 29, 2024 Michael Lieberman](https://www.kusari.dev/blog/software-supply-chain-security-predictions-hits-misses-from-2024)
[
AI Alone Won't Fix Your Supply Chain
 Properly integrating AI into your processes can help identify risks and offer proactive insights, but the final decisions must always remain in human hands. January 10, 2025 Tim Miller](https://www.kusari.dev/blog/ai-alone-wont-fix-your-supply-chain)
[
Software Supply Chain Security Predictions for 2025
 This year, we focus on the evolving role of AI, pressing software security concerns, and emerging regulations. January 13, 2025 Michael Lieberman](https://www.kusari.dev/blog/software-supply-chain-security-predictions-for-2025)
[
Stick a Pin in It: Managing Dependencies for Supply Chain Security
 Managing software dependencies is an important part of software supply chain security. Here are three approaches you can take to pin your dependencies to known-good versions. January 23, 2025 Ben Cotton](https://www.kusari.dev/blog/pinning-dependencies)
[
Alarms Raised by Critical Reverse Backdoor Vulnerability in Medical Devices
 Medical monitors have critical security flaws, allowing unauthorized code execution and patient data leaks. February 3, 2025 Michael Lieberman](https://www.kusari.dev/blog/reverse-backdoor-medical-devices)
[
Unpacking the Kusari Score
 Cut through the noise to prioritize which vulnerability gets fixed next February 13, 2025 Parth Patel Jeff Mendoza](https://www.kusari.dev/blog/kusari-score)
[
Unpacking the Kusari “Effort to Fix” Capability
 Get a clear understanding of the work involved in remediating a vulnerability so you can schedule it in your sprint without blocking feature work. February 18, 2025 Parth Patel Jeff Mendoza](https://www.kusari.dev/blog/effort-to-fix)
[
Building a Foundation of Trust for a Stronger Software Supply Chain
 Creating a secure foundation of trust enables organizations to safely delegate specific actions in the software development life cycle. February 20, 2025 Michael Lieberman](https://www.kusari.dev/blog/foundation-trust-stronger-software-supply-chain)
[
Analyzing Third-Party Risk in Open Source Software
 Third-party risk management is an important part of protecting your organization. But how do you manage the risks of open source software when you have no vendor relationship? February 25, 2025 Parth Patel Ben Cotton](https://www.kusari.dev/blog/tprm-open-source-software)
[
Addressing Third-Party Risk in Open Source Software
 Once you've discovered the third-party risks in the open source projects you consume, how do you address those risks without having a vendor relationship with the projects? February 27, 2025 Parth Patel Ben Cotton](https://www.kusari.dev/blog/tprm-open-source-addressing)
[
Raising the Bar for Open Source Security: Introducing the OSPS Baseline
 Kusari is proud to contribute to the Open Source Project Security Baseline, an OpenSSF project to help open source maintainers improve their security posture. March 3, 2025 Ben Cotton](https://www.kusari.dev/blog/introducing-osps-baseline)
[
Unpacking Kusari Platform Views
 Kusari Platform gives you the information you need to secure your software supply chain. March 5, 2025 Parth Patel Melissa Kee](https://www.kusari.dev/blog/unpacking-kusari-platform-views)
[
Starting the Security Journey: Producing an SBOM
 A hypothetical organization takes the first step on their software supply chain security journey by creating an SBOM for their application. March 11, 2025 Michael Lieberman](https://www.kusari.dev/blog/starting-the-security-journey-producing-an-sbom)
[
The Next Step in the Security Journey: Comparing SBOMs
 Once you have multiple releases, you have multiple SBOMs. What can you learn from comparing them? March 13, 2025 Michael Lieberman](https://www.kusari.dev/blog/the-next-step-in-the-security-journey-comparing-sboms)
[
Another Step on the Security Journey: A Constellation of SBOMs
 Comparing two SBOMs is useful, but as your portfolio grows, you need to take a holistic approach. March 18, 2025 Michael Lieberman](https://www.kusari.dev/blog/another-step-on-the-security-journey-a-constellation-of-sboms)
[
The Last Step on the Security Journey: Kusari Platform
 When you need a solution for managing your software supply chain, the Kusari Platform provides enterprise-ready features backed by security expertise. March 20, 2025 Michael Lieberman](https://www.kusari.dev/blog/security-journey-kusari-platform)
[
Securing Your AI Models
 The abilities of generative and agentic AI models require a proactive approach to protecting the AI supply chain. March 25, 2025 Tim Miller](https://www.kusari.dev/blog/securing-your-ai-models)
[
GUAC Now Supports Runtime Kubernetes SBOMs using Kubescape
 GUAC v0.14.0 includes a Kubescape collector that can be run inside your Kubernetes cluster to watch for new scan results from Kubescape and ingest those results into GUAC March 27, 2025 Jeff Mendoza Ben Hirschberg](https://www.kusari.dev/blog/guac-kubescape)
[
Securing the Software Supply Chain book now available!
 This new book from Michael Liberman and Brandon Lum guides you from the basics of supply chain security through to being a security expert. April 1, 2025 Michael Lieberman Brandon Lum](https://www.kusari.dev/blog/book-available)
[
Providing Secure Updates with TUF
 A secure and resilient method for distributing software updates is a key part of keeping your supply chain trustworthy. April 10, 2025 Michael Lieberman](https://www.kusari.dev/blog/providing-secure-updates-with-tuf)
[
The Hidden Risk in Your Software: Understanding Transitive Dependencies
 Transitive dependencies are the invisible majority of your applications. Failure to properly understand them increases your risk. April 15, 2025 Parth Patel](https://www.kusari.dev/blog/understanding-transitive-dependencies)
[
Codifying the SDLC with in-toto
 in-toto helps ensure product integrity by making transparent what steps were performed, by whom, and in what order. April 17, 2025 Michael Lieberman](https://www.kusari.dev/blog/codifying-the-sdlc-with-in-toto)
[
The Hidden Risk in Your Software: Managing Transitive Dependencies
 Beyond knowing why transitive dependencies are important, you have to know how to manage them. April 22, 2025 Parth Patel](https://www.kusari.dev/blog/the-hidden-risk-in-your-software-managing-transitive-dependencies)
[
VulnCon 2025 Recap
 Kusari CTO Mike Lieberman shares his thoughts after attending the second-annual VulnCon conference. April 24, 2025 Michael Lieberman](https://www.kusari.dev/blog/vulncon-2025-recap)
[
The Future of CVEs
 Recent funding concerns have highlighted the need for a more resilient system of vulnerability identification. April 28, 2025 Michael Lieberman Ben Cotton](https://www.kusari.dev/blog/future-cves)
[
Identifying Threats in the Implementation Phase
 Many threats present themselves while implementing software. Here's how to find and address them. April 30, 2025 Michael Lieberman](https://www.kusari.dev/blog/implementation-phase-threats)
[
Endpoint Security is Supply Chain Security
 Endpoint security is a key part of many IT security efforts, but it's not always thought about in the specific context of software supply chain security. May 7, 2025 Michael Lieberman](https://www.kusari.dev/blog/endpoint-security)
[
OpenSSF Tech Talk Recap: Using the OSPS Baseline to Navigate Standards and Regulations
 Open source projects are in the spotlight as regulated industries, governments and those that sell to them ramp cybersecurity expectations. Enter Open Source Project Security (OSPS) Baseline! May 8, 2025](https://www.kusari.dev/blog/openssf-tech-talk-recap-using-the-osps-baseline-to-navigate-standards-and-regulations)
[
Open Source Accelerates Secure Software
 The US DoD's Software Fast-Track Initiative looks to improve software procurement and security. Open source software must be a key part of this. May 12, 2025 Ben Cotton](https://www.kusari.dev/blog/open-source-accelerates-secure-software)
[
Code is More Important than Identity for Security
 Asking open source contributors to prove their legal identity doesn't make software more secure. May 14, 2025 Michael Lieberman Ben Cotton](https://www.kusari.dev/blog/code-is-more-important-than-identity-for-security)
[
Choosing an SBOM Generation Tool
 There are so many tools to build SBOMs for your application. How do you know which one to pick? May 21, 2025 Nathan Naveen](https://www.kusari.dev/blog/choosing-an-sbom-generation-tool)
[
Securing the Maintenance Phase
 Securing the software supply chain doesn't end when a release ships. Maintaining released software is an important part of security. May 28, 2025 Michael Lieberman](https://www.kusari.dev/blog/securing-the-maintenance-phase)
[
AI and the Secure Software Factory
 Artificial intelligence can help secure the software supply chain, but it also brings additional considerations. June 4, 2025 Michael Lieberman](https://www.kusari.dev/blog/ai-and-the-secure-software-factory)
[
Kusari Inspector: Security Insights Where You Need Them
 Kusari Inspector is now generally available to provide immediate supply chain security insights in pull requests. June 17, 2025 Parth Patel](https://www.kusari.dev/blog/kusari-inspector-security-insights-where-you-need-them)
[
Top 5 Pull Request Security Risks Every Maintainer Should Know
 For maintainers responsible for project integrity, understanding these risks isn't optional. It's essential for protecting your software supply chain. June 19, 2025 Parth Patel](https://www.kusari.dev/blog/top-5-pull-request-security-risks-every-maintainer-should-know)
[
Stop Merging Risky Code: Secure Pull Requests with Automated Security Checks
 Implementing secure pull requests has become essential to prevent security vulnerabilities from making their way into the codebase. June 23, 2025 Parth Patel](https://www.kusari.dev/blog/stop-merging-risky-code)
[
Going Beyond Vibes with Kusari Inspector
 Your security reviews need to be based on facts, not vibes. June 25, 2025 Parth Patel](https://www.kusari.dev/blog/going-beyond-vibes-with-kusari-inspector)
[
GitHub Code Review Best Practices for Security-Critical Projects
 Explore essential GitHub code security review strategies, specifically designed for projects where security cannot be compromised. July 2, 2025 Ben Cotton](https://www.kusari.dev/blog/github-code-review-best-practices-for-security-critical-projects)
[
Using Pull Requests on a Single-Developer Project
 The pull request workflow might seem unnecessary for projects with one developer, but it offers security, testing, and feedback benefits. July 9, 2025 Karly Nelson](https://www.kusari.dev/blog/using-pull-requests-on-a-single-developer-project)
[
Supply Chain Security for GitOps
 Software supply chain security doesn't stop at the application layer. Kusari Inspector can help secure your infrastructure-as-code, too. July 16, 2025 Ben Cotton](https://www.kusari.dev/blog/supply-chain-security-for-gitops)
[
Addressing the Challenges of Cloud-Native Application Security
 Kusari's software supply chain expertise gives you the ability to overcome the challenges in securing your cloud-native applications. July 23, 2025 Ben Cotton](https://www.kusari.dev/blog/addressing-the-challenges-of-cloud-native-application-security)
[
What Security Leaders Need to Know about America's AI Action Plan
 Here's what the new report from the White House means for software supply chain leaders, and how you can get ahead. July 30, 2025 Tim Miller](https://www.kusari.dev/blog/what-security-leaders-need-to-know-about-americas-ai-action-plan)
[
Celebrating OpenSSF's Anniversary
 Kusari celebrates the past, present, and future of the Open Source Security Foundation. August 6, 2025 Ben Cotton](https://www.kusari.dev/blog/celebrating-openssfs-anniversary)
[
Using Kusari to Manage your Open Source Dependencies
 Companies need to pay attention to the security of their open source dependencies. Kusari Platform can help. August 13, 2025 Tim Miller](https://www.kusari.dev/blog/using-kusari-platform-to-manage-your-open-source-dependencies)
[
Securing Medical Devices: Cyber Threats, SBOMs, and FDA Premarket Readiness
 How Medical Devices Can Comply with Section 524B to Meet FDA Cybersecurity Requirements September 17, 2025 Tim Miller](https://www.kusari.dev/blog/securing-medical-devices-cyber-threats-sboms-and-fda-premarket-readiness)
[
Understanding the Proposed CISA 2025 SBOM Minimum Elements
 CISA has proposed updates to the SBOM Minimum Elements. What does this mean for business leaders and engineers? September 23, 2025 Michael Lieberman](https://www.kusari.dev/blog/understanding-the-proposed-cisa-2025-sbom-minimum-elements)
[
Securing Yesterday's Medical Devices against Cyber Threats: Addressing Legacy MedTech
 Medical devices often far outlast their support period. How can these reliable devices avoid becoming a security liability? September 25, 2025 Tim Miller](https://www.kusari.dev/blog/securing-yesterdays-medical-devices-against-cyber-threats-addressing-legacy-medtech)
[
Best SBOM Tools 2025: How to Choose the Right SBOM Generation Tool
 Compare the best SBOM tools for 2025. Expert analysis of cdxgen, Syft, npm-sbom & more. Choose the right SBOM generator for your needs. October 1, 2025 Michael Lieberman](https://www.kusari.dev/blog/best-sbom-tools-2025)
[
Updating Legacy Medical Applications for Modern Security Requirements
 You can prepare yourself for future updates by bringing your post-market applications into a modern security paradigm. October 8, 2025 Tim Miller](https://www.kusari.dev/blog/updating-legacy-medical-applications-for-modern-security-requirements)
[
It Takes More Than AI to Deliver Code Faster
 Large language models write code quickly, but to get value to your customers, you need better security processes. October 15, 2025 Ben Cotton](https://www.kusari.dev/blog/it-takes-more-than-ai-to-deliver-code-faster)
[
The Top 10 To-Dos for CRA Compliance Right Now
 A strategic guide for CISOs and software security leaders October 22, 2025 Michael Lieberman](https://www.kusari.dev/blog/top-10-cra-compliance)
[
Breaking the "Department of No" - Ship Fast, but also Secure
 Security shouldn't slow you down. Kusari and Cloudsmith enable faster, safer releases by turning noisy CVE scans into actionable insight and enforcing policy from build to deploy. Go fast and secure. November 6, 2025 Ben Cotton Nigel Douglas](https://www.kusari.dev/blog/breaking-the-department-of-no-ship-fast-but-also-secure)
[
Integrating GitLab and Kusari
 Use Kusari's tools directly in GitLab workflows to improve your supply chain security. November 11, 2025 Parth Patel](https://www.kusari.dev/blog/integrating-gitlab-and-kusari)
[
2026 Predictions: Open Source Accountability, AI Security, and Standardization Will Define the Next Era of Software
 For years, software security has lived in the realm of best practices. In 2026, software security stops being theoretical and moves firmly into the realm of requirements. January 20, 2026 Michael Lieberman](https://www.kusari.dev/blog/2026-predictions-why-open-source-accountability-ai-security-and-standardization-will-define-the-next-era-of-software)
[
Compliance Is Getting Real
 Why software integrity is becoming the defining security challenge of the next decade January 27, 2026 Tim Miller](https://www.kusari.dev/blog/compliance-is-getting-real)
[
The Hidden Cost of Reactive AppSec
 Security leaders often talk about risk reduction. Developers talk about velocity. The tension between the two has defined AppSec for over a decade. February 18, 2026 Tim Miller](https://www.kusari.dev/blog/the-hidden-cost-of-reactive-appsec)
[
Why the EU Cyber Resilience Act Will Catch US Software Companies Off Guard
 Most US software regulations are built around intent. The EU Cyber Resilience Act (CRA) is built around outcomes. That difference is why 2026 will feel like a shock for many US companies selling softw February 19, 2026 Michael Lieberman](https://www.kusari.dev/blog/why-the-eu-cyber-resilience-act-will-catch-us-software-companies-off-guard)
[
The 95% Problem: Why Transitive Dependencies Are Your Biggest Software Supply Chain Blind Spot in 2026
 Your security team just finished a vulnerability scan. The dashboard looks clean, but there's a catch: that scan only covered about 5% of your actual risk surface. March 4, 2026 Tim Miller](https://www.kusari.dev/blog/why-transitive-dependencies-biggest-software-supply-chain-blind-spot-2026)
[
AI Coding Assistants in 2026: 4× Faster, 10× Riskier and The Hidden Security Cost
 AI coding assistants (LLMs) dramatically increase developer velocity, but introduce critical new AppSec risks. AI-generated code is consistently less secure. March 18, 2026 Michael Lieberman](https://www.kusari.dev/blog/ai-coding-assistants-in-2026-4x-faster-10x-riskier-the-hidden-security-cost)
[
Kusari and CNCF: Advancing Software Supply Chain Security for Cloud Native Projects
 March 23, 2026 Michael Lieberman](https://www.kusari.dev/blog/kusari-and-cncf-advancing-software-supply-chain-security-for-cloud-native-projects)
[
Kusari Partners with OpenSSF to Strengthen Open Source Software Supply Chain Security
 Open source software powers the modern world; securing it remains a shared responsibility. March 23, 2026 Michael Lieberman](https://www.kusari.dev/blog/kusari-partners-with-openssf-to-strengthen-open-source-software-supply-chain-security)
[
Vibe Coding & Vulnerabilities: A Security Team's Guide to AI-Generated Code Risks
 March 30, 2026 Michael Lieberman](https://www.kusari.dev/blog/vibe-coding-is-shipping-vulnerabilities-a-security-teams-guide-to-ai-generated-code-risks)
[
How Kusari Protects Against Recent Supply Chain Attacks
 Recent attacks against projects like Trivy, LiteLLM, and Axios show the need for automated supply chain checks. April 2, 2026 Ben Cotton](https://www.kusari.dev/blog/how-kusari-protects-against-recent-supply-chain-attacks)
[
Why 72% of Organizations Can't See Their Real Attack Surface: Solving the Transitive Dependency Visibility Gap
 Most security leaders think they have a handle on their attack surface, using SCA, SBOMs, tracking libraries. But there's a problem with that confidence. April 9, 2026 Tim Miller](https://www.kusari.dev/blog/why-72-of-organizations-cant-see-their-real-attack-surface-solving-the-transitive-dependency-visibility-gap)
[
Facts and Mythos: understanding the future of AI security analysis
 Mythos undoubtedly represents an advancement in the capability of frontier models. It's also not the apocalypse. April 13, 2026 Michael Lieberman Ben Cotton](https://www.kusari.dev/blog/facts-and-mythos)
[
Software Is a Supply Chain — Start Treating It Like One
 Modern software delivery now resembles global manufacturing. If we demand traceability for physical components, we must demand the same for code. April 14, 2026 Michael Lieberman Gaurav Saxena](https://www.kusari.dev/blog/software-is-a-supply-chain-start-treating-it-like-one)
[
Identity, Signing, and Transparency: The Foundation of Verifiable Builds
 Signing artifacts is not new. Making that signing keyless, auditable, and transparently verifiable is. April 20, 2026 Michael Lieberman Gaurav Saxena](https://www.kusari.dev/blog/identity-signing-and-transparency-the-foundation-of-verifiable-builds)
[
From Provenance to Enforcement: SLSA, in-toto, and Kubernetes Admission Control
 If provenance is not evaluated, it is merely metadata. Enforcement is what transforms integrity into control. April 27, 2026 Michael Lieberman Gaurav Saxena](https://www.kusari.dev/blog/from-provenance-to-enforcement-slsa-in-toto-and-kubernetes-admission-control)
[
kusari-cli gives you Kusari's power wherever you go
 The kusari-cli 1.0 release means you can connect to Kusari Inspector and Kusari Platform no matter what platform you use. April 30, 2026 Ben Cotton](https://www.kusari.dev/blog/kusari-cli-1-0)
[
Kusari Platform now tells you which vulnerabilities can actually be exploited — and writes the VEX
 Most CVEs can't actually be reached by your code. Kusari's new AI Analysis Agent reads your codebase and traces each vulnerability so you can fix what matters and prove what doesn't. May 5, 2026 Parth Patel](https://www.kusari.dev/blog/improving-vulnerability-reachability-and-exploitability-analysis)
No other
articles available.
Previous
Next
1 / 3
Previous
[
Why the EU Cyber Resilience Act Will Catch US Software Companies Off Guard
 Most US software regulations are built around intent. The EU Cyber Resilience Act (CRA) is built around outcomes. That difference is why 2026 will feel like a shock for many US companies selling softw February 19, 2026 Michael Lieberman](https://www.kusari.dev/blog/why-the-eu-cyber-resilience-act-will-catch-us-software-companies-off-guard)
Next
[
AI Coding Assistants in 2026: 4× Faster, 10× Riskier and The Hidden Security Cost
 AI coding assistants (LLMs) dramatically increase developer velocity, but introduce critical new AppSec risks. AI-generated code is consistently less secure. March 18, 2026 Michael Lieberman](https://www.kusari.dev/blog/ai-coding-assistants-in-2026-4x-faster-10x-riskier-the-hidden-security-cost)
Want to learn more about Kusari?
Schedule a Demo
Sign up for our newsletter
Monthly updates from the intersection of software supply chain, open source and security
Kusari is committed to protecting and respecting your privacy. We may use the information you provide to contact you about our products and services. Check out our Privacy Policy. You may unsubscribe at any time.
Email*
headline_variant
headline_text Subscribe 
About Kusari Resources Contact Careers Company Logos  
© 2025 Kusari Inc. All rights reserved.
Terms
Privacy
Cookies
By clicking “Accept”, you agree to the storing of cookies on your device to enhance site navigation, analyze site usage, and assist in our marketing efforts. View our Privacy Policy for more information.
Preferences Deny Accept
Privacy Preference Center
When you visit websites, they may store or retrieve data in your browser. This storage is often necessary for the basic functionality of the website. The storage may be used for marketing, analytics, and personalization of the site, such as storing your preferences. Privacy is important to us, so you have the option of disabling certain types of storage that may not be necessary for the basic functioning of the website. Blocking categories may impact your experience on the website.
Reject all cookies Allow all cookies
Manage Consent Preferences by Category
Essential
Always Active
These items are required to enable basic website functionality.
Marketing [-]
Essential
These items are used to deliver advertising that is more relevant to you and your interests. They may also be used to limit the number of times you see an advertisement and measure the effectiveness of advertising campaigns. Advertising networks usually place them with the website operator's permission.
Personalization [-]
Essential
These items allow the website to remember choices you make (such as your user name, language, or the region you are in) and provide enhanced, more personal features. For example, a website may provide you with local weather reports or traffic news by storing data about your current location.
Analytics [-]
Essential
These items help the website operator understand how its website performs, how visitors interact with the site, and whether there may be technical issues. This storage type usually doesn't collect information that identifies a visitor.
Confirm my preferences and close Submit
