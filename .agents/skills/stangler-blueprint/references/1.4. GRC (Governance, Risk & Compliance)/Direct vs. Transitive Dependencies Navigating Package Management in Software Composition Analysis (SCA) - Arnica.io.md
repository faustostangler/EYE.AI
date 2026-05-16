---
name: Direct vs. Transitive Dependencies: Navigating Package Management in Software Composition Analysis (SCA) - Arnica.io
keywords: (placeholder)
metadata:
  url: https://www.arnica.io/blog/direct-vs-transitive-dependencies-navigating-package-management-in-software-composition-analysis-sca
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T23:03:23.186Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
Direct vs. Transitive Dependencies: Navigating Package Management in Software Composition Analysis (SCA) 
Product
Solutions
Arnie AI
AI SAST
Agentic Rules Enforcer
Pipelineless Security
Security Champions
Application Security Posture Management
Developer-Native Security Workflows
Container Image Mapping & Scanning
Al-Assisted & Automated Mitigation
Compliance & Security Reporting
USe Cases
Hardcoded Secrets
SCA
SAST
IaC
Package Reputation
SBOM
Integrations
Source Code Management
ChatOps
Issue Management
AI
Benefits
For DevOps
For Security
For Developers
For HealthTech
For FinTech
Resources
Resources
Customer Stories How Arnica customers built their own world class security programs.
Announcements New features, partnerships, updates, and more.
Press Read about Arnica in the news and media.
Blog The most pressing issues in application security.
Docs Arnica product and technical documentation.
Featured
Meet Arnie: Your AI Code Protector
No items found.
Company
Company
About Who is Arnica?
Careers Join the team!
Contact The Arnica team wants to hear from you
Security Explore our security best practices
Pricing
Log In 
Get Started 
Talk to Arnica 
Blog
|
APPSEC
Featured
Direct vs. Transitive Dependencies: Navigating Package Management in Software Composition Analysis (SCA)
By
Anna Daugherty
February 25, 2025
•
9 mins
Share this post 
Understanding Direct & Transitive Dependencies in Software Development
Modern software development often relies heavily on third-party packages to accelerate development and introduce powerful features. When incorporating these packages, developers typically declare the ones they intend to use directly in their source code—these are known as direct dependencies. However, those direct dependencies often rely on additional packages, bringing in a chain of transitive dependencies.
This dynamic introduces a cascading effect where not only third-party code but also "fourth-party" and even "nth-party" code becomes part of your software. These transitive dependencies, while crucial for functionality, are not explicitly declared, making them harder to track and manage. Without visibility into the full dependency tree, risks such as outdated or vulnerable packages can go unnoticed, potentially compromising the software's security and integrity.
To address these challenges, Software Composition Analysis (SCA) tools (such as Arnica) play a vital role in mapping the complete dependency graph. This holistic view helps developers identify risks, understand their origins, and implement mitigation strategies effectively. Recognizing the impact of both direct and transitive dependencies is the first step toward mastering secure and efficient software development practices.
Dependencies in Software Development
Let's start with establishing clear definitions of direct and transitive dependencies:
Direct Dependencies
In package management, a direct dependency is a library or package that a project explicitly depends on and has directly listed in its configuration file (such as package.json in Node.js, requirements.txt in Python, or pom.xml in Maven for Java). These are packages that the project needs to function and that developers intentionally add to meet specific requirements.
Direct dependencies are the packages that developers intentionally choose to add to the project.
Direct dependencies may have their own dependencies, which are referred to as transitive dependencies or indirect dependencies.
In package management, direct dependencies are often automatically installed along with their transitive dependencies, but only direct dependencies are explicitly specified in the configuration.
Transitive Dependencies
In package management, a transitive dependency (also called an indirect dependency) is a package that a project depends on indirectly. These dependencies are not directly listed by the project but are dependencies of the project's direct dependencies. In other words, if a package that your project depends on has its own dependencies, those are considered transitive dependencies.
Transitive dependencies are automatically installed and managed by the package manager along with direct dependencies.
Transitive dependencies can create compatibility issues or dependency conflicts, especially when multiple direct dependencies require different versions of the same transitive dependency.
Transitive dependencies can sometimes lead to dependency hell if not managed properly, especially in large projects with many dependencies.
Key Differences Between Direct and Transitive Dependencies
Visibility and Control
Direct Dependencies are specified directly in configuration files, such as package.json, requirements.txt, or pom.xml, making it visible and easy to track. The developer has direct control over the chosen package and version of the dependency and can update, add, or remove it as needed.
Transitive Dependencies are not specified in the configuration files of the main project but are automatically installed as a requirement of a direct dependency. They may be less visible and harder to track. A transitive dependency is managed by the package manager, not directly controlled by the developer. Changes are often based on the version requirements set by direct dependencies.
Locked Files and Dependencies
A locked file in software development is a file that records the exact versions of all dependencies (both direct and transitive) used in a project at a specific point in time. It acts as a snapshot of the dependency graph, ensuring that the project builds consistently with the same versions across different environments.
Locked versions reduce some risks in the software supply chain by minimizing unexpected updates that could introduce vulnerabilities. However, locked dependencies might still contain older vulnerabilities if newer versions addressing them are not updated.
Ecosystems with locked files (e.g., package-lock.json in npm) provide visibility into the entire dependency graph, including transitive dependencies, making it easier to track and audit what is being installed.
In development ecosystems without locked files (e.g., Java's pom.xml), transitive dependencies are not explicitly listed, which can make managing and auditing dependencies more challenging.
Package Risk Exposure
Package risk exposure refers to the vulnerabilities that may arise from the use of both direct and transitive dependencies. Both direct and transitive dependencies can expose a system to risks, including security vulnerabilities and potential exploits.
For example, consider a scenario where a project uses a JSON parser indirectly through another package. Even though the parser is not directly declared in the project's dependency list, it is still included in the build process as a transitive dependency. If a security vulnerability (e.g., a CVE) exists in the JSON parser, the project is exposed to that risk regardless of its direct dependency list. Simply omitting a direct declaration does not shield a project from the risks posed by its full dependency tree.
This issue is exacerbated by the fact that many tools fail to provide full visibility into transitive dependencies and their associated vulnerabilities. While tools might effectively flag risks in direct dependencies, they often fall short in identifying and analyzing risks that arise deeper within the dependency graph. This lack of insight leaves developers and organizations potentially unaware of critical security gaps in their software supply chain.
Dependency Management Complexity in Software Projects
Dependency management is a critical yet challenging aspect of modern software development. Managing both direct and transitive dependencies introduces layers of complexity that can significantly impact the stability, security, and maintainability of a software project.
Direct Dependencies are relatively easier to handle since the developer has explicit control over them. By specifying compatible versions in the configuration file, conflicts are usually manageable, and modifications can be made directly. However, this simplicity doesn't extend to transitive dependencies, which are introduced indirectly through other dependencies. These dependencies are often prone to conflicts, such as when different direct dependencies require different versions of the same package, a scenario commonly referred to as " dependency hell."
The situation becomes even more intricate with internal packages, which many organizations use to standardize and secure their dependency ecosystems. Internal packages are typically maintained by dedicated teams and shared across the organization.
While this approach improves governance, it adds complexity when vulnerabilities are discovered. Developers relying on these packages cannot directly resolve vulnerabilities and must wait for the internal team responsible for the package to provide an updated, secure version. This division of responsibility can lead to delays in addressing critical issues.
Another layer of complexity arises from the way some ecosystems, like npm, handle transitive dependencies. It is possible for the same transitive dependency to exist in multiple versions within a single dependency tree. For example, one path may include version X of a package with certain vulnerabilities, while another path includes version X+2 with a different set of vulnerabilities.
Resolving these issues often requires navigating the intricate dependency tree to ensure that updates address all vulnerabilities across all paths, which may not be possible with a single fix. In such cases, even direct interventions by developers may only partially resolve the problem, leaving some vulnerabilities unaddressed.
Strategies for Managing Direct Dependencies
Version Control
Effective management of direct dependencies is crucial for maintaining software security, stability, and reproducibility. Here are some strategies to ensure proper version control and dependency management:
Specify Dependency Versions Explicitly: Always specify the version of every direct dependency in your project's configuration file. In some languages, like Python, not specifying a version will result in the latest version being downloaded by default. However, relying on the latest version can introduce new security risks or break functionality if an update is incompatible. Explicit versioning ensures predictable behavior and reduces the risk of unexpected changes.
Adopt Approved Versions: Establish a system to define and enforce approved versions of dependencies. Tools like Nexus or JFrog Artifactory can help manage approved artifacts within an organization. These systems allow developers to use only pre-approved versions of dependencies, reducing the risk of introducing vulnerabilities or incompatible updates into the project.
Leverage Version Ranges Judiciously: When specifying dependency versions, use fixed versions (1.2.3) rather than broad version ranges (>=1.0.0). Fixed versions offer greater control, while ranges may inadvertently allow updates that introduce breaking changes or vulnerabilities.
Audit and Update Regularly: Regularly audit direct dependencies to ensure they are secure and up-to-date. Tools like Dependabot or Renovate can automate this process by notifying developers of new versions and potential vulnerabilities in dependencies.
Centralized Artifact Management: By using artifact management systems, organizations can maintain a centralized repository of approved and tested dependency versions. This approach ensures consistency across projects and helps enforce compliance with security and quality standards.
Lock Dependencies Where Possible: Generate and maintain lock files for environments where direct dependencies include transitive dependencies. Lock files ensure that the same versions are used across development, testing, and production environments, reducing inconsistencies and related issues.
License Compliance
Ensuring license compliance in software development is critical to avoid legal and operational risks, especially when using open-source packages. Since licenses dictate how software can be used, distributed, or modified, managing them effectively requires a proactive and structured approach.
It is unclear what the legal action would be if a direct package is permissive and a transitive package is restricted. We prebuilt default rules in Arnica that align to Google's Open Source standards in order to help answer questions like this: https://opensource.google/documentation/reference/thirdparty/licenses#types
Simplify Dependency Management by Using Internal Packages
Simplifying dependency management using internal packages involves centralizing and standardizing the dependencies used across an organization. Internal packages are pre-approved, curated versions of open-source or proprietary dependencies that are maintained within the organization. By creating and using these packages, teams can ensure consistency, reduce the risk of introducing unverified or vulnerable components, and simplify the resolution of dependency conflicts.
Developers can rely on these pre-validated packages without needing to individually assess their security, license compliance, or compatibility. Tools like private repositories (e.g., Nexus, JFrog Artifactory) streamline this process by hosting these internal packages, enforcing version control, and providing centralized governance. This approach minimizes dependency-related risks while improving maintainability and ensuring alignment with organizational policies.
Understanding Limitations to Managing Transitive Dependencies
Direct Package Updates May Not Fix Transitive Vulnerabilities
Updating a direct package does not always resolve vulnerabilities present in transitive dependencies. This limitation arises because direct fixes are constrained to the package that developers can control directly, while transitive dependencies—indirectly introduced by those packages—often remain untouched.
In many cases, even updating a direct package to its latest version may not address vulnerabilities deep in the dependency tree. This is particularly true if the transitive dependency in question is less actively maintained. A less maintained package might not utilize the latest versions of its own dependencies, leaving vulnerabilities unpatched. As a result, no matter how current the direct package is, its reliance on outdated or vulnerable transitive dependencies perpetuates the risk.
Dependency management tools often provide fixes by analyzing paths in the dependency graph, identifying problematic versions. However, resolving vulnerabilities at deeper levels of the tree is challenging, especially when the transitive dependency lacks active maintenance or when all versions of the direct package rely on the same problematic transitive dependency. Upgrading the direct package may mitigate some issues, but it rarely addresses every vulnerability throughout the entire dependency graph.
Reachability of Transitive Vulnerabilities
Transitive vulnerabilities can pose significant risks because they may be directly reachable by your source code, even if they are not explicitly declared as direct dependencies. When you include a dependency in your project, you inherently pull in all its transitive dependencies. These packages become accessible in your codebase, and vulnerabilities within them can potentially be exploited if they are used in your application.
For instance, consider a scenario where your project depends on a server library, which in turn relies on a JSON parser. Although the JSON parser is a transitive dependency and not explicitly listed in your package file, your source code might use it directly. This creates a scenario where a vulnerability in the JSON parser is reachable and exploitable through your application, despite not being a direct dependency.
This issue highlights the importance of understanding the full dependency tree. Tools like Arnica address this by building a comprehensive map of your project's dependencies, marking specific transitive packages that are embedded and reachable in your source code. This visibility is crucial for identifying and mitigating security risks effectively.
Leveraging Software Composition Analysis to Address Package Vulnerabilities
Software Composition Analysis (SCA) is a critical practice for identifying and mitigating vulnerabilities in open-source dependencies. By implementing automated tools and strategies, organizations can ensure a more secure and efficient approach to dependency management. Below are some key strategies to leverage SCA effectively:
Implement Automated Real-Time Scans
Automated real-time scanning ensures that vulnerabilities in both direct and transitive dependencies are identified promptly. Integrating these scans into CI/CD workflows allows developers to detect and address vulnerabilities early in the development process. This proactive approach minimizes the risk of introducing exploitable vulnerabilities into production environments.
Leverage Developer-Friendly Workflows for SCA Vulnerability Mitigation
For SCA to be effective, it must integrate seamlessly with developer workflows. Arnica enhances Software Composition Analysis (SCA) vulnerability mitigation by integrating seamlessly into developer workflows in places like Slack and Jira with real-time scanning and feedback, thereby promoting efficient and effective security practices.
Arnica offers developers multiple options to address vulnerabilities, such as patching, upgrading, or rebuilding the dependency tree. This flexibility allows developers to choose the most suitable remediation strategy for their specific context, balancing security needs with development priorities.
Effective Prioritization of Vulnerabilities
Not all vulnerabilities pose the same level of risk. Effective prioritization requires considering additional factors beyond traditional metrics like CVSS (Common Vulnerability Scoring System) from NIST. Modern prioritization methods incorporate:
EPSS (Exploit Prediction Scoring System): This metric predicts the likelihood of a vulnerability being exploited in the wild, enabling teams to focus on high-risk vulnerabilities. Daily updates to EPSS provide real-time threat intelligence, ensuring relevance.
Reachability: Assessing whether a vulnerability is reachable in the context of your application is crucial. Tools should not only highlight reachable vulnerabilities but also identify what is definitively not reachable, reducing noise and allowing teams to concentrate on actionable risks.
Dependency Depth: Vulnerabilities closer to your direct dependencies generally pose a higher risk than those buried deep in the dependency tree. Prioritizing issues based on depth helps allocate resources effectively.
Focus on Noise Reduction
A significant challenge in SCA is managing the volume of reported vulnerabilities. While identifying reachable vulnerabilities is essential, reducing noise by confirming non-reachable vulnerabilities is equally critical. This approach ensures that security teams can focus on addressing the most pressing threats without being overwhelmed by low-risk or irrelevant findings.
Enforce Security Gates with SCA
Enforcing security gates with Software Composition Analysis (SCA) ensures that vulnerabilities are identified and mitigated early in the development process, reducing the burden of addressing issues after they reach production. The key to effective security gate implementation is making them contextual, actionable, and aligned with development workflows.
Contextual Security Gates
Security gates should be tailored to the type and urgency of the vulnerabilities. For example, if the priority is to "stop the bleeding," security checks can be implemented directly on pull requests (PRs). This ensures that vulnerabilities are addressed promptly, as they are flagged while developers are actively working on the code. Policies can vary in strictness, ranging from blocking PR merges for critical vulnerabilities to simply notifying developers about issues that need attention.
Integrate Security Fixes Into Existing Workflows
To ensure vulnerabilities are fixed effectively, it is important to embed security actions into developers' everyday workflows. For instance, instead of creating a new pull request to update a vulnerable package, which developers might overlook, security fixes can be suggested within existing PRs. By adding comments or recommendations directly in active PRs, developers are more likely to prioritize these fixes as part of their ongoing work, rather than treating them as separate tasks.
Improve Developer Engagement and Accountability
Security gates can be designed to engage developers more effectively by providing actionable insights and incorporating fixes into their measured workstreams. For instance, by tying remediation efforts to active PRs, developers are more likely to resolve vulnerabilities as part of their regular tasks, fostering a security-first mindset without introducing friction.
Master Dependency Management With Software Composition Analysis
Dependency management is a cornerstone of modern software development, yet its complexity grows with the increasing reliance on open-source components and intricate dependency graphs.
Effective SCA enables visibility into direct and transitive dependencies, helping developers identify and mitigate vulnerabilities early. Automating real-time scans, embedding security gates into developer workflows, and enforcing contextual policies allow organizations to address risks proactively without disrupting development.
Tools like Arnica empower teams with actionable insights, prioritizing vulnerabilities based on metrics such as reachability, EPSS, and dependency depth, ensuring that remediation efforts focus on the most critical issues.
At the same time, integrating fixes into existing workflows, prioritizing vulnerabilities based on real-world exploitability, and reducing noise through intelligent reachability analysis ensure that security becomes a collaborative effort, not an afterthought.
Scan your dependencies for free with Arnica's SCA tools at app.arnica.io
Share this post
Recommended posts
View all blog posts
[ APPSEC Featured
Building AWS Zero Trust Architecture for Continuous Application Security Validation
May 13, 2026](https://www.arnica.io/blog/aws-zero-trust-architecture-application-security)
[ APPSEC Featured
Implementing the AWS Shared Responsibility Model for DevSecOps Teams Managing Application Security
May 12, 2026](https://www.arnica.io/blog/aws-shared-responsibility-model-devsecops)
[ APPSEC Featured
How to Generate a Software Bill of Materials From Your Repositories Without Slowing CI
March 18, 2026](https://www.arnica.io/blog/generate-sbom-from-repositories-without-slowing-ci)
View all
Reduce Risk and Accelerate Velocity
Integrate Arnica ChatOps with your development workflow to eliminate risks before they ever reach production.
Try Arnica  
Anna Daugherty
Senior PMM
Connect with Simon:
Subscribe to our newsletter
Subscribe to our newsletter to receive the latest content and updates from Arnica. Subscribe
By subscribing you agree to with our Privacy Policy
Thank you! Your submission has been received!
Oops! Something went wrong while submitting the form.
Solutions
Arnie AI AI SAST Agentic Rules Enforcer Pipelineless Security Security Champions Application Security Posture Management (ASPM) Developer-Native Security Workflows Container Image Mapping & Scanning Al-Assisted & Automated Mitigation Compliance & Security Reporting
Integrations
Source Code Management ChatOps Issue Management Artificial Intelligence
Benefits
Arnica for DevOps Arnica for Security Arnica for Developers Arnica for HealthTech Arnica for FinTech
Resources
Blog Announcements Press Docs
Company
About Careers Security Contact
© 2026 Arnica, Inc. All rights reserved.
Privacy Policy Terms of Use Status    
