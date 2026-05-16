---
name: CAP Theorem in System Design - GeeksforGeeks
keywords: (placeholder)
metadata:
  url: https://www.geeksforgeeks.org/system-design/cap-theorem-in-system-design/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
CAP Theorem in System Design - GeeksforGeeks
 
Sign In
Courses
Tutorials
Interview Prep
System Design Tutorial
HLD
LLD
Functional and Non Functional
Life Cycle
Design Patterns
UML Diagrams
System Design Interview Guide
Scalability
Databases
CAP Theorem in System Design
Last Updated : 30 Apr, 2026
According to the CAP theorem, only two of the three desirable characteristics consistency, availability, and partition tolerance can be shared or present in a networked shared-data system or distributed system.
The theorem provides a way of thinking about the trade-offs involved in designing and building distributed systems.
It helps to explain why certain types of systems may be more appropriate for certain use cases.
The theorem states that a distributed system can have at most two of these guarantees. 
CAP Theorem
Properties
The property of three distributed system characteristics to which CAP Theorem refers: 
Properties of CAP Theorem
1. Consistency
Consistency defines that all clients see the same data simultaneously, no matter which node they connect to in a distributed system. For eventual consistency, the guarantees are a bit loose. Eventual consistency guarantee means client will eventually see the same data on all the nodes at some point of time in the future. 
Consistency
In the above Diagram
All nodes in the system see the same data at the same time. This is because the nodes are constantly communicating with each other and sharing updates.
Any changes made to the data on one node are immediately propagated to all other nodes, ensuring that everyone has the same up-to-date information.
2. Availability
Availability defines that all non-failing nodes in a distributed system return a response for all read and write requests in a bounded amount of time, even if one or more other nodes are down. 
Availability
In above Diagram
User send requests, even though we don't see specific network components. This implies that the system is available and functioning.
Every request receives a response, whether successful or not. This is a crucial aspect of availability, as it guarantees that users always get feedback.
3. Partition Tolerance
Partition Tolerance defines that the system continues to operate despite arbitrary message loss or failure in parts of the system. Distributed systems guaranteeing partition tolerance can gracefully recover from partitions once the partition heals. 
Partition Tolerance
In the above Diagram
Addresses network failures, a common cause of partitions. It suggests that the system is designed to function even when parts of the network become unreachable.
The system can adapt to arbitrary partitioning, meaning it can handle unpredictable network failures without complete failure.
Trade-Offs in the CAP Theorem
The CAP Theorem states that a distributed system can provide only two out of three guarantees at the same time: Consistency (C), Availability (A), and Partition Tolerance (P). When a network partition occurs, a system must choose between maintaining consistency or availability.
We can classify the systems into the following three categories: 
Trade-offs in CAP theorem
1. CA System
A CA system provides Consistency and Availability but does not tolerate network partitions. This means that all nodes always return the same data and the system remains accessible, but if a network partition occurs, the system cannot continue operating correctly.
Example: Traditional relational databases in a single data center are often designed as CA systems.
2. CP System
A CP system provides Consistency and Partition Tolerance but sacrifices availability during network failures. When a partition occurs between nodes, the system may temporarily block requests to ensure that all nodes maintain consistent data.
Systems that prefer consistency over availability during partitions.
Examples: MongoDB (default replica set behavior), HBase
3. AP System
An AP system provides Availability and Partition Tolerance but does not guarantee immediate consistency. During a network partition, the system continues to serve requests, but some nodes may return stale or outdated data until the system eventually synchronizes.
Systems that prefer availability and may return eventually consistent data.
Examples: Apache Cassandra, DynamoDB
Example
This example demonstrates how the CAP theorem trade-off works during a network partition in a distributed system. 
Example
In the above Diagram,
We have a simple distributed system where S1 and S2 are two server. The two server can talk to each other. Here, System is partition tolerant. Here We will prove that system can be either consistent or available.
Suppose there is a network failure and S1 and S2 cannot talk to each other. Now assume that the client makes a write to S1. The client then send a read to S2.
Given S1 and S2 cannot talk, they have different view of the data. If the system has to remain consistent, it must deny the request and thus give up on availability.
If the system is available, then the system has to give up on consistency. This proves the CAP Theorem.
Use Cases
Here we will see how we can use all the trade-off system in real application:
1. Banking Transactions (CP System)
Problem Statement
Imagine a bank teller updating your account balance on a secure computer system. This system prioritizes consistency (C) and partition tolerance (P).
We use CP System
Each transaction must be accurately reflected across all servers (consistency) even if individual branches face network disruption (partition tolerance).
Inconsistency could lead to double spending or incorrect balances, unacceptable situations in financial transactions.
While data is always consistent, some users might experience momentary delays during network issues due to stricter synchronization requirements.
2. Social Media Newsfeed (AP System)
Problem Statement
Think of your newsfeed on a social media platform constantly updating with new posts and stories. This system prioritizes availability (A) and partition tolerance (P).
We use AP System
Users expect immediate access to their newsfeeds (availability) even if parts of the network are temporarily down (partition tolerance). Slight inconsistencies in data, like seeing a friend's post slightly sooner on one device than another, are tolerable in this context.
Data might not be perfectly consistent across all servers immediately after updates. Users might occasionally see slightly different versions of their newsfeed before data propagates across the system.
3. Online Shopping Cart (Hybrid System CAP System):
Problem Statement
Imagine an online shopping cart, adding items, and checking out. This system might employ a hybrid approach balancing CAP trade-offs.
We use AP and CP System
Adding items to the cart could be available and partition-tolerant (AP), allowing uninterrupted browsing even if temporary network glitches occur.
But when confirming the order and processing payment, the system might switch to a CP mode, ensuring consistency across all servers before finalizing the transaction.
The system requires careful design to switch seamlessly between availability and consistency modes at the right points to handle different stages of the user journey effectively.
Suggested Quiz 
6 Questions
Which of the following is an example of an AP (Available + Partition Tolerant) system?
A MongoDB
B HBase
C Cassandra
D RDBMS
Strong consistency ensures:
A All nodes may return different values temporarily
B All nodes return the most recent write for a read request
C Writes may be delayed but eventually applied
D System always prefers availability over consistency
Which consistency model guarantees that once a process reads a value, all future reads return the same or newer values?
A Strong Consistency
B Causal Consistency
C Monotonic Read Consistency
D Eventual Consistency
Eventual consistency is MOST suitable for:
A Banking transactions
B Social media feeds
C Stock trading platforms
D Airline reservation systems
What does the CAP Theorem state about distributed systems?
A A system can achieve all three properties simultaneously
B A system can achieve at most two out of three properties
C A system must always prioritize consistency
D A system cannot tolerate failures
Which type of system allows temporary stale data but remains responsive?
A CA system
B CP system
C AP system
D Hybrid system 
Quiz Completed Successfully
Your Score : 0/ 6
Accuracy : 0%
Login to View Explanation
1/6
< Previous Next >
Comment
S
supriyami26p4
12
Article Tags:
Article Tags:
System Design
Explore
Basics
Introduction 8 min read
SDLC 6 min read
Components 10 min read
Goals & Objectives 5 min read
Importance of System Design 6 min read
Key Concepts and Terminologies 9 min read
Advantages 4 min read
Fundamentals
Monolithic vs Distributed Systems 8 min read
Requirements Gathering 6 min read
System Analysis vs System Design 4 min read
Scaling 6 min read
Capacity Estimation 9 min read
Answering System Design Problems 5 min read
Functional vs Non Functional Requirements 5 min read
Web Server and Proxies 7 min read
Scalability
Scalability 5 min read
Choosing Scalability Approach 4 min read
Scalability Bottlenecks 5 min read
Databases in Designing Systems
Database Design 11 min read
SQL vs NoSQL 5 min read
File vs Database Storage Systems 4 min read
Block, Object and File Storage 7 min read
Database Sharding 8 min read
Database Replication 6 min read
High Level Design(HLD)
Introduction 8 min read
Availability 5 min read
Consistency 8 min read
Reliability 6 min read
CAP Theorem 5 min read
API Gateway 6 min read
Content Delivery Network 7 min read
Load Balancer 7 min read
Caching 8 min read
Communication Protocols 5 min read
Activity Diagrams 9 min read
Message Queues 12 min read
Low Level Design(LLD)
LLD 6 min read
Authentication vs Authorization 3 min read
Optimization Techniques 5 min read
OOAD 5 min read
DSA for System Design 6 min read
Containerization Architecture 10 min read
Modularity and Interfaces 7 min read
UML Diagrams 8 min read
Data Partitioning Techniques 6 min read
Prepare for LLD Interviews 4 min read
Security Measures 7 min read
Design Patterns
Design Patterns 4 min read
Creational Design Patterns 5 min read
Structural Design Patterns 6 min read
Behavioral Design Patterns 7 min read
Cheat Sheet 7 min read
Interview Guide for System Design
Cracking System Design Interviews 6 min read
Interview Q & A 1 min read
Concepts for Interview Preparation 6 min read
Crack LLD Interviews 4 min read
System Design Interview Questions & Answers
Commonly Asked Questions 3 min read
Design Dropbox 14 min read
Designing Twitter 15+ min read
Designing Netflix 15+ min read
Uber App 14 min read
Design BookMyShow 11 min read
Designing Facebook Messenger 8 min read
Roadmap 6 min read
System Design Guide for Freshers 15+ min read
 
Corporate & Communications Address:
A-143, 7th Floor, Sovereign Corporate Tower, Sector- 136, Noida, Uttar Pradesh (201305) 
Registered Address:
K 061, Tower K, Gulshan Vivante Apartment, Sector 137, Noida, Gautam Buddh Nagar, Uttar Pradesh, 201305     
 
Company
About Us
Legal
Privacy Policy
Contact Us
Advertise with us
GFG Corporate Solution
Campus Training Program
Explore
POTD
Job-A-Thon
Blogs
Nation Skill Up
Tutorials
Programming Languages
DSA
Web Technology
AI, ML & Data Science
DevOps
CS Core Subjects
Interview Preparation
Software and Tools
Courses
ML and Data Science
DSA and Placements
Web Development
Programming Languages
DevOps & Cloud
GATE
Trending Technologies
Videos
DSA
Python
Java
C++
Web Development
Data Science
CS Subjects
Preparation Corner
Interview Corner
Aptitude
Puzzles
GfG 160
System Design
@GeeksforGeeks, Sanchhaya Education Private Limited, All rights reserved 
