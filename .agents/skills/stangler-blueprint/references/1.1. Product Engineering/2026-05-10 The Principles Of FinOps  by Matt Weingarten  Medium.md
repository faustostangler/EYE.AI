---
name: 2026-05-10 The Principles Of FinOps | by Matt Weingarten | Medium
keywords: (placeholder)
metadata:
  url: None
  source: SOURCE_TYPE_TEXT
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
WebSync metadata
title: The Principles Of FinOps | by Matt Weingarten | Medium
url: https://medium.com/@matt_weingarten/the-principles-of-finops-c083d79ff972
date: 2026-05-10T22:32:52.667Z
parsing method: defuddle
Sitemap
Save those gold bars
Note: This is a post written in collaboration with the people at Hevo Data. Definitely check out their platform if you’re interested!
Introduction
So far in this series, we’ve looked at the role data engineering can play in FinOps, and then we went into more depth and looked at various cost-saving techniques for AWS, Databricks, and Snowflake. However, we haven’t really zoomed out and discussed FinOps as a whole.
I’ll spare a post dedicated to “What is FinOps?” specifically and instead take the definition from the FinOps Foundation website:
FinOps is an operational framework and cultural practice which maximizes the business value of cloud, enables timely data-driven decision making, and creates financial accountability through collaboration between engineering, finance, and business teams.
In short, FinOps is a mindset where teams focus on maximizing the value that Cloud usage brings through data-driven (hey, a DE buzzword!) decision making, and providing financial accountability in all places. Sounds like a great idea, but what are the principles that can help get you there?
Note that these principles come from the FinOps Foundation as well. I’m not smart enough to think of these things on my own.
Collaboration
Collaboration is paramount if an organization is going to work together to achieve FinOps-related goals. Technology teams will need to work closely with finance in order to figure out their budgets for the upcoming year/quarter and then see how costs stack up against said budgets. Having a direct channel of communication instead of going through other teams will make things a lot easier here, even though that’s not the norm currently.
In many cases, there’s a centralized team that helps lead the FinOps initiative in an organization (more on this later). Technology and finance teams should work closely with this centralized team (or tiger team, as I’ve heard it be called before) on finding the biggest anomalies and seeing how those can be rectified.
Ownership
Accountability for Cloud usage and its associated costs should drill down to individual teams instead of being a higher initiative. Teams should be in a position where they can take ownership on that work from the beginning (when initially building out new products) to continual refinement. Decision-making should be decentralized so that the team leading the overall FinOps mission can focus on higher-level work.
It’s imperative that cost is considered upfront when designing new applications. Dr. Werner Vogels (yes, the Amazon luminary himself) had a great speech on this at the latest re:Invent conference where he focused on the Frugal Architect. Tradeoffs will need to be made between cost, performance, quality, etc., but cost definitely needs a seat at the table, which has generally not been the case over time. I do see that improving, though, based on how we’re treating it more actively in our projects now.
Reporting
How can you make data-driven decision making? Through reporting, of course. Data should be available in real-time as it becomes available, as this can drive better Cloud utilization, and fast feedback loops result in higher efficiency overall.
With this reporting in place, it’s also crucial to have proper anomaly detection and trend analysis set up. Anomaly detection allows you to better see spikes as they occur. Trend analysis looks over a longer period of time so you can analyze why costs are starting to rise/fall.
All of this reporting can be properly managed with a solid tagging strategy. If resources are clumped together with appropriate tags, it’s easy to track down where to begin as opposed to having resource disorganization.
Centralized Team
So, what exactly does that centralized team I mentioned above do anyway? They have to encourage, evangelize, and enable best practices for the organization. They must be up to date on the latest and greatest in the Cloud (which is always changing) and work with executive teams as well as individual engineering teams to drive these goals to completion.
The centralized team should manage any rate, commitment, and discount agreements that the organization has with Cloud vendors, as they’re in the best position with the information at their disposal to take those calls. I’d also suggest that this team work with champions (volunteers in each of the different spokes of the traditional hub & spoke model) to get best practices moving in those spokes. That way, the greater team can focus on the bigger mission and not get too caught up in efforts that don’t necessarily need to involve them.
Conclusion
With these principles (and others) in hand, organizations will be in a better place to begin their FinOps journey and see some wonderful benefits. My last post in this series will suggest some tips for success. I hope this has been providing the value it should so far!
Currently a Data Engineer at Samsara. Previously at Disney, Meta, and Nielsen. Bridge player and sports fan. Thoughts are my own.
