---
name: Securing CI/CD Pipelines Through Security Gates with Kubescape - ARMO Platform
keywords: (placeholder)
metadata:
  url: https://www.armosec.io/blog/securing-ci-cd-pipelines-security-gates/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T19:00:57.430Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
Securing CI/CD Pipelines Through Security Gates | ARMO 
Kubescape 5 About Kubescape
Kubescape 5
What is Kubescape? An open-source Kubernetes security platform
GitHub The pure open-source version
Kubescape.io Kubescape's official website 🐼
Community Discuss all things Kubescape Talk it out
Kubescape VS. ARMO Platform Elevate your cloud security beyond Kubescape in just two clicks
Solutions 7 ARMO Platform
Solutions 7
Kubernetes Security Posture Management (KSPM)
Cloud Applications Detection & Response (CADR)
Cloud-Native Security for AI Workloads
Runtime-based Vulnerability Management
Runtime-based Cloud Hardening & Remediation
Continuous Cloud Security Posture Management (CSPM)
On-Premises Kubernetes Security
Resources 9 Resources & learning
Resources 9
Documentation Visit ARMO's doc hub
Blog All things cloud security and some
CTRL by ARMO Cloud Threat Readiness Lab
Resource Hub Cloud and Runtime Security Resources Hub
Customer stories Learn from the experience of others
Use cases Your cloud, your security use-case
2025 State of Cloud Runtime Security Key Challenges and the Path Forward
ARMO Platform vs CNAPP/CSPM AKA: ARMO Platform > CNAPP/CSPM
Glossary Your Kubernetes security digital handbook
Company 5 Company Insights
Company 5
About us If you're really into us, that's the place to go
In the news All the headlines ARMO generated
Careers Join our team!
Contact us We always appreciate a good conversation
CADR:CON We created The First Cloud Runtime Security Summit
Pricing
❤ Love
Start Free Book a Demo
Book a Demo
Get the latest, first
Work Email*
UTM Campaign
UTM Medium
UTM Source
utm_content
utm_term Subscribe
 Blog
Home
Blog
Securing CI/CD Pipelines Through Security Gates with Kubescape 
Securing CI/CD Pipelines Through Security Gates with Kubescape
Dec 28, 2022 
Ben Hirschberg
CTO & Co-founder
Tap to unmute
Your browser can't play this video.
Learn more 
An error occurred.
Try watching this video on www.youtube.com, or enable JavaScript if it is disabled in your browser.
DevOps and modern engineering have enabled us to provide higher quality code at greater speeds by introducing guardrails and checks into our automated continuous integration (CI) and continuous deployment (CD) processes. However, with security becoming a more pressing matter as more critical zero-day threats arise and misconfigurations are introduced to production systems, while at the same time as application and development processes all moving to more automated CI/CD processes––this is becoming a critical point for enforcing security validations and checks.
With DevSecOps coming a long way as a discipline, there are now great frameworks and best practices for applying security gates in your CI, and later CD.
We'd like to provide a practical guide for doing so in cloud-native environments, and particularly Kubernetes environments. These security gates will enable you to detect early and prevent known security issues from reaching production, such as documented vulnerabilities, common misconfigurations, permissions, and others. CI/CD Security gates include not only the technical controls that need to be applied but also the way we think about security posture, risk appetite, and how to continuously enforce cloud-native security in an ongoing manner.
We believe that security can be embedded as early as your first line of YAML, upon pulling your container images, scanning, deploying, and then even in ongoing post-deployment continuous security monitoring; all with open-source tooling. In addition, with the ability to leverage widely adopted developer tooling from VSCode, CLIs, and GitHub Actions, all of these checks can be included from within existing developer workflows and context.
CI Security Hygiene Needs a Hard Reset
CI security receives far less attention than other areas of application and cloud security. Let's not even talk about security, let's take quality as an example. You have an endless number of linters or compilers that will return warnings if there are errors in the code. There are even grammar-checking tools for README files (A LOT!), probably even more than those that check for security. In the same way, we as developers, are obsessed with our code and grammar hygiene, how are we not equally concerned with our CI security hygiene?
As we all know and have heard many times through the “shift left” manifesto, the earlier we apply security in the process the better this will be from every kind of perspective––cost, effort, and time. However, likely the most critical piece is catching issues early before they propagate and manifest to production, but also with sufficient context (for non-security experts) to actually be able to do something meaningful about it.
There is also a common misconception that security needs to be a heavy lift, and bog down development processes, and I'd like to bust some of these myths and enable you to adopt security as you write your code, through your CI and CD, rinse and repeat.  
Common CICD Pipeline
Security Gate #1: Prevention During Coding
Security hygiene starts as early as the first lines of code you write – whether it's JSON, YAML, Helm charts, or anything else, there are well-known misconfigurations and vulnerabilities that can be caught during coding.
Kubescape VSCode Extension
With the open-source Kubescape VSCode extension, you receive in-editor notifications while writing YAML about potential security issues by marking the relevant lines in your manifest files. This saves the extra step of having to scan your config files after you have already completed the work and enables developers while still in context to make immediate changes and edits.
In addition, these alerts can also enforce security hygiene based on known and popular security frameworks like NSA-CISA and MITRE ATT&CK and other K8s-related compliance frameworks. You can also build an internal or custom security framework, that contains common misconfigurations that can be custom-defined and continuously updated, such as avoiding privilege escalation through least-privilege practices, and best practice resource limitations.  
Highlighting potential security issues while doing in VS Code with Kubescape
By proactively adding security controls into your coding, you can minimize the number of vulnerabilities your scanning tools will later find, and lower the noise level. This matters in the context of security scanning tools, as they will always find misconfigurations and vulnerabilities––and this creates a lot of alert fatigue and what we call “CVE Shock”. This overwhelms developers – not knowing where to get started with remediating these known vulnerabilities and issues.
Security Gate #2: Detection Through Code Repository Scanning
After we've written the configuration code, the natural next step is to push it through our CI (usually via the CLI) and try to get our Pull Request (PR) merged into our codebase. However, a good security practice is to nonetheless scan your public and private code repositories and your container image registries before deploying to production, as there are always additional security considerations with your stack, tools, supply chain, and registries.
Kubescape CI Config & CLI
This is where the Kubescape CLI comes in handy.
The Kubescape CLI can scan any of the common Kubernetes / CI configuration files including YAML, JSON, and even their output in the XML & JUnit formats. It can also scan your config based on common and well-known security frameworks like MITRE, NSA, or CIS, or by your own custom-defined security framework of choice.
Because the threat and vulnerability landscapes are constantly growing, be forewarned, it will always find vulnerabilities (sometimes many), that are then categorized by severity. This is when good security practices and processes are important.
We'll start by saying that you DO NOT need to resolve and remediate every issue immediately, but a security best practice is to acknowledge all of the vulnerabilities and to create exceptions when you choose not to fix them. This way there is a log for the process, as well as a decision owner, and full context to the vulnerability.
This means that whenever you run a security scan, you should always do the following once there are findings:
Acknowledge the findings (in a log)
Fix or Ignore them
In addition to this, you can also define many different parameters that enable you to make the right fix / ignore security decisions, such as:
Risk threshold
When to fail/pass a build (based on severity or the risk threshold defined)
Custom frameworks
Exceptions
This is the GitOp s way to apply security from a CI/CD perspective and enables the ongoing prioritization of security threat remediation based on how lucrative the fix is.  
Scanning Kubernetes workload definitions files (YAML) with Kubescape CLI
Kubescape & GitHub Actions
GitHub Actions are becoming a popular way to configure simple pipelines and CI processes for GitHub repositories. Therefore, in the same way, that you can leverage Kubescape, you can also utilize GitHub Actions.
In addition to the same features and capabilities you receive from the CLI, the GitHub Actions support also makes it possible to receive visualizations and graphical representations right inside your GitHub repository. It also enables CI security scanning to happen directly inside developer workflows and context without the need to add any additional solutions.  
Example: Running Kubescape from GitHub actions  
Example: Showing Kubescape scan results in GitHub
Security Gate #3: Detection Through Container Image Registry Scanning
One commonly accepted Kubernetes security best practice is ensuring that any resources we take off the public web are thoroughly scanned, to ensure the end-to-end security of everything in our software supply chain. And this isn't limited to just our code imports and packages, but also to the containers we use and the registries we employ.
Another thing we have learned along the way is that if security isn't embedded into existing processes, it very often simply won't happen. That is why you need container image registry scanning that enables you to scan images directly from their registries (e.g., ECR, GCR, quay.io, and more) before they are deployed and run in the cluster.
This is an incredibly important security guardrail that can be easily applied and automated, to ensure that vulnerabilities are detected during the development process from third-party registries, and like the previous guardrails––have some mechanism in place to prevent vulnerabilities from reaching deployments and production environments from this vector, as well.  
Container image registry scanning by Kubescape cloud
This leads us to our next guardrail, as security is never simply a one-off scan.
Security Gate 4: Continuous Security Post-Deployment
We've spoken about good practices and tooling when it comes to CI security, but security is a living, breathing, and continuous process, and it doesn't end once your PR is merged. We need to have the proper guardrails in place, to monitor for ongoing threats as they emerge.
Therefore, while we scanned our registries during our CI security process, what happens if threats emerge for container registries and configurations already running in production? This is where CD security good practices are required.
By proactively requiring security scanning upon a compelling event (e.g. if someone changed something in the system), according to a predefined schedule (daily, weekly, monthly), or when a security vulnerability is discovered––you can detect if the CVE exists in your production systems or discover potential configuration drift. This means you don't have to have already strapped security engineers continuously monitoring for security threats, you can create a greater sense of ownership for security on the entire team, through continuous and ongoing security that will alert you to new threats in your running operations, without any specific security domain expertise.
By ensuring CI security starts as early as the code, then adding gates before deployment and more checks post-deployment you can provide end-to-end security controls throughout your CI/CD processes, and minimize the potential of vulnerabilities leaking into production systems. When we apply security controls early, and natively into development processes, we create shared ownership and understanding that security cannot be an afterthought with the complexity of cloud-native systems.  
Embedding security gates into CI/CD pipeline
Share
Read Next Post 
The First Runtime Behavioral Cloud Application Detection & Response { CADR }
Watch a Demo
Related Articles
[
Apr 10, 2026
How to Triage an AI Agent Execution Graph: A Three-Tier Decision Framework for Security Teams
A platform security engineer gets an alert at 2:14 a.m. One of the LangChain agents... Yossi Ben Naim VP of Product Management](https://www.armosec.io/blog/how-to-triage-an-ai-agent-execution-graph-a-three-tier-decision-framework-for-security-teams/)
[
Apr 10, 2026
AI Workload Baseline and Drift Detection: Defining “Normal” Agent Behavior
Security teams deploying AI agents into Kubernetes know they need behavioral baselines. The concept is... Ben Hirschberg CTO & Co-founder](https://www.armosec.io/blog/ai-workload-baseline-drift-detection/)
[
Apr 1, 2026
Detecting Rogue AI Agents: Tool Misuse and API Abuse at Runtime
When your CNAPP flags a suspicious dependency in an AI agent container, your WAF logs... Yossi Ben Naim VP of Product Management](https://www.armosec.io/blog/ai-agent-tool-misuse-api-abuse/)  
Your Cloud Security Advantage Starts Here
Webinars
Data Sheets
Surveys and more
Explore the Hub  
Ben Hirschberg CTO & Co-Founder  
Rotem Refael VP R&D  
Amit Schendel Security researcher 
Company
About us
Careers
News
Contact us
ARMO Platfrom
Get a demo
Sign up
Pricing
Docs
Powered by Kubescape
Cloud Security Resources
Blog
Glossary
CVE Database
Copyright © 2026 ARMO Ltd
Privacy Policy
Cookies Policy  
Continue to Slack
Get the information you need directly from our experts!
 Continue as a guest Cancel
× 
Zoom In Zoom Out
