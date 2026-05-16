---
name: Differences to expect when migrating from Azure Cosmos DB to Amazon DynamoDB - AWS
keywords: (placeholder)
metadata:
  url: https://aws.amazon.com/blogs/database/differences-to-expect-when-migrating-from-azure-cosmos-db-to-amazon-dynamodb/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Differences to expect when migrating from Azure Cosmos DB to Amazon DynamoDB | AWS Database Blog
Select your cookie preferences
We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.
If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”
Accept Decline Customize
Customize cookie preferences
We use cookies and similar tools (collectively, "cookies") for the following purposes.
Essential
Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.
Performance
Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes. [x]
Allowed
Functional
Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly. [x]
Allowed
Advertising
Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising. [x]
Allowed
Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the AWS Cookie Notice .
Cancel Save preferences
Your privacy choices
We and our advertising partners (“we”) may use information we collect from or about you to show you ads on other websites and online services. Under certain laws, this activity is referred to as “cross-context behavioral advertising” or “targeted advertising.”
To opt out of our use of cookies or similar technologies to engage in these activities, select “Opt out of cross-context behavioral ads” and “Save preferences” below. If you clear your browser cookies or visit this site from a different device or browser, you will need to make your selection again. For more information about cookies and how we use them, read our Cookie Notice . [x] allowed
Allow cross-context behavioral ads [-] not allowed Opt out of cross-context behavioral ads
To opt out of the use of other identifiers, such as contact information, for these activities, fill out the form here .
For more information about how AWS handles your information, read the AWS Privacy Notice .
Cancel Save preferences
Unable to save cookie preferences
We will only store essential cookies at this time, because we were unable to save your cookie preferences.
If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.
Dismiss
Skip to Main Content 
Filter: All
English
Contact us
AWS Marketplace
Support
My account
More
Search Filter: All
Sign in to console
Create account
AWS Blogs
AWS Database Blog
Differences to expect when migrating from Azure Cosmos DB to Amazon DynamoDB
by Utsav Joshi and Joydeep Dutta on 27 JAN 2023 in Advanced (300), Amazon DynamoDB, Technical How-to Permalink Comments Share
 https://aws.amazon.com/blogs/database/differences-to-expect-when-migrating-from-azure-cosmos-db-to-amazon-dynamodb/
Customers who are considering migrating their Azure Cosmos DB workloads to Amazon DynamoDB ask what differences to expect. In this post, we discuss the differences to expect and plan for when migrating from Azure Cosmos DB to DynamoDB. DynamoDB is a serverless key-value database optimized for common access patterns, typically to store and retrieve large volumes of data. It's a fully managed, multi-Region, active-active database that provides consistent single-digit millisecond latency at any scale, encryption at rest, backup and restore, and in-memory caching. DynamoDB is commonly used as part of event-driven architectures, which enable you to use other AWS services to extend DynamoDB capabilities.
Terminology and architectural comparison
Azure Cosmos DB and DynamoDB are both NoSQL databases, but there are architectural and terminology differences that you must consider before you begin a migration.
Table 1: DynamoDB and Azure Cosmos DB terminology and architectural comparison
Amazon DynamoDB tables, schema, and indexes
To keep migration simple, keep one-to-one mapping between Azure Cosmos DB collections and DynamoDB tables. DynamoDB doesn't have a concept of a database as such; instead, it has entities called tables. When creating a DynamoDB table based on an Azure Cosmos DB collection:
Choose a partition key that has high cardinality. DynamoDB uses the partition key's value as an input to an internal hash function. The output from the hash function determines the partition in which the item is stored. Each item's location is determined by the hash value of its partition key. In most cases, items with the same partition key are stored together in an item collection, which is defined as a group of items with the same partition key but different sort keys. For tables with composite primary keys, the sort key can be used as a partition boundary. DynamoDB splits virtual partitions by sort key if the collection size grows beyond 10 GB. A sort key can also be used to replace a primary composite index on Azure Cosmos DB. See Choosing the Right DynamoDB Partition Key for a more detailed discussion on how to choose a partition key.
For a query pattern that requires the same partition key and a different sort key, you can create either a GSI or an LSI during the main table creation along with the non-key attributes. You can create a GSI either during or after table creation, along with the non-key attributes Note: GSI is the preferred option. When using LSI, the total size of indexed items for any one partition key value can't exceed 10 GB.
For a query pattern where there are different primary and sort keys, a GSI is recommended. You can create a GSI during or after the main table creation along with the non-key attributes. If you are importing DynamoDB data from Amazon Simple Storage Service (Amazon S3), a GSI will be added during the import. Local and global secondary indexes, once defined, are automatically maintained by DynamoDB. Secondary indexes help reduce the size of the data as compared to the base table. The reduced size of the secondary index depends upon the number of non-key attributes used and helps improve provisioned throughput performance. When you create a GSI on a provisioned-mode table, you must specify read and write capacity units for the expected workload on that index. The provisioned throughput settings of a GSI are separate from those of its base table. A query operation on a GSI consumes read capacity units from the index, not the base table. When you put, update, or delete items in a table, the global secondary indexes on that table are updated asynchronously. These index updates consume write capacity units from the index, not from the base table. If you're projecting the table attributes to your GSI, it's recommended that you set the provisioned write capacity units to a value that is equal to or greater than the write capacity of the base table because new updates write to both the base table and GSI. A GSI update requires two writes: one to delete the previous item from the index and another write to put the new item into the index when you're updating an attribute that is the GSI partition key or sort key.
Azure Cosmos DB supports two or more properties in composite indexes. It can be mapped to a DynamoDB primary key and secondary index with a concatenated sort key. For example, if Azure Cosmos DB has Employee ID, Country, State, and City fields defined as a composite key, replace Employee ID as a partition key and the sort key as country#state#city on DynamoDB. Note, # on a sort key is a user specified delimiter and can be changed to some other delimiter such as a colon ( : ), comma ( , ) or tilde ( ~ ).
DynamoDB supports Azure Cosmos DB data types and additionally supports the Binary and Set data types. For attribute mapping from Azure Cosmos DB to DynamoDB, refer to Table 2:
Table 2: DynamoDB attribute mapping
DynamoDB indexes are different from Azure Cosmos DB. Azure Cosmos DB uses an inverted index, while DynamoDB uses a hashing algorithm for the table and index partitions. When migrating the Azure Cosmos DB nested JSON indexes, the Azure Cosmos DB indexed attributes must be a part of the primary key, LSIs, or GSIs on DynamoDB. Nested non-indexed objects can be added as a map data type.
There is no equivalent to Azure Cosmos DB stored procedures or user-defined functions in DynamoDB, but it's possible to run an equivalent functionality with AWS Lambda or a combination of DynamoDB Streams and Lambda. The DynamoDB client owns the responsibility of post-processing on DynamoDB data.
Capacity units
DynamoDB offers a read capacity unit (1 RCU is 4 KB per second for a strong consistency read and 8 KB per second for an eventual consistency read) and write capacity unit (1 WCU is 1 KB per second write on a DynamoDB table). To understand your DynamoDB RCU and WCU requirements, we suggest running DynamoDB in on-demand mode. Running a load test with your table in on-demand mode before completing the migration will verify that the application and tables are optimized for the live traffic. For spiky traffic patterns, continue with DynamoDB on-demand mode. For a predictable usage pattern, use the baseline details from the load test to set up provisioned capacity. It's a recommended practice to use auto-scaling with provisioned capacity so DynamoDB can scale as your application traffic grows and avoid errors that may result from having insufficient throughput provisioned.
For global tables, write capacity settings should be set consistently across your replica tables and secondary indices in each Region used. The read capacity settings on a global table's replica should be based on Regional read requirements.
Time-to-Live (TTL)
You can port Azure Cosmos DB time to live (TTL) settings to DynamoDB. You must convert the Azure Cosmos DB TTL in seconds to epoch time on DynamoDB. DynamoDB TTL allows you to define a per-item timestamp to determine when an item is no longer needed. Within 48 hours of the timestamp indicating the item is no longer needed, DynamoDB deletes the item from the table without consuming write throughput. TTL is provided at no extra cost as a means to reduce stored data volumes by retaining only the items that remain current for the workload's needs.
DynamoDB granular access
Azure Cosmos DB provides built-in role-based access control (RBAC). DynamoDB uses AWS Identity and Access Management (IAM) to provide granular access at the item and attribute level. IAM policies regulate access to items and attributes stored in DynamoDB tables. Following are some two examples of fine-grained access control:
A mobile app that displays information for nearby airports based on the user's location. The app can access and display attributes such as airline names, arrival times, and flight numbers. However, it cannot access or display pilot names or passenger counts.
A mobile game that stores high scores for users in a single table. Each user can update their own scores but has no access to update the scores of other players.
Amazon DynamoDB DAX for micro-second performance
If you're using third-party caching solutions for micro second responses on reads on Azure Cosmos DB, you have the option of using Amazon DynamoDB Accelerator (DAX). DAX allows you to incorporate a caching solution without code refactoring. DAX is an eventually consistent write-thru caching layer for DynamoDB. You can use DAX in read through mode, write through mode, or write around mode, based on their needs.
Re-architecting Azure Cosmos DB Change Feed to DynamoDB
Azure Cosmos DB propagates changes to other Azure services using Azure Cosmos DB Change Feed. DynamoDB offers two streaming options for change data capture (CDC): Amazon Kinesis Data Streams and Amazon DynamoDB Streams. Each streaming option caters to use cases as described in the following paragraphs.
Use Kinesis Data Streams for use cases such as log data capture, real-time metrics and reporting, real-time data analytics, and complex stream processing. Use Data Streams when record ordering and duplication isn't critical (you can handle duplicates on the final destination to achieve idempotent processing). For example, with Amazon OpenSearch Service, you can use a combination of versioning and unique IDs to prevent duplicated processing, when you need multiple consumers to process streams in parallel with unlimited throughput, and when you need more than 24 hours of data retention.
DynamoDB Streams captures a time-ordered stream of changes and retains this information in a log for up to 24 hours. You can then use the DynamoDB Streams Kinesis adapter and the DynamoDB Streams API from within the application to read data records from a dedicated endpoint. You can also use Lambda with automatic scaling to process data from DynamoDB streams.
When using DynamoDB Streams, the Kinesis adapter is the preferred option to consume streaming data. The DynamoDB Streams Kinesis adapter automates shard management (expiration and splitting of shards) on the application's behalf, along with additional benefits as documented in Using the DynamoDB Streams Kinesis adapter to process stream records. Lambda can be used to initiate DynamoDB insert, update, or delete events. Consider using DynamoDB Streams with Lambda triggers to replace Azure Cosmos DB triggers.
Please refer to DynamoDB Streams Use Cases and Design Patterns for a more detailed discussion on using DynamoDB Streams and to the DynamoDB documentation for a more detailed comparison of Kinesis Data Streams and DynamoDB Streams.
Handling items larger than 400 KB
The maximum item size in DynamoDB is 400 KB, which includes both attribute name binary length (UTF-8 length) and attribute value lengths (binary length). There are several options available in DynamoDB to address items larger than 400 KB, such as using compression algorithms like GZIP before inserting items, and splitting large items into several smaller items. Alternatively, you can save these large objects in an S3 bucket and then store the S3 object URLs in a DynamoDB table as attributes. This approach lets you use a DynamoDB index for fast lookups and S3 as a highly durable and cost-effective object store.
As an example, suppose an application keeps track of employee records (name, address, and other information) and also needs to store a 600×400 pixel image of each employee. In this case, the item size for a single employee exceeds the 400 KB limit. Additionally, the user must update a human resource application as soon as the employee item is inserted into DynamoDB. You can store the image in an S3 bucket with the URL of the image stored as an attribute of the employee Item. You can use DynamoDB Streams to initiate a Lambda function to update the HR application. Figure 1 that follows illustrates the approach. 
Figure 1: Architecture for handling large Item size
See Large object storage strategies for Amazon DynamoDB and Use vertical partitioning to scale data efficiently in Amazon DynamoDB for a more detailed discussion of the solution options mentioned in this post.
Global and Regional tables
DynamoDB global tables is a fully managed solution for deploying a multi-Region, active-active database without having to build and maintain your own cross-region replication solution. You can specify the AWS Regions where you want the tables to be available and DynamoDB propagates ongoing data changes to the tables through those Regions. It allows low-latency data access to your users no matter where they are located. You can easily use DynamoDB global tables in place of Azure Cosmos DB global data replication. DynamoDB provides asynchronous replication to sync up with replicas and usually takes less than one second to replicate across Regions. In the case of replica conflicts, DynamoDB global tables use a last writer wins model, for which DynamoDB makes a best effort to determine the last writer. DynamoDB global tables are ideal for geographically distributed applications with globally dispersed users.
Amazon DynamoDB backup and restore capabilities
DynamoDB provides several options to backup and restore your data. You can use point-in-time recovery (PITR) to protect your DynamoDB tables from accidental write or delete operations. PITR continuously backs up your data enabling you to restore your table(s) to any point in time during the last 35 days using the AWS Management Console, the AWS Command Line Interface (AWS CLI), or the DynamoDB API. With PITR, you don't have to worry about creating, maintaining, or scheduling on-demand backups. You can also use the DynamoDB on-demand backup capability to create full backups of your tables for long-term retention, and archiving for regulatory compliance needs. Both PITR and on-demand backups don't affect your table's performance or API latencies.
Migrate Azure Cosmos DB data to DynamoDB
Follow the steps below to migrate data from Azure Cosmos DB to DynamoDB:
Use the Azure Azure Data Explorer to export data in CSV format.
Once the data is in CSV format, use AWS Database Migration Service (AWS DMS) to migrate to DynamoDB. See Migrate Delimited Files from Amazon S3 to an Amazon DynamoDB NoSQL Table Using AWS Database Migration Service and AWS CloudFormation for a tutorial on AWS DMS.
Use DMS to sync-up the data.
You can migrate Cosmos DB using AWS Glue. See Migrate from Azure Cosmos DB to Amazon DynamoDB using AWS Glue for more details.
You can also import table data from Amazon S3. See Amazon DynamoDB can now import Amazon S3 data into a new table for more details.
Conclusion
In this post, you learned the relevant feature differences between Azure Cosmos DB and DynamoDB and architecture patterns to consider during migration. Even though there are differences, there is a clear path to adjust for them. For more details on strategies for global secondary index sharding and index overloading, scalable graph processing with materialized queries, relational modeling with composite keys, and executing transactional workflows on DynamoDB refer to DynamoDB Deep Dive: Advanced Design Patterns.
If you have any questions or suggestions, leave a comment.
About the Authors
**  Utsav Joshi** is a Principal Technical Account Manager at AWS. He lives in New Jersey and enjoys working with AWS customers in solving architectural, operational, and cost optimization challenges. In his spare time, he enjoys traveling, road trips, and playing with his kids. 
Joydeep Dutta is a Senior Solutions architect at AWS. Joydeep enjoys working with AWS customers to migrate their workloads to the AWS Cloud, optimize for cost and help with architectural best practices. He is passionate about enterprise architecture to help reduce cost and complexity in the enterprise. He lives in New Jersey and enjoys listening to music and spending time in the outdoors in his spare time.
Like (0)
Share
Comments
Log in to comment Log in
Resources
Getting Started
What's New
Blog Topics
Amazon Aurora
Amazon DocumentDB
Amazon DynamoDB
Amazon ElastiCache
Amazon Keyspaces (for Apache Cassandra)
Amazon Managed Blockchain
Amazon MemoryDB for Redis
Amazon Neptune
Amazon Quantum Ledger Database (Amazon QLDB)
Amazon RDS
Amazon Timestream
AWS Database Migration Service
AWS Schema Conversion Tool
Follow
Twitter
Facebook
LinkedIn
Twitch
Email Updates
Create an AWS account
Learn
What Is AWS?
What Is Cloud Computing?
What Is Agentic AI?
Cloud Computing Concepts Hub
AWS Cloud Security
What's New
Blogs
Press Releases
Resources
Getting Started
Training
AWS Trust Center
AWS Solutions Library
Architecture Center
Product and Technical FAQs
Analyst Reports
AWS Partners
Developers
Builder Center
SDKs & Tools
.NET on AWS
Python on AWS
Java on AWS
PHP on AWS
JavaScript on AWS
Help
Contact Us
File a Support Ticket
AWS re:Post
Knowledge Center
AWS Support Overview
Get Expert Help
AWS Accessibility
Legal
English
Back to top
Amazon is an equal opportunity employer and does not discriminate on the basis of protected veteran status, disability or other legally protected status.        
Privacy
Site terms
Your Privacy Choices
Cookie Preferences
© 2026, Amazon Web Services, Inc. or its affiliates. All rights reserved.
