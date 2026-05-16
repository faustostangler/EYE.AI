---
name: What is dependency scanning in cloud security? - Wiz
keywords: (placeholder)
metadata:
  url: https://www.wiz.io/academy/vulnerability-management/dependency-scanning-in-cloud-security
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T23:03:23.186Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
What is dependency scanning in cloud security? | Wiz
Sign in
Experiencing an incident?
Wiz
Pricing Get a demo
Platform
Solutions
Pricing
Resources
Customers
Company
Get a demo
All articles Vulnerability Management
What is dependency scanning in cloud security?
Wiz Experts Team
December 26, 2025
| 10 minute read
Vulnerability Management Buyer's Guide Watch 5-min demo    
Key takeaways
Dependency scanning is an automated process that identifies security vulnerabilities and license issues in third-party libraries and packages used by your applications.
In cloud-native environments, this practice is critical because a single vulnerable component in a container or serverless function can compromise hundreds of microservices.
Effective scanning integrates into the entire development lifecycle, from the IDE and CI/CD pipelines to container registries and runtime environments.
Context is essential for prioritization, as teams need to distinguish between theoretical risks and vulnerabilities that are actually reachable and exploitable in their specific cloud configuration.
What is dependency scanning?
Dependency scanning is the automated analysis of the third-party libraries, frameworks, and packages that developers use to build applications. Instead of reviewing the code you write, it inspects the external open-source and commercial components you import to find known security risks. This process is often referred to as software composition analysis (SCA).
This scanning identifies known vulnerabilities, cataloged as Common Vulnerabilities and Exposures (CVEs), in both direct and transitive dependencies.
Direct dependencies: These are the libraries you explicitly list in your project's manifest file.
Transitive dependencies: These are the libraries that your direct dependencies rely on to function, often pulling in a deep tree of extra code.
A dependency checker works by reading manifest files like package.json , pom.xml , or requirements.txt . It compares the versions listed in these files against comprehensive vulnerability databases such as the National Vulnerability Database (NVD) or the GitHub Advisory Database.
Scanning can occur at multiple stages of the software lifecycle to catch issues early and often:
Development: Tools run in the Integrated Development Environment (IDE) as code is written.
Build: Scanners check code during the commit process or within CI/CD pipelines.
Runtime: Advanced tools analyze running applications to see what is actually loaded in memory.
It is important to distinguish dependency scanning from other testing methods. Static Application Security Testing (SAST) scans your proprietary source code for flaws, while Dynamic Application Security Testing (DAST) tests running applications for external vulnerabilities. Dependency scanning specifically targets the supply chain of pre-built code you consume.
Vulnerability Management Buyer's Guide
This buyers guide will not only help you objectively choose or replace a vulnerability management solution, but also provide insights on how your organization can work together to own the responsibility of security as one team.
Your work email here
Download 
Why dependency scanning matters in cloud-native environments
Modern applications rely heavily on open-source components, with a typical application containing hundreds or even thousands of external dependencies. This reliance means that the majority of the code in your production environment was likely written by someone outside your organization.
Cloud-native architectures, such as containers, microservices, and serverless functions, amplify the risks associated with these dependencies.
Ephemeral workloads: Vulnerable code can be deployed rapidly across infrastructure in short-lived containers, making it hard to track without automation.
Container images: A container image bundles dependencies together, meaning a single vulnerable image can be replicated instantly across thousands of pods.
Shared base images: If a base image contains a vulnerability, that flaw propagates to every application that builds upon it.
Supply chain attacks have demonstrated the severity of these risks. High-profile incidents like Log4Shell (CVE-2021-44228) in December 2021 and attacks involving malicious npm packages exploited the trust organizations place in external code.
Supply chain attacks exploit the trust organizations place in external code through multiple vectors:
Typosquatting attacks
Attackers publish packages with names similar to popular libraries (e.g., "reqeusts" instead of "requests")
Developers accidentally install malicious packages due to typos
Dependency confusion
Attackers upload malicious packages to public registries using internal package names
Build systems prioritize public packages over private ones due to misconfiguration
Malicious maintainer takeovers
Attackers compromise maintainer accounts or convince maintainers to transfer ownership
Legitimate packages are updated with malicious code
Malicious post-install scripts
Packages execute arbitrary code during installation via lifecycle hooks
Scripts can exfiltrate credentials, install backdoors, or mine cryptocurrency
Known vulnerability exploitation
Attackers scan public repositories for applications using vulnerable dependencies
Log4Shell (CVE-2021-44228) was exploited within hours of public disclosure
Automated scanning makes it trivial to find targets at scale
Public sector directives and industry guidance increasingly emphasize software supply chain security. Executive Order 14028 (issued May 2021) and NIST Secure Software Development Framework (SSDF) drive SBOM adoption for U.S. federal agencies and their software suppliers. Many enterprises are adding SBOM requirements to procurement processes for critical infrastructure and regulated workloads.
Failing to secure dependencies can lead to severe business impacts:
Data breaches: Attackers can exploit known vulnerabilities to access sensitive customer data.
Service disruptions: Malicious packages can contain cryptominers or code that crashes applications.
Regulatory penalties: Non-compliance with data protection laws can result in significant fines.
Reputational damage: Trust is lost when customers learn their data was exposed via a known vulnerability.
wiz academy
[
What is SBOM scanning?
An SBOM contains an inventory of all software components, libraries, dependencies, versions, licenses, and relationships.](https://www.wiz.io/academy/sbom-scanning)
Read more 
How dependency scanning works
Dependency scanning generally follows a structured four-stage process to identify and report risks.
Discovery: The scanner identifies dependency manifest files within your code repositories or container images.
Inventory: The tool parses these files to build a complete dependency graph, mapping out every direct and transitive library.
Matching: The scanner compares the discovered inventory against vulnerability databases to find matches for specific versions.
Reporting: The tool generates a report detailing findings, severity ratings, affected versions, and guidance on how to remediate the issues.
Scanners use different techniques depending on the target. Static manifest parsing reads configuration files, while container image layer analysis inspects compiled dependencies within Docker images. Runtime scanning adds precision by identifying libraries that are actually loaded and executing in production environments, complementing static manifest analysis and image-layer scanning.
For accurate software dependency analysis, keeping vulnerability databases current is crucial. Security researchers discover new vulnerabilities daily, so scanners must sync frequently with sources to detect the latest threats. While most tools use signature-based detection, some modern solutions also employ behavior-based detection to identify malicious activity that hasn't yet been cataloged as a CVE.
wiz academy
[
What is container image scanning?
Container image scanning is the automated process of analyzing container images for security vulnerabilities, misconfigurations, and compliance violations.](https://www.wiz.io/academy/container-image-scanning)
Read more 
Types of dependencies and scanning approaches
Different programming languages and infrastructure components require specific scanning approaches to be effective.
Language-specific package ecosystems
Each programming language uses its own package manager and manifest file format, which dictates how dependencies are resolved and scanned.
Each ecosystem handles dependency resolution differently. For example, npm allows nested dependencies that can result in multiple versions of the same library, while Go attempts to flatten dependencies. Some languages have highly mature dependency scanning tools, while others may require more specialized configuration.
Container and cloud-native scanning
Scanning container images involves checking for vulnerabilities in both the base image layers and the application layers.
Base image layers: These contain Operating System (OS) packages installed via tools like apt or yum .
Application layers: These contain the language-specific libraries and code added on top of the OS.
Scanning both is vital because a vulnerability in a system library like openssl is just as dangerous as a flaw in a Python package.
In Kubernetes environments, teams commonly use admission controllers with policy engines (such as Open Policy Agent or Kyverno) to block vulnerable or non-compliant images from being deployed. Combine image scanning and cluster policy with runtime signals to focus on dependencies that are actually loaded and executing in production workloads. Serverless functions, such as AWS Lambda, also require scanning, as they bundle dependencies into the deployment package which can become outdated over time.
[
Watch 5-minute demo
Learn how Wiz Code scans IaC, containers, and pipelines to stop misconfigurations and vulnerabilities before they hit your cloud.](https://www.wiz.io/recorded-demo/code)
Watch now 
Integration with development workflows and CI/CD pipelines
The most effective security strategy is "shift-left," which means catching vulnerabilities early in the development process before they reach production.
You can integrate scanning at several key points in your workflow:
IDE plugins: These provide real-time feedback to developers as they write code and import new libraries.
Pre-commit hooks: These scripts block code commits if they introduce critical vulnerabilities.
Pull request scanning: Automated checks run on every pull request to ensure new code meets security standards before review.
CI/CD pipeline gates: Build pipelines can be configured to fail if high-severity issues are detected, preventing the creation of vulnerable artifacts. Use a single policy engine so IDE checks, pull request scans, pipeline gates, registry scans, and cluster admission decisions all follow the same severity thresholds and exception rules.
Registry scanning: Many container registries (such as Amazon ECR, Azure Container Registry, and Google Artifact Registry) offer built-in or integrated scanning to catch vulnerabilities in stored images, including those that haven't been redeployed recently.
Runtime monitoring: Continuous scanning of production workloads identifies risks in active applications.
Balancing security gates with developer velocity is a common challenge. If every low-severity finding blocks a deployment, developers may bypass security controls. It is important to establish clear policies regarding which severity levels trigger a block.
Automated dependency updates help maintain this balance. Tools can automatically create pull requests to update vulnerable libraries, allowing developers to merge fixes with a single click.
Risk prioritization and vulnerability management
A common pain point with OSS ** scanning** is alert fatigue, where teams are overwhelmed by hundreds of findings.
To manage this, you must prioritize risks based on context rather than just raw severity scores.
Severity scores: CVSS ratings provide a baseline but do not reflect your specific environment.
Exploitability: Check if the vulnerability has a known exploit in the wild, often referenced in the CISA KEV catalog.
Reachability: Determine if the vulnerable code is actually loaded and executed by your application.
Exposure: Identify if the vulnerable component is internet-facing or protected behind a firewall.
Data sensitivity: Prioritize applications that handle PII, PHI, or other critical business data.
Business criticality: Focus on production environments over staging or development sandboxes.
"Toxic combinations" occur when multiple risk factors align, such as a critical vulnerability in an internet-facing container with administrative privileges. Correlate vulnerabilities with network exposure, identity permissions, and data sensitivity to highlight realistic attack paths instead of isolated CVEs. These correlated risks represent immediate threats that require urgent attention.
Reachability vs. exploitability distinction
Reachability and exploitability are related but distinct risk factors:
Reachability: The vulnerable library is loaded into memory and the specific vulnerable function is called by your application code. Static analysis tools trace call graphs to determine reachability.
Exploitability: The vulnerability can be triggered by an attacker through available attack vectors (network requests, file uploads, API calls). A vulnerability may be reachable but not exploitable if inputs are sanitized or the code path requires privileged access.
True risk prioritization combines reachability with environmental context:
Network exposure (internet-facing vs. internal)
Identity permissions (what the workload can access)
Data sensitivity (PII, PHI, payment data)
Existing security controls (WAF rules, network segmentation)
For example, a critical SQL injection vulnerability in a reachable database library poses minimal risk if the application runs in a private subnet with no external network access and read-only database credentials.
Vulnerability management goes beyond simple detection. It involves the ongoing process of tracking, prioritizing, and resolving issues. A Software Bill of Materials (SBOM) is a key tool here, acting as a comprehensive inventory that allows you to quickly check for affected components when new vulnerabilities are disclosed.
Tap to unmute
Your browser can't play this video.
Learn more 
An error occurred.
Try watching this video on www.youtube.com, or enable JavaScript if it is disabled in your browser.
Implementation challenges and best practices
Implementing a robust scanning program comes with hurdles, but following best practices can ensure success.
Common challenges
Organizations often face specific obstacles when rolling out scanning tools.
False positives: Scanners may flag vulnerabilities in code paths that are never used.
Noise management: A high volume of low-severity findings can distract from critical issues.
Remediation complexity: Some dependencies may not have a patched version available, or an update might break the application.
Developer friction: Excessive security gates can slow down development and frustrate engineering teams.
Tool sprawl: Using multiple different scanners can lead to inconsistent results and data silos.
Transitive dependency hell: Indirect dependencies are often difficult to upgrade without breaking the direct dependency that requires them.
License compliance: Managing open-source licenses (such as GPL, Apache 2.0, MIT) is a parallel challenge to security scanning; license policy violations are common and require continuous monitoring to avoid legal and intellectual property risks.
wiz academy
[
What is cloud vulnerability scanning? Modern best practices
Cloud vulnerability scanning is the automated process of identifying security flaws within your cloud infrastructure, workloads, and configurations. Unlike traditional scanning designed for static, on-premises servers, cloud scanning is built to handle the dynamic nature of the cloud.](https://www.wiz.io/academy/cloud-vulnerability-scanning)
Read more 
Best practices for effective scanning
You can overcome these challenges by adopting a strategic approach to implementation.
Establish clear policies: Define exactly what severity thresholds require immediate action and what the response SLAs are.
Automate where possible: Use tools that automatically generate pull requests for dependency updates.
Prioritize ruthlessly: Focus your limited resources on exploitable, exposed vulnerabilities first.
Enable developers: Provide teams with the open source dependency scanner tools and context they need to fix issues independently.
Scan everywhere: Ensure coverage across repositories, CI/CD pipelines, registries, and runtime environments.
Maintain SBOM: Keep an accurate, up-to-date inventory of all software components.
Regular updates: Schedule regular cycles to refresh dependencies, even if no security issues are found.
Monitor continuously: Do not rely solely on build-time scans; monitor production for newly disclosed vulnerabilities.
Educate teams: Train developers on how to select secure dependencies and interpret scan results.
How Wiz transforms dependency scanning with cloud context
Wiz transforms software dependency analysis by moving beyond simple lists of vulnerabilities and providing deep cloud context.
Wiz Code offers native SCA capabilities across repositories with a unified policy engine, enabling consistent enforcement from code commit through container registries and into runtime environments. This is complemented by the Wiz Runtime Sensor, which supports reachability analysis to identify which dependencies are actually loaded and executing in production.
The Wiz Security Graph correlates dependency findings with cloud exposure (internet-facing workloads), identity permissions (IAM roles and service accounts), and data sensitivity (PII, PHI, payment data) to surface real attack paths and prioritize what matters.
Network exposure: Wiz identifies if the vulnerable workload is exposed to the internet.
Identity and permissions: The platform analyzes what cloud permissions the vulnerable workload possesses.
Data sensitivity: Wiz detects if the workload has access to sensitive data like PII or PHI.
Lateral movement paths: The graph shows how an attacker could use the vulnerability to move to other parts of the network.
Code-to-cloud correlation allows you to trace a vulnerable dependency in a running container back to its specific source repository and owner. This visibility enables streamlined workflows in common version control and CI platforms so the right person is notified immediately.
Wiz integrates into CI/CD pipelines to prevent risky dependencies from reaching production. It can block builds based on policy, and supports AI-assisted remediation that drafts pull requests with specific version updates and dependency changes, accelerating fixes while keeping developers in their existing workflows. This approach ensures teams focus on the best dependency scanning and management platform practices by prioritizing the small percentage of findings that represent actual attack paths.
Get a demo to see how Wiz can help you prioritize dependency risks with full cloud context.
Catch code risks before you deploy
Learn how Wiz Code scans IaC, containers, and pipelines to stop misconfigurations and vulnerabilities before they hit your cloud.
Work Email*
First Name*
Last Name*
Country
Phone Number*
Company* [-] false
Keep me updated about Wiz product releases, industry news, and events (You can unsubscribe at any time) [-] false
Subscribe me to the Wiz blog digest emails
Submit
For information about how Wiz handles your personal data, please see our Privacy Policy.
Your work email here
Get a demo 
FAQs about dependency scanning
Table of contents
What is dependency scanning?
Why dependency scanning matters in cloud-native environments
How dependency scanning works
Types of dependencies and scanning approaches
Language-specific package ecosystems
Container and cloud-native scanning
Integration with development workflows and CI/CD pipelines
Risk prioritization and vulnerability management
Implementation challenges and best practices
Common challenges
Best practices for effective scanning
How Wiz transforms dependency scanning with cloud context
FAQs about dependency scanning 
Watch 12-min demo
Watch how Wiz protects cloud environments from code to runtime.
Watch now
Explore more on this topic
Vulnerability Management Fundamentals
15 Vulnerability Management Metrics to Measure your Program
What is vulnerability management?
What is Cloud Vulnerability Management? CVM That Prioritizes Real Risk, Not Just CVEs
Vulnerability Management Best Practices
What is Continuous Vulnerability Management?
Risk Based Vulnerability Management: How to Prioritize the Threats That Actually Matter
How to Build an Airtight Vulnerability Management Program
Vulnerability Assessment & Remediation
Vulnerability Assessment: Prioritization, Metrics, and Tools
Vulnerability Remediation: A Fast-Track Guide
Vulnerability Prioritization: Building a Maximum Security Strategy
Vulnerability Assessments vs. Penetration Testing: Unpacking the differences
Top OSS Vulnerability Scanners [By Category]
Top 11 Cloud Security Vulnerabilities and How to Fix Them
Data Security
Data Security Compliance: A Practical Guide for CISOs
What Is Database Security? An Overview and Best Practices
What is Data Classification?
What is Data Flow Mapping?
Data Poisoning: Current Trends and Recommended Defense Strategies
13 Data Security Best Practices Every Security Team Needs
What is Cloud Data Security? Risks and Best Practices
Cloud Security Fundamentals
What is Cloud Security Monitoring? Benefits, Challenges, and Best Practices
What Is Cloud Infrastructure Security? Components and Strategies
Cloud Security: The Ultimate 2026 Guide to the Modern Cloud
The Only Cloud Security Checklist You'll Ever Need
Cloud Security Controls: Framework, Checklist, and Best Practices for Implementation
What is CSPM (Cloud Security Posture Management)?
10 Cloud Security Standards Explained: ISO, NIST, CSA, and More
Threat Intel
Threat Intelligence: Types, Lifecycle, and Use Cases
The 13 Must-Follow Threat Intel Feeds
Top Threat Intelligence Tools for 2026 and Beyond
Threat hunting framework: A cloud security best practice guide
What is the threat intelligence lifecycle?
What is Proactive Threat Hunting?
Detection & Resposne
What is Detection Engineering?
What is Cloud Detection and Response (CDR)?
What is Application Detection and Response (ADR)?
Threat Detection and Response (TDR) Explained
Identity Threat Detection and Response
What is incident response? Process, practices, and automation
Vulnerability Management Fundamentals
15 Vulnerability Management Metrics to Measure your Program
What is vulnerability management?
What is Cloud Vulnerability Management? CVM That Prioritizes Real Risk, Not Just CVEs
Vulnerability Management Best Practices
What is Continuous Vulnerability Management?
Risk Based Vulnerability Management: How to Prioritize the Threats That Actually Matter
How to Build an Airtight Vulnerability Management Program
Vulnerability Assessment & Remediation
Vulnerability Assessment: Prioritization, Metrics, and Tools
Vulnerability Remediation: A Fast-Track Guide
Vulnerability Prioritization: Building a Maximum Security Strategy
Vulnerability Assessments vs. Penetration Testing: Unpacking the differences
Top OSS Vulnerability Scanners [By Category]
Top 11 Cloud Security Vulnerabilities and How to Fix Them
Data Security
Data Security Compliance: A Practical Guide for CISOs
What Is Database Security? An Overview and Best Practices
What is Data Classification?
What is Data Flow Mapping?
Data Poisoning: Current Trends and Recommended Defense Strategies
13 Data Security Best Practices Every Security Team Needs
What is Cloud Data Security? Risks and Best Practices
Cloud Security Fundamentals
What is Cloud Security Monitoring? Benefits, Challenges, and Best Practices
What Is Cloud Infrastructure Security? Components and Strategies
Cloud Security: The Ultimate 2026 Guide to the Modern Cloud
The Only Cloud Security Checklist You'll Ever Need
Cloud Security Controls: Framework, Checklist, and Best Practices for Implementation
What is CSPM (Cloud Security Posture Management)?
10 Cloud Security Standards Explained: ISO, NIST, CSA, and More
Threat Intel
Threat Intelligence: Types, Lifecycle, and Use Cases
The 13 Must-Follow Threat Intel Feeds
Top Threat Intelligence Tools for 2026 and Beyond
Threat hunting framework: A cloud security best practice guide
What is the threat intelligence lifecycle?
What is Proactive Threat Hunting?
Detection & Resposne
What is Detection Engineering?
What is Cloud Detection and Response (CDR)?
What is Application Detection and Response (ADR)?
Threat Detection and Response (TDR) Explained
Identity Threat Detection and Response
What is incident response? Process, practices, and automation
Footer
Platform
Cloud & AI Security
Wiz Code
Wiz Cloud
Wiz Defend
Integrations
Environments
Documentation
Learn
Customer Stories
Cloud Security Courses
Blog
CloudSec Academy
Resources Center
Cloud Threat Landscape
Cloud Security Assessment
Vulnerability Database
Company
About Wiz
Join the Team
Newsroom
Events
Contact Us
Trust Center
Wiz Partner Alliance
English (US)
X LinkedIn RSS
© 2026 Wiz, Inc.
Status Privacy Policy Terms of Use Modern Slavery Statement 
Your Opt Out Request is Honored
Your Privacy Choices
We allow certain advertising partners to collect information from our services through cookies and similar technologies as described in our Privacy Policy to deliver ads which are more relevant to you, and assist us with advertising-related analytics. This may be considered "selling" or "sharing”/ processing for targeted online advertising under certain U.S. laws. To opt out of these activities, set the toggle below to the left (button will be gray) and then click “Confirm.” Please note that your choice will apply only to your current device/browser. If you want to opt out of our sale/sharing for targeted advertising disclosures that are not cookie based, please see Section 7(c) of our Privacy Policy.
More information about cookies
Manage Preferences
Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
Functional Cookies
Always Active These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
View Vendor Details
Targeting, Sale or Share of Personal Data
[x]
Targeting, Sale or Share of Personal Data
Under the US privacy laws, you have the right to opt-out of the sale or sharing of your personal information to third parties or targeted advertising. These cookies collect information for analytics and to personalize your experience with targeted ads. You may exercise your right to opt out of the sale or sharing of personal information by using this toggle switch. If you opt out we will not be able to offer you personalized ads and will not hand over your personal information to any third parties. Additionally, you may contact our legal department for further clarification about your rights as a California consumer by using this Exercise My Rights link.If you have enabled privacy controls on your browser (such as a plugin), we have to take that as a valid request to opt-out. Therefore we would not be able to track your activity through the web. This may affect our ability to personalize ads according to your preferences.
Targeting Cookies
[-]  Switch Label label These cookies may be set by Google Ads and used to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Performance Cookies
[-]  Switch Label label These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.
View Vendor Details
Vendors List
Clear
[-] checkbox label label
Apply Cancel
Consent Leg.Interest [-]
checkbox label label [-]
checkbox label label [-]
checkbox label label
Confirm
