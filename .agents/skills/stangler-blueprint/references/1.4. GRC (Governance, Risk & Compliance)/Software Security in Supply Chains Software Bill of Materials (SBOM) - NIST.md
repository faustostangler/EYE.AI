---
name: Software Security in Supply Chains: Software Bill of Materials (SBOM) - NIST
keywords: (placeholder)
metadata:
  url: https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity/software-security-supply-chains-software-1
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T19:00:57.430Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
Software Security in Supply Chains: Software Bill of Materials (SBOM) | NIST
Skip to main content 
An official website of the United States government
Here's how you know
Here's how you know 
Official websites use .gov
A .gov website belongs to an official government organization in the United States. 
Secure .gov websites use HTTPS
A lock ( A locked padlock ) or https:// means you've safely connected to the .gov website. Share sensitive information only on official, secure websites.
https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity/software-security-supply-chains-software-1 
Search NIST 
Menu
Close
Publications
What We Do
All Topics
Advanced communications
Artificial intelligence
Bioscience
Buildings and construction
Chemistry
Cybersecurity and Privacy
Electronics
Energy
Environment
Fire
Forensic science
Health
Information technology
Infrastructure
Manufacturing
Materials
Mathematics and statistics
Metrology
Nanotechnology
Neutron research
Performance excellence
Physics
Public safety
Quantum information science
Resilience
Standards
Transportation
Labs & Major Programs
Assoc Director of Laboratory Programs
Laboratories
Communications Technology Laboratory
Engineering Laboratory
Information Technology Laboratory
Material Measurement Laboratory
Physical Measurement Laboratory
User Facilities
NIST Center for Neutron Research
CNST NanoFab
Research Test Beds
Research Projects
Tools & Instruments
Major Programs
Baldrige Performance Excellence Program
CHIPS for America Initiative
Manufacturing Extension Partnership (MEP)
Office of Advanced Manufacturing
Special Programs Office
Technology Partnerships Office
Services & Resources
Measurements and Standards
Calibration Services
Laboratory Accreditation (NVLAP)
Quality System
Standard Reference Materials (SRMs)
Standard Reference Instruments (SRIs)
Standards.gov
Time Services
Office of Weights and Measures
Software
Data
Chemistry WebBook
National Vulnerability Database
Physical Reference Data
Standard Reference Data (SRD)
Storefront
License & Patents
Computer Security Resource Center (CSRC)
NIST Research Library
News & Events
News
Events
Blogs
NIST In Focus
Feature Stories
Awards
Video Gallery
Image Gallery
Media Contacts
About NIST
About Us
Leadership
Organization Structure
Budget & Planning
Contact Us
Visit
Careers
Student programs
Work with NIST
History
NIST Digital Archives
NIST Museum
NIST and the Nobel
Educational Resources
Information Technology Laboratory
Executive Order 14028, Improving the Nation's Cybersecurity
Software Supply Chain Security Guidance Expand or Collapse
Software Security in Supply Chains Expand or Collapse
Guidance, Purpose, Scope, and Audience
EO-Critical Software and Security Measures for EO-Critical Software
Software Cybersecurity for Producers and Users Expand or Collapse
Attesting to Conformity with Secure Software Development Practices
Software Verification
Evolving Standards, Tools, and Recommended Practices Expand or Collapse
Software Bill of Materials (SBOM)
Enhanced Vendor Risk Assessments
Open Source Software Controls
Vulnerability Management
Additional Existing Industry Standards, Tools, and Recommended Practices
FAQs
Software Cybersecurity for Producers and Purchasers
Critical Software Expand or Collapse
Critical Software Definition Expand or Collapse
Introduction
Background & Approach
Definition & Explanatory Material
FAQs
Security Measures for Critical Software Use Expand or Collapse
Introduction
Purpose & Scope
Security Measures for EO-Critical Software Use
FAQs
Software Verification Expand or Collapse
Introduction
Background & Approach
Recommended Minimum Standard for Vendor or Developer Verification of Code
FAQs
Cybersecurity Labeling for Consumers Expand or Collapse
Consumer Cybersecurity Labeling Pilots: The Approach and Contributions
Workshops on Cybersecurity Labeling of Consumer Products
IoT Product Criteria
Consumer Software Criteria
News & Updates
Engage
Resources
FAQs
Workshops & Call for Papers
News & Updates
Engage
Fact Sheet
Resources
FAQs
Cybersecurity @ NIST
Software Security in Supply Chains: Software Bill of Materials (SBOM)
Share 
Facebook
Linkedin
X.com
[Email](mailto:?subject=NIST.gov&body=Check out this site https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity/software-security-supply-chains-software-1)
Section 10(j) of EO 14028 defines an SBOM as a “formal record containing the details and supply chain relationships of various components used in building software,”
 [1] similar to food ingredient labels on packaging. SBOMs offer increased transparency, provenance, and speed at which vulnerabilities
 [2] can be identified and remediated by federal departments and agencies. SBOMs can also indicate a developer or supplier's application of secure software development practices across the SDLC. Figure 2 illustrates an example of how an SBOM may be assembled across the SDLC.
Download | Image info
Figure 2 - Illustrative Example of Software Life Cycle and Bill of Materials Assembly Line
When applicable to a procurement action, federal agencies should require their suppliers of software products and services to provide access to machine-readable SBOMs in conformance with the EO and NTIA's The Minimum Elements For a Software Bill of Materials (SBOM) by containing:
Data fields: Documenting baseline information about each component that should be tracked
Automation support: Allowing for scaling across the software ecosystem through automatic generation and machine readability
Practices and processes: Defining the operations of SBOM requests, generation, and use
NTIA's guidance acknowledges that SBOM capabilities are currently nascent for federal acquirers and that the minimum elements are only the first key step in a process that will mature over time. As SBOMs mature, agencies should ensure that they do not deprioritize existing C-SCRM capabilities (e.g., vulnerability management practices, vendor risk assessments). SBOMs are meant to complement those capabilities rather than replace them. Federal acquirers that are unable to appropriately ingest, analyze, and act on the data that SBOMs provide will likely not improve their overall C-SCRM posture.
Federal acquirers should further consider that effectively implemented SBOMs are still subject to operational constraints. For example, SBOMs that are retroactively generated may not be able to produce the same list of dependencies used at build time. Federal acquirers should continue using the risk-based approaches outlined in SP 800-161r1 and SP 800-218 to guide their implementation of SBOMs over this period of rapid transition.
In this context, federal agencies should evaluate whether and to what extent software providers can satisfy the following recommended SBOM capabilities.
Foundational SBOM Capabilities 
Ensure that SBOMs received from third-party suppliers conform to industry standard formats to enable the automated ingestion and monitoring of versions. According to the NTIA, acceptable standard formats currently include SPDX , CycloneDX , and SWID.
Confirm that SBOMs received from third-party suppliers meet the NTIA's Recommended Minimum Elements, including a catalog of the supplier's integration of open-source software components.
Catalog SBOMs for all classes of software across the acquiring entities' enterprise — including purchased software, open-source software, and in-house software — by requiring sub-tier software suppliers to produce, maintain, and provide SBOMs whenever practical.
Require software producers to maintain readily accessible and digitally signed SBOM repositories and to share SBOMs with software purchasers directly or by publishing them on a public website.
Sustaining Capabilities 
Contextualize SBOMs received from third-party suppliers with additional data elements (e.g., plug-ins, hardware components, organizational controls, and other community-provided components  [3]) that inform the risk posture of the acquiring entity.
Confirm that SBOMs received from third-party suppliers detail the supplier's integration of commercial software components.
Integrate vulnerability detection capabilities with the acquiring entity's SBOM repositories to enable automated alerting for applicable cybersecurity risks throughout the supply chain.  [4]
Enhancing Capabilities 
Ensure that third-party suppliers continuously enrich SBOM data with a VAR.
Acquiring entities should develop risk management and measurement capabilities to dynamically monitor the impacts of SBOM-related VARs. Acquiring organizations should align with asset inventories for further risk exposure and criticality calculations.[5]
Perform binary decomposition of software installation packages to generate SBOMs if no vendor-supplied SBOM is available (e.g., legacy software), when technically and legally feasible.  [6]
[1] Executive Office of the President. (2021). Executive Order 14028 on Improving the Nation's Cybersecurity. https://www.federalregister.gov/d/2021-10460
[2] References to vulnerabilities are inclusive of Common Weakness Enumerations (CWE) found pre-release and Common Vulnerabilities and Exposures (CVE) found post-release, as outlined in IR 8011 .
[3] GitLab. (2021). NIST Position Paper #2.
[4] Vigilant Ops. (2021). Section 4 Enhancing Software Supply Chain Security - Areas 4 and 5.
[5] Synopsys. (2021). Guidelines for software integrity chains and provenance.
[6] National Telecommunications and Information Administration. (2021). The Minimum Elements For a Software Bill of Materials (SBOM). https://www.ntia.doc.gov/files/ntia/publications/sbom_minimum_elements_report.pdf
Content:
Introduction
Guidance, Purpose, Scope, and Audience
EO-Critical Software and Security Measures for EO-Critical Software
Software Cybersecurity for Producers and Users
Attesting to Conformity with Secure Software Development Practices
Software Verification
Evolving Standards, Tools, and Recommended Practices
Software Bill of Materials (SBOM)
Enhanced Vendor Risk Assessments
Open Source Software Controls
Vulnerability Management
Additional Existing Industry Standards, Tools, and Recommended Practices
Frequently Asked Questions (FAQs)
Information technology and Cybersecurity and privacy
Created May 3, 2022, Updated November 1, 2024
Was this page helpful?
HEADQUARTERS
100 Bureau Drive
Gaithersburg, MD 20899
301-975-2000
Webmaster | Contact Us | Our Other Offices
X.com Facebook LinkedIn Instagram YouTube Giphy RSS Feed Mailing List
How are we doing? Feedback
Site Privacy
Accessibility
Privacy Program
Copyright & Disclaimers
Vulnerability Disclosure
No Fear Act Policy
FOIA
Environmental Policy
Scientific Integrity
Information Quality Standards
Commerce.gov
Science.gov
USA.gov
Vote.gov
Back to top
