---
name: What Are DORA Metrics? - Datadog
keywords: (placeholder)
metadata:
  url: https://www.datadoghq.com/knowledge-center/dora-metrics/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
What Are DORA Metrics? | Datadog 
Knowledge Center
Categories
Blog
Docs
Sign Up 
Applications
What Are DORA Metrics?
Ingest, monitor, apply, and act on DevOps Research and Assessment (DORA) metrics to identify issues in software development, release processes, and continuous integration/continuous delivery (CI/CD) workflows.
on this page
What are DORA metrics?
What are the benefits of DORA metrics for your organization?
How are DORA metrics calculated?
What are the use cases for DORA metrics?
What are the implementation challenges for DORA metrics?
Considerations when choosing a DORA metrics–based solution
What are practices to avoid with DORA metrics?
Learn more
further reading
What Is DevSecOps?
[
Get Started with Datadog Monitoring
Get started with Datadog with a free 14 day trial. Try it now](https://www.datadoghq.com/knowledge-center/dora-metrics/)
What are DORA metrics?
DORA metrics are four measurements of software delivery velocity and stability, developed by the DevOps Research and Assessment (DORA) program at Google Cloud and backed by over a decade of industry research. These measurements are:
DORA metrics are often broken into four performance categories: low performers, medium performers, high performers, and elite performers. The thesholds for each metric and category are:
DORA metrics help DevOps teams, engineering leadership, platform engineering teams, and developer experience (DevEx) teams identify areas for improvement, set goals for service-level agreements (SLAs), and establish objective baselines across teams for the velocity and stability of their organizations' software development lifecycle (SDLC). It is important to remember that DORA metrics should not be used to measure certain performance characteristics of development and engineering teams, including customer satisfaction, team dynamics, or the amount and quality of individual work.
What are the benefits of DORA metrics for your organization?
Implementing DORA metrics provides your organization with comparative measurements that can help identify and improve software development workflows, release processes, and continuous integration/continuous delivery (CI/CD) pipelines. Consider the following use cases:
Evaluate the progress and success of engineering initiatives. By focusing on key measurements, DORA metrics offer an objective look at the return on investment (ROI) and business impact of initiatives such as infrastructure modernization and changes to development platforms.
Identify performance trends in your SDLC and improve developer experiences. DORA metrics help DevOps teams identify issues with code repositories, staging and quality assurance (QA) tasks, CI/CD pipelines, and other software delivery tooling and processes. Measurements throughout these stages can help you discover bottlenecks in software delivery. Metrics that examine change failure rates and lead time for changes offer teams a roadmap to resolving problems and improving developer response times.
Identify best and worst practices across engineering teams. DORA metrics offer quantifiable measurements that can be applied widely across your engineering organization. Teams that produce faster results, release high-quality changes with fewer failure rates, and reduce service restoration times show better performance figures. Such measurements can also be used to identify practices in high-performing teams so you can recommend them for other teams.
How are DORA metrics calculated?
The steps needed to implement and review DORA metrics vary among organizations. The following explanations can help teams understand how these metrics are calculated:
Deployment frequency checks when deployment services were started and finished. To generally calculate the frequency, review the number of deployment events from CI/CD and deployment infrastructure tooling to determine the rate of deployment. Each organization must come up with its own definition for what makes a deployment successful or not.
Change lead time, measures deployment events in pipelines, such as code migrations from development to staging to production, running scheduled scripts, and user or data changes. To calculate this, determine: 1) when commits occur and 2) when deployments occur that include a specific commit. Every deployment should maintain a list of all changes, where every change is mapped to a Secure Hash Algorithm (SHA) identifier (a unique ID for each commit). Joining this list to the changes table and comparing timestamps provides the lead time. This metric can also be calculated in other ways, such as by reviewing pull request (PR) time and CI/CD pipeline duration.
Change failure rate watches for incident messaging, deployment failures, deployment rollbacks, and application error rates. To calculate the change failure rate, determine: 1) the total number of deployments attempted and 2) deployments that failed in production. Incidents are a primary way of understanding failures in production. Each incident should be mapped to a deployment (by its unique identifier). This allows for the calculation of a percentage of deployments that had at least one incident.
Time to restore measures the backing out of faulty code and restoration of data/services to a state of previous availability. To calculate the mean time to restore, locate the timestamp of each incident during a deployment and compare the timestamp when the incident was resolved. Like the other DORA metrics, there is no concrete or singular method to obtain this calculation. Teams could also look at mean time to repair, which measures the time it takes to mitigate customer impact from a deployment fault.
Depending on the solution, teams should be able to view and visualize DORA metrics on a dedicated dashboard and/or integrate the metrics via other workflows or tools. Dashboards should be adjustable to show information per team, service, repository, and environment, in addition to being sortable by time period.
What are the use cases for DORA metrics?
Looking beyond DevOps, DORA metrics have practical uses across various organizations and infrastructures. Consider the following use cases:
For engineering executive leadership: DORA metrics can help leadership quantify and review the holistic health of an engineering organization and how its teams are performing, in addition to tracking the ROI of initiatives.
For engineering leaders and managers: DORA metrics can identify high-performing teams, evangelize and help implement best practices, and objectively justify progress toward implementing initiatives proposed by leadership.
For platform engineering and site reliability engineering (SRE): DORA metrics can be used to identify bottlenecks in the SDLC, help focus on reducing higher rates of failure and longer restore times, and suggest or recommend areas for improvement.
What are the implementation challenges for DORA metrics?
Implementing DORA metrics requires planning and consideration. Specifically, collecting data is a twofold effort.
First, teams need to collect data for tooling across the SDLC. DevOps and engineering teams must account for source code management, CI/CD pipeline management, service management, infrastructure and application observability, and incident management. Though calculating DORA metrics can be accomplished in-house, the high number of integrations required, the full-time equivalent (FTE) time and cost, and an ever-changing infrastructure or technology stack can make such efforts time-consuming, resource-intensive, and unproductive. A DORA metrics–based solution provided by your organization's chosen observability platform can help eliminate these obstacles.
Second, teams need to determine the right level of aggregation. Organizations can view DORA metrics through different lenses, whether that is service-wide, team-wide, department-wide, or across the organization. Each level of aggregation is an effort unto itself and adds complexity. Additionally, engineering teams tasked with implementing DORA metrics might not have access to all layers of an infrastructure or the right levels of access to be able to fully report DORA metrics.
Considerations when choosing a DORA metrics–based solution
When evaluating an off-the-shelf (OTS) or a software-as-a-service (SaaS) solution to implement DORA metrics, consider the following features and pitfalls:
Does the solution provide explanations, breakdowns, and drilldowns of the data produced for each DORA metric? Any selected tool must be able to not only show the data but also provide mechanisms to ascertain how the data was collected and the history of such data collection. For example, a solution could provide a drilldown into recent incidents or CI pipeline executions to help understand deployment bottlenecks.
Does the solution provide customizable views? Engineering teams should determine the customizability of their views and have flexibility for how metrics can be presented in a clear, easy-to-understand format by team, department, time range, project, and so on.
Does the solution provide actionable steps for engineering teams to respond to? Key to DORA metrics is not only reporting but also interpreting findings to create actionable items for change, define baselines, plan improvements, and derive insights.
What are practices to avoid with DORA metrics?
DORA metrics can be used to compare velocity, performance, change rate failure, and time to restore. However, they should not be used as an evaluation tool to measure the performance of individual engineers within your organization. DORA metrics can be misinterpreted, especially where it concerns individual developer productivity based on metrics such as how many lines of code were written, the number of action items opened, the number of times code was edited, and so on.
Learn more
By measuring and analyzing their software delivery performance, organizations can identify targeted opportunities for improvement and drive meaningful change over time. Explore how to turn insights from Datadog's DORA Metrics into action:
3 ways to drive software delivery success with Datadog DORA Metrics
Getting started with Datadog DORA Metrics
Further Reading
[
What Is DevSecOps?
Learn what DevSecOps means and how it helps organizations prioritize security in an ongoing way as they build and support applications.](https://www.datadoghq.com/knowledge-center/devsecops/) 
Get free unlimited monitoring for 14 days
start your free trial
© Datadog 2026
en
© Datadog 2026
en
TERMS
PRIVACY
Your Privacy Choices    
Get Started with Datadog
×     
