---
name: How to implement CI/CD security scanning: Best practices - Wiz
keywords: (placeholder)
metadata:
  url: https://www.wiz.io/academy/application-security/ci-cd-security-scanning
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T19:00:57.430Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
CI/CD Security Scanning: Definition and Best Practices | Wiz
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
All articles Application Security
How to implement CI/CD security scanning: Best practices
Wiz Experts Team
December 12, 2025
| 15 minute read
CI/CD Cheat Sheet Watch 5-min demo    
Key takeaways
CI/CD security scanning integrates automated security checks throughout the software delivery pipeline to identify vulnerabilities, misconfigurations, and compliance issues before they reach production.
Modern scanning approaches combine multiple techniques including SAST, DAST, SCA, secrets detection, and container scanning with contextual prioritization to reduce alert fatigue.
Successful implementation requires balancing security coverage with developer productivity through non-blocking scans, progressive enforcement, and integration with existing developer workflows.
Why CI/CD security scanning matters in cloud-native environments
CI/CD security scanning is the practice of adding automated security checks into your build and deployment pipelines. This means every meaningful code change is tested for risk before it can reach production.
Cloud-native development moves fast. You may be pushing code several times a day, across many services and environments.
To keep control, you need security checks living directly inside your CI/CD pipelines. That is how you get real CI/CD pipeline security and continuous integration security without blocking developer velocity.
In practice this is what people call:
DevSecOps: Bringing security into DevOps instead of treating it as a separate function.
Shift-left security: Catching issues earlier in development rather than in production. Industry surveys show growing adoption of shift-left practices, with organizations reporting faster vulnerability remediation when security checks run during development rather than post-deployment.
Continuous security testing: Running checks on every change, not once a year.
Security as code and policy as code: Expressing rules as code so they can be versioned and automated.
Security gates: Automated rules that decide if a build can move to the next stage.
CI/CD Pipeline Security Best Practices [Cheat Sheet]
In this 13 page cheat sheet we'll cover best practices in the following areas of the CI/CD pipeline: Infrastructure security, code security, secrets management, access and authentication, monitoring and response
Your work email here
Download cheat sheet 
Scanning types for comprehensive coverage
To cover the most important risks, you need several kinds of scanners working together. Each one looks at a different part of your system and finds a different class of problems.
Static Application Security Testing (SAST) is a way to scan your application code without running it. This means the tool reads your source or bytecode and looks for insecure patterns like SQL injection or cross-site scripting.
You should configure SAST to run on every commit or pull request. That way developers get feedback while they are still working on the code.
Software Composition Analysis (SCA) scans both direct dependencies you explicitly include and transitive dependencies (libraries your dependencies require). SCA tools check these components against vulnerability databases like the National Vulnerability Database (NVD) and verify license compliance for legal risk management.
SCA should be part of your build so you know exactly which components are risky. You can also use it to enforce license policies and avoid legal surprises.
Dynamic Application Security Testing (DAST) is a way to test a running application from the outside. This means the scanner sends real HTTP requests to a test environment and looks for security issues in live behavior.
DAST works best against staging or pre-production environments where applications run in realistic configurations. Schedule full DAST scans after deployments or nightly. For faster feedback, complement with targeted API security tests earlier in the pipeline using lightweight DAST tools that check specific endpoints without full application crawls.
Container image scanning looks inside your container images for vulnerabilities and bad configs. This includes the base operating system, application libraries, and even your Dockerfile instructions.
Cloud Security Posture Management (CSPM) is a way to continuously assess your cloud infrastructure for misconfigurations and compliance violations. This means the tool evaluates cloud resources against security best practices and regulatory requirements to find risks like overly permissive access policies, unencrypted storage, or exposed databases.
Secrets scanning is a way to find sensitive values that accidentally end up in code or images. This means the tool looks for API keys, tokens, passwords, and certificates in your repos and artifacts—a critical need given GitGuardian's 2024 State of Secrets Sprawl report documented over 12.8 million secrets exposed in public GitHub repositories during 2023, representing a 67% increase from the previous year.
You can add secrets scanning as:
Pre-commit hooks: To stop secrets before they leave a laptop.
Repository scans: To clean up old leaks.
Pipeline scans: To inspect build artifacts and images.
CI/CD security scanning best practices
Implementing context-driven vulnerability prioritization
Vulnerability prioritization is how you decide what to fix first. This matters because scanners can easily produce more findings than any team can handle.
Traditional tools rely mostly on generic severity scores. This often leads to long lists of “critical” issues with no sense of which ones are actually dangerous to your business.
Context-driven prioritization adds real-world information from your actual cloud environment. You analyze where the vulnerable component lives, how it's exposed to networks, what identities can access it, and what sensitive data it touches. Graph-based analysis connects these factors to show attack paths—how an attacker could chain multiple weaknesses together. This context across identities, network exposure, data sensitivity, and runtime reachability enables attack-path analysis and risk-based remediation that focuses work on toxic combinations rather than isolated findings.
Key questions you should answer include:
Exposure: Is the service internet-facing or internal only?
Runtime use: Is the vulnerable code path even used in production?
Data sensitivity: Does this component handle customer or financial data?
Identity and privileges: Could this lead to admin access or lateral movement?
You can go a step further and map vulnerabilities into attack paths. Graph-based analysis helps you see how an attacker could chain multiple weaknesses into a single exploit.
For example:
A misconfigured security group opens a port.
A vulnerable service listens on that port.
An overprivileged role on that service provides access to a critical database.
Each single issue might not look urgent alone. Together, they form a toxic combination that deserves immediate attention.
When you assess risk, you also need to consider compensating controls. A critical bug behind multiple layers of strong controls might be less urgent than a medium bug with no protection around it.
Good risk scoring should include:
Asset criticality: Production vs. test, crown jewels vs. low-impact.
Business impact: What happens if this asset is compromised?
Technical exploitability: How easy is it to actually attack this in your environment?
By building this model you get CI/CD security best practices that focus work where it really matters.
Advanced secrets management and credential hygiene
Secrets management is how you store and use sensitive credentials safely. This means you stop treating secrets like normal config and give them stricter handling.
Use dedicated secrets managers like HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, or Google Secret Manager rather than storing credentials in source control. Prioritize short-lived credentials through OIDC workload identity federation to cloud providers over static secrets in environment variables. When environment variables are necessary, inject them at runtime from the secrets manager rather than hardcoding them in deployment manifests.
At a minimum, your setup should:
Centralize storage: Keep secrets in one secure system.
Control access: Use roles and policies to decide who or what can read each secret.
Inject at runtime: Fetch secrets only when needed and avoid writing them to logs or artifacts.
Different types of secrets need different rotation schedules. Short-lived CI tokens might live for minutes, while database passwords may rotate every few weeks.
It also helps to define clear “break-glass” procedures. These are emergency steps for gaining access when something fails, without dumping secrets into insecure places.
To catch leaks you should scan for secrets across the entire software lifecycle: pre-commit hooks warn developers before secrets leave their laptop, repository scans find historical leaks in Git history, pipeline scans inspect build artifacts and container images, and runtime scans detect exposed credentials in running workloads. Extending detection into build artifacts, registries, and runtime environments reduces dwell time for leaked credentials and provides complete visibility from code to cloud.
Custom detectors are useful for your own secret formats. This reduces both false alarms and missed exposures.
Securing Infrastructure as Code and container builds
Infrastructure as Code (IaC) is how you define cloud resources in files. This means your networks, databases, and servers are declared in code and deployed automatically.
You should scan IaC templates before they ever reach the cloud. Policy-as-code frameworks turn security rules into versioned, testable code. Open Policy Agent (OPA) with Rego language lets you write policies for Terraform, Kubernetes, and CI/CD systems. Conftest validates configurations against OPA policies. For Kubernetes specifically, Kyverno provides a Kubernetes-native policy engine with simpler YAML-based rules. These frameworks make policies reusable across teams and auditable through version control.
Common misconfigurations to catch include:
Security groups that allow traffic from anywhere.
Storage buckets without encryption at rest.
Datastores missing backups or logging.
Public endpoints on internal-only services.
Detecting these issues in code is cheaper than fixing them later. It also helps enforce consistent CI/CD pipeline security best practices across teams.
Configuration drift is another risk you need to manage. Drift happens when someone changes cloud resources directly in the console instead of through IaC.
You can detect drift by comparing what your IaC says should exist with what actually exists. When they do not match, you alert or automatically fix it.
For containers, you want a secure build process. Start with trusted, hardened base images and avoid random images from public registries.
A “ golden image” program means:
You maintain a small set of known-good base images.
You keep them patched and minimal.
Teams build on top of those instead of starting from scratch.
Image signing adds cryptographic integrity verification. Sigstore's Cosign tool signs container images with ephemeral keys backed by OIDC identity, eliminating long-lived signing keys. Docker Content Trust uses Notary v2 for signature verification. At deploy time, Kubernetes admission controllers like Kyverno or OPA Gatekeeper verify signatures before allowing pods to run, ensuring only approved images reach production.
Admission controllers are your last safety net before production. They enforce rules such as:
No containers running as root.
Resource limits must be set.
Only images from approved registries are allowed.
Policy engines let you write security rules as code so you can test and version them like application code. Centralized policy-as-code lets teams enforce signature verification, SBOM requirements, and configuration standards consistently across development clusters, staging environments, and production clouds. This unified approach prevents policy drift where different environments have different security baselines, and reduces tool sprawl by expressing rules once and applying them everywhere.
Implementing software supply chain security and provenance
Software supply chain security ensures you can verify what you build and deploy, providing cryptographic proof of your build process and a complete inventory of all components.
SBOMs (Software Bills of Materials) list every software component in SPDX or CycloneDX format. Generate them during builds using tools like Syft, Trivy, or native package managers. They should include:
Direct and transitive dependencies
OS packages from container base images
License information
SLSA is a framework for software build integrity.
SLSA Level 2 requires:
Version-controlled source
Authenticated build service
Generated build provenance
SLSA Level 3 adds:
Hardened, isolated build environments
Non-falsifiable provenance
Provenance attestations (via in-toto) record commit SHA, builder identity, parameters, and timestamps. Sign them with Sigstore Cosign so they can be verified at deployment.
Admission controllers should then validate:
Image signatures
SBOM presence and vulnerability status
Provenance linking back to trusted source and builder
This creates an auditable chain from commit to production and lets you quickly identify impacted services when new vulnerabilities arise.
Designing zero-trust CI/CD pipeline architecture
Zero-trust pipeline architecture means you do not automatically trust any pipeline component. You assume an attacker could try to abuse your CI/CD just like any other system.
One of the first steps is pipeline isolation. Instead of one big, powerful service account, you give each stage its own narrow identity.
For example:
A build job can compile and push artifacts but not deploy them.
A deploy job can pull images and update services, but not change source code.
Avoid shared static credentials across pipelines. Instead, implement OIDC-based workload identity federation. GitHub Actions, GitLab CI, and CircleCI support OIDC tokens that AWS, Azure, and GCP can exchange for short-lived cloud credentials. Each pipeline job authenticates with its own identity, receives temporary credentials valid for minutes, and leaves no long-lived secrets to rotate or leak.
Network segmentation adds another strong layer. You keep build runners, artifact registries, and production environments in separate network zones.
Secure communication between pipeline components should use: private endpoints instead of public internet, encryption in transit with TLS 1.3, and mutual TLS (mTLS) for service-to-service authentication.
You also need monitoring focused on the pipelines themselves. If a malicious actor gains access, they may try to:
Create new pipelines that deploy unreviewed code.
Change existing pipeline definitions.
Abuse credentials to reach other systems.
By logging and analyzing pipeline activity, you can spot unusual patterns early. Sending these logs to a central monitoring or SIEM system helps your security team see the full picture.
Supply chain controls round this out. They help ensure that what you build and deploy is legit.
This can include:
Verifying checksums and signatures of critical dependencies.
Recording build attestation data that describes how an artifact was made.
Tracking provenance from commit to container image to running workload.
This kind of pipeline hardening and build isolation is what many teams now expect from the best CI/CD tools for software supply chain protection.
Optimizing scan performance without sacrificing security
A common worry is that all this scanning will make pipelines slow. You can avoid that if you design for performance from the start.
Parallel scanning is a simple win. You run independent scans at the same time instead of in a long queue.
You can also cache results where it makes sense. If a part of the code did not change, you might not need to re-scan it with a heavy tool.
Incremental scanning focuses on what changed. Many SAST tools can analyze only the modified files or modules in a pull request.
You still run deeper, full scans, just less often. This keeps everyday feedback fast while still catching edge cases on a schedule.
Not all pipelines need the same level of checking. You can tune rigor by branch or environment.
For example:
Feature branches: fast, non-blocking checks, mostly for developer feedback.
Release branches: full scans, with some blocking rules.
Production deploys: strict gates on critical and high-risk findings.
This is called progressive security. You increase the strength of controls the closer you get to real users.
You also want to cut down duplicate noise. If three scanners all complain about the same vulnerable library, that should be one ticket, not three.
A centralized vulnerability database or platform can:
Normalize findings from multiple tools.
Group related issues.
Track remediation status and ownership.
This is how you keep automated scanning tools for continuous security powerful without drowning your teams. Schrödinger did this kind of tuning to support rapid drug discovery workflows without sacrificing protection.
wiz academy
[
Shift Left Explained: What It Means to Shift Security Left
Improve development workflows with shift left security by embedding testing early to catch vulnerabilities and speed delivery.](https://www.wiz.io/academy/shift-left-security)
Read more 
Integrating runtime context into build-time decisions
Runtime context is information you get from real systems in production. Using this data in your CI/CD decisions makes your scanning smarter.
Production telemetry reveals which code paths execute in real workloads, which services handle sensitive data, and where attackers probe your defenses. Closing the loop between runtime detections and code owners speeds root-cause fixes and reduces repeat incidents. When runtime protection blocks an attack, automated feedback creates tickets linking the blocked request to the owning team and source commit, then updates scanning rules to detect similar patterns earlier in the pipeline. This creates a learning system where security improves continuously based on real attack data.
If a vulnerability affects code that is never called in production, it might not be top priority. If it hits a hot path with important data, it should jump to the front of the queue.
You can automate this feedback loop. When runtime protection blocks an attack, a pipeline can:
Capture details about the blocked request and target service.
Create a ticket linking back to the owning team and commit.
Update scanning rules to better detect similar issues earlier.
This is how your security model learns over time. It stops being just static rules and becomes a living system.
Runtime data also helps you validate scan results. If SAST identifies a vulnerability in code that appears unused, validate through runtime telemetry before de-prioritizing. Use code coverage data from production to confirm the code path is never executed. Only after confirming zero production usage should you lower priority, and document the decision with supporting telemetry data.
Adaptive policies adjust to the environment. The same code deployed in dev and prod might be treated differently.
You might accept certain risks in dev to move quickly. In production, those same findings trigger a hard block.
Building developer-friendly security workflows
For security scanning to work long term, developers need to be comfortable with it. The goal is to give them clear, direct help rather than extra friction.
You get there by putting security feedback where developers already work. That means IDEs, pull requests, and team chat, not separate dashboards they never open.
Each finding should be straightforward:
What is wrong: A simple, clear description.
Where it is: Exact file and line or resource.
How to fix it: Short, specific guidance or a code example.
You can avoid overwhelming people by using progressive disclosure. Show the most important issues by default and let power users drill into full details if they want.
Risk-based filtering also helps. Developers see issues that matter most for the services they own, rather than every low-level warning in the company.
Self-service is another big win. If developers can run scans locally, check the status of their services, and see their security “scorecards,” they are more likely to engage.
Helpful self-service elements include:
Security scoreboards per service or repo.
Remediation playbooks for common issues.
Auto-fix suggestions for simple patterns.
A security champions program can pull this together. These are developers embedded in teams who understand both the code and the security tooling.
Establishing continuous compliance and audit trails
Many teams also need to prove they are doing the right things. That is where compliance and audit come in.
Automated compliance checks map security controls to regulatory frameworks and industry standards. Common mappings include: SOC 2 Type II (CC6 for logical access, CC7 for system operations), ISO 27001/27002 (A.8.16 for software management, A.14.2 for secure development), NIST 800-53 (SA family for system and services acquisition), NIST Secure Software Development Framework (SSDF) for supply chain security, CIS Benchmarks for configuration hardening, PCI DSS for payment systems, and HIPAA for healthcare data protection.
This might include:
Required encryption settings.
Approved regions or instance types.
Mandatory logging or monitoring on certain services.
You then run these rules as part of the pipeline and on a schedule. Violations can block deployments or at least trigger reviews.
Audit trails are your evidence. They show auditors and stakeholders what actually happened over time.
You should record:
Who triggered deployments and when.
Which scans ran and what they found.
How and when issues were fixed.
Mapping CI/CD security controls to compliance frameworks
Different industries require different compliance frameworks. This table maps common CI/CD security controls to specific framework requirements:
Each control should be implemented with automated checks that run continuously and generate audit evidence. Store compliance reports in tamper-evident logs that auditors can review to verify continuous adherence to framework requirements.
How Wiz enables advanced CI/CD security practices
Wiz provides a single platform to secure everything you build and run in the cloud. CI/CD security scanning is one of the key workflows it supports.
Wiz Code scans IaC templates, dependencies, container images, and secrets across repositories and CI/CD pipelines. Unlike generic scanners, Wiz Code provides cloud-aware context by understanding how your code will actually deploy—which IAM roles it will use, which networks it will join, and which data it will access. This context flows into IDE plugins and pull request comments, giving developers focused guidance on issues that matter in your specific cloud environment rather than generic vulnerability lists.
The Wiz Security Graph ties pipeline findings to what is actually running in your cloud. Graph context connects scanner findings with identities, network paths, and data sensitivity to surface toxic combinations and real attack paths. For example, the graph might show that a medium-severity container vulnerability becomes critical because the container runs with admin privileges, connects to an internet-exposed load balancer, and accesses a database containing customer PII—three separate issues that together create an exploitable path from the internet to sensitive data.
This context lets you prioritize work based on real attack paths rather than raw scores. It also lets you trace issues from production all the way back to their source in code and pipeline.
Wiz's unified policy engine gives you one place to define rules across code, CI/CD, cloud, and runtime. You do not have to recreate the same policies in ten different tools.
WizOS hardened images add another layer by providing near-zero CVE base images. They reduce noise from base image issues so your teams can focus on application risks instead.
Together, these capabilities help you implement CI/CD security scanning that is both strong and developer-friendly. They support the modern cloud security operating model where security, development, and operations work from the same shared view. Get a demo to see how Wiz can help you secure your CI/CD pipelines without slowing down delivery.
Watch 5-min Wiz Code demo
Watch how Wiz scans code, dependencies, and CI/CD pipelines to catch vulnerabilities, exposed secrets, and misconfigurations before they reach production.
Your work email here
Watch now 
FAQs about CI/CD security scanning
How do you handle security scanning in microservices architectures?
What is the best approach for scanning in multi-cloud CI/CD environments?
How can you reduce false positives in CI/CD security scanning?
Should security scans be blocking or non-blocking in CI/CD pipelines?
How do you manage CI/CD security scanning costs at scale?
Table of contents
Why CI/CD security scanning matters in cloud-native environments
Scanning types for comprehensive coverage
CI/CD security scanning best practices
Implementing context-driven vulnerability prioritization
Advanced secrets management and credential hygiene
Securing Infrastructure as Code and container builds
Implementing software supply chain security and provenance
Designing zero-trust CI/CD pipeline architecture
Optimizing scan performance without sacrificing security
Integrating runtime context into build-time decisions
Building developer-friendly security workflows
Establishing continuous compliance and audit trails
Mapping CI/CD security controls to compliance frameworks
How Wiz enables advanced CI/CD security practices
FAQs about CI/CD security scanning 
CI/CD Pipeline Security [Cheat Sheet]
Get the cheat sheet for securing every stage of your CI/CD pipeline.
Download now
Explore more on this topic
Fundamentals of Code Security
7 Code Security Best Practices (and How to Implement Them)
Cloud Application Security Best Practices for DevSecOps
The Secure Software Development Framework (SSDF)
What is Security by Design?
What Is Secure Coding? Overview and Best Practices
Secure SDLC
DevOps and DevSecOps
What is SecDevOps? + How It Differs From DevSecOps
What DevSecOps Means in 2026: How to Build and Scale Maturity
DevSecOps Best Practices to Help You Build a Secure Pipeline
What Is DevOps Security? Implementation, Challenges and Best Practices
GitOps vs. DevOps: How GitOps Keeps You Aligned
11 DevSecOps Tools and The Top Use Cases in 2026
CI/CD Pipeline Security Best Practices 2026
Security Testing and Analysis
What is vulnerability scanning? Best practices & challenges
SAST vs. SCA: What's the Difference?
What Is SAST? How Static Application Security Testing Works
SAST vs DAST: How to Use Both Testing Tools for App Security
Secure Code Scanning: Basics & Best Practices
SCA Implementation: A Step-by-Step Framework for 2026
What is Application Security Posture Management (ASPM)?
Top 9 Open-Source SAST Tools
Open Source and Supply Chain Security
Essential Application Security Best Practices
Open-source security: Best practices and tools
Guide to Standard SBOM Formats
What Is SBOM? Practical Guide to Implementation
Software Supply Chain Best Practices [Step by Step Guide]
The Top 28 Open-Source Code Security Tools: A 2026 Guide
Guide to SBOM Tools: 5 Picks for Enterprise Security Teams
Software Supply Chain Security: Key Risks and Best Defenses
Infrastructure and Policy Security
What is Security as Code (SaC)?
Policy as Code: Benefits, Examples, and How to Get Started
IaC Scanning: Concepts, Process, and Tools
IaC Security: Red Flags to Watch and 6 Best Practices
Top IaC Tools and Practices to Strengthen Code and Cloud Security
What is Malicious Code? Types, Risks, and Prevention Strategies
Source Code Security: Basics and Best Practices
API and Secrets Security
What is API Security?
The Best Open-Source API Security Tools and When to Use Them
Secrets Detection: A Fast-Track Guide
Secret scanning: How it works and best practices
API Security: Best Practices for Safer Cloud Security
Fundamentals of Code Security
7 Code Security Best Practices (and How to Implement Them)
Cloud Application Security Best Practices for DevSecOps
The Secure Software Development Framework (SSDF)
What is Security by Design?
What Is Secure Coding? Overview and Best Practices
Secure SDLC
DevOps and DevSecOps
What is SecDevOps? + How It Differs From DevSecOps
What DevSecOps Means in 2026: How to Build and Scale Maturity
DevSecOps Best Practices to Help You Build a Secure Pipeline
What Is DevOps Security? Implementation, Challenges and Best Practices
GitOps vs. DevOps: How GitOps Keeps You Aligned
11 DevSecOps Tools and The Top Use Cases in 2026
CI/CD Pipeline Security Best Practices 2026
Security Testing and Analysis
What is vulnerability scanning? Best practices & challenges
SAST vs. SCA: What's the Difference?
What Is SAST? How Static Application Security Testing Works
SAST vs DAST: How to Use Both Testing Tools for App Security
Secure Code Scanning: Basics & Best Practices
SCA Implementation: A Step-by-Step Framework for 2026
What is Application Security Posture Management (ASPM)?
Top 9 Open-Source SAST Tools
Open Source and Supply Chain Security
Essential Application Security Best Practices
Open-source security: Best practices and tools
Guide to Standard SBOM Formats
What Is SBOM? Practical Guide to Implementation
Software Supply Chain Best Practices [Step by Step Guide]
The Top 28 Open-Source Code Security Tools: A 2026 Guide
Guide to SBOM Tools: 5 Picks for Enterprise Security Teams
Software Supply Chain Security: Key Risks and Best Defenses
Infrastructure and Policy Security
What is Security as Code (SaC)?
Policy as Code: Benefits, Examples, and How to Get Started
IaC Scanning: Concepts, Process, and Tools
IaC Security: Red Flags to Watch and 6 Best Practices
Top IaC Tools and Practices to Strengthen Code and Cloud Security
What is Malicious Code? Types, Risks, and Prevention Strategies
Source Code Security: Basics and Best Practices
API and Secrets Security
What is API Security?
The Best Open-Source API Security Tools and When to Use Them
Secrets Detection: A Fast-Track Guide
Secret scanning: How it works and best practices
API Security: Best Practices for Safer Cloud Security
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
