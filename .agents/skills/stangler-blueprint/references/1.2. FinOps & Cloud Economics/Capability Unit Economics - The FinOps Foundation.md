---
name: Capability: Unit Economics - The FinOps Foundation
keywords: (placeholder)
metadata:
  url: https://www.finops.org/framework/capabilities/unit-economics/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Capability: Unit Economics
This website utilises technologies such as cookies to enable essential site functionality, as well as for analytics, personalisation, and targeted advertising purposes. You may close this banner to continue with only essential cookies. Cookie Policy
Accept Decline
Close Search
Loading... 
AI Value
AI for FinOps
Community
Training
Framework
FOCUS
FinOps X
Assets
About
Who We Are
What is FinOps?
Mission & Structure
Governing Board
Technical Advisory Council
Member Organizations
Ambassadors
Foundation Staff
Latest Information
Adopting FinOps: Getting Started
Content Attribution
FinOps Foundation Insights
FinOps Landscape
Cloud FinOps Book
What's New in FinOps
Get Involved
[
Join as an Individual
](https://www.finops.org/membership/) [
Join as an Enterprise
](https://www.finops.org/membership/enterprise/)
Get Certified Join the Community
AI Value
AI for FinOps
Community
Back to menu Overview Topics Events Jobs Board FinOps X FinOps X Session Library FinOps Foundation Insights
Training
Back to menu Training Catalog Recommended Training Mentorship Program FinOps Certified Professionals Professional Contributions FAQs
Framework
Back to menu Overview Scopes Principles Personas Phases Maturity Domains Capabilities Technology Categories Asset Library
FOCUS
FinOps X
Assets
Back to menu Asset Library FinOps X Session Library FinOps Landscape KPIs Terminology FinOps Assessment FinOps Cloud Book
About
Back to menu About
Who We Are
What is FinOps?
Mission & Structure
Governing Board
Technical Advisory Council
Member Organizations
Ambassadors
Foundation Staff
Latest Information
Adopting FinOps: Getting Started
Content Attribution
FinOps Foundation Insights
FinOps Landscape
Cloud FinOps Book
What's New in FinOps
Get Involved
[
Join as an Individual
](https://www.finops.org/membership/) [
Join as an Enterprise
](https://www.finops.org/membership/enterprise/)
Get Certified Join the Community
FinOps X 2026 · June 8-11 · San Diego Register Now
Framework
Overview
Scopes
Principles
Personas
Phases
Maturity
Domains
Capabilities
Technology Categories
Asset Library
Make Suggestion
This work is licensed under CC BY 4.0 - Read how use or adaptation requires attribution 
Unit Economics
Framework / Domains / Quantify Business Value / Unit Economics
On this page
Definition
Maturity Assessment
Functional Activities
Measures of Success & KPIs
Inputs & Outputs
Develop and track metrics that provide an understanding of how an organization's technology use and technology management practices impact the value of the organization's products, services, or activities.
Define Unit Metrics which support Organizational Goals
Define and document goals the organization is trying to achieve through the investment in technology and its application
Define and document metrics which will drive the decisions, behaviors or outcomes needed
Define and document measurements that are appropriate to evaluate technology use and cost
Define unit metrics and KPIs which satisfy the needs of those organizational goals
Distinguish resource efficiency unit metrics from business unit metrics, and clarify how they relate
Ensure Unit Economic data is available
Provide feedback to Data Ingestion to gather appropriate information to calculate unit metrics and KPIs
Assess business data quality and validate terminology alignment early, leveraging FOCUS
Define a strategy for providing KPI data to all appropriate stakeholders in the channels they use for decision making
Document data sources, correlations, and unit metric calculations for all personas
Validate Impact of Unit Metrics
Review impact of unit metrics on actual performance and other goals
Establish a cadence for metric review, adoption, modification, and refresh
Definition
Unit Economics brings together what an organization spends on technology and the value that technology spending creates. Without a way to relate costs to benefits received, it is difficult to understand whether spending is appropriate.
Unit economics provide cues to meet organizational goals through technology usage. They help communication between personas by tying technology costs more directly to business outcomes.
Unit economic metrics can be defined for many aspects of technology usage. They may track technology cost by revenue, per million authorized users, per transaction, per customer, or per case resolved, depending on the goals of the organization or the product. They can also be defined for technical aspects such as cost per service request, cost per workload, cost per seat used, cost per VM, cost per GB stored, or cost per token.
These unit economics can help engineering teams identify design and operational improvements, and help product owners understand direct and indirect costs driven by customer or employee usage, enabling workload placement, packaging, pricing, and roadmap tradeoffs. They can also reinforce progress toward margin or financial goals, including industry specific unit views such as cost of service delivery as a percent of revenue, or IT spend framed against the business units that generate premium or margin outcomes.
By pairing technology spend with value measurements, changes in spending can be interpreted as economies of scale, productivity gains, or runaway cost drivers within a unit metric. In practice, many organizations find the most actionable view is a trend over time within a defined FinOps Scope, rather than forcing broad comparability across unrelated business objectives, products or services.
Unit economics is often discussed in terms of marginal cost (unit cost metrics) and, where feasible, marginal revenue (unit revenue metrics). Comparing marginal cost and marginal revenue can help highlight break-even points and profitability dynamics. Where revenue attribution is difficult, outcome value proxies are often used, for example demand, throughput, customer experience, risk reduction, or service levels. When compared with the revenue or value generated by each unit, these metrics can support broader economic discussions such as contribution margin, product sustainability, or pricing tradeoffs.
When FinOps practitioners first address measuring unit costs, it is often in the context of Cloud Unit Economics. The unit economics of public cloud and other consumption-based IT services can be more useful for decision making because the variable use and cost model of public cloud allows for rapid increases or decreases in usage, and multiple rate optimization options. So understanding the impact of these near-real-time changes can be more impactful to business value. For further details on defining, implementing, and building upon unit economics with FinOps teams, the unit economics working group has published a paper on Introduction to Cloud Unit Economics.
Unit costs can guide strategic decisions and generate benefits beyond efficiency by exposing underutilized services, prompting consolidation or architecture changes, and highlighting cases where costs are outpacing delivered value. Unit costs can also show why rising costs are not always negative if proportionally more business value is being delivered.
Unit metrics can generally be sorted into two broad categories:
Resource Efficiency Unit Metrics (for example cost per GB stored, cost per GB transferred, cost per virtual CPU, cost per seat used, cost per token)
Business Unit Metrics (for example cost per tenant, cost per transaction, cost to serve, cost per case resolved)
Engineers can more easily implement resource efficiency unit metrics as controllable signals within their domain and a way to demonstrate value and best practices. Implementing business unit metrics provides broader organizational context, enabling Leadership and Product owners to make explicit tradeoffs across cost, speed, quality, and risk, and is often an indicator of higher maturity.
For organizations adopting Generative AI, early unit economics often starts with cost per token and expands toward outcome oriented measures, for example cost per assist, cost per agent action, or cost per case deflected, so decision makers understand what the token was used for and what value it generated. Baselines can help demonstrate efficiency gains as adoption grows, and point of consumption awareness can reduce surprise spend by making unit costs visible where usage happens.
Ultimately, unit costs are more than KPIs, as they can guide a cultural shift. They foster shared responsibility for technology spending and consumption by aligning technology costs with business value. Engineers become cost conscious architects, product teams build value driven features, and leadership steers technology investments toward outcomes aligned to business strategy and objectives.
Maturity Assessment
Crawl
Unit economics at the total cost / organizational results level in basic ways
Primarily working on technical unit cost metrics which are more concrete and centered on variable cost and use technology categories like public cloud
Business outcome data, which may be harder to gather or correlate is not used at a granular level of detail
Low organizational adoption or understanding of unit economics to drive decision making
Unit economics focus on direct variable costs rather than TCO, ROI or shared costs more broadly
Walk
Leadership, Product or Engineering teams develop unit economics with support of FinOps Practitioners, specific to their scope of work
Unit economics used in other important technology categories to create visibility of cost across public cloud, SaaS use, data centers, etc. for important Scopes of spend
Value and outcome data is used more often, leaders start referencing stable business unit metrics in decision making routines
Moderate trust and decision use, typically in priority areas rather than across the technology investment and operational landscape
Unit economics begin to account for fully loaded costs, or costs outside of direct technology use
Run
All operational FinOps Scopes include defined unit metrics for related segments of technology spending and usage, aligned to business context for visibility and decision making at multiple levels of the organization
Unit economics applied equally across all managed technology categories, consistently across different FinOps Scopes
Unit metrics incorporate fully loaded costs across all applicable technology categories
Unit metrics available at multiple levels of organizational and technical granularity
High trust and consistent use in investment and optimization decisions, with clear ownership and governance of definitions
Unit economics are defined and considered early, shaping build vs buy, architecture, workload placement, migration, sourcing, and pricing decisions
Functional Activities
 FinOps Practitioner
As someone in the FinOps team role, I will…
Connect technology-related spend, usage and adoption to the organization's business strategy and priorities through Executive Strategy Alignment
Communicate the importance of using Unit Economics to tie technology cost to organizational value consistently
Build collaboration between other personas to understand the key metrics involved in the organization, for applicable FinOps Scopes
Define and document meaningful metrics in partnership with Leadership, Engineering and Product Personas that relate technology cost and usage to business value
Document metric definitions, assumptions, and cost inclusions for consistent interpretation
Provide visibility to unit metrics and KPIs in appropriate channels for each FinOps Persona, including point of consumption visibility where usage decisions occur
Align FinOps Personas on outcomes, demand drivers, and relevant unit metrics
Support governance cadence for metric review, changes, and retirement
 Product
As someone in a Product role, I will…
Define outcome goals, demand assumptions, and sustainable cost to serve targets
Provide input to FinOps Practitioners regarding key organizational metrics and goals related to my area of responsibility
Co-define meaningful metrics that demonstrate business value from my products
Clarify business data sources, data points and unit definitions to reduce debate
Track defined metrics to demonstrate the value the products are bringing to the business
Work with FinOps teams to expand AI metrics beyond tokens toward outcome related measures
 Finance
As someone in a Finance role, I will…
Provide input to FinOps Practitioners regarding key organizational metrics and goals related to my area of responsibility
Align unit metrics with organization wide budgeting, forecasting, reporting, and financial guardrails
Define allocation rules and cost structures supporting fully loaded business unit metrics
Incorporate unit metrics into variance narratives, explaining drivers, not just spend
Validate metric assumptions, reconciliation, and consistency across sources
Track and embed these into financial reporting to demonstrate our improved/worsened financial position in terms of technology investment/efficiency
 Procurement
As someone in a Procurement role, I will…
Provide input to FinOps Practitioners regarding key organizational metrics and goals related to my area of responsibility
Incorporate the use of unit metrics into procurement planning and decision making
Use unit metrics to inform vendor selection, renewals, and commercial model choices
Consider terms affecting unit economics, including commitments, entitlements, and consumption exposure
 Engineering
As someone in an Engineering role, I will…
Provide input to FinOps Practitioners regarding key organizational metrics and goals related to my area of responsibility
Support the ideation of unit economic metrics that support engineering making meaningful contributions to the organization.
Use Unit Economics metrics to drive better organizational efficiencies through architectural, performance, reliability and workload placement decisions
Define controllable drivers behind resource efficiency metrics, explain impacts on business metrics
Partner on data instrumentation to improve unit definitions and outcome correlation
 Leadership
As someone in a Leadership role, I will…
Make clear to all Personas what unit economic metrics are meaningful to the organization's success, aligned to strategic outcomes
Sponsor ownership, governance, and change control for metric definitions and cost inclusions
Provide specific guidance on timing, format, and scope of required unit economic metrics, including distinguishing between leadership business unit metrics from engineering control metrics
Use these delivered metrics to make better informed, data driven decisions aligning technology spend to business value
Measures of Success & KPIs
Measuring success in this capability often focuses on whether unit economics is improving decisions and outcomes, not only whether dashboards exist.
Organizational success can be measured in terms of the percentage of teams, personas, or stakeholders that are using unit economics metrics in decision making to communicate about technology use, and the percentage of priority areas where business unit metrics are stable enough to reduce repeated debate over definitions.
The use of both resource efficiency unit metrics and business unit metrics can be in place for FinOps Scopes which materially impact business results or drive large amounts of value. In some organizations, continuous improvement is reflected in unit cost trends over time within a product, cohort, or defined scope, and may be reviewed in a consistent cadence, for example as part of operating reviews or annual efficiency routines.
Automation, or the ability to automatically calculate unit economics metrics using repositories which are well documented, accessible, and correlated, tends to be most apparent in metrics critical to broader business decision making. Where unit economics expands across vendors and technology categories, normalization of cost and usage datasets can improve consistency and trust.
Regular review and periodic analysis of impacts can allow adjustment of metrics where needed, addition of new metrics to drive additional good behavior, or retirement of metrics which no longer serve the needs of the organization, including situations where comparisons across dissimilar products are creating more confusion than insight.
KPIs
Cost per API Call
Measures the average cost for each API call made to AI services. This KPI helps track the efficiency of managed AI services like AWS SageMaker or Google Vertex AI.
Read more
×
Cost per API Call
Measures the average cost for each API call made to AI services. This KPI helps track the efficiency of managed AI services like AWS SageMaker or Google Vertex AI.
Formula
Cost Per API Call = Total API Costs / Number of API Calls
Candidate Data Sources:
API usage reports
Dashboards from AI platforms
Logs from AI platforms
Cloud billing data
Example:
If the total API costs are $1,200 and the number of API calls made is 240,000, the cost per API call is: $1,200/240,000 = $0.005 per API call
Related Capabilities
Unit Economics Reporting & Analytics
Related Assets
[
GenAI FinOps vs. Cloud FinOps: Similar Roots, Different Challenges
](https://www.finops.org/wg/genai-finops-vs-cloud-finops/)
[
GenAI FinOps: How Token Pricing Really Works
](https://www.finops.org/wg/genai-finops-how-token-pricing-really-works/)
[
How to Build a Generative AI Cost and Usage Tracker
](https://www.finops.org/wg/how-to-build-a-generative-ai-cost-and-usage-tracker/)
Data Value Density
Measures the strategic ROI of data cloud platform assets by comparing the business value generated to the total cost of ownership (TCO) of the data product. This KPI shifts the focus from cost-cutting to value-maximization. A higher ratio indicates a high-margin data product that generates significant business utility, while a ratio approaching or falling below
Read more
×
Data Value Density
Measures the strategic ROI of data cloud platform assets by comparing the business value generated to the total cost of ownership (TCO) of the data product. This KPI shifts the focus from cost-cutting to value-maximization. A higher ratio indicates a high-margin data product that generates significant business utility, while a ratio approaching or falling below 1.0 signals a "value leak" where the cost of maintaining the data exceeds its benefit.
Formula
Data Value Density = Total Business Revenue or Value Index / Total Data Platform TCO
Candidate Data Source(s):
End-to-end Data Cloud Platform cost reports
Product analytics or user engagement telemetry
Finance or capital allocation systems
Related Capabilities
Unit Economics Rate Optimization Usage Optimization Licensing & SaaS
Related Assets
[
GenAI FinOps vs. Cloud FinOps: Similar Roots, Different Challenges
](https://www.finops.org/wg/genai-finops-vs-cloud-finops/)
[
GenAI FinOps: How Token Pricing Really Works
](https://www.finops.org/wg/genai-finops-how-token-pricing-really-works/)
[
How to Build a Generative AI Cost and Usage Tracker
](https://www.finops.org/wg/how-to-build-a-generative-ai-cost-and-usage-tracker/)
Value for AI Initiatives
Measures the financial or value return generated by AI initiatives relative to their cost. This KPI helps to justify the investment in AI services and aligns them with business outcomes.
Read more
×
Value for AI Initiatives
Measures the financial or value return generated by AI initiatives relative to their cost. This KPI helps to justify the investment in AI services and aligns them with business outcomes.
Formula
Return On Investment = (Financial Benefits – Costs) / Costs * 100
Candidate Data Sources:
API usage reports
Dashboards from AI platforms
Logs from AI platforms
Cloud billing data
Example:
If the financial benefits from an AI project are $50,000 and the total costs incurred are $20,000, the ROI is: (50,000−20,000)/20,000 * 100 = 150%
Related Capabilities
KPIs & Benchmarking Reporting & Analytics Unit Economics
Related Assets
[
GenAI FinOps vs. Cloud FinOps: Similar Roots, Different Challenges
](https://www.finops.org/wg/genai-finops-vs-cloud-finops/)
[
GenAI FinOps: How Token Pricing Really Works
](https://www.finops.org/wg/genai-finops-how-token-pricing-really-works/)
[
How to Build a Generative AI Cost and Usage Tracker
](https://www.finops.org/wg/how-to-build-a-generative-ai-cost-and-usage-tracker/)
Cost per Gigabytes Stored
Measures average cost per GB stored, impacted through storage tiers and by maximizing data life-cycle management.
Read more
×
Cost per Gigabytes Stored
Measures the average cost per GB stored, impacted through storage tiers and by maximizing data life-cycle management. This average cost can be categorized by specific or combination of the following FOCUS fields to gain more insights and map them to business units : Region ID, Account ID, Service Category ID, SKU ID.
Formula
Cloud Storage Costs / Number of GB stored
Data Sources:
CSP Billing Data and Cloud Console
Related Capabilities
Unit Economics
Time to Achieve Business Value
Measures the time it takes to achieve measurable business value from AI initiatives. This KPI uses a “breakeven point” of doing a function with AI versus the cost of performing it some other way (like with labor). It provides the awareness around the forecasted days to achieve the full business benefit vs the actual business
Read more
×
Time to Achieve Business Value
Measures the time it takes to achieve measurable business value from AI initiatives. This KPI uses a “breakeven point” of doing a function with AI versus the cost of performing it some other way (like with labor). It provides the awareness around the forecasted days to achieve the full business benefit vs the actual business results achieved and understanding the opportunity costs and value per month.
Formula
Time to Value (days) = Total Value associated with AI Service / daily Cost of Alternative solution
Candidate Data Sources:
API usage reports
Dashboards from AI platforms
Logs from AI platforms
Cloud billing data
Example:
If an AI initiative starts on January 1, 2024, and the model is successfully deployed on April 1, 2024, the Time to Value is: April 1, 2024−January 1, 2024=3 months.
Forecast to get $100k/mo of business within 1 month, but it actually took 5 months and only achieved $50k/mo business benefit, 5 months was the time to business value metric to track and seek to improve.
Related Capabilities
Forecasting Unit Economics Reporting & Analytics Planning & Estimating
Related Assets
[
GenAI FinOps vs. Cloud FinOps: Similar Roots, Different Challenges
](https://www.finops.org/wg/genai-finops-vs-cloud-finops/)
[
GenAI FinOps: How Token Pricing Really Works
](https://www.finops.org/wg/genai-finops-how-token-pricing-really-works/)
[
How to Build a Generative AI Cost and Usage Tracker
](https://www.finops.org/wg/how-to-build-a-generative-ai-cost-and-usage-tracker/)
Inputs & Outputs
Inputs
Data Ingestion technology cost and usage data, business relevant value and demand data, and requirements for a common repository of usage and billing data that can span technology categories such as public cloud, data center, SaaS, AI etc.
Use of FOCUS (FinOps Open Cost and Usage Specification) as a standardized billing and usage schema that can simplify normalization of cost datasets as well as terminology used in unit economics reporting
Business Performance data from operational areas or FinOps Scopes being measured with Unit Economics
Outputs
Unit Economic targets (ranges and thresholds) for each Scope of the FinOps practice
Unit metrics used to measure business outcomes may be consistent, but the target values expected for each Scope may differ
View former Measuring Unit Costs page
On this page
Definition
Maturity Assessment
Functional Activities
Measures of Success & KPIs
Inputs & Outputs
Related Assets
Introduction to Cloud Unit Economics Cloud Unit Economics Story Collection Unit Economics: A Government Organizational Perspective The Benefits of Cloud Unit Economics for Your Organization Driving Intelligent FinOps Investment Decisions with Unit Economics
Follow Us:
Linkedin GitHub YouTube
FinOps Foundation
About
Media Resources
Training Scholarship
Technical Charter
Access Criteria
Code of Conduct
Code of Conduct Committee
Resources
FinOps Assets
Events
O'Reilly FinOps Book
Training and Certification
Full Course Catalog
FinOps Certified Practitioner
FinOps Certified Professional
Member Certification
This work is licensed under Attribution 4.0 International
© 2026 FinOps Foundation Project a Series of LF Projects, LLC.
For web site terms of use, trademark policy and other project policies please see https://lfprojects.org.
For the technical charter of FinOps Project a Series of LF Projects, LLC, please see the Technical Charter.
×
Make Suggestions
×
×
Suggest a Resource
× 
