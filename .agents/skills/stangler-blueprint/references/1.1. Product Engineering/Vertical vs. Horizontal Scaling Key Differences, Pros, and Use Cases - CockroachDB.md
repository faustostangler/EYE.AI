---
name: Vertical vs. Horizontal Scaling: Key Differences, Pros, and Use Cases - CockroachDB
keywords: (placeholder)
metadata:
  url: https://www.cockroachlabs.com/blog/vertical-scaling-vs-horizontal-scaling/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Vertical vs. Horizontal Scaling: Key Differences, Pros, and Use Cases
Product
Solutions
Resources
Pricing
Company
Contact us
Sign in
Try CockroachDB
Home/
Resources/
Back to Blog 
Vertical vs. horizontal scaling: What's the difference and which is better?
 Charlie Custer
Last updated on January 29, 2026
|
7 minute read
Content
What is horizontal vs vertical scaling?
What is horizontal scaling?
What is the difference between scaling up and scaling out?
How does vertical scaling compare to horizontal scaling?
What are the advantages of vertical scaling?
What are the disadvantages of vertical scaling?
What are the advantages of horizontal scaling?
What are the disadvantages of horizontal scaling?
Which should you choose: horizontal or vertical scaling?
What's the difference between vertical and horizontal scaling? (TL;DR)
FAQ 
Key Takeaways
Vertical scaling increases capacity by upgrading a single host's resources, but remains constrained by hardware limits, a single point of failure, and a single-host performance bottleneck (e.g., CPU, I/O, or connection limits).
Horizontal scaling increases capacity by distributing workloads, data, and connection load across multiple hosts, enabling greater scalability and fault tolerance.
Distributed systems typically favor horizontal scaling for improved resilience, availability, and long-term growth.
So you need to scale. That's a good problem to have!
But should you scale up or scale out? There's no easy answer, so let's take a closer look at horizontal scaling vs. vertical scaling , how they compare, and what the pros and cons are for each approach.
What is horizontal vs vertical scaling?
Vertical scaling refers to increasing the capacity of a system by adding capability to the machines it is using (as opposed to increasing the overall number of machines). This is also called scaling up.
Vertical scaling can be upgrading the physical machine that's running your system, or it can be swapping over to a different, more capable machine. As long as the number of machines our system uses isn't changing, that's scaling vertically.
For example, imagine that we have an application with a cloud database that has reached the limits of the server it's running on: a single 8 vCPU GCP instance with 32 GB of RAM.
To scale that database vertically, we might move it to an instance with 32 vCPUs and 64 GB of RAM. The database is still running on a single server, but the server is more powerful, enabling the database to handle heavier workloads.
Related
The Blueprint to Deliver Distributed Data at Scale: Learn how to design resilient, horizontally scalable data architectures for modern, global applications.
What is horizontal scaling?
Horizontal scaling refers to increasing the capacity of a system by adding additional machines (nodes), as opposed to increasing the capability of the existing machines. This is also called scaling out.
For example, imagine that we again have an application with a cloud database that has reached the limits of the server it's running on: a single 8 vCPU GCP instance with 32 GB of RAM.
To scale that database horizontally, we might partition it over two additional server nodes, each with 8 vCPUs and 32 GB of RAM. While each machine individually has the same capacity as our original server, we can now spread our workload across these three nodes, which in turn will allow us to handle heavier workloads.
Tap to unmute
Your browser can't play this video.
Learn more 
1x
An error occurred.
Try watching this video on www.youtube.com, or enable JavaScript if it is disabled in your browser.
What is the difference between scaling up and scaling out?
Before we get into comparing these two options, it's worth making a quick note on terminology.
“Scaling up” and “scaling out” are technically different things – the former refers to vertical scaling, the latter refers to horizontal scaling. In the real world, however, these terms are often used imprecisely. For some people, they are essentially interchangeable.
For that reason, in work-related conversations about scaling, it's worth clarifying what somebody means when they say they want to “scale up” or “scale out.”
How does vertical scaling compare to horizontal scaling?
Here's a visual demonstration of the difference between vertical vs. horizontal scaling. (We're using a database icon for the image here, but the same concept applies to up your application layer, too).
So which of these approaches is going to be better for you and your workloads? Well, it depends.
What are the advantages of vertical scaling?
It can sometimes be more cost effective. If you're running an on-prem system, for example, upgrading the components of a server you already own is likely to be cheaper than buying additional whole servers.
It can sometimes be simpler to work with. Depending on the tools you're using and the approach you take, scaling horizontally can get complicated as you have to work out all the details of how multiple machines will share the load.
It can be easier to maintain. Again, particularly in the case of on-prem systems, it is easier to handle upgrades, maintenance, etc. on a single machine than it is to have to manage multiple machines.
What are the disadvantages of vertical scaling?
You still have a single point of failure. Whether your database is running on 8 vCPUs or 64, if it's all on a single machine and that machine goes down, your entire database – and by extension, most or all of your application – will be offline until you can resolve the problem.
It is inherently limited. Vertical scaling is not infinite; whether you're running on a public cloud or a local machine, you will reach a point where upgrading a single machine's capacity is prohibitively expensive, or straight-up impossible.
It can sometimes cost more**.** While vertical scaling can be more cost effective in some circumstances, the costs can increase rather dramatically as you get closer to the top tier of single-machine capability.
Additionally, vertical scaling can come with “hidden” costs that aren't apparent when upgrading. For example, relying on a system that does have a single point of failure can be very costly. Downtime costs companies $12,900 per minute on average, according to a 2022 study from analyst firm Enterprise Management Associates (EMA) and AIOps company BigPanda. Those kinds of costs can very quickly wipe out any savings that were associated with opting for vertical scaling to begin with.
What are the advantages of horizontal scaling?
It increases availability and resilience/fault-tolerance. When configured properly, a system that is scaled across multiple machines should be able to survive the loss of one or more of those machines while still operating normally. This means less downtime. In fact, it is possible to come very close to zero downtime with the right horizontally-scaled setup.
It can be more cost-effective. While two or more machines is generally more expensive than one in the short term, the increased availability and resilience can quickly pay for themselves by allowing you to avoid the lost business and reputational damage that comes from both planned and unplanned downtime.
It can increase performance. When configured properly, a system that is scaled across multiple machines can route traffic efficiently to spread work evenly and ensure there are no processing bottlenecks. Having multiple nodes also allows for the possibility of multi-region deployments, allowing you to locate services in different geographical locations to place them closest to the users who access them.
What are the disadvantages of horizontal scaling?
It can be more complex. Particularly if you're implementing it manually – for example, if you're manually sharding a database – setting up a multi-node system can be quite complex, and it can also add complexity to management and ops work.
Tap to unmute
Your browser can't play this video.
Learn more 
1x
An error occurred.
Try watching this video on www.youtube.com, or enable JavaScript if it is disabled in your browser.
However, this complexity can often be avoided by choosing the right tools. In the realm of databases, for example, distributed SQL databases such as CockroachDB handle virtually all of that complexity automatically, under the hood. In some cases, using a tool like CockroachDB can actually lead to less work for development and ops teams than what was required when they were managing a single-machine system.
It generally costs more up-front. As previously mentioned, in the long-term horizontal scaling often ends up being more affordable, but the up-front costs tend to be higher since you're paying for two or more machines instead of a single one. If you're scaling out manually rather than using tools that are inherently distributed such as CockroachDB, there will also be costs associated with the setup and management of your manual distribution systems.
Which should you choose: horizontal or vertical scaling?
When assessing whether vertical or horizontal scaling is the best choice for your organization, it's important to consider a number of factors, including but not limited to:
Costs. Consider not only the up-front costs of both options, but also the long-term costs. What will managing and operating this system cost? What will an outage cost our organization?
Future growth. If your company is growing quickly, scaling from 32 vCPU machine to a 64vCPU machine may solve your problem, but for how long? For most medium and large companies, there is a point where scaling vertically simply isn't viable.
Similarly, with the right tools, scaling out a multi-node setup can be quite easy. With CockroachDB, for example, this can be as simple as hitting an “Add Node” button. Even in cases where the initial implementation is time-consuming or expensive, it can be worth it in the long run because going from (for example) three nodes to five to seven to dozens doesn't require much additional work.
Uptime requirements. How critical is the system these machines will be running? How available does it need to be? What will it cost if the system becomes unavailable? Mission-critical systems and workloads likely require high availability and thus will be better suited to horizontal scaling; less important workloads may be fine to scale vertically.
(For example, the hardware that's running your internal analytics database may not need five-nines availability. If it goes down for an hour or two, the business impact isn't likely to be massive. On the other hand, if the hardware that's running your payments system goes offline, that will have a much higher cost).
Performance requirements. Multi-node systems can be more performant when correctly optimized.
Regulatory requirements. Some locations have specific laws regarding things like geo-locating user data. This may require you to implement a multi-node, multi-region setup to ensure compliance.
Related
Navigate Data Modernization with Confidence: A practical playbook for moving from legacy databases to resilient, horizontally scalable data infrastructure.
What's the difference between vertical and horizontal scaling? (TL;DR)
Ultimately, the solution that's right for your company is going to involve a lot of company-specific factors, and there are no one-size-fits-all solutions.
In general, though…
Vertical scaling is best for:
Less important systems and workloads.
Systems and workloads that aren't likely to need additional scale in the future.
Keeping initial costs down (but it may increase future costs).
Systems and workloads that do not require high availability, high performance, or multi-region deployment.
Horizontal scaling is best for…
Mission-critical (tier 0) and important (tier 1) systems and workloads.
Systems and workloads that are likely to need additional scale in the future as the company grows.
Systems and workloads that do require high availability, high performance, or multi-region deployment.
Have a relational database that you need to scale? CockroachDB is the best solution for mission-critical transactional workloads like payment systems, metadata systems, and much more. Learn why.
In this short video tutorial you can see what it looks like to scale CockroachDB:
Tap to unmute
Your browser can't play this video.
Learn more 
1x
An error occurred.
Try watching this video on www.youtube.com, or enable JavaScript if it is disabled in your browser.
Try CockroachDB Today
Spin up your first CockroachDB Cloud cluster in minutes. Start with $400 in free credits. Or get a free 30-day trial of CockroachDB Enterprise on self-hosted environments.
Try Cloud Today Try Self-Hosted Today
Charlie Custer is a former teacher, tech journalist, and filmmaker who's now combined those three professions into writing and making videos about databases and application development (and occasionally messing with NLP and Python to create weird things in his spare time).
horizontal scaling
vertical scaling
Data 101
FAQ
FAQs about vertical scaling vs. horizontal scaling
What is vertical scaling?
What is horizontal scaling?
What is the difference between vertical and horizontal scaling?
What are the main advantages of vertical scaling?
What are the main disadvantages of vertical scaling?
When should I choose vertical scaling over horizontal scaling?
When should I choose horizontal scaling over vertical scaling?
How does CockroachDB help with horizontal scaling?
Share
Subscribe to our newsletter
Submit
We will email you updates about CockroachDB. You can unsubscribe at any time. Learn more about our privacy practices here.
Recommended
Navigate SQL Database Modernization with Confidence
From Resilience to Scalability: 12 Mission-Critical CockroachDB Use Cases
The State of AI Infrastructure 2026
The Blueprint to Deliver Distributed Data at Scale
CockroachDB vs PostgreSQL Services
More resources
Keep reading
View all posts
 No Prying Eyes: How to Set Up Azure Private Link for CockroachDB When your application talks to your database over the public internet, every hop is one more place something can go wrong, leading to potential latency, misconfiguration, or (worst case) exposure. Read now
 8 AI Use Cases That Depend on Database Resilience As AI systems become embedded in core business workflows, they increasingly interact directly with systems of record, turning model outputs into durable state changes. Read now
 Scaling AI Agents: PostgreSQL vs CockroachDB Under High-Concurrency Workloads Autonomous agents behave fundamentally differently from humans or “faster users,” and that difference reshapes the demands placed on your database. Read now
Join our community and get updates delivered straight to your inbox.
Subscribe
We will email you updates about CockroachDB. You can unsubscribe at any time. Learn more about our privacy practices here.
Product
Product overview
CockroachDB Fully-Managed Cloud
CockroachDB Bring Your Own Cloud
CockroachDB Enterprise
Latest release
Pricing
Sign in
Solutions
Customers
Database Modernization
High availability and disaster recovery
By Industry
AI Innovators
Banking & Fintech
Cybersecurity
Gambling
Gaming
Healthcare
Manufacturing & Logistics
Media & Streaming
Quant Firms
Retail & eCommerce
Software & Tech
By Use Case
Vector Search
Banking & Wallet
Gaming
Identity Access Management
IoT & Device Management
Orders & Inventory Management
Payments
Routing and Logistics
User Metadata
By Initiative
Database Modernization
Architectural Simplification
Resources
Documentation
Connect
Events
Podcast
Professional Services
Support
Webinars
Learn
Blog
Cockroach University
Database Comparisons
Guides
Product Demos
Company
About
Careers
Contact Us
Legal Notices
News / Press
Partners
Privacy
Security
Trust Center
   
Cookie Settings © 2026 Cockroach Labs     
Ask AI 
Cookie Consent
We share information you communicate to us through our site and information about how you use our site with our vendors, advertising and analytics partners.
Accept All Cookies Reject All
Cookies Settings 
Opt-Out Request Honored
Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer.
Allow All
Manage Consent Preferences
Performance Cookies
[x]
Performance Cookies
These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.
Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
Functional Cookies
[x]
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
Targeting Cookies
[-]
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Cookie List
Clear
[-] checkbox label label
Apply Cancel
Consent Leg.Interest [-]
checkbox label label [-]
checkbox label label [-]
checkbox label label
Confirm My Choices
 
