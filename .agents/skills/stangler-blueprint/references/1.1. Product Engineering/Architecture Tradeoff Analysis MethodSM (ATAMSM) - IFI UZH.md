---
name: Architecture Tradeoff Analysis MethodSM (ATAMSM) - IFI UZH
keywords: (placeholder)
metadata:
  url: https://www.ifi.uzh.ch/dam/jcr:ffffffff-fd5f-cdf8-ffff-ffffde53807c/swa-04-ATAM.pdf
  source: SOURCE_TYPE_PDF
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Architecture Tradeoff Analysis MethodSM 
(ATAMSM) Software Engineering Institute Carnegie Mellon University Pittsburgh, PA  15213 
SMATAM and Architecture Tradeoff Analysis Method are registered service marks of Carnegie Mellon University
© 2002 by Carnegie Mellon University 2 
Why Analyze Software Architectures? All design involves tradeoff in system qualities 
 System qualities are largely dependent on 
architectural decisions 
 Promoting one quality often comes at the expense 
of another quality A software architecture is the earliest life-cycle artifact that embodies significant design decisions: choices and tradeoffs. 
 Choices are easy to make, but hard to change 
once the system is implemented
© 2002 by Carnegie Mellon University 3 
The ATAM 
SEI has developed the Architecture Tradeoff Analysis Method (ATAM) over several years. 
The purpose of ATAM is: to assess the consequences of architectural decision alternatives in light of quality attribute requirements.
© 2002 by Carnegie Mellon University 4 
Purpose of ATAM - 1 We need a method in which the right questions are asked early to: 
 Discover risks - alternatives that might create future problems in 
some quality attribute 
 Discover non-risks - decisions that promote qualities that help realize business/mission goals 
 Discover sensitivity points - alternatives for which a slight change makes a significant difference in some quality attribute 
 Discover tradeoffs - decisions affecting more than one quality attribute
© 2002 by Carnegie Mellon University 5 
Purpose of ATAM - 2 The purpose of an ATAM is NOT to provide precise analyses . . . the purpose IS to discover risks created by architectural decisions. 
We want to find trends: correlation between architectural decisions and predictions of system properties. 
Discovered risks can then be made the focus of mitigation activities: e.g. further design, further analysis, prototyping. 
Surfaced tradeoffs can be explicitly identified and documented.
© 2002 by Carnegie Mellon University 6 
ATAM Benefits 
There are a number of benefits from performing ATAM analyses: 
 Clarified quality attribute requirements 
 Improved architecture documentation 
 Documented basis for architectural decisions 
 Identified risks early in the life-cycle 
 Increased communication among stakeholders 
The results are improved architectures.
© 2002 by Carnegie Mellon University 7 
Purpose of ATAM The purpose of ATAM is to assess the consequences of architectural decisions in light of quality attribute requirements. 
The ATAM process is a short, facilitated interaction between multiple stakeholders, leading to the identification of risks, sensitivities, and tradeoffs. 
The purpose of an ATAM is NOT to provide precise analyses, the purpose IS to discover risks created by architectural decisions.
© 2002 by Carnegie Mellon University 8 
Preconditions for an ATAM 
1. Clients must have a Software Architecture - Scope/scale must be manageable - ATAM will not work if the software architecture has not 
been created yet - ATAM team members will review architectural artifacts, 
and may help refine documentation - Architect must prepare an architecture presentation 
2. Clients must prepare a business/mission goals presentation 3. ATAM will review architecture artifacts, presentations, and 
read ahead material to become familiar with domain
© 2002 by Carnegie Mellon University 9 
Evaluation Team Each ATAM team consists of a leader and at least three other team members 
 domain expertise is not necessary 
 ATAM team members must be experienced 
architects 
 ATAM leaders must have EXCELLENT 
communication and facilitation skills 
The ATAM team members fill multiple roles during the course of the evaluation.
© 2002 by Carnegie Mellon University 10 
Evaluation Team Roles - 1 Moderator — facilitates discussions, brainstorming, analysis Scenario scribe(s) — writes utility tree, raw scenarios, risks, sensitivities, tradeoffs on flip-charts or whiteboards Proceedings scribe — captures scribe’s writing on a laptop computer, preparing the Results Presentation template
© 2002 by Carnegie Mellon University 11 
Evaluation Team Roles - 2 
Process enforcer/observer — monitors the process steps, takes notes about the process, and how it could be improved Timekeeper — informs the evaluation leader when the time allocated for a step has expired Questioner(s) — raise issues that the stakeholders have not thought of; asks questions based on how quality attributes of interest relate to architectural styles
© 2002 by Carnegie Mellon University 12 
Basic Rules for ATAM Team Members 
 Keep the process moving! 
 Ask questions 
 Propose scenarios 
 Write down exactly what stakeholders say; do not “edit” their words!
© 2002 by Carnegie Mellon University 13 
ATAM Steps 1.  Present the ATAM 2.  Present business drivers 3.  Present architecture 4.  Identify architectural approaches 5.  Generate quality attribute utility tree 6.  Analyze architectural approaches 7.  Brainstorm and prioritize scenarios 8.  Analyze architectural approaches 9. Present results 
Phase I 
Phase II
© 2002 by Carnegie Mellon University 14 
1. Present the ATAM 
Evaluation Team presents an overview of the ATAM including: 
 ATAM steps in brief 
 Techniques 
- utility tree generation - architecture elicitation and analysis - scenario brainstorming/mapping 
 Outputs - architectural approaches - utility tree - scenarios - risks and “non-risks” - sensitivity points and tradeoffs
© 2002 by Carnegie Mellon University 15 
2.  Present Business Drivers ATAM customer representative describes the system’s business drivers including: 
 Business context for the system 
 High-level functional requirements 
 High-level quality attribute requirements - architectural drivers: quality attributes that “shape” the 
architecture 
- critical requirements: quality attributes most central to the system’s success
© 2002 by Carnegie Mellon University 16 
3.  Present Architecture Architect presents an overview of the architecture including: 
 Technical constraints such as an OS, hardware, or 
middle-ware prescribed for use 
 Other systems with which the system must interact 
 Architectural approaches/styles used to address 
quality attribute requirements 
Evaluation team begins probing for and capturing risks.
© 2002 by Carnegie Mellon University 17 
ATAM Steps 1.  Present the ATAM 2.  Present business drivers 3.  Present architecture 4.  Identify architectural approaches 5.  Generate quality attribute utility tree 6.  Analyze architectural approaches 7.  Brainstorm and prioritize scenarios 8.  Analyze architectural approaches 9. Present results 
Phase I 
Phase II
© 2002 by Carnegie Mellon University 18 
Start to identify places in the architecture that are key for realizing quality attribute goals. 
Identify any predominant architectural approaches. 
Examples: 
 client-server 
 3-tier 
 watchdog 
 publish-subscribe 
 redundant hardware 
4. Identify Architectural     Approaches
© 2002 by Carnegie Mellon University 19 
Identify, prioritize, and refine the most important quality attribute goals by building a utility tree. 
 A utility tree is a top-down vehicle for characterizing the “driving” attribute-specific requirements 
 Select the most important quality goals to be the high-level nodes (typically performance, modifiability, security, and availability) 
 Scenarios are the leaves of the utility tree 
Output: a characterization and a prioritization of specific quality attribute requirements. 
High/Medium/Low importance for the success of the system High/Medium/Low difficulty to achieve (architect’s assessment) 
5. Generate Quality     Attribute Utility Tree
© 2002 by Carnegie Mellon University 20 
Utility Tree Construction -1 
Utility 
Performance 
Modifiability 
Availability 
Security 
Add CORBA middleware in < 20 person-months Change web user interface in < 4 person-weeks Power outage at site1 requires traffic  redirected to site2 in < 3 seconds. Restart after disk failure in < 5 minutes 
Network failure detected and recovered  in < 1.5 minutes 
Reduce storage latency on customer DB to < 200 ms. 
Deliver video in real time 
Customer DB authorization works  99.999% of the time 
Credit card transactions are secure 99.999% of the time 
Data Latency 
Transaction Throughput 
New product categories Change COTS 
H/W failure 
COTS S/W failures 
Data 
Data confidentiality 
integrity
© 2002 by Carnegie Mellon University 21 
Utility Tree Construction -2 
Utility 
Performance 
Modifiability 
Availability 
Security 
Add CORBA middleware in < 20 person-months Change web user interface in < 4 person-weeks Power outage at site1 requires traffic  redirected to site2 in < 3 seconds. Restart after disk failure in < 5 minutes 
Network failure detected and recovered  in < 1.5 minutes 
Reduce storage latency on customer DB to < 200 ms. 
Deliver video in real time 
Customer DB authorization works  99.999% of the time 
Credit card transactions are secure 99.999% of the time 
Data Latency 
Transaction Throughput 
New product categories Change COTS 
H/W failure 
COTS S/W failures 
Data 
Data confidentiality 
integrity 
(M,L) 
(H,M) 
(L,H) 
(H,L) 
(L,H) 
(M,M) 
(H,M) 
(L,H) 
(L,H)
© 2002 by Carnegie Mellon University 22 
Scenarios  are used to 
 Represent stakeholders’ interests 
 Understand quality attribute requirements 
Scenarios should cover a range of 
 Anticipated uses of (use case scenarios), 
 Anticipated changes to (growth scenarios), or 
 Unanticipated stresses (exploratory scenarios) to the system. 
A good scenario makes clear what the stimulus is that causes it and what responses are of interest. 
Scenarios
© 2002 by Carnegie Mellon University 23 
Example Scenarios Use case scenario 
Remote user requests a database report via the Web during peak period and receives it within 5 seconds. 
Growth scenario Add a new data server to reduce latency in scenario 1 to 2.5 seconds within 1 person-week. 
Exploratory scenario Half of the servers go down during normal operation without affecting overall system availability. 
=> Scenarios should be as specific as possible.
© 2002 by Carnegie Mellon University 24 
Stimuli, Environment, Responses Use Case Scenario 
Remote user requests a database report via the Web during peak period and receives it within 5 seconds. 
Growth Scenario Add a new data server to reduce latency in scenario 1 to 2.5 seconds within 1 person-week. 
Exploratory Scenario Half of the servers go down during normal operation without affecting overall system availability. 
=> Scenarios should be as specific as possible.
© 2002 by Carnegie Mellon University 25 
Evaluation Team probes architectural approaches from the point of view of specific quality attributes to identify risks. 
 Identify the approaches that pertain to the highest priority quality 
attribute requirements 
 Generate quality-attribute specific questions for highest priority quality attribute requirement 
 Ask quality-attribute specific questions 
 Identify and record risks and non-risks, sensitivity points and tradeoffs 
6. Analyze Architectural Approaches
© 2002 by Carnegie Mellon University 26 
Quality Attribute Questions Quality attribute questions probe styles to elicit architectural decisions which bear on quality attribute requirements. 
Performance 
 How are priorities assigned to processes? 
 What are the message arrival rates? 
Modifiability 
 Are there any places where layers/facades are circumvented 
? 
 What components rely on detailed knowledge of message 
formats?
© 2002 by Carnegie Mellon University 27 
Risks and Non-Risks Example Risks 
 Rules for writing business logic modules in the 
second tier of your 3-tier style are not clearly articulated.  This could result in replication of functionality thereby compromising modifiability of the third tier. 
Example Non-Risk 
 Assuming message arrival rates of once per 
second, a processing time of less than 30 ms, and the existence of one higher priority process, a 1 second soft deadline seems reasonable.
© 2002 by Carnegie Mellon University 28 
Sensitivities and Tradeoffs 
Example Sensitivity 
 Changing the timing scheme from a harmonic 
framework to a non-harmonic framework would be easy, but due to implied timing dependencies, there would be far reaching impacts to other modules. 
Example Tradeoffs 
 In order to achieve the required level of performance in 
the discrete event generation component, assembly language had to be used thereby reducing the portability of this component.
© 2002 by Carnegie Mellon University 29 
ATAM Steps 1.  Present the ATAM 2.  Present business drivers 3.  Present architecture 4.  Identify architectural approaches 5.  Generate quality attribute utility tree 6.  Analyze architectural approaches 7.  Brainstorm and prioritize scenarios 8.  Analyze architectural approaches 9. Present results 
Phase I 
Phase II
© 2002 by Carnegie Mellon University 30 
Stakeholders generate scenarios using a facilitated brainstorming process. 
 Scenarios at the leaves of the utility tree serve as examples to facilitate the step. 
 The new scenarios are added to the utility tree 
Each stakeholder is allocated a number of votes roughly equal to 0.3 x #scenarios. 
7. Brainstorm and     Prioritize Scenarios
© 2002 by Carnegie Mellon University 31 
Identify the architectural approaches impacted by the scenarios generated in the previous step. 
This step continues the analysis started in step 6 using the new scenarios. 
Continue identifying risks and non-risks. 
Continue annotating architectural information. 
8. Analyze Architectural Approaches
© 2002 by Carnegie Mellon University 32 
Recapitulate steps of the ATAM 
Present ATAM outputs 
 architectural approaches 
 utility tree 
 scenarios 
 risks and “non-risks” 
 sensitivity points and tradeoffs 
9. Present Results
© 2002 by Carnegie Mellon University 33 
Conceptual Flow of ATAM Business Drivers 
Software Architecture 
Quality Attributes 
Architectural Approaches 
Architectural Decisions 
Scenarios 
Risks 
Sensitivity Points 
Tradeoffs 
Non-Risks 
impacts 
Risk Themes 
distilled into 
Analysis
© 2002 by Carnegie Mellon University 34 
ATAM evaluations are often conducted in two stages or phases: 
 During phase 1 the architect describes the quality attribute goals and how the architecture meets these goals 
 During phase 2 we determine if a larger group of stakeholders agrees with the goals and the results 
ATAM Nominal Phases - 1
© 2002 by Carnegie Mellon University 35 
ATAM Steps 1   2 3   4 5   6 7   8 9 
Phase 1     (small group,      usually one day) 
(informal interactions in between phases) 
Phase 2     (larger group, (recap and           usually two days) elaborate) 
ATAM Nominal Phases - 2 Ti 
m e
© 2002 by Carnegie Mellon University 36 
ATAM versus QAW ATAM 
 Need architecture 
 Focused on: - business/mission goals - quality attributes - architecture decisions 
 Scenario-driven 
 Proven to be useful for software architectures 
 Analysis done by evaluation team 
 Short duration 
QAW (quality attribute workshops) 
 Need requirements 
 Quality-attribute focused 
 Scenario-driven 
 Proven to be useful at system level 
- helps define software’s role in overall system 
 Analysis done by developers, designers ~ reviewed by evaluation team 
 Iterative, extended duration
© 2002 by Carnegie Mellon University 37 
When to use ATAM 
Academically, the time to use ATAM is right after the architecture has been specified when there is little or no code. However, in practice, ATAM has been very effective in the following situations: 
 Evaluating alternative candidate architectures 
 Evaluating existing systems prior to committing 
to major upgrades 
 Deciding between upgrade or replace
