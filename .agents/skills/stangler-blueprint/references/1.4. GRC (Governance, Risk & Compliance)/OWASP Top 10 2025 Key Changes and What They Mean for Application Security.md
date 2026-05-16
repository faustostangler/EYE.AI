---
name: OWASP Top 10 2025: Key Changes and What They Mean for Application Security
keywords: (placeholder)
metadata:
  url: https://orca.security/resources/blog/owasp-top-10-2025-key-changes/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T19:00:57.430Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
OWASP Top 10 2025: Key Changes & What They Mean | Orca Security
___
2026 State of AppSec Report is live. See the data behind modern application risk.
Get the Report 2026 State of AppSec Report is live. See the data behind modern application risk.
Platform
Capabilities
Who We Serve Platform Overview CNAPP Secure cloud native applications with a purpose-built platform CSPM Identify and remediate misconfigurations across clouds CWPP Protect VMs, containers, and serverless functions CIEM Secure cloud identities, users, and entitlements DSPM Reduce the risk of data breaches and protect sensitive PII Container & Kubernetes Security Scalable containers, images, and Kubernetes applications Multi-Cloud Compliance Achieve regulatory compliance for industry standards and custom checks Vulnerability Management Agentless vulnerability management that prioritizes your most critical risks API Security Complete API discovery, security posture management, and drift detection CDR 24x7 monitoring and response across the entire cloud attack surface Application Security Secure cloud-native applications across the SDLC and trace dev risks to production. AI Security Reduce AI risk across code, posture, and runtime Orca AI Accelerate cloud security with AI agents and AI-driven workflows SideScanning™ Technology Our innovative approach provides complete cloud coverage Orca Sensor Fully integrated runtime visibility and security for advanced CDR Industries Financial Services Government Healthcare Media & Entertainment Retail Technology Roles CISO DevOps Security Practitioner
Resources
Resources
Research Learn Resource Library Blog Cloud Security Learning Glossary Comparisons Connect Events & Webinars Support Documentation User Center  Research Report 2026 State of Application Security Report Research Pod Meet our team that discovers and analyzes cloud risks. Discovered Vulnerabilities Critical cloud vulnerabilities discovered by the Orca Research Pod. Open Source Projects Cloud security tools for developers and security teams. “Orca Watch” Series Blog series that highlights new trends and risks seen by the Orca Platform. Technical Deep Dives In-depth, technical articles on cloud security and recommended best practices.  Report 2025 State of Cloud Security
Customers Case Studies      View all Case Studies Dive Deeper Ratings & Reviews See what our users say about us Why Orca Learn all about our purpose-built cloud security platform
Partners
CSPs
Integrations Partner Overview Amazon Web Services Microsoft Azure Google Cloud Alibaba Cloud Oracle Cloud Tencent Cloud New Become a Partner Integrations Overview Chainguard Jira PagerDuty Snowflake Splunk Zscaler View All Integrations Integrate with us Learn how We're Building an Open Ecosystem
Company About Us Contact Us Careers Newsroom Media Kit Why Orca Learn how Orca is Leading the Market
Log In
USA
Europe
Australia
US-Gov
Get Demo
Press Enter to search
No search results
View more results
Blog Home
Research
Research Pod 
OWASP Top 10 2025: Key Changes and What They Mean for Application Security
 Bar Kaduri
Published: Nov 20, 2025
[](mailto:?Subject=OWASP Top 10 2025: Key Changes and What They Mean for Application Security&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fowasp-top-10-2025-key-changes%2F)
Table of contents
A closer look at the OWASP Top 10 2025
A01:2025 – Broken Access Control
A02:2025 – Security Misconfiguration
A03:2025 – Software Supply Chain Failures
A04:2025 – Cryptographic Failures
A05:2025 – Injection
A06:2025 – Insecure Design
A07:2025 – Authentication Failures
A08:2025 – Software or Data Integrity Failures
A09:2025 – Logging & Alerting Failures
A10:2025 – Mishandling of Exceptional Conditions
How Orca can help
The OWASP Top 10 2025 release candidate is here, marking an important milestone in the evolution of application security best practices. Published for public review and revision, this candidate list offers an early look at the most critical risks shaping today's application landscape before the final version is ratified.
As one of the most trusted resources in the AppSec community, the OWASP Top 10 helps security teams focus on the vulnerabilities most likely to impact modern applications. The 2025 release highlights a shift toward identifying root causes rather than symptoms, emphasizing how today's threats often originate from design flaws, misconfigurations, and dependency-level weaknesses that ripple across complex software ecosystems.
Orca Security is proud to have partnered with OWASP project leaders to contribute our unique data and insights to the project.
Compared to the 2021 version, two new categories have been added, one has been consolidated, and several have been refocused to reflect today's most pressing risks. 
Changes to the OWASP Top 10 list, comparing 2021 to 2025
The new OWASP Top 10:2025 categories are:
A01:2025 – Broken Access Control
A02:2025 – Security Misconfiguration
A03:2025 – Software Supply Chain Failures
A04:2025 – Cryptographic Failures
A05:2025 – Injection
A06:2025 – Insecure Design
A07:2025 – Authentication Failures
A08:2025 – Software or Data Integrity Failures
A09:2025 – Logging & Alerting Failures
A10:2025 – Mishandling of Exceptional Conditions
A few key trends stand out in this year's update:
SSRF was merged into Broken Access Control, reflecting the significant impact that server-side request forgery has on access controls. This change highlights how, in modern applications, the line between service-level and user-level access is blurring—a direct consequence of the widespread use of microservices, cloud services, and APIs.
The “Vulnerable and Outdated Components” category has evolved into “Software Supply Chain Failures,” broadening its scope beyond known vulnerabilities to include unknown vulnerabilities introduced by third-parties. Supply chain attacks have become both more frequent and harder to detect, as they often exploit trust in dependencies, open source, and outsourced services.
A shift from symptoms to root causes defines the 2025 update. OWASP explicitly states that it aims to focus more on root causes rather than symptoms. For example, where the 2021 list included “Sensitive Data Exposure” (a symptom), the updated list identifies “Cryptographic Failures” (a root cause). Similarly, “Software Supply Chain Failures” expands the prior component-vulnerability concept to encompass the entire software lifecycle.
A closer look at the OWASP Top 10 2025
Let's explore each of the new and updated categories to understand what has changed, and why these shifts matter for modern AppSec programs.
A01:2025 – Broken Access Control
Broken Access Control remains the top risk in the OWASP Top 10:2025, affecting virtually every tested application. Compared to 2021, new attack methods have emerged, making this the category with the highest number of mapped CWEs. It covers issues like privilege escalation, insecure direct object references, CORS misconfigurations, and token manipulation, with SSRF (Server-Side Request Forgery) newly added to this group. These flaws allow unauthorized access or data exposure, reinforcing the need for strict, server-side access controls and denial-by-default policies.
A02:2025 – Security Misconfiguration
Security Misconfiguration rose from #5 to #2 in the OWASP Top 10:2025, with every tested application showing some form of misconfiguration. As software becomes more configurable, the risk has grown, with over 719,000 mapped CWEs, such as CWE-16 (Configuration) and CWE-611 (XXE). This category covers issues like exposed default accounts, unnecessary services, insecure permissions, missing security headers, and misconfigured cloud storage. Common examples include unremoved sample applications, verbose error messages, and open cloud permissions.
Preventing this risk requires automated, repeatable hardening processes, minimal platform setups, secure configuration management across all environments, and regular verification of security settings.
A03:2025 – Software Supply Chain Failures
Software Supply Chain Failures (A03:2025) is now a top community concern, with 50% of respondents ranking it #1. It has evolved from 2013's “Using Components with Known Vulnerabilities” into a broader category covering build, distribution, update, and tooling compromises. Although only 11 CVEs map to related CWEs, the category shows the highest average incidence rate (5.19%) in contributed testing data and more than 215,000 occurrences. Key drivers include obsolete or unmaintained components, non-updateable dependencies, insecure CI/CD, and poor change tracking.
You're at risk if you don't maintain an SBOM, track transitive dependencies, remove unused packages, automate vulnerability scanning and patching, harden and monitor developer tooling and CI/CD (with separation of duties and signed/immutable builds), and enforce least privilege and MFA on repos, build servers, and artifact stores. High-impact examples (SolarWinds, Bybit, GlassWorm) show why organizations must inventory, triage, and remediate supply-chain risks continuously.
A04:2025 – Cryptographic Failures
Cryptographic Failures (A04:2025) dropped to #4, emphasizing weaknesses from missing, weak, or misapplied encryption that expose sensitive data. With over 1.6 million occurrences, common issues include outdated algorithms, predictable randomness, poor key management, and missing TLS enforcement. As cryptography has become easier to implement through modern APIs and cloud-managed certificates, many failures now stem from misuse rather than absence.
Preventing this risk requires strong, up-to-date encryption standards, authenticated encryption modes, secure key storage and rotation, adaptive password hashing, and enforcing encryption for all sensitive data in transit and at rest.
A05:2025 – Injection
Injection (A05:2025) slipped to #5 but remains a critical, well-tested risk, affecting 100% of tested applications, with the largest number of CVEs across all categories. Injection is driven by frequent XSS (high-frequency, lower-impact) and rarer but devastating SQL injection (low-frequency, high-impact). It occurs when untrusted input is treated as code or query structure (SQL, NoSQL, OS commands, LDAP, EL/OGNL, etc.), and is best prevented by separating data from commands: use safe/parameterized APIs or ORMs, employ positive server-side validation, context-aware escaping only when necessary, and add SAST/DAST/IAST + fuzzing in CI/CD.
Note that injection threats in LLMs are now tracked separately. Organizations should address both traditional interpreter injection and emerging AI prompt-based threats in their threat models.
A06:2025 – Insecure Design
Insecure Design (A06:2025) dropped to #6, reflecting progress in secure design awareness but continued weaknesses in application architecture and business logic. Unlike insecure implementation flaws, insecure design stems from missing or ineffective security controls that can't be fixed by perfect code. Common causes include poor threat modeling, lack of security requirements early in design, and failure to anticipate unwanted states or misuse cases.
A07:2025 – Authentication Failures
Authentication Failures (A07:2025) holds its #7 spot with a refined name and 36 mapped CWEs, emphasizing persistent weaknesses in login and session management despite widespread use of frameworks. Common issues include hard-coded or weak passwords, missing MFA, poor credential recovery, insecure session handling, and exposure to brute-force or credential-stuffing attacks. These flaws often arise from weak password policies, improper session invalidation, or reliance on outdated practices like password rotation.
A08:2025 – Software or Data Integrity Failures
Software or Data Integrity Failures (A08:2025) remains at #8 and focuses on situations when systems trust code or data without verifying provenance or integrity; for example, unsigned updates, unvetted plugins/CDNs, or CI/CD pipelines that accept artifacts without checks. These failures let attackers inject malicious code or tampered data (including insecure deserialization) and are distinct from broader supply-chain issues because they focus on integrity verification at the artifact/data level.
A09:2025 – Logging & Alerting Failures
Logging & Alerting Failures (A09:2025) continues to rank at #9, with a new emphasis on alerting as a critical part of detection and response. Though underrepresented in CVE data, these failures severely impact visibility and incident response. Common issues include insufficient or inconsistent logging, unmonitored or tamperable logs, missing alerts for suspicious activity, and excessive false positives that overwhelm SOC teams.
A10:2025 – Mishandling of Exceptional Conditions
Mishandling of Exceptional Conditions (A10:2025) is a new addition to the OWASP Top 10, addressing poor error and exception handling that leads to unpredictable or insecure behavior. It focuses on failures like improper input validation, incomplete error recovery, “failing open,” and inconsistent exception handling, which can result in crashes, logic flaws, data corruption, or denial-of-service. With 24 CWEs, including leaking sensitive errors (CWE-209) and failing securely (CWE-636), this category highlights the risks of not planning for abnormal conditions.
How Orca can help
Orca Security is a proud contributor to OWASP initiatives, including OWASP Top 10 2025 and the OWASP Top 10 for Non-Human Identities. Through these collaborations, Orca provides data-driven insights that help shape industry benchmarks and improve understanding of cloud-native application risks.
Within the Orca Cloud Security Platform, organizations can:
Detect and remediate risks that map directly to OWASP Top 10 categories across their cloud, container, and application environments.
Leverage comprehensive Application Security (AppSec) capabilities to catch vulnerabilities, misconfigurations, and secrets before they can reach production environments.
Trace risks from Cloud-to-Dev, enabling full visibility from deployed workload to the code origin and owner of an alert.
Leverage OWASP-aligned frameworks, dashboards, and alert labels that make it easy to visualize exposure and measure compliance against these industry standards.
Stay ahead of emerging threats through coverage of related benchmarks, including the OWASP AI Security Top 10. 
Prioritized alert in the Orca Platform, which is aligned with OWASP Top 10 framework
By unifying visibility from code to cloud, Orca helps security teams operationalize the OWASP Top 10 and measurably reduce risk at scale.
Learn more
Interested in learning about the benefits of the Orca Cloud Security Platform? Schedule a personalized 1:1 demo.
Table of contents
A closer look at the OWASP Top 10 2025
A01:2025 - Broken Access Control
A02:2025 - Security Misconfiguration
A03:2025 - Software Supply Chain Failures
A04:2025 - Cryptographic Failures
A05:2025 - Injection
A06:2025 - Insecure Design
A07:2025 - Authentication Failures
A08:2025 - Software or Data Integrity Failures
A09:2025 - Logging & Alerting Failures
A10:2025 - Mishandling of Exceptional Conditions
How Orca can help
[](mailto:?Subject=OWASP Top 10 2025: Key Changes and What They Mean for Application Security&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fowasp-top-10-2025-key-changes%2F)
Related articles
  
Research
TanStack and 160+ npm/PyPI Packages Compromised in Supply Chain Worm Attack
May 12, 2026
  
Research
Dirty Frag: Linux Kernel Vulnerability Chain Enables Local Privilege Escalation to Root
May 10, 2026
  
Research
Critical Apache HTTP Server HTTP/2 Vulnerability Could Enable Remote Code Execution
May 08, 2026
Stay in the loop
Keep up to date with everything you need to know about cloud security and our latest research
Email Address
This site is protected by reCAPTCHA.
Submit
By submitting my email address I agree to the use of my personal data in accordance with Orca Security Privacy Policy. 
Personalized Demo
See Orca Security in Action
Gain visibility, achieve compliance, and prioritize risks with the Orca Cloud Security Platform.
Get a Demo 
Chat with Us
See Orca Security in Action
Gain visibility, achieve compliance, and prioritize risks with the Orca Cloud Security Platform.
Chat with an Orca Expert
No Slack account required.
Platform
Cloud Security Platform
Cloud Native Application Protection
Vulnerability Management
SideScanning™ Technology
Container and Kubernetes Security
Cloud Security Posture Management (CSPM)
Cloud Infrastructure Entitlement Management (CIEM)
Cloud Workload Protection Platform (CWPP)
AI Security
Orca AI
Multi-Cloud Compliance and Security
Cloud Detection and Response (CDR)
Application Security
API Security
Data Security Posture Management (DSPM)
Orca Sensor
Technology Ecosystem
Integrations
Amazon Web Services
Microsoft Azure
Google Cloud Platform
Oracle Cloud
Alibaba Cloud
Tencent Cloud
Solutions
By Solution
Malware Detection
Sensitive Data Detection
IAM Risk
Lateral Movement Risk
By Industry
Financial Services
Technology
Government
Media & Entertainment
Healthcare
Retail
Resources
Library
Blog
Cloud Security Learning
Glossary
Product Info
Case Studies
Events
Comparisons
CrowdStrike
Wiz
Check Point CloudGuard
Lacework FortiCNAPP
Rapid7
Tenable
Qualys TotalCloud
Prisma Cloud
Company
About
Partners
Research Pod
Reviews
Careers
Newsroom
Media Kit
Contact
Security Portal
User Center
Login
Partner Portal
Try Free with AWS
Stay in touch
Get cloud security insights and the latest Orca news * Email Address Submit
Awards & Certifications
AWS Advanced Technology Partner Security Competency
FedRAMP Moderate Authorized
ISO/EC 27001 Information
ISO/EC 27017 Information
ISO/EC 27018 Information
ISO/EC 27701 Privacy
PCI SAQ-D
SOC 2 TYPE II Certified
2022 AWS Global Security Partner of the Year
Star Level One: Self-Assessment Cloud Security Alliance
CSA Trusted Cloud Provider Cloud Security Alliance
IRAP Certification
©2026 Orca Security. All rights reserved.
Privacy Policy
Terms of Use
Cookies Settings
Virtual Patent Marking
    
By clicking “Accept All Cookies”, you agree to the storing of cookies on your device to enhance site navigation, analyze site usage, and assist in our marketing efforts. Cookie Policy
Accept All Cookies Reject All
Cookies Settings 
Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences, or your device, and is mostly used to make the site work as you expect. The information does not usually identify you directly, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to learn more and change our default settings. Blocking some types of cookies may impact your experience of the site and the services we are able to offer.
More information
Allow All
Manage Consent Preferences
Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
Performance Cookies
[x]
Performance Cookies
These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.
Functional Cookies
[x]
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
Targeting Cookies
[x]
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Cookie List
Clear
[-] checkbox label label
Apply Cancel
Consent Leg.Interest [-]
checkbox label label [-]
checkbox label label [-]
checkbox label label
Reject All Confirm My Choices
 
