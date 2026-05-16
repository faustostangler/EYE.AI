---
name: Your Teams are not Call Centers - DataChef Blog
keywords: (placeholder)
metadata:
  url: https://blog.datachef.co/your-teams-are-not-call-centers/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Improve cross-team collaboration with Team APIs
Home
About
How we cook?
Sign in Subscribe
team
Your Teams are not Call Centers
How Team APIs can address a basic need for clarity in the organization
 
DataChef, Davide Rovati
30 Dec 2024 — 5 min read
Share 
This article is part of a series:
Team interactions must be designed for success
Get more done with less
Your Teams are not Call Centers
It's Christmas day — or whatever holiday you celebrate with your family. Kids are running around screaming like banshees, grandparents are pontificating that young people don't want to work anymore. You're one bite of stew away from freedom, just one bite before you can skedaddle and not have to think about this nightmare for the next 365 days.
As you're about to excuse yourself, your old uncle shuffles over, holding something you can't believe still exists in this universe, a device so ancient that you wonder whether he stole it from a museum. It's a BlackBerry.
“It doesn't make calls anymore, can you fix it? I know you're good with computers and stuff”.
Suddenly, the whole house falls silent. Everyone is staring at you, waiting expectantly for your answer. The pressure of three different generations feels heavy on your shoulders. You reluctantly agree to take a look.
The last time you saw a BlackBerry was in 1996. And your background is in finance.
In business, every day is Christmas day
Similar interactions occur almost daily in organizations counting more than 10 people, when teams start forming and become, de facto, the most atomic organizational unit.
You — and everyone else born after the first Moon landing — know that no one has any business in repairing a BlackBerry in 2025. But your well-mannered, technologically outdated uncle doesn't see why not.
This is a classic issue of mismatched expectations. Internally, a team knows its domain and limitations. However, these boundaries are often unclear or not communicated externally.
Failing to delineate these boundaries or a protocol for interactions leads to a sprawl of uncontrolled requests. Teams end up bombarded through every channel—chat, email, phone call, video call, in the office, from any time zone in the world. 
Parkison's Law states: "Work expands to fill the time available for its completion”.
I'll add a corollary: “Work requests expand to fill a team's available time — and then some.”
This is detrimental to organizations. First, these requests are often ad hoc, short-term fixes that only vaguely align with the organization's long-term goals. Second, they significantly increase a team's cognitive load, a leading cause of reduced performance and morale.
Your teams need a user manual
The principle is the same for everything discussed in this series: don't let chance rule your organization.
To be more specific, the goal is to define a “Team API” for each of your (software) teams. I didn't come up with this term, and like most unnecessary uses of jargon, I don't love it — so let me break down what it means.
First, a quick intro to the API concept: it stands for Application Programming Interface, which is more jargon and likely makes you none the wiser. In simple terms, an API defines what an external user can do with a program. APIs are designed to make interactions with software easier and more predictable.
Let's use an example.
Imagine it's 1960, and to check your bank account balance, you must walk to your bank in person. Not very convenient, right? Now, imagine your bank introduces a new service: they give each customer a private phone number they can call anytime. When you call, a voicemail tells you your current balance. That's essentially an API.
But could you use that same number to transfer money? Of course not. That number is exclusively for checking balances. An API doesn't just define how you interact (i.e., through calling a phone number); it also defines what to expect (i.e., to get your balance).
A Team API defines what to expect from a team and how to interact with them. In other words, it makes explicit things like:
The services the team provides
The software they own
Where to find their documentation
How and when to interact with them
What interaction modes they are open to
Which teams they typically collaborate with
These are just examples, and they should be adapted to suit your organization's needs. The creators of this concept offer a simple template to help you get started.
A Team API must also be accessible and usable. The primary goal here is to reduce unnecessary workloads and facilitate smoother interactions — Team APIs should not create more friction. If you introduce Team APIs and everyone in your organization has to jump through hoops for even the smallest task, it might be a symptom of other underlying issues in team interactions.
Now, the book that introduced the concept of Team APIs was published before COVID, and as such, it doesn't offer many practical examples for today's increasingly digital-first world. So, let me share an example from a former client of ours — one that implemented Team APIs brilliantly.
A case study
This client has a massive cloud infrastructure. Without going into detail, it's enough to say their cloud spend easily reaches six figures — monthly.
Setting up and maintaining infrastructure at that scale is no small feat, especially when the organization operates across multiple time zones and works with several unaligned external contractors. At any given time, there's a big risk that things might go wrong.
The team responsible for managing this infrastructure is called the Cloud Center of Excellence (CCoE). While I don't know exactly how many people are on that team (though I'd guess no more than ten), I do know that they are highly efficient and have, consciously or not, perfectly applied the principles of a Team API.
Why their Team API works
Clear scope
You should contact them only if you need specific changes to the cloud infrastructure. No distractions, no ambiguity.
Defined interaction method
The method of interaction is equally well-defined. No random emails, messages, or drop-ins — just a structured form.
Targeted questions
The form isn't just a technical checklist; it also asks business-oriented questions, including:
Why do you need this change?
Which business case does it support?
Who benefits from this change?
These questions force users to seriously consider why they request a change rather than simply “fire and forget” their demands and wait for someone to deliver.
The results
After submitting the form, users might be contacted for clarification. Once all questions are addressed, the team gets to work. The process is so efficient that requests are typically completed in under two weeks.
Nothing is left to chance, and the system ensures that the team and its users stay focused and aligned.
To recap
This marks the final chapter in our series on Team Topologies.
In the first article, we introduced the broader concept: the mechanisms that impact team efficiency and how to counteract them.
The second article focused on a silent killer: team cognitive load. We delved into its causes and effects and offered practical strategies to reduce it.
This third and final chapter highlighted one of the most actionable strategies for improving team dynamics: the Team API. It's a tool you can apply right now to reshape your organization and foster better collaboration.
At their core, most of these changes are cultural and organizational. They revolve around setting people up for success—an unsurprising truth, as successful people form the foundation of any successful organization.
But here's the challenge: organizational change is one of the toughest transformations to implement. Sometimes, seeking expert guidance to navigate this maze can be the smartest move.
Do you think your organization could benefit from these changes?
Send us a message — we've been in your shoes before and would happily share tailored advice.
Until then, stay tuned for more articles about business strategies, data engineering, and AI.
Discussion Member discussion
0 comments
Start the conversation
Become a member of DataChef Blog to start commenting.
Sign up now
Already a member? Sign in
Read more
[
How Product Organizations Scale Without Splitting Strategy from Execution
Quick recap from my previous article: In high-performing product organizations, strategy and execution aren't split between different roles. Every product team needs someone who owns both the "why" an By Davide Rovati](https://blog.datachef.co/how-product-organizations-scale-without-splitting-strategy-from-execution/)
[
Legacy Migration Starts with Understanding, not Inventory
An alternative to scale and direct legacy migration activities By Shahin](https://blog.datachef.co/legacy-migration-starts-with-understanding-not-inventory/)
[
How we use Claude to write code
Claude is a tool. It helps us think faster and write code faster. But the developer is still in charge. The goal is simple: better code, clear thinking, and full responsibility. This document explains By Farbod Ahmadian](https://blog.datachef.co/how-we-use-claude-to-write-code/)
[
Introducing DANA: Conversational AI for Legacy System Modernization
Imagine your data expert could answer every team's questions at once, without a single meeting. That's DANA. Built by DataChef, DANA is a conversational AI that learns from your domain experts, unders By Alireza Ebrahimkhani](https://blog.datachef.co/introducing-dana-conversational-ai-for-legacy-system-modernization/) 
Sign up
Powered by Ghost
Don't Miss New Articles
DataChef is a big data consultancy based in Amsterdam. We help modern marketing and sales teams by demystifying data and simplifying information.
Subscribe Email sent
