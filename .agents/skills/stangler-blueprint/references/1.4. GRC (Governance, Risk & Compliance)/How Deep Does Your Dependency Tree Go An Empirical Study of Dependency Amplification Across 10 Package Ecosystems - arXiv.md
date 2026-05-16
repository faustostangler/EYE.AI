---
name: How Deep Does Your Dependency Tree Go? An Empirical Study of Dependency Amplification Across 10 Package Ecosystems - arXiv
keywords: (placeholder)
metadata:
  url: https://arxiv.org/html/2512.14739v1
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T19:00:57.430Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
How Deep Does Your Dependency Tree Go? An Empirical Study of Dependency Amplification Across 10 Package Ecosystems
 Back to arXiv  
 Back to arXiv
This is experimental HTML to improve accessibility. We invite you to report rendering errors. Use Alt+Y to toggle on accessible reporting links and Alt+Shift+Y to toggle off. Learn more about this project and help improve conversions.
Why HTML? Report Issue Back to Abstract Download PDF 
Table of Contents
Abstract
1 Introduction
2 Dataset Overview
2.1 Ecosystem Selection
2.2 Data Collection
2.3 Dependency Resolution
2.4 Ecosystem Characteristics
3 RQ1: Dependency Amplification Across Ecosystems
3.1 Methodology for RQ1
3.2 Answer to RQ1
4 RQ2: Supply Chain Exposure and Propagation Scope
4.1 Methodology for RQ2
4.2 Answer to RQ2
5 RQ3: Ecosystem Design Factors Explaining Amplification Differences
5.1 Methodology for RQ3
5.2 Answer to RQ3
6 Discussion
6.1 Implications
6.2 Threats to Validity
7 Related Work
8 Conclusion
License: arXiv.org perpetual non-exclusive license
arXiv:2512.14739v1 [cs.SE] 12 Dec 2025
How Deep Does Your Dependency Tree Go? An Empirical Study of Dependency Amplification Across 10 Package Ecosystems
Report issue for preceding element
Jahidul Arafat jza0145@auburn.edu Auburn University Auburn Alabama USA
Report issue for preceding element
Abstract.
Report issue for preceding element
Modern software development relies on package ecosystems where declaring a single dependency can introduce dozens of additional transitive packages. This dependency amplification, defined as the ratio of transitive to direct dependencies, has critical implications for software supply chain security, yet no prior work compares amplification patterns across ecosystems at scale. We present an empirical study of 500 projects across 10 major package ecosystems: Maven Central for Java, npm Registry for JavaScript, crates.io for Rust, PyPI for Python, NuGet Gallery for .NET, RubyGems for Ruby, Go Modules for Go, Packagist for PHP, CocoaPods for Swift/Objective-C, and Pub for Dart. Our analysis reveals that Maven exhibits mean amplification of 24.70 times compared to 4.48 times for Go Modules, 4.32 times for npm, and 0.32 times for CocoaPods. We find significant differences with large effect sizes in 22 of 45 pairwise comparisons. These findings challenge prevailing assumptions that npm's preference for small, single-purpose packages leads to the highest amplification. We find that 28% of Maven projects exhibit amplification exceeding 10 times, indicating elevated amplification is systematic rather than outlier-driven, compared to 14% for RubyGems, 12% for npm, and 0% for Cargo, PyPI, Packagist, CocoaPods, and Pub. We trace these differences to ecosystem design choices including dependency resolution strategies, standard library comprehensiveness, and platform constraints. Our findings suggest practitioners should implement ecosystem-specific security strategies: systematic transitive dependency auditing for Maven environments given 28% of projects exceed 10 times amplification, targeted outlier identification for npm and RubyGems projects, and continued standard practices for the five ecosystems with controlled amplification. We provide a replication package with data for 500 projects and analysis scripts.
Report issue for preceding element † †
conference: ; ; † † copyright: none
1. Introduction
Report issue for preceding element
Modern software development relies on package ecosystems to accelerate development and reduce duplication of effort. Developers declare dependencies on external libraries, leveraging functionality ranging from simple utilities to complex frameworks. However, each declared dependency brings with it a cascade of transitive dependencies. The term transitive dependencies refers to packages required by the direct dependency and its own dependencies, resolved recursively ( decan2019empirical; cox2019surviving; kikas2017structure) . This phenomenon, which we term dependency amplification, has implications for software security and maintenance.
Report issue for preceding element
The software supply chain has emerged as a critical attack vector. High-profile incidents such as the event-stream compromise ( ohm2020backstabber) , ua-parser-js malware injection ( ladisa2023sok) , and Log4Shell vulnerability ( wetter2022forensic) demonstrate how vulnerabilities in transitive dependencies can cascade through the software ecosystem. When a developer adds a single dependency, they implicitly trust not only that package but also dozens to hundreds of transitive packages ( zimmermann2019small) , each representing a potential attack surface. Figure 1 illustrates how a single Maven project declaring 8 direct dependencies expands to include over 100 additional packages through transitive relationships.
Report issue for preceding element
Figure 1. Dependency specification from a typical Maven project. The project directly requires 8 packages, but these bring over 100 additional transitive dependencies. A single Spring Boot dependency transitively depends on dozens of other packages including web servers, JSON processors, and database connectors. Updating any package in this chain can trigger cascading version changes throughout the dependency tree. Report issue for preceding element
Despite growing awareness of supply chain risks, dependency amplification patterns remain uncharacterized across ecosystems using consistent methodology. Conventional wisdom suggests that the npm ecosystem leads to extreme dependency proliferation due to its culture of small, single-purpose packages ( abdalkareem2017why) . However, this assumption lacks empirical validation across multiple ecosystems with consistent methodology and sufficient statistical power. Prior studies have examined individual ecosystems including npm ( zimmermann2019small; chinthanet2021lags) , Maven ( soto2021comprehensive; benelallam2019maven) , PyPI ( alfadel2023empirical) , Cargo ( he2023empirical) , and others, but cross-ecosystem comparison of amplification patterns remains limited. No prior work has examined amplification patterns across 10 or more diverse ecosystems representing different language families, platform targets, and design philosophies.
Report issue for preceding element
This paper presents an empirical study of dependency amplification across 10 major package ecosystems representing widely-used programming languages and platforms in modern software development. We analyze Maven Central for Java, npm Registry for JavaScript, crates.io for Rust, PyPI for Python, NuGet Gallery for .NET, RubyGems for Ruby, Go Modules for Go, Packagist for PHP, CocoaPods for Swift/Objective-C, and Pub for Dart. Together they represent diverse design philosophies from enterprise frameworks to platform-constrained development, from dynamic scripting languages to statically-typed systems languages, and from small single-purpose package designs to comprehensive framework architectures.
Report issue for preceding element
We answer the following research questions:
Report issue for preceding element
• RQ1: How does dependency amplification vary across 10 major package ecosystems? Report issue for preceding element
• RQ2: What are the supply chain exposure and propagation scope implications of transitive dependency growth across diverse ecosystems? Report issue for preceding element
• RQ3: What ecosystem characteristics and design factors explain amplification differences? Report issue for preceding element
Our key findings challenge prevailing assumptions about ecosystem amplification profiles and reveal fundamental patterns in dependency management. First, Maven exhibits higher amplification at 24.70 times compared to most ecosystems, with large effect sizes that are significant at the 0.05 level. This contradicts expectations that npm's culture of small, single-purpose packages leads to the highest amplification. Second, amplification patterns diverge across ecosystems where Maven shows 28% of projects with amplification exceeding 10 times while 5 of 10 ecosystems show 0% at this threshold. Third, ecosystem design choices impact amplification where platform constraints and standard library comprehensiveness correlate with lower amplification. Fourth, hierarchical clustering reveals Maven occupies an isolated position with extreme amplification while most ecosystems cluster together with controlled amplification below 5 times, suggesting current security frameworks may require ecosystem-specific strategies rather than uniform approaches.
Report issue for preceding element
These findings have practical implications for security practitioners and tool developers. Enterprise Java environments may require more aggressive transitive dependency auditing than previously assumed ( plate2015impact; pashchenko2018vulnerable) , while five ecosystems including PyPI, Cargo, and Packagist demonstrate that controlled amplification is achievable through careful design choices ( amann2018study) . The discovery that npm's actual amplification at 4.32 times falls far below Maven's 24.70 times suggests security investment priorities may need substantial revision.
Report issue for preceding element
Contributions. We list our contributions as follows:
Report issue for preceding element
• Comprehensive quantification of dependency amplification patterns across 10 major package ecosystems representing diverse language families, platform targets, and design philosophies, with 500 analyzed projects providing robust statistical power. Report issue for preceding element
• Identification of dramatic ecosystem divergence in supply chain exposure profiles where Maven shows 28% of projects with amplification exceeding 10 times compared to 0% for five ecosystems, with hierarchical clustering revealing Maven's isolated position. Report issue for preceding element
• Discovery that platform constraints and ecosystem design choices correlate with amplification patterns, with Maven at 24.70 times versus CocoaPods at 0.32 times demonstrating a 77-fold difference between highest and lowest amplification ecosystems. Report issue for preceding element
• Analysis of ecosystem design factors including dependency resolution strategies, zero-dependency prevalence, correlation structures, and variance metrics explaining observed amplification patterns. Report issue for preceding element
• Complete replication package with dependency data for 500 projects across 10 ecosystems, statistical analysis scripts, and visualization code available for future research. Report issue for preceding element
2. Dataset Overview
Report issue for preceding element
We provide context on the analyzed package ecosystems in this section. Table 1 summarizes the mathematical notation used throughout this paper.
Report issue for preceding element
Table 1. Summary of Notation
Report issue for preceding element
2.1. Ecosystem Selection
Report issue for preceding element
We selected 10 major package ecosystems representing diverse language families and application domains. Maven Central serves as the primary repository for Java artifacts, supporting enterprise applications, Android development, and backend services. The npm Registry is the largest package ecosystem by package count, serving both frontend and backend JavaScript development. The Cargo registry at crates.io serves the Rust programming community that emphasizes safety and performance. PyPI hosts Python packages dominating data science, machine learning, and scientific computing. NuGet Gallery provides packages for .NET languages across multiple platforms. RubyGems serves the Ruby community. Go Modules manages dependencies for Go emphasizing standard library usage. Packagist provides PHP packages for web development. CocoaPods manages dependencies for Swift and Objective-C in Apple ecosystem development. Pub serves Dart and Flutter development focused on mobile and web UI.
Report issue for preceding element
These ecosystems differ in their dependency management approaches. Maven uses XML-based project definitions with explicit version constraints and scope declarations for compile, test, and runtime dependencies. The npm ecosystem uses JSON-based manifest files with semantic versioning ranges and distinguishes between production dependencies, development dependencies, and peer dependencies. Cargo uses TOML-based manifests with strict version resolution and a lock file mechanism, which records exact dependency versions to ensure reproducible builds. Other ecosystems employ distinct manifest formats, version resolution strategies, and dependency scoping mechanisms.
Report issue for preceding element
2.2. Data Collection
Report issue for preceding element
We collected 50 projects from each ecosystem totaling 500 projects. Table 2 summarizes dataset characteristics and technical specifications. Projects were sampled from popular packages to ensure relevance and representativeness.
Report issue for preceding element
Table 2. Dataset and Ecosystem Characteristics Characteristic Maven npm Cargo PyPI NuGet RubyGems Go Packagist CocoaPods Pub
Report issue for preceding element
For Maven, we sampled projects from Maven Central's most-downloaded artifacts including framework components and enterprise utilities. For npm, we sampled packages from the registry's most-depended-upon packages including framework ecosystem components, utility libraries, and build tools. For Cargo, we sampled crates from crates.io's most-downloaded crates including async runtimes, serialization libraries, and web frameworks. For PyPI, we sampled popular packages spanning scientific computing, web frameworks, and machine learning libraries. For other ecosystems, we sampled from frequently-used packages representing diverse application domains.
Report issue for preceding element
2.3. Dependency Resolution
Report issue for preceding element
For each project, we measured two types of dependencies following established terminology in dependency analysis research ( decan2019empirical; kikas2017structure) . Direct dependencies are packages explicitly declared in the project's manifest file. Transitive dependencies are all packages recursively required by direct dependencies, resolved using native package manager tooling to ensure accurate version resolution and conflict handling.
Report issue for preceding element
We used each ecosystem's native dependency resolution tooling to ensure measurements reflect actual installed packages. This approach accounts for version resolution, conflict mediation, and platform-specific dependencies. For Maven projects, we extracted complete dependency trees including compile-scope and runtime-scope dependencies. For npm packages, we resolved all production dependencies, development dependencies, and peer dependencies. For Cargo crates, we resolved normal dependencies, development dependencies, and build dependencies. For other ecosystems, we used native tooling to resolve complete dependency trees.
Report issue for preceding element
2.4. Ecosystem Characteristics
Report issue for preceding element
Maven projects declare fewer direct dependencies with mean of 5.4 but accumulate more transitive dependencies. The npm projects declare the most direct dependencies with mean of 30.9 reflecting the ecosystem's composition-focused design. Cargo projects show moderate direct dependency counts with mean of 13.7 and controlled transitive dependency accumulation. PyPI and NuGet show conservative dependency patterns with means of 4.2 and 3.9 direct dependencies respectively. CocoaPods demonstrates minimal external dependency usage with mean of only 0.5 direct dependencies.
Report issue for preceding element
These characteristics reflect fundamental design differences. Maven's ecosystem favors comprehensive frameworks providing extensive functionality through single dependencies. The npm ecosystem favors small focused packages following the Unix philosophy of doing one thing well. Cargo's ecosystem emphasizes safety and explicit dependency management with strict version resolution preventing ambiguous package selection. CocoaPods faces platform constraints where most functionality comes from system frameworks rather than external packages.
Report issue for preceding element
3. RQ1: Dependency Amplification Across Ecosystems
Report issue for preceding element
We provide the methodology and results in Sections 3.1 and 3.2.
Report issue for preceding element
3.1. Methodology for RQ1
Report issue for preceding element
We analyzed 500 projects across 10 ecosystems with 50 projects per ecosystem. For each project, we extracted dependency information from manifest files and resolved complete dependency trees using native package manager tooling.
Report issue for preceding element
Our analysis involved three steps. First, we extracted manifest files from each project repository. For Maven projects, we parsed pom.xml files to identify declared dependencies. For npm packages, we parsed package.json files to identify production dependencies, development dependencies, and peer dependencies. For Cargo crates, we parsed Cargo.toml files to identify normal dependencies, development dependencies, and build dependencies. For PyPI packages, we parsed setup.py or pyproject.toml files. For NuGet projects, we parsed .csproj or packages.config files. For RubyGems, we parsed Gemfile specifications. For Go Modules, we parsed go.mod files. For Packagist packages, we parsed composer.json files. For CocoaPods, we parsed Podfile specifications. For Pub packages, we parsed pubspec.yaml files.
Report issue for preceding element
Second, we resolved complete dependency trees using native package manager tooling. This step identifies all transitive dependencies by recursively resolving each direct dependency's own requirements. We used Maven's dependency resolution for Java projects, npm's package installation for JavaScript projects, Cargo's dependency resolution for Rust projects, and analogous native tooling for all remaining ecosystems. Using native tooling ensures accurate version resolution accounting for conflict mediation and platform-specific dependencies.
Report issue for preceding element
Third, we computed dependency metrics for each project. Let p p denote a project and 𝒫 \mathcal{P} denote the set of all projects in an ecosystem. We define the following dependency sets:
Report issue for preceding element
• D d  i  r  e  c  t  ( p ) D_{direct}(p) : Set of packages explicitly declared in the manifest file of project p p Report issue for preceding element
• D t  r  a  n  s  i  t  i  v  e  ( p ) D_{transitive}(p) : Set of packages recursively required by direct dependencies but not explicitly declared Report issue for preceding element
• D t  o  t  a  l  ( p ) D_{total}(p) : Complete dependency footprint where D t  o  t  a  l  ( p ) = D d  i  r  e  c  t  ( p ) ∪ D t  r  a  n  s  i  t  i  v  e  ( p ) D_{total}(p)=D_{direct}(p)\cup D_{transitive}(p) Report issue for preceding element
We define the amplification factor α \alpha as the ratio of transitive to direct dependencies following prior work on dependency analysis ( zimmermann2019small) :
Report issue for preceding element
(1)
α  ( p ) = | D t  r  a  n  s  i  t  i  v  e  ( p ) | max  ( | D d  i  r  e  c  t  ( p ) | , 1 ) \alpha(p)=\frac{|D_{transitive}(p)|}{\max(|D_{direct}(p)|,1)}
This metric captures how a single declared dependency expands into multiple installed packages. We use the maximum of direct dependencies and one to handle projects with zero direct dependencies. An amplification factor of α = 10 \alpha=10 indicates that each direct dependency brings 10 transitive packages.
Report issue for preceding element
Given the non-normal distribution of dependency counts confirmed by Shapiro-Wilk tests with all p-values below 0.001, we employ non-parametric statistical methods following established guidelines for software engineering experiments ( arcuri2011practical) .
Report issue for preceding element
For omnibus comparison across all 10 ecosystems, we use the Kruskal-Wallis H-test which evaluates whether samples originate from the same distribution:
Report issue for preceding element
(2)
H = 12 N  ( N + 1 )  ∑ i = 1 k R i 2 n i − 3  ( N + 1 ) H=\frac{12}{N(N+1)}\sum_{i=1}^{k}\frac{R_{i}^{2}}{n_{i}}-3(N+1)
where N N is the total sample size, k k is the number of groups, n i n_{i} is the sample size of group i i , and R i R_{i} is the sum of ranks for group i i .
Report issue for preceding element
For pairwise ecosystem comparisons, we use Mann-Whitney U tests with Holm-Bonferroni correction for multiple comparisons. With 10 ecosystems we perform 45 pairwise comparisons. We compute Cliff's delta δ \delta for effect size estimation ( cliff1993dominance) :
Report issue for preceding element
(3)
δ = | { ( x i , y j ) : x i > y j } | − | { ( x i , y j ) : x i < y j } | n 1 ⋅ n 2 \delta=\frac{|{(x_{i},y_{j}):x_{i}>y_{j}}|-|{(x_{i},y_{j}):x_{i}<y_{j}}|}{n_{1}\cdot n_{2}}
where x i x_{i} are observations from group 1, y j y_{j} are observations from group 2, and n 1 n_{1} , n 2 n_{2} are respective sample sizes. We interpret effect sizes following Romano et al ( romano2006appropriate) : | δ | < 0.147 |\delta|<0.147 as negligible, | δ | < 0.33 |\delta|<0.33 as small, | δ | < 0.474 |\delta|<0.474 as medium, and | δ | ≥ 0.474 |\delta|\geq 0.474 as large. We report 95% confidence intervals computed via bootstrap resampling with 10,000 iterations.
Report issue for preceding element
3.2. Answer to RQ1
Report issue for preceding element
Table 3 presents descriptive statistics for dependency counts and amplification factors across ecosystems.
Report issue for preceding element
Table 3. Dependency Characteristics Across 10 Ecosystems
Report issue for preceding element
Maven exhibits the highest amplification with mean of 24.70 times, indicating that a Maven project declaring 5.4 direct dependencies installs 74.9 transitive packages. This finding contradicts conventional expectations that npm's preference for small, single-purpose packages leads to the highest amplification. The npm ecosystem shows mean amplification of 4.32 times, tied with RubyGems at 4.32 times. Go Modules shows amplification of 4.48 times despite its minimalist standard library philosophy. Pub demonstrates moderate amplification at 2.61 times while NuGet shows 2.32 times.
Report issue for preceding element
PyPI exhibits controlled amplification at 1.50 times, Packagist shows 1.24 times, and Cargo demonstrates amplification below unity at 0.97 times indicating transitive dependencies barely exceed direct declarations. CocoaPods shows the lowest amplification at only 0.32 times, reflecting platform constraints where most functionality comes from system frameworks.
Report issue for preceding element
The Kruskal-Wallis H-test confirms significant differences across ecosystems with H statistic of 150.90 and p-value of 5.74 × 10 − 28 5.74\times 10^{-28} . Table 4 presents pairwise comparisons with effect sizes.
Report issue for preceding element
Table 4. Pairwise Ecosystem Comparisons for Amplification
Report issue for preceding element
Maven differs from all other ecosystems with large effect sizes for comparisons against CocoaPods with Cliff's delta of 0.750, against Cargo with delta of 0.634, and against npm with delta of 0.494. The comparison between Maven and npm represents the contrast between the two ecosystems often considered to have highest amplification. Maven's higher amplification challenges assumptions about npm being the primary concern.
Report issue for preceding element
Figure 2 visualizes amplification distributions. Maven shows not only higher median amplification but also extreme outliers with maximum amplification reaching 198.5 times. The 95th percentile for Maven at 112.7 times far exceeds Go Modules at 13.9 times, npm at 22.1 times, and all remaining ecosystems.
Report issue for preceding element 
Figure 2. Dependency amplification distribution across 10 ecosystems. Maven exhibits significantly higher amplification with extreme outliers reaching 198.5 times. Cargo and CocoaPods maintain controlled amplification below 4 times. Report issue for preceding element
Distribution shapes differ across ecosystems. Maven's amplification distribution shows high positive skewness indicating a long right tail with extreme values. The npm and Go Modules ecosystems show even higher variance reflecting heterogeneous package composition. Cargo, PyPI, Packagist, and Pub demonstrate more controlled distributions. CocoaPods shows the most constrained distribution with maximum amplification of only 2.0 times.
Report issue for preceding element
Table 5 presents extended statistics with confidence intervals and percentile information.
Report issue for preceding element
Table 5. Extended Amplification Statistics
Report issue for preceding element
The wide confidence intervals for Maven and npm reflect high variance in these ecosystems. Maven's 95% confidence interval spans from 11.8 to 40.9 times. CocoaPods shows a narrow interval from 0.1 to 0.5 times indicating consistent low amplification across projects. PyPI and Packagist similarly show narrow confidence intervals reflecting consistent behavior.
Report issue for preceding element
Answer to RQ1: Maven exhibits higher dependency amplification at 24.70 times compared to Go Modules at 4.48 times, npm at 4.32 times, RubyGems at 4.32 times, and Cargo at 0.97 times. CocoaPods shows the lowest amplification at 0.32 times. These differences are significant at the 0.05 level with large effect sizes in 22 of 45 pairwise comparisons. Maven's amplification reaches extreme values up to 198.5 times while Cargo and CocoaPods maintain controlled amplification below 4 times. These findings challenge assumptions that npm's culture of small, single-purpose packages leads to the highest amplification.
Report issue for preceding element
4. RQ2: Supply Chain Exposure and Propagation Scope
Report issue for preceding element
We provide the methodology and results in Sections 4.1 and 4.2.
Report issue for preceding element
4.1. Methodology for RQ2
Report issue for preceding element
We analyze supply chain exposure and propagation scope using formal metrics for attack surface, concentration ratios, and vulnerability propagation potential. While we do not analyze specific CVEs, these metrics quantify the extent of code trust and the potential scope of impact if vulnerabilities occur.
Report issue for preceding element
We define the attack surface 𝒜 \mathcal{A} of a project p p as the total number of distinct packages that must be trusted:
Report issue for preceding element
(4)
𝒜  ( p ) = | D t  o  t  a  l  ( p ) | = | D d  i  r  e  c  t  ( p ) | + | D t  r  a  n  s  i  t  i  v  e  ( p ) | \mathcal{A}(p)=|D_{total}(p)|=|D_{direct}(p)|+|D_{transitive}(p)|
Each package in D t  o  t  a  l  ( p ) D_{total}(p) represents code that executes within the application context, creating potential sources of vulnerabilities, malicious code injection, or maintenance abandonment.
Report issue for preceding element
We analyze amplification distribution by comparing mean and maximum attack surfaces to distinguish consistent versus outlier-driven patterns. Let μ 𝒜  ( E ) \mu_{\mathcal{A}}(E) denote mean attack surface and max 𝒜  ( E ) \max_{\mathcal{A}}(E) denote maximum attack surface for ecosystem E E . We define the concentration ratio:
Report issue for preceding element
(5)
𝒞  ( E ) = max 𝒜  ( E ) μ 𝒜  ( E ) \mathcal{C}(E)=\frac{\max_{\mathcal{A}}(E)}{\mu_{\mathcal{A}}(E)}
High concentration ratio indicates amplification concentrated in outliers while low ratio indicates consistent amplification across projects.
Report issue for preceding element
We model vulnerability propagation potential using the impact function ℐ \mathcal{I} . When a vulnerability occurs in package v v , the number of affected projects depends on both direct and transitive usage:
Report issue for preceding element
(6)
ℐ  ( v , E ) = ∑ p ∈ E 𝟙  [ v ∈ D t  o  t  a  l  ( p ) ] \mathcal{I}(v,E)=\sum_{p\in E}\mathbb{1}[v\in D_{total}(p)]
where 𝟙  [ ⋅ ] \mathbb{1}[\cdot] is the indicator function. We estimate expected propagation by multiplying direct dependents by mean amplification: if package v v has d d direct dependents, the estimated total affected projects is d ⋅ α ¯  ( E ) d\cdot\bar{\alpha}(E) where α ¯  ( E ) \bar{\alpha}(E) is the mean amplification factor for ecosystem E E .
Report issue for preceding element
For statistical analysis of exposure metrics, we use non-parametric tests given the non-normal distributions. We compute percentiles at 90th, 95th, and 99th levels to characterize distribution tails where supply chain risks concentrate. We report bootstrap confidence intervals for prevalence estimates.
Report issue for preceding element
To visualize amplification distribution patterns, we compute cumulative distribution functions (CDFs) for amplification factors. The CDF F  ( x ) F(x) represents the proportion of projects with amplification factor less than or equal to x x :
Report issue for preceding element
(7)
F  ( x ) = P  ( α  ( p ) ≤ x ) = | { p ∈ E : α  ( p ) ≤ x } | | E | F(x)=P(\alpha(p)\leq x)=\frac{|{p\in E:\alpha(p)\leq x}|}{|E|}
Steep CDF curves indicate consistent low amplification while gradual curves with long tails indicate substantial proportions of high-amplification projects.
Report issue for preceding element
4.2. Answer to RQ2
Report issue for preceding element
Table 6 presents attack surface and supply chain exposure metrics across ecosystems.
Report issue for preceding element
Table 6. Attack Surface and Supply Chain Exposure Analysis
Report issue for preceding element
Maven shows consistently elevated attack surfaces with mean of 80.3 packages. This means the average Maven project trusts code from over 80 distinct packages, each representing potential sources of vulnerabilities, malicious code, or maintenance issues. The npm ecosystem shows similar mean attack surface at 83.7 packages but higher maximum at 785 packages indicating extreme outliers.
Report issue for preceding element
The concentration ratio 𝒞 \mathcal{C} quantifies whether amplification is systematic or outlier-driven. The npm ecosystem shows concentration ratio of 𝒞 n  p  m = 9.4 \mathcal{C}{npm}=9.4 indicating amplification concentrated in extreme outliers. Maven shows concentration ratio of 𝒞 m  a  v  e  n = 5.6 \mathcal{C}{maven}=5.6 indicating more systematic amplification distribution. Cargo shows 𝒞 c  a  r  g  o = 6.6 \mathcal{C}{cargo}=6.6 while CocoaPods shows 𝒞 c  o  c  o  a  p  o  d  s = 10.0 \mathcal{C}{cocoapods}=10.0 , both reflecting occasional outliers in otherwise controlled ecosystems.
Report issue for preceding element
Maven exhibits 28% of projects with amplification exceeding 10 times compared to 14% for RubyGems, 12% for npm, and 0% for five ecosystems including Cargo, PyPI, Packagist, CocoaPods, and Pub. This finding indicates Maven's elevated amplification is systematic rather than concentrated in outliers. Figure 3 visualizes this pattern showing Maven's steep amplification slope.
Report issue for preceding element 
Figure 3. Direct versus total dependencies across 10 ecosystems. Maven and RubyGems show steep amplification slopes indicating systematic elevated amplification. The npm ecosystem shows higher variance with some projects reaching extreme values while others maintain moderate totals. Cargo, PyPI, and Packagist maintain controlled linear growth across all projects. Report issue for preceding element
The npm ecosystem shows the largest maximum attack surface at 785 packages from a single project, exceeding Maven's maximum of 450 packages. However, npm's mean attack surface remains comparable to Maven indicating that extreme cases are outliers rather than typical behavior. This distinction has practical implications: npm's elevated amplification can be managed by identifying specific high-amplification packages while Maven requires systematic auditing across most projects.
Report issue for preceding element
Cargo and five other ecosystems maintain controlled attack surfaces with 0% of projects exceeding 10 times amplification. Even at the 95th percentile, Cargo's attack surface of 132.4 packages and PyPI's of 30.2 packages remain moderate compared to Maven's 397.2 packages. This controlled behavior suggests these ecosystems' designs limit transitive dependency growth.
Report issue for preceding element
Figure 4 shows cumulative distribution functions of amplification factors. CocoaPods and Cargo show steep rise indicating consistent low amplification across projects. Maven shows gradual rise with long tail indicating substantial portion of projects with high amplification. The npm ecosystem shows intermediate pattern with most projects below 10 times amplification but extreme outliers.
Report issue for preceding element 
Figure 4. Cumulative distribution functions of amplification factor across 10 ecosystems. Cargo and CocoaPods show steep rise indicating consistent low amplification. Maven and RubyGems show gradual rise with long tail. The npm ecosystem shows bimodal pattern with concentration at low amplification but extreme outliers. Report issue for preceding element
Answer to RQ2: Maven exhibits elevated supply chain exposure with 28% of projects showing amplification exceeding 10 times, compared to 14% for RubyGems, 12% for npm, and 0% for five ecosystems. While npm shows the largest maximum attack surface at 785 packages, its elevated amplification concentrates in outliers rather than typical projects. Propagation scope is highest in Maven where a single vulnerable package can affect over 24 times more projects than direct dependency counts suggest. Cargo, PyPI, Packagist, CocoaPods, and Pub maintain controlled attack surfaces with no projects exceeding 10 times amplification.
Report issue for preceding element
5. RQ3: Ecosystem Design Factors Explaining Amplification Differences
Report issue for preceding element
We provide the methodology and results in Sections 5.1 and 5.2.
Report issue for preceding element
5.1. Methodology for RQ3
Report issue for preceding element
We investigated ecosystem characteristics that may explain the observed amplification differences through three analytical approaches: zero-dependency analysis, correlation analysis, and ecosystem design examination.
Report issue for preceding element
For zero-dependency analysis, we define the zero-dependency indicator function:
Report issue for preceding element
(8)
𝒵  ( p ) = 𝟙  [ | D d  i  r  e  c  t  ( p ) | = 0 ] \mathcal{Z}(p)=\mathbb{1}[|D_{direct}(p)|=0]
Zero-dependency packages represent self-contained functionality with no external requirements. We compute zero-dependency prevalence for ecosystem E E as:
Report issue for preceding element
(9)
𝒵 E = ∑ p ∈ E 𝒵  ( p ) | E | \mathcal{Z}{E}=\frac{\sum{p\in E}\mathcal{Z}(p)}{|E|}
We report bootstrap 95% confidence intervals for prevalence estimates and test for ecosystem differences using chi-square test for independence.
Report issue for preceding element
For correlation analysis, we compute Spearman's rank correlation coefficient ρ \rho between direct and transitive dependency counts:
Report issue for preceding element
(10)
ρ = 1 − 6  ∑ i = 1 n d i 2 n  ( n 2 − 1 ) \rho=1-\frac{6\sum_{i=1}^{n}d_{i}^{2}}{n(n^{2}-1)}
where d i d_{i} is the difference between ranks of paired observations and n n is sample size. Strong positive correlation indicates predictable amplification where direct dependency counts reliably predict transitive growth. Weak correlation indicates unpredictable amplification where direct counts provide limited information about total footprint.
Report issue for preceding element
We define the predictability ratio 𝒫 \mathcal{P} as the correlation between direct and total dependencies:
Report issue for preceding element
(11)
𝒫  ( E ) = ρ  ( | D d  i  r  e  c  t | , | D t  o  t  a  l | )  for  p ∈ E \mathcal{P}(E)=\rho(|D_{direct}|,|D_{total}|)\text{ for }p\in E
High predictability ratio near 1.0 indicates developers can estimate supply chain exposure from direct dependency counts alone.
Report issue for preceding element
For variance analysis, we compute coefficient of variation to measure consistency within ecosystems:
Report issue for preceding element
(12)
C  V  ( E ) = σ α  ( E ) μ α  ( E ) CV(E)=\frac{\sigma_{\alpha}(E)}{\mu_{\alpha}(E)}
where σ α  ( E ) \sigma_{\alpha}(E) and μ α  ( E ) \mu_{\alpha}(E) are standard deviation and mean of amplification factors in ecosystem E E . High C  V CV indicates heterogeneous amplification patterns while low C  V CV indicates consistent behavior across projects.
Report issue for preceding element
We also compute the Gini coefficient G G to measure inequality in total dependency distribution within each ecosystem. The Gini coefficient ranges from 0 (perfect equality where all projects have identical dependency counts) to 1 (perfect inequality where one project has all dependencies):
Report issue for preceding element
(13)
G  ( E ) = ∑ i = 1 n ∑ j = 1 n | D t  o  t  a  l  ( p i ) − D t  o  t  a  l  ( p j ) | 2  n 2  D ¯ G(E)=\frac{\sum_{i=1}^{n}\sum_{j=1}^{n}|D_{total}(p_{i})-D_{total}(p_{j})|}{2n^{2}\bar{D}}
where n = | E | n=|E| is the number of projects in ecosystem E E and D ¯ \bar{D} is the mean total dependency count. High Gini coefficient indicates a few projects dominate the dependency landscape while most remain lightweight.
Report issue for preceding element
For ecosystem design analysis, we examine how package manager architecture influences amplification. We analyze version resolution strategies, dependency scope distinctions, and lock file practices across ecosystems. We also perform hierarchical clustering using Ward's linkage method with Euclidean distance on standardized amplification metrics to identify natural ecosystem groupings.
Report issue for preceding element
5.2. Answer to RQ3
Report issue for preceding element
Table 7 presents zero-dependency analysis results.
Report issue for preceding element
Table 7. Zero-Dependency Package Analysis
Report issue for preceding element
CocoaPods shows the highest proportion of zero-dependency packages at 𝒵 c  o  c  o  a  p  o  d  s = 76.0 % \mathcal{Z}{cocoapods}=76.0% reflecting platform constraints where most functionality comes from Apple system frameworks rather than external packages. The npm ecosystem shows 𝒵 n  p  m = 40.0 % \mathcal{Z}{npm}=40.0% and Go Modules shows 𝒵 g  o = 36.0 % \mathcal{Z}{go}=36.0% consistent with preferences for small, single-purpose utilities that often have no dependencies. Maven shows moderate zero-dependency prevalence at 𝒵 m  a  v  e  n = 28.0 % \mathcal{Z}{maven}=28.0% while Cargo and Packagist show lowest at 𝒵 c  a  r  g  o = 𝒵 p  a  c  k  a  g  i  s  t = 10.0 % \mathcal{Z}{cargo}=\mathcal{Z}{packagist}=10.0% . The chi-square test for ecosystem differences is significant with χ 2 = 91.4 \chi^{2}=91.4 and p < 0.001 p<0.001 .
Report issue for preceding element
Zero-dependency packages contribute to ecosystem amplification patterns. When a package has zero direct dependencies, its amplification is zero by our formula. This partially explains why npm's average of 4.32 times remains lower than Maven's 24.70 times despite npm's reputation for deep dependency trees. However, zero-dependency prevalence alone cannot explain all differences as Maven shows 28.0% zero-dependency packages yet maintains highest amplification.
Report issue for preceding element
Table 8 presents correlation analysis results.
Report issue for preceding element
Table 8. Correlation Between Direct and Transitive Dependencies
Report issue for preceding element
Maven shows the weakest correlation between direct and transitive dependencies with ρ m  a  v  e  n = 0.196 \rho_{maven}=0.196 which is not significant at the 0.05 level. This weak correlation indicates Maven's transitive dependency growth is unpredictable from direct dependency counts. Adding one dependency to a Maven project may introduce varying numbers of transitive packages depending on which framework components are included.
Report issue for preceding element
CocoaPods shows the strongest correlation with ρ c  o  c  o  a  p  o  d  s = 0.950 \rho_{cocoapods}=0.950 indicating predictable amplification behavior. PyPI shows ρ p  y  p  i = 0.906 \rho_{pypi}=0.906 and Go Modules shows ρ g  o = 0.838 \rho_{go}=0.838 , both indicating strong predictability. Cargo shows ρ c  a  r  g  o = 0.681 \rho_{cargo}=0.681 indicating moderate-to-strong predictability. These ecosystems demonstrate that predictable amplification is achievable through careful design.
Report issue for preceding element
We also examined the predictability ratio 𝒫 \mathcal{P} measuring correlation between direct and total dependencies. CocoaPods shows near-perfect predictability with 𝒫 c  o  c  o  a  p  o  d  s = 0.989 \mathcal{P}{cocoapods}=0.989 indicating total dependency footprint is highly predictable from direct dependencies. PyPI shows 𝒫 p  y  p  i = 0.947 \mathcal{P}{pypi}=0.947 and Cargo shows 𝒫 c  a  r  g  o = 0.894 \mathcal{P}{cargo}=0.894 . Maven's weak predictability at 𝒫 m  a  v  e  n = 0.433 \mathcal{P}{maven}=0.433 means direct dependency counts provide limited information about actual supply chain exposure.
Report issue for preceding element
Table 9 presents variance analysis showing amplification consistency within ecosystems.
Report issue for preceding element
Table 9. Amplification Variance by Ecosystem
Report issue for preceding element
The npm ecosystem shows highest coefficient of variation at C  V n  p  m = 272 % CV_{npm}=272% reflecting extreme heterogeneity where amplification ranges from zero to 76.2 times. Maven shows C  V m  a  v  e  n = 245 % CV_{maven}=245% and RubyGems shows C  V r  u  b  y  g  e  m  s = 217 % CV_{rubygems}=217% indicating high variability. Pub shows the lowest coefficient of variation at C  V p  u  b = 70 % CV_{pub}=70% followed by Packagist at C  V p  a  c  k  a  g  i  s  t = 98 % CV_{packagist}=98% and PyPI at C  V p  y  p  i = 101 % CV_{pypi}=101% indicating more consistent amplification patterns across projects.
Report issue for preceding element
Figure 5 presents a heatmap visualization of ecosystem characteristics showing normalized values for key dependency metrics. The heatmap reveals clear clustering where Maven exhibits extreme values for transitive dependencies and amplification while CocoaPods shows minimal external dependency usage. PyPI, Packagist, and Cargo form a moderate cluster with balanced characteristics.
Report issue for preceding element 
Figure 5. Heatmap of normalized ecosystem characteristics across five metrics: mean direct dependencies, mean transitive dependencies, mean amplification, Gini coefficient, and zero-dependency percentage. Darker colors indicate higher normalized values. Maven shows extreme amplification and transitive dependency characteristics. CocoaPods demonstrates minimal dependency footprint. Color intensity reveals natural ecosystem clustering with Maven isolated and most ecosystems forming a controlled-amplification cluster. Report issue for preceding element
Hierarchical clustering analysis reveals natural ecosystem groupings. Figure 6 shows the clustering dendrogram where Maven occupies an isolated position representing high amplification and high unpredictability. Most other ecosystems cluster together representing controlled amplification. The npm ecosystem shows intermediate position reflecting its variable nature.
Report issue for preceding element 
Figure 6. Hierarchical clustering dendrogram of 10 ecosystems based on dependency characteristics using Ward's linkage method. Maven occupies an isolated position reflecting extreme amplification and unpredictability. Most other ecosystems cluster together representing controlled amplification patterns. The npm ecosystem shows intermediate position reflecting high variance. Report issue for preceding element
Ecosystem design philosophy impacts amplification patterns. Maven's ecosystem evolved to support enterprise Java development where frameworks like Spring provide comprehensive functionality. A single Spring dependency can include dozens of modules covering web serving, data access, security, and other enterprise concerns. This comprehensive approach maximizes developer convenience but amplifies transitive dependencies in ways that are difficult to predict.
Report issue for preceding element
The npm ecosystem culture favors small focused packages following the philosophy of doing one thing well. While this can lead to deep dependency trees in some cases, it also means many packages are leaf nodes with zero or few dependencies. The high variance in npm reflects this heterogeneous ecosystem where some packages have zero dependencies while others accumulate hundreds.
Report issue for preceding element
CocoaPods faces platform constraints from Apple's development requirements where most functionality comes from system frameworks rather than external packages. This constraint controls amplification with mean of only 0.32 times. PyPI benefits from Python's comprehensive standard library, which provides substantial functionality and reduces external dependency needs, contributing to controlled amplification at 1.50 times.
Report issue for preceding element
Cargo's strict version resolution with unified dependency specifications and compilation-time dependency checking enforces discipline. Features including optional dependencies and feature flags allow fine-grained control over what gets compiled. This design constrains amplification with maximum of only 3.9 times.
Report issue for preceding element
Go Modules emphasizes standard library usage and minimalist external dependencies. The language philosophy discourages excessive external dependencies, though some projects still accumulate substantial transitive dependencies leading to moderate amplification at 4.48 times.
Report issue for preceding element
Answer to RQ3: Ecosystem design choices impact amplification patterns. Maven's enterprise-oriented architecture leads to high unpredictable amplification with weak correlation between direct and transitive dependencies at rho of 0.196. The npm ecosystem's preference for small, single-purpose packages creates high variance with coefficient of variation at 272% including both zero-dependency packages and deep trees. CocoaPods demonstrates platform constraints can control amplification to 0.32 times with strong predictability. PyPI, Packagist, and Cargo show that controlled amplification below 1.5 times is achievable through comprehensive standard libraries, pragmatic design, and strict dependency models respectively. Hierarchical clustering reveals Maven occupies an isolated position with extreme amplification while most ecosystems cluster together with controlled amplification. These findings demonstrate that language-level and ecosystem-level design choices can mitigate supply chain risks.
Report issue for preceding element
6. Discussion
Report issue for preceding element
We discuss the implications of our findings and threats to validity in Sections 6.1 and 6.2.
Report issue for preceding element
6.1. Implications
Report issue for preceding element
Implications for Practitioners on Ecosystem-Specific Security Strategies. Our findings suggest practitioners should adopt ecosystem-specific approaches to dependency security rather than uniform policies across all projects.
Report issue for preceding element
For Maven projects, our findings indicate elevated amplification requiring comprehensive auditing. With 28% of projects showing amplification exceeding 10 times and weak correlation between direct and transitive dependencies at rho of 0.196, practitioners cannot predict supply chain exposure from direct dependency counts alone. Organizations heavily invested in Java development should implement transitive dependency auditing tools that examine complete dependency trees rather than only direct declarations. Software Bill of Materials generation should be standard practice for Maven projects given mean attack surfaces of 80.3 packages.
Report issue for preceding element
For RubyGems projects, our findings suggest elevated attention with 14% of projects showing amplification exceeding 10 times. While lower than Maven, RubyGems shows substantial amplification at 4.32 times and weak predictability at rho of 0.368. Practitioners working in Ruby environments should implement dependency auditing focusing on projects that declare multiple framework dependencies.
Report issue for preceding element
For npm projects, our findings suggest targeted auditing focusing on outlier identification. While npm shows 12% of projects with amplification exceeding 10 times and the largest maximum attack surface at 785 packages, typical projects show mean amplification of 4.32 times comparable to RubyGems but substantially lower than Maven. Practitioners can identify high-amplification packages before adding them to projects and seek lower-amplification alternatives when available. The 40% zero-dependency prevalence indicates many npm packages pose minimal transitive exposure.
Report issue for preceding element
For Go Modules projects, our findings indicate moderate attention with 6% of projects showing amplification exceeding 10 times and mean amplification of 4.48 times. The strong correlation at rho of 0.838 indicates predictable amplification where developers can estimate supply chain exposure from direct dependency counts.
Report issue for preceding element
For PyPI, Cargo, Packagist, CocoaPods, and Pub projects, our findings indicate standard security practices may suffice. With 0% of projects exceeding 10 times amplification and maximum amplification ranging from 2.0 times for CocoaPods to 5.3 times for Packagist, these ecosystems demonstrate that controlled amplification is achievable. Practitioners working in these environments can focus security resources on other concerns while maintaining awareness that any ecosystem can evolve toward higher amplification.
Report issue for preceding element
Implications for Practitioners on Rethinking Ecosystem Amplification Assumptions. Our findings challenge prevailing assumptions about ecosystem amplification profiles. The conventional narrative positions npm as the ecosystem with highest amplification due to its preference for small, single-purpose packages and incidents such as the left-pad removal in 2016. However, our data suggests Maven environments show greater elevated amplification due to values affecting over one quarter of all projects analyzed.
Report issue for preceding element
This has practical implications for security resource allocation. Organizations with mixed technology stacks should consider prioritizing Maven dependency auditing over npm auditing, contrary to conventional assumptions. The finding that Maven's amplification is unpredictable from direct dependency counts makes manual review more difficult, suggesting automated tooling is important for Maven environments.
Report issue for preceding element
The discovery that five ecosystems maintain 0% of projects exceeding 10 times amplification demonstrates that controlled amplification is not aspirational but achievable in production environments. CocoaPods at 0.32 times, PyPI at 1.50 times, and Cargo at 0.97 times represent existence proofs that ecosystem design can constrain supply chain exposure.
Report issue for preceding element
Implications for Tool Developers. Current dependency management tools often focus on direct dependencies and known vulnerabilities. Our findings suggest tools should expand their scope to address amplification-related exposure with ecosystem-specific strategies.
Report issue for preceding element
Tools should display amplification metrics alongside package information when developers consider adding dependencies. Showing that adding a particular Maven dependency will install 100 additional packages through transitive relationships helps developers make informed decisions. Tools should suggest lower-amplification alternatives when available, noting for example that a similar package provides equivalent functionality with fewer transitive dependencies.
Report issue for preceding element
Dependency visualization tools should show complete dependency paths rather than only direct relationships. Highlighting deep transitive chains helps practitioners understand supply chain exposure. Tools should integrate attack surface metrics into security dashboards alongside vulnerability counts.
Report issue for preceding element
For Maven specifically, tools should implement aggressive warnings when amplification exceeds 10 times given that 28% of projects reach this threshold. For npm, tools should focus on identifying outlier packages contributing to extreme amplification. For ecosystems with controlled amplification, tools can apply less aggressive warning thresholds.
Report issue for preceding element
Implications for Security Researchers. Our analysis reveals that ecosystem structural patterns correlate with security-relevant metrics. Researchers developing supply chain security models should consider amplification-aware approaches that weight vulnerabilities by their amplification potential. A vulnerability in a Maven package with high amplification affects more downstream projects than one in a PyPI package with controlled amplification.
Report issue for preceding element
The divergent amplification patterns we identify suggest ecosystem-specific security strategies may be more effective than uniform approaches. Research should investigate how to optimize security investment across heterogeneous technology stacks with different amplification profiles. Our hierarchical clustering results provide a foundation for grouping ecosystems by amplification characteristics.
Report issue for preceding element
The finding that ecosystem design choices correlate with amplification patterns suggests future research should examine how standard library comprehensiveness and platform constraints influence dependency patterns. The contrast between Maven at 24.70 times and CocoaPods at 0.32 times warrants investigation into specific design factors.
Report issue for preceding element
Implications for Ecosystem Governance. The amplification patterns we identified raise governance considerations. Ecosystem maintainers could consider displaying amplification metrics in package registries to help developers make informed decisions. Incentive structures encouraging minimal dependency footprints through badges or rankings could influence package design toward lower amplification.
Report issue for preceding element
CocoaPods demonstrates that platform constraints can control amplification. Other ecosystems could consider whether stricter version resolution policies would reduce amplification without limiting flexibility. Cargo's strict dependency model with mandatory lock files, which record exact dependency versions to ensure reproducible builds, provides a middle ground between flexibility and control.
Report issue for preceding element
The finding that Maven exhibits both highest amplification and weakest predictability suggests the Java ecosystem may benefit from tooling initiatives that expose transitive dependency trees more prominently. Build tool improvements that make amplification visible during development could influence framework design toward more modular architectures.
Report issue for preceding element
6.2. Threats to Validity
Report issue for preceding element
External Validity: Our study analyzes 50 projects per ecosystem totaling 500 projects. While this sample size provides substantial statistical power to detect large effects as evidenced by our significant findings with 22 of 45 pairwise comparisons showing large effect sizes, larger samples would increase confidence in effect size estimates. Our projects were sampled from popular packages which may not represent long-tail packages with different dependency patterns.
Report issue for preceding element
Our findings for Maven, npm, Cargo, PyPI, NuGet, RubyGems, Go Modules, Packagist, CocoaPods, and Pub may not generalize to other ecosystems such as CPAN for Perl, Hackage for Haskell, or Hex for Elixir. Each ecosystem has unique characteristics warranting separate investigation. However, the dependency management patterns we identify including transitive amplification and predictability metrics represent fundamental software engineering challenges that appear across ecosystems.
Report issue for preceding element
Our sampling focused on popular packages to ensure relevance to real-world development practices. Less popular packages may exhibit different amplification patterns. However, popular packages receive more usage and therefore their amplification characteristics affect more projects, making them appropriate for security-focused analysis.
Report issue for preceding element
Conclusion Validity: We employed non-parametric statistical tests appropriate for non-normal distributions confirmed by Shapiro-Wilk tests with all p-values below 0.001. Effect sizes using Cliff's delta provide standardized measures enabling comparison across studies. Bootstrap confidence intervals account for sampling uncertainty. Multiple comparison corrections using Holm-Bonferroni adjustment control family-wise error rate across 45 pairwise comparisons.
Report issue for preceding element
Our threshold of 10 times amplification for reporting percentages is a descriptive choice. Different thresholds would yield different prevalence estimates. We selected this threshold as it represents cases where over 90% of installed packages come from transitive relationships rather than explicit declarations. Sensitivity analysis with thresholds at 5 times and 15 times confirms qualitative findings remain consistent.
Report issue for preceding element
The clustering analysis uses Ward's linkage with Euclidean distance on standardized metrics. Different linkage methods or distance metrics might yield different groupings. However, the isolation of Maven with extreme amplification appears robust across multiple clustering approaches.
Report issue for preceding element
Internal Validity: Dependency resolution using native package manager tooling ensures accurate measurement but resolution can vary based on platform, existing lock files, and optional dependency configurations. We used clean environments and default configurations to minimize variation. For ecosystems with lock files, we regenerated lock files to ensure consistency.
Report issue for preceding element
Our amplification metric divides transitive by direct dependencies. Alternative formulations such as total divided by direct or log-scaled ratios might yield different insights. We chose our formulation for interpretability and alignment with prior work. Sensitivity analysis with alternative metrics confirms Maven exhibits highest amplification across formulations.
Report issue for preceding element
Zero-dependency packages receive amplification of zero by our formula which may underestimate exposure for ecosystems with many such packages. However, zero-dependency packages by definition introduce no transitive exposure, so this treatment aligns with security concerns.
Report issue for preceding element
Construct Validity: We use dependency count as a proxy for security risk. While more dependencies increase attack surface, not all dependencies pose equal risk. A project with 100 well-maintained transitive dependencies may be safer than one with 10 unmaintained packages. Future work could incorporate vulnerability data, maintenance status, and code quality metrics to refine this proxy.
Report issue for preceding element
High amplification indicates more transitive packages but does not directly measure security impact. Our supply chain exposure analysis provides interpretation of potential vulnerability propagation scope but does not validate against actual vulnerability incidence. Empirical validation using historical CVE data would strengthen claims about propagation scope and exposure impact.
Report issue for preceding element
Package popularity and maintenance status influence actual security risk beyond dependency counts. Our analysis focuses on structural properties of dependency networks rather than package quality. Combining amplification metrics with package health indicators represents promising future work.
Report issue for preceding element
7. Related Work
Report issue for preceding element
Our paper relates to prior research addressing software ecosystem analysis, dependency network studies, supply chain security, and vulnerability propagation.
Report issue for preceding element
Software Ecosystem Studies. Extensive research has characterized package ecosystems and their evolution. Decan et al conducted large-scale comparison of dependency network evolution across seven ecosystems including npm, RubyGems, and Cargo ( decan2019empirical) . Kikas et al analyzed dependency networks in multiple ecosystems identifying structural properties and evolution patterns ( kikas2017structure) . Wittern et al examined the dynamics of the JavaScript package ecosystem revealing rapid growth and dependency patterns ( wittern2016look) . Manikas provided a longitudinal literature study revisiting software ecosystems research ( manikas2016software) . Jansen et al established foundational research agenda for software ecosystems ( jansen2009sense) . Bogart et al studied how breaking API changes are negotiated across different ecosystems ( bogart2016break) . Constantinou and Mens examined socio-technical evolution in the Ruby ecosystem ( constantinou2017attack) . Valiev et al studied ecosystem-level determinants of sustained activity in open-source projects ( valiev2018ecosystem) . These studies characterize individual ecosystems but do not compare amplification patterns across 10 major ecosystems using consistent methodology and statistical rigor.
Report issue for preceding element
Ecosystem-Specific Dependency Analysis. Prior work examined dependency patterns in individual ecosystems. For npm, Abdalkareem et al examined trivial packages finding that 16.8% of npm packages are trivial contributing to deep dependency trees ( abdalkareem2017why) . Zimmermann et al conducted security-focused analysis revealing that installing an average npm package introduces implicit trust on 79 third-party packages ( zimmermann2019small) . Chinthanet et al studied lags in adoption and propagation of npm vulnerability fixes ( chinthanet2021lags) . Zahan et al identified weak links in the npm supply chain ( zahan2022weak) . Liu et al demystified vulnerability propagation via dependency trees in npm ( liu2022demystifying) . Staicu et al developed SYNODE for preventing injection attacks on Node.js applications ( staicu2018synode) .
Report issue for preceding element
For Maven, Soto-Valero et al introduced bloated dependencies finding that 75% of Maven artifacts contain unused dependencies ( soto2021comprehensive) . Benelallam et al created temporal graph-based representation of Maven Central ( benelallam2019maven) . Raemaekers et al studied semantic versioning and breaking changes in Maven ( raemaekers2017semantic) . Wang et al conducted empirical study of third-party library usages in Java projects ( wang2020watchman) . Ponta et al developed code-centric analysis of known vulnerabilities ( ponta2018beyond) .
Report issue for preceding element
For Rust, He et al presented empirical study of Rust adoption in Linux kernel development ( he2023empirical) . Qian et al investigated package provenance in Cargo ecosystem ( qian2022understanding) . Evans et al studied whether Rust is used safely by developers ( evans2020rust) .
Report issue for preceding element
For Python, Alfadel et al conducted empirical analysis of security vulnerabilities in Python packages ( alfadel2021empirical; alfadel2023empirical) . These ecosystem-specific studies provide deep insights but lack systematic cross-ecosystem comparison that would reveal fundamental differences in amplification patterns.
Report issue for preceding element
Our work extends these studies by providing systematic cross-ecosystem comparison of amplification patterns across 10 major ecosystems representing diverse language families, design philosophies, and platform targets.
Report issue for preceding element
Software Supply Chain Security. Software supply chain security has emerged as critical research area. Ohm et al provided comprehensive review of open source supply chain attacks ( ohm2020backstabber) . Ladisa et al presented taxonomy of attacks on open-source supply chains analyzing real-world incidents ( ladisa2023sok) . Duan et al measured supply chain attacks on package managers for interpreted languages ( duan2021measuring) . Vu et al studied typosquatting and combosquatting attacks on Python ecosystem ( vu2020typosquatting) . Taylor et al developed SpellBound for defending against package typosquatting ( taylor2020defending) . Garrett et al developed methods for detecting suspicious package updates ( garrett2019detecting) . Wetter conducted forensic analysis of the Log4j vulnerability ( wetter2022forensic) . Our amplification metrics quantify attack surface showing how vulnerabilities propagate through transitive relationships across diverse ecosystems.
Report issue for preceding element
Vulnerability Analysis and Propagation. Research has examined how vulnerabilities propagate through dependency networks. Pashchenko et al developed methods for counting vulnerable dependencies that actually matter ( pashchenko2018vulnerable) . Plate et al created impact assessment methods for vulnerabilities in open-source libraries ( plate2015impact) . Decan et al studied impact of security vulnerabilities in npm dependency network ( decan2018impact) . Alfadel et al conducted empirical analysis of security vulnerabilities in Python packages ( alfadel2021empirical; alfadel2023empirical) . Gkortzis et al examined relationship between software reuse and security vulnerabilities ( gkortzis2021software) . Lauinger et al analyzed use of outdated JavaScript libraries on the web ( lauinger2018thou) . High amplification as we document in Maven exacerbates vulnerability propagation since transitive dependencies are less visible to developers.
Report issue for preceding element
Dependency Management and Updates. Studies examined how developers manage and update dependencies. Kula et al investigated whether developers update library dependencies finding significant lag in updates ( kula2018developers) . Mirhosseini and Parnin studied whether automated pull requests encourage dependency updates ( mirhosseini2017can) . Zerouali et al developed formal framework for measuring technical lag ( zerouali2019formal) . Bavota et al studied how Apache community upgrades dependencies ( bavota2015how) . Hora et al examined how developers react to API evolution ( hora2018developers) . Cogo et al conducted empirical study of dependency downgrades in npm ( cogo2019empirical) . Our findings on unpredictable amplification in Maven suggest that dependency update decisions have cascading effects difficult to predict.
Report issue for preceding element
Technical Debt and Maintenance. Studies examined maintenance patterns in software ecosystems. Amann et al systematically evaluated API-misuse detectors ( amann2018study) . Li et al studied dependency maintenance practices in npm ( li2017understanding) . German et al studied code copying between applications ( german2010code) . Robbes et al examined how developers react to API deprecation ( robbes2012developers) . Derr et al studied third-party library updatability on Android ( derr2017keep) . Wang et al developed methods for detecting third-party libraries in Android applications ( wang2018detecting) . Hejderup et al proposed software ecosystem call graphs for dependency management ( hejderup2018software) .
Report issue for preceding element
Positioning Our Work. Our work differs from prior research in several ways. First, we provide cross-ecosystem amplification comparison using consistent methodology across 10 major ecosystems representing diverse language families and platform targets where prior work focuses on single ecosystems or limited comparisons. Second, we frame amplification as supply chain exposure metric computing attack surface, high-risk prevalence, and propagation potential where prior work often treats dependency count as proxy without explicit security framing. Third, we employ appropriate non-parametric statistical tests following established guidelines ( arcuri2011practical; cliff1993dominance; romano2006appropriate; wohlin2012experimentation) with effect sizes and confidence intervals across 45 pairwise comparisons addressing limitations of descriptive prior work. Fourth, we investigate why ecosystems differ connecting amplification to design choices, language families, and platform constraints through correlation analysis, hierarchical clustering, and design pattern examination rather than describing patterns alone. Fifth, our sample of 500 projects provides statistical power to detect meaningful differences with 22 of 45 pairwise comparisons showing large effect sizes. Our findings challenge conventional assumptions positioning Maven rather than npm as the ecosystem requiring most aggressive security attention.
Report issue for preceding element
8. Conclusion
Report issue for preceding element
As dependency amplification can expand attack surfaces in software projects, it is important to understand how amplification patterns vary across ecosystems. We characterize dependency amplification across 10 major package ecosystems: Maven Central for Java, npm Registry for JavaScript, crates.io for Rust, PyPI for Python, NuGet Gallery for .NET, RubyGems for Ruby, Go Modules for Go, Packagist for PHP, CocoaPods for Swift/Objective-C, and Pub for Dart. Our empirical study analyzes 500 projects examining dependency structures, amplification factors, supply chain exposure, and propagation scope. We find Maven exhibits higher amplification at 24.70 times compared to Go Modules at 4.48 times, npm at 4.32 times, and CocoaPods at 0.32 times, with large effect sizes in 22 of 45 pairwise comparisons challenging assumptions that npm's preference for small, single-purpose packages leads to highest amplification. We observe that 28% of Maven projects show amplification exceeding 10 times while five ecosystems including Cargo, PyPI, Packagist, CocoaPods, and Pub maintain 0% at this threshold, demonstrating that controlled amplification is achievable. We identify that ecosystem design choices influence amplification patterns where Maven's enterprise architecture leads to unpredictable transitive growth with weak correlation at rho of 0.196 while CocoaPods demonstrates platform constraints can control amplification to 0.32 times with strong predictability at rho of 0.950. Hierarchical clustering reveals Maven occupies an isolated position with extreme amplification while most ecosystems cluster together with controlled amplification. Based on our findings, we recommend practitioners implement ecosystem-specific security strategies where Maven environments receive transitive dependency auditing given 28% of projects exceeding 10 times amplification, npm and RubyGems projects focus on identifying high-amplification outliers given 12% and 14% prevalence respectively, and five ecosystems continue standard security practices given their demonstrated controlled amplification behavior with 0% of projects exceeding 10 times amplification.
Report issue for preceding element
Report Issue
Report GitHub Issue
Title:
Content selection saved. Describe the issue below:
Description:
Submit without GitHub Submit in GitHub
Report Issue for Selection
Generated by L A T E xml
Instructions for reporting errors
We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:
Click the "Report Issue" button.
Open a report feedback form via keyboard, use " Ctrl + ?".
Make a text selection and click the "Report Issue for Selection" button near your cursor.
You can use Alt+Y to toggle on and Alt+Shift+Y to toggle off accessible reporting links at each section.
Our team has already identified the following issues. We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.
Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion, and welcome developer contributions.
