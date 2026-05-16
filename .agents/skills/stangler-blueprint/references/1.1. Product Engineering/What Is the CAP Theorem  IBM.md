---
name: What Is the CAP Theorem? | IBM
keywords: (placeholder)
metadata:
  url: https://www.ibm.com/think/topics/cap-theorem
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
What Is the CAP Theorem? | IBM
What's new
Skip to content  [](javascript:void 0)  [](javascript:void 0)
My IBM Log in
Think
Overview
Think 2026
Think 2026
Think 2026 on demand
Think on Tour
Artificial intelligence
Cloud
Security
News
Podcasts
Overview
Mixture of Experts
Security Intelligence
Smart Talks with IBM
Techsplainers
The Coherence Times
Videos
Overview
AI Academy
Think 2026 on demand
Webinars
Reports
IBM X-Force 2026 Threat Intelligence Index
Cost of a Data Breach Report
The CEO Study
Industries in the AI era
Orchestrating agentic AI for intelligent business operations
Scaling supply chain resilience: Agentic AI for autonomous operations
AI in Action report
View all IBV reports
Events
Think 2026
Think on Tour
TechXchange
View all IBM Events
More
Topics
Analytics
Artificial intelligence
Asset management
Business automation
Business operations
Cloud
Compute and servers
DevOps
IT automation
IT infrastructure
Leadership
Middleware
Network
Quantum
Security
Storage
Sustainability
Content types
Explainers
Insights
News
Newsletters
Reference architectures
Tutorials
Industries
Automotive
Banking
Consumer Goods
Energy & Utilities
Government
Healthcare
Manufacturing
Retail
Telecommunications
Travel View all
Subscribe
What is the CAP theorem?
What is the CAP theorem?
More on the 'CAP' in the CAP theorem
CAP theorem NoSQL database types
MongoDB and the CAP theorem
Cassandra and the CAP theorem (AP)
Microservices and the CAP theorem
Data Management Guide
Welcome
Introduction
Overview
Modern data stack
AI-ready data
AI data management
DataOps
Overview
DataOps framework
DataOps architecture
Data
Overview
Structured vs. unstructured data
Metadata
Metadata management
Datasets
Databases
Overview
Relational databases
Overview
SQL
Primary key
NoSQL databases
OLTP
Vector databases
RAG vector databases
Database as a service (DBaaS)
Distrubuted databases
CAP theorem
Database schema
Popular databases
MongoDB
PostgreSQL
Redis
Elasticsearch
OpenSearch
etcd
Cassandra
Apache HBase
CouchDB
Query engines
Presto
Query optimization
Database management
Entity relationship diagram
Data platforms
Overview
Data warehouse
Overview
Data mart
Data lake
Overview
Delta lake
Apache iceberg
AWS data lake formation
Data lakehouse
Overview
Feature store
Cloud data lake, data warehouse and data mart
Master data management (MDM)
Data architecture
Overview
Data fabric
Data mesh
Data modeling
Data engineering
Overview
Agentic AI data engineering
Data acquisition
Data pipeline
Overview
Data pipeline automation
10 steps for automating data pipelines
Directed acyclic graph
Data preparation
Data cleaning
Data reconciliation
Data validation
Data enrichment
Data wrangling
Data virtualization
Data automation
Data orchestration
Data transfer
File transfer
Data migration
Streaming data
Data integration
Overview
ETL
ELT
Change data capture
Real-time data integration
Cloud data integration
AI data integration
Data interoperability
Overview
Data contract
Data integration techniques and methods
Data processing
Overview
Data retrieval
Data ingestion
OLAP
Stream processing
Unstructured data processing
Real-time data streaming
Big data
Overview
Apache Hadoop
Overview
HDFS
Mapreduce
Apache Avro
Apache Ranger
Enterprise data management
Overview
Chief Data Officer (CDO)
Data democratization
Overview
Data literacy
Data marketplace
Data optimization
Data modernization
Data reduction
Data silos
Data strategy
Data SLA
Data fragmentation
Data quality
Overview
Data quality management
Data quality dimensions
Overview
Data accuracy
Data integrity
Data reliability
Data quality management
Overview
Data observability
Poor data quality
Bad data
Dark data
Dirty data
AI data quality
Data governance
Overview
Data stewardship
The CAP theorem says that a distributed system can deliver only two of three desired characteristics: consistency, availability and * partition tolerance* (the ' C,' ' A' and ' P' in CAP).
Have you ever seen an advertisement for a landscaper, house painter, or some other tradesperson that starts with the headline, “Cheap, Fast, and Good: Pick Two”? The CAP theorem applies a similar type of logic to distributed systems.
A distributed system is a network that stores data on more than one node (physical or virtual machines) at the same time. Because all cloud applications are distributed systems, it's essential to understand the CAP theorem when designing a cloud app so that you can choose a data management system that delivers the characteristics your application needs most.
The CAP theorem is also called Brewer's Theorem, because it was first advanced by Professor Eric A. Brewer during a talk he gave on distributed computing in 2000. Two years later, MIT professors Seth Gilbert and Nancy Lynch published a proof of “Brewer's Conjecture.”
More on the 'CAP' in the CAP theorem
Let's take a detailed look at the three distributed system characteristics to which the CAP theorem refers.
Consistency
Consistency means that all clients see the same data at the same time, no matter which node they connect to. For this to happen, whenever data is written to one node, it must be instantly forwarded or replicated to all the other nodes in the system before the write is deemed 'successful.'
Availability
Availability means that any client making a request for data gets a response, even if one or more nodes are down. Another way to state this—all working nodes in the distributed system return a valid response for any request, without exception.
Partition tolerance
A partition is a communications break within a distributed system—a lost or temporarily delayed connection between two nodes. Partition tolerance means that the cluster must continue to work despite any number of communication breakdowns between nodes in the system.
The latest tech news, backed by expert insights
Stay up to date on the most important—and intriguing—industry trends on AI, automation, data and beyond with the Think newsletter. See the IBM Privacy Statement.
Thank you! You are subscribed.
First name*
Field required
Last name*
Field required
Business email*
Field required. Must be valid email. example@yourdomain.com
Your subscription will be delivered in English. You will find an unsubscribe link in every newsletter. Refer to our IBM Privacy Statement for more information.
Subscribe
CAP theorem NoSQL database types
NoSQL databases are ideal for distributed network applications. Unlike their vertically scalable SQL (relational) counterparts, NoSQL databases are horizontally scalable and distributed by design—they can rapidly scale across a growing network consisting of multiple interconnected nodes. (See " SQL vs. NoSQL Databases: What's the Difference?" for more information.)
Today, NoSQL databases are classified based on the two CAP characteristics they support:
CP database: A CP database delivers consistency and partition tolerance at the expense of availability. When a partition occurs between any two nodes, the system has to shut down the non-consistent node (i.e., make it unavailable) until the partition is resolved.
AP database: An AP database delivers availability and partition tolerance at the expense of consistency. When a partition occurs, all nodes remain available but those at the wrong end of a partition might return an older version of data than others. (When the partition is resolved, the AP databases typically resync the nodes to repair all inconsistencies in the system.)
CA database: A CA database delivers consistency and availability across all nodes. It can't do this if there is a partition between any two nodes in the system, however, and therefore can't deliver fault tolerance.
We listed the CA database type last for a reason—in a distributed system, partitions can't be avoided. So, while we can discuss a CA distributed database in theory, for all practical purposes a CA distributed database can't exist. This doesn't mean you can't have a CA database for your distributed application if you need one. Many relational databases, such as PostgreSQL, deliver consistency and availability and can be deployed to multiple nodes using replication.
Mixture of Experts | 24 April, episode 104 
Decoding AI: Weekly News Roundup
Join our world-class panel of engineers, researchers, product leaders and more as they cut through the AI noise to bring you the latest in AI news and insights. 
Watch all episodes of Mixture of Experts
MongoDB and the CAP theorem
MongoDB is a popular NoSQL database management system that stores data as BSON (binary JSON) documents. It's frequently used for big data and real-time applications running at multiple different locations. Relative to the CAP theorem, MongoDB is a CP data store—it resolves network partitions by maintaining consistency, while compromising on availability.
MongoDB is a single-master system—each replica set can have only one primary node that receives all the write operations. All other nodes in the same replica set are secondary nodes that replicate the primary node's operation log and apply it to their own data set. By default, clients also read from the primary node, but they can also specify a read preference that allows them to read from secondary nodes.
When the primary node becomes unavailable, the secondary node with the most recent operation log will be elected as the new primary node. Once all the other secondary nodes catch up with the new master, the cluster becomes available again. As clients can't make any write requests during this interval, the data remains consistent across the entire network.
Cassandra and the CAP theorem (AP)
Apache Cassandra is an open source NoSQL database maintained by the Apache Software Foundation. It's a wide-column database that lets you store data on a distributed network. However, unlike MongoDB, Cassandra has a masterless architecture, and as a result, it has multiple points of failure, rather than a single one.
Relative to the CAP theorem, Cassandra is an AP database—it delivers availability and partition tolerance but can't deliver consistency all the time. Because Cassandra doesn't have a master node, all the nodes must be available continuously. However, Cassandra provides eventual consistency by allowing clients to write to any nodes at any time and reconciling inconsistencies as quickly as possible.
As data only becomes inconsistent in the case of a network partition and inconsistencies are quickly resolved, Cassandra offers “repair” functionality to help nodes catch up with their peers. However, constant availability results in a highly performant system that might be worth the trade-off in many cases.
Microservices and the CAP theorem
Microservices are loosely coupled, independently deployable application components that incorporate their own stack—including their own database and database model—and communicate with each other over a network. As you can run microservices on both cloud servers and on-premises data centers, they have become highly popular for hybrid and multicloud applications.
Understanding the CAP theorem can help you choose the best database when designing a microservices-based application running from multiple locations. For example, if the ability to quickly iterate the data model and scale horizontally is essential to your application, but you can tolerate eventual (as opposed to strict) consistency, an AP database like Cassandra or Apache CouchDB can meet your requirements and simplify your deployment. On the other hand, if your application depends heavily on data consistency—as in an eCommerce application or a payment service—you might opt for a relational database like PostgreSQL.
Share
Link copied       
Ebook Four steps to better business forecasting with analytics Use the power of analytics and business intelligence to plan, forecast and shape future outcomes that best benefit your company and customers. 
Read the ebook
Resources
Carousel   
Ebook The hybrid, open data lakehouse for AI Simplify data access and automate data governance. Discover the power of integrating a data lakehouse strategy into your data architecture, including cost-optimizing your workloads and scaling AI and analytics, with all your data, anywhere. 
Read the ebook   
Insights From data chaos to AI clarity: Activating AI through high-quality enterprise data Understand how focusing on well-governed, secure and collaborative access to data at scale empowers enterprises to maximize their AI investments 
Read the insights - This link downloads a pdf   
AI in Action podcast Decision intelligence: Thoughtful, data-driven choices Learn how data intelligence helps leaders make sense of data, use generative AI wisely and make decisions based on what truly matters. 
Watch the episode   
Case study Streamlining and evolving fraud investigations with AI Discover how Cogniware leverages AI solutions from IBM to drive efficiency in the financial crime space. 
Read the case study   
Webinar | On demand Turning data strategy into AI impact Discover how to scale AI with a strong data foundation, deliver explainable and governed outcomes, and apply real-world lessons to your own AI roadmap. 
Watch now - This link opens in a new tab   
Report How the C-suite is turning information into impact Explore insights from 1,700 CDOs in this cross-industry report for data leaders. 
Read the report   
Ebook Unify and access your data to help scale your AI Learn why the path to AI-ready data often starts with effective access to both structured and unstructured data and the challenges that can impede data leaders. 
Read the ebook   
Insights Unleash the power of AI for seamless data integration Understand why organizations need to adopt a unified approach that lets them manage the full spectrum of integration capabilities from a single pane of glass, eliminating the need to rely on numerous tools. 
Read the insights - This link downloads a pdf
1 / 8 Slide 1 of 8. Showing 1 items.
Related solutions
Analytics tools and solutions
To thrive, companies must use data to build customer loyalty, automate business processes and innovate with AI-driven solutions. 
Explore analytics solutions
Data and analytics consulting services
Unlock the value of enterprise data with IBM Consulting, building an insight-driven organization that delivers business advantage. 
Discover analytics services
IBM Cognos Analytics
Introducing Cognos Analytics 12.0, AI-powered insights for better decision-making. 
Explore Cognos Analytics
Take the next step
To thrive, companies must use data to build customer loyalty, automate business processes and innovate with AI-driven solutions. Make better decisions faster with IBM Cognos® Analytics.
Explore Cognos Analytics
Discover analytics solutions 
Discover
Products Consulting services Industries Case studies Financing Research
Follow
LinkedIn X Instagram YouTube Podcasts
Connect
Business partners Documentation Events Newsletters Support TechXchange community
About
Overview Careers Investor relations Leadership Newsroom Security, privacy and trust
United States — English
Contact IBM Privacy Terms of use Accessibility
START
END
START
END  
