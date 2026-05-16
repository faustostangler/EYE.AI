---
name: WHY USE LINDDUN
keywords: (placeholder)
metadata:
  url: https://linddun.org/linddun/whyuselinddun/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T19:00:57.430Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
WHY USE LINDDUN | linddun.org
LINDDUN
WHY USE LINDDUN
PUBLICATIONS
WHAT OTHERS SAY
PRIVACY THREATS
PRIVACY THREATS
THREAT TYPES
THREAT TREES
EXAMPLES & CASES
LINDDUN METHODS
LINDDUN METHODS
LINDDUN PRO
LINDDUN PRO
PRO – INSTRUCTIONS
LINDDUN GO
LINDDUN GO
GO – INSTRUCTIONS
NEWS
JOBS
CONTACT
Select Page
LINDDUN
WHY USE LINDDUN
PUBLICATIONS
WHAT OTHERS SAY
PRIVACY THREATS
PRIVACY THREATS
THREAT TYPES
THREAT TREES
EXAMPLES & CASES
LINDDUN METHODS
LINDDUN METHODS
LINDDUN PRO
LINDDUN PRO
PRO – INSTRUCTIONS
LINDDUN GO
LINDDUN GO
GO – INSTRUCTIONS
NEWS
JOBS
CONTACT
why use linddun?
s
Supports a rich set of privacy threats
The LINDDUN framework provides a rich catalog of privacy threat types to investigate a wide range of complex privacy design issues. Together, the types Linking, Identifying, Non-repudiation, Detecting, Data Disclosure, Unawareness, and Non-compliance form the acronym LINDDUN.
Privacy is not the same as confidentiality. While confidentiality is about protecting data against unauthorized access, privacy is about protecting the rights of individuals to control how their personal information is collected, processed and shared. The privacy-specific protection goals 'unlinkability' (ensure that personal data items cannot be linked across domains), 'intervenability' (give individuals control over the processing of their personal data) and 'transparency' (inform individuals about the processing of their personal data), complement the traditional security goals, confidentiality, integrity and availability.
LINDDUN's rich privacy threat knowledge will help you understand and identify complex privacy design flaws in your software architecture.

A practical method
LINDDUN offers a systematic but practical approach to help you assess the privacy posture of your software system. Its outcome reflects how mature your system is regarding privacy concerns, exposes the remaining privacy flaws, and suggests privacy enhancing techniques and countermeasures. The strength of the LINDDUN privacy engineering framework resides in the combination of the systematic guidance and the privacy knowledge support. Its model-based approach guides you on which privacy issues to investigate, and on where in the system model they may emerge. To do this, it uses a catalog of privacy threat types that provide insight into complex privacy risks. Further knowledge support comes in the form of mapping tables (mapping threat types onto system components), threat trees (providing a detailed breakdown of privacy threat knowledge), a taxonomy of mitigation strategies and a classification of privacy enhancing solutions.
To serve different needs, LINDDUN comes in multiple flavors: Go, Pro, Maestro.

Compatible with STRIDE
Teams already familiar with security threat modeling approaches such as STRIDE, will find it easy to adopt LINDDUN, as it follows the same principles. As privacy and security threat modeling have much in common and start from the same system model, you can perform both approaches in parallel.
The Threat Modeling Manifesto describes the main values and principles of threat modeling. When we threat model, we ask 4 questions. LINDDUN adopts the same approach.
What are we building? As a starting point, you need a model of the system. F or LINDDUN this can be a Data Flow Diagram or an informal sketch.
What can go wrong? You go over each of the system components and interactions to look for potential issues. LINDDUN's privacy threat types will drive the analysis. The outcome will pinpoint to privacy design issues.
What are we going to do about it? LINDDUN's catalog of privacy mitigation strategies and privacy enhancing technologies (PETs) will guide you.
Did we do a decent job*?*
Similarities and differences between security and privacy threat modeling approaches: 

Supports privacy threat mitigation
After identifying privacy flaws in your software system, you need to remediate them. The LINDDUN framework therefore offers support in the form of mitigation strategies and a catalog of privacy enhancing technologies (PETs). In short, for each privacy threat, LINDDUN offers a suitable mitigation strategy, and links this to a technical solution.
As the range of PETs is huge, it is not easy to make an educated decision about which solution is best suited for your privacy concern. LINDDUN provides guidance by taking a step back. Rather than getting lost in the multitude of existing solutions, you should first think about the general approach (strategy) you will apply to your system.
For instance, if the threat analysis indicates that a certain dataset needs to be minimized, first determine if you can do that proactively (before collecting it) or at storage time. Next, determine the minimization strategy that is most suited: Can you remove certain data attributes because you don't actually need them? Maybe it is sufficient to only collect or store a generalized view of the aggregated dataset? Etc. Once the most suitable mitigation strategy is determined, the search for corresponding privacy solutions is more focused.
To aid this process, LINDDUN provides an overview of mitigation strategies, which capture a high-level view of common techniques used to prevent privacy threats. These are mapped to the corresponding LINDDUN threat types they mitigate. The LINDDUN framework also provides an initial PETs table consisting of a collection of academic PETs, classified according to the LINDDUN mitigation strategies to get you started on your quest for the best PET for your privacy problem.

Investigates the privacy posture of YOUR system
What is great about LINDDUN is that you can apply it to an actual software system to cover relevant privacy design flaws. Following the privacy-by-design principle, the method allows you to investigate your system architecture for privacy issues during the early development phase and to proactively build privacy enhancing techniques and measures into the system. LINDDUN's approach thus enables you to tackle these privacy issues proactively, to analyze them systematically, to integrate this process into your development lifecycle, and to document your findings and solutions. Unlike other more generic privacy assessment procedures, which often follow a 'checkbox compliance approach', LINDDUN's knowledge support aims to trigger discussion and inspire out-of-the-box thinking.
In addition to software systems under development, existing software systems can benefit from LINDDUN privacy threat modeling.

Aligns with GDPR
The General Data Protection Regulation (GDPR) imposes a data protection by design and by default approach. When processing personal data, organizations must take technical and organizational measures that safeguard privacy and data protection principles. This approach is risk-based and requires accountability.
In software development, a privacy assessment is a great way to evaluate the impact on privacy and to identify privacy threats. LINDDUN provides a systematic methodology to do this. It complements the purely legal analysis by zooming in on privacy threats in the system's architecture from a technical angle. Analysts will systematically investigate each part of their system architecture to look for privacy threats. The assessment will pinpoint to any design and implementation issues that require countermeasures. LINDDUN offers support in the form of mapping tables, threat tree catalogs, a taxonomy for mitigation strategies, and classification of PETs.
From a legal perspective, LINDDUN also helps meeting the accountability requirements. During the assessment you will document the identified privacy threats and ensuing countermeasures, as well as the threat analysis process itself. This documentation will be invaluable to demonstrate that you have adopted a holistic approach to identify privacy threats during your system development.
As LINDDUN focuses on privacy threats, it is only complementary to security engineering approaches and further legal and organizational measures to attain full GDPR compliance.
Two LINDDUN privacy threat types closely align with GDPR: unawareness and unintervenability (threats against data subject rights) and non-compliance (violations against data protection principles). The remaining types target more technical privacy threats and as such contribute more directly to the selection of “appropriate technical and organizational protection measures”.

LINDDUN comes in multiple flavors
To serve different needs, LINDDUN comes in various flavors: approaches that vary in complexity and comprehensiveness – ranging from lean to in-depth analysis. Which method is the best fit depends on your needs and requirements.
LINDDUN GO takes on a lean, cross-team approach in finding privacy issues. GO comes in the form of a card deck representing the most common privacy threats, already mapped onto their most impactful system hotspots. These self-contained cards will guide you through the privacy assessment. Best performed in a structured brainstorming setting with a diverse team of privacy enthusiasts.
LINDDUN PRO takes on a systematic and exhaustive approach in finding privacy issues. Starting point is a DFD system abstraction, where you focus on all interactions between DFD elements and investigate potential privacy threats. Available knowledge support: privacy threat types, privacy threat trees, mapping table. PRO allows you to leverage tooling to automate your analysis activities.
LINDDUN MAESTRO takes on a systematic and exhaustive approach in finding privacy issues by leveraging an enriched system description to enable more precise threat elicitation. Starting point is a threat-specific system abstraction, to support the advanced analysis for threats of that particular type.
w
Acknowledged threat modeling approach
The LINDDUN privacy threat methodology was first published by KU Leuven in 2010 and has meanwhile gained significant importance. It has been acknowledged by various authorities:
ENISA, the European Union Agency for Network and Information Security
ISO 27550 on Privacy engineering for system life cycle processes
EDPS, the European Data Protection Supervisor
NIST, the National Institute of Standards and Technology
Adam Shostack in “Threat Modeling. Designing for Security.”
Izar Tarandach and Matthew J. Coles in “Threat Modeling – A Practical Guide for Development Teams”.
LINDDUN has been used as a research instrument in various European research projects (e.g. PDP4E, PRIPARE) and has been applied, evaluated, and extended by several academic researchers in a diverse range of domains.
The LINDDUN method was successfully applied in a business context by companies and organizations in the automotive industry, healthcare, government, …
According to a recent study (2022), the LINDDUN methodology is among the two best known in the industry by the IT practitioners in the requirements area, and among the ten most used in the literature. 
LINDDUN is created by DistriNet Research Unit, KU Leuven.
CONTACT US
Copyright © 2026 DistriNet, KU Leuven
