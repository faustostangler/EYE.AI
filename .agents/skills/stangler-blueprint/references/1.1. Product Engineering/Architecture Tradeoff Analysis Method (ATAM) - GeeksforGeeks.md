---
name: Architecture Tradeoff Analysis Method (ATAM) - GeeksforGeeks
keywords: (placeholder)
metadata:
  url: https://www.geeksforgeeks.org/software-engineering/architecture-tradeoff-analysis-method-atam/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Architecture Tradeoff Analysis Method (ATAM) - GeeksforGeeks
 
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
Architecture Tradeoff Analysis Method (ATAM)
Last Updated : 23 Jul, 2025
This article focuses on discussing the Architecture Tradeoff Analysis Method (ATAM).
Architecture Tradeoff Analysis
This Method is a method used to evaluate the quality attributes (such as performance, availability, and security) of software architectures. ATAM is used to mitigate risks in software architectures in the early stages of the software development life cycle (SDLC).
Participants in ATAM
The ATAM requires the participation of three groups as follows.
The evaluation team: The evaluation team consists of the members who are external to the project. This team consists of 3–5 members who play their specific roles in the team.
Project decision-makers: Project decision-makers have the power to speak for the development of the project and have the authority to mandate changes.
Architecture stakeholders: Any individual, team, or organization who has an interest in the realization of the architecture and is somehow related to the architecture is a stakeholder of that architecture. Stakeholders include users, maintainers, performance engineers, testers, integrators, and developers.
Process of Architecture Tradeoff Analysis Method
The ATAM process starts with bringing all the stakeholders to find business drivers like system goals, constraints, system functionality, and desired non-functional properties. Then from these drivers quality attributes and business scenarios are created. Then, in conjunction with architectural approaches and architectural designs, these scenarios are used to create an analysis of trade-offs, sensitivity points, and risks (or non-risks). This analysis is then converted to the risk themes and their impacts from where the process can be repeated. With every analysis cycle, the process gradually proceeds from the more general to the more specific. The whole architecture will be fine-tuned and risk themes will be addressed by examining the questions that were discovered in the previous cycle. 
ATAM Process
Steps of ATAM Process
There are nine steps in the ATAM process as follows:
Present ATAM: Present the concept of the process to all the stakeholders of the process and answer the questions asked by the participants. This step makes the participants familiar with the process.
Present Business Drivers: All the participants involved in the presentation are expected to present, understand, and evaluate the business drivers for the system.
Present Architecture: A brief overview of the architecture is presented by the architect with an appropriate level of detail, i.e., at least modules and C&C views are discussed.
Identify Architectural Approaches: The architect presents some specific architectural approaches to the team and then the proposed architecture is discussed.
Generate Quality Attribute Utility Tree: In this step, the core business and technical requirements of the system are defined and then mapped into an appropriate architectural property. Put all these parts of evaluations, designs, and requirement elicitation into a tree.
Analyze architectural approaches: Every scenario is compared and rated by priority, and then highly rated scenarios are mapped onto the architecture.
Brainstorm Scenarios: The larger stakeholders group present and contribute current scenarios and their concerns.
Analyze architectural approaches: Step 6 is repeated with added knowledge from larger stakeholders in step.
Present results: At the end of the evaluation, the team reviews the existing and newly discovered risks, non-risks, sensitivities, and tradeoffs. The team discusses whether any new risk themes have arisen. Then the team provides all the documentation to the stakeholders.
Phases of ATAM
The ATAM consists of four phases as follows:
Phase 0: Preparation, planning, stakeholder recruitment, and team formation takes place in this phase. Participants are evaluation team key project decision-makers.
Phase 1: This phase consists of steps 1-6 of the evaluation process. Participants are evaluation team key project decision-makers. Its typical duration is 1 day followed by a hiatus of 2 to 3 weeks.
Phase 2: This phase consists of steps 7-9 of the evaluation process. Participants are evaluation team key project decision-makers and stakeholders. The duration of this phase is 2 days.
Phase 3: This phase is a follow-up phase. Report generation and delivery of the report are done in this phase. Any scope for improvement in the process is also looked upon. Participants are the Evaluation team and evaluation clients. Duration is 1 week.
Outputs of ATAM
A concise presentation of the architecture. The architecture is presented in one hour.
Articulation of business goals. This helps the new participants understand the business goals.
Prioritized quality attribute requirements expressed as quality attribute scenarios.
A set of risks and non-risks as follows:
A risk is defined as an architectural decision that may lead to undesirable consequences in light of quality attribute requirements.
non-risk is an architectural decision that is not expected to result in undesirable consequences of quality attributes.
A set of risk themes. This set helps the evaluation team to examine all the discovered risk themes that identify systematic weaknesses in the architecture, process, and team.
Mapping of architectural decisions to quality requirements. For each quality attribute scenario examined during an ATAM, those architectural decisions that help to achieve it are determined and captured.
Comment
V
vermaman947
11
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
Software Engineering Courses
Tech Interview 101 Course | DSA and System Design 2 min read
MERN Full Stack Development Course with AI 2 min read
DevOps Engineering Course with AI 2 min read
 
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
