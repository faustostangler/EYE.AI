---
name: Architecture Tradeoff Analysis Method Collection | CMU Software Engineering Institute
keywords: (placeholder)
metadata:
  url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Architecture Tradeoff Analysis Method Collection | CMU Software Engineering Institute
Carnegie Mellon University
Home About Research and Development Publications and Media Education Careers
Search
Mobile Menu
Home
Publications
Digital Library
Architecture Tradeoff Analysis Method Collection
Architecture Tradeoff Analysis Method Collection
February 14, 2018 • Collection
By Software Engineering Institute
This collection contains resources about the Architecture Tradeoff Analysis Method (ATAM®), a method for evaluating software architectures against quality attribute goals.
Publisher
Software Engineering Institute
Topic or Tag
Software Architecture
Abstract
The Architecture Tradeoff Analysis Method (ATAM) is a method for evaluating software architectures relative to quality attribute goals. ATAM evaluations expose architectural risks that potentially inhibit the achievement of an organization's business goals. The ATAM gets its name because it not only reveals how well an architecture satisfies particular quality goals but it also provides insight into how those quality goals interact with each other—how they trade off against each other.
The ATAM is the leading method in the area of software architecture evaluation. An evaluation using the ATAM typically takes three to four days and gathers together a trained evaluation team, architects, and representatives of the architecture's various stakeholders.
Challenges
Most complex software systems are required to be modifiable and have good performance. They may also need to be secure, interoperable, portable, and reliable. But for any particular system
What precisely do these quality attributes such as modifiability, security, performance, and reliability mean?
Can a system be analyzed to determine these desired qualities?
How soon can such an analysis occur?
How do you know if a software architecture for a system is suitable without having to build the system first?
Description
Business drivers and the software architecture are elicited from project decision-makers. These are refined into scenarios and the architectural decisions made in support of each one. Analysis of scenarios and decisions results in the identification of risks, non-risks, sensitivity points, and tradeoff points in the architecture. Risks are synthesized into a set of risk themes, showing how each one threatens a business driver.
The ATAM consists of nine steps:
Present the ATAM. The evaluation leader describes the evaluation method to the assembled participants, tries to set their expectations, and answers questions they may have.
Present business drivers. A project spokesperson (ideally the project manager or system customer) describes what business goals are motivating the development effort and hence what will be the primary architectural drivers (e.g., high availability or time to market or high security).
Present architecture. The architect will describe the architecture, focusing on how it addresses the business drivers.
Identify architectural approaches. Architectural approaches are identified by the architect but are not analyzed.
Generate quality attribute utility tree. The quality factors that comprise system "utility" (performance, availability, security, modifiability, usability, etc.) are elicited, specified down to the level of scenarios, annotated with stimuli and responses, and prioritized.
Analyze architectural approaches. Based on the high-priority factors identified in Step 5, the architectural approaches that address those factors are elicited and analyzed (for example, an architectural approach aimed at meeting performance goals will be subjected to a performance analysis). During this step, architectural risks, sensitivity points, and tradeoff points are identified.
Brainstorm and prioritize scenarios. A larger set of scenarios is elicited from the entire group of stakeholders. This set of scenarios is prioritized via a voting process involving the entire stakeholder group.
Analyze architectural approaches. This step reiterates the activities of Step 6 but uses the highly ranked scenarios from Step 7. Those scenarios are considered to be test cases to confirm the analysis performed thus far. This analysis may uncover additional architectural approaches, risks, sensitivity points, and tradeoff points, which are then documented.
Present results. Based on the information collected in the ATAM (approaches, scenarios, attribute-specific questions, the utility tree, risks, non-risks, sensitivity points, and tradeoffs), the ATAM team presents the findings to the assembled stakeholders.
The most important results are improved architectures. The output of an ATAM is an out-brief presentation and/or a written report that includes the major findings of the evaluation. These are typically:
a set of architectural approaches identified
a "utility tree"—a hierarchic model of the driving architectural requirements
the set of scenarios generated and the subset that were mapped onto the architecture
a set of quality-attribute-specific questions that were applied to the architecture, and the responses to these questions
a set of identified risks
a set of identified non-risks
a synthesis of the risks into a set of risk themes that threaten to undermine the business goals of the system
Benefits
identified risks early in the life cycle
increased communication among stakeholders
clarified quality attribute requirements
improved architecture documentation
documented basis for architectural decisions
The most important results are improved architectures. The ATAM aids in eliciting sets of quality requirements along multiple dimensions, analyzing the effects of each requirement in isolation, and then understanding the interactions of these requirements.
Who Would Benefit
Many people have a stake in a system's architecture, and all of them exert whatever influence they can on the architect(s) to make sure that their goals are addressed. For example, the users want a system that is easy to use and has rich functionality. The maintenance organization wants a system that is easy to modify. The developing organization (as represented by management) wants a system that is easy to build and that will employ the existing workforce to good advantage. The customer (who pays the bill) wants the system to be built on time and within budget. All of these stakeholders will benefit from applying the ATAM. And needless to say, the architect is also a primary beneficiary.
Collection Items
Results per page
10
25
50
100
[
Scaling Up Incremental Design Reviews
](https://www.sei.cmu.edu/library/scaling-up-incremental-design-reviews/)
May 7, 2019 • Presentation
By Felix Bachmann, Stephany Bellomo
This presentation describes an experimental incremental design review method motivated by the agile method that scales to realistic operational contexts.
Learn More
[
Integrate End to End Early and Often
](https://www.sei.cmu.edu/library/integrate-end-to-end-early-and-often/)
July 1, 2013 • Article
By Felix Bachmann, Luis Carballo, Jim McHale, Robert Nord
This article discusses using architecture-centric engineering and the Team Software Process to develop software for a new trading engine at the Mexican Stock Exchange.
Read
[
Impact of Army Architecture Evaluations
](https://www.sei.cmu.edu/library/impact-of-army-architecture-evaluations/)
March 31, 2009 • Special Report
By Robert Nord, John K. Bergey, Stephen Blanchette, Jr., Mark H. Klein
This 2009 report describes the results of a study of the impact that the ATAM evaluations and QAWs had on Army programs.
Read
[
Progress Toward an Organic Software Architecture Capability in the U.S. Army
](https://www.sei.cmu.edu/library/progress-toward-an-organic-software-architecture-capability-in-the-us-army/)
May 31, 2007 • SEI Report
By Stephen Blanchette, Jr., John K. Bergey
This 2007 report describes the Software Architecture Initiative of the Army Strategic Software Improvement Program.
Read
[
Risk Themes Discovered Through Architecture Evaluations
](https://www.sei.cmu.edu/library/risk-themes-discovered-through-architecture-evaluations/)
August 31, 2006 • SEI Report
By Len Bass, Robert Nord, William Wood, David Zubrow
Analyzes the output of 18 evaluations conducted using the Architecture Tradeoff Analysis Method in order to find patterns in the risk themes identified.
Read
[
Risk Themes from ATAM Data: Preliminary Results
](https://www.sei.cmu.edu/library/risk-themes-from-atam-data-preliminary-results/)
April 26, 2006 • Presentation
By Len Bass, Robert Nord, William Wood
Presents a preliminary analysis of the results of a collection of ATAMs.
Learn More
[
Categorizing Business Goals for Software Architectures
](https://www.sei.cmu.edu/library/categorizing-business-goals-for-software-architectures/)
November 30, 2005 • SEI Report
By Rick Kazman, Len Bass
This report provides a categorization of possible business goals for software-intensive systems, so that individuals have some guidance in the elicitation, expression, and documentation of business goals.
Read
[
Using the SEI Architecture Tradeoff Analysis Method to Evaluate WIN-T: A Case Study
](https://www.sei.cmu.edu/library/using-the-sei-architecture-tradeoff-analysis-method-to-evaluate-win-t-a-case-study/)
August 31, 2005 • Technical Note
By Paul C. Clements, John K. Bergey, Dave Mason
This report describes the application of the SEI ATAM (Architecture Tradeoff Analysis Method) to the U.S. Army's Warfighter Information Network-Tactical (WIN-T) system.
Read
[
Integrating the Architecture Tradeoff Analysis Method (ATAM) with the Cost Benefit Analysis Method (CBAM)
](https://www.sei.cmu.edu/library/integrating-the-architecture-tradeoff-analysis-method-atam-with-the-cost-benefit-analysis-method-cbam/)
November 30, 2003 • Technical Note
By Robert Nord, Mario R. Barbacci, Paul C. Clements, Rick Kazman, Mark H. Klein, Liam O'Brien, James E. Tomayko
This technical note reports on a proposal to integrate the SEI ATAM (Architecture Tradeoff Analysis Method) and the CBAM (Cost Benefit Analysis Method).
Read
[
Using the Architecture Tradeoff Analysis Method (ATAM) to Evaluate the Software Architecture for a Product Line of Avionics Systems: A Case Study
](https://www.sei.cmu.edu/library/using-the-architecture-tradeoff-analysis-method-atam-to-evaluate-the-software-architecture-for-a-product-line-of-avionics-systems-a-case-study/)
June 30, 2003 • Technical Note
By Mario R. Barbacci, Paul C. Clements, Anthony J. Lattanze, Linda M. Northrop, William Wood
This 2003 technical note describes an ATAM evaluation of the software architecture for an avionics system developed for the Technology Applications Program Office (TAPO) of the U.S. Army Special Operations …
Read
[
SEI Architecture Analysis Techniques and When to Use Them
](https://www.sei.cmu.edu/library/sei-architecture-analysis-techniques-and-when-to-use-them/)
September 30, 2002 • Technical Note
By Mario R. Barbacci
When analyzing system and software architectures, the Quality Attribute Workshop (QAW) and the Architecture Tradeoff Analysis Method (ATAM) can be used in combination to obtain early and continuous benefits.
Read
[
Use of the Architecture Tradeoff Analysis Method (ATAM) in Source Selection of Software-Intensive Systems
](https://www.sei.cmu.edu/library/use-of-the-architecture-tradeoff-analysis-method-atam-in-source-selection-of-software-intensive-systems/)
May 31, 2002 • Technical Note
By John K. Bergey, Matt Fisher, Lawrence G. Jones
This report explains the role of software architecture evaluation in a source selection and describes the contractual elements that are needed to support its use.
Read
[
Using the Architecture Tradeoff Analysis Method to Evaluate a Wargame Simulation System: A Case Study
](https://www.sei.cmu.edu/library/using-the-architecture-tradeoff-analysis-method-to-evaluate-a-wargame-simulation-system-a-case-study/)
November 30, 2001 • Technical Note
By Lawrence G. Jones, Anthony J. Lattanze
This report describes the application of the ATAM (Architecture Tradeoff Analysis Method) to a major wargaming simulation system.
Read
[
Evaluating Software Architectures: Methods and Case Studies
](https://www.sei.cmu.edu/library/evaluating-software-architectures-methods-and-case-studies/)
October 22, 2001 • Book
By Paul C. Clements, Rick Kazman, Mark H. Klein
This book is a comprehensive, step-by-step guide to software architecture evaluation, describing specific methods that can quickly and inexpensively mitigate enormous risk in software projects.
Read
[
Applicability of General Scenarios to the Architecture Tradeoff Analysis Method
](https://www.sei.cmu.edu/library/applicability-of-general-scenarios-to-the-architecture-tradeoff-analysis-method/)
September 30, 2001 • SEI Report
By Len Bass, Mark H. Klein, Gabriel Moreno
In this report, we compare the scenarios elicited from five ATAM (Architecture Tradeoff Analysis Method) evaluations with the scenarios used to characterize the quality attributes.
Read
[
Use of the ATAM in the Acquisition of Software-Intensive Systems
](https://www.sei.cmu.edu/library/use-of-the-atam-in-the-acquisition-of-software-intensive-systems/)
August 31, 2001 • Technical Note
By John K. Bergey, Matt Fisher
Discusses the role of software architecture evaluations in system acquisition, describes required contractual elements, and provides an example of contractual language.
Read
[
An Evaluation Theory Perspective of the Architecture Tradeoff Analysis Method (ATAM)
](https://www.sei.cmu.edu/library/an-evaluation-theory-perspective-of-the-architecture-tradeoff-analysis-method-atam/)
August 31, 2000 • SEI Report
By Marta Lopez
Analyzes and identifies the ATAM's evaluation process and criteria, as well as its data-gathering and synthesis techniques, and more.
Read
[
ATAM: Method for Architecture Evaluation
](https://www.sei.cmu.edu/library/atam-method-for-architecture-evaluation/)
July 31, 2000 • SEI Report
By Rick Kazman, Mark H. Klein, Paul C. Clements
This report presents technical and organizational foundations for performing architectural analysis, and presents the SEI's ATAM, a technique for analyzing software architectures.
Read
[
Using the Architecture Tradeoff Analysis Method to Evaluate a Reference Architecture: A Case Study
](https://www.sei.cmu.edu/library/using-the-architecture-tradeoff-analysis-method-to-evaluate-a-reference-architecture-a-case-study/)
May 31, 2000 • Technical Note
By Brian P. Gallagher
This report describes the application of the ATAM (Architecture Tradeoff Analysis Method) to evaluate a reference architecture for ground-based command and control systems.
Read
[
Software Architecture Evaluation with ATAM in the DoD System Acquisition Context
](https://www.sei.cmu.edu/library/software-architecture-evaluation-with-atam-in-the-dod-system-acquisition-context/)
August 31, 1999 • Technical Note
By John K. Bergey, Matt Fisher, Lawrence G. Jones, Rick Kazman
This report explains the basics of software architecture and software architecture evaluation in a system acquisition context.
Read
[
The Architecture Tradeoff Analysis Method
](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/)
June 30, 1998 • SEI Report
By Rick Kazman, Mark H. Klein, Mario R. Barbacci, Thomas A. Longstaff, Howard F. Lipson, Jeromy Carriere
This paper presents the Architecture Tradeoff Analysis Method (ATAM), a structured technique for understanding the tradeoffs inherent in the architectures of software-intensive systems.
Read
[
Steps in an Architecture Tradeoff Analysis Method: Quality Attribute Models and Analysis
](https://www.sei.cmu.edu/library/steps-in-an-architecture-tradeoff-analysis-method-quality-attribute-models-and-analysis/)
April 30, 1998 • SEI Report
By Mario R. Barbacci, Peter H. Feiler, Mark H. Klein, Howard F. Lipson, Thomas A. Longstaff, Charles Weinstock, Jeromy Carriere
This paper presents some of the steps in an emerging architecture tradeoff analysis method (ATAM).
Read
[
The Architecture Tradeoff Analysis Method
](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method-2/)
April 1, 1998 • White Paper
By Rick Kazman, Mark H. Klein, Mario R. Barbacci, Thomas A. Longstaff, Howard F. Lipson, Jeromy Carriere
This paper presents the Architecture Tradeoff Analysis Method (ATAM), a structured technique for understanding the tradeoffs inherent in design.
Read
No results available for the selected filters.
SHARE
Ask a question about this Collection
Report a Vulnerability to CERT/CC
Subscribe to SEI Bulletin
Request Permission to Use SEI Materials
Advancing Software for National Security
Sponsored by the Department of War, the SEI is a federally funded research and development center managed by Carnegie Mellon University.
Main Office
4500 Fifth Avenue
Pittsburgh, PA 15213-2612
412-268-5800 [-]
SEI
About Research and Development Publications and Media Education Careers [-]
Helpful links
Digital Library Blog Podcasts [-]
Connect
Facebook LinkedIn X YouTube
2026 Carnegie Mellon University
Contact Us
Office Locations
Privacy Notice
Legal
www.cmu.edu
2026 Carnegie Mellon University 
Opt-Out Request Honored
Cookie Settings
When you visit our website, we store cookies on your browser to collect information. The information collected might relate to you, your preferences or your device, and is mostly used to make the site work as you expect it to and to provide a more personalized web experience. However, you can choose not to allow certain types of cookies, which may impact your experience of the site and the services we are able to offer. Click on the different category headings to find out more and change our default settings according to your preference. You cannot opt-out of our First Party Strictly Necessary Cookies as they are deployed in order to ensure the proper functioning of our website (such as prompting the cookie banner and remembering your settings, to log into your account, to redirect you when you log out, etc.). For more information about the First and Third Party Cookies used please follow this link.
More information
Allow All
Manage Consent Preferences
Strictly Necessary Cookies
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
Performance Cookies
[x]
Performance Cookies Active
These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.
Targeting Cookies
[x]
Targeting Cookies Active
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Cookie List
Clear
[-] checkbox label label
Apply Cancel
Consent Leg.Interest [-]
checkbox label label [-]
checkbox label label [-]
checkbox label label
Reject All Confirm My Choices
