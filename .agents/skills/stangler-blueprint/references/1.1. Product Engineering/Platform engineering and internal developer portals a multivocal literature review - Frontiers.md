---
name: Platform engineering and internal developer portals: a multivocal literature review - Frontiers
keywords: (placeholder)
metadata:
  url: https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Frontiers | Platform engineering and internal developer portals: a multivocal literature review 
Frontiers in Computer Science
About us
About us
Who we are
Mission and values
History
Leadership
Awards
Impact and progress
Frontiers' impact
Our annual reports
Thought leadership
Publishing model
How we publish
Open access
Quality and research integrity
Peer review
Research Topics
Publish your data
Fee policy
Services
Societies
National consortia
Institutional partnerships
Collaborators
More from Frontiers
Frontiers Forum
Frontiers Planet Prize
Press office
Sustainability
Career opportunities
Contact us
All journals All articles Submit your research
Search Login 
Frontiers in Computer Science
Sections
Sections
Computer Graphics and Visualization
Computer Security
Computer Vision
Digital Education
Human-Media Interaction
Mobile and Ubiquitous Computing
Networks and Communications
Software
Theoretical Computer Science
Articles Research Topics Editorial board
About journal
About journal
Scope
Field chief editors
Mission & scope
Facts
Journal sections
Open access statement
Copyright statement
Quality
For authors
Why submit?
Article types
Author guidelines
Editor guidelines
Publishing fees
Submission checklist
Contact editorial office
About us
About us
Who we are
Mission and values
History
Leadership
Awards
Impact and progress
Frontiers' impact
Our annual reports
Thought leadership
Publishing model
How we publish
Open access
Quality and research integrity
Peer review
Research Topics
Publish your data
Fee policy
Services
Societies
National consortia
Institutional partnerships
Collaborators
More from Frontiers
Frontiers Forum
Frontiers Planet Prize
Press office
Sustainability
Career opportunities
Contact us
All journals All articles Submit your research
Frontiers in Computer Science
Sections
Sections
Computer Graphics and Visualization
Computer Security
Computer Vision
Digital Education
Human-Media Interaction
Mobile and Ubiquitous Computing
Networks and Communications
Software
Theoretical Computer Science
Articles Research Topics Editorial board
About journal
About journal
Scope
Field chief editors
Mission & scope
Facts
Journal sections
Open access statement
Copyright statement
Quality
For authors
Why submit?
Article types
Author guidelines
Editor guidelines
Publishing fees
Submission checklist
Contact editorial office 
Frontiers in Computer Science
Sections
Sections
Computer Graphics and Visualization
Computer Security
Computer Vision
Digital Education
Human-Media Interaction
Mobile and Ubiquitous Computing
Networks and Communications
Software
Theoretical Computer Science
Articles Research Topics Editorial board
About journal
About journal
Scope
Field chief editors
Mission & scope
Facts
Journal sections
Open access statement
Copyright statement
Quality
For authors
Why submit?
Article types
Author guidelines
Editor guidelines
Publishing fees
Submission checklist
Contact editorial office
Submit your research Search Login
SYSTEMATIC REVIEW article
Front. Comput. Sci., 03 May 2026
Sec. Software
Volume 8 - 2026 | https://doi.org/10.3389/fcomp.2026.1814498
SYSTEMATIC REVIEW article
Front. Comput. Sci., 03 May 2026
Sec. Software
Volume 8 - 2026 | https://doi.org/10.3389/fcomp.2026.1814498
Platform engineering and internal developer portals: a multivocal literature review
M A Mateen Ali Anjum *
Phono Technologies Inc., Kitchener, ON, Canada
Article metrics
View details
497
Views
31
Downloads
Abstract
Platform engineering has become the dominant approach to managing developer infrastructure at scale, with industry surveys indicating that 94% of organizations have adopted or plan to adopt dedicated platform teams. Despite this rapid practitioner uptake, academic research remains scarce: a systematic search across five major databases identified fewer than a dozen peer-reviewed papers from reputable venues that address platform engineering directly, while gray literature from foundations, vendors, and industry surveys is abundant. This study presents the first multivocal literature review (MLR) of platform engineering and internal developer portals, following published guidelines for including gray literature in software engineering reviews. The review synthesizes 88 sources across both peer-reviewed and gray literature, with sources explicitly tiered by provenance and gray literature assessed using the AACODS framework. Five research questions address the state of the literature, architectural components and patterns, success metrics and KPIs, adoption barriers, and the relationship between platform maturity and developer productivity. The synthesis yields a taxonomy of internal developer portal components grounded in 36 architecture-focused sources, an integrated metrics framework spanning DORA, SPACE, and developer experience dimensions, a comparative analysis of four platform engineering maturity models, and a quantification of the academic–practitioner divide: only 2 of 88 included sources (2.3%) originate from tier-1 venues with platform engineering as their primary topic, while practitioner communities have generated the authoritative definitions, frameworks, and measurement instruments as academic engagement lags by two to three years. A particularly striking gap concerns scorecards, the primary governance mechanism within IDPs, for which no peer-reviewed empirical evidence of effectiveness exists despite widespread commercial adoption. These findings carry implications for both researchers and practitioners. For the research community, the study identifies nine specific opportunities where empirical work is most needed, with a validated PE maturity model and a PE-specific measurement instrument representing the highest-impact contributions. For practitioners, the evidence supports treating platforms as products, combining delivery metrics with developer experience surveys, and designing golden paths as enablers instead of mandates.
1 Introduction
Software organizations face a persistent tension between development velocity and operational reliability. As microservices architectures proliferate and cloud-native tooling fragments into hundreds of specialized products, developers increasingly spend time navigating infrastructure complexity instead of building features. The Cloud Native Computing Foundation's 2024 Annual Survey reported that the majority of responding organizations have adopted Kubernetes in production ( Cloud Native Computing Foundation, 2024), and the surrounding ecosystem of service meshes, observability stacks, secrets managers, and policy engines has expanded the surface area that development teams must understand. The 2024 State of Internal Developer Portals report estimates that 70% of developers spend three to four hours daily on non-core work due to insufficient internal tooling ( Port, 2024). Stack Overflow's 2024 Developer Survey, which sampled over 65,000 developers globally, confirmed that developer satisfaction with internal tooling ranks among the lowest-scoring categories, with developers routinely reporting that toolchain fragmentation and onboarding friction are primary sources of frustration ( Stack Overflow, 2024). The DORA Accelerate State of DevOps report, drawing on responses from more than 39,000 professionals, identified platform engineering as a key practice distinguishing elite-performing organizations from their peers ( DeBellis et al., 2024).
Platform engineering responds to this problem not by replacing DevOps, but by evolving it into an organizational capability that manages cognitive load at scale. Instead of expecting every development team to assemble and maintain its own delivery pipeline, dedicated platform teams build curated, self-service capabilities that abstract away operational complexity, preserving DevOps principles while shifting the delivery mechanism from distributed responsibility to centralized, product-managed infrastructure. Gartner named platform engineering a Top 10 Strategic Technology Trend for both 2024 and 2025, projecting that 80% of large engineering organizations will establish dedicated platform teams by 2026 ( Gartner, 2024). The Puppet State of DevOps Report 2024 found that 94% of surveyed organizations either already operate platform engineering practices or plan to adopt them within the year ( Puppet by Perforce, 2024).
The academic literature tells a different story. A systematic search across IEEE Xplore, the ACM Digital Library, Springer Link, ScienceDirect, and Google Scholar revealed only two peer-reviewed papers from tier-1 venues that treat platform engineering as their primary topic: ( Dursun 2023), published at ACM EASE, and ( van de Kamp et al. 2024), published in Springer LNCS. A handful of additional papers appear in regional conferences, workshop proceedings, and lower-tier journals. arXiv, which typically captures early-stage computer science research, returned zero directly relevant results. This academic void stands in sharp contrast to the gray literature, where the Cloud Native Computing Foundation (CNCF), DORA, Puppet, Humanitec, and numerous engineering blogs produce detailed reports, maturity models, and architectural guidance. The disparity is not merely quantitative: the gray literature sources include the canonical definitions used by the field (CNCF Platforms White Paper), the most widely adopted maturity models (CNCF, Humanitec), and the only large-sample empirical evidence for PE's effectiveness (DORA, with 39,000+ respondents). Excluding these sources would leave a review with almost nothing to synthesize.
The disconnect between practitioner knowledge and academic coverage is not unusual for nascent software engineering topics. Guidelines for conducting multivocal literature reviews (MLRs) address exactly this pattern, proposing methods that formally integrate gray literature alongside peer-reviewed sources ( Garousi et al., 2019). An MLR is the appropriate methodology when a topic has thin academic coverage but extensive practitioner discourse, exactly the situation that platform engineering presents. This study follows those guidelines, applying the AACODS framework ( Tyndall, 2010) for gray literature quality assessment and explicit source tiering throughout the analysis.
This review poses five research questions:
RQ1: What is the current state of academic and gray literature on platform engineering and internal developer portals?
RQ2: What are the key components, patterns, and architectural approaches for building internal developer portals?
RQ3: How do organizations measure the success of platform engineering initiatives?
RQ4: What are the adoption barriers, challenges, and failure patterns in platform engineering implementations?
RQ5: What is the relationship between platform engineering maturity and developer productivity?
The study makes six contributions. The first is the earliest academic multivocal literature review of platform engineering, formally integrating 88 sources assessed for quality and tiered by provenance. From 36 architecture-focused sources, the review synthesizes a taxonomy of IDP components spanning service catalogs, golden paths, self-service provisioning, and scorecards. A metrics framework integrating DORA, SPACE, and developer experience dimensions gives practitioners a unified measurement approach. Comparing four maturity models from CNCF, industry vendors, and academic literature reveals convergences and blind spots. The study quantifies the academic–practitioner divide, mapping where gray literature compensates for the absence of peer-reviewed research, and closes with nine specific open questions and a prioritized research agenda.
The closest existing work is the systematic mapping by ( Guisao et al. 2025) (Authorea preprint, not yet peer-reviewed), which charts the broad evolution from DevOps to platform engineering. This review differs in three ways: it focuses specifically on internal developer portals, not the general DevOps-to-PE trajectory, it formally assesses gray literature quality using AACODS, and it proposes practical frameworks (taxonomy, maturity model, metrics) instead of a mapping of publication trends.
The remainder of this paper is organized as follows. Section 2 covers background on the evolution from DevOps to platform engineering, internal developer portals, the developer experience movement, and the platform-as-a-product concept. Section 3 describes the MLR methodology, including the search strategy, inclusion and exclusion criteria, quality assessment, and synthesis approach. Section 4 presents findings organized by research question. Section 5 synthesizes cross-cutting themes, presents the comparative maturity model analysis and tool selection framework, discusses implications, and identifies threats to validity. Section 6 summarizes contributions and outlines future work.
2 Background
2.1 From DevOps to platform engineering
DevOps emerged around 2009 as a cultural and technical movement bridging software development and operations ( Jabbari et al., 2016), with early adopters reporting measurable improvements in deployment frequency and time to recovery ( Erich et al., 2017). As cloud-native tooling expanded, however, teams encountered a new bottleneck: the ecosystem surrounding Kubernetes ( Cloud Native Computing Foundation, 2024), spanning service meshes, observability stacks, CI/CD pipelines, and policy engines, created what practitioners describe as “cognitive load overload.” Tool sprawl and integration complexity were growing concerns ( Mishra and Otaiwi, 2020) even before platform engineering gained its current name.
Platform engineering responds by introducing a dedicated team whose product is the internal developer platform itself. The CNCF Platforms White Paper defines a platform as “an internal product providing a curated experience for developers, reducing cognitive load while retaining autonomy” ( CNCF TAG App Delivery, 2023b). This positions PE not as a replacement for DevOps, but as its maturation: the principles remain, while the delivery mechanism shifts from distributed responsibility to centralized, product-managed infrastructure. Organizations delivering product-service systems found that the “DevServOps” extension ( Dakkak et al., 2023) was needed to manage bidirectional information flows beyond pure software delivery, while ( Seremet and Rakić 2022) distinguished PE from SRE, noting that SRE targets service reliability through error budgets and SLOs, whereas PE targets developer productivity through self-service and cognitive load reduction.
2.2 Internal developer portals and developer platforms
Terminology in this space remains fragmented, and the fragmentation is not merely cosmetic. “Internal developer portal,” “internal developer platform,” and “developer experience platform” are used interchangeably across different vendor and practitioner communities, but each term carries slightly different connotations. “Portal” suggests a user-facing interface layer; “platform” implies a broader infrastructure abstraction; “developer experience platform” foregrounds the UX dimension. Some practitioners distinguish between the portal (the UI layer developers interact with) and the platform (the underlying abstraction and orchestration layer), while others treat them as synonymous. This terminological inconsistency complicates literature search, as studies using different terms may address identical concepts, and studies using the same term may describe different scope. Spotify popularized the “developer portal” framing when it open-sourced Backstage in 2020 ( Spotify Engineering, 2020), establishing a reference architecture built around a software catalog, plugin system, and template engine. Humanitec uses “platform orchestrator” to describe its approach to abstracting infrastructure provisioning. Port and Cortex focus on the portal layer that sits atop existing infrastructure tooling.
Despite the terminological diversity, a consistent set of components recurs across definitions. Service catalogs maintain a searchable registry of software components, APIs, and their ownership metadata. Golden paths, sometimes called “paved roads,” offer pre-configured, opinionated workflows that codify best practices for common tasks such as creating a new microservice, provisioning a database, or setting up a CI/CD pipeline. Self-service capabilities allow developers to provision infrastructure and perform day-2 operations without filing tickets or waiting for operations teams. Scorecards measure software component health against organizational standards ( van de Kamp et al., 2024; CNCF TAG App Delivery, 2023b).
A four-layer reference model for platform engineering, spanning infrastructure, runtime, delivery, and experience, was proposed by ( van de Kamp et al. 2024). Metamodeling concepts can further improve the structural coherence of internal developer platforms, especially for organizations managing multiple cloud providers ( Bayer, 2024).
2.3 The developer experience movement
Platform engineering is closely intertwined with the broader developer experience (DevEx) movement. The SPACE framework ( Forsgren et al., 2021) challenged reliance on single-metric proxies by decomposing developer productivity into five dimensions: Satisfaction and well-being, Performance, Activity, Communication and collaboration, and Efficiency and flow. Building on SPACE, developer experience was distilled into three core dimensions, feedback loops, cognitive load, and flow state ( Noda et al., 2023), which became the basis for the DX Core 4 measurement instrument ( Noda et al., 2024). A practical DevEx framework then bridged these theoretical models to practice ( Greiler et al., 2022).
Empirical evidence supports the connection between developer experience and productivity. At Google, code quality emerged as the strongest predictor of developer productivity ( Cheng et al., 2022), and onboarding, code review, and tooling were identified as key experience factors ( Jaspan and Green, 2022). A synthesis of 166 papers confirmed that tooling and environment, the very domain platform engineering targets, constitute top-tier productivity factors ( Razzaq et al., 2025b), while survey data linked job satisfaction to perceived productivity ( Storey et al., 2021).
2.4 Platform as a product and team topologies
The concept of treating platforms as internal products draws heavily on ( Skelton and Pais 2019), who introduced Team Topologies as an organizational design framework. Team Topologies identifies four fundamental team types: stream-aligned, enabling, complicated-subsystem, and platform. The platform team exists to reduce the cognitive load of stream-aligned teams by offering self-service capabilities through a “thinnest viable platform,” one that does as little as possible, as well as possible.
A multivocal literature review of Team Topologies adoption found that organizations struggled most ( Ahmed and Colomo-Palacios, 2021) with the transition from traditional team structures to the topology model, when existing Conway's Law dynamics resisted restructuring. This product thinking was formalized in a framework for managing platforms as products in IT organizations ( Mori and Kittlaus, 2025), incorporating product management practices such as user research, roadmapping, and internal satisfaction tracking.
The DORA 2024 report showed that organizations treating their platforms as user-centric products achieved measurably higher developer satisfaction and delivery performance ( DeBellis et al., 2024), and the Puppet 2024 report confirmed that 94% of organizations with mature PE practices described their platform teams in product-oriented terms ( Puppet by Perforce, 2024). The product orientation introduces a distinctive organizational challenge: internal platform customers choose between using the platform and building ad-hoc solutions, a dynamic the DORA findings suggest is heavily influenced by whether the platform is perceived as an enabler or a mandate ( DeBellis et al., 2024). Organizations at higher maturity levels resolve this tension through clear service-level agreements between platform teams and internal users ( Humanitec, 2024).
Despite the maturation of these adjacent areas, several open questions remain. The literature lacks a systematic assessment of IDP component architectures across academic and practitioner sources, an integrated framework for measuring PE success that bridges delivery metrics with developer experience, a critical comparison of the multiple maturity models circulating in industry, and an honest accounting of what adoption barriers organizations face in practice. These questions motivate the five research questions that this review addresses.
3 Methodology
3.1 Multivocal literature review design
This study follows the MLR guidelines proposed by ( Garousi et al. 2019) for including gray literature in software engineering systematic reviews. The guidelines recommend an MLR when three conditions hold: the topic has limited formal literature, substantial gray literature exists, and the gray literature contains unique, non-redundant insights. Platform engineering satisfies all three criteria. Fewer than a dozen peer-reviewed papers address it from reputable venues, while foundation whitepapers, industry surveys of tens of thousands of practitioners, and detailed vendor reports contain detailed analysis of adoption patterns, architectural approaches, and measurement frameworks.
The review protocol was designed before the formal search and covers search strategy, inclusion and exclusion criteria, quality assessment, source tiering, data extraction, and thematic synthesis. As a single-author review, two-pass screening with a two-week interval was applied to mitigate individual bias, following the approach described by ( Kitchenham and Charters 2007) for situations where a second reviewer is unavailable. The second screening pass yielded 97.9% agreement (140 of 143 sources). The three disagreements were all duplicate entries (two books and one arXiv preprint that appeared twice in the screening list under different formatting) reclassified as EC4 exclusions in the second pass; no substantive screening decisions changed between passes. The complete screening records for both passes are available in the supplementary data repository.
3.2 Search strategy
3.2.1 Academic database search
Five academic databases were searched: IEEE Xplore, the ACM Digital Library, Springer Link, ScienceDirect, and Google Scholar. The primary search string was:
(~platform engineering~ OR ~internal developer portal~ OR~internal developer platform~ OR ~developer platform~ OR~developer experience platform~) AND (~software engineering~ OR ~DevOps~ OR ~cloud~ OR ~microservices~ OR ~kubernetes~ OR ~software development~ OR ~developer productivity~)
Four supplementary search strings targeted specific facets: tools-focused (Backstage, Port, Cortex, and Humanitec), concepts-focused (golden path, service catalog, and developer self-service), metrics-focused (DORA metrics, SPACE framework, and developer experience measurement), and organizational-focused (platform team, Team Topologies, and cognitive load reduction). The date range was January 2020 through February 2026, reflecting the period in which platform engineering gained its current identity.
Forward and backward snowball sampling from the ten most-cited included papers was conducted to identify additional sources not captured by the database searches. The snowball sampling proved most productive for developer experience literature, where foundational papers such as ( Forsgren et al. 2021) have generated extensive citation networks that connect to platform engineering through shared concerns about developer productivity measurement and cognitive load reduction. Forward citation analysis from the SPACE paper alone identified over 80 citing works, of which 12 met the inclusion criteria. By contrast, the PE-specific papers ( Dursun, 2023; van de Kamp et al., 2024) had accumulated only two to three forward citations each at the time of the search, further confirming the field's academic immaturity.
The raw search across five databases returned substantially more records than the final candidate pool: Google Scholar alone returned approximately 2,400 results for the primary search string, but the vast majority were duplicates across databases, tangentially related cloud computing or DevOps papers without PE-specific content, or marketing material filtered during initial title screening. The 125 unique academic records and 18 snowball additions yielded 143 candidates that survived deduplication and title-level relevance screening. The relatively high inclusion rate (61.5%) is a direct consequence of using targeted search terms (“platform engineering,” “internal developer portal”) that are themselves niche: sources matching these terms tend to address the topic directly. Comparable MLRs in emerging SE topics report similar patterns: ( Kreuzberger et al. 2023) on MLOps synthesized 198 sources, ( Ahmed and Colomo-Palacios 2021) on Team Topologies included a similarly concentrated corpus, and ( Waqas et al. 2024) on low-code DevOps operated at comparable scale.
3.2.2 Gray literature search
Gray literature was identified through targeted searches of practitioner sources listed in Table 1. Sources were selected based on organizational authority, sample size, and relevance to the research questions. The CNCF Platforms White Paper and Platform Engineering Maturity Model were prioritized as the most authoritative practitioner references, having been developed through an open expert review process. Survey-based reports were included when they documented sample sizes, methodology, and respondent demographics.
Table 1
Gray literature sources and their characteristics.
3.3 Inclusion and exclusion criteria
Table 2 presents the inclusion and exclusion criteria applied during screening.
Table 2
Inclusion and exclusion criteria.
3.4 Quality assessment
Peer-reviewed papers were assessed using a five-item quality checklist: (1) research question clearly defined, (2) methodology appropriate and described, (3) results support conclusions, (4) threats to validity addressed, and (5) contribution clearly stated. Each item was scored on a 0–2 scale, yielding a maximum of 10.
Gray literature was assessed using the AACODS framework ( Tyndall, 2010), operationalized with 0–2 scoring across six dimensions: Authority (authoring organization's credibility), Accuracy (data backing and methodology transparency), Coverage (depth and breadth), Objectivity (vendor bias acknowledgment), Date (currency), and Significance (direct relevance to research questions). Sources scoring below 4 out of 12 were excluded.
Table 3 summarizes the quality assessment scores across all 88 included sources. Tier A papers scored a mean of 8.4 out of 10 on the five-item academic quality checklist, while Tier C gray literature averaged 9.9 out of 12 on the AACODS rubric, reflecting the high authority and methodological transparency of foundation-produced whitepapers and large-scale industry surveys. The complete per-source quality scores appear in the Supplementary material.
Table 3
Quality assessment score summary by tier.
Tier A/B use the five-item academic checklist (max 10). Tier C/D use the AACODS rubric (max 12).
3.5 Source tiering
All included sources were assigned to one of four tiers, and this tiering is maintained throughout the analysis to distinguish the strength of evidence behind each finding:
Tier A: Peer-reviewed papers from reputable venues (IEEE, ACM, Springer, Elsevier journals, and top conferences).
Tier B: Lower-tier peer-reviewed papers, theses, and preprints.
Tier C: High-quality gray literature with AACODS scores of 7 or above.
Tier D: Moderate gray literature with AACODS scores of 4–6.
3.6 Data extraction and thematic synthesis
Data was extracted using a structured 28-field template covering bibliographic metadata, source classification, RQ relevance mapping, and PE-specific fields: PE definition used, IDP tools mentioned, platform team structure, golden paths discussed, self-service capabilities, service catalog features, scorecard metrics, DORA metrics reported, developer satisfaction measured, organizational size and industry, adoption stage, maturity level, key findings, limitations, and future work suggested. Each source was classified with a binary (Y/N) mapping across all five research questions, enabling systematic coverage analysis. Of the 88 included sources, 25 received full extraction (complete access to full-text content), while 63 received partial extraction (abstract, metadata, and secondary-source corroboration). The partial extraction rate reflects the access constraints common in young fields where many sources are paywalled, available only as thesis PDFs, or published in venues without institutional access. To mitigate the risk of extraction error from partial access, key findings for partially extracted sources were triangulated against citing works, secondary analyses (i.e., reviews or surveys that summarized the same primary source), and the quality assessment data.
Thematic synthesis followed the approach recommended by ( Cruzes and Dybå 2011). Extracted findings were coded into themes for each research question, cross-tabulated by source tier (A through D), and synthesized with critical commentary that distinguishes peer-reviewed evidence from practitioner claims. The coding process was iterative: an initial pass generated 47 codes from the 88 sources, which were then consolidated into the themes reported in Sections 4.2–4.6 through card-sorting and affinity diagramming. Where multiple sources described the same phenomenon using different terminology, codes were merged under the prevailing term.
To distinguish included MLR sources from other cited works (methodology references, background literature), each of the 88 included sources receives a unique identifier: S1–S70 for academic studies (Tier A and B) and G1–G18 for gray literature (Tier C and D). The complete mapping between identifiers and bibliographic entries is provided in the Supplementary Data repository. Throughout the Results and Discussion sections, these identifiers appear alongside standard citations to indicate which findings derive from the reviewed corpus.
4 Results
4.1 Search results and literature landscape
The search process identified 143 candidate sources. Academic database searches contributed 125 unique records, and snowball sampling of the ten most-cited included papers yielded an additional 18 sources not captured by the primary search. After screening and quality assessment, 88 sources were included in the final synthesis: 44 Tier A (peer-reviewed, reputable venues), 26 Tier B (lower-tier journals, theses, and preprints), 9 Tier C (high-quality gray literature), and 9 Tier D (moderate gray literature). Fifty-five sources were excluded, with lack of PE-specific focus (23 sources, EC2) and questionable journal provenance (14 sources, EC5) accounting for the majority of exclusions. Sources could address multiple research questions; per-RQ counts therefore exceed the total of 88 included sources.
Figure 1 presents the PRISMA-adapted flow diagram for this MLR, illustrating the identification, screening, and inclusion process across both academic and gray literature streams.
Figure 1
PRISMA-adapted flow diagram for the multivocal literature review, showing the identification, screening, and inclusion of academic and gray literature sources.
The temporal distribution of included sources ( Figure 2) reveals a pronounced recency bias: 72% of all included sources were published in 2023 or later, and only six pre-2020 sources met the inclusion criteria (two seminal books and four foundational studies). The year 2024 produced the highest volume of included sources (32) across all tiers, driven largely by the simultaneous maturation of platform engineering industry surveys and the first wave of academic engagement with the topic.
Figure 2
Temporal distribution of the 88 included sources by tier (2017–2026). The search window spans 2020–2026; six pre-2020 sources are foundational references included for background context. The sharp increase from 2023 onward reflects the simultaneous maturation of practitioner surveys and the first wave of academic engagement.
Figure 3 provides an overview of the thematic structure across all five research questions, showing the number of sources contributing to each theme and the tier distribution of that evidence. Table 4 presents a representative selection of the included sources grouped by tier, illustrating the range of venues, methods, and research questions covered. The complete list of all 88 sources, with full quality assessment scores, RQ mappings, and S/G identifiers, appears in the Supplementary material.
Figure 3
Thematic structure and evidence tier distribution across all five research questions. Bar segments indicate the proportion of sources from each tier contributing to each theme. Source counts per theme may overlap, as individual sources can address multiple themes.
Table 4
Representative included studies by tier (selected from 88 sources).
Full list in Supplementary material.
4.2 RQ1: state of academic and gray literature
The platform engineering literature exhibits an inversion of the typical academic-to-practice knowledge flow. In most software engineering domains, peer-reviewed research establishes theoretical foundations that practitioners later adopt. Platform engineering exhibits the opposite pattern: practitioner communities have generated the authoritative definitions, frameworks, and measurement instruments, while PE-specific academic research lags by approximately three years. The lag is measured between the emergence of platform engineering as a named discipline in practitioner communities (Spotify open-sourced Backstage in 2020; CNCF formalized PE terminology in 2021–2022) and the first peer-reviewed papers treating PE as their primary subject ( Dursun, 2023 [S1] in 2023). Figure 2 shows the temporal distribution of all 88 included sources; note that the pre-2023 academic sources (Tier A) address adjacent topics (DevOps, DevEx, and Team Topologies) rather than platform engineering directly.
Only two papers from tier-1 academic venues focus on platform engineering as their central topic. ( Dursun 2023) [S1], published at ACM EASE, proposes a platform engineering approach for “full spec software” delivery. ( van de Kamp et al. 2024) [S2], published in Springer LNCS, presents a four-layer reference model. Both are short papers (under 10 pages) without empirical validation. A broader set of Tier A papers cover adjacent topics, including developer experience ( Greiler et al., 2022; Noda et al., 2023; Razzaq et al., 2025b; Forsgren et al., 2024), DORA metrics measurement ( Wilkes et al., 2023; Ruegger et al., 2024; Sallin et al., 2021), and DevOps practice evolution ( Erich et al., 2017; Mishra and Otaiwi, 2020), but none of these treat platform engineering as their primary subject.
The Tier A papers that do exist scatter across diverse venues, never clustering in a recognized community: ACM EASE, Springer LNCS workshops, IEEE ICODSE, IEEE Access, IEEE Software ( Galante, 2023), and a regional business technology conference ( Soeldner et al., 2023). No software engineering journal has published a PE-focused research article, and no top conference (ICSE, FSE, ASE, and ESEM) includes platform engineering as a track or theme. The geographic distribution of academic contributions is similarly scattered, with authors based in the Netherlands, Austria, Indonesia, Italy, and Finland. North American institutions, which dominate the practitioner discourse (CNCF, DORA, and Spotify), are conspicuously absent from the academic contributions.
Tier B sources, particularly master's theses from Tampere University, Aalto University, the University of Innsbruck, and the University of Padova, provide detailed single-organization studies of platform engineering adoption. These theses collectively constitute the richest academic treatments of PE available, as they typically include structured methodology sections, literature reviews, and empirical data from real implementations. One thesis detailed the challenges of transitioning from traditional DevOps to platform engineering at a European enterprise, identifying organizational resistance as the primary barrier ( Winkler, 2025) [S4]. Another designed and evaluated an internal developer platform at a Finnish software company, yielding rare first-hand implementation data ( Nieminen, 2024) [S39]. A third measured the impact of developer portals on developer experience through interviews and surveys at a Nordic organization ( Laredo Velázquez, 2023) [S40]. These theses fill a void between industry surveys (broad but methodologically limited) and the sparse Tier A papers, though their limitations must be acknowledged: they are student projects subject to less rigorous peer review than journal articles, typically examine a single organization, and may reflect supervisor interests more than systematic research agendas. Findings drawn primarily from thesis evidence are flagged as such throughout the results. Additional theses address self-service infrastructure provisioning at the University of Padova ( Nazo, 2024), a production-ready Backstage portal at UOC ( Franch López, 2024), PE in digital transformation ( Arrulo, 2024), and developer infrastructure experience at Aalto ( Donner, 2023). PlatFab, a platform engineering approach for improving developer productivity ( Srinivasan et al., 2025), represents one of the few academic proposals of a concrete PE framework.
The gray literature (Tiers C and D) supplies practical guidance that the peer-reviewed corpus does not. The CNCF Platforms White Paper ( CNCF TAG App Delivery, 2023b) [G1] and Platform Engineering Maturity Model ( CNCF TAG App Delivery, 2023a) [G2] serve as the de facto reference documents for the discipline, developed through open expert review. The DORA 2024 report ( DeBellis et al., 2024), with its 39,000-respondent sample, delivers the strongest statistical evidence for platform engineering's impact on delivery performance. Survey-based reports from ( Puppet by Perforce 2024), ( Port 2024), and ( Humanitec 2024) offer adoption statistics, but these carry identifiable vendor bias that is accounted for in the AACODS assessment. Further gray literature includes CNCF trend analyses ( CNCF TAG App Delivery, 2024), a Google Cloud perspective on PE practices ( Google Cloud, 2024b), and a platform-as-product adoption guide ( PlatformEngineering.org, 2024).
One blind spot in the gray literature concerns conference proceedings. PlatformCon, the largest platform engineering conference, hosted 169 talks in 2023 and over 80 h of content in 2024, yet does not publish formal proceedings. These talks contain a large body of practitioner knowledge that is inaccessible through traditional literature search mechanisms. Individual talks can be referenced as gray literature, but the absence of proceedings means that the conference's collective contribution to the field's knowledge base cannot be systematically assessed. This is both a limitation of this review and an opportunity for the PlatformCon organizers to formalize their contribution through published proceedings or curated talk summaries.
The multivocal literature review on Team Topologies adoption ( Ahmed and Colomo-Palacios, 2021) is a useful methodological precedent. That study similarly confronted a field where gray literature substantially outweighed peer-reviewed research, and its inclusion of practitioner blog posts, conference talks, and vendor reports alongside academic papers demonstrated the viability of the MLR approach for emerging software engineering topics. The DevEx-focused MLR from Aalto University ( Nylund, 2020) and the MLOps MLR published in ACM Computing Surveys ( Kreuzberger et al., 2023) further validate this approach, with the latter synthesizing 150 peer-reviewed and 48 gray literature sources using a methodology closely aligned with the current study.
4.3 RQ2: IDP components, patterns, and architecture
Analysis of 36 sources addressing IDP architecture yields a consistent component taxonomy ( Figure 4) despite the terminological fragmentation noted in Section 2.2. The taxonomy was developed through bottom-up thematic coding: each source's description of IDP components was coded into atomic capabilities, which were then grouped into categories through iterative comparison. Six primary categories recur across the reviewed sources: Developer Experience, Service Catalog, Platform Capabilities, Observability and Insights, Workflow Automation, and Governance and Standards. The convergence across sources is notable given that practitioners developed these components independently, without a shared academic reference. Where sources disagree, the disagreement is typically terminological (“golden path” vs. “paved road”), not functional.
Figure 4
Taxonomy of Internal Developer Portal components synthesized from 36 sources across Tiers A–D, showing six primary capability categories and their constituent features.
Before examining the components, the definitional terrain that emerged from the data extraction deserves attention. Of the 88 included sources, 52 provided an explicit or implicit definition of platform engineering, and these definitions cluster into three families. The CNCF family, used by 19 sources, defines PE as “the practice of planning and providing computing platforms” to reduce cognitive load while retaining developer autonomy. The Team Topologies family, used by 14 sources, defines PE through the lens of platform teams providing self-service capabilities via a “thinnest viable platform” ( Skelton and Pais, 2024; The New Stack, 2024). This connection was formalized by applying Team Topologies concepts within model-driven strategic alignment ( Noel et al., 2023). The remaining 19 sources use ad hoc definitions, typically framing PE as an evolution of DevOps or as an organizational approach to standardizing developer tooling. The lack of a consensus definition across academic and practitioner communities complicates systematic study, as different definitions emphasize different aspects: cognitive load reduction, self-service capabilities, team structure, or infrastructure abstraction. This definitional fragmentation is itself a research opportunity (see Section 5.6).
Figure 5 situates these components within the broader platform engineering ecosystem, illustrating how platform teams, developer experience layers, and infrastructure interact.
Figure 5
Platform engineering ecosystem showing the relationship between organizational structure (platform teams, stream-aligned teams), platform layers (infrastructure, IDP, developer experience), and feedback mechanisms (DORA, SPACE, DevEx metrics).
The following subsections examine each category. The Developer experience category encompasses golden paths and onboarding workflows. Service catalog covers software entity registries and dependency mapping. Platform capabilities spans self-service provisioning and infrastructure abstraction. Observability and insights includes scorecards and compliance tracking. Workflow automation and Governance and standards are discussed as distinct operational and compliance layers respectively.
Service catalogs are the most widely discussed component, mentioned in 28 of 36 RQ2 sources. Backstage set the dominant implementation model, structuring the catalog around software entities (services, APIs, resources, users, and teams) linked by ownership metadata and dependency graphs. Empirical evidence from at least one organization confirms the approach: measurable improvements in service discoverability were reported ( Ciancarini et al., 2025) [S9] and reduced time spent locating documentation after deploying a self-hosted catalog.
Twenty-two sources discuss golden paths, standardized, opinionated workflows that let developers build without needing to understand the full infrastructure stack. The concept was formalized as the mechanism for reducing cognitive load in full-spec software delivery ( Dursun, 2023) [S1]. “Development Environment as Code” (DEaC) extended this idea, demonstrating through action design research that codifying development environments as standardized, version-controlled artifacts reduced onboarding time and improved environment consistency ( Ghanbari et al., 2025) [S56]. The CNCF White Paper ( CNCF TAG App Delivery, 2023b) describes golden paths as “guardrails, not gates,” emphasizing that they should enable, not constrain, developer autonomy. Practitioner accounts describe implementation patterns that balance enablement with consistency ( The New Stack, 2023; Google Cloud, 2024a; Red Hat, 2024b). Paved roads resolve cognitive overload by offering clear defaults without restricting alternatives ( Brown, 2024).
The CNCF identifies self-service infrastructure provisioning as the defining characteristic of platform engineering ( CNCF TAG App Delivery, 2023b), and 20 sources discuss it. The recurring emphasis is on eliminating ticket-based workflows that create bottlenecks between developers and operations teams. Self-service capabilities range from simple resource provisioning (database creation, environment setup) to complex multi-step workflows involving approval chains, cost estimation, and compliance checks. Earlier work demonstrated microservices-based developer self-service ( Tilak et al., 2020), extended self-service to performance testing for autonomous teams ( Vasilevskii and Kachur, 2024), and proposed deployment-oriented specifications that reduce manual provisioning ( Gomes, 2024). A self-service DevOps platform for black-box testing on Kubernetes showed how platform teams can supply on-demand testing infrastructure without requiring developers to understand the underlying container orchestration ( Golis and Dakić, 2024). The design of a cloud-native DevOps platform that transitions from manual provisioning to self-service through API abstractions predates the formal PE terminology but embodies its principles ( Chen and Suo, 2022). In a notable expansion of PE beyond its software engineering origins, model-driven platform engineering was applied to automate the deployment of fog computing applications in smart factories ( Cuadra et al., 2024).
Almost all evidence on scorecards and compliance tracking comes from Tier C and D literature, with 16 sources contributing. Scorecards measure software components against organizational standards (test coverage, documentation completeness, vulnerability scanning, and production readiness) and surface the results in the developer portal. No Tier A paper provides empirical evaluation of scorecard effectiveness. This absence is significant because scorecards serve as the primary governance mechanism within IDPs ( van de Kamp et al., 2024; Port, 2024): they translate organizational quality standards into measurable, actionable feedback for developers. The commercial IDP tools (Cortex, OpsLevel, and Atlassian Compass) have made scorecards a central feature of their value proposition, yet the academic literature has not examined whether scorecard-driven governance actually improves software quality or whether it introduces perverse incentives analogous to the “Goodharting” problem documented for DORA metrics.
Workflow automation, covering self-service actions, approval workflows, and resource lifecycle management, appears in 14 sources and represents the operational backbone of platform engineering. Without automation, self-service capabilities degenerate into request-and-wait ticket systems under a different name. Automatic pipeline provisioning illustrates one approach, generating CI/CD configurations from declarative specifications without human intervention ( Labonté-Lamoureux and Boyer, 2025) [S37]. Thesis work at Tampere demonstrated end-to-end workflow automation through a Backstage portal that integrated provisioning, deployment, and monitoring into a single developer-facing interface ( Nieminen, 2024) [S39]. The self-service platform described by ( Golis and Dakić 2024) [S8] automated black-box testing workflows on Kubernetes, removing the need for developers to interact with container orchestration directly. The critical finding across these sources is that automation maturity follows a progression: from manual requests with digital interfaces (Level 1), through template-driven provisioning (Level 2), to fully declarative, event-driven workflows (Level 3). Most organizations in the reviewed literature remain at Level 1 or 2, suggesting that workflow automation represents an area where tooling has outpaced organizational adoption.
Governance and standards enforcement, including policy-as-code, compliance automation, audit trails, and role-based access, appears in 12 sources. Governance requirements in regulated industries create additional constraints that complicate platform adoption, as standard IDP workflows must be augmented with approval chains and audit capabilities that commercial IDP tools do not natively support ( Salin et al., 2025) [S55]. The tension between self-service velocity and governance compliance is most acute in financial services, healthcare, and government sectors, where organizational context significantly shapes the capability profiles that DevOps (and by extension, platform) teams must develop ( Plant et al., 2025) [S67]. The CNCF Platforms White Paper ( CNCF TAG App Delivery, 2023b) [G1] acknowledges governance as a necessary layer but provides only high-level guidance, deferring implementation specifics to individual organizations. The four-layer reference model by ( van de Kamp et al. 2024) [S2] places governance within the experience layer, suggesting that governance should be surfaced through the developer portal rather than enforced through separate tooling. This synthesis indicates that governance remains the least mature IDP category: it is broadly recognized as necessary but lacks both standardized implementation patterns and empirical evidence for which governance approaches produce the best compliance-velocity trade-offs.
A small number of tools dominate IDP architecture. Port.io's 2024 survey reports that Backstage holds 89% penetration among organizations using IDP tools ( Port, 2024). This figure must be interpreted with substantial caution: Port is a direct Backstage competitor, the survey sampled only 100 engineering leaders, and the respondent selection methodology is not disclosed. Independent corroboration of the penetration figure is unavailable from any Tier A source. Table 5 compares the major IDP tools across key capability dimensions.
Table 5
Feature comparison of major IDP tools across key capability dimensions.
Ratings based on vendor documentation, practitioner reports, and Tier B academic evaluations. Figure 7 extends this comparison to eleven dimensions with finer-grained scoring.
4.4 RQ3: success metrics and KPIs
Success measurement drew the broadest engagement across the corpus, with 51 sources contributing to the analysis. Platform engineering metrics operate at three levels, which this review synthesizes into the integrated framework shown in Figure 6.
Figure 6
Three-layer platform engineering success measurement model synthesized from DORA, SPACE, DevEx, and practitioner-specific metrics. Leading indicators at the platform health layer drive lagging business outcomes through developer productivity improvements.
Figure 7
Feature comparison heatmap of major IDP tools across 11 capability dimensions. Ratings derived from vendor documentation, practitioner reports, and academic evaluations.
4.4.1 Delivery performance metrics (DORA)
The four key metrics introduced by ( Forsgren et al. 2018) [G6] and refined through annual DORA reports, deployment frequency, lead time for changes, change failure rate (CFR), and mean time to recovery (MTTR), serve as the baseline for measuring delivery performance. The DORA 2024 report found that organizations with mature platform engineering practices cluster disproportionately in the “elite” performance tier, characterized by on-demand deployment, lead times under one hour, change failure rates below 5%, and recovery times under 1 h ( DeBellis et al., 2024). Two independent frameworks for automating DORA measurement from Git and CI/CD pipeline data have reduced the manual effort required for continuous tracking ( Wilkes et al., 2023; Ruegger et al., 2024) [S64, S61]. Early empirical validation of the four key metrics in agile teams confirmed their applicability beyond Google's original context ( Sallin et al., 2021) [S62]. A systematic review identified 47 distinct DevOps metrics used in practice, of which the four DORA metrics were dominant ( Kumar et al., 2025) [S68]. Thesis-level work has addressed metrics operationalization ( Pettersson, 2025; Koskinen, 2024; Riihimäki, 2024), examining how productivity metrics can be automated and integrated into DevOps workflows.
4.4.2 Developer experience metrics (SPACE and DevEx)
DORA metrics, while necessary, are insufficient for capturing developer productivity in full ( Forsgren et al., 2021) [S15]. The SPACE framework adds dimensions of satisfaction, communication, and efficiency that delivery metrics do not target. Developer experience was subsequently simplified into three concrete dimensions, feedback loops, cognitive load, and flow state, forming the basis for the DX Core 4 measurement instrument ( Noda et al., 2023, 2024) [S16]. A practice-oriented DevEx framework then bridged theory to practice by mapping survey data to specific organizational interventions ( Greiler et al., 2022) [S58]. A synthesis of 166 papers confirmed that tooling environment quality is among the top-3 factors influencing the DevEx–productivity relationship, directly validating platform engineering's focus area ( Razzaq et al., 2025b) [S17]. Foundational work on rethinking productivity measurement ( Sadowski and Zimmermann, 2019), recent empirical studies ( Razzaq et al., 2025a; Palomino et al., 2024; Guthardt et al., 2024), and thesis research on developer portal evaluation ( Morelius, 2024) further demonstrate that tooling quality drives developer satisfaction.
4.4.3 Platform-specific metrics
Gray literature sources introduce metrics that are specific to platform engineering but lack academic validation. These include: self-service adoption rate (the proportion of infrastructure provisioned through the platform instead of manual requests), golden path adherence rate, internal NPS (Net Promoter Score) from platform users, developer onboarding time, and time-to-first-deployment for new services. Spotify engineering blogs report that onboarding time was halved after Backstage adoption ( Spotify Engineering, 2020). The Puppet 2024 survey claims a 30% faster deployment rate for organizations with mature PE practices ( Puppet by Perforce, 2024). These metrics are promising but derive entirely from self-reported survey data and vendor case studies (Tier C/D) and have not been independently validated.
Developer satisfaction strongly predicts perceived productivity ( Storey et al., 2021) [S63], and developer burnout has been modeled as a downstream consequence of poor developer experience ( Trinkenreich et al., 2023) [S65]. These findings, while not PE-specific, suggest that platform engineering's emphasis on reducing cognitive load may have measurable impact beyond delivery metrics, extending to developer well-being and retention.
4.4.4 Emerging measurement approaches
Several recent contributions target the operationalization disconnect between frameworks and measurement practice. One study examined developer experience measurement in the context of AI-augmented workflows, arguing that traditional metrics require recalibration as AI tools change the nature of developer work ( Valiulla, 2025b) [S30]. The proposed three-layer model, developer metrics (DORA-based), developer experience (flow vs. context-switching), and value alignment (business KPIs), offers a structured approach to integrating PE measurement with broader organizational goals. The Prismetrix method combines quantitative metrics with qualitative developer insights ( Kawalerowicz and Pietranik, 2025) [S69], which addresses the limitation of pure survey-based or pure telemetry-based approaches. These approaches remain at the proposal stage, without empirical validation in PE contexts, but they signal a maturing measurement discourse that may soon produce the validated PE-specific instruments that this field currently lacks. Complementary work includes framework comparisons across DORA, SPACE, and HEART ( Valiulla, 2025a) [S29], an exploration of SPACE metrics in practice ( Kaul et al., 2025) [S22], and foundational work toward a science of developer experience ( Combemale, 2025) [S23].
Table 6 summarizes how each metric family is operationalized in practice, highlighting the measurement approaches, data sources, and cadences reported in the reviewed literature.
Table 6
Operationalization of platform engineering success metrics across three levels.
Sources indicate the tier providing the strongest evidence for each metric.
A critical observation from the synthesis is that automated measurement is advancing rapidly for DORA metrics, with fully automated pipelines ( Wilkes et al., 2023; Ruegger et al., 2024) that extract the four key metrics from Git and CI/CD data without manual intervention. DevEx measurement, on the other hand, still relies predominantly on periodic survey instruments ( Noda et al., 2024; Greiler et al., 2022), creating a temporal mismatch: delivery metrics can be tracked continuously, while developer experience is sampled quarterly at best. Platform-specific metrics occupy an intermediate position, as self-service adoption and golden path adherence can be tracked through platform telemetry, while internal NPS and developer onboarding time still require manual collection ( Humanitec, 2024; Port, 2024). This measurement asymmetry means that organizations risk over-indexing on what is easy to measure (DORA) and neglecting what matters most (whether developers actually find the platform useful).
The measurement operationalization challenge extends beyond tooling to organizational interpretation. A systematic review identified 47 distinct DevOps metrics used in practice ( Kumar et al., 2025), yet most organizations track fewer than ten, and the selection criteria are rarely documented or justified. The “Goodharting” problem, where optimizing for a metric undermines the goal it was designed to measure, is a recognized risk for DORA metrics in particular. Deployment frequency, the easiest DORA metric to automate, can be inflated through pipeline splitting without any genuine improvement in delivery capability. Change failure rate is sensitive to the definition of “failure,” which varies across organizations and is rarely standardized even within a single organization. These measurement validity concerns apply with equal force to PE-specific metrics: a high self-service adoption rate may reflect genuine platform value, or it may reflect organizational mandates that force developers to use the platform regardless of whether it meets their needs.
4.5 RQ4: adoption barriers and challenges
Twenty-eight sources contribute to the analysis of adoption barriers. Organizational resistance is the dominant obstacle, followed by cognitive load trade-offs, measurement attribution challenges, technical sustainability concerns, and skills shortages.
4.5.1 Organizational resistance and mandate failure
The DORA 2024 report offers the strongest evidence on this theme: organizations where platforms were mandated top-down reported lower developer satisfaction than those where adoption was driven by demonstrated value ( DeBellis et al., 2024). Team Topologies adoption, which underpins platform team structures, required extensive organizational restructuring that many organizations underestimated ( Ahmed and Colomo-Palacios, 2021) [S33]. DevOps team performance depends on alignment between organizational context and team capabilities; when this alignment is absent, platform engineering initiatives stall regardless of technical quality ( Plant et al., 2025) [S67]. Platform-centric agile transformation similarly requires organizational restructuring that many enterprises underestimate ( Wang, 2025) [S12].
4.5.2 Cognitive load trade-off
Platforms themselves can become a source of complexity when poorly designed, undermining the very cognitive load reduction they promise. The “thinnest viable platform” principle from Team Topologies ( Skelton and Pais, 2019) [G13] addresses this tension, but in practice, organizations frequently over-engineer their platforms before validating that developers need the capabilities being built ( CNCF TAG App Delivery, 2023b). Microservices architectures increase cognitive load, which IDPs should reduce, yet the IDP itself adds a learning curve ( Gangula, 2024) that temporarily increases load during adoption. This pattern suggests a hypothesized J-curve effect: developer productivity may dip during initial platform adoption before recovering and eventually exceeding pre-platform levels. The dip duration and depth would depend on the platform's complexity, the quality of onboarding documentation, and whether golden paths align with existing developer workflows. No study in the reviewed literature quantifies this J-curve, and the hypothesis rests entirely on adoption narratives reported in Tier B theses rather than empirical measurement. Validating or refuting this hypothesis through longitudinal productivity tracking during PE rollouts represents a concrete research opportunity.
4.5.3 Measurement attribution
Pinpointing whether productivity improvements come from platform engineering or from concurrent changes is an unsolved attribution problem. Multiple changes, new tools, team restructuring, process improvements, typically occur concurrently. The same attribution problem was identified for DevOps adoption more than 5 years earlier ( Erich et al., 2017) [S66], and the challenge persists. DORA metrics can be “goodharted” (optimized for the metric at the expense of the underlying goal), and self-reported DevEx surveys are subject to response bias.
4.5.4 Technical sustainability
Platforms accumulate technical debt, above all in plugin-based architectures. Backstage's ecosystem of over 800 plugins varies significantly in quality and maintenance status, and the upgrade path for the Backstage framework itself requires ongoing engineering investment that many organizations underestimate during initial adoption planning. Migration from ad-hoc tooling to a unified platform is a multi-year effort that requires sustained investment beyond initial setup. Domain-specific platform engineering, as in manufacturing, adds cross-domain integration complexity ( Cuadra et al., 2024) [S53] that pure software organizations do not face. The technical debt problem is compounded by the pace of change in the cloud-native ecosystem: the CNCF landscape lists over 1,100 projects as of 2024, and platform teams must decide which integrations to support, maintain, and deprecate as the ecosystem evolves. Organizations that build deep integrations with specific tools risk lock-in, while those that maintain shallow integrations across many tools risk providing insufficient value to justify the platform's existence.
4.5.5 Skills and staffing
Building a platform team requires a combination of infrastructure engineering, product management, and user experience skills that few organizations have concentrated in one group. The Humanitec 2024 survey reported that staffing was the second most frequently cited barrier after organizational buy-in ( Humanitec, 2024). Platform engineers must understand both the infrastructure they are abstracting and the developer workflows they are optimizing, a dual competency that is scarce in the labor market. Product management skills are particularly critical, as platform teams without them tend to build technically impressive solutions that fail to address actual developer pain points ( Mori and Kittlaus, 2025), a pattern observed independently in the DORA 2024 findings on mandated vs. product-oriented platforms ( DeBellis et al., 2024). The skills shortage is compounded by the absence of formal educational pathways for platform engineering. Unlike DevOps, which now features in university curricula and professional certifications, platform engineering has no established training programs, professional certification bodies, or academic specialization tracks. The challenges of developing effective engineering team structures at SaaS companies confirm that platform team formation requires deliberate organizational design ( Bhorkar, 2023) [S35], not organic emergence. The theses from Tampere, Aalto, and Innsbruck represent early steps toward academic engagement with the topic, but they remain individual efforts rather than components of a structured educational program.
4.6 RQ5: maturity and developer productivity
The relationship between platform engineering maturity and developer productivity surfaces in 38 sources, with the evidence split between survey-based correlational findings (Tiers C/D) and theoretical frameworks (Tier A).
4.6.1 Maturity model overview
Four distinct maturity models operate in the practitioner ecosystem. The CNCF Platform Engineering Maturity Model ( CNCF TAG App Delivery, 2023a) [G2] defines four levels: Provisional, Operational, Scalable, and Optimizing, assessed across investment, adoption, interfaces, operations, and measurement dimensions. Humanitec's model, documented across four annual State of Platform Engineering reports ( Humanitec, 2022, 2023, 2024, 2025) [G-series], uses five stages focused on tool adoption maturity. The DORA performance clusters (Low, Medium, High, and Elite) provide a delivery performance maturity lens ( DeBellis et al., 2024), and the Puppet 2024 report identifies three evolutionary stages from DevOps to mature PE ( Puppet by Perforce, 2024). No Tier A source proposes or validates a PE maturity model; all existing models originate from gray literature.
4.6.2 Practical model application
How organizations use these maturity models in practice differs from their intended design. The CNCF model is the most frequently cited in organizational assessment contexts, yet its qualitative level descriptions (e.g., “investments are made with no formal tracking of ROI” at the Provisional level) leave considerable room for self-serving interpretation. The Humanitec model, by contrast, ties maturity levels to specific tool adoption milestones, making assessment more concrete but narrowing the scope to technical tooling at the expense of organizational and cultural dimensions. In practice, organizations often combine elements from multiple models, using CNCF dimensions for organizational assessment and Humanitec stages for technical roadmapping, yet none of the reviewed sources documents this hybrid usage formally.
4.6.3 Correlation evidence
The DORA 2024 survey, representing the strongest statistical evidence, reports that elite-performing organizations are substantially more likely to have mature platform engineering practices, although the report notes that the causal direction cannot be established from cross-sectional survey data ( DeBellis et al., 2024). The Puppet 2024 report claims that organizations with mature PE report 30% faster deployment and 50% fewer incidents ( Puppet by Perforce, 2024), but these figures come from a smaller, self-selected sample. Improvements in deployment frequency and onboarding time were demonstrated at a single organization after IDP implementation ( Ciancarini et al., 2025) [S9], and Development Environment as Code reduced environment setup time through an action design research study at one company ( Ghanbari et al., 2025) [S56].
4.6.4 Developer experience as mediating variable
Why would platform maturity drive productivity? The most parsimonious explanation runs through developer experience as an intermediary: platform maturity influences developer experience, which in turn drives productivity. DevEx improvements lead to measurable productivity gains ( Noda et al., 2023; Greiler et al., 2022) [S16, S58]. A synthesis of 166 papers confirmed that tooling environment, the specific domain platform engineering targets, is among the strongest predictors of developer productivity ( Razzaq et al., 2025b) [S17]. Empirical evidence from a government organization showed that developer experience hindrances in regulated environments differ from those in commercial settings, suggesting that maturity models should account for organizational context ( Salin et al., 2025) [S55]. The theoretical link between satisfaction and perceived productivity has been demonstrated through large-scale survey data ( Storey et al., 2021) [S63].
4.6.5 Adjacent productivity evidence
While direct PE-productivity evidence remains thin, adjacent studies provide indirect support for the platform engineering hypothesis. At Google, code quality was the strongest predictor of developer productivity ( Cheng et al., 2022) [S60], with engineering system quality (the domain PE targets) ranking among the top five factors. Developer onboarding, a process directly improved by golden paths and self-service capabilities, significantly affected perceived productivity in a separate Google study ( Jaspan and Green, 2022) [S59]. SPACE framework validation demonstrated that input-output perspectives on productivity measurement can capture the effects of tooling improvements ( Tunggono and Princes, 2025) [S19]. The Prismetrix method for systematic productivity measurement ( Kawalerowicz and Pietranik, 2025), which combines quantitative metrics with qualitative insights, could capture PE's multidimensional impact. These studies, while not PE-specific, support the theoretical mechanism through which platform engineering would drive productivity: by improving the tooling environment, reducing onboarding friction, and enabling flow state through reduced cognitive load.
The overall evidence pattern is clear: organizations with more mature PE practices report better outcomes across DORA metrics, DevEx surveys, and self-reported productivity. The evidence is weakest on the question practitioners care about most, whether platform engineering causes these improvements or whether already high-performing organizations are simply more likely to adopt PE practices. Establishing causation would require either longitudinal studies that track organizations before and after PE adoption, or quasi-experimental designs that compare matched organizations with and without PE practices. Neither design has been attempted in the current literature, and the organizational complexity of PE adoption makes randomized controlled trials impractical. The strongest available evidence for a causal link comes from the single-organization case studies by ( Ciancarini et al. 2025) and ( Ghanbari et al. 2025), where before-and-after comparisons within the same organization control for some organizational confounds, but not for concurrent changes.
5 Discussion
5.1 Key findings synthesis
What do these findings add up to? The research question answers paint a field in a distinctive state of maturity.
RQ1 answer (supported by 17 sources across all tiers): Only 2 of 88 included sources (2.3%) from Tier A venues treat PE as their primary topic, while Tier C gray literature supplies the authoritative frameworks, definitions, and adoption data. Peer-reviewed research lags practitioner knowledge by two to three years.
RQ2 answer (drawing on 36 sources, with Tier A evidence anchoring the taxonomy and Tier C/D informing tool-specific claims): Internal developer portals share a consistent set of core components organized into six categories: service catalogs, golden paths, self-service provisioning, scorecards, workflow automation, and governance and standards enforcement. The dominant implementation pattern is a plugin-based architecture exemplified by Backstage. Emerging directions include Development Environment as Code and model-driven PE for non-software domains.
RQ3 answer (the broadest engagement at 51 sources—29 Tier A, 15 Tier B, 5 Tier C, 2 Tier D; Tier A underpins the DORA/SPACE/DevEx frameworks, while PE-specific metrics rest on Tier C/D only): PE success measurement integrates three metric families: DORA for delivery performance, SPACE/DevEx for developer experience, and PE-specific metrics (self-service adoption, golden path adherence, internal NPS) that lack academic validation. Automated measurement frameworks for DORA are advancing rapidly, while DevEx measurement relies primarily on survey instruments.
RQ4 answer (28 sources; DORA 2024 provides strongest evidence, supplemented by Tier B theses and Tier D practitioner reports): The data surfaces five adoption barriers: organizational resistance (mandate failure, Conway's Law), cognitive load trade-offs (platform learning curves), measurement attribution challenges, technical sustainability concerns (platform debt accumulation), and skills shortages (combined infrastructure engineering, product management, and UX competencies). Organizations that treat platforms as mandated infrastructure, not user-centric products, report worse outcomes.
RQ5 answer (38 sources, split between Tier C survey correlations and Tier A theoretical frameworks): Survey data from large samples uniformly shows that mature PE correlates with better delivery performance and developer experience. The causal mechanism likely operates through developer experience as a mediating variable, though longitudinal and interventional evidence is absent from the current literature.
5.1.1 Cross-RQ patterns
Beyond the individual answers, the findings reveal interconnected themes that span multiple research questions.
A measurement maturity gradient runs through the entire field: delivery metrics (RQ3) are well-defined and increasingly automated, while adoption barriers (RQ4) and the maturity-productivity relationship (RQ5) remain almost entirely characterized through self-reported survey data. The paradox is that the aspects of platform engineering that matter most to organizations, whether it is working and what is blocking adoption, are the hardest to measure rigorously.
The RQ2 taxonomy and RQ4 barrier analysis, read together, expose a tension between standardization and autonomy. IDP components are built around standardized golden paths and self-service workflows, yet organizational resistance to mandated tooling is the primary adoption barrier. The maturity evidence (RQ5) suggests that this tension resolves itself when platforms are treated as products that developers choose to use, not infrastructure they are forced to adopt, though the evidence for this resolution mechanism comes exclusively from gray literature.
RQ1 also has downstream implications for all other findings. Academic absence constitutes a structural risk: the missing measurement instruments (RQ3), the reliance on vendor-funded survey data for adoption patterns (RQ4), and the absence of longitudinal evidence for the maturity-productivity link (RQ5) are all consequences of academic disengagement from a field that has grown rapidly without scholarly infrastructure.
A fourth pattern concerns definitional fragmentation and its measurement consequences. The three definition families, CNCF-centered (cognitive load reduction), Team Topologies-centered (self-service delivery), and ad hoc (infrastructure abstraction), lead organizations to measure different things. A team defining PE through cognitive load will prioritize DevEx surveys; one defining it through infrastructure abstraction will track self-service adoption rates. This pluralism partly explains the measurement heterogeneity in RQ3 and will persist until the field converges on a working definition (research agenda, opportunity 5).
A fifth pattern, evidence quality degradation at increasing specificity, cuts across all research questions. Broad claims like “PE improves developer productivity” are supported by large-sample surveys, but specific claims narrow sharply: service catalog discoverability rests on one study ( Ciancarini et al., 2025) [S9], golden path onboarding benefits on one action design research study ( Ghanbari et al., 2025) [S56] and one thesis ( Nieminen, 2024) [S39], and scorecard effectiveness on no empirical evidence at all. This diminishing evidence at increasing specificity underscores the priority of empirical research opportunities in Section 5.6.
5.2 Comparative maturity model analysis
The four maturity models identified in RQ5 differ in scope, granularity, and intended audience ( Figure 8). The CNCF model is the broadest in scope, spanning five dimensions with four levels each, but offers only qualitative descriptions without measurable criteria. Humanitec's model is tool-adoption focused and carries vendor bias. DORA's performance clusters are empirically grounded but measure delivery outcomes rather than platform capabilities. Puppet's three-stage evolution model captures the DevOps-to-PE journey but lacks specificity at each stage.
Figure 8
Comparative analysis of four platform engineering maturity models, showing convergence toward three-to-five progressive stages despite differing dimensional focus.
All four models converge on certain principles: maturity progresses through three to five stages, early stages focus on basic tool adoption and ad-hoc self-service, and advanced stages require measurement-driven optimization and platform-as-product thinking. The models diverge on what dimensions to assess. The CNCF model includes investment and organizational adoption alongside technical interfaces; Humanitec focuses almost exclusively on technical tooling progression; DORA measures outcomes, not capabilities; and Puppet tracks the organizational journey from DevOps to PE. None of the models provides quantitative thresholds for advancing between levels, relying instead on qualitative descriptions that leave wide room for interpretation. This absence of operationalized thresholds is a recurring limitation in software engineering maturity models, though it is particularly consequential for platform engineering because organizations use these models to justify significant investment decisions. A platform team told by a maturity assessment that it is at “Level 2” has no objective basis for knowing what “Level 3” would require in terms of staffing, tooling, or organizational change, beyond the qualitative descriptions provided by the model authors.
Of the 38 sources (43%) addressing the maturity-productivity relationship, only three provide before-and-after evidence from real implementations; the remainder cite correlational survey data or describe aspirational maturity stages without operational definitions. This is concerning because maturity models justify organizational investment decisions. The CNCF model is cited most frequently (12 of 38 RQ5-relevant sources), yet it acknowledges that boundaries between levels are fuzzy and context-dependent.
A synthesized maturity model should integrate the CNCF's dimensional breadth with DORA's empirical grounding, measure both platform capabilities (supply side) and developer outcomes (demand side), and include explicit metrics at each level. Such a model should also account for organizational context, as regulated environments face different maturity barriers ( Salin et al., 2025) [S55] than commercial software organizations. Developing and validating such a model represents an important opportunity for future research.
5.3 Tool selection framework
The tool comparison in Table 5 and Figure 7 shows that no single tool spans all IDP components. Backstage dominates in adoption, community size, and extensibility, yet its plugin quality varies and operational overhead is non-trivial. Commercial offerings from Port, Cortex, and OpsLevel trade extensibility for reduced operational burden. Humanitec focuses on the platform orchestration layer, not the portal experience.
Tool selection should be driven by organizational maturity: early-stage PE initiatives may benefit from commercial tools with lower setup costs, while organizations with dedicated platform teams and mature platform engineering practices can leverage Backstage's extensibility. This mirrors the “thinnest viable platform” principle, where the right starting point depends on current capabilities, not aspirational architecture.
Tool mentions follow a power-law distribution across the 36 RQ2-relevant sources: Backstage appears in 23 sources, followed by Humanitec (12), Port (9), Crossplane (8), and ArgoCD (6). Backstage's dominance likely reflects its open-source status and CNCF incubation rather than technical superiority. Cloud-native Java teams required specialized IDP configurations that generic tools did not support ( Ghanta, 2025) [S44], and practitioner books supply extended guidance on architectural perspectives ( Körbächer et al., 2024; Salatino, 2024), enterprise adoption ( Peters and Pallapa, 2025; Leander, 2025), and comparative tool analyses ( Makani and Jangampeta, 2024; Kalluru, 2025). AI augmentation may represent the next frontier ( Padur, 2025) [S45], though empirical evidence for AI-enhanced IDP capabilities remains thin.
No controlled tool comparisons exist in the literature. Current evaluations, including this review's, rely on feature-list analysis, vendor documentation, and practitioner reports. A rigorous evaluation would compare developer outcomes across organizations using different IDP tools, controlling for organizational size, industry, and pre-existing DevOps maturity.
5.4 The academic–practitioner divide
The academic–practitioner divide documented across all five research questions warrants closer examination. In the 88 included sources, Tier C and D gray literature offers more practically useful platform engineering guidance than the combined Tier A and B literature. CNCF whitepapers define the canonical terminology. DORA surveys supply the statistical backbone. Vendor reports document adoption patterns. Academic papers, meanwhile, address adjacent topics (DevEx, DevOps metrics, and Team Topologies) instead of PE directly.
This pattern has implications for the software engineering research community. Platform engineering is not a minor practitioner trend. It marks a structural shift in how organizations manage developer infrastructure, supported by survey data from tens of thousands of respondents. The 2- to 3-year lag between practitioner adoption and academic engagement risks making eventual academic contributions irrelevant to practitioners who have already moved to the next concern.
The divide also creates an evidence quality problem. Without academic engagement, the claims most central to platform engineering's value proposition, that it improves productivity, reduces cognitive load, and accelerates delivery, rest on survey data collected by organizations with financial stakes in the outcomes. The DORA reports partially mitigate this concern through their scale and methodological rigor, but even DORA relies on self-reported survey responses rather than independent measurement. The theses from Tampere, Aalto, Innsbruck, and Padova represent the closest approximation to independent evaluation currently available, although their single-organization designs limit generalizability.
The temporal dynamics confirm the lag's magnitude: the first PE-specific peer-reviewed publication appeared in 2023 ( Dursun, 2023) [S1], approximately three years after Spotify open-sourced Backstage and the CNCF began formalizing PE terminology. By then, practitioners had already produced the CNCF Platforms White Paper, the Platform Engineering Maturity Model, four Humanitec State of PE volumes, and two DORA reports with PE-specific findings. While ( Garousi et al. 2019) identified similar patterns for DevOps and microservices, PE stands out because of the scale of the practitioner evidence base: the DORA 2024 survey alone represents 39,000 respondents, a sample size most academic SE studies cannot approach. The CNCF White Paper was developed through an open expert review process. These are methodologically structured documents that happen to originate outside the academic publishing system, and the SE research community might benefit from more systematic approaches to engaging with such evidence rather than treating the peer-review boundary as a quality proxy.
A parallel development that warrants attention is the growing integration of artificial intelligence into platform engineering workflows. Potential AI use cases in IDPs include code generation, automated testing suggestions, and intelligent documentation search ( Aslina and Nugraha, 2024) [S3]. A more comprehensive framework for AI-enabled infrastructure management from a platform engineering perspective has also been proposed ( Tadi and Mittal, 2025) [S54]. The Red Hat 2024 survey reported that 72% of organizations are exploring or implementing AI-augmented developer tools within their platforms ( Red Hat, 2024a). These claims remain unvalidated through controlled experiments, but the convergence of PE and AI represents a pressing near-term research opportunity.
5.5 Implications for practitioners
The synthesis yields several concrete implications. Organizations should start with a service catalog and self-service capabilities, the two components with the broadest evidence base, before expanding to scorecards and advanced automation. Measurement should combine DORA metrics (lagging, monthly), DevEx surveys (leading, quarterly), and platform-specific metrics (operational, weekly). Platform teams should be staffed with product management skills alongside engineering skills, given the persistent finding that product-oriented platforms outperform mandated infrastructure.
From twelve years of managing cloud infrastructure across enterprise environments, the practitioner experience of this author confirms a key theme: the organizations that succeeded with platform engineering invested in understanding developer workflows before building platform capabilities. A common failure pattern is “premature abstraction:” building elaborate golden paths before understanding which pain points warrant platform investment. The thinnest viable platform principle ( Skelton and Pais, 2019) addresses this, but its application requires product management discipline that many engineering-led platform teams lack.
Organizations in regulated industries should expect additional maturity barriers ( Salin et al., 2025) [S55], and those delivering product-service systems need an extended “DevServOps” model ( Dakkak et al., 2023) [S11] that accounts for bidirectional information flow. PE implementations should be tailored to the organizational delivery model, not adopted as a one-size-fits-all practice. Tool selection should resist feature-checklist evaluation: team size, existing ecosystem, and engineering culture all influence whether Backstage (high flexibility and high operational cost) or a commercial solution (lower operational cost and less customization) is appropriate.
Cognitive load measurement deserves explicit attention from platform teams. While cognitive load reduction is platform engineering's central value proposition, only 4 of the 88 reviewed sources attempt to measure cognitive load directly. Cognitive load has been documented in microservices environments ( Gangula, 2024), and cognitive load is one of three core DevEx dimensions ( Noda et al., 2023), yet operational methods for measuring cognitive load in platform engineering contexts are absent. Platform teams that track only delivery metrics (DORA) without measuring cognitive load are optimizing for the observable, not the essential.
5.6 Research agenda
This review identifies nine specific research opportunities, ordered by potential impact.
Validated PE maturity model: All existing models originate from gray literature. An empirically validated, academically rigorous maturity model is the single highest-impact research opportunity.
PE measurement framework: No PE-specific measurement instrument has been proposed or validated in academic literature. Adapting the DX Core 4 methodology to platform engineering contexts would be a concrete contribution.
Multi-organization case study: Published PE case studies are limited to single organizations. A comparative case study across organizations of different sizes, industries, and maturity levels would yield the first cross-context evidence.
Longitudinal adoption study: All current evidence is cross-sectional. Tracking organizations over two or more years of PE adoption would illuminate causal mechanisms.
PE definition consensus: The field lacks an agreed academic definition. A Delphi study among researchers and practitioners could establish a working consensus.
AI–PE integration evaluation: Claims about AI-enhanced IDPs are proliferating ( Aslina and Nugraha, 2024; Tadi and Mittal, 2025; Red Hat, 2024a) but remain empirically unvalidated. Controlled experiments comparing AI-augmented and traditional PE workflows are needed.
PE in regulated industries: Only ( Salin et al. 2025) examines PE in a regulated context. Multi-sector studies are needed to understand how compliance requirements affect PE adoption.
IDP tool comparison with empirical data: Current comparisons (including Table 5) are based on feature lists. Controlled experiments or matched-pair studies comparing IDP tools on developer outcomes would yield stronger evidence.
PE and developer burnout: ( Trinkenreich et al. 2023) developed a burnout model; measuring burnout reduction after PE adoption would connect PE to a growing research area.
5.7 Threats to validity
5.7.1 Internal validity
Gray literature sources carry vendor bias, which the AACODS assessment and explicit tiering mitigate but cannot eliminate. Negative platform engineering experiences are systematically underrepresented in the gray literature: vendors and foundations preferentially report positive adoption outcomes and market successes, while failed PE initiatives are rarely documented publicly. This survivorship bias means the corpus likely overestimates PE adoption success rates and underestimates implementation difficulty. The AACODS objectivity dimension partially accounts for this by scoring vendor neutrality, but cannot fully compensate for the structural absence of failure reports. As a single-author review, screening and extraction bias is present. Two-pass screening with a two-week interval achieved 97.9% self-agreement (140/143 sources), with the three disagreements limited to duplicate-entry corrections rather than substantive screening changes. This high consistency reduces the likelihood of inattentional screening errors, though it does not mitigate systematic biases that a second independent reviewer would catch. Future replications should consider recruiting a co-screener for at least 20% of sources to quantify inter-rater agreement.
5.7.2 External validity
As a qualitative synthesis, this review's generalizability rests on analytical generalization rather than statistical generalization ( Merriam, 2009). The findings are transferable to the extent that readers can assess the fit between the reviewed contexts and their own settings. To support this assessment, the review provides detailed source descriptions, explicit tiering, and per-source quality scores in the Supplementary material, enabling readers to judge the applicability of each finding to their organizational context ( Merriam, 1995). Platform engineering is a rapidly evolving field; findings represent a snapshot as of February 2026, and tool features, adoption rates, and organizational practices may have shifted by the time of publication. The corpus is dominated by sources from North American and European organizations, which limits transferability to other geographic or regulatory contexts. To increase external validity, the review triangulates findings across multiple independent sources and tiers: claims supported by both Tier A academic studies and Tier C industry surveys (e.g., the taxonomy of IDP components, the three-level metrics framework) carry stronger external validity than claims resting on a single source type.
5.7.3 Construct validity
The lack of a consensus definition for “platform engineering” means that the search strategy may over-include adjacent topics or miss sources using novel terminology. Five search string variants and snowball sampling mitigate this concern.
5.7.4 Selection validity
The 143 candidates represent deduplicated, title-screened sources from raw search results across five databases (Google Scholar alone returned approximately 2,400 results for the primary search string; other databases returned substantially fewer due to more restrictive indexing). The high inclusion rate (61.5%) reflects the specificity of the search terms (“platform engineering,” “internal developer portal”) rather than cherry-picking; sources matching these niche terms tend to be directly relevant. Comparable MLRs in emerging SE topics report similar pool sizes and inclusion rates.
5.7.5 Reliability
Source tiering introduces subjectivity in the assignment of Tier B vs. Tier A for borderline venues. The quality assessment scores, extraction data, and tier assignments are published as Supplementary material to enable replication and scrutiny.
5.7.6 Sensitivity analysis
To assess whether gray literature disproportionately influences the conclusions, findings were examined under a Tier A/B-only restriction (70 sources, excluding Tier C and D). The core taxonomy of IDP components, the three-level metrics framework structure, and the identification of adoption barriers all hold under this restriction, as they are supported by multiple peer-reviewed sources. The claims most sensitive to gray literature removal are the adoption statistics (94% PE adoption, 89% Backstage penetration), which originate exclusively from Tier C/D surveys. The maturity model comparison would be infeasible without gray literature, as all four models originate from practitioner sources. Pre-2020 references ( Forsgren et al., 2018; Skelton and Pais, 2019; Jabbari et al., 2016; Erich et al., 2017) fall outside the 2020–2026 search date range but are included as foundational background and methodology references, not as part of the reviewed corpus.
6 Conclusions
By synthesizing 88 academic and gray literature sources, this review mapped the current state of platform engineering and internal developer portals. The overarching finding is that practitioner knowledge far outpaces academic research: authoritative definitions, maturity models, and measurement frameworks originate from industry communities, not peer-reviewed venues.
The synthesis produced several tangible outputs. The study maps the building blocks of internal developer portals from 36 architecture-focused sources into a six-category component taxonomy. It bridges three measurement traditions, DORA delivery metrics, SPACE productivity dimensions, and developer experience surveys, into a unified evaluation approach. It compares four competing maturity models to expose where they converge and where they leave blind spots. It quantifies how far academic research trails practitioner knowledge, with only 2.3% of included sources from tier-1 venues. And it closes with nine prioritized research opportunities that target the field's most consequential evidence deficits. Together, these outputs give researchers a structural vocabulary for describing what IDPs contain, a measurement vocabulary for evaluating whether they work, and an assessment vocabulary for gauging organizational progress.
Practitioners reading this review should take away three points: platform engineering adoption succeeds when platforms are treated as products with dedicated product management, when measurement combines delivery metrics with developer experience surveys, and when golden paths function as enablers, not mandates.
The research community faces a different set of priorities. The highest-value opportunities are developing a validated PE maturity model, creating a PE-specific measurement instrument, and conducting longitudinal studies that can establish causal relationships between PE adoption and organizational outcomes. Among the nine research opportunities identified, three have particular urgency. The PE definition consensus problem (opportunity 5) impedes all other research because different definitions lead to different inclusion criteria, different comparison baselines, and different outcome measures. The absence of longitudinal evidence (opportunity 4) is the most fundamental methodological shortcoming, as cross-sectional surveys, no matter how large, cannot establish whether platform engineering drives better outcomes or whether better-performing organizations are simply more likely to invest in platforms. The AI-PE integration evaluation (opportunity 6) has time-sensitive relevance, as adoption is outpacing evidence at a rate that risks repeating the pattern this review documents for platform engineering itself: practitioners will have already moved to the next concern by the time academic evidence arrives.
Several limitations should be acknowledged alongside these contributions. The 88-source corpus, while comprehensive for this young field, is small compared to systematic reviews in established domains. The gray literature, despite AACODS assessment, carries vendor bias that cannot be fully eliminated through quality scoring. Single-author screening, despite 97.9% self-agreement across two passes, introduces consistency risks that dual screening would reduce. The temporal snapshot as of February 2026 means that specific tool capabilities and adoption rates may shift before publication.
Methodologically, restricting this study to peer-reviewed sources would have shrunk the corpus from 88 to 70 sources, excluding the most practice-relevant findings: CNCF definitions, maturity models, and adoption statistics from DORA and Puppet. The AACODS quality assessment and explicit tiering distinguish the MLR from an uncritical literature survey, and future reviews of emerging SE topics should adopt a similar approach.
Platform engineering is not a passing trend but a fundamental reorganization of how software organizations manage developer infrastructure. Whether academic research engages with this shift while it is still unfolding will determine its relevance to the professionals it aims to serve.
Statements
Data availability statement
The complete literature database (88 included sources with full quality scores, RQ mappings, and tier classifications), screening records for both passes, the AACODS scoring rubric, and figure-generation scripts are openly available at: https://github.com/mateenali66/pe-mlr-data, and archived at Zenodo: https://doi.org/10.5281/zenodo.18713861. The Supplementary Material accompanying this article contains the full per-source quality assessment scores and S/G identifier mapping.
Author contributions
MA: Conceptualization, Data curation, Formal analysis, Investigation, Methodology, Visualization, Writing – original draft, Writing – review & editing.
Funding
The author(s) declared that financial support was received for this work and/or its publication. The article processing charge was funded by Phono Technologies Inc. The funder was not involved in the study design, collection, analysis, interpretation of data, the writing of this article, or the decision to submit it for publication.
Acknowledgments
The author acknowledges the Cloud Native Computing Foundation TAG App Delivery working group for making the Platforms White Paper and Platform Engineering Maturity Model publicly available, and the DORA team at Google Cloud for publishing their survey methodology.
Conflict of interest
MA was employed by Phono Technologies Inc.
Generative AI statement
The author(s) declared that generative AI was used in the creation of this manuscript. Gemini (Google, https://gemini.google.com, model gemini-2.0-flash) was used to assist with literature search result deduplication, thematic coding verification, and manuscript drafting and editing. The author reviewed and edited all AI-generated content and takes full responsibility for the final manuscript.
Any alternative text (alt text) provided alongside figures in this article has been generated by Frontiers with the support of artificial intelligence and reasonable efforts have been made to ensure accuracy, including review by the authors wherever possible. If you identify any issues, please contact us.
Publisher's note
All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.
Supplementary material
The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fcomp.2026.1814498/full#supplementary-material
References
1 Ahmed W. Colomo-Palacios R. ( 2021). “Team topologies in software teams: a multivocal literature review,” in Proceedings of PROFES 2021, Lecture Notes in Computer Science ( Springer), 1– 2. doi: 10.1007/978-3-030-87013-3_21
CrossRef
Google Scholar
2 Arrulo T. ( 2024). The role of platform engineering in digital transformation. Master's thesis, ISTEC-Instituto Superior de Tecnologias Avançadas.
Google Scholar
3 Aslina Y. R. Nugraha I. G. B. B. ( 2024). “Exploring potential AI use cases in internal developer portals: A path to enhanced developer experience,” in Proceedings of the 2024 International Conference on Data Science and Engineering (ICODSE) ( IEEE). doi: 10.1109/ICoDSE63307.2024.10829893
CrossRef
Google Scholar
4 Bayer F. ( 2024). “How metamodeling concepts improve internal developer platforms and cloud platforms to foster business agility,” in Enterprise Architecture and Digital Transformation ( Springer). doi: 10.1007/978-3-031-56862-6_1
CrossRef
Google Scholar
5 Bhorkar G. ( 2023). Developing a software engineering team structure at a SaaS company. Master's thesis, Haaga-Helia University of Applied Sciences.
Google Scholar
6 Brown G. ( 2024). From paralysis to paved roads: How platform engineering resolves the cognitive crisis in DevOps and SRE. Google Cloud-Community (Medium).
Google Scholar
7 Chen W. Suo K. ( 2022). “Design and practice of DevOps platform via cloud native technology,” in Proceedings of IEEE ICSESS 2022. doi: 10.1109/ICSESS54813.2022.9930226
CrossRef
Google Scholar
8 Cheng L. Murphy-Hill E. Canning M. Jaspan C. Green C. Knight A. et al. ( 2022). “What improves developer productivity at Google? Code quality,” in Proceedings of the 30th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE 2022) ( ACM). doi: 10.1145/3540250.3558940
CrossRef
Google Scholar
9 Ciancarini P. Giancarlo R. Grimaudo G. Missiroli M. Xia T. C. ( 2025). The design and realization of a self-hosted and open-source agile internal development platform. IEEE Access13, 79516– 79533. doi: 10.1109/ACCESS.2025.3564141
CrossRef
Google Scholar
10 Cloud Native Computing Foundation ( 2024). CNCF annual survey 2024. Technical report, Cloud Native Computing Foundation.
Google Scholar
11 CNCFTAG App Delivery ( 2023a). CNCF platform engineering maturity model, version 1.0. Technical report, Cloud Native Computing Foundation,.
Google Scholar
12 CNCFTAG App Delivery ( 2023b). CNCF platforms white paper, version 1.0. Technical report, Cloud Native Computing Foundation.
Google Scholar
13 CNCFTAG App Delivery ( 2024). Platform engineering in 2024: Industry trends. CNCF TAG Blog.
Google Scholar
14 Combemale B. ( 2025). Towards a science of developer experience (DevX). arXiv preprint arXiv:2506.23715. doi: 10.5381/jot.2025.24.1.a2
CrossRef
Google Scholar
15 Cruzes D. S. Dybå T. ( 2011). “Recommended steps for thematic synthesis in software engineering,” in Proceedings of the 5th International Symposium on Empirical Software Engineering and Measurement (ESEM) ( IEEE), 275– 284. doi: 10.1109/ESEM.2011.36
CrossRef
Google Scholar
16 Cuadra J. Hurtado E. Sarachaga I. Estevez E. Casquero O. Armentia A. ( 2024). Enabling DevOps for fog applications in the smart manufacturing domain: a model-driven based platform engineering approach. Future Gener. Comput. Syst. 157, 360– 375. doi: 10.1016/j.future.2024.03.053
CrossRef
Google Scholar
17 Dakkak A. Bosch J. Olsson H. H. ( 2023). “DevServOps: DevOps for product-oriented product service systems,” in Proceedings of IEEE SEAA 2023. doi: 10.1109/SEAA60479.2023.00057
CrossRef
Google Scholar
18 DeBellis D. Storer K. Lewis A. Good B. Villalba D. Maxwell E. et al. ( 2024). Accelerate state of DevOps report 2024. Technical report, DORA, Google Cloud.
Google Scholar
19 Donner W. ( 2023). Improving developer experience of the development infrastructure. Master's thesis, Aalto University.
Google Scholar
20 Dursun H. ( 2023). “Full spec software via platform engineering,” in Proceedings of the 27th International Conference on Evaluation and Assessment in Software Engineering (EASE '23) ( ACM). doi: 10.1145/3593434.3593440
CrossRef
Google Scholar
21 Erich F. M. A. Amrit C. Daneva M. ( 2017). A qualitative study of DevOps usage in practice. Evol. Proc. 29: e1885. doi: 10.1002/smr.1885
CrossRef
Google Scholar
22 Forsgren N. Humble J. Kim G. ( 2018). Accelerate: The Science of Lean Software and DevOps: Building and Scaling High Performing Technology Organizations. Portland: IT Revolution Press.
Google Scholar
23 Forsgren N. Kalliamvakou E. Noda A. Greiler M. Houck B. Storey M.-A. ( 2024). DevEx in action. Commun. ACM67, 46– 53. doi: 10.1145/3643140
CrossRef
Google Scholar
24 Forsgren N. Storey M.-A. Maddila C. Zimmermann T. Houck B. Butler J. ( 2021). The SPACE of developer productivity. ACM Queue19, 20– 48. doi: 10.1145/3454122.3454124
CrossRef
Google Scholar
25 Franch López E. ( 2024). Centralizing software development: Production-ready Backstage portal. Master's thesis, Universitat Oberta de Catalunya.
Google Scholar
26 Galante L. ( 2023). Luca galante on platform engineering. IEEE Softw. 40, 87– 89. doi: 10.1109/MS.2023.3236832
CrossRef
Google Scholar
27 Gangula A. K. ( 2024). Reducing cognitive load in complex hybrid systems: the role of microservices architecture in simplifying developer experience. Int. J. Latest Res. Publish. 5: 1788. doi: 10.70528/IJLRP.v5.i3.1788
CrossRef
Google Scholar
28 Garousi V. Felderer M. Mäntylä M. V. ( 2019). Guidelines for including grey literature and conducting multivocal literature reviews in software engineering. Inf. Softw. Technol. 106, 101– 121. doi: 10.1016/j.infsof.2018.09.006
CrossRef
Google Scholar
29 Gartner ( 2024). Hype cycle for platform engineering, 2024. Technical report, Gartner.
Google Scholar
30 Ghanbari H. Terimaa T. Koskinen K. ( 2025). Using development environment as code for enhancing developer experience: an action design research study. J. Syst. Softw. 236: 112803. doi: 10.1016/j.jss.2026.112803
CrossRef
Google Scholar
31 Ghanta S. ( 2025). Engineering productivity at scale: Designing IDPs for cloud-native Java teams. ResearchGate Preprint.
Google Scholar
32 Golis T. Dakić P. ( 2024). “Creating a self-service DevOps platform for black-box testing on Kubernetes,” in Proceedings of the Ninth International Congress on Information and Communication Technology (ICICT 2024) ( Springer). doi: 10.1007/978-981-97-3305-7_28
CrossRef
Google Scholar
33 Gomes A. ( 2024). Deploy-oriented specification of cloud native applications. Master's thesis, Universidade do Porto.
Google Scholar
34 Google Cloud ( 2024a). Golden paths for engineering execution consistency. Google Cloud Blog.
Google Scholar
35 Google Cloud ( 2024b). Platform engineering research report. Technical report, Google Cloud.
Google Scholar
36 Greiler M. Storey M.-A. Noda A. ( 2022). An actionable framework for understanding and improving developer experience. IEEE Trans. Softw. Eng. 49, 1411– 1425. doi: 10.1109/TSE.2022.3175660
CrossRef
Google Scholar
37 Guisao Y. Suescún E. Noreña P. Pardo C. ( 2025). Towards platform engineering, the evolution of DevOps-a systematic mapping. J. Softw. 38: e70108. doi: 10.22541/au.175311016.61108565/v1
CrossRef
Google Scholar
38 Guthardt J. Kosiol J. Hohlfeld O. ( 2024). “Low-code vs. the developer: an empirical study on DevEx and efficiency,” in Companion Proceedings of the ACM/IEEE 27th International Conference on Model Driven Engineering Languages and Systems (MODELS '24) ( ACM). doi: 10.1145/3652620.3688332
CrossRef
Google Scholar
39 Humanitec ( 2022). State of platform engineering, volume 1. Technical report, Humanitec.
Google Scholar
40 Humanitec ( 2023). State of platform engineering, volume 2. Technical report, Humanitec.
Google Scholar
41 Humanitec ( 2024). State of platform engineering, volume 3. Technical report, Humanitec.
Google Scholar
42 Humanitec ( 2025). State of platform engineering, volume 4. Technical report, Humanitec.
Google Scholar
43 Jabbari R. bin Ali N. Petersen K. Tanveer B. ( 2016). “What is DevOps? A systematic mapping study on definitions and practices,” in Proceedings of the Scientific Workshop Proceedings of XP2016 ( ACM). doi: 10.1145/2962695.2962707
CrossRef
Google Scholar
44 Jaspan C. Green C. ( 2022). A human-centered approach to developer productivity. IEEE Softw. 40, 23– 28. doi: 10.1109/MS.2022.3212165
CrossRef
Google Scholar
45 Kalluru V. ( 2025). Accelerating microservice delivery: A framework for enterprise-grade IDPs. Authorea Preprint. doi: 10.22541/au.175649112.20052731/v1
CrossRef
Google Scholar
46 Kaul S. Nhu K. Eissayou J. Eser I. Borup V. ( 2025). SpaceX: exploring metrics with the SPACE model. arXiv preprint arXiv:2511.20955.
Google Scholar
47 Kawalerowicz M. Pietranik M. ( 2025). “A systematic approach to measuring developer productivity: the Prismetrix method,” in Proceedings of ICCCI 2025, Lecture Notes in Artificial Intelligence ( Springer). doi: 10.1007/978-3-032-09318-9_23
CrossRef
Google Scholar
48 Kitchenham B. Charters S. ( 2007). Guidelines for performing systematic literature reviews in software engineering. Technical Report EBSE-2007–01, Keele University and Durham University.
Google Scholar
49 Körbächer M. Grabner A. Lipsig H. ( 2024). Platform Engineering for Architects. Birmingham: Packt/Sciendo.
Google Scholar
50 Koskinen L. ( 2024). Setting productivity metrics for automation development teams. Master's thesis, Aalto University.
Google Scholar
51 Kreuzberger D. Kühl N. Hirschl S. ( 2023). Machine learning operations (MLOps): overview, definition, and architecture. IEEE Access11, 31866– 31879. doi: 10.1109/ACCESS.2023.3262138
CrossRef
Google Scholar
52 Kumar A. Nadeem M. Shameem M. ( 2025). A systematic literature review for investigating DevOps metrics to implement in software development organizations. J. Softw. 37: e2733. doi: 10.1002/smr.2733
CrossRef
Google Scholar
53 Labonté-Lamoureux A.-X. Boyer S. ( 2025). Automatic pipeline provisioning. arXiv preprint arXiv:2511.14825.
Google Scholar
54 Laredo Velázquez L. d. J. ( 2023). Using portals to improve the developer experience. Master's thesis, Tampere University.
Google Scholar
55 Leander K. R. ( 2025). Developer Experience Unleashed. Cham: Apress/Springer. doi: 10.1007/979-8-8688-0242-3
CrossRef
Google Scholar
56 Makani S. T. Jangampeta S. ( 2024). A comparative study of platform engineering tools. ResearchGate.
Google Scholar
57 Merriam S. B. ( 1995). What can you tell from an N of 1?: issues of validity and reliability in qualitative research. PAACE J. Lifelong Learn. 4, 51– 60.
Google Scholar
58 Merriam S. B. ( 2009). Qualitative Research: A Guide to Design and Implementation. San Francisco, CA: Jossey-Bass, 3rd edition.
Google Scholar
59 Mishra A. Otaiwi Z. ( 2020). DevOps and software quality: a systematic mapping. Comput. Sci. Rev. 38: 100308. doi: 10.1016/j.cosrev.2020.100308
CrossRef
Google Scholar
60 Morelius J. ( 2024). Advancing developer experiences: Evaluating in developer portals. Master's thesis, KTH Royal Institute of Technology.
Google Scholar
61 Mori V. S. Kittlaus H.-B. ( 2025). “A framework for managing platforms as products in IT organizations,” in Software-Intensive Business, Lecture Notes in Business Information Processing ( Springer). doi: 10.1007/978-3-031-71515-0_5
CrossRef
Google Scholar
62 Nazo R. ( 2024). Design and development of a self-service platform for automating infrastructure provisioning. Master's thesis, University of Padova.
Google Scholar
63 Nieminen V. ( 2024). Internal developer platform. Master's thesis, Tampere University.
Google Scholar
64 Noda A. Storey M.-A. Forsgren N. Greiler M. ( 2023). DevEx: What actually drives productivity. ACM Queue66, 44– 49. doi: 10.1145/3595878
CrossRef
Google Scholar
65 Noda A. Tacho L. Storey M.-A. Greiler M. ( 2024). Measuring Developer Productivity with the DX Core 4. Technical report, DX ( getdx.com). Available online at: https://getdx.com/research/measuring-developer-productivity-with-the-dx-core-4/ (Accessed February 16, 2026).
Google Scholar
66 Noel R. Panach J. I. Pastor O. ( 2023). “Using team topologies in model-driven strategic alignment,” in Proceedings of CIbSE 2023. doi: 10.5753/cibse.2023.24701
CrossRef
Google Scholar
67 Nylund A. ( 2020). A multivocal literature review on developer experience. Master's thesis, Aalto University.
Google Scholar
68 Padur S. ( 2025). AI augmented platform engineering. ResearchGate Preprint.
Google Scholar
69 Palomino P. Fonseca M. Souza J. Toda A. Pereira R. L. Cordeiro T. ( 2024). Enhancing developers experience (DevEx) for successful design system implementation. Int. J. Hum.-Comput. Inter. 41, 807– 819. doi: 10.1080/10447318.2024.2304912
CrossRef
Google Scholar
70 Peters M. Pallapa G. ( 2025). Mastering Enterprise Platform Engineering. Birmingham: Packt.
Google Scholar
71 Pettersson M. ( 2025). Developer productivity: factors affecting productivity and team performance. Master's thesis, Karlstad University.
Google Scholar
72 Plant O. H. Aldea A. van Hillegersberg J. ( 2025). Improving DevOps team performance through context-capability coalignment: towards a profile for public sector organizations. Inf. Softw. Technol. 178: 107585. doi: 10.1016/j.infsof.2024.107585
CrossRef
Google Scholar
73 PlatformEngineering.org ( 2024). Platform as a product: The key to platform engineering success. PlatformEngineering.org.
Google Scholar
74 Port ( 2024). State of internal developer portals 2024. Technical report, Port.
Google Scholar
75 Puppet by Perforce ( 2024). State of DevOps report 2024: The evolution of platform engineering. Technical report, Puppet by Perforce.
Google Scholar
76 Razzaq A. Botterweck G. Lai Q. Buckley J. ( 2025a). Empirical pathways to developer experience: Facet-based synthesis. J. Syst. Softw. 233: 112648. doi: 10.1016/j.jss.2025.112648
CrossRef
Google Scholar
77 Razzaq A. Buckley J. Lai Q. Yu T. Botterweck G. ( 2025b). A systematic literature review on the influence of enhanced developer experience on developers' productivity: factors, practices, and recommendations. ACM Comput. Surv. 57, 1– 46. doi: 10.1145/3687299
CrossRef
Google Scholar
78 Red Hat ( 2024a). The state of platform engineering in the age of AI. Technical report, Red Hat.
Google Scholar
79 Red Hat ( 2024b). What is a golden path for software development? Technical report, Red Hat.
Google Scholar
80 Riihimäki R. ( 2024). Productivity metrics and their integration into DevOps. Master's thesis, University of Turku.
Google Scholar
81 Ruegger J. Kropp M. Graf S. Anslow C. ( 2024). “Fully automated DORA metrics measurement for continuous improvement,” in Proceedings of the International Conference on Software and System Processes (ICSSP 2024) ( ACM). doi: 10.1145/3666015.3666020
CrossRef
Google Scholar
82 Sadowski C. Zimmermann T. ( 2019). Rethinking Productivity in Software Engineering. Cham: Apress/Springer. doi: 10.1007/978-1-4842-4221-6
CrossRef
Google Scholar
83 Salatino M. ( 2024). Platform Engineering on Kubernetes. Shelter Island, NY: Manning.
Google Scholar
84 Salin H. Klotins E. Zabardast E. ( 2025). “Hindrances and strengths in software delivery: insights from a developer experience study at the swedish transport administration,” in Proceedings of PROFES 2025, Lecture Notes in Computer Science ( Springer). doi: 10.1007/978-3-032-12092-2_8
CrossRef
Google Scholar
85 Sallin M. Kropp M. Anslow C. Quilty J. Meier A. ( 2021). “Measuring software delivery performance using the four key metrics of DevOps,” in Agile Processes in Software Engineering and Extreme Programming (XP 2021), Lecture Notes in Business Information Processing ( Springer). doi: 10.1007/978-3-030-78098-2_7
CrossRef
Google Scholar
86 Seremet V. Rakić K. ( 2022). “Platform engineering and site reliability engineering: The path to DevOps success,” in DAAAM International Scientific Book ( DAAAM International), 155– 162. doi: 10.2507/daaam.scibook.2022.13
CrossRef
Google Scholar
87 Skelton M. Pais M. ( 2019). Team Topologies: Organizing Business and Technology Teams for Fast Flow. Portland: IT Revolution Press.
Google Scholar
88 Skelton M. Pais M. ( 2024). Team Topologies: Five Years of Transforming Organizations. Portland: IT Revolution.
Google Scholar
89 Soeldner J.-H. Ajouaoui L. Fritzsche A. Soeldner G. ( 2023). “Platform engineering for cloud-native organizations,” in Proceedings of the 5th International Conference Business Meets Technology (BMT 2023) ( Editorial Universitat Politécnica de Valéncia). doi: 10.4995/BMT2023.2023.16741
CrossRef
Google Scholar
90 Spotify Engineering ( 2020). Backstage: An open platform for building developer portals. Spotify Engineering Blog.
Google Scholar
91 Srinivasan V. Rajkumar M. Santhanam S. Garg A. ( 2025). PlatFab: a platform engineering approach to improve developer productivity. J. Inf. Syst. Eng. Bus. Intell. 11, 79– 90. doi: 10.20473/jisebi.11.1.79-90
CrossRef
Google Scholar
92 Stack Overflow ( 2024). Stack overflow developer survey 2024. Stack Overflow Annual Survey.
Google Scholar
93 Storey M.-A. Zimmermann T. Bird C. Czerwonka J. Murphy B. Kalliamvakou E. ( 2021). Towards a theory of software developer job satisfaction and perceived productivity. IEEE Trans. Softw. Eng. 47, 2125– 2142. doi: 10.1109/TSE.2019.2944354
CrossRef
Google Scholar
94 Tadi G. Mittal A. ( 2025). “AI-enabled infrastructure management: a comprehensive framework and empirical analysis from platform engineering perspective,” in Proceedings of IEEE CARS 2025 ( IEEE). doi: 10.1109/CARS67163.2025.11337561
CrossRef
Google Scholar
95 The New Stack ( 2023). How to pave golden paths that actually go somewhere. Technical paper, The New Stack.
Google Scholar
96 The New Stack ( 2024). Q &A: How team topologies supports platform engineering. Technical paper, The New Stack.
Google Scholar
97 Tilak S. Patni S. Gargav S. Shah A. ( 2020). “A platform for enhancing application developer productivity using microservices and micro-frontends,” in Proceedings of IEEE HYDCON 2020 ( IEEE). doi: 10.1109/HYDCON48903.2020.9242913
CrossRef
Google Scholar
98 Trinkenreich B. Stol K.-J. Steinmacher I. Gerosa M. A. Sarma A. Tamburri D. A. et al. ( 2023). “A model for understanding and reducing developer burnout,” in Proceedings of the 45th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP 2023) ( IEEE). doi: 10.1109/ICSE-SEIP58684.2023.00010
CrossRef
Google Scholar
99 Tunggono J. Princes E. ( 2025). “Understanding developer productivity: input-output perspectives within the SPACE framework,” in Proceedings of IEEE ICCAI 2025. doi: 10.1109/ICCAI65301.2025.11279703
CrossRef
Google Scholar
100 Tyndall J. ( 2010). AACODS checklist for appraising grey literature. Flinders University.
Google Scholar
101 Valiulla A. ( 2025a). Comparative analysis of engineering performance frameworks: DORA, SPACE, HEART. SSRN Preprint. doi: 10.2139/ssrn.5335258
CrossRef
Google Scholar
102 Valiulla R. ( 2025b). Developer experience measurement in the age of AI. SSRN Preprint. doi: 10.2139/ssrn.5316738
CrossRef
Google Scholar
103 van de Kamp R. Bakker K. Zhao Z. ( 2024). “Paving the path towards platform engineering using a comprehensive reference model,” in Service-Oriented Computing-ICSOC 2023 Workshops, Lecture Notes in Computer Science ( Springer). doi: 10.1007/978-3-031-54712-6_11
CrossRef
Google Scholar
104 Vasilevskii A. Kachur O. ( 2024). “Self-service performance testing platform for autonomous development teams,” in Companion of the 15th ACM/SPEC International Conference on Performance Engineering (ICPE '24) ( ACM). doi: 10.1145/3629527.3652268
CrossRef
Google Scholar
105 Wang W.-J. ( 2025). “Platform-centric agile transformation,” in Proceedings of IEEE ICCBE 2025 ( IEEE).
Google Scholar
106 Waqas M. Ali Z. Sánchez-Gordón M. Kristiansen M. ( 2024). “Using low-code and no-code tools in DevOps: a multivocal literature review,” in Springer LNCS ( Springer). doi: 10.1007/978-3-031-50590-4_5
CrossRef
Google Scholar
107 Wilkes B. Milani A. M. P. Storey M.-A. ( 2023). “A framework for automating the measurement of DevOps research and assessment (DORA) metrics,” in Proceedings of the 39th IEEE International Conference on Software Maintenance and Evolution (ICSME 2023) ( IEEE). doi: 10.1109/ICSME58846.2023.00018
CrossRef
Google Scholar
108 Winkler L. ( 2025). Beyond DevOps: Leveraging platform engineering to surpass the challenges of traditional DevOps practices. Master's thesis, University of Innsbruck.
Google Scholar
Summary
Keywords
cloud-native, developer experience, developer productivity, DevOps, internal developer portal, multivocal literature review, platform engineering, service catalog
Citation
Anjum MA (2026) Platform engineering and internal developer portals: a multivocal literature review. Front. Comput. Sci. 8:1814498. doi: 10.3389/fcomp.2026.1814498
Received
20 February 2026
Revised
24 March 2026
Accepted
08 April 2026
Published
04 May 2026
Volume
8 - 2026
Edited by
Mohammad Alshayeb, King Fahd University of Petroleum and Minerals, Saudi Arabia
Reviewed by
Mohamed Wiem Mkaouer, University of Michigan–Flint, United States
Ítalo Belo, Federal Rural University of Pernambuco, Brazil
Updates 
Check for updates
Copyright
© 2026 Anjum.
This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.
Correspondence: Mateen Ali Anjum, mateen@phonotech.ca
Disclaimer
All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article or claim that may be made by its manufacturer is not guaranteed or endorsed by the publisher.
Editor & Reviewers
Edited by
M A Mohammad Alshayeb
Reviewed by
M W Mohamed Wiem Mkaouer
Í B Ítalo Belo
High-impact AI
AI playbook for researchers
Your step by step support for responsible and impactful AI use
Explore the guide
[Published in Frontiers in Computer Science
Software
2.7 impact factor
5.3 citescore](https://www.frontiersin.org/journals/computer-science)
Article metrics
View details
497
Views
31
Downloads
Download PDF
Download other formats
ReadCube
epub
XML
Cite article Share article
PDF Download other format
ReadCube
epub
XML
Outline
Figures
Cite
Share
Metrics
Suppl. material
More
Cite
Share
Metrics
Suppl. material
Abstract
1 Introduction
2 Background
3 Methodology
4 Results
5 Discussion
6 Conclusions
Data availability statement
Author contributions
Funding
Acknowledgments
Conflict of interest
Generative AI statement
Publisher's note
Supplementary material
References
Figures and Tables
Figure 1 View in article
Figure 2 View in article
Figure 3 View in article
Figure 4 View in article
Figure 5 View in article
Figure 6 View in article
Figure 7 View in article
Figure 8 View in article
Table 1 Gray literature sources and their characteristics. View in article
Table 2 Inclusion and exclusion criteria. View in article
Table 3 Quality assessment score summary by tier. View in article
Table 4 Representative included studies by tier (selected from 88 sources). View in article
Table 5 Feature comparison of major IDP tools across key capability dimensions. View in article
Table 6 Operationalization of platform engineering success metrics across three levels. View in article
Copy to clipboard
Citation
Anjum MA (2026) Platform engineering and internal developer portals: a multivocal literature review. Front. Comput. Sci. 8:1814498. doi: 10.3389/fcomp.2026.1814498
Copy citation
Export citation file
BibTex
EndNote
Reference Manager
Simple Text file
Facebook
X
LinkedIn
[](mailto:?subject=Interesting science article: Platform engineering and internal developer portals: a multivocal literature review&body=Hi!!%0D%0A%0D%0AI think you might find interesting the article "Platform engineering and internal developer portals: a multivocal literature review".%0D%0A%0D%0AYou can read more about it here: https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full)[Email](mailto:?subject=Interesting science article: Platform engineering and internal developer portals: a multivocal literature review&body=Hi!!%0D%0A%0D%0AI think you might find interesting the article "Platform engineering and internal developer portals: a multivocal literature review".%0D%0A%0D%0AYou can read more about it here: https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full)
WeChat
Data Sheet 1.csv 
Guidelines
Author guidelines
Services for authors
Policies and publication ethics
Editor guidelines
Fee policy
Explore
Articles
Research Topics
Journals
How we publish
Outreach
Frontiers Forum
Frontiers Policy Labs
Frontiers for Young Minds
Frontiers Planet Prize
Connect
Help center
Emails and alerts
Contact us
Submit
Career opportunities
Follow us    
© 2026 Frontiers Media SA. All rights reserved.
Privacy policy | Terms and conditions | Accessibility statement
Share on WeChat
Scan with WeChat to share this article 
We use cookies
Our website uses cookies that are essential for its operation and additional cookies to track performance, or to improve and personalize our services. To manage your cookie preferences, please click Cookie Settings. For more information on how we use cookies, please see our Cookie Policy
Cookies Settings Reject non-essential cookies Accept cookies 
Privacy Preference Center
Our website uses cookies that are necessary for its operation. Additional cookies are only used with your consent. These cookies are used to store and access information such as the characteristics of your device as well as certain personal data (IP address, navigation usage, geolocation data) and we process them to analyse the traffic on our website in order to provide you a better user experience, evaluate the efficiency of our communications and to personalise content to your interests. Some cookies are placed by third-party companies with which we work to deliver relevant ads on social media and the internet. Click on the different categories' headings to change your cookie preferences. If you wish to learn more about how we use cookies, please see our cookie policy below.
Cookie Policy
Allow all
Manage Consent Preferences
Strictly Necessary Cookies
Always Active
These cookies are necessary for our websites to function as they enable you to navigate around the sites and use our features. They cannot be switched off in our systems. They are activated set in response to your actions such as setting your privacy preferences, logging-in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work.
Performance/Analytics Cookies
[x]
Performance/Analytics Cookies
These cookies allow us to collect information about how visitors use our website, including the number of visitors, the websites that referred them to our website, and the pages that they visited. We use them to compile reports, to measure and improve the performance of our website, analyze which pages are the most viewed, see how visitors move around the site and fix bugs. If you do not allow these cookies, your experience will not be altered but we will not be able to improve the performance and content of our website.
Targeting/Advertising Cookies
[x]
Targeting/Advertising Cookies
These cookies may be set by us to offer your personalized content and opportunities to cooperate. They may also be used by social media companies we work with to build a profile of your interests and show you relevant adverts on their services. They do not store directly personal information but are based on unique identifiers related to your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Cookie List
Clear [-]
checkbox label label
Apply Cancel
Consent Leg.Interest [-]
checkbox label label [-]
checkbox label label [-]
checkbox label label
Confirm My Choices
          
