---
name: DORA Metrics: Guide to Measuring Software Delivery Performance - Planview
keywords: (placeholder)
metadata:
  url: https://www.planview.com/resources/articles/what-are-dora-metrics/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
DORA Metrics: Guide to Measuring Software Delivery Performance
Skip to content
Partners
Become a Partner
Find a Partner
Customer Care
Customer Success Center
Submit a Ticket
Log in
Planview® AdaptiveWork
Planview® Advisor Contact your admin for instructions
Planview® AgilePlace
Planview® ChangePoint Contact your admin for instructions
Planview® Daptiv
US
EU
Planview® Enterprise Architecture Contact your admin for instructions
Planview® IdeaPlace Contact your admin for instructions
Planview® Portfolios Contact your admin for instructions
Planview® PPM Pro (formerly Innotas ®)
Planview® ProjectPlace
Planview® Hub Contact your admin for instructions
Planview® Viz Contact your admin for instructions
Planview Browse Demos Search Toggle menu navigation
English
Deutsch
English
Français
Svenska
Search
Solutions
Back Solutions
Project Management and Portfolio Management Solutions
Strategic Portfolio Management Manage project and product portfolios enterprise-wide Watch demo • Strategic Portfolio Management
Project Portfolio Management Deliver projects at scale and with ease Watch demo • Project Portfolio Management
Product Portfolio Management Accelerate delivery of your product pipeline Watch demo • Product Portfolio Management
Professional Services Automation Grow your services revenue and margins Watch demo • Professional Services Automation
Software Product Delivery Solutions
Software Product Delivery Get continuous visibility into your software product delivery Watch Demo • Software Product Delivery
Value Stream Management Measure and manage software development efficiency Watch demo • Value Stream Management
Release Management Streamline software releases at scale Watch demo • Release Management
Software Toolchain Integration Connect Jira, ADO, ServiceNow, and more Watch demo • Software Toolchain Integration
Test Environment Management Optimize testing resources and reduce conflicts Watch demo • Test Environment Management
Enterprise Agile Planning Drive Agile transformation your way Watch demo • Enterprise Agile Planning
Explore Planview service offerings
Resources
Back Resources
Resource Center Fast access to the information you need, including articles, eBooks, on-demand webinars, whitepapers, and more
Analyst Recognition See what key industry analysts have to say about our solutions
Customer Stories Hear what our customers have to say about our products
Product Reviews and Testimonials See how our customers rate our products
Event Center In person and online opportunities to learn how Planview helps you solve your business problems
The Planview Blog Get expert advice and trend analysis insights on what's new and next in digital connected work
Thought Leadership Why New Software Won't Fix Your Broken Portfolio
Trending Topics
Artificial Intelligence
Strategy Implementation
Product Operating Model
Demos & Free Trials
About Us
Back About Us
About Us We're building the digital future of connected work
Leadership Learn more about the senior leadership team at Planview
Press Releases Browse recent and past press releases from Planview
In the News Browse the latest news stories and articles regarding Planview
Careers View open jobs, and learn more about working at Planview
Contact
1Open search panel
Worldwide
Deutsch
English
Français
Svenska
Browse Demos
Partners
Become a Partner
Find a Partner
Customer Care
Customer Success Center
Submit a Ticket
Call Email Log In
Planview Close search panel
Search for:
Search
Popular Searches
Popular search: Project Portfolio Management
Popular search: Enterprise Agile Planning
Popular search: Strategic Planning
Popular search: Lean Portfolio Management
Popular search: Collaborative Work Management
Popular search: Scaling Agile
Popular search: Agile Program Management
Popular search: Enterprise Architecture
Popular search: Application Portfolio Management
Popular search: Product Lifecycle Management
Popular search: New Product Development
Log In
Planview® AdaptiveWork
Planview® Advisor Contact your admin for instructions
Planview® AgilePlace
Planview® ChangePoint Contact your admin for instructions
Planview® Daptiv
US
EU
Planview® Enterprise Architecture Contact your admin for instructions
Planview® IdeaPlace Contact your admin for instructions
Planview® Portfolios Contact your admin for instructions
Planview® PPM Pro (formerly Innotas ®)
Planview® ProjectPlace
Planview® Hub Contact your admin for instructions
Planview® Viz Contact your admin for instructions
What are DORA metrics?
Achieving optimal performance is a constant pursuit in the world of software development and delivery. To enable enterprises to gauge their progress and identify areas for improvement, DevOps Research and Assessment (DORA) metrics have emerged as a valuable measurement framework. DORA metrics provide key insights into the effectiveness of DevOps practices and their impact on software delivery performance.
DORA metrics are four key metrics that DevOps and engineering teams can use to measure their performance. DORA metrics provide a framework for measuring software delivery throughput (speed) and reliability (quality).
Flow Metrics: A Business Leader's Guide to Measuring What Matters in Software Delivery
View the eBook • Flow Metrics: A Business Leader's Guide to Measuring What Matters in Software Delivery
Share on Linkedin 
Flow Metrics build on DORA standards to provide a top-level view of the value stream
In this article, we will delve into the world of DORA metrics, exploring their significance and how they can be leveraged to drive excellence in software delivery.
What Does DORA Metrics Stand For?
Within software development, there has also historically been tension in the divide between development and operations teams. The DevOps movement has worked to address this tension, encouraging collaboration, trust, and the creation of multidisciplinary teams to break down silos between “dev” and “ops” —hence, DevOps.
DevOps has become widely adopted since its inception in 2007-2008. A handful of leaders within the DevOps movement released the State of DevOps Report from 2014-2017, and later banded together to form a start-up called DevOps Research and Assessment —otherwise known as DORA. (DORA has since been acquired by Google Cloud and continues to publish the annual report.)
Jez Humble, Gene Kim, and Dr. Nicole Forsgren formed DORA with the goal of using their DevOps research to gain a better understanding of the practices, processes, and capabilities that enable teams to achieve top levels of performance in software development and delivery.
What Are the Four DORA Metrics?
DORA's founders identified four key metrics that are essential for success in DevOps:
Deployment frequency (DF)
Lead time to changes (LT)
Mean time to recovery (MTTR)
Change failure rate (CFR)
The DORA team identified these critical metrics as having the biggest impact on software development and delivery, based on survey responses from over 31,000 professionals over the course of six years.
The four DORA metrics enable engineering leaders to benchmark the performance of their teams against others in the industry, i.e., to determine whether they are “elite performers” or have room for improvement (teams that are high-, medium- and low-performing). This information empowers leaders to identify actionable opportunities for improvement and make changes to address them.
Deployment Frequency (DF)
Deployment frequency (DF) is a measure of average throughput. It is the average frequency at which code is deployed to production over a period of time. Deployment frequency can be used to assess how often an engineering team is delivering value to customers.
Being able to deliver new features into the hands of customers consistently and quickly is key to boosting customer retention and staying ahead of the competition.
Measuring deployment frequency over time can help teams identify ways to improve their speed of delivery. One insight that DORA has identified is that more successful DevOps teams tend to deliver smaller deployments more frequently (as opposed to delivering large batches of deployments less often).
DevOps teams can use their DF metrics to compare their performance against other teams. High-performing teams deploy an average of once a week, while top-performing teams might deploy several times within a single day.
If a team is performing poorly on this metric, they can use that information to identify specific ways to improve: For example, by breaking work down into smaller batches or creating smaller pull requests.
Lead Time for Changes (LT)
Lead time for changes (LT), or mean lead time to changes (MTLC), measures how long it takes for a team to implement a change once coding has begun.
Lead time for changes is measured by tracking the time it takes between when a commitment is made to a change and when that change is released to production. Mean lead time to changes is the mean, or average, of all changes made over a period of time.
Measuring MLTC is important because it quantifies how long it takes a team to deliver work to customers. Poor performance on this metric means that a team is unable to reliably implement changes in a timely manner.
Like other DORA metrics, mean lead time for changes can be useful for benchmarking team performance. Typically, elite performers can implement changes within a day, whereas average teams take about a week. Understanding this metric can help leaders gain a better understanding of team capacity and adjust expectations realistically when changes arise.
There are many factors that can affect MLTC, which is why it's important to analyze lead time metrics corresponding to each stage of the development process. Leaders can analyze patterns in how long it takes their team to open, address, test, and deploy changes to understand where bottlenecks might be occurring.
If a team is unsatisfied with their lead time for changes, they might try breaking work down into smaller batches, creating smaller pull requests, improving their code review process, or automating their testing or deployment processes.
Mean Time to Recovery (MTTR)
Mean Time to Recovery (MTTR) measures the time it takes for a team to restore a system to its normal functionality after a failure occurs in the production environment.
The ability to quickly recover from a failure is an essential capability for DevOps teams. There are two key components to recovery: being able to quickly identify a failure and then being able to resolve it. Increasing observability—having systems in place to ensure that failures are quickly identified—is a helpful step in improving mean time to recovery.
When it comes to MTTR, the faster, of course, the better. Top-performing teams might be able to recover from a failure in under an hour. However, most teams likely take several hours or even a full day.
To improve this metric, teams should develop a clear action plan for addressing failures and work to ensure that every team member understands the process.
Change Failure Rate (CFR)
The fourth and final DORA metric is change failure rate (CFR), which is a calculation designed to quantify the percentage of deployments that caused a failure in production. CFR is determined by dividing the number of incidents by the total number of deployments.
When teams are under pressure to deliver work and implement changes quickly, it's inevitable that some bugs or defects might go undetected. If the CFR is high, it's an indication that this is happening frequently, and quality is suffering. According to the 2021 State of DevOps Report, most teams report a change failure rate of 0-15%.
In this way, CFR serves as a critical counterpoint to other DORA metrics, which focus on speed (i.e., deployment frequency and lead time for changes). Deploying frequently is great, but not if that means consistently sacrificing quality—and then having to dedicate time to fixes. Analyzing CFR can help leaders ensure that teams are optimizing for both stability and throughput.
Many of the approaches to improving change failure rate mirror those suggested for other DORA metrics: decreasing batch size, automating testing processes, and working to improve the efficacy of the code review processes.
Why Use DORA Metrics?
Management expert Peter Drucker is quoted as saying, “You can't manage what you don't measure.” DORA metrics empower DevOps and engineering teams to make meaningful improvements by arming them with a standardized way to benchmark their performance against other teams and identify specific, actionable opportunities for improvement.
Optimizing for success in each of the four DORA metrics is a proven way to achieve stability, quality, and speed. Tracking deployment frequency and lead time for changes helps teams manage capacity, improve reliability, and deliver value consistently.
Working to improve mean time to recovery can help ensure customer satisfaction and protect against churn. Looking at change failure rate over time can help leaders ensure that teams are optimizing not only for speed, but also for quality.
DORA Metrics + Flow Metrics: A Winning Combination
Mastering DORA metrics can help teams release quality code quickly and confidently. However, they can't reveal whether your team is delivering the right value and business outcomes, i.e., what the customer needs and wants. DORA metrics optimize for a small part of a much larger process: the end-to-end journey from customer request to release.
DORA metrics help DevOps teams optimize for speed, quality, and stability in software development and delivery, but they don't help teams stay aligned with business outcomes, like revenue or customer retention. Maintaining this alignment is essential. It doesn't matter how quickly you can deploy code if that code is not aligned with actual business value.
To truly optimize for customer value, teams must be able to understand and visualize the entire development process from end to end. In software delivery, this concept is called value stream management (VSM). Dr. Mik Kersten, CTO of Planview, created the Flow Framework® to bridge the gap in software delivery, giving software organizations a way to measure and optimize for the delivery of business value across the entire value stream.
“Measuring only one area of the value stream is like only using two inches of a 12-inch ruler.”
– John Willis, Senior Director of the Global Transformation Office at Red Hat, co-author of The DevOps Handbook, Mik+One: Project to Product Podcast, Episode 17
The Flow Framework is based on the need to measure the end-to-end flow of business value and its resulting outcomes. Flow Metrics are used to assess the flow of business value across all the activities that contribute to the software value stream. By measuring the correlation between Flow Metrics and business outcomes, organizations can evaluate the impact of their investments and identify areas where flow and feedback cycles are too slow to respond to market changes and competition.
What Are Flow Metrics?
Flow Metrics offer a precise assessment of whether value stream flow is adequate to support desired business outcomes, such as revenue, cost reduction, customer satisfaction, and employee engagement. They evaluate the pace of business value delivery for software products, viewed from the perspective of your customers (internal or external).
There are four key Flow Metrics for measuring product value streams:
Flow Velocity® gauges whether value delivery is accelerating or slowing down. Flow Velocity is the number of Flow Items (features, defects, risks, and debt) completed over a particular period of time.
Flow Time measures time to market. Flow Time measures the time elapsed from 'work start' to 'work complete' on any given Flow Item, including both active and wait times.
Flow Efficiency® identifies waste in a value stream. Flow Efficiency is the ratio of active time out of the total Flow Time.
Flow Load® monitors over and under-utilization of value streams, which can lead to reduced productivity. Flow Load measures the number of Flow Items in progress (active or waiting) within a particular value stream.
In addition to the four Flow Metrics, Flow Distribution® helps identify the various types of work completed during specific time frames. Flow Distribution measures the ratio of Flow Items (Features, Defects, Risk, or Debt) completed over a particular window of time.
The Flow Metrics outlined in the Flow Framework are not meant to replace DORA metrics, but rather to complement them. Like any process, you need meaningful, comprehensive data insights to understand how fast you're delivering, what's slowing you down and what you can do to improve at every stage.
By combining DORA metrics with Flow Metrics, teams can ensure they get a holistic view of the entire software delivery process and are optimizing not only for speed and quality but also for business value and outcomes.
Flow Metrics: A Business Leader's Guide to Measuring What Matters in Software Delivery
View the eBook • Flow Metrics: A Business Leader's Guide to Measuring What Matters in Software Delivery
Share on Linkedin
Meet our author 
Michelle Wong
Senior Content Marketing Manager
Michelle Wong is the Content Strategist for Planview's value stream management solution for software delivery. Her content focuses on digital transformation topics including Project to Product, Flow Framework, DevOps, Agile, and SAFe.
Company
About Us
Leadership
Careers
Partners
Trust, Security, & Privacy
Sustainability
Customer Care
Customer Success Center
Submit a Ticket
Solutions
All Solutions
Strategic Portfolio Management
Software Product Delivery
Project Portfolio Management
Product Portfolio Management
Software Toolchain Integration
Value Stream Management
Enterprise Agile Planning
Release Management
Test Environment Management
Professional Services Automation
Work Management for Teams
Products
All Products
Planview® Portfolios
Planview Anvi™
Planview® Viz (formerly Tasktop Viz)
Planview® Hub (formerly Tasktop Hub)
Planview® AdaptiveWork
Planview® AgilePlace
Planview® ProjectAdvantage (formerly Sciforma)
Planview® Enterprise Architecture
Planview® Roadmaps
Planview® Advisor
Planview® IdeaPlace
Planview® ProjectPlace
Planview® Release (formerly Plutora)
Planview® Verify
Planview® ChangePoint
Planview® PPM Pro
Planview® Adopt
Services
Featured Toolchain Integrations
All Integrations
Atlassian Jira
Microsoft Azure DevOps
Jama
ServiceNow
IBM Engineering Workflow Management
Micro Focus ALM
Explore By Role
Resources
Analyst Recognition
Customer Stories
Product Reviews
Resource Center
Event Center
Blog
Press Room
Press Releases
In the News Avis(Index de l'égalité professionnelle) X Pour l'année 2026, notre index de l'égalité professionnelle basé sur les données 2025 est de 76 / 100. Il se décompose comme suit :
indicateur écart de rémunération : 25
indicateur écart de taux d'augmentations : 35
indicateur retour de congé maternité : non calculable
indicateur hautes rémunérations: 5 Conscients des enjeux de l'égalité professionnelle dans les entreprises, nous nous efforçons d'encourager la promotion des femmes au sein de nos services et veillons à assurer une rémunération juste et équitable en fonction des compétences de chaque salarié· e.
Acquisitions
Troux®
Projectplace®
Innotas®
LeanKit®
Clarizen™
Changepoint™
Aptage
Spigit®
Tasktop®
Enrich™
Plutora®
Sciforma®
Follow Planview on Twitter
Follow Planview on LinkedIn
Follow Planview on Facebook
Follow Planview on YouTube
Follow Planview on Instagram
Contact Us
All Data Subject Access Requests (DSARs), and requests of “Do Not Sell My Personal Information” according to the CCPA, must be submitted through the Planview DSAR portal located here.
Planview has appointed a Data Privacy Officer (DPO) to be responsible for overseeing our Privacy Management Program and related privacy compliance measures. DPO can be contacted at privacy@planview.com.
The Planview Privacy Statement was last reviewed on October 27, 2025.
© 2026 Planview
Legal
Privacy
Cookie Preferences
Worldwide
Deutsch
English
Français
Svenska
Worldwide    
