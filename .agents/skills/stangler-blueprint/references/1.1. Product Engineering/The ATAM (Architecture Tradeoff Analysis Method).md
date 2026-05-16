---
name: The ATAM (Architecture Tradeoff Analysis Method)
keywords: (placeholder)
metadata:
  url: https://www.recw.ac.in/v1.8/wp-content/uploads/2021/03/SA-UNIT-5.pdf
  source: SOURCE_TYPE_PDF
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Software Architecture  
Unit5  Page 1  
The ATAM (Architecture Tradeoff Analysis Method)  
 It is a thorough and comprehensive way to evaluate software architecture. 
The ATAM is designed to elicit the business goals for the system as well as for the 
architecture. It is also designed to use those goals and stakeholder participation to focus the 
attention of the evaluators on the portion of the architecture that is central to the achievement 
of the goals. 
Participants in the ATAM:- 
The ATAM requires the participation and mutual cooperation of three groups: 
1. The evaluation team. This group is external to the project whose architecture is 
being evaluated. It usually consists of three to five people. Each member of the team 
is assigned a number of specific roles to play during the evaluation. (See Table 
11.1 for a description of these roles, along with a set of desirable characteristics for 
each.) The evaluation team may be a standing unit in which architecture evaluations 
are regularly performed, or its members may be chosen from a pool of architecturally 
savvy individuals for the occasion. In any case, they need to be recognized as 
competent, unbiased outsiders with no hidden agendas or axes to grind. 
 
2. Project decision makers. These people are empowered to speak for the 
development project or have the authority to mandate changes to it. They usually 
include the project manager, and, if there is an identifiable customer who is footing 
the bill for the development, he or she will be present (or represented) as well. The 
architect is always included-a cardinal rule of architecture evaluation is that the 
architect must willingly participate. Finally, the person commissioning the evaluation 
is usually empowered to speak for the development project; even if not, he or she 
should be included in the group. 
 
3. Architecture stakeholders. Stakeholders have a vested interest in the architecture 
performing as advertised. They are the ones whose ability to do their jobs hinges on 
the architecture promoting modifiability, security, high reliability, or the like. 
Stakeholders include developers, testers, integrators, maintainers, performance 
engineers, users, builders of systems interacting with the one under consideration, and 
others. Their job during an evaluation is to articulate the specific quality attribute 
goals that the architecture should meet in order for the system to be considered a 
success. You should expect to enlist the services of twelve to fifteen stakeholders for 
the evaluation. 
Table 11.1. ATAM evaluation team roles 
Role Responsibilities Desirable characteristics 
Team 
Leader 
Sets up the evaluation; coordinates with 
client, making sure client's needs are met; 
establishes evaluation contract; forms 
evaluation team; sees that final report is 
produced and delivered (although the 
Well-organized, with managerial 
skills; good at interacting with 
client; able to meet deadlines 
Software Architecture  
Unit5  Page 2  
writing may be delegated) 
Evaluation 
Leader 
Runs evaluation; facilitates elicitation of 
scenarios; administers scenario 
selection/prioritization process; facilitates 
evaluation of scenarios against 
architecture; facilitates onsite analysis 
Comfortable in front of audience; 
excellent facilitation skills; good 
understanding of architectural 
issues; practiced in architecture 
evaluations; able to tell when 
protracted discussion is leading 
to a valuable discovery or when 
it is pointless and should be re-
directed 
Scenario 
Scribe 
Writes scenarios on flipchart or 
whiteboard during scenario elicitation; 
captures agreed-on wording of each 
scenario, halting discussion until exact 
wording is captured 
Good handwriting; stickler about 
not moving on before an idea 
(scenario) is captured; can absorb 
and distill the essence of 
technical discussions 
Proceedings 
Scribe 
Captures proceedings in electronic form 
on laptop or workstation, raw scenarios, 
issue(s) that motivate each scenario (often 
lost in the wording of the scenario itself), 
and resolution of each scenario when 
applied to architecture(s); also generates a 
printed list of adopted scenarios for 
handout to all participants 
Good, fast typist; well organized 
for rapid recall of information; 
good understanding of 
architectural issues; able to 
assimilate technical issues 
quickly; unafraid to interrupt the 
flow of discussion (at opportune 
times) to test understanding of an 
issue so that appropriate 
information is captured 
Timekeeper Helps evaluation leader stay on schedule; 
helps control amount of time devoted to 
each scenario during the evaluation phase 
Willing to interrupt discussion to 
call time 
Process 
Observer 
Keeps notes on how evaluation process 
could be improved or deviated from; 
usually keeps silent but may make discreet 
process-based suggestions to the 
evaluation leader during the evaluation; 
after evaluation, reports on how the 
process went and lessons learned for 
future improvement; also responsible for 
reporting experience to architecture 
evaluation team at large 
Thoughtful observer; 
knowledgeable in the evaluation 
process; should have previous 
experience in the architecture 
evaluation method 
Process 
Enforcer 
Helps evaluation leader remember and 
carry out the steps of the evaluation 
method 
Fluent in the steps of the method, 
and willing and able to provide 
discreet guidance to the 
evaluation leader 
Questioner Raise issues of architectural interest that 
stakeholders may not have thought of 
Good architectural insights; good 
insights into needs of 
stakeholders; experience with 
Software Architecture  
Unit5  Page 3  
systems in similar domains; 
unafraid to bring up contentious 
issues and pursue them; familiar 
with attributes of concern  
Outputs of the ATAM:- 
An ATAM-based evaluation will produce at least the following outputs: 
A concise presentation of the architecture. Architecture documentation is often 
thought to consist of the object model, a list of interfaces and their signatures, or some 
other voluminous list. But one of the requirements of the ATAM is that the 
architecture be presented in one hour, which leads to an architectural presentation that 
is both concise and, usually, understandable. 
 
Articulation of the business goals. Frequently, the business goals presented in the 
ATAM are being seen by some of the development team for the first time. 
 
Quality requirements in terms of a collection of scenarios. Business goals lead 
to quality requirements. Some of the important quality requirements are captured in 
the form of scenarios. 
 
Mapping of architectural decisions to quality requirements. Architectural 
decisions can be interpreted in terms of the qualities that they support or hinder. For 
each quality scenario examined during an ATAM, those architectural decisions that 
help to achieve it are determined.  
A set of identified sensitivity and tradeoff points. These are architectural 
decisions that have a marked effect on one or more quality attributes. Adopting a 
backup database, for example, is clearly an architectural decision as it affects 
reliability (positively), and so it is a sensitivity point with respect to reliability. 
However, keeping the backup current consumes system resources and so affects 
performance negatively. Hence, it is a tradeoff point between reliability and 
performance. Whether this decision is a risk or a nonrisk depends on whether its 
performance cost is excessive in the context of the quality attribute requirements of 
the architecture. 
 
A set of risks and nonrisks. A risk is defined in the ATAM as an architectural 
decision that may lead to undesirable consequences in light of stated quality attribute 
requirements. Similarly, a nonrisk is an architectural decision that, upon analysis, is 
deemed safe. The identified risks can form the basis for an architectural risk 
mitigation plan.  
A set of risk themes. When the analysis is complete, the evaluation team will 
examine the full set of discovered risks to look for over-arching themes that identify 
systemic weaknesses in the architecture or even in the architecture process and team. 
If left untreated, these risk themes will threaten the project's business goals. 
Software Architecture  
Unit5  Page 4  
The outputs are used to build a final written report that recaps the method, summarizes the 
proceedings, captures the scenarios and their analysis, and catalogs the findings. 
There are secondary outputs as well. Very often, representations of the architecture 
will have been created expressly for the evaluation and may be superior to whatever existed 
before. This additional documentation survives the evaluation and can become part of the 
project's legacy. Also, the scenarios created by the participants are expressions of the 
business goals and requirements for the architecture and can be used to guide the 
architecture's evolution. Finally, the analysis contained in the final report can serve as a 
statement of rationale for certain architectural decisions made (or not made). The secondary 
outputs are tangible and enumerable. 
There are intangible results of an ATAM-based evaluation. These include a palpable 
sense of community on the part of the stakeholders, open communication channels between 
the architect and the stakeholders, and a better overall understanding on the part of all 
participants of the architecture and its strengths and weaknesses. 
Phases of the ATAM:- 
Activities in an ATAM-based evaluation are spread out over four phases. 
In phase 0, "Partnership and Preparation," the evaluation team leadership and the 
key project decision makers informally meet to work out the details of the exercise. The 
project representatives brief the evaluators about the project so that the team can be 
supplemented by people who possess the appropriate expertise. Together, the two groups 
agree on logistics, such as the time and place of meetings, who brings the flipcharts, and who 
supplies the donuts and coffee. They also agree on a preliminary list of stakeholders (by 
name, not just role), and they negotiate on when the final report is to be delivered and to 
whom. They handle formalities such as a statement of work or nondisclosure agreements. 
They work out delivery to the evaluation team of whatever architectural documentation exists 
and may be useful. Finally, the evaluation team leader explains what information the manager 
and architect will be expected to show during phase 1, and helps them construct their 
presentations if necessary. 
Phase 1 and phase 2 are the evaluation phases, where everyone gets down to the 
business of analysis. By now the evaluation team will have studied the architecture 
documentation and will have a good idea of what the system is about, the overall architectural 
approaches taken, and the quality attributes that are of paramount importance. During phase 
1, the evaluation team meets with the project decision makers (usually for about a day) to 
begin information gathering and analysis. For phase 2, the architecture's stakeholders join the 
proceedings and analysis continues, typically for two days. The exact steps of phase 1 and 
phase 2 are detailed in the next section. 
Phase 3 is follow-up in which the evaluation team produces and delivers a written 
final report. The essence of this phase, however, is team self-examination and improvement. 
During a post-mortem meeting, the team discusses what went well and what didn't. They 
study the surveys handed out to participants during phase 1 and phase 2, and the process 
observer makes his or her report. Team members look for improvements in how they carry 
out their functions so that the next evaluation can be smoother or more effective. The team 
Software Architecture  
Unit5  Page 5  
catalogs how much effort was spent during the evaluation, on the part of each of the three 
participating groups. After an appropriate number of months, the team leader contacts the 
evaluation client to gauge the long-term effects of the exercise so that costs and benefits can 
be compared. 
Table 11.2 shows the four phases of the ATAM, who participates in each one, and an 
approximate timetable. 
Table 11.2. ATAM Phases and Their Characteristics 
Phase Activity Participants Typical Duration 
0 Partnership and 
preparation 
Evaluation team leadership and 
key project decision makers 
Proceeds informally as 
required, perhaps over a few 
weeks 
1 Evaluation Evaluation team and project 
decision makers 
1 day followed by a hiatus of 2 
to 3 weeks 
2 Evaluation 
(continued) 
Evaluation team, project 
decision makers, and 
stakeholders 
2 days 
3 Follow-up Evaluation team and evaluation 
client 
1 week 
STEPS OF THE EVALUATION PHASES:- 
The ATAM analysis phases (phase 1 and phase 2) consist of nine steps. Steps 1 through 6 are 
carried out in phase 1. In phase 2, with all stakeholders present, those steps are summarized 
and steps 7 through 9 are carried out. 
The analysis steps are nominally carried out in sequential order according to a set 
agenda, but sometimes there must be dynamic modifications to the schedule to accommodate 
personnel availability or architectural information. Every evaluation is unique, and there may 
be times when the team returns briefly to an earlier step, jumps forward to a later step, or 
iterates among steps, as the need dictates. 
Step 1-Present the ATAM: 
The first step calls for the evaluation leader to present the ATAM to the assembled project 
representatives. This time is used to explain the process that everyone will be following, to 
answer questions, and to set the context and expectations for the remainder of the activities. 
Using a standard presentation, the leader will describe the ATAM steps in brief and the 
outputs of the evaluation. 
Step 2-Present Business Drivers: 
Everyone involved in the evaluation-the project representatives as well as the evaluation team 
members-needs to understand the context for the system and the primary business drivers 
motivating its development. In this step, a project decision maker (ideally the project 
Software Architecture  
Unit5  Page 6  
manager) presents a system overview from a business perspective. The presentation should 
describe the following: 
The system's most important functions 
Any relevant technical, managerial, economic, or political constraints 
The business goals and context as they relate to the project 
The major stakeholders 
The architectural drivers (that is, the major quality attribute goals that shape the 
architecture) 
Step 3-Present Architecture: 
Here, the lead architect (or architecture team) makes a presentation describing the 
architecture at an appropriate level of detail. The "appropriate level" depends on several 
factors: how much of the architecture has been designed and documented; how much time is 
available; and the nature of the behavioral and quality requirements. 
In this presentation the architect covers technical constraints such as operating system, 
hardware, or middleware prescribed for use, and other systems with which the system must 
interact. Most important, the architect describes the architectural approaches (or patterns, if 
the architect is fluent in that vocabulary) used to meet the requirements. 
The architect's presentation should have a high signal-to-noise ratio. That is, it should 
convey the essence of the architecture and not stray into ancillary areas or delve too deeply 
into the details of just a few aspects. Thus, it is extremely helpful to brief the architect 
beforehand about the information the evaluation team requires. Depending on the architect, a 
dress rehearsal can be included as part of the phase 1 activities. 
FIGURE 11.1 Example of a template for the architecture presentation Source: 
Architecture Presentation (~20 slides; 60 minutes) 
Driving architectural requirements, the measurable quantities you associate with these 
requirements, and any existing standards/models/approaches for meeting these (2-3 slides) 
Important Architectural Information (4-8 slides) 
- Context diagram-the system within the context in which it will exist. Humans or 
other systems with which the system will interact. 
- Module or layer view-the modules (which may be subsystems or layers) that 
describe the system's decomposition of functionality, along with the objects, 
procedures, functions that populate these, and the relations among them (e.g., 
procedure call, method invocation, callback, containment). 
- Component-and-connector view-processes, threads along with the synchronization, 
data flow, and events that connect them. 
Software Architecture  
Unit5  Page 7  
- Deployment view-CPUs, storage, external devices/sensors along with the networks 
and communication devices that connect them. Also shown are the processes that 
execute on the various processors. 
Architectural approaches, patterns, or tactics employed, including what quality attributes they 
address and a description of how the approaches address those attributes (3-6 slides) 
- Use of commercial off-the-shelf (COTS) products and how they are 
chosen/integrated (1-2 slides) 
- Trace of 1 to 3 of the most important use case scenarios. If possible, include the 
runtime resources consumed for each scenario (1-3 slides) 
- Trace of 1 to 3 of the most important change scenarios. If possible, describe the 
change impact (estimated size/difficulty of the change) in terms of the changed 
modules or interfaces (1-3 slides) 
- Architectural issues/risks with respect to meeting the driving architectural 
requirements (2-3 slides) 
- Glossary (1 slide) 
Context diagrams, component-and-connector views, module decomposition or layered 
views, and the deployment view are useful in almost every evaluation, and the architect 
should be prepared to show them.  
During the presentation, the evaluation team asks for clarification based on their 
phase 0 examination of the architecture documentation and their knowledge of the business 
drivers from the previous step. They also listen for and write down any architectural tactics or 
patterns they see employed. 
Step 4-Identify Architectural Approaches:  
The ATAM focuses on analyzing architecture by understanding its architectural approaches.  
Architectural patterns are useful for the known ways in which each one affects particular 
quality attributes. A layered pattern tends to bring portability to a system, possibly at the 
expense of performance. 
By now, the evaluation team will have a good idea of what patterns and approaches 
the architect used in designing the system. They will have studied the architecture 
documentation, and they will have heard the architect's presentation in step 3. During that 
step, the architect is asked to explicitly name the patterns and approaches used. In this short 
step, the evaluation team simply catalogs the patterns and approaches that are evident. The 
list is publicly captured by the scribe for all to see and will serve as the basis for later 
analysis. 
Step 5-Generate Quality Attribute Utility Tree: 
Software Architecture  
Unit5  Page 8  
An architecture is either suitable or unsuitable with respect to its ability to deliver particular 
quality attributes to the system(s) built from it. The highest-performance architecture may be 
totally wrong for a system in which performance is not nearly as important as, say, security. 
The important quality attribute goals for the architecture under consideration were named in 
step 2, when the business drivers were presented, but not to any degree of specificity that 
would permit analysis. Broad goals such as "modifiability" or "high throughput" or "ability to 
be ported to a number of machines" establish important context and direction,  
In this step, the quality attribute goals are articulated in detail via a mechanism known 
as the utility tree. Here, the evaluation team works with the project decision makers to 
identify, prioritize, and refine the system's most important quality attribute goals, which are 
expressed as scenarios. The utility tree serves to make the requirements concrete, forcing the 
architect and customer representatives to define precisely the relevant quality requirements 
that they were working to provide. 
A utility tree begins with utility as the root node. Utility is an expression of the overall 
"goodness" of the system. Quality attributes form the second level because these are the 
components of utility. Quality attributes named in the business drivers presentation in step 2 
make up the initial or seed set of this second level. Typically, performance, modifiability, 
security, usability, and availability are the children of utility, but participants are free to name 
their own 
Under each of these quality attributes are specific quality attribute refinements. For 
example, performance might be decomposed into "data latency" and "transaction 
throughput." This is a step toward refining the attribute goals into quality attribute scenarios 
that are concrete enough for prioritization and analysis. Data latency might be further refined 
into "Lower storage latency on customer database to 20 ms." and "Deliver 20 frame/second 
video in real time" because both kinds of data latency are relevant to the system. 
ATAM scenarios consist of three parts: stimulus (what condition arrives at a system, 
who generated it, and what system artifact it stimulates), environment (what is going on at the 
time), and response (system's reaction to the stimulus expressed in a measurable way). 
Now we have something tangible against which to evaluate the architecture. In fact, 
the analysis steps of the ATAM consist of choosing one scenario at a time and seeing how 
well the architecture responds to, or achieves, it. Some scenarios might express more than 
one quality attribute and so might appear in more than one place in the tree.  
Not only does the team need to understand the precise goals levied on the 
architecture, but it also needs to understand their relative importance. A utility tree can easily 
contain fifty scenarios at its leaves, and there will not be time during the evaluation meeting 
to analyze them all. Hence, utility tree generation also includes a prioritization step. By 
consensus, the decision makers assign a priority to each scenario. This prioritization may be 
on a 0 to 10 scale or use relative rankings such as high, medium, and low.  
After that, scenarios are prioritized a second time, using a different criterion. The 
architect is asked to rank each scenario by how difficult he or she believes it will be for the 
architecture to satisfy. Again, a simple high/medium/low scheme works well here. 
Software Architecture  
Unit5  Page 9  
Now each scenario has an associated ordered pair: (H,H), (H,M), (H,L), and so forth. 
The scenarios that are the most important and the most difficult will be the ones where 
precious analysis time will be spent and the remainder will be kept as part of the record. A 
scenario that is considered either unimportant (L,*) or very easy to achieve (*,L) is not likely 
to receive much attention. 
The output of utility tree generation is a prioritized list of scenarios that serves as a 
plan for the remainder of the ATAM evaluation. It tells the ATAM team where to spend its 
(relatively limited) time and, in particular, where to probe for architectural approaches and 
risks. The utility tree guides the evaluators toward the architectural approaches for satisfying 
the high-priority scenarios at its leaves. 
At this point in the evaluation, all of the information necessary for analysis is on the 
table: the important qualities expected of the architecture that came from step 2's business 
drivers and step 5's utility tree, and the architecture in place as captured in step 3's 
architecture presentation and step 4's catalog of approaches used. An example of a utility tree, 
shown in tabular form (omitting the root utility node) is given in Table 11.5. 
Table 11.5. Tabular Form of the Utility Tree for the Nightingale 
ATAM Exercise 
Quality 
Attribute 
Attribute 
Refinement Scenarios 
Performance Transaction 
response time 
A user updates a patient's account in response to a 
change-of-address notification while the system is 
under peak load, and the transaction completes in 
less than 0.75 second. (H,M) 
    A user updates a patient's account in response to a 
change-of-address notification while the system is 
under twice the current peak load, and the 
transaction completes in less than 4 seconds. (L,M) 
  Throughput At peak load, the system is able to complete 150 
normalized transactions per second. (M,M) 
  Generating 
reports 
No scenarios suggested. 
Usability Proficiency 
training 
A new hire with two or more years experience in 
the business becomes proficient in Nightingale's 
core functions in less than 1 week. (M,L) 
    A user in a particular context asks for help, and the 
system provides help for that context. (H,L) 
  Normal operations A hospital payment officer initiates a payment plan 
for a patient while interacting with that patient and 
completes the process without the system 
introducing delays. (M,M) 
Maintainability   A maintainer encounters search- and response-
time deficiencies, fixes the bug, and distributes the 
bug fix. (H,M) 
Software Architecture  
Unit5  Page 10  
Table 11.5. Tabular Form of the Utility Tree for the Nightingale ATAM Exercise 
Quality 
Attribute 
Attribute 
Refinement Scenarios 
    A reporting requirement requires a change to the 
report-generating metadata. (M,L) 
    The database vendor releases a new version that 
must be installed in a minimum amount of time. 
(H,M) 
Extensibility Adding new 
product 
A product that tracks blood bank donors is created. 
(M,M) 
Security Confidentiality A physical therapist is allowed to see the part of a 
patient's record dealing with orthopedic treatment, 
but not other parts nor any financial information. 
(H,M) 
  Integrity The system resists unauthorized intrusion. (H,M) 
Availability   The database vendor releases new software, which 
is hot-swapped into place. (H,L) 
    The system supports 24/7 Web-based account 
access by patients. (L,L) 
Scalability Growing the 
system 
The kickoff customer purchases a health care 
company three times its size, requiring a 
partitioning of the database. (L,H) 
    The kickoff customer divests a business unit. (L,M) 
    The kickoff customer consolidates two business 
units. (L,M) 
    The developing organization wants to sell 
components of Nightingale. (M,L) 
Modularity Functional subsets Build a system that can function autonomously with 
core functionality. (M,L) 
  Flexibility to 
replace COTS 
products 
Replace the commercial database with one by 
another vendor. (H,M) 
    Replace the operating system. (H,M) 
    Replace the database portability layer. (H,M) 
    Replace the transaction manager. (H,M) 
Software Architecture  
Unit5  Page 11  
Table 11.5. Tabular Form of the Utility Tree for the Nightingale ATAM Exercise 
Quality 
Attribute 
Attribute 
Refinement Scenarios 
    Replace the work flow engine. (H,M) 
    Replace the commercial accounting package. (H,M) 
    Replace Solaris on the Sun platforms that host the 
database. (H,M) 
    Replace the rules engine. (H,M) 
Interoperability   Build a system that interfaces with the 
epidemiological database at the National Centers 
for Disease Control. (M,M)  
    
     
Step 6-Analyze Architectural Approaches: 
Here the evaluation team examines the highest-ranked scenarios one at a time; the architect is 
asked to explain how the architecture supports each one. Team members-especially the 
questioners-probe for the architectural approaches that the architect used to carry out the 
scenario. Along the way, the team documents the relevant architectural decisions and 
identifies and catalogs their risks, nonrisks, sensitivity points, and tradeoffs. For well-
known approaches, the team asks how the architect overcame known weaknesses in the 
approach or how the architect gained assurance that the approach sufficed. The goal is for the 
evaluation team to be convinced that the instantiation of the approach is appropriate for 
meeting the attribute-specific requirements for which it is intended. 
The scenario walkthrough leads to a discussion of possible risks, nonrisks, sensitivity 
points, or tradeoff points. These, in turn, may catalyze a deeper analysis, depending on how 
the architect responds. The key is to elicit sufficient architectural information to establish 
some link between the architectural decisions that have been made and the quality 
attribute requirements that need to be satisfied. 
Figure 11.2 shows a form for capturing the analysis of an architectural approach for a 
scenario. As shown, based on the results of this step the evaluation team can identify and 
record a set of sensitivity points and tradeoff points, risks and nonrisks. All sensitivity points 
and tradeoff points are candidate risks. The risks, nonrisks, sensitivity points, and tradeoff 
points are gathered in separate lists. The numbers R8, T3, S4, N12, and so forth, in Figure 
11.2 are simply pointers into these lists. 
 
 
Software Architecture  
Unit5  Page 12  
Figure 11.2. Example of architectural approach Analysis  
s  
At the end of this step, the evaluation team should have a clear picture of the 
most important aspects of the entire architecture, the rationale for key design decisions, 
and a list of risks, nonrisks, sensitivity points, and tradeoff points. 
Hiatus and Start of Phase 2 
At this point, phase 1 is concluded. The evaluation team retreats to summarize what it 
has learned and interacts informally (usually by phone) with the architect during a hiatus of a 
week or two. More scenarios might be analyzed during this period, if desired, or questions of 
clarification can be resolved. 
When the project's decision makers are ready to resume and the stakeholders are 
assembled, phase 2 commences. This phase is enacted by an expanded list of participants 
with additional stakeholders attending. First, step 1 is repeated so that the stakeholders 
understand the method and the role they are to play. Then the evaluation leader recaps the 
results of steps 2 through 6, and shares the current list of risks, nonrisks, sensitivity points, 
Software Architecture  
Unit5  Page 13  
and tradeoff points. Now the stake holders are up to speed with the evaluation results so far, 
and the remaining three steps can be carried out. 
Step 7-Brainstorm and Prioritize Scenarios: 
While utility tree generation is used primarily to understand how the architect perceived and 
handled quality attribute architectural drivers, the purpose of scenario brainstorming is to take 
the pulse of the larger stakeholder community. Scenario brainstorming works well in larger 
groups, creating an atmosphere in which the ideas and thoughts of one person stimulate 
others' ideas. The process fosters communication and creativity, and serves to express the 
collective mind of the participants. The prioritized list of brainstormed scenarios is compared 
with those from the utility tree exercise. 
 In this step, the evaluation team asks the stakeholders to brainstorm scenarios that are 
operationally meaningful with respect to the stakeholders' individual roles. A maintainer will 
likely propose a modifiability scenario, for example, while a user will probably come up with 
a scenario that expresses useful functionality or ease of operation. 
Utility tree scenarios that have not been analyzed are fair game. Stakeholders are free 
to put them into the brainstorm pool, which gives them the opportunity to revisit scenarios 
from step 5 and step 6 that they might feel received too little attention. 
Once the scenarios have been collected, they must be prioritized, for the same reasons 
that the scenarios in the utility tree needed to be prioritized: The evaluation team needs to 
know where to devote its limited analytical time. First, stakeholders are asked to merge 
scenarios they feel represent the same behavior or quality concern. Then they vote for those 
they feel are most important. Each stakeholder is allocated a number of votes equal to 30% of 
the number of scenarios,[1] rounded up. So, if there were twenty scenarios collected, each 
stakeholder would be given six votes. These votes can be allocated in any way that the 
stakeholder sees fit: all six votes for one scenario, one vote for each of the six, or anything in 
between. 
[1] This is a common facilitated brainstorming technique. 
Each stakeholder casts his or her votes publicly; our experience tells us it is more fun 
that way and builds unity among the participants. Once the votes are tallied, the evaluation 
leader orders the scenarios by vote total and looks for a sharp drop-off in the number of votes. 
Scenarios "above the line" are adopted and carried forth to subsequent steps. So for example, 
a team might consider only the top five scenarios. 
Step 8-Analyze Architectural Approaches: 
After the scenarios have been collected and prioritized, the evaluation team guides the 
architect in the process of carrying out the highest ranked scenarios from step 7. The architect 
explains how relevant architectural decisions contribute to realizing each one.  
In this step the evaluation team performs the same activities as in step 6, mapping the 
highest-ranked, newly generated scenarios onto the architectural artifacts uncovered thus far. 
Software Architecture  
Unit5  Page 14  
Step 9-Present Results: 
Finally, the collected information from the ATAM needs to be summarized and presented 
once again to stakeholders. The following outputs are presented: 
The architectural approaches documented 
The set of scenarios and their prioritization from the brainstorming 
The utility tree 
The risks discovered 
The nonrisks documented 
The sensitivity points and tradeoff points found 
These outputs are all uncovered, publicly captured, and cataloged during the evaluation. 
In step 9, however, the evaluation team adds value by grouping risks into risk themes, based 
on some common underlying concern or systemic deficiency. For example, a group of risks 
about inadequate or out-of-date documentation might be grouped into a risk theme stating 
that documentation is given insufficient consideration. A group of risks about the system's 
inability to function in the face of various hardware and/or software failures might lead to a 
risk theme about insufficient attention to backup capability or providing high availability. 
For each risk theme, the evaluation team identifies which of the business drivers listed in 
step 2 are affected. Identifying risk themes and then relating them to specific drivers brings 
the evaluation full circle by relating the final results to the initial presentation, thus providing 
a satisfying closure to the exercise. As important, it elevates the risks that were uncovered to 
the attention of management. What might otherwise have seemed to a manager like an 
esoteric technical issue is now identified unambiguously as a threat to something the manager 
is on record as caring about. 
Table 11.3 summarizes the nine steps of the ATAM and shows how each step contributes 
to the outputs the ATAM delivers after an evaluation. A "**" means that the step is a primary 
contributor to the output; a "*" means that it is a secondary contributor. 
Table 11.3. Steps and ATAM Outputs, Correlated 
  ATAM Outputs 
Steps 
Prioritized 
Statement of 
Quality 
Attribute 
Requirement 
s 
Catalog of 
Architectura 
l Approaches 
Used 
Approach 
- and 
Quality 
Attribute-
Specific 
Analysis 
Questions 
Mapping of 
Architectura 
l Approaches 
to Quality 
Attributes 
Risk 
s and 
Non-
risks 
Sensitivit 
y and 
Tradeoff 
Points 
1. Present 
ATAM 
            
2. Present 
business 
drivers 
*[a]       *[b]   
Software Architecture  
Unit5  Page 15  
Table 11.3. Steps and ATAM Outputs, Correlated 
  ATAM Outputs 
3. Present 
architecture 
  **     *[c] *[d] 
4. Identify 
architectura 
l 
approaches 
  ** **   *[e] *[f] 
5. Generate 
quality 
attribute 
utility tree 
**           
6. Analyze 
architectura 
l 
approaches 
  *[g] ** ** ** ** 
7. 
Brainstorm 
and 
prioritize 
scenarios 
**           
8. Analyze 
architectura 
l 
approaches 
  * ** ** ** ** 
9. Present 
results 
            
 
[a] The business drivers include the first, coarse description of the quality attributes. 
[b] The business drivers presentation might disclose an already identified or long-standing risk 
that should be captured. 
[c] The architect may identify a risk in his or her presentation. 
[d] The architect may identify a sensitivity of tradeoff point in his or her presentation. 
[e] Many architectural approaches have standard associated risks. 
[f] Many architectural approaches have associated standard sensitivities and quality attribute 
tradeoffs. 
Software Architecture  
Unit5  Page 16  
[g] The analysis steps might reveal one or more architectural approaches not identified in step 
4, which will then produce new approach-specific questions. 
USING THE LIMITED TIME OF AN EVALUATION EFFECTIVELY 
In the introduction, we identified limited time as one of the main problems in conducting an 
architectural evaluation. Now we can see how the ATAM solves that problem. The business 
goals are used as motivation for the collection of scenarios that represent the utility tree. 
Other scenarios are prioritized, essentially, as a bottom-up check on the top-down scenario 
generation of the utility tree. Only the high-priority and difficult scenarios are analyzed. The 
evaluators are guided to these important but problematic areas of the architecture by the steps 
of the method. These are the areas that will yield the most important results. 
The CBAM (Cost Benefit Analysis Method) 
In ATAM is missing an important consideration: The biggest tradeoffs in large, complex 
systems usually have to do with economics. How should an organization invest its resources 
in a manner that will maximize its gains and minimize its risk? In the past, this question 
primarily focused on costs, and even then these were primarily the costs of building the 
system in the first place and not the long-term costs through cycles of maintenance and 
upgrade. As important, or perhaps more important than costs, are the benefits that an 
architectural decision may bring to an organization. 
Called the Cost Benefit Analysis Method (CBAM), it builds on the ATAM to model 
the costs and the benefits of architectural design decisions and is a means of optimizing such 
decisions. The CBAM provides an assessment of the technical and economic issues and 
architectural decisions. 
Decision-Making Context:- 
The software architect or decision maker wishes to maximize the difference between the 
benefit derived from the system and the cost of implementing the design. The CBAM begins 
where the ATAM concludes and, in fact, depends upon the artifacts that the ATAM produces 
as output. Figure 12.1 depicts the context for the CBAM. 
Figure 12.1. Context for the CBAM 
 
Software Architecture  
Unit5  Page 17  
Because architectural strategies have technical and economic implications, the 
business goals of a software system should influence the strategies used by software 
architects or designers. The direct economic implication is the cost of implementing the 
system. The technical implications are the characteristics of the system-namely, the quality 
attributes. In turn the quality attributes have economic implications because of the benefits 
that can be derived. 
When an ATAM has been applied to a software system, we have as a result a set of 
artifacts documented on completion. They are: 
A description of the business goals that are crucial to the success of the system 
A set of architectural views that document the existing or proposed architecture 
A utility tree that represents a decomposition of the stakeholders' goals for the 
architecture, starting with high-level statements of quality attributes and ending with 
specific scenarios 
A set of risks that have been identified 
A set of sensitivity points (architectural decisions that affect some quality attribute 
measure of concern) 
A set of tradeoff points (architectural decisions that affect more than one quality 
attribute measure, some positively and some negatively) 
The ATAM identifies the set of key architectural decisions relevant to the quality 
attribute scenarios elicited from the stakeholders. These decisions result in some specific 
quality attribute responses-namely, particular levels of availability, performance, security, 
usability, modifiability, and so forth. But each architectural decision also has associated costs.  
The ATAM uncovers the architectural decisions made in the system and links them to 
business goals and quality attribute response measures. The CBAM builds on this base by 
eliciting the costs and benefits associated with these decisions. Given this information, the 
stakeholders can then decide whether to use redundant hardware, checkpointing, or some 
other tactic to achieve the system's desired availability. Or they can choose to invest their 
finite resources in some other quality attribute-perhaps believing that higher performance will 
have a better benefit-to-cost ratio. A system always has a limited budget for creation or 
upgrade, so every architectural choice is, in some sense, competing with every other one for 
inclusion. 
The CBAM simply aids in the elicitation and documentation of the costs, benefits, 
and uncertainty of a "portfolio" of architectural investments and gives the stakeholders 
a framework within which they can apply a rational decision-making process that suits 
their needs and their risk aversion. 
To briefly summarize, the idea behind the CBAM is that architectural strategies (a 
collection of architectural tactics) affect the quality attributes of the system and these in turn 
provide system stakeholders with some benefit. We refer to this benefit as utility. Each 
architectural strategy provides a specific level of utility to the stakeholders. Each also has 
cost and takes time to implement. Given this information, the CBAM can aid the stakeholders 
in choosing architectural strategies based on their return on investment (ROI)-the ratio of 
benefit to cost. 
Software Architecture  
Unit5  Page 18  
The Basis for the CBAM:- 
Our goal here is to develop the theory underpinning a measure of ROI for various 
architectural strategies in light of scenarios chosen by the stakeholders. 
We begin by considering a collection of scenarios generated either as a portion of an 
ATAM or especially for the CBAM evaluation. We examine how they differ in the values of 
their projected responses and then assign utility to those values. The utility is based on the 
importance of each scenario being considered with respect to its anticipated response value. 
We next consider the architectural strategies that lead to the various projected responses. 
Each strategy has a cost, and each impacts multiple quality attributes. That is, an architectural 
strategy could be implemented to achieve some projected response, but while achieving that 
response it also affects some other quality attributes. The utility of these "side effects" must 
be taken into account when considering a strategy's overall utility. It is this overall utility that 
we combine with the project cost of an architectural strategy to calculate a final ROI measure. 
UTILITY:-  
Utility is determined by considering the issues described in the following sections. 
Variations of Scenarios: 
The CBAM uses scenarios as a way to concretely express and represent specific quality 
attributes, just as in the ATAM. Also as in the ATAM, we structure scenarios into three parts: 
stimulus (an interaction with the system), environment (the system's state at the time), and 
response (the measurable quality attribute that results). However, there is a difference 
between the methods: The CBAM actually uses a set of scenarios (generated by varying the 
values of the responses) rather than individual scenarios as in the ATAM. This leads to the 
concept of a utility-response curve. 
Utility-Response Curves: 
Every stimulus-response value pair in a scenario provides some utility to the stakeholders, 
and the utility of different possible values for the response can be compared. We can portray 
each relationship between a set of utility measures and a corresponding set of response 
measures as a graph-a utility-response curve. Some examples of utility-response curves are 
shown in Figure 12.2. In each, points labeled a, b, or c represent different response values. 
The utility-response curve thus shows utility as a function of the response value. 
 
 
 
 
 
Software Architecture  
Unit5  Page 19  
Figure 12.2. Some sample utility-response curves 
 
The utility-response curve depicts how the utility derived from a particular response 
varies as the response varies. As seen in Figure 12.2, the utility could vary nonlinearly, 
linearly, or even as a step-function. For example, graph (c) portrays a steep rise in utility over 
a narrow change in a quality attribute response level, such as the performance example stated 
above. The availability example might be better characterized by graph (a), where a modest 
change in the response level results in only a very small change in utility to the user. 
To build the utility-response curve, we first determine the quality attribute levels for 
the best-case and worst-case situations. The best-case quality attribute level is that above 
which the stakeholders foresee no further utility. For example, a system response to the user 
of 0.1 second is perceived as instantaneous, so improving it further so that it responds in 0.03 
second has no utility. Similarly, the worst-case quality attribute level is a minimum threshold 
above which a system must perform; otherwise it is of no use to the stakeholders. These 
levels-best-case and worst-case-are assigned utility values of 100 and 0, respectively. 
We must then determine the current and desired utility levels for the scenario. The 
respective utility values (between 0 and 100) for the current and desired cases are elicited 
from the stakeholders, using the best-case and worst-case values as reference points (e.g., we 
are currently half as good as we would like to be, but if we reach the desired quality attribute 
level, we will have 90% of the maximum utility; hence, the current utility level is set to 50 
and the desired utility level is set to 90). In this manner the curves are generated for all of the 
scenarios. 
Software Architecture  
Unit5  Page 20  
Priorities of Scenarios: 
Different scenarios within a given system have different levels of importance to the 
stakeholders and hence different utilities. To characterize the relative importance of each 
scenario, a weight is assigned through a two-step voting exercise. In the first step the 
stakeholders vote on the scenarios to establish an ordering among them. This voting is based 
on each scenario's "expected" response value. The stakeholders then assign a weight of 1 to 
the highest-rated scenario and a fractional amount to the other scenarios based on their 
relative importance. 
Architectural Strategies: 
It is the job of the architect, or architects, to determine the architectural strategies for moving 
from the current quality attribute response level to the desired or even best-case level. A 
portion of the CBAM is devoted to this task. For each strategy, we can derive 
the expected value of the response in each scenario. The utility of the expected value 
is calculated using interpolation from the four values already elicited from the 
stakeholders. 
the effect of the architectural strategy on other attributes of interest. 
a cost estimate for implementing the architectural strategy. 
Side effects - 
Each architectural strategy will impact not only the quality attribute from the scenario being 
considered currently but will typically also affect other quality attributes (this is why there are 
architectural tradeoffs!). It is important to determine the utility of these additional side 
effect attribute responses that arise as a result of applying the architectural strategy. In the 
worst case, we must create a new version of the scenario for the side effect attribute and 
determine its utility-response curve. However, in practice, if the quality attribute is important 
to the stakeholders, then it has occurred in one of the other scenarios and the utility-response 
curve has already been constructed for that response. In this case, the only thing left to 
determine is the expected utility associated with that quality attribute for the given 
architectural strategy. Notice that it is possible that the expected utility for a particular 
attribute may be negative if the architectural strategy is designed to emphasize an attribute in 
conflict with the one whose utility we are currently calculating. 
Once this additional information has been elicited we can calculate the benefit of 
applying an architectural strategy by summing its benefits to all relevant quality attributes. 
Determining benefit and normalization -  
We calculate the overall utility of an architectural strategy across scenarios from the utility-
response curves by summing the utility associated with each one (weighted by the importance 
of the scenario). For each architectural strategy, i, we calculate a benefit, Bi as follows: 
 
Software Architecture  
Unit5  Page 21  
where bi,j is the benefit accrued to strategy i due to its effect on scenario j and Wj is the weight 
of scenario j. Referring to Figure 12.2, each bi,j is calculated as the change in utility brought 
about by the architectural strategy with respect to this scenario: bi,j = Uexpected - Ucurrent; that 
is, the utility of the expected value of the architectural strategy minus the utility of the current 
system relative to this scenario. The effect of multiplying the weight, Wj, is to normalize this 
utility value by the relative importance of the various scenarios, as already described. 
CALCULATING ROI:-  
The ROI value for each architectural strategy is the ratio of the total benefit, Bi, to the 
Cost, Ci, of implementing it. 
 
Using this ROI score, the architectural strategies can be rank-ordered; this rank 
ordering can then be used to determine the optimal order for implementation of the various 
strategies. 
Consider curves (a) and (b) in Figure 12.2. Curve (a) "flattens out" as the quality 
attribute response improves. In this case, it is likely that a point is reached past which ROI 
decreases as the quality attribute response improves. In other words, spending more money 
will not yield a significant increase in utility. On the other hand, consider curve (b), for which 
a small improvement in quality attribute response can yield a very significant increase in 
utility. There an architectural strategy whose ROI is too low might rank significantly higher 
with a modest improvement in its quality attribute response. 
Implementing the CBAM:- 
Turning the foundations for the CBAM into a set of practical steps involves the following 
steps. 
STEPS 
A process flow diagram for the CBAM is given in Figure 12.3. The first four steps are 
annotated with the relative number of scenarios they consider. That number steadily 
decreases, ensuring that the method concentrates the stakeholders' time on the scenarios 
believed to be of the greatest potential in terms of ROI. 
Step 1: Collate scenarios. Collate the scenarios elicited during the ATAM exercise, 
and give the stakeholders the chance to contribute new ones. Prioritize these scenarios 
based on satisfying the business goals of the system and choose the top one-third for 
further study. 
 
Step 2: Refine scenarios. Refine the scenarios output from step 1, focusing on their 
stimulus-response measures. Elicit the worst-case, current, desired, and best-case 
quality attribute response level for each scenario. 
 
Step 3: Prioritize scenarios. Allocate 100 votes to each stakeholder and have them 
distribute the votes among the scenarios, where their voting is based on 
Software Architecture  
Unit5  Page 22  
the desired response value for each scenario. Total the votes and choose the top 50% 
of the scenarios for further analysis. Assign a weight of 1.0 to the highest-rated 
scenario; assign the other scenarios a weight relative to the highest rated. This 
becomes the weighting used in the calculation of a strategy's overall benefit. Make a 
list of the quality attributes that concern the stakeholders. 
 
Step 4: Assign utility. Determine the utility for each quality attribute response level 
(worst-case, current, desired, best-case) for the scenarios from step 3. 
 
Step 5: Develop architectural strategies for scenarios and determine their 
expected quality attribute response levels. Develop (or capture already developed) 
architectural strategies that address the chosen scenarios and determine the "expected" 
quality attribute response levels that will result from them. Given that an architectural 
strategy may have effects on multiple scenarios, we must perform this calculation for 
each scenario affected. 
 
Step 6: Determine the utility of the "expected" quality attribute response 
levels by interpolation. Using the elicited utility values (that form a utility curve), 
determine the utility of the expected quality attribute response level for the 
architectural strategy. Do this for each relevant quality attribute enumerated in step 3. 
 
Step 7: Calculate the total benefit obtained from an architectural 
strategy. Subtract the utility value of the "current" level from the expected level and 
normalize it using the votes elicited in step 3. Sum the benefit due to a particular 
architectural strategy across all scenarios and across all relevant quality attributes. 
 
Step 8: Choose architectural strategies based on ROI subject to cost and 
schedule constraints. Determine the cost and schedule implications of each 
architectural strategy. Calculate the ROI value for each as a ratio of benefit to cost. 
Rank-order the architectural strategies according to the ROI value and choose the top 
ones until the budget or schedule is exhausted. 
Step 9: Confirm results with intuition. For the chosen architectural strategies, 
consider whether these seem to align with the organization's business goals. If not, 
consider issues that may have been overlooked while doing this analysis. If there are 
significant issues, perform another iteration of these steps. 
 
 
 
 
 
 
Software Architecture  
Unit5  Page 23  
Figure 12.3. Process flow diagram for the CBAM 
 
  
Software Architecture  
Unit5  Page 24  
The World Wide Web: A Case Study in Interoperability  
The Architecture Business Cycle (ABC) can be found in the way in which the goals, business 
model, and architecture of the World Wide Web have changed since its introduction in 1990. 
No one-not the customers, the users, or the architect (Tim Berners-Lee)-could have foreseen 
the explosive growth and evolution of the Web. In this chapter, we interpret the Web from the 
point of view of the ABC and observe how changes in its architecture reflect the changing 
goals and business needs of the various players. We first look at the Web's origins in terms of 
its original requirements and players and then look at how its server-side architecture has 
changed as a result of the ABC. 
Relationship to the Architecture Business Cycle:- 
The original proposal for the Web came from Tim Berners-Lee, a researcher with the 
European Laboratory for Particle Physics (CERN), who observed that the several thousand 
researchers at CERN formed an evolving human "web." People came and went, developed 
new research associations, lost old ones, shared papers, chatted in the hallways, and so on, 
and Berners-Lee wanted to support this informal web with a similar web of electronic 
information. In 1989, he created and circulated throughout CERN a document 
entitled Information Management: A Proposal. By October of 1990 a reformulated version of 
the project proposal was approved by management, the name World Wide Web was chosen, 
and development began. 
Figure 13.1 shows the elements of the ABC as they applied to the initial proposal 
approved by CERN management. The system was intended to promote interaction among 
CERN researchers (the end users) within the constraints of a heterogeneous computing 
environment. The customer was CERN management, and the developing organization was a 
lone CERN researcher. The business case made by Berners-Lee was that the proposed system 
would increase communication among CERN staff. This was a very limited proposal with 
very limited (and speculative) objectives. There was no way of knowing whether such a 
system would, in fact, increase communication.  
Figure 13.1. The original ABC for the Web 
 
Software Architecture  
Unit5  Page 25  
The technical environment was familiar to those in the research community, for which 
the Internet had been a mainstay since its introduction in the early 1970s. The net had weak 
notions of central control (volunteer committees whose responsibilities were to set protocols 
for communication among different nodes on the Internet and to charter new newsgroups) 
and an unregulated, "wild-west" style of interaction, primarily through specialized 
newsgroups. 
Hypertext systems had had an even longer history, beginning with the vision of 
Vannevar Bush in the 1940s. Bush's vision had been explored throughout the 1960s and 
1970s and into the 1980s, with hypertext conferences held regularly to bring researchers 
together. However, Bush's vision had not been achieved on a large scale by the 1980s: The 
uses of hypertext were primarily limited to small-scale documentation systems. That was to 
change. 
CERN management approved Berners-Lee's proposal in October 1990. By November 
he had developed the first Web program on the NeXT platform, which meant he clearly had 
begun working on the implementation before receiving formal management approval. This 
loose coupling between management approval and researcher activity is quite common in 
research organizations in which small initial investments are required. By their nature, 
research organizations tend to generate projects from the bottom up more often than 
commercial organizations do, because they are dependent on the researchers' originality and 
creativity and allow far more freedom than is typical in a commercial organization. 
The initial implementation of a Web system had many features that are still missing 
from more recent Web browsers. For example, it allowed users to create links from within the 
browser, and it allowed authors and readers to annotate information. Berners-Lee initially 
thought that no user would want to write HyperText Markup Language (HTML) or deal with 
uniform resource locators (URLs). He was wrong. Users have been willing to put up with 
these inconveniences to have the power of publishing on the Web. 
Requirements and Qualities:- 
The World Wide Web, as conceived and initially implemented at CERN, had several 
desirable qualities. It was portable, able to interoperate with other types of computers running 
the same software, and was scalable and extensible. The business goals of promoting 
interaction and allowing heterogeneous computing led to the quality goals of remote access, 
interoperability, extensibility, and scalability, which in turn led to libWWW, the original 
software library that supported Web-based development and a distributed client-server 
architecture. libWWW embodies strict separation of concerns and therefore works on 
virtually any hardware and readily accepts new protocols, new data formats, and new 
applications. Because it has no centralized control, the Web appears to be able to grow 
without bounds. 
Table 13.1. Web Growth Statistics 
Date Number of Web Sites Percentage of .com Sites Hosts per Web Server 
6/93 130 1.5 13,000 
12/93 623 4.6 3,475 
Software Architecture  
Unit5  Page 26  
Table 13.1. Web Growth Statistics 
Date Number of Web Sites Percentage of .com Sites Hosts per Web Server 
6/94 2,738 13.5 1,095 
12/94 10,022 18.3 451 
6/95 23,500 31.3 270 
1/96 100,000 50.0 94 
6/96 252,000 68.0 41 
1/97 646,162 62.6 40 
1/98 1,834,710   16.2 
1/99 4,062,280   10.6 
1/00 9,950,491   7.3 
1/01 27,585,719 54.68 4.0 
We will deal with these core requirements, and others, in more detail now, returning 
to the structure of libWWW later in Section 13.3. The requirement for portability and the 
heterogeneous computing environment led to the introduction of the browser as a separate 
element, thereby fostering the development of more sophisticated browsers. 
THE ORIGINAL REQUIREMENTS:  
The initial set of requirements for the Web, as established in the original project proposals, 
were as follows: 
 
Remote access across networks. Any information had to be accessible from any 
machine on a CERN network. 
 
Heterogeneity. The system could not be limited to run on any specific hardware or 
software platform. 
 
Noncentralization. In the spirit of a human web and of the Internet, there could not 
be any single source of data or services. This requirement was in anticipation that the 
Web would grow. The operation of linking to a document, in particular, had to be 
decentralized. 
 
Access to existing data. Existing databases had to be accessible. 
 
Ability for users to add data. Users should be able to "publish" their own data on 
the Web, using the same interface used to read others' data. 
Software Architecture  
Unit5  Page 27  
 
Private links. Links and nodes had to be capable of being privately annotated. 
 
Bells and whistles. The only form of data display originally planned was display on 
a 24 x 80 character ASCII terminal. Graphics were considered optional. 
 
Data analysis. Users should be able to search across the various databases and look 
for anomalies, regularities, irregularities, and so on. Berners-Lee gave, as examples, 
the ability to look for undocumented software and organizations with no people. 
 
Live links. Given that information changes all the time, there should be some way of 
updating a user's view of it. This could be by simply retrieving the information every 
time the link is accessed or (in a more sophisticated fashion) by notifying a user of a 
link whenever the information has changed. 
In addition to these requirements, there were a number of nonrequirements identified. For 
example, copyright enforcement and data security were explicitly mentioned as requirements 
that the original project would not deal with. The Web, as initially conceived, was to be a 
public medium. Also, the original proposal explicitly noted that users should not have to use 
any particular markup format. 
Other criteria and features that were common in proposals for hypertext systems at the 
time but that were missing from the Web proposal are as follows: 
Controlling topology 
Defining navigational techniques and user interface requirements, including keeping a 
visual history 
Having different types of links to express differing relationships among nodes 
For example, data analysis, live links, and private link capabilities are still relatively 
crude to this day.  
Adaptation and selective postponement of requirements are characteristic of 
unprecedented systems. Requirements are often lists of desirable characteristics, and in 
unprecedented systems the tradeoffs required to realize these requirements are often unknown 
until a design exists. In the process of making the tradeoffs, some requirements become more 
important and others less so. 
The effect of one of the requirements turned out to have been greatly underestimated. 
Namely, the "bells and whistles" of graphics dominate much of today's Web traffic. Graphics 
today carry the bulk of the interest and consume the bulk of the Internet traffic generated by 
the Web. And yet Berners-Lee and CERN management did not concern themselves with 
graphics in the initial proposal, and the initial Web browser was line oriented. Similarly, the 
original proposal eschewed any interest in multimedia research for supporting sound and 
video. 
Some nonrequirements, as the ABC has been traversed, have also become 
requirements. Security, for one, has proven to be a substantial issue, particularly as the Web 
has become increasingly dominated by commercial traffic. The security issue is large and 
Software Architecture  
Unit5  Page 28  
complex, given the distributed, decentralized form of the Internet. Security is difficult to 
ensure when protected access to private data cannot be guaranteed-the Web opens a window 
onto your computer, and some uninvited guests are sure to crawl through. 
This has become even more relevant in recent years as e-commerce has begun to drive 
the structure and direction of the Web and a large number of ad hoc mechanisms have been 
created to facilitate it. The most obvious is simple encryption of sensitive data, typically via 
SSL (Secure Sockets Layer), seen in Web browsers as HTTPS (HyperText Transfer Protocol 
Secure). But this protocol only decreases the likelihood of others snooping on your private 
data while it is being transmitted over a public network. Other solutions-such as Microsoft's 
Passport-have you prove that you are who you say you are.  
REQUIREMENTS COME AND GO: 
No one could have foreseen the tremendous growth of the Web, or of the Internet, over the 
past few years. According to recent statistics, the Web has been doubling in size every three 
to six months, from about 130 sites in mid-1993 to more than 230,000 sites in mid-1996 to 27 
million in early 2001 (see Table 13.1). Figure 13.2 shows how the base communication paths 
for the Internet blanket the United States. Similarly, the number of Internet hosts-at least as 
counted by registered Internet Protocol (IP) addresses-grew from 1.3 million in 1993 to 9.5 
million in early 1996. 
Figure 13.2. Internet backbones in the United States. 
 
Both the Web and the Internet have grown, but the Web has grown much faster as a 
whole. This can be seen in the final column of Table 13.1, where we see that the ratio of 
Internet hosts to Web servers keeps decreasing. This means that an ever-greater proportion of 
Internet hosts are becoming Web servers. 
Software Architecture  
Unit5  Page 29  
In addition to its enormous growth, the nature of the Web has changed, as indicated 
by the third column of Table 13.1. Although its beginnings were in the research community, 
it is increasingly dominated by commercial traffic (as indicated by Internet hosts whose 
names end in ".com"). The percentage of .com sites has leveled out at around 55%, but this is 
due mainly to the rise of other domains, such as .net and .biz, rather than to any decline in 
commercial activity. 
The advent of easy, widespread access to the Web has had an interesting side effect. 
Easy access to graphics in a distributed, largely uncontrolled fashion has spawned the 
"cyberporn" industry, which has led to a new requirement: that content be labeled and access 
to content be controllable. The result is the platform for Internet content selection (PICS) 
specification, an industry-wide set of principles, and vendor implementations of them, that 
allows the labeling of content and flexible selection criteria. In this way, content producers 
are not limited in what they provide, but content consumers can tailor what they view or what 
they permit others to view according to their own tastes and criteria. For example, a parent 
can prevent a child from viewing movies other than those suitably rated, and an employer can 
prevent an employee from accessing non-business-related sites during business hours. 
To see how far and how fast the Web has diverged from its original concept, imagine 
that Berners-Lee had proposed a requirement for restriction of content to prevent children 
from accessing pornography. The management of CERN would have tossed out his proposal 
without discussion. We return to this point about changing stakeholder concerns when we 
revisit the ABC for the WWW in Section 13.5. 
Architectural Solution:- 
The basic architectural approach used for the Web, first at CERN and later at the World Wide 
Web Consortium (W3C), relied on clients and servers and a library (libWWW) that masks all 
hardware, operating system, and protocol dependencies. Figure 13.3 shows how the content 
producers and consumers interact through their respective servers and clients. The producer 
places content that is described in HTML on a server machine. The server communicates 
with a client using the HyperText Transfer Protocol (HTTP). The software on both the server 
and the client is based on libWWW, so the details of the protocol and the dependencies on the 
platforms are masked from it.  
Figure 13.3. Content producers and consumers interact through clients and servers 
 
Software Architecture  
Unit5  Page 30  
We now go into more detail about both the libWWW and the client-server 
architecture used as the basis for the original  
MEETING THE ORIGINAL REQUIREMENTS: libWWW 
As stated earlier, libWWW is a library of software for creating applications that run on either 
the client or the server. It provides the generic functionality that is shared by most 
applications: the ability to connect with remote hosts, the ability to understand streams of 
HTML data, and so forth. 
libWWW is a compact, portable library that can be built on to create Web-based 
applications such as clients, servers, databases, and Web spiders. It is organized into five 
layers, as shown in Figure 13.4. 
Figure 13.4. A layered view of libWWW 
 
The generic utilities provide a portability layer on which the rest of the system rests. 
This layer includes basic building blocks for the system such as network management, data 
types such as container classes, and string manipulation utilities. Through the services 
provided by this layer, all higher levels can be made platform independent, and the task of 
porting to a new hardware or software platform can be almost entirely contained within the 
porting of the utilities layer, which needs to be done only once per platform. 
The core layer contains the skeletal functionality of a Web application-network 
access, data management and parsing, logging, and the like. By itself, this layer does nothing. 
Rather, it provides a standard interface for a Web application to be built upon, with the actual 
functionality provided by plug-in modules and call-out functions that are registered by an 
application. Plug-ins are registered at runtime and do the actual work of the core layer-
sending and manipulating data. They typically support protocols, handle low-level transport, 
and understand data formats. Plug-ins can be changed dynamically, making it easy to add 
new functionality or even to change the very nature of the Web application. 
Software Architecture  
Unit5  Page 31  
Call-out functions provide another way for applications to extend the functionality 
provided in the core layer. They are arbitrary application-specific functions that can be called 
before or after requests to protocol modules. 
What is the relationship between the generic utilities and the core? The generic 
utilities provide platform-independent functions, but they can be used to build any networked 
application. The core layer, on the other hand, provides the abstractions specific to building a 
Web application. 
The stream layer provides the abstraction of a stream of data used by all data 
transported between the application and the network. 
The access layer provides a set of network-protocol-aware modules. The standard set 
of protocols that libWWW originally supported are HTTP-the underlying protocol of the 
World Wide Web; Network News Transport Protocol (NNTP)-the protocol for Usenet 
messages; Wide Area Information Server (WAIS)-a networked information retrieval system; 
File Transfer Protocol (FTP), TELNET, rlogin, Gopher, local file system, and TN3270. But 
others, such as HTTPS (HTTP Secure) have been added.  
The uppermost layer, consisting of the Web application modules, is not an actual 
application but rather a set of functionality useful for writing applications. It includes 
modules for common functionality, such as caching, logging, and registering proxy servers 
(for protocol translation) and gateways (for dealing with security firewalls, for example); 
history maintenance, and so on. 
LESSONS  FROM  libWWW: 
As a result of building libWWW and the many applications that rest on it, several lessons 
have been learned. These lessons have derived in part from the developers' experience in 
trying to meet the requirements that we listed in Section 13.2-that Web-based tools be 
heterogeneous, support remote access across networks, be noncentralized, and so forth. 
However, the requirement that turned out to be the most challenging was supplying 
unforeseen bells and whistles. That is, allowing the features of Web-based applications to 
grow has driven many decisions in libWWW and has led to the following lessons: 
Formalized application programming interfaces (APIs) are required. These are the 
interfaces that present the functionality of libWWW to the programs built on top of it. 
For this reason, APIs should be specified in a language-independent fashion because 
libWWW is meant to support application development on a wide variety of platforms 
and in many languages. 
Functionality and the APIs that present it must be layered. Different applications 
will need access to different levels of service abstraction, which are most naturally 
provided by layers. 
The library must support a dynamic, open-ended set of features. All of these 
features must be replaceable, and it must be possible to make replacements at runtime. 
Processes built on the software must be thread safe. Web-based applications must 
support the ability to perform several functions simultaneously, particularly because 
operations such as downloading large files over a slow communication link may take 
a considerable amount of real time. This requires the use of several simultaneous 
Software Architecture  
Unit5  Page 32  
threads of control. Thus, the functionality exposed by the APIs must be safe to use in 
a threaded environment. 
It turns out that libWWW does not support all of these goals as well as it might. 
Furthermore, libWWW is meant to run on many different platforms, and so it can’t depend 
on a single-thread model. Thus, it has implemented pseudothreads, which provide some, but 
not all, of the required functionality. Finally, most current Web applications do not support 
dynamic feature configuration; they require a restart before new services can be registered. 
AN EARLY CLIENT-SERVER ARCHITECTURE USING libWWW: 
In Figure 13.5 we show a deployment view of a typical Web client-server that was built using 
libWWW services. A module decomposition view is also shown for the HTTP client and 
server components of the deployment view. The figure makes a few points about libWWW. 
First, not all parts of a client-server are built from it. For example, the user interface is 
independent. Second, the names of the managers do not directly correspond to the names of 
the layers: Although the access manager, protocol manager, and stream manager are clearly 
related to the access and stream layers, the cache manager uses the services of the application 
layer. The stream managers in the client-server pair manage the low-level communications, 
thus ensuring transparent communication across a network for the other parts of the system. 
Figure 13.5. Deployment view of a Web client-server with a module decomposition view of 
the HTTP client and server components 
 
The user interface (UI) manager handles the look-and-feel of the client's user 
interface. However, given the open-ended set of resources that a WWW system can handle, 
Software Architecture  
Unit5  Page 33  
another element, the presentation manager, can delegate information display to external 
programs (viewers) to view resources known by the system but that the UI manager does not 
directly support. This delegation is a compromise between the competing desires of user 
interface integration (which provides for a consistent look-and-feel and hence better 
usability) and extensibility. 
The UI manager captures a user's request for information retrieval in the form of a 
URL and passes the information to the access manager. The access manager determines if the 
requested URL exists in cache and also interprets history-based navigation (e.g., "back"). If 
the file is cached, it is retrieved from the cache manager and passed to the presentation 
manager for display to either the UI or an external viewer. If it is not cached, the protocol 
manager determines the type of request and invokes the appropriate protocol suite to service 
it. The client stream manager uses this protocol for communicating the request to the server. 
Once it receives a response from the server in the form of a document, this information is 
passed to the presentation manager for appropriate display. The presentation manager 
consults a static view control configuration file (mimerc, mailcap, etc.) to help it map 
document types to external viewers. 
The HTTP server ensures transparent access to the file system-the source of the 
documents that the Web exists to transfer. It does this either by handling the access directly 
(for known resource types) or through a proxy known as common gateway interface (CGI). 
CGI handles resource types that a native server cannot handle and handles extension of server 
functionality, as will be discussed next. Before these extensions, the available WWW servers 
implemented a subset of defined HTTP requests, which allowed for the retrieval of 
documents, the retrieval of document meta-information, and server-side program execution 
via CGI. 
When a request is received by the server stream manager, its type is determined and 
the path of the URL is resolved via the path resolver. The HTTP server consults an access list 
to determine if the requesting client is authorized for access. It might initiate a password 
authentication session with the client to permit access to secured data. Assuming 
authentication, it accesses the file system (which is outside the server boundary) and writes 
the requested information to the output stream. If a program is to be executed, a process is 
made available (either new or polled) through CGI and the program is executed, with the 
output written by the server stream manager back to the client. 
In either case, CGI is one of the primary means by which servers provide 
extensibility, which is one of the most important requirements driving the evolution of Web 
software. CGI became such an important aspect of Web-based applications that we now 
discuss this topic at greater length. 
COMMON GATEWAY INTERFACE (CGI): 
Most information returned by a server is static, changing only when modified on its home file 
system. CGI scripts, on the other hand, allow dynamic, request-specific information to be 
returned. CGI has historically been used to augment server functionality: for input of 
information, for searches, for clickable images. The most common use of CGI, however, is to 
create virtual documents-documents that are dynamically synthesized in response to a user 
request. For example, when a user looks for something on the Internet, the search engine 
Software Architecture  
Unit5  Page 34  
creates a reply to the user's search request; a CGI script creates a new HTML document from 
the reply and returns it to the user. 
CGI scripts show the flexibility of early architectures which were based on libWWW. 
In Figure 13.5, CGI is shown as external to the HTTP server. CGI scripts are written in a 
variety of languages, some of which are compiled (C, C++, Fortran) and some of which are 
interpreted (perl, VisualBasic, AppleScript, etc.). These scripts allow a developer to extend a 
server's functionality arbitrarily and, in particular, to produce information that the server will 
return to the user. 
However, because scripts may contain any functionality written in C, perl, and so on, 
they represent an enormous security hole for the system on which they are installed. For 
example, a script (which runs as a process separate from the server) might be "tricked" into 
executing an arbitrary command on the host system on behalf of a remote user. For this 
reason, server-side scripts such as CGI have led to a new requirement for increased security. 
The use of HTTPS to address this requirement will be described in the next section. 
Probably the most important additional feature that CGI brought to the Web 
architecture is that it allows users to "put" information into the Web, in contrast to the "get" 
operation that servers normally provide. Although the requirement to put in information was 
listed in the original World Wide Web project requirements, it has not been fully achieved. 
CGI allows users to put information only in application-specific ways, such as adding it to a 
database by filling out a form. 
CGI solved many problems inherent in the original design of libWWW-principally 
because it provided much needed server extensibility to handle arbitrary resources, allowed 
users to put data in limited ways-it also had several substantial shortcomings. The security 
issue was one; another was portability. CGI scripts written in VisualBasic, AppleScript, and 
C Shell work on Windows, Macintosh, and UNIX, respectively. These scripts cannot be 
(easily) moved from one platform to another. 
ACHIEVING INITIAL QUALITY GOALS: 
Table 13.2 describes how the Web achieved its initial quality goals of remote access, 
interoperability, extensibility, and scalability. 
Table 13.2. How the WWW Achieved Its Initial Quality Goals 
Goal How Achieved Tactics Used 
Remote Access Build Web on top of Internet Adherence to defined 
protocols 
Interoperability Use libWWW to mask platform details Abstract common 
services; 
Hide information; 
Extensibility of 
Software 
Isolate protocol and data type extensions in 
libWWW; allow for plug-in components (applets 
and servlets) 
Abstract common 
services; 
Hide information; 
Software Architecture  
Unit5  Page 35  
Table 13.2. How the WWW Achieved Its Initial Quality Goals 
Goal How Achieved Tactics Used 
Replace components; 
Configuration files; 
Extensibility of 
Data 
Make each data item independent except for 
references it controls 
Limit possible 
options; 
Scalability Use client-server architecture and keep references 
to other data local to referring data location 
Introduce 
concurrency; 
Reduce 
computational 
overhead 
Achieving Quality Goals:- 
Together the elements we have described allow the Web-based e-commerce system to 
achieve its stringent quality goals of security, high availability, modifiability, scalability, and 
high performance. How they do this is shown in Table 13.3. 
Table 13.3. How the Web e-Commerce Architecture Achieves Its Quality Goals 
Goal How Achieved Tactics 
High 
Performance 
Load balancing, network address 
translation, proxy servers 
Introduce concurrency; increase 
resources; multiple copies 
High 
Availability 
Redundant processors, networks, 
databases, and software; load 
balancing 
Active redundancy; transactions; 
introduce concurrency 
Scalability Allow for horizontal and vertical 
scaling; load balancing 
Abstract common services; 
adherence to defined protocols; 
introduce concurrency 
Security Firewalls; public/private key 
encryption across public networks 
Limit access; integrity; limit 
exposure 
Modifiability Separation of browser functionality, 
database design, and business logic 
into distinct tiers 
Abstract common services; 
semantic coherence; intermediary; 
interface stability 
 
 
 
ALL THE BEST 
