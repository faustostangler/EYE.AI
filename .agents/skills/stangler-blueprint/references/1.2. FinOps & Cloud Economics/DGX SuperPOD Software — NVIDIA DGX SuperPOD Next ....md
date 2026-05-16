---
name: DGX SuperPOD Software — NVIDIA DGX SuperPOD: Next ...
keywords: (placeholder)
metadata:
  url: https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-gb200/latest/dgx-software.html
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
DGX SuperPOD Software — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX GB200
Skip to main content 
Back to top Ctrl + K
 NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX GB200
Search Ctrl + K
Search Ctrl + K
 NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX GB200
Table of Contents
Reference Architecture
Abstract
DGX SuperPOD Architecture
Key Components of the DGX SuperPOD
Network Fabrics
Storage Architecture
DGX SuperPOD Software
Summary
Notices
Notices
DGX SuperPOD Software
Is this page helpful?
DGX SuperPOD Software#
NVIDIA Mission Control software delivers a full-stack data center solution engineered for enterprise infrastructure deployments, like NVIDIA DGX SuperPOD. It integrates essential management and operational capabilities into a unified platform, providing enterprise customers with seamless control over their infrastructure deployments at scale.
Figure 20 shows the detailed decomposition of DGX GB200 SuperPOD software stack. 
Figure 20 NVIDIA DGX GB200 SuperPOD Software Stack#
NVIDIA Mission Control software stack comprises a five-layer architecture that builds from foundational system health and diagnostics to advanced NVIDIA DGX SuperPOD cluster management operations. It leverages NVIDIA Base Command Manager (BCM) technology and NVIDIA Run:ai functionality to provide scheduler access with SLURM and Kubernetes for AI and HPC workload orchestration. The Telemetry and Observability layer leverages proprietary diagnostic tools and health-checks for system insights, while the Validation and Diagnostics layer, supports the built-in autonomous recovery engine that ensures rapid failure recovery and system restoration with minimal time to recovery.
NVIDIA Mission Control also handles deployment optimization and system health monitoring, seamlessly cooperating NVIDIA Base Command Manager (BCM) technology for coordinating cluster provisioning & operations. Included in the software stack there is also Network Management eXpert (NMX) for monitoring & control of NVLINK Switch trays.
NVIDIA Mission Control delivers critical innovations that directly impact DL and HPC environments, improving efficiency, reducing downtime, and optimizing resource utilization. Here's how these advancements translate into tangible business value:
Automated Failure Detection & Self-Recovery: NVIDIA Mission Control's automated failure detection and recovery mechanisms significantly minimize downtime compared to manual interventions. With faster recovery times, AI training continues without significant disruption, resulting in improved GPU utilization. This reduces the risk of resource wastage.
Optimized Workload Migration & Resource Allocation: NVIDIA Mission Control ensures that workloads are continuously reassigned to healthy nodes, preventing idle GPU time. This leads to increased overall GPU efficiency, enabling the system to process more workloads within the same timeframe. By optimizing resource allocation, NVIDIA Mission Control helps organizations achieve higher throughput for AI training tasks, thereby accelerating time-to-results.
Unified Diagnostics for Infrastructure & Applications: By combining infrastructure and application-level diagnostics, NVIDIA Mission Control helps significantly reduce troubleshooting time. Model builders can identify and resolve issues much faster compared to traditional methods. This considerably decreases the operational burden on SREs and DevOps, leading to savings in personnel costs and reducing the time to production.
In-Memory Checkpointing for Seamless Job Recovery: NVIDIA Mission Control enables recovery of training workloads by automatically restarting failed processes/ranks from the most recent valid checkpoint, ensuring no data loss or rework. In environments with frequent failures, it significantly reduces retraining time, thereby eliminating downtime and preventing interruptions in the training loop. This results in an increase in model iteration speed and faster go-to-market timelines for AI products.
Run:ai#
Included with NVIDIA Mission Control, the Run:ai platform employs a distributed architecture consisting of two primary components: the control plane (backend) and the cluster. The control plane serves as the central management system, capable of orchestrating multiple Run:ai clusters across an organization. For BCM-managed installations, the control plane is hosted on the control plane while cluster components are deployed directly onto the customer's Kubernetes infrastructure. This separation of responsibilities allows for centralized management while maintaining workload execution close to computational resources.
Figure 21 showcases the architecture of NVIDIA Run:ai 
Figure 21 NVIDIA Run:ai#
previous Storage Architecture
next Summary
On this page
Run:ai
Privacy Policy | Your Privacy Choices | Terms of Service | Accessibility | Corporate Policies | Product Security | Contact
Copyright © 2024-2025, NVIDIA Corporation.
Last updated on Nov 19, 2025.
NVIDIA uses cookies to improve your experience on our web site. We and our third-party partners also use cookies and other tools to collect and record information you provide as well as information about your interactions with our websites for performance improvement, analytics, and to assist in marketing efforts. By continuing to use this site or by clicking one of the buttons below, you agree to the use of cookies and other tools as described in our Privacy Policy and Cookie Policy (subject to your settings) and accept our Terms of Service (which contains important waivers). Please see our Privacy Policy for more information on our privacy practices.
We have detected the Global Privacy Control (GPC) signal and have opted you out of all optional cookies on this site for this browser. You can manage your cookie settings by clicking on "Manage Settings". Please see our Cookie Policy for more information. To opt out of non-cookie personal information "sales" / "sharing" for targeted advertising purposes, please visit the NVIDIA Preference Center. Please see our Privacy Policy for more information on our privacy practices.
We have detected the Global Privacy Control Signal (GPC) and have opted you out of all optional cookies on this browser. You can manage your cookie settings by clicking on "Manage Settings". Please see our Cookie Policy for more information. We have also opted you out of "sharing"/"sales" of personal information outside of cookies. You can manage these settings in the NVIDIA NVIDIA Preference Center. Please see our Privacy Policy for more information.
We have detected the Global Privacy Control Signal (GPC) and have opted you out of all optional cookies on this browser. You can manage your cookie settings by clicking on "Manage Settings". Please see our Cookie Policy for more information. We have also opted you out of "sharing"/"sales" of personal information outside of cookies which overrides at least one of your previous settings. You can manage them in the NVIDIA Preference Center. Please see our Privacy Policy for more information.
Manage Settings
Turn Off Optional Cookies Agree 
Cookie Settings
We and our third-party partners (including social media, advertising, and analytics partners) use cookies and other tracking technologies to collect, store, monitor, and process certain information about you when you visit our website. The information collected might relate to you, your preferences, or your device. We use that information to make the site work, analyze performance and traffic on our website, provide a more personalized web experience, and assist in our marketing efforts.
Under certain privacy laws, you have the right to direct us not to "sell" or "share" your personal information for targeted advertising. To opt-out of the "sale" and "sharing" of personal information through cookies, you must opt-out of optional cookies using the toggles below. To opt out of the "sale" and "sharing" of data collected by other means (e.g., online forms) you must also update your data sharing preferences through the NVIDIA Preference Center.
Click on the different category headings below to find out more and change the settings according to your preference. You cannot opt out of Required Cookies as they are deployed to ensure the proper functioning of our website (such as prompting the cookie banner and remembering your settings, etc.). By clicking "Save and Accept" or "Decline All" at the bottom, you consent to the use of cookies and other tools as described in our Cookie Policy in accordance with your settings and accept our Terms of Service (which contains important waivers). For more information about our privacy practices, please see our Privacy Policy.
Required Cookies
Always Active
These cookies enable core functionality such as security, network management, and accessibility. These cookies are required for the site to function and cannot be turned off.
Cookies Details
Performance Cookies [-]
Performance Cookies
These cookies are used to provide quantitative measures of our website visitors, such as the number of times you visit, time on page, your mouse movements, scrolling, clicks and keystroke activity on the websites; other browsing, search, or product research behavior; and what brought you to our site. These cookies may store a unique ID so that our system will remember you when you return. Information collected with these cookies is used to measure and find ways to improve website performance.
Cookies Details
Personalization Cookies [-]
Personalization Cookies
These cookies collect data about how you have interacted with our website to help us improve your web experience, such as which pages you have visited. These cookies may store a unique ID so that our system will remember you when you return. They may be set by us or by third party providers whose services we have added to our pages. These cookies enable us to provide enhanced website functionality and personalization as well as make the marketing messages we send to you more relevant to your interests. If you do not allow these cookies, then some or all of these services may not function properly.
Cookies Details
Advertising Cookies [-]
Advertising Cookies
These cookies record your visit to our websites, the pages you have visited and the links you have followed to influence the advertisements that you see on other websites. These cookies and the information they collect may be managed by other companies, including our advertising partners, and may be used to build a profile of your interests and show you relevant advertising on other sites. We and our advertising partners will use this information to make our websites and the advertising displayed on it, more relevant to your interests.
Cookies Details
Cookie List
Clear
[-] checkbox label label
Apply Cancel
Consent Leg.Interest [-]
checkbox label label [-]
checkbox label label [-]
checkbox label label
Decline All Save and Accept
