---
name: 2026-05-10 Team Topologies: The blueprint for Cloud & AI transformations | by Christian Dussol | Medium
keywords: (placeholder)
metadata:
  url: None
  source: SOURCE_TYPE_TEXT
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
WebSync metadata
title: Team Topologies: The blueprint for Cloud & AI transformations | by Christian Dussol | Medium
url: https://medium.com/@christian.dussol/team-topologies-the-blueprint-for-cloud-ai-transformations-e255475d50a0
date: 2026-05-10T21:26:09.645Z
parsing method: defuddle
Sitemap
I just finished re-reading “Team Topologies” (2nd Edition) by Matthew Skelton and Manuel Pais. The second time through, one thing became crystal clear: your organizational structure is either your greatest accelerator or your biggest bottleneck.
After working across three different team types in Modernization and Cloud transformations: Stream-aligned, Enabling, and Platform teams, I have seen firsthand how the right team structure can turn a 6-month deployment cycle into monthly releases. And how the wrong structure can make even the best technology investments feel like pushing a boulder uphill.
Let me share what I have learned.
The Cloud paradox: Great technologies, slow delivery
Here’s a pattern I see across organizations:
Modern technologies adopted:
✅ Cloud computing (Azure, AWS, GCP)
✅ Kubernetes for container orchestration
✅ AI/ML pipelines
✅ Microservices architecture
✅ DevOps practices
✅ Automation everywhere
Same old organizational problems:
❌ Siloed teams (Dev, QA, Ops, Security)
❌ Endless dependencies between teams
❌ 6-month lead times for simple changes
The hard truth: The issue is not technology. It’s organization.
Companies invest millions in Kubernetes, Cloud and AI. They hire brilliant engineers. They adopt cutting-edge practices. Yet they are still waiting months for feature deployments.
Why?
Conway’s Law: The hidden force shaping your architecture
In 1967, Melvin Conway observed something insightful:
“Organizations design systems that mirror their communication structure.”
This is not just theory, I have seen this play out in every company I have worked with.
What this means in practice:
If your organization is structured like this:
Frontend team
Backend team
Database team
Infrastructure team
Security team
Your architecture will look like:
Tightly coupled layers
Handoffs at every boundary
Integration nightmares
Deployment dependencies
Change amplification
Siloed teams → Monolithic systems.
No matter how many microservices you build. No matter how cloud-native your tech stack is.
Your architecture mirrors your org chart.
The modern complexity problem
Here’s what makes this worse in 2025:
The cognitive load of modern Cloud & AI systems is crushing:
Cloud Infrastructure: IaaS, PaaS, networking, cost optimization
Container Orchestration: Kubernetes, service mesh, ingress
Data Platforms: Data lakes, warehouses, streaming pipelines
ML Operations: Model training, deployment, monitoring, retraining
Security & Compliance: Zero trust, secrets management, audit trails
FinOps: Cost allocation, optimization, forecasting
Observability: Logs, metrics, traces, distributed tracing
No single team can master it all.
Yet most companies still organize like it’s 2010, functional silos with handoffs at every boundary.
The result? Brilliant engineers drowning in cognitive overload, waiting on other teams and shipping slowly.
The Team Topologies framework: 4 team types
Instead of endless organizational variations, Team Topologies proposes 4 fundamental team types:
🎯 1. Stream-Aligned teams: own value end-to-end
Purpose: Aligned to a flow of business value: a product, service or user journey.
Key principle: Autonomous with minimal dependencies. They own their complete stack: code, infrastructure, deployment, and operations
Cloud examples:
Customer AI team (owns ML models, APIs, frontend)
Payment platform team (owns transactions end-to-end)
Mobile app team (owns iOS/Android experience)
Why it works: No handoffs. No waiting. Fast feedback from production. Clear ownership.
The stream-aligned team is the fundamental building block. Everything else exists to support them.
🏗️ 2. Platform teams: absorb complexity
Purpose: Provide compelling internal services that reduce complexity for other teams.
Key principle: Self-service, not shared bottleneck. Think “internal product.”
Cloud examples:
MLOps platform (model deployment, monitoring, retraining as-a-service)
Cloud infrastructure platform (Kubernetes, networking, observability)
Developer portal (golden paths, documentation, service catalog)
Why it works: Stream teams stay focused on business value. Platform teams hide infrastructure complexity behind excellent developer experience.
Critical insight: Platform teams need product managers. They are building products for internal customers. Give them product managers, not just engineers.
🎓 3. Enabling teams: Accelerate capability building
Purpose: Help other teams adopt new technologies and practices through coaching.
Key principle: Time-boxed missions, NOT permanent dependencies.
Cloud examples:
FinOps experts coaching cost optimization (3-month engagement)
Kubernetes specialists helping with migration (6-month engagement)
Security team enabling secure-by-default practices
Why it works: Teams become autonomous and skilled. No permanent dependencies. Knowledge transfer, not gatekeeping.
Important: Enabling teams move on once capability is built. If they become permanent, they’re a bottleneck.
⚙️ 4. Complicated-Subsystem teams: Handle deep complexity
Purpose: Manage technically complex domains requiring deep specialization.
Key principle: Hide complexity behind clear interfaces.
Cloud examples:
GPU optimization for ML training
Real-time inference engine
High-frequency trading systems
Custom cryptography implementation
Why it works: Stream teams consume these services without understanding internals. Specialists can focus deeply on hard problems.
Use judiciously: Most organizations need 0–2 of these teams. Don’t create them prematurely.
The 3 interaction modes: How teams work together
Team types alone are not enough. You need to define HOW teams interact.
🤝 Collaboration: Work together closely (temporary)
When to use:
Exploring new technology
Quick discovery phase
High uncertainty
Important: This is temporary. Extended collaboration = unclear boundaries = cognitive overload.
📦 X-as-a-Service: Clear interfaces, minimal interaction
When to use:
Mature platform services
Well-defined APIs
Stable capabilities
This is the goal. Minimize cognitive load by consuming services with clear contracts.
🎓 Facilitating: Coach until autonomous
When to use:
Transferring new capability
Adopting new technology
Building team skills
Critical: Has an end date. The goal is autonomy, not dependency.
Match the i,nteraction to the situation.
Real-World results: Industry metrics
These are not just concepts. Companies are achieving remarkable results:
Footasylum (UK Retail)
Before: 6 releases per year
After: 1,250 deployments per week
200x improvement in deployment frequency
PureGym (UK Fitness)
Trust with Peers: +11% (8.1 → 9.0)
Team Mastery: +16% (6.8 → 7.9)
Engagement: +10% (7.6 → 8.4)
Improbable (Gaming/Tech)
30x faster Mean Time to Recover (MTTR)
5x reduction in major incidents
100% customer retention on new products
EBSCO (Information Services)
26% faster feature delivery
45% fewer dependency-related blockers
$9.1M annual cost reduction
These companies didn’t just reorganize. They fundamentally changed how teams interact and own work.
My Journey through team types
I have worked across three of these team types:
🎯 Stream-Aligned Team: ML product ownership
I led a team building an ML anomaly detection product. We owned everything:
Data pipelines
Model training and deployment
APIs
Monitoring and alerting
Production operations
The lesson: End-to-end ownership eliminated handoffs. We deployed daily. When something broke at 2 AM, we fixed it because we built it. Fast feedback loop. Clear accountability.
The challenge: Cognitive load was real. We needed strong platform support.
🎓 Enabling Team: Kubernetes & Azure adoption
I worked with teams adopting Kubernetes and migrating to Azure. Our job: transfer capability then leave.
The lesson: Time-boxing is essential. We had 3–6 month engagements. Taught. Paired. Documented. Then moved on. Teams became autonomous.
The challenge: Knowing when to let go. Resisting the urge to become a permanent bottleneck.
🏗️ Platform Team: Internal microservices platform
Currently, I’m building an internal platform (Spring Boot-based) for stream teams.
The lesson: Product thinking is crucial. We have internal customers. We measure adoption, satisfaction and toil reduction. We iterate based on feedback.
The challenge: Balancing “paved road” golden paths with flexibility. Making the right thing easy without being prescriptive.
Each role taught me something different about optimizing for fast flow.
None of this would have been possible without the incredible teams I worked with. Success came from communication, empathy, and truly understanding each other’s challenges.
Getting started: A practical approach
Don’t redesign everything at once. Start small. Learn. Iterate.
Step 1: Map one value stream
Pick one flow of business value. Map it end-to-end:
Where does work enter?
What teams touch it?
How many handoffs?
Where are the delays?
Visualize the current state. You might be shocked by the complexity.
Step 2: Form one Stream-Aligned team
Take that value stream. Give it to one team. Make them autonomous:
Cross-functional (dev, QA, ops, product)
End-to-end ownership
Clear mission
Empowered to deploy
This is your pilot. Prove the model works.
Step 3: Identify platform needs
What’s slowing your stream team down?
Infrastructure provisioning?
Deployment complexity?
Observability gaps?
These are your platform opportunities. Start with the “thinnest viable platform”, the minimum service that unblocks flow.
Step 4: Measure and evolve
Track metrics:
Lead time: Commit to production
Deployment frequency: How often you ship
MTTR: How fast you recover
Change failure rate: How often deployments fail
Team cognitive load: Subjective team assessment
Iterate based on data. Evolve your topology as you learn.
Key principle: Optimize for fast flow of change, not resource efficiency.
Common pitfalls to avoid
After watching multiple transformations, here are the common mistakes:
❌ Creating platform teams without stream teams
Platforms exist to serve stream teams. If you don’t have stream teams yet, you don’t need platforms.
❌ Enabling teams that never leave
If your “enabling team” has been helping the same team for 18 months, they’re not enabling, they are a dependency.
❌ Too many complicated-subsystem teams
These should be rare. Don’t create them because work is “hard.” Create them when domain complexity truly requires deep specialization.
❌ Unclear team boundaries
“Who owns this service?” should have one clear answer. Shared ownership = no ownership.
❌ Ignoring cognitive load
Can the team understand, develop, test and operate their entire scope? If not, the boundary is wrong.
Why this matters for Cloud & AI
Cloud and AI transformations fail when we treat them as purely technical initiatives.
You can adopt:
The latest Kubernetes features
Cutting-edge ML frameworks
Serverless architectures
GitOps workflows
AI-powered everything
But if your teams are organized in functional silos with handoffs at every boundary, you’ll still be slow.
Team Topologies bridges the gap between technology and organization, the gap where most transformations fail.
It provides:
A common language for discussing team design
Clear team types that map to real needs
Interaction modes that reduce cognitive load
Principles for evolving structure over time
The path forward
If you are leading Cloud or AI initiatives, ask yourself:
Are our teams aligned to value streams or functions?
Do we have clear platform teams reducing cognitive load?
Are our enabling efforts time-boxed or creating dependencies?
Can teams deploy independently or are they waiting on others?
Is our architecture mirroring our communication structure?
If these questions make you uncomfortable, it might be time to rethink your topology.
Start small. Pick one value stream. Form one stream-aligned team. Measure. Learn. Iterate.
The technology is ready. The frameworks exist. The question is: Is your organization designed for fast flow?
Resources
Book: “Team Topologies: Organizing Business and Technology Teams for Fast Flow” (2nd Edition) by Matthew Skelton & Manuel Pais
Website:teamtopologies.com
Case Studies:teamtopologies.com/examples
Christian Dussol is a Cloud & AI practitioner who has led Stream-aligned, Enabling and Platform teams. He currently focuses on Platform Engineering, building internal services that accelerate software delivery. Connect with him on LinkedIn.
Senior Engineering Manager @ teciem | Cloud & AI | FinTech Leadership
