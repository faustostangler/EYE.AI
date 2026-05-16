---
name: Access tiers for blob data - Azure Storage - Microsoft Learn
keywords: (placeholder)
metadata:
  url: https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Access tiers for blob data - Azure Storage | Microsoft Learn
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
Azure
Products
Popular products
Microsoft Foundry
Azure App Service
Azure Databricks
Azure DevOps
Azure Functions
Azure Monitor
Azure Virtual Machines
Popular categories
Compute
Networking
Storage
AI & machine learning
Analytics
Databases
Security
View all products
Architecture
Cloud Adoption Framework
Well-Architected Framework
Azure Architecture Center
Migration
Develop
Python
.NET
JavaScript
Java
PowerShell
Azure CLI
View all developer resources
Learn Azure
Start your AI learning assessment
Top learning paths
Cloud concepts
AI fundamentals
Intro to generative AI
Azure Architecture fundamentals
Earn credentials
Instructor-led courses
View all training
Troubleshooting
Resources
Product overview
Azure updates
Pricing information
Cost management & billing
Latest blog posts
Support options
More
Products
Popular products
Microsoft Foundry
Azure App Service
Azure Databricks
Azure DevOps
Azure Functions
Azure Monitor
Azure Virtual Machines
Popular categories
Compute
Networking
Storage
AI & machine learning
Analytics
Databases
Security
View all products
Architecture
Cloud Adoption Framework
Well-Architected Framework
Azure Architecture Center
Migration
Develop
Python
.NET
JavaScript
Java
PowerShell
Azure CLI
View all developer resources
Learn Azure
Start your AI learning assessment
Top learning paths
Cloud concepts
AI fundamentals
Intro to generative AI
Azure Architecture fundamentals
Earn credentials
Instructor-led courses
View all training
Troubleshooting
Resources
Product overview
Azure updates
Pricing information
Cost management & billing
Latest blog posts
Support options
Portal Get started with Azure
Table of contents Exit editor mode
Learn
Azure
Storage
Blobs
Learn
Azure
Storage
Blobs
Ask Learn Ask Learn
Reading mode Table of contents Read in English Add to Collections Add to plan Edit
Copy Markdown Print
Note
Access to this page requires authorization. You can try signing in or changing directories.
Access to this page requires authorization. You can try changing directories.
Access tiers for blob data
Feedback
Summarize this article for me
In this article
Online access tiers
Archive access tier
Minimum billable object size on cooler tiers
Default account access tier setting
Setting or changing a blob's tier
Blob lifecycle management
Storage Actions
Summary of access tier options
Pricing and billing
Cold tier
Feature support
Next steps
Show 8 more
Data stored in the cloud grows at an exponential pace. To manage costs for your expanding storage needs, it can be helpful to organize your data based on how frequently it will be accessed and how long it will be retained. Azure storage offers different access tiers so that you can store your blob data in the most cost-effective manner based on how it's being used. Azure Storage access tiers include:
Hot tier - An online tier optimized for storing data that is accessed or modified frequently. The hot tier has the highest storage costs, but the lowest access costs.
Cool tier - An online tier optimized for storing data that is infrequently accessed or modified. Data in the cool tier should be stored for a minimum of 30 days. The cool tier has lower storage costs and higher access costs compared to the hot tier.
Cold tier - An online tier optimized for storing data that is rarely accessed or modified, but still requires fast retrieval. Data in the cold tier should be stored for a minimum of 90 days. The cold tier has lower storage costs and higher access costs compared to the cool tier.
Archive tier - An offline tier optimized for storing data that is rarely accessed, and that has flexible latency requirements, on the order of hours. Data in the archive tier should be stored for a minimum of 180 days.
Smart tier - Smart tier automatically moves your data between the hot, cool, and cold access tiers based on usage patterns, optimizing your costs for these access tiers automatically. To learn more, see Optimize costs with smart tier.
Azure storage capacity limits are set at the account level, rather than according to access tier. You can choose to maximize your capacity usage in one tier, or to distribute capacity across two or more tiers.
Note
Setting the access tier is only allowed on Block Blobs. They are not supported for Append and Page Blobs.
Online access tiers
When your data is stored in an online access tier (either hot, cool or cold), users can access it immediately. The hot tier is the best choice for data that is in active use. The cool or cold tier is ideal for data that is accessed less frequently, but that still must be available for reading and writing.
Example usage scenarios for the hot tier include:
Data that's in active use or data that you expect will require frequent reads and writes.
Data that's staged for processing and eventual migration to the cool access tier.
Usage scenarios for the cool and cold access tiers include:
Short-term data backup and disaster recovery.
Older data sets that aren't used frequently, but are expected to be available for immediate access.
Large data sets that need to be stored in a cost-effective way while other data is being gathered for processing.
To learn how to move a blob to the hot, cool, or cold tier, see Set a blob's access tier.
Data in the cool and cold tiers have slightly lower availability, but offer the same high durability, retrieval latency, and throughput characteristics as the hot tier. For data in the cool or cold tiers, slightly lower availability and higher access costs may be acceptable trade-offs for lower overall storage costs, as compared to the hot tier. For more information, see SLA for storage.
Blobs are subject to an early deletion penalty if they are deleted, overwritten or moved to a different tier before the minimum number of days required by the tier have transpired. For example, a blob in the cool tier in a general-purpose v2 account is subject to an early deletion penalty if it's deleted or moved to a different tier before 30 days has elapsed. For a blob in the cold tier, the deletion penalty applies if it's deleted or moved to a different tier before 90 days has elapsed. This charge is prorated. For example, if a blob is moved to the cool tier and then deleted after 21 days, you'll be charged an early deletion fee equivalent to 9 (30 minus 21) days of storing that blob in the cool tier. Early deletion charges also occur if the entire object is rewritten through any operation (i.e. Put Blob, Put Block List, or Copy Blob) within the specified time window. This charge is prorated based on the data storage price of the corresponding tier, i.e. deleting an archived blob after 120 days will lead to this object being charged for 180 days.
Note
In an account that has soft delete enabled, a blob is considered deleted after it is deleted and retention period expires. Until that period expires, the blob is only soft-deleted and is not subject to the early deletion penalty.
The hot, cool, and cold tiers support all redundancy configurations. For more information about data redundancy options in Azure Storage, see Azure Storage redundancy.
Archive access tier
The archive tier is an offline tier for storing data that is rarely accessed. The archive access tier has the lowest storage cost. However, this tier has higher data retrieval costs with a higher latency as compared to the hot, cool, and cold tiers. Example usage scenarios for the archive access tier include:
Long-term backup, secondary backup, and archival datasets
Original (raw) data that must be preserved, even after it has been processed into final usable form
Compliance and archival data that needs to be stored for a long time and is hardly ever accessed
To learn how to move a blob to the archive tier, see Archive a blob.
Data must remain in the archive tier for at least 180 days or be subject to an early deletion charge. For example, if a blob is moved to the archive tier and then deleted or moved to the hot tier after 45 days, you'll be charged an early deletion fee equivalent to 135 (180 minus 45) days of storing that blob in the archive tier.
Note
In an account that has soft delete enabled, a blob is considered deleted after it is deleted and retention period expires. Until that period expires, the blob is only soft-deleted and is not subject to the early deletion penalty.
While a blob is in the archive tier, it can't be read or modified. To read or download a blob in the archive tier, you must first rehydrate it to an online tier, either hot, cool, or cold. Data in the archive tier can take up to 15 hours to rehydrate, depending on the priority you specify for the rehydration operation. For more information about blob rehydration, see Overview of blob rehydration from the archive tier.
An archived blob's metadata remains available for read access, so that you can list the blob and its properties, metadata, and index tags. Metadata for a blob in the archive tier is read-only, while blob index tags can be read or written. Storage costs for metadata of archived blobs will be charged on cool tier rates. Snapshots aren't supported for archived blobs.
The following operations are supported for blobs in the archive tier:
Copy Blob
Delete Blob
Undelete Blob
Find Blobs by Tags
Get Blob Metadata
Get Blob Properties
Get Blob Tags
List Blobs
Set Blob Tags
Set Blob Tier
Only storage accounts that are configured for LRS, GRS, or RA-GRS support moving blobs to the archive tier. The archive tier isn't supported for ZRS, GZRS, or RA-GZRS accounts. For more information about redundancy configurations for Azure Storage, see Azure Storage redundancy.
To change the redundancy configuration for a storage account that contains blobs in the archive tier, you must first rehydrate all archived blobs to the hot, cool, or cold tier. Because rehydration operations can be costly and time-consuming, Microsoft recommends that you avoid changing the redundancy configuration of a storage account that contains archived blobs.
Migrating a storage account from LRS to GRS is supported as long as no blobs were moved to the archive tier while the account was configured for LRS.
Minimum billable object size on cooler tiers
For storage accounts that use Azure Blob Storage or Azure Data Lake Storage, a minimum billable object size of 128 KiB applies to objects stored in the cool, cold, and archive access tiers. Objects in these tiers that are smaller than 128 KiB are billed as 128 KiB objects at the rate for the corresponding tier. Billing uses the existing capacity billing meters (data stored), and there is no change to transaction billing.
This billing behavior will be introduced in two stages:
July 1, 2026: The billing behavior applies to all new storage accounts created on or after this date. There is no change for existing storage accounts.
July 1, 2027: The billing behavior applies to all storage accounts.
The creation time of a storage account, which is part of the account-level metadata, determines which stage applies.
The hot access tier continues to have no minimum billable object size. To reduce potential cost impact, consider packaging small objects into larger objects before moving data to cooler tiers, or using smart tier to automatically keep small objects on the hot access tier.
To support this change, the Blob Capacity metrics in the Azure portal will introduce new blob types: BlockBlobSmall and Azure Azure Data Lake Storage Small.
Note
Customers with existing dashboards, alerts, cost reports, or automation that explicitly depend on the BlockBlob blob type should review and update those workflows accordingly.
Workflows that assume all block blobs are reported under the BlockBlob datatype may return incomplete or unexpected results once these new datatypes appear in capacity metrics.
Default account access tier setting
Storage accounts have a default access tier setting that indicates the online tier in which a new blob is created. The default access tier setting can be set to either hot, cool or cold. Users can override the default setting for an individual blob when uploading the blob or changing its tier.
The default access tier for a new general-purpose v2 storage account is set to the hot tier by default. You can change the default access tier setting when you create a storage account or after it's created. If you don't change this setting on the storage account or explicitly set the tier when uploading a blob, then a new blob is uploaded to the hot tier by default.
A blob that doesn't have an explicitly assigned tier infers its tier from the default account access tier setting. If a blob's access tier is inferred from the default account access tier setting, then the Azure portal displays the access tier as Hot (inferred), Cool (inferred), or Cold (inferred).
Changing the default access tier setting for a storage account applies to all blobs in the account for which an access tier hasn't been explicitly set. If you toggle the default access tier setting to a cooler tier in a general-purpose v2 account, then you're charged for write operations (per 10,000) for all blobs for which the access tier is inferred. You're charged for both read operations (per 10,000) and data retrieval (per GB) if you toggle to a warmer tier in a general-purpose v2 account.
When you create a legacy Blob Storage account, you must specify the default access tier setting as hot or cool at create time. There's no charge for changing the default account access tier setting to a cooler tier in a legacy Blob Storage account. You're charged for both read operations (per 10,000) and data retrieval (per GB) if you toggle to a warmer tier in a Blob Storage account. Microsoft recommends using general-purpose v2 storage accounts rather than Blob Storage accounts when possible.
Note
The archive tier is not supported as the default access tier for a storage account.
Setting or changing a blob's tier
To explicitly set a blob's tier when you create it, specify the tier when you upload the blob.
After a blob is created, you can change its tier in either of the following ways:
By calling the Set Blob Tier operation, either directly or via a lifecycle management policy. Calling Set Blob Tier is typically the best option when you're changing a blob's tier from a warmer tier to a cooler one. Note You can't rehydrate an archived blob to an online tier by using lifecycle management policies.
By calling the Copy Blob operation to copy a blob from one tier to another. Calling Copy Blob is recommended for most scenarios where you're rehydrating a blob from the archive tier to an online tier, or moving a blob from cool or cold to hot. By copying a blob, you can avoid the early deletion penalty, if the required storage interval for the source blob hasn't yet elapsed. However, copying a blob results in capacity charges for two blobs, the source blob and the destination blob.
Changing a blob's tier from a warmer tier to a cooler one is instantaneous, as is changing from cold or cool to hot. Rehydrating a blob from the archive tier to an online tier such as the hot, cool, or cold tier can take up to 15 hours.
Keep in mind the following points when changing a blob's tier:
You can't use Set Blob Tier to archive a blob that uses an encryption scope. You can only use Set Blob Tier to move between online access tiers. For more information about encryption scopes, see Encryption scopes for Blob storage.
If a blob is explicitly moved to the cool or cold tier and then moved to the archive tier, the early deletion charge applies.
Blob lifecycle management
Blob storage lifecycle management offers a rule-based policy that you can use to transition your data to the desired access tier when your specified conditions are met. You can also use lifecycle management to expire data at the end of its life. See Optimize costs by automating Azure Blob Storage access tiers to learn more.
You can't rehydrate an archived blob to an online tier by using lifecycle management policies. Data stored in a premium block blob storage account cannot be tiered to hot, cool, cold or archive by using Set Blob Tier or using Azure Blob Storage lifecycle management. To move data, you must synchronously copy blobs from the block blob storage account to the hot tier in a different account using the Put Block From URL API or a version of AzCopy that supports this API. The Put Block From URL API synchronously copies data on the server, meaning the call completes only once all the data is moved from the original server location to the destination location.
Storage Actions
While lifecycle management helps you move data between tiers in a single account, you can use a storage task to accomplish this task at scale across multiple accounts. A storage task is a resource available in Azure Storage Actions; a serverless framework that you can use to perform common data operations on millions of objects across multiple storage accounts. To learn more, see What is Azure Storage Actions?
Summary of access tier options
The following table summarizes the features of the hot, cool, cold, and archive access tiers.
Expand table
Objects in the cool tier on general-purpose v2 accounts have a minimum retention duration of 30 days. Objects in the cold tier on general-purpose v2 accounts have a minimum retention duration of 90 days. For Blob Storage accounts, there's no minimum retention duration for the cool or cold tier. 2
When rehydrating a blob from the archive tier, you can choose either a standard or high rehydration priority option. Each offers different retrieval latencies and costs. For more information, see Overview of blob rehydration from the archive tier. 3
For more information about redundancy configurations in Azure Storage, see Azure Storage redundancy.
Pricing and billing
All storage accounts use a pricing model for block blob storage that is based on a blob's tier. Keep in mind the billing considerations described in the following sections.
For more information about pricing for block blobs, see Block blob pricing.
Storage capacity costs
In addition to the amount of data stored, the cost of storing data varies depending on the access tier. The per-gigabyte capacity cost decreases as the tier gets cooler. Objects in the cool, cold, and archive tiers that are smaller than 128 KiB might be billed as 128 KiB objects, depending on when the storage account was created. For details, see Minimum billable object size on cooler tiers.
Data access costs
Data access charges increase as the tier gets cooler. For data in the cool, cold and archive access tier, you're charged a per-gigabyte data access charge for reads.
Transaction costs
A per-transaction charge applies to all tiers and increases as the tier gets cooler.
Geo-replication data transfer costs
This charge only applies to accounts with geo-replication configured, including GRS, RA-GRS and GZRS. Geo-replication data transfer incurs a per-gigabyte charge.
Outbound data transfer costs
Outbound data transfers (data that is transferred out of an Azure region) incur billing for bandwidth usage on a per-gigabyte basis. For more information on outbound data transfer charges, see Bandwidth Pricing Details page.
Changing the default account access tier
Changing the account access tier results in tier change charges for all blobs that don't already have a tier explicitly set. For more information, see the following section, Changing a blob's access tier.
Changing a blob's access tier
Keep in mind the following billing impacts when changing a blob's tier:
When a blob is uploaded or moved between tiers, it's charged at the corresponding rate immediately upon upload or tier change.
When a blob is moved to a cooler tier, the operation is billed as a write operation (per 10,000) to the destination tier. An additional data write (per GB) charge applies when moving blobs to a cooler tier within a legacy Blob Storage account.
When a blob is moved to a warmer tier, the operation is billed as a read from the source tier, where the read operation (per 10,000) and data retrieval (per GB) charges of the source tier apply. Early deletion charges for any blob moved out of the cool, cold or archive tier may apply as well.
While a blob is being rehydrated from the archive tier, that blob's data is billed as archived data until the data is restored and the blob's tier changes to hot, cool, or cold.
The following table summarizes how tier changes are billed.
Expand table
Changing the access tier for a blob when versioning is enabled, or if the blob has snapshots, might result in more charges. For information about blobs with versioning enabled, see Pricing and billing in the blob versioning documentation. For information about blobs with snapshots, see Pricing and billing in the blob snapshots documentation.
Cold tier
The cold tier requires the following minimum versions of REST, SDKs, and tools
Expand table
Feature support
Support for this feature might be impacted by enabling Data Lake Storage Gen2, Network File System (NFS) 3.0 protocol, or the SSH File Transfer Protocol (SFTP). If you've enabled any of these capabilities, see Blob Storage feature support in Azure Storage accounts to assess support for this feature.
Next steps
Set a blob's access tier
Archive a blob
Optimize costs by automatically managing the data lifecycle
Best practices for using blob access tiers
Feedback
Was this page helpful?
Yes No No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
Additional resources
Training
Module
Manage the Azure Blob Storage Lifecycle - Training
Learn how to manage data availability throughout the Azure Blob storage lifecycle.
Last updated on 04/13/2026
In this article
Online access tiers
Archive access tier
Minimum billable object size on cooler tiers
Default account access tier setting
Setting or changing a blob's tier
Blob lifecycle management
Storage Actions
Summary of access tier options
Pricing and billing
Cold tier
Feature support
Next steps
Show 3 more
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
