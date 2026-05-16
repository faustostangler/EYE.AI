---
name: Introducing Cloud Storage object retention lock | Google Cloud Blog
keywords: (placeholder)
metadata:
  url: https://cloud.google.com/blog/products/storage-data-transfer/introducing-cloud-storage-object-retention-lock
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T19:00:57.430Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
Introducing Cloud Storage object retention lock | Google Cloud Blog
cloud.google.com uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. Learn more
OK, got it
Jump to Content
Cloud
Blog
Contact sales Get started for free
Cloud
Blog
Solutions & technology
Security
Ecosystem
Industries
Solutions & technology
Ecosystem
Developers & Practitioners
Transform with Google Cloud
AI & Machine Learning
API Management
Application Development
Application Modernization
Chrome Enterprise
Compute
Containers & Kubernetes
Data Analytics
Databases
DevOps & SRE
Maps & Geospatial
Security
Infrastructure
Infrastructure Modernization
Networking
Productivity & Collaboration
SAP on Google Cloud
Storage & Data Transfer
Sustainability
Security & Identity
Threat Intelligence
IT Leaders
Industries
Partners
Startups & SMB
Training & Certifications
Inside Google Cloud
Google Cloud Next & Events
Google Cloud Consulting
Google Maps Platform
Google Workspace
Financial Services
Healthcare & Life Sciences
Manufacturing
Media & Entertainment
Public Sector
Retail
Supply Chain
Telecommunications
Solutions & technology
AI & Machine Learning
API Management
Application Development
Application Modernization
Chrome Enterprise
Compute
Containers & Kubernetes
Data Analytics
Databases
DevOps & SRE
Maps & Geospatial
Security
Security & Identity
Threat Intelligence
Infrastructure
Infrastructure Modernization
Networking
Productivity & Collaboration
SAP on Google Cloud
Storage & Data Transfer
Sustainability
Ecosystem
IT Leaders
Industries
Financial Services
Healthcare & Life Sciences
Manufacturing
Media & Entertainment
Public Sector
Retail
Supply Chain
Telecommunications
Partners
Startups & SMB
Training & Certifications
Inside Google Cloud
Google Cloud Next & Events
Google Cloud Consulting
Google Maps Platform
Google Workspace
Developers & Practitioners
Transform with Google Cloud
Contact sales Get started for free
Storage & Data Transfer
Boosting data cyber-resilience for your Cloud Storage data with object retention lock
April 4, 2024
Subhasish Chakraborty
Group Product Manager
Karthik Gangidi
Product Manager
Data retention is crucial for customers especially in regulated industries such as financial services, healthcare, and government. Customers can use write once, read many (WORM) storage to meet their data retention needs, keeping their data immutable, and comply with industry regulations set forth by governing bodies such as FINRA, SEC, and CFTC. WORM storage can also provide an extra layer of security to organizations dealing with sensitive data, by preventing any data modifications or deletions and reducing the risk of accidental data loss, data breaches, and unauthorized alterations.
We are now making it easier for our customers to configure WORM storage, and meet regulatory standards, strengthen security posture, and improve data protection with the new object retention lock for Cloud Storage. It adds to existing WORM storage capabilities such as bucket lock and object holds in Cloud Storage, and can give organizations flexibility to manage data retention at the desired granularity level: either objects or buckets.
How does object retention lock work?
Object retention lock can help you set and lock retention configurations on Cloud Storage objects, with a “retain until time.” This means that an object with an object retention lock can not be deleted or replaced until the retain until time has passed.
Based on your data retention management needs, you can also choose to use both bucket lock and object retention lock at the same time. If an object has a bucket lock and an objection retention lock simultaneously applied, the object can not be deleted until each “retain until time” has elapsed.
Object retention lock is available through the Google Cloud Storage console, Cloud Storage APIs, gCloud CLI, and client libraries.
To enable object retention lock through the Google Cloud Storage Console:
Check the “Enable Object Retention” box when configuring your bucket.  
Configure “Retain until time” for the objects you want to make immutable.  
Choose whether you want to lock the retention policy. Once locked, you can not lower the “retain until time”.  
Objects can not be deleted or overwritten until the configured “retain until time” has elapsed.  
Keep costs down and deliver low latency
Object retention lock does not require you to enable object versioning in Cloud Storage. This means you can use object retention and still get object deduplication in your storage when performing operations like backups.
Cloud Storage is also unique by providing consistent low latency characteristics across storage classes, even for colder storage tiers. With this you benefit by selecting the appropriate storage class without having to compromise your object retention lock requirements. Customers can thus leverage their retained data for active, data intensive use-cases such as Data Analytics or AI/ML as well through instant access provided by Cloud Storage.
What customers saying about object retention lock
A number of Google Cloud Storage customers and partners have begun using object retention lock. Customers are also using data protection partners leveraging object retention lock for Cyber Resilience through immutable vault solutions on Cloud Storage. Here's what they are saying:
“The constant threat of ransomware continues to evolve with hackers increasingly attacking backup data as an organizations' most valuable asset. The immutable storage capabilities of Object Lock will provide Veritas customers who choose Google Cloud as a target for their backups with another layer of defense, so they have zero doubt their mission-critical data is protected,” said Matt Waxman, senior vice president and general manager, Data Protection, Veritas.
“Customers' data is growing exponentially, and companies need to make sure their backup capabilities can support this with ease and at-scale. They must do this with better storage efficiency and the ability to keep their data safe for different periods of time. Object retention lock and HYCU's Cloud Dedup together provide an invaluable layer of protection and defense combined with the storage efficiency that customers desire. The tremendous partnership we have with Google provides both our on-prem customers and our cloud-native customers the peace of mind they all want,” said Subbiah Sundaram, senior vice president, Product, HYCU.
“In the evolving threat landscape, Google Cloud Storage's object retention lock offers Commvault customers a strong defense mechanism against ransomware. We're leveraging this critical feature for our immutable storage on Google Cloud, offering our customers an unalterable layer of ransomware protection. And with its consistent low latencies across storage classes and deduplication-friendly implementation, it delivers tremendous value to our customers,” said Victor Bishay, director, worldwide alliances, Commvault.
Getting started with object retention lock
Object retention lock is generally available, and you can enable your buckets for object retention lock now. Object retention lock is available in all locations where Cloud Storage is available and across all storage classes. It also works with Object Lifecycle Management (OLM) and Autoclass. If you enable object retention lock while your objects are in the Standard storage class, the lock remains in place even as the object shifts between storage classes.
Cloud Storage object retention lock has been assessed for SEC 17a-4(f), FINRA, and CFTC Regulations by Cohasset Associates. Cohasset determined that Cloud Storage meets the WORM requirement when properly configured and used with the Retention Policy feature in locked mode.
For more information and detailed instructions on how to enable object retention lock and set retention times on objects, refer to the documentation here.
Posted in
Storage & Data Transfer
Security & Identity
Related articles
[ Storage & Data Transfer
Cloud Storage Rapid: Turbocharged object storage for AI and analytics
By Marco Abela • 7-minute read](https://cloud.google.com/blog/products/storage-data-transfer/cloud-storage-rapid-turbocharges-object-storage-for-ai-analytics)
[ Storage & Data Transfer
Storage innovations to accelerate your AI workloads at Next '26
By Sameet Agarwal • 9-minute read](https://cloud.google.com/blog/products/storage-data-transfer/next26-storage-announcements)
[ Compute
Cross-cloud infrastructure innovation for the agentic enterprise
By Nirav Mehta • 9-minute read](https://cloud.google.com/blog/products/compute/cross-cloud-infrastructure-at-next26)
[ Containers & Kubernetes
New GKE Cloud Storage FUSE Profiles take the guesswork out of configuring AI storage
By Nishtha Jain • 4-minute read](https://cloud.google.com/blog/products/containers-kubernetes/optimize-aiml-workloads-with-gke-cloud-storage-fuse-profiles)
Footer Links
Follow us
 
Google Cloud
Google Cloud Products
Privacy
Terms
Cookies management controls
Help
Language English Deutsch Français 한국어 日本語
