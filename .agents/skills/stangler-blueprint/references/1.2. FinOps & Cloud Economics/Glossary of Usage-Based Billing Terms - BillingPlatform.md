---
name: Glossary of Usage-Based Billing Terms - BillingPlatform
keywords: (placeholder)
metadata:
  url: https://billingplatform.com/glossary-of-usage-based-billing-terms
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Glossary of Usage-Based Billing Terms | BillingPlatform   
Skip to content
Skip to footer
Homepage  
Platform
Platform Overview The only Platform that adapts to your unique monetization needs Learn More
Extensible Data Model Adapt data for better monetization
Billing Automation Automate processes for efficiency and control
Global Support Support where you need it
Enterprise Scalability Effortlessly grow with your business needs
Integration Connect seamlessly with your ecosystem
Security & Control Protect data with enterprise-grade security
AI-Powered Reporting & Insights Make smarter decisions, faster
AI-Powered Navigation & Assistant intelligent, in-platform guidance
RevenueIQ
Solutions
clear
Billing Enterprise billing automation for any market
Usage-Based Billing Monetize products as customers consume them
E-Invoicing Simplify global invoicing and compliance
clear
Payments Streamline payments to accelerate cash
Collections Reduce DSO and minimize revenue leakage
AR Automation Unlock working capital with powerful AR Automation
clear
Revenue Recognition Achieve immediate insights with zero-day close
Financial Management Real-time execution of financial processes
Customer Portal Enhance CX with custom portal features
clear
clear Explore BillingPlatform solutions that meet your unique business needs
BY Business Model
By Role
By Industry
Customers
Resources
empty
Resource Center Analyst reports, white papers, case studies, videos, webinars, podcasts & more
Documentation BillingPlatform Knowledgebase — reference materials to support your success
Built on BP Marketplace of Value-Added Services & Accelerators
Find a Partner Partnering with industry leaders to exceed the needs of every enterprise
empty
Blog Read the latest industry trends, tips and best practices
Customer Success BillingPlatform Academy & Certification, Community, Professional Services, Technical Support
Community The discussion hub for BillingPlatform & modern monetization
Find a Partner Partnering with industry leaders to exceed the needs of every enterprise
Become a Partner Join the network that's changing the monetization landscape
Explore the MasterClass library, Product Capabilities and other informative sessions built for BillingPlatform customers Learn More
Company
About Us
News and Events
Careers
Find a Partner
Become a Partner
EN
DE
FR
ES
Contact Us
Glossary of Usage-Based Billing Terms
A reference guide to the terms used in usage-based billing, consumption pricing, and metered revenue management. For general billing terminology, see the BillingPlatform Glossary of Billing Terms.
A B C D E F H I M N O P R S T U V
A
Aggregation window: The time period over which usage events are collected and summed before being rated and billed. A monthly aggregation window means all events in the calendar month are totaled before pricing rules are applied. The choice of aggregation window affects how tiered pricing thresholds are calculated and how variable consideration is estimated for revenue recognition purposes.
Annual Recurring Revenue (ARR) in usage-based models: In a hybrid billing model, ARR typically reflects the subscription base component only, not the variable usage component. Usage revenue is reported separately as expansion revenue. Companies running hybrid models often track ARR alongside Net Revenue Retention to get a complete picture of revenue performance. See the CFO Playbook for Usage-Based Billing for how finance teams model these two revenue streams together. For the general definition of ARR, see the BillingPlatform Glossary of Billing Terms.
B
Bill shock: A situation in which a customer receives an invoice significantly larger than expected, typically because they exceeded usage thresholds without real-time visibility into their consumption. Bill shock is one of the most common causes of churn in usage-based products and is almost entirely preventable with a customer portal that shows current-period usage and projected invoice amounts. See Best Practices for Usage-Based Billing Implementation.
Billing metric: The unit of consumption that a usage-based product uses to calculate charges. Examples include API calls, tokens processed, gigabytes stored, compute hours, active seats, and transactions rated. A good billing metric scales directly with the value the customer receives — when value goes up, the metric goes up. Choosing the wrong billing metric is one of the most common causes of failed usage-based billing implementations.
Breakage: The portion of prepaid usage credits that customers purchase but never redeem before expiration. Under ASC 606, breakage must be recognized as revenue using either the proportional method (recognized in proportion to credit redemption patterns) or the remote method (recognized when redemption becomes unlikely). Breakage accounting requires historical redemption data and a consistently applied policy. See Revenue Recognition for Usage-Based Billing Contracts.
Burst pricing: See Overage Pricing.
C
Call Detail Record (CDR): A data record generated by a telecommunications system that documents the details of a call or communication event, including origin, destination, duration, and timestamp. CDRs are the primary usage data source for telecom billing and must be ingested, normalized, and rated before they can become invoice line items. Processing CDRs at scale requires a mediation layer capable of handling high event volumes in real time. See BillingPlatform's mediation capabilities.
Consumption-based pricing: A pricing model in which customers are charged based on the actual resources they consume rather than a fixed periodic fee. Consumption-based pricing, usage-based billing, metered billing, and pay-as-you-go are terms often used interchangeably, though consumption-based pricing sometimes implies a broader framing that includes outcome-based and value-based models. See Usage-Based Billing: The Definitive Enterprise Guide.
Contract liability: A balance sheet liability created when a customer pays for goods or services before they are delivered. In usage-based billing, prepaid credit purchases create a contract liability that is reduced as credits are consumed and revenue is recognized. The terms contract liability and deferred revenue are often used interchangeably under ASC 606.
Credit burndown: The process by which a customer draws down a prepaid usage credit balance over time as they consume a product or service. Credit burndown tracking requires real-time visibility into remaining credit balances and consumption rates so customers can anticipate when their credits will be exhausted.
Cumulative catch-up: An accounting adjustment made when an estimate of variable consideration changes from one reporting period to the next. Under ASC 606, changes in variable consideration estimates are recognized in the current period as a cumulative catch-up rather than restated in prior periods. For usage-based contracts with retroactive re-rating or minimum commitment true-ups, cumulative catch-up adjustments are a routine part of month-end close. See Revenue Recognition for Usage-Based Billing Contracts.
D
Days Sales Outstanding (DSO): A measure of how long it takes to collect payment after an invoice is issued. Usage-based invoices tend to have higher DSO than subscription invoices because the variable amount makes it harder for customers to anticipate and budget for payment. Tracking DSO separately for usage-based and subscription contracts helps identify where collections processes need adjustment. See the CFO Playbook for Usage-Based Billing.
Deduplication: The process of identifying and removing duplicate usage events from a data stream before rating and billing. Duplicate events can be caused by network retries, system errors, or multiple data sources reporting the same consumption. Without deduplication in the mediation layer, duplicate events result in overbilling customers and eroding trust. See B illingPlatform's mediation capabilities.
E
Expansion revenue: Revenue generated from existing customers through increased usage, rather than from new customer acquisition. In usage-based models, expansion revenue grows automatically when customers consume more of the product — no separate upsell motion is required. Expansion revenue is a primary driver of Net Revenue Retention above 100%. See Usage-Based vs. Subscription Billing: How to Choose.
F
Formula-based pricing: A pricing model in which the charge is calculated from a custom multi-variable formula rather than a fixed rate or tier structure. Formula-based pricing handles complex enterprise agreements where price depends on multiple factors simultaneously — for example, (calls x unit rate) x (1 minus volume discount). This model requires a rating engine capable of executing custom expressions without custom engineering for each contract. See Usage-Based Billing: The Definitive Enterprise Guide.
H
High-water mark pricing: See Staircase pricing.
Hybrid billing: A billing model that combines a fixed subscription component with one or more usage-based components in a single contract and invoice. The subscription provides a revenue floor and predictable cost for the customer; the usage component captures expansion as consumption grows. Hybrid billing is now the most common enterprise pricing pattern and requires a platform that handles both components natively without reconciling between separate modules. See BillingPlatform's hybrid billing capabilities.
I
Idempotency key: A unique identifier attached to a usage event submission that allows the receiving system to detect and reject duplicate submissions. Idempotency keys are a standard mechanism for preventing double-billing in high-volume event ingestion pipelines where retries and network failures can cause the same event to be submitted more than once.
M
Metered billing: A billing model in which customers are charged based on a measured unit of consumption — minutes, gigabytes, API calls, tokens — rather than a fixed fee. Metered billing is the original form of usage-based billing, with roots in telecom and utilities. The term is now used broadly across SaaS, cloud, and IoT. See Usage-Based Billing: The Definitive Enterprise Guide.
Minimum commitment: A contractual obligation in which a customer agrees to pay for a minimum quantity or dollar amount of usage per period, regardless of actual consumption. Minimum commitments give sellers a revenue floor and give buyers predictability on maximum spend. Under ASC 606, minimum commitments affect variable consideration estimation and may require true-up accounting at the end of the commitment period. See Revenue Recognition for Usage-Based Billing Contracts.
N
Net Revenue Retention (NRR): A metric that measures the percentage of revenue retained from existing customers over a period, accounting for churn, contraction, and expansion from increased usage. An NRR above 100% means existing customers are collectively spending more than they were a year ago — growth without new customer acquisition. Best-in-class usage-based businesses sustain NRR above 120%. NRR is the single most important metric for a usage-based business. See the CFO Playbook for Usage-Based Billing.
O
Out-of-period event: A usage event that is reported, corrected, or disputed after the billing period in which it occurred has closed. Out-of-period events create variable consideration adjustments in the current period rather than restatements of prior periods under ASC 606. Billing systems need a defined cutoff policy and the ability to process backdated events with correct period attribution. See Revenue Recognition for Usage-Based Billing Contracts.
Overage pricing: A pricing model in which a base subscription covers a defined usage allowance and any consumption above that threshold is charged at a separate overage rate. For example, a $500 per month plan includes 10 million API calls, with additional calls billed at $0.0002 each. Overage pricing preserves revenue predictability while capturing expansion above the included usage level. Also called burst pricing. See Usage-Based Billing: The Definitive Enterprise Guide.
P
Pay-as-you-go: A pricing model in which customers are charged only for what they actually consume, with no upfront commitment or minimum spend requirement. Pay-as-you-go removes acquisition friction and lowers the barrier for new customers to start using a product, since there is no large spend commitment to clear through procurement.
Performance obligation: Under ASC 606, a promise to transfer a distinct good or service to a customer. Identifying performance obligations correctly is the foundation of usage-based revenue recognition — it determines how the transaction price is allocated and when revenue is recognized. Usage-based contracts often bundle multiple performance obligations such as platform access, usage consumption, and professional services, each of which may be recognized differently. See Revenue Recognition for Usage-Based Billing Contracts.
Prepaid credits: Units of consumption that a customer purchases in advance and draws down as they use a product. When customers buy prepaid credits, the seller records a contract liability (deferred revenue) and recognizes revenue as credits are consumed. Unused credits that expire require breakage accounting under ASC 606. See Revenue Recognition for Usage-Based Billing Contracts.
R
Rating: The process of applying pricing rules to clean usage data to calculate the charges owed by a customer for a given billing period. The rating engine takes validated, deduplicated usage records from the mediation layer and applies the applicable pricing model — flat rate, tiered, volume, staircase, overage, or formula-based — to produce invoice line items. Rating accuracy depends entirely on the quality of the data entering it. See BillingPlatform's usage-based billing capabilities.
Retroactive re-rating: A pricing mechanism in which a lower rate is applied retroactively to all usage in a period once a customer crosses a volume threshold. For example, if a customer's total monthly usage exceeds 1 million units, all units in that month are re-rated at the lower tier price, not just the units above the threshold. Retroactive re-rating creates variable consideration that must be estimated during the period and trued up at period end. See Revenue Recognition for Usage-Based Billing Contracts.
Revenue leakage: The portion of billable usage that fails to appear on a customer invoice due to dropped events, duplicate records, transformation errors, or mediation failures. A 1 to 3 percent leakage rate is common in organizations running usage billing without robust mediation infrastructure. At $10 million ARR, that represents up to $300,000 in revenue that never gets billed. Revenue leakage is a controllable loss that finance teams should measure explicitly. See Best Practices for Usage-Based Billing Implementation.
S
Staircase pricing: A pricing model in which the unit rate that applies to the highest tier a customer reaches during a billing period is applied to all units consumed, not just the units above the threshold. For example, if a customer uses 51 units and the pricing breaks at 50, all 51 units are billed at the 51-plus rate. Also called high-water mark pricing. This model is common in telecom. See Usage-Based Billing: The Definitive Enterprise Guide.
T
Tiered pricing (usage-based context): In usage-based billing, tiered pricing applies a lower unit price to consumption that crosses defined thresholds, with each tier's rate applying only to the units within that band. For example, the first million tokens are billed at $0.002 each, and anything above that at $0.0015. Customers who consume more pay less per unit, creating a natural incentive to grow. See Usage-Based Billing: The Definitive Enterprise Guide. For the general definition of tiered pricing, see the BillingPlatform Glossary of Billing Terms.
Token-based pricing: A usage-based pricing model in which the billing metric is the number of tokens processed by a language model API. Token-based pricing typically differentiates between input tokens (the prompt) and output tokens (the model's response), with different rates applied to each. Model-version-specific rate tables are common, requiring a rating engine that can apply different pricing rules to different model versions simultaneously.
True-up: A billing adjustment made at the end of a defined period to reconcile actual consumption against a minimum commitment or estimated usage. If a customer's actual usage exceeds their minimum commitment, the true-up captures the incremental charges. If usage falls short, the true-up may represent a forfeit of unused capacity. True-ups that cross reporting period boundaries require the liability to be accrued at period end even if the invoice is issued in the following period. See Revenue Recognition for Usage-Based Billing Contracts.
U
Usage growth rate: The rate at which a customer's consumption of a product increases over time, measured per customer rather than in aggregate. Usage growth rate is an early indicator of Net Revenue Retention trajectory and is more actionable than lagging revenue metrics. A customer whose usage is growing is a fundamentally different risk profile from one whose usage is flat or declining. See the CFO Playbook for Usage-Based Billing.
V
Variable consideration: Under ASC 606, any component of a contract's transaction price that is not fixed at contract inception. Usage-based revenue is almost always variable consideration because the total amount depends on how much the customer consumes. Variable consideration must be estimated using the expected value or most likely amount method, constrained to avoid significant revenue reversal risk, and updated each reporting period as actual usage accumulates. See Revenue Recognition for Usage-Based Billing Contracts.
Volume pricing (usage-based context): In usage-based billing, volume pricing applies the rate corresponding to the highest tier a customer reaches to all units consumed in the period — not just the units above the threshold. For example, if a customer consumes 500 GB and the volume rate at that level is $0.03 per GB, the $0.03 rate applies to all 500 GB. See Usage-Based Billing: The Definitive Enterprise Guide. For the general definition of tiered pricing, see the BillingPlatform Glossary of Billing Terms.
For general billing terminology, including subscription billing, accounts receivable, payment processing, and financial reporting terms — see the BillingPlatform Glossary of Billing Terms.
Platform
Overview
Extensible Data Model
Integration
Billing Automation
Security & Control
Global Support
Enterprise Scalability
AI-Powered Reporting & Insights
AI-Powered Navigation & Assistance
Revenue IQ
Copilot
Predictive Insights
AI-Powered Admin
AI Studio
Solutions
Billing
Products & Pricing
Mediation & Charge Routing
Order Processing
Rating & Invoicing
Accounts Receivable
AR Automation
E-Invoicing
Payments
Cash Application
Wallets
Electronic Payments
BP Pay
Collections
Collector Dashboard
Alerts & Notifications
Dunning Strategies
Financial Management
General Ledger Rules
Journal Entries
Period Close
Financial Reporting
Revenue Recognition
SSP Determination
Revenue Contracts & Modifications
Waterfall/Rollforward Reporting
Customer Portal
Account Management
Hosted Payment Pages
Solutions
By Business Model
Recurring Billing
Subscription Billing
Usage-Based Billing
Dynamic Billing
Hybrid Billing
Digital Commerce
Product-Led Growth
By Role
Business Leader
Finance Leader
IT Leader
Finance IT Leader
Go-to-Market Leader
Billing Operations Leader
Revenue Accounting Leader
Digital Transformation Leader
By Industry
Healthcare Services
Media & Communications Services
Cloud Apps and Infrastructure
Financial Services
Transportation Services
SaaS
AI Monetization & Revenue Management
Resources
Learn
Resource Center
Blog
Find a Partner
Become a Partner
Documentation
Customer Success
Connect
BP Community
BillingPlatform Academy
Contact Us
Customers
Company
About Us
News and Events
Careers
Support
Privacy Notice
AI Use and Policies
Request Demo
Guided Tour
© 2026 BillingPlatform | 10333 E Dry Creek, Englewood, CO 80112 | +1 (866) 341-7394 - All Rights Reserved
Our website makes use of cookies to offer you the best possible service and experience. By clicking “Accept”, you declare your agreement in the utilization of all cookies.
CookiesettingsAccept 
Manage consent
Close
Privacy Overview
This website uses cookies to improve your experience while you navigate through the website. Out of these, the cookies that are categorized as necessary are stored on your browser as they are essential for the working of basic functionalities of the website. We also use third-party cookies that help us analyze and understand how you use this website. These cookies will be stored in your browser only with your consent. You also have the option to opt-out of these cookies. But opting out of some of these cookies may affect your browsing experience.
Necessary [x]
Necessary
Always Enabled
Necessary cookies are absolutely essential for the website to function properly. These cookies ensure basic functionalities and security features of the website, anonymously.
Functional [-]
Functional
Functional cookies help to perform certain functionalities like sharing the content of the website on social media platforms, collect feedbacks, and other third-party features.
Performance [-]
Performance
Performance cookies are used to understand and analyze the key performance indexes of the website which helps in delivering a better user experience for the visitors.
Analytics [-]
Analytics
Analytical cookies are used to understand how visitors interact with the website. These cookies help provide information on metrics the number of visitors, bounce rate, traffic source, etc.
Advertisement [-]
Advertisement
Advertisement cookies are used to provide visitors with relevant ads and marketing campaigns. These cookies track visitors across websites and collect information to provide customized ads.
Others [-]
Others
Other uncategorized cookies are those that are being analyzed and have not been classified into a category as yet.
SAVE & ACCEPT
Platform
Platform Overview The only Platform that adapts to your unique monetization needs Learn More
Extensible Data Model Adapt data for better monetization
Billing Automation Automate processes for efficiency and control
Global Support Support where you need it
Enterprise Scalability Effortlessly grow with your business needs
Integration Connect seamlessly with your ecosystem
Security & Control Protect data with enterprise-grade security
AI-Powered Reporting & Insights Make smarter decisions, faster
AI-Powered Navigation & Assistant intelligent, in-platform guidance
RevenueIQ
Solutions
clear
Billing Enterprise billing automation for any market
Usage-Based Billing Monetize products as customers consume them
E-Invoicing Simplify global invoicing and compliance
clear
Payments Streamline payments to accelerate cash
Collections Reduce DSO and minimize revenue leakage
AR Automation Unlock working capital with powerful AR Automation
clear
Revenue Recognition Achieve immediate insights with zero-day close
Financial Management Real-time execution of financial processes
Customer Portal Enhance CX with custom portal features
clear
clear Explore BillingPlatform solutions that meet your unique business needs
BY Business Model
By Role
By Industry
Customers
Resources
empty
Resource Center Analyst reports, white papers, case studies, videos, webinars, podcasts & more
Documentation BillingPlatform Knowledgebase — reference materials to support your success
Built on BP Marketplace of Value-Added Services & Accelerators
Find a Partner Partnering with industry leaders to exceed the needs of every enterprise
empty
Blog Read the latest industry trends, tips and best practices
Customer Success BillingPlatform Academy & Certification, Community, Professional Services, Technical Support
Community The discussion hub for BillingPlatform & modern monetization
Find a Partner Partnering with industry leaders to exceed the needs of every enterprise
Become a Partner Join the network that's changing the monetization landscape
Explore the MasterClass library, Product Capabilities and other informative sessions built for BillingPlatform customers Learn More
Company
About Us
News and Events
Careers
Find a Partner
Become a Partner
EN
DE
FR
ES
Contact Us  
