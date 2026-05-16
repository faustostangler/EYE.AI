---
name: Centralize access to security logs (Secure Future Initiative) - Microsoft Learn
keywords: (placeholder)
metadata:
  url: https://learn.microsoft.com/en-us/security/zero-trust/sfi/centralize-access-to-security-logs
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T19:00:57.430Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
Centralize access to security logs - Microsoft Secure Future Initiative | Microsoft Learn
Skip to main content Skip to Ask Learn chat experience
Microsoft Build 2026
June 2-3, 2026
Go deep on real code and real systems in San Francisco and online
Learn more
Dismiss alert
This browser is no longer supported.
Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support.
Download Microsoft Edge More info about Internet Explorer and Microsoft Edge
Learn 
Suggestions will filter as you type
Sign in  
Profile
Analytics
Settings
Sign out 
Learn
Documentation
All product documentation
Azure documentation
Dynamics 365 documentation
Microsoft Copilot documentation
Microsoft 365 documentation
Power Platform documentation
Code samples
Troubleshooting documentation Register now. Spots filling fast Microsoft Build Build, ship, and scale with AI-first tools and platforms.
Training & Labs
All training
Azure training
Dynamics 365 training
Microsoft Copilot training
Microsoft 365 training
Microsoft Power Platform training
Labs
Credentials
Career paths Register now. Spots filling fast Microsoft Build Build, ship, and scale with AI-first tools and platforms.
Q&A
Ask a question
Azure questions
Windows questions
Microsoft 365 questions
Microsoft Outlook questions
Microsoft Teams questions
Popular tags
All questions Register now. Spots filling fast Microsoft Build Build, ship, and scale with AI-first tools and platforms.
Topics
Agents Key concepts and resources for agentic computing
Artificial intelligence Learning hub to build AI skills
DevOps DevOps practices, Git version control and Agile methods
Learn for Organizations Curated offerings from Microsoft to boost your team's technical skills
Platform engineering Tools from Microsoft and others to build personalized developer experiences
Security Guidance to help you tackle security challenges
Assessments Interactive guidance with custom recommendations
Student hub Self-paced and interactive training for students
Educator center Resources for educators to bring technical innovation in their classroom Register now. Spots filling fast Microsoft Build Build, ship, and scale with AI-first tools and platforms.
Suggestions will filter as you type
Sign in  
Profile
Analytics
Settings
Sign out
Microsoft Security
Product documentation
AI shared responsibility model
Microsoft Defender
Microsoft Defender for Cloud
Microsoft Entra
Microsoft Purview
Microsoft Sentinel
Microsoft Intune
Secure Azure
Secure Microsoft 365
Microsoft Security Copilot
Security training
Self-paced learning paths
Security, compliance, and identity training
Microsoft Entra training
Microsoft Defender training
Microsoft Purview training
Security certifications
Instructor-led security training
Cloud Games
Architecture
Reference architectures
Cloud Adoption Framework for Azure
Azure Well-Architected
Cybersecurity architect learner journey assessment
Resources
Engage
Connect with community
Learn for Organizations
Microsoft Secure
Training Services Partners
Virtual Training Days
Reference architecture videos
CISO workshop
Security tech communities
Security blog
Security YouTube
Hub extras
Top picks archive
More
Product documentation
AI shared responsibility model
Microsoft Defender
Microsoft Defender for Cloud
Microsoft Entra
Microsoft Purview
Microsoft Sentinel
Microsoft Intune
Secure Azure
Secure Microsoft 365
Microsoft Security Copilot
Security training
Self-paced learning paths
Security, compliance, and identity training
Microsoft Entra training
Microsoft Defender training
Microsoft Purview training
Security certifications
Instructor-led security training
Cloud Games
Architecture
Reference architectures
Cloud Adoption Framework for Azure
Azure Well-Architected
Cybersecurity architect learner journey assessment
Resources
Engage
Connect with community
Learn for Organizations
Microsoft Secure
Training Services Partners
Virtual Training Days
Reference architecture videos
CISO workshop
Security tech communities
Security blog
Security YouTube
Hub extras
Top picks archive
Table of contents Exit editor mode
Learn
Security
Zero Trust
Learn
Security
Zero Trust
Ask Learn Ask Learn
Reading mode Table of contents Read in English Add to Collections Add to plan Edit
Copy Markdown Print
Note
Access to this page requires authorization. You can try signing in or changing directories.
Access to this page requires authorization. You can try changing directories.
Centralize access to security logs (Secure Future Initiative)
Feedback
Summarize this article for me
In this article
Context and problem
Solution
Guidance
Benefits
Trade-offs
Key success factors
Summary
Show 3 more
Pillar name: Monitor and detect threats
Pattern name: Centralize access to security logs
Security logs are essential for monitoring threats and supporting investigations, but without centralization and standardization, they can create more management overhead and slow down response times. Microsoft addressed these challenges by centralizing log access, standardizing data capture, and extending retention periods, enabling faster, more effective investigations. These measures, alongside AI-powered detection and expanded log retention for customers, improve overall security and forensic capabilities.
Context and problem
Security logs are critical tools for security staff, as they reveal who accessed what, when, and how. Logs support continuous monitoring of threat activity, speed up incident response, and provide forensic records for security investigations.
Yet without centralization and standardization, logs can create more problems than they solve. Inconsistent formats, disparate storage locations, and variable retention periods make it difficult to quickly piece together a complete picture of an attack. At Microsoft, investigations were slowed by fragmented log sources and gaps in retention that left security teams unable to trace initial access points or lateral movement paths.
Solution
As part of SFI, Microsoft centralized access to security logs and extended retention policies. Key measures include:
Standardized security logging library: Ensures consistent data capture across services, reducing observability gaps.
Centralized log collection: Specialized investigator accounts provide unified access to cross-service logs, simplifying correlation and speeding up investigations.
Extended log retention: Audit logs retained for up to two years across Microsoft services, to enable forensic investigation of long-term attack patterns.
Advanced detection analytics: Integration of machine learning and AI-powered models improves detection of complex attack techniques and reduces false positives.
Expanded customer logging: Microsoft increased standard audit log retention for Microsoft 365 customers to 180 days, with options for longer retention.
Guidance
Organizations can adopt a similar pattern using the following actionable practices:
Expand table
Use case
Recommended action
Resource
Standardized logging
Use Microsoft Purview auditing solution for Microsoft Entra and Microsoft 365 applications logs (for example, Exchange Online, SharePoint, OneDrive).
Implement a common log library across applications and services to enforce consistent fields (identity, actions, timestamps).
Learn about auditing solutions in Microsoft Purview
Microsoft Sentinel data lake overview
Central log storage
Use Microsoft Sentinel's data lake to transform SIEM with AI and unified security data.
Direct all security logs into a central repository, accessible to authorized investigators.
Centralize access to logs with Azure's Monitor and Log Analytics to reduce blind spots.
Use Microsoft Sentinel's security information and event management (SIEM) solution to enhance visibility and context for security logs and data, threat investigation, and response.
Microsoft Sentinel data lake overview - Microsoft Security
Azure Monitor Logs
Microsoft Sentinel data connectors
Microsoft Entra security operations for infrastructure
Encryption and immutable storage
In Azure Monitor, you can secure log data in transit and encrypt Log Analytics data at rest in Azure Storage using Microsoft-managed keys (MMK)
Encrypt logs in transit and at rest, and store them immutably to preserve forensic integrity, using Microsoft Sentinel's data tiering for cost-efficient retention.
We recommend using immutable to protect from overwrites and deletes.
Log Analytics workspace overview
Secure your Azure Monitor deployment
Encryption at rest in Azure Storage
Immutable storage
Manage data tiers and retention in Microsoft Sentinel
Real-time monitoring
Set up continuous monitoring and alerts with Azure Monitor and Microsoft Sentinel to detect suspicious activity or logging coverage gaps.
In Azure Monitor and Log Analytics, you can monitor, improve logging coverage, and alert on suspicious activities using KQL queries and alert rules
Microsoft Sentinel provides advanced monitoring and detection features such as real-time log ingestion, analytics rules to watch ingested data, log matching against threat intelligence, alert grouping into incidents, and security orchestration, automation, and response (SOAR) capabilities.
Log queries in Azure Monitor
Azure Monitor diagnostics settings
Monitor Azure resources with Azure Monitor
Log ingestion with data connectors
Detect and analyze anomalies using KQL in Azure Monitor
Quick threat detection with near-real-time (NRT) analytics rules in Microsoft Sentinel
Advanced analytics
Correlate logs across services using AI/ML and integrate with threat intelligence feeds.
Correlate logs in Azure Monitor and Log Analytics using KQL queries to connect signals across data sources.
Apply advanced analytics in Microsoft Sentinel with prebuilt rule libraries that map to common attack patterns, user and entity behavior analytics (UEBA) for anomaly detection, AI-powered alert correlation, ML-driven anomaly detection, and logs enriched with threat intelligence.
Microsoft Sentinel documentation
Threat detection in Microsoft Sentinel
Advanced threat detection with User and Entity Behavior Analytics (UEBA) in Microsoft Sentinel
Alert correlation in Microsoft Sentinel
Threat intelligence - Microsoft Sentinel
Review cadence
Conduct quarterly reviews to validate coverage, retention compliance, and pipeline integration.
Optimize SOC processes with Microsoft best practices and guidance on security operations.
Azure Monitor best practices
Optimize security operations
Benefits
Improved visibility: Provides security teams with a unified view of activity across identities, infrastructure, applications and endpoint devices.
Faster investigations: Investigators can correlate events across services without manual searches or format conversion.
Forensic readiness: Extended retention ensures security teams can analyze long-term attack campaigns.
Proactive detection: AI-driven analytics surface emerging attack patterns earlier.
Regulatory alignment: Supports compliance with standards requiring centralized, retained audit evidence.
Trade-offs
Increased storage costs: Extending retention and centralizing logs requires scalable infrastructure.
Access governance complexity: Centralized investigator accounts must be strictly controlled to prevent misuse.
Operational overhead: Teams must maintain log libraries, pipelines, and monitoring tools across services.
Signal-to-noise balance: Centralized logging increases data volume, requiring investment in advanced filtering and analytics.
Key success factors
To track success, measure the following:
Percentage of services using the standardized logging library.
Number of pipelines and services successfully forwarding logs to the central repository.
Mean time to investigate (MTTI) reduced by centralized access.
Compliance with two-year audit log retention standard.
Detection accuracy improvements from AI/ML-enhanced analytics.
Summary
Centralizing access to security logs transforms fragmented monitoring data into actionable intelligence. By standardizing log formats, consolidating collection, extending retention, and applying AI-driven analytics, Microsoft has improved both the speed and effectiveness of its threat detection and investigation.
Organizations can adopt this approach by ensuring consistent log formats, enforcing central storage and immutability, extending retention for forensic readiness, and integrating logs with advanced analytics platforms. These steps enable security teams to monitor and detect threats with clarity and precision---turning logs from scattered records into a powerful, unified security capability.
Centralize your security logs today to reduce blind spots, accelerate investigations, and stay ahead of evolving threats.
Feedback
Was this page helpful?
Yes No No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
Additional resources
Last updated on 10/06/2025
In this article
Context and problem
Solution
Guidance
Benefits
Trade-offs
Key success factors
Summary
Was this page helpful?
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
Ask Learn
Preview
Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
Sign in
English (United States)
Your Privacy Choices
Theme
Light
Dark
High contrast
AI Disclaimer
Previous Versions
Blog
Contribute
Privacy
Consumer Health Privacy
Terms of Use
Trademarks
© Microsoft 2026
