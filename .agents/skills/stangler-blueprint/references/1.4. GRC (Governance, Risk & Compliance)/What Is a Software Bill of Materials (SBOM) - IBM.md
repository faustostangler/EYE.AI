---
name: What Is a Software Bill of Materials (SBOM)? - IBM
keywords: (placeholder)
metadata:
  url: https://www.ibm.com/think/topics/sbom
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T19:00:57.430Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
What Is a Software Bill of Materials (SBOM)? | IBM
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
Tags
DevOps IT automation Security IT infrastructure
What is a software bill of materials (SBOM)?
What is a software bill of materials (SBOM)?
What does an SBOM contain?
How SBOMs work
SBOM formats
SCA vs SBOM: What's the difference?
SBOM use cases
SBOM implementation challenges and solutions
Industry trends shaping the future of SBOMs
Authors
Tasmiha Khan
Writer 
Michael Goodwin
Staff Editor, Automation & ITOps
IBM Think
What is a software bill of materials (SBOM)?
A software bill of materials (SBOM) lists all components, libraries and modules in a software product in a machine-readable format. This inventory helps organizations track software elements, identify vulnerabilities and mitigate security risks across the supply chain.
Software development teams started using SBOMs over a decade ago to manage open-source libraries and third-party repositories. Cybersecurity concerns moved SBOMs to center stage after major supply chain attacks exposed critical weaknesses. The 2020 SolarWinds breach saw attackers insert malicious code into trusted software updates, affecting 18,000 organizations including multiple government agencies. Shortly after, the 2021 Log4j vulnerability was exposed, affecting hundreds of millions of devices globally and further revealing how compromised components might threaten entire systems.
These cyber attacks highlighted a stark reality: organizations, including federal government agencies, lacked visibility into the components and dependencies within their software systems. This lack of visibility makes it difficult to assess cybersecurity risks and respond to threats effectively. The urgency of the threat spurred decisive action from the White House. Executive Order 14028 mandated SBOMs for all federal software procurement in May 2021.
The National Telecommunications and Information Administration (NTIA) established the minimum elements for SBOMs that software vendors must follow when selling to government entities. In September 2024, CISA published a document titled " Framing Software Component Transparency," expanding upon these minimum requirements and providing more detailed guidance on SBOM implementation and management across the software ecosystem.
This federal directive now serves as a model for software transparency across industries. For instance, in the financial services industry, the Payment Card Industry Data Security Standard (PCI DSS) version 4.0 includes requirements for software inventory management to protect payment systems and address vulnerabilities. In healthcare, the FDA requires SBOMs for medical devices, while the International Medical Device Regulators Forum (IMDRF) recommends their use to safeguard medical devices and patient data systems.
These industry guidelines and recommendations reflect a broader shift toward SBOM adoption across the private sector. Gartner predicts that by 2025, 60% of organizations building or procuring critical infrastructure software will mandate SBOMs, up from less than 20% in 2022. This adoption is driven by necessity—recent analysis shows that over 90% of modern software applications contains open-source dependencies , with 74% containing high-risk dependencies. Organizations are increasingly using SBOMs to meet compliance requirements, validate third-party components and address security vulnerabilities as they're discovered. 
The latest AI News + Insights
Discover expertly curated insights and news on AI, cloud and more in the weekly Think Newsletter.
Subscribe today
What does an SBOM contain?
Like food labels that detail ingredients and their sources, SBOMs provide structured documentation of software components, their suppliers and the relationships between dependencies.
SBOM requirements have evolved significantly since their introduction in Executive Order 14028 (2021). What began as minimum requirements from NTIA has expanded through industry adoption and regulatory refinement. The current framework, published by CISA in September 2024, builds upon these foundations with enhanced guidance for broader implementation.
Organizations face different SBOM requirements depending on their sector and relationships with the federal government. U.S. government contractors, critical infrastructure providers and organizations in regulated sectors must comply with specific SBOM requirements. While the federal government mandates SBOM adoption for its suppliers, private sector organizations outside government contracts have voluntary adoption, though implementing SBOM practices has become increasingly important for supply chain security and customer trust.
SBOM attribute maturity levels
CISA's 2024 framework introduces a three-tiered maturity model that helps organizations progressively enhance their SBOM practices:
Minimum expected: Essential elements required for basic SBOM functionality and compliance
Recommended practice: Enhanced documentation that supports broader security and compliance use cases
Aspirational goal: Advanced features that enable comprehensive supply chain visibility
Baseline SBOM attributes
The following attributes represent the essential elements required in a complete SBOM:
SBOM meta-information: Core data of the SBOM document itself, including author of the SBOM data, timestamp of its creation and the primary component being documented
Supplier name: The entity that creates, defines and manufactures the software component
Component name: The designated name of software component, assigned by the original supplier
Version of component: Captures version-specific changes to accurately track updates and modifications
Other unique identifiers: Includes reference types such as Common Platform Enumeration (CPE), SWID tags, or Package URLs (PURL) for precise component tracking
Cryptographic hash: A unique fingerprint for each software component that enables verification of integrity and precise identification
Dependency relationship: A structured map showing how components are interconnected, covering both direct and transitive dependencies
License information: Documentation of legal terms for supplied software components
Copyright notice: Entity holding exclusive and legal rights to the listed components
Dependency relationships
Software dependencies create complex interconnections within modern applications. An SBOM must capture these relationships clearly, distinguishing between direct dependencies (components explicitly included in the software) and transitive dependencies (components pulled in by other dependencies).
When documenting dependencies, organizations should explicitly indicate the completeness of their knowledge. The default assumption is that dependency information might be incomplete unless explicitly marked otherwise. This transparency helps downstream users understand potential blind spots in their software supply chain.
Organizations must also account for dynamic dependencies loaded at runtime and remote dependencies called from external services. While these might not be part of the traditional software build, understanding these relationships is crucial for comprehensive security assessment.
Handling unknown information
In real-world implementations, complete knowledge of all software components isn't always possible. Organizations must handle these gaps transparently by explicitly documenting unknown dependencies and incomplete information. When certain components can't be fully documented due to contractual obligations or other constraints, the SBOM should indicate these redactions while preserving the overall dependency structure.
Rather than omitting uncertain information, organizations should explicitly mark these areas as unknown or incomplete. This approach helps downstream users make informed decisions about risk management and further investigation needs. For redacted components, organizations should maintain both complete internal SBOMs and appropriately redacted versions for external sharing.
AI Academy 
Become an AI expert
Gain the knowledge to prioritize AI investments that drive business growth. Get started with our free AI Academy today and lead the future of AI in your organization. 
Watch the series
How SBOMs work
The process of creating and maintaining SBOMs involves multiple stakeholders throughout the software development lifecycle (SDLC). Organizations should generate SBOMs for both proprietary and open source software (OSS) components. Software vendors and developers are primarily responsible for generating initial SBOMs early in the development process. These SBOMs capture a comprehensive view of the entire codebase's components. Software purchasers play a key role in validating and maintaining these documents for their deployed applications.
Integration with development workflows
Software development teams integrate SBOM generation directly into their continuous integration and continuous delivery (CI/CD) pipelines. During the build process, automated scanning tools analyze source code to inventory all components, capturing both direct and transitive dependencies. These tools generate standardized SBOM files in formats like SPDX and CycloneDX. (SWID tags are less prominent, but still valid, option.) They document each component's metadata, version information and licensing details.
Version control and continuous update processes
Version control systems maintain historical records of SBOM changes, tracking how software composition evolves over time. Organizations can track version changes and security patches within software components for each release, which is vital for managing vulnerabilities and handling security incidents.
Development teams typically configure their pipelines to trigger SBOM updates based on specific events: when new dependencies are added, when existing components are updated or when security patches are applied. This continuous update process maintains alignment between the software's actual composition and its documentation.
Quality control checkpoints
Quality control checkpoints throughout the development pipeline validate SBOM completeness and accuracy. These validation steps verify that each SBOM meets required standards and contains all necessary component information before software release. Automated validation reduces documentation gaps and improves consistency across releases.
Automation tools and capabilities
The tooling ecosystem supporting SBOM creation continues to expand. SBOM generators form the foundation, automatically scanning source code to identify components and their relationships. Validation tools then verify the generated SBOMs against established standards and specifications, flagging missing or incorrect information. Successful SBOM automation relies on established best practices: standardizing formats across teams, implementing consistent naming conventions, maintaining clear documentation of automation rules and establishing feedback loops for continuous improvement.
Management platforms build upon these capabilities, offering features for SBOM storage, analysis and distribution across organizations. Advanced platforms go further by integrating SBOM data into broader risk and compliance workflows.
For example, automation tools can map vulnerabilities to specific software components, prioritize remediation efforts based on severity and track changes over time to identify newly introduced risks. By consolidating data and providing real-time insights, these tools empower development, security and compliance teams to collaborate effectively.
SBOM formats
Selecting the right SBOM format is crucial for effective implementation. SBOMs must support automated generation and machine-readability to scale across software ecosystems. The automation of SBOM processes eliminates manual input errors during creation and enables seamless integration with security and development tools.
There are several standardized formats used to enable automated generation, validation and consumption of SBOM data while supporting integration with existing security and development tools. Organizations should implement automated SBOM generation within their CI/CD pipelines to make sure that documentation stays current with software changes.
The current CISA framework primarily recognizes two formats: SPDX and CycloneDX. Each approaches software component documentation differently, offering varying levels of detail and focusing on specific use cases within the software development lifecycle.
SPDX
Software Package Data Exchange (SPDX) was developed by the Linux Foundation and has gained widespread adoption across the open source ecosystem and commercial software vendors. The format supports cryptographic package verification and offers multiple machine-readable format options including JSON, RDF, XML and YAML. Its rich metadata support enables detailed security and provenance tracking throughout the software supply chain.
SPDX excels in open source compliance scenarios, providing detailed license information and helping organizations manage their open source component usage effectively. Major software vendors and cloud service providers have adopted SPDX for its robust specification and broad ecosystem support.
CycloneDX
CycloneDX, developed by the OWASP Foundation, is designed specifically for application security and software supply chain risk management. It provides essential features for vulnerability management, component tracking and supply chain security, with strong emphasis on VEX integration and container analysis support.
The format's security-focused elements make it especially suitable for organizations implementing comprehensive software supply chain security programs. Its native support for security use cases has driven adoption among security teams and vulnerability management workflows.
SWID tags
Software Identification (SWID) tags provide a standardized mechanism for software identification and management. The format supports comprehensive software asset tracking with features for lifecycle management, patch tracking and inventory control in enterprise environments. Notably, SWID tags are no longer listed as a supported format in the 2024 guidance for mapping of attributes, but they remain a valid option as a unique identifier within SBOMs.
SCA vs SBOM: What's the difference?
Software composition analysis (SCA) is an active cybersecurity process (with associated tools) that scans code for vulnerabilities, while a software bill of materials (SBOM) provides a standardized inventory of all software components in a product. Though both support software supply chain security, they serve distinct purposes in modern development environments.
While both tools focus on software components, SCA tools actively scan and analyze code during development, focusing primarily on open source components and third-party dependencies. These tools provide real-time insights for vulnerability detection, license compliance and security policy enforcement.
SBOM functions as a standardized inventory document that captures all software components, including proprietary code. SBOMs provide transparency into software composition through structured formats like SPDX and CycloneDX, but don't inherently include analytical capabilities. While SCA tools typically support internal security practices, SBOMs are increasingly mandated by regulations and industry standards.
Organizations typically implement both solutions together, using SCA tools to actively monitor security during development while maintaining SBOMs for compliance requirements and supply chain visibility. SCA tools often generate and validate SBOMs automatically, while SBOM documentation helps inform scanning policies.
SBOM use cases
The complexity of modern software supply chains has made SBOM adoption essential for comprehensive risk management and security assurance. Organizations increasingly use automated platforms that can consolidate SBOM data with other security and compliance information for more effective decision-making.
Security applications
Security teams integrate SBOM data into their broader application risk management strategies through automated platforms that enable real-time vulnerability detection and response. When new Common Vulnerabilities and Exposures (CVEs) emerge, these platforms can instantly map them to affected components across the entire software portfolio using SBOM inventories. This helps organizations support secure software practices.
This integration enables AI-driven insights for risk prioritization, helping teams address the most critical CVEs first. During incident response, the detailed component data from SBOMs provides crucial intelligence about potentially compromised components. This enables targeted remediation efforts and more accurate risk assessments.
Vulnerability management and VEX integration
SBOMs play an important role in vulnerability management by providing a comprehensive inventory of software components and enabling rapid identification of affected systems when new vulnerabilities are discovered.
However, not all vulnerabilities pose equal risk and determining exploitability can be challenging. This is where the Vulnerability Exploitability eXchange (VEX) comes in. VEX is a security framework that strengthens SBOM utility by providing essential context about known vulnerabilities. While an SBOM identifies all components within a software product, it doesn't indicate whether discovered vulnerabilities are exploitable. VEX bridges this gap by clarifying the real-world impact of vulnerabilities.
VEX informs Product Security Incident Response Teams (PSIRTs) and security teams about whether specific vulnerabilities affect their software environments. Using the Common Security Advisory Framework (CSAF), VEX delivers machine-readable status updates on vulnerability impact. With this information, security teams can make faster and more informed decisions.
By integrating VEX data with SBOMs, organizations can reduce false positives, prioritize actual risks and streamline vulnerability management workflows. This combined approach marks a significant advancement in automated security risk assessment and targeted remediation.
Compliance requirements
As regulatory requirements evolve, organizations need sophisticated compliance management capabilities that can handle complex SBOM requirements. SBOMs act as a form of attestation, providing verifiable documentation that software components adhere to standards like NIST guidelines and Executive Order 14028. By offering transparent records of software composition and security, SBOMs simplify audits and demonstrate regulatory alignment across industries.
Federal agencies and regulated industries must demonstrate compliance with various frameworks, including NIST guidelines and Executive Order 14028. Advanced compliance platforms can automatically verify that software components meet security standards, track compliance status across multiple frameworks and provide real-time alerts when components deviate from requirements. These capabilities can help organizations maintain continuous compliance while reducing manual oversight.
Cloud SBOM considerations
Cloud-native and containerized environments pose unique challenges for SBOM management. The dynamic nature of these environments requires specialized approaches to handle complex microservice s architectures, frequently changing container images and deployments that span multiple cloud providers and platforms.
Organizations address these challenges through specialized SBOM tools that integrate directly with container orchestration platforms. These solutions enable real-time SBOM generation as container images are built and deployed, while providing unified visibility across hybrid cloud environments.
By automating component tracking and integrating with existing cloud security tools, organizations can maintain accurate software component inventories and respond quickly to security threats across their entire cloud infrastructure. This capability applies whether applications run in containers, as serverless functions, or in traditional environments.
Risk management
SBOMs serve as the foundation for supply chain risk management by enabling comprehensive visibility into third-party software. Organizations often use AI-driven platforms to analyze SBOM data alongside other security metrics, creating a holistic view of their application health and risk posture.
These platforms track component versions, assess supplier risks and drive license compliance while providing actionable insights for risk mitigation. The integration of SBOM data with broader risk management processes enables organizations to make informed decisions about their software dependencies and maintain more secure, compliant application environments.
SBOM implementation challenges and solutions
Organizations can face several significant hurdles when implementing SBOM practices across their software ecosystem. Understanding and addressing these challenges is a key part of successful adoption and maintaining effective data security across the supply chain.
Common obstacles
The following challenges often arise when organizations implement SBOM practices:
Managing thousands of software components across diverse environments
Integrating SBOM data between different development tools and security platforms
Maintaining data quality, especially for legacy software and third-party components
Tracking dependencies in cloud environments with rapid deployment cycles
Balancing resource constraints with the need for accurate, current SBOM data
Adapting to dynamic cloud-native architectures where components change frequently
Best practices
Successful SBOM implementation requires a strategic approach that aligns with industry standards and organizational needs. Key elements include:
Automation and integration
Automate processes throughout the software development lifecycle
Seamlessly integrate with existing workflows and security tools
Use a unified platform for SBOM management
Follow CISA's maturity model:
Implement essential elements for basic SBOM functionality and compliance
Enhance documentation for broader security and compliance use cases
Enable comprehensive supply chain visibility through advanced features
Data management and transparency:
Generate and update SBOMs in real time, particularly in cloud-native environments
Document unknown information transparently rather than omitting it
Manage both complete internal SBOMs and redacted versions for external sharing
Governance and security integration:
Create clear SBOM governance policies with regular audits and automated validation
Connect SBOM data with Vulnerability Exploitability eXchange (VEX) for better vulnerability management
By following these practices, organizations can improve supply chain visibility, strengthen security and maintain compliance while addressing the challenges of SBOM implementation.
Industry trends shaping the future of SBOMs
The landscape of software supply chain security continues to evolve, driving innovations in SBOM technology and adoption. As organizations face increasingly sophisticated threats, the role of SBOMs in securing software ecosystems becomes more critical.
Several key trends are shaping the future of SBOM implementation and utilization:
AI-driven automation
Artificial intelligence advances are transforming how organizations manage and utilize SBOMs. Modern AI systems now automate SBOM generation and analysis while delivering more accurate predictive risk analysis and refined vulnerability detection. This automation extends to proactive security risk identification across software supply chains.
AI-specific documentation
A significant development is the emergence of specialized AI/ ML BOMs, addressing unique challenges in AI-generated code and models. These enhanced BOMs document AI model architectures, training data and testing methods, bringing necessary transparency to the AI development processes.
Enhanced security infrastructure
The security landscape for SBOM management continues to evolve. Blockchain and distributed ledger technology offer new solutions for secure SBOM storage and sharing, creating immutable audit trails that are particularly valuable for critical infrastructure systems. Organizations increasingly demand actionable SBOM data that enables rapid identification of compromised components and streamlined remediation.
Blockchain can enhance SBOM security by providing tamper-evident storage, enabling decentralized verification and facilitating secure cross-organizational sharing with strict access controls.
Unified platform adoption
This technological convergence drives adoption of unified platforms that integrate with existing DevSecOps practices. These solutions automate the entire SBOM lifecycle—from merging different data sources to managing approvals across multiple software versions and branches—while providing intelligence for risk mitigation.
Share
Link copied       
Upcoming webinar—2 June 2026 Embedding security into delivery Join us to explore how early risk detection can cut costs, reduce friction and strengthen compliance across your pipeline. 
Register now
Resources
Carousel   
Webinar The future of application performance monitoring (APM) and observability Learn how to get started with application monitoring, prioritize critical applications and use modern observability and Agentic AI to detect issues early, reduce downtime and deliver reliable user experiences. 
Watch the webinar   
Whitepaper Achieving application health in the microservices age Learn how real-time monitoring and automated remediation help identify issues faster, prevent failures, and maintain application health for a more reliable and consistent user experience. 
Read the whitepaper   
Report IDC Spotlight: Modern application resilience with AI-driven automation Discover how AI-powered application management helps teams overcome complexity, improve collaboration and gain a complete view of application health across modern cloud-native environments. 
Read the report   
Article 5 best practices for application growth Unlock actionable insights across fragmented application ecosystems. As application sprawl and dependencies grow, breaking down data silos is critical to connect teams, surface valuable information and drive smarter, faster business decisions. 
Read the article   
Report IDC: AI driven automation for application resilience that ensures compliance Discover how leading organizations use AI-driven automation to unify security, operations and development, strengthening resilience, reducing risk and meeting compliance requirements. 
Read the report
Video
AI agents: Transforming anomaly detection and resolution
Explore how agentic AI helps reduce downtime and resolve IT anomalies faster through smarter detection, faster root cause analysis and automated operations.
Watch the video
1 / 6 Slide 1 of 6. Showing 1 items.
Related solutions
IBM Concert
Streamline application management and get AI-generated insights that you can act on by using IBM® Concert®, a generative AI-driven technology automation platform. 
Explore IBM Concert
Application performance management software and solutions
Bridge full-stack observability with automated application resource management to address performance issues before they impact customer experience. 
Explore application performance management solutions
Application management services for hybrid cloud
Discover highly innovative services delivered by IBM Consulting® for managing complex, hybrid and multicloud environments. 
Explore application management services
Take the next step
By using AI, IBM Concert® uncovers crucial insights about your operations and provides application-specific recommendations for improvement. Discover how Concert can move your business forward.
Discover IBM Concert
Explore application performance management 
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
