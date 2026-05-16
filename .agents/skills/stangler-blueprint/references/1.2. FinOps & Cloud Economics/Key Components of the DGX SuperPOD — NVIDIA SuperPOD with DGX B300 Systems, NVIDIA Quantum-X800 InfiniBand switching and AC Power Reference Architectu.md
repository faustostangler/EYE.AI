---
name: Key Components of the DGX SuperPOD — NVIDIA SuperPOD with DGX B300 Systems, NVIDIA Quantum-X800 InfiniBand switching and AC Power Reference Architecture
keywords: (placeholder)
metadata:
  url: https://docs.nvidia.com/dgx-superpod/reference-architecture/scalable-infrastructure-b300-xdr/latest/dgx-superpod-components.html
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Key Components of the DGX SuperPOD — NVIDIA SuperPOD with DGX B300 Systems, NVIDIA Quantum-X800 InfiniBand switching and AC Power Reference Architecture
Skip to main content 
Back to top Ctrl + K
 NVIDIA SuperPOD with DGX B300 Systems, NVIDIA Quantum-X800 InfiniBand switching and AC Power Reference Architecture
Search Ctrl + K
Search Ctrl + K
 NVIDIA SuperPOD with DGX B300 Systems, NVIDIA Quantum-X800 InfiniBand switching and AC Power Reference Architecture
Table of Contents
Reference Architecture
Abstract
Key Components of the DGX SuperPOD
DGX SuperPOD Architecture
Network Fabrics
High Performance Storage Architecture
Management Servers
DGX SuperPOD Software
Summary
Major Components
Notices
Notices
Key Components of the DGX SuperPOD
Is this page helpful?
Key Components of the DGX SuperPOD#
The DGX SuperPOD architecture has been designed to maximize performance for state-of-the-art model training, scale to exaflops of performance, provide the highest performance to storage and support all customers in the enterprise, higher education, research, and the public sector. It is a digital twin of the main NVIDIA research and development system, meaning the company's software, applications, and support structure are first tested and vetted on the same architecture. By using SUs, system deployment times are reduced from months to weeks. Leveraging the DGX SuperPOD design reduces time-to-solution and time-to-market of next generation models and applications.
DGX SuperPOD is the integration of key NVIDIA components, as well as storage solutions from partners certified to work in the DGX SuperPOD environment.
NVIDIA DGX B300 System#
The NVIDIA DGX B300 system ( Figure 1) is an AI powerhouse that enables enterprises to expand the frontiers of business innovation and optimization. The DGX B300 system delivers breakthrough AI performance with the most powerful chips ever built, in an eight GPU configuration. The NVIDIA Blackwell Ultra GPU architecture provides the latest technologies that brings months of computational effort down to days and hours, on some of the largest AI/ML workloads.
Figure 1 DGX B300 system#
Some of the key highlights of the DGX B300 system when compared to the DGX B200 system include:
InfiniBand XDR or Spectrum-X 2.0 based compute fabric
Alternative DC Busbar powered appliance design available, fully N+N redundant
72 petaFLOPS FP8 training and 144 petaFLOPS FP4 inference
Fifth generation of NVIDIA NVLink.
2.1 TB of aggregated HBM3e memory
NVIDIA InfiniBand Technology#
InfiniBand is a high-performance, low latency, RDMA capable networking technology, proven over 20 years in the harshest compute environments to provide the best inter-node network performance. InfiniBand continues to evolve and lead data center network performance.
NVIDIA InfiniBand XDR has a peak speed of 800 Gbps per direction with an extremely low port-to-port latency and is backwards compatible with the previous generations of InfiniBand specifications. InfiniBand is more than just peak bandwidth and low latency. InfiniBand provides additional features to optimize performance including Adaptive Routing (AR), collective communication with SHARP TM, dynamic network healing with SHIELD TM, and supports several network topologies.
NVIDIA InfiniBand NDR with a peak speed of 400 Gbps per direction with the same extremely low port-to-port latency is used for Storage Fabric for fast and reliably storage access to feed the data required for AI training.
NVIDIA Mission Control#
The DGX SuperPOD Reference Architecture represents the best practices for building high-performance AI factories. There is flexibility in how these systems can be presented to customers and users. NVIDIA Mission Control software is used to manage all DGX SuperPOD with DGX B300 systems deployments.
NVIDIA Mission Control is a sophisticated full-stack software solution. As an essential part of the DGX SuperPOD experience, it optimizes developer workload performance and resiliency, ensures unmatched uptime with automated failure handling, and provides unified cluster-scale telemetry and manageability. Key features include full-stack resiliency, predictive maintenance, unified error reporting, data center optimizations, cluster health checks, and automated node management.
NVIDIA Mission Control software incorporates the same technology that NVIDIA uses to manage thousands of systems for our award-winning data scientists and provides an immediate path to an AI factory for organizations that need the best of the best.
DGX SuperPOD is to be deployed on-premises, meaning the customer owns and manages the hardware. This can be within a customer's data center or co-located at a commercial data center. In each case the customer owns the hardware, the service it provides, and is responsible for their cluster infrastructure as well as providing the building management system for integration.
Components#
The hardware components of DGX SuperPOD are described in Table 1. The software components are shown in Table 2.
Table 1 DGX SuperPOD hardware components by NVIDIA#
Table 2 DGX SuperPOD software components#
Note
NVIDIA Mission Control now includes Base Command Manager and Run:ai functionality. No separate purchase is needed. SuperPOD only supports multiteam environments through Base Command Manager; multitenancy is not supported with SuperPOD currently.
Design Requirements#
DGX SuperPOD is designed to minimize system bottlenecks throughout the tightly coupled configuration to provide the best performance and application scalability. Each subsystem has been thoughtfully designed to meet this goal. In addition, the overall design remains flexible so that data center requirements can be tailored to better integrate into existing data centers.
System Design#
DGX SuperPOD is optimized for a customers' particular workload of multi-node AI and HPC applications:
A modular architecture based on SUs of 72 DGX B300 systems each.
A fully tested system scales to 8 SUs, but larger deployments can be built based on customer requirements.
Single rack that can support up to four DGX B300 systems per rack, enabling modification to accommodate different data center requirements if there is additional power and cooling capacity.
Storage partner equipment that has been certified to work in DGX SuperPOD environments.
Full system support, including compute, storage, network, and Mission Control software is provided by NVIDIA Enterprise Experience (NVEX).
Compute Fabric#
The compute fabric is rail-optimized, full-fat tree topology
Managed Quantum-X800 switches are used throughout the design to provide better management of the fabric.
Storage Fabric (High Speed Storage)#
The storage fabric provides high bandwidth to shared storage. It also has the following characteristics:
It is independent of the compute fabric to maximize performance of both storage and application performance.
Storage is provided over InfiniBand or RDMA over Converged Ethernet to provide maximum performance and minimize CPU overhead.
It is flexible and can scale to meet specific capacity and bandwidth requirements.
Connectivity to management nodes is required to provide storage access independent of compute nodes.
In-Band Management Network#
The in-band management network fabric is Ethernet-based and is used for node provisioning, data movement, Internet access, and other services that must be accessible by the users.
The in-band management network connections for compute and management nodes operate at 200 Gbps and are bonded for resiliency.
Out-of-Band Management Network#
The OOB management network connects all the base management controller (BMC) ports, as well as other devices that should be physically isolated from users. The Switch Management Network is a subset of the Out-Of-Band Network that provides additional security and resiliency.
Storage Requirements#
The DGX SuperPOD compute architecture must be paired with a high-performance, balanced, storage system to maximize overall system performance. DGX SuperPOD is designed to use two separate storage systems, high-performance storage (HPS) and user storage, optimized for key operations of throughput, parallel I/O, as well as higher IOPS and metadata workloads.
High-Performance Storage#
High-Performance Storage is provided via InfiniBand or high-speed Ethernet connected storage from a DGX SuperPOD certified storage partner, and is engineered and tested with the following attributes in mind:
High-performance, resilient, POSIX-style file system optimized for multi-threaded read and write operations across multiple nodes.
RDMA on InfiniBand or Ethernet support
Local system RAM for transparent caching of data.
Leverage local flash device transparently for read and write caching. The specific storage fabric topology, capacity, and components are determined by the DGX SuperPOD certified storage partner as part of the DGX SuperPOD design process.
User Storage#
User Storage differs from High-Performance storage in that it exposes an NFS share on the in-band management fabric for multiple uses. It is typically used for “home directory” type usage (especially with clusters deployed with Slurm), administrative scratch space, and shared storage as needed by DGX SuperPOD components in a High Availability configuration (e.g., Base Command Manager), and log files.
With that in mind, User Storage has the following minimum requirements:
100 - 400Gbps Ethernet connectivity with 100G SerDes connectivity is required.
Designed for high metadata performance, IOPS, and key enterprise features such as checkpointing. This is different than the HPS, which is optimized for parallel I/O and large capacity.
Communicate over Ethernet, using NFS. User storage in a DGX SuperPOD is often satisfied with existing NFS servers already deployed, such that a new export is created and made accessible to the DGX SuperPOD's in-band management network. For the best performance, we require 100 Gb/s minimum bandwidth for the user storage.
Footnotes
[ 1]
NVIDIA Mission Control includes Base Command Manager and Run:ai functionality. No separate purchase needed.
previous Abstract
next DGX SuperPOD Architecture
On this page
NVIDIA DGX B300 System
NVIDIA InfiniBand Technology
NVIDIA Mission Control
Components
Design Requirements
System Design
Compute Fabric
Storage Fabric (High Speed Storage)
In-Band Management Network
Out-of-Band Management Network
Storage Requirements
High-Performance Storage
User Storage
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
