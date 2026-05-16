---
name: Differences between Coupling and Cohesion - Software Engineering - GeeksforGeeks
keywords: (placeholder)
metadata:
  url: https://www.geeksforgeeks.org/software-engineering/software-engineering-differences-between-coupling-and-cohesion/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Differences between Coupling and Cohesion - Software Engineering - GeeksforGeeks
 
Sign In
Courses
Tutorials
Interview Prep
Software Engineering Tutorial
Software Development Life Cycle
Waterfall Model
Software Requirements
Software Measurement and Metrics
Software Design Process
System configuration management
Software Maintenance
Software Development Tutorial
Software Testing Tutorial
Differences between Coupling and Cohesion - Software Engineering
Last Updated : 11 Jul, 2025
Coupling and Cohesion are two key concepts in software engineering that are used to measure the quality of a software system's design. Both coupling and cohesion are important factors in determining the maintainability, scalability, and reliability of a software system. High coupling and low cohesion can make a system difficult to change and test, while low coupling and high cohesion make a system easier to maintain and improve. 
Coupling vs Cohesion
What is Cohesion?
Cohesion refers to the degree to which elements within a module work together to fulfill a single, well-defined purpose. High cohesion means that elements are closely related and focused on a single purpose, while low cohesion means that elements are loosely related and serve multiple purposes.
Types of Cohesion
The following are the types of cohesion:
Functional Cohesion
Procedural Cohesion
Temporal Cohesion:
Sequential Cohesion.
Layer Cohesion.
Communication Cohesion. 
Types of Cohesion
What is Coupling
Coupling refers to the degree of interdependence between software modules. High coupling means that modules are closely connected and changes in one module may affect other modules. Low coupling means that modules are independent, and changes in one module have little impact on other modules.
Types of Coupling
Following are the types of Coupling:
Data Coupling
Stamp Coupling
Control Coupling
External Coupling
Common Coupling
Content Coupling 
Types of Coupling
Differences between Coupling and Cohesion
The differences between cohesion and coupling are given below:
Example of High Cohesion and Low Coupling
Below diagram shows the example of high cohesive and low coupling: 
High Cohesive and Low Coupling
Explanation
High Cohesion: User Module
The User Module is designed to handle all user-related functionalities:
Attributes: It has attributes like id , name , and email .
Functions: It includes functions such as register() , login() , and logout() .
Why is it high cohesion?
Single Purpose: All the functions in the User Module are related to managing users. This means everything in this module is focused on one specific task - handling user operations.
Low Coupling: Book and Member Modules
The Library System consists of two separate modules: Book and Member .
Book Module:
Attributes: It has attributes like title and author .
Functions: It includes functions such as addBook() and removeBook() .
Member Module:
Attributes: It has attributes like memberId and memberName .
Functions: It includes functions such as addMember() and removeMember() .
Why is it low coupling?
Independent Modules: The Book and Member modules operate independently. They have their own specific functions and attributes and don't need to know the internal workings of each other.
Minimal Interaction: The only interaction is through simple actions like borrowing a book or managing memberships, but they don't rely on each other for their main tasks.
Important Questions on Coupling vs Cohesion
1. In the context of modular software design, which one of the following combinations is desirable? [ ISRO CS 2017 - May ]
(A) High cohesion and high coupling
(B) High cohesion and low coupling
(C) Low cohesion and high coupling
(D) Low cohesion and low coupling
Solution: The Correct answer is (B)
2. A software design is highly modular if: [ UGC NET CS 2015 Jun - III ]
(A) cohesion is functional and coupling is data type.
(B) cohesion is coincidental and coupling is data type.
(C) cohesion is sequential and coupling is content type.
(D) cohesion is functional and coupling is stamp type.
Solution: The Correct answer is (A)
3. Which of the following statement(s) is/are true with respect to software architecture ? S1 : Coupling is a measure of how well the things grouped together in a module belong together logically. S2 : Cohesion is a measure of the degree of interaction between software modules. S3 : If coupling is low and cohesion is high then it is easier to change one module without affecting others. [ UGC NET CS 2017 Jan - II ]
(A) Only S1 and S2
(B) Only S3
(C) All of S1, S2 and S3
(D) Only S1
Solution: The Correct answer is (B)
Comment
M
mks075
68
Article Tags:
Article Tags:
Software Engineering
Explore
Software Engineering Basics
Introduction to Software Engineering 4 min read
Software Development Life Cycle (SDLC) 4 min read
Software Quality - Software Engineering 5 min read
ISO/IEC 9126 in Software Engineering 4 min read
Boehm's Software Quality Model 4 min read
Software Crisis - Software Engineering 3 min read
Software Measurement & Metrices
Software Measurement and Metrics 4 min read
People Metrics and Process Metrics in Software Engineering 7 min read
Halstead's Software Metrics - Software Engineering 10 min read
Cyclomatic Complexity 6 min read
Functional Point (FP) Analysis - Software Engineering 8 min read
Lines of Code (LOC) in Software Engineering 4 min read
Software Development Models & Agile Methods
Waterfall Model - Software Engineering 5 min read
Spiral Model in Software Engineering 4 min read
Prototyping Model - Software Engineering 7 min read
Incremental Process Model - Software Engineering 3 min read
Rapid Application Development Model (RAD) - Software Engineering 4 min read
Coupling and Cohesion - Software Engineering 10 min read
Agile Software Development - Software Engineering 7 min read
SRS & SPM
Software Requirement Specification (SRS) Format 5 min read
Software Engineering | Quality Characteristics of a good SRS 7 min read
Software Project Management (SPM) - Software Engineering 8 min read
COCOMO Model - Software Engineering 15+ min read
Capability Maturity Model (CMM) - Software Engineering 10 min read
Integrating Risk Management in SDLC | Set 1 8 min read
Software Maintenance - Software Engineering 13 min read
Testing & Debugging
Introduction to Software Testing 4 min read
Types of Software Testing 15+ min read
Testing Guidelines - Software Engineering 3 min read
What is Debugging in Software Engineering? 11 min read
Verification & Validation
Verification and Validation in Software Engineering 6 min read
Role of Verification and Validation (V&V) in SDLC 5 min read
Requirements Validation Techniques - Software Engineering 8 min read
Practice Questions
Top 50+ Software Engineering Interview Questions and Answers 15+ min read
 
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
