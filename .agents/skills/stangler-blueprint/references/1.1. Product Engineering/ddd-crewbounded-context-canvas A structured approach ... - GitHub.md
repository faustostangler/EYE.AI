---
name: ddd-crew/bounded-context-canvas: A structured approach ... - GitHub
keywords: (placeholder)
metadata:
  url: https://github.com/ddd-crew/bounded-context-canvas
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
GitHub - ddd-crew/bounded-context-canvas: A structured approach to designing and documenting each of your bounded contexts · GitHub
Skip to content
Navigation Menu
Toggle navigation 
Sign in
Appearance settings
Platform
AI CODE CREATION
GitHub Copilot Write better code with AI
GitHub Spark Build and deploy intelligent apps
GitHub Models Manage and compare prompts
MCP Registry New Integrate external tools
DEVELOPER WORKFLOWS
Actions Automate any workflow
Codespaces Instant dev environments
Issues Plan and track work
Code Review Manage code changes
APPLICATION SECURITY
GitHub Advanced Security Find and fix vulnerabilities
Code security Secure your code as you build
Secret protection Stop leaks before they start
EXPLORE
Why GitHub
Documentation
Blog
Changelog
Marketplace View all features
Solutions
BY COMPANY SIZE
Enterprises
Small and medium teams
Startups
Nonprofits
BY USE CASE
App Modernization
DevSecOps
DevOps
CI/CD
View all use cases
BY INDUSTRY
Healthcare
Financial services
Manufacturing
Government
View all industries View all solutions
Resources
EXPLORE BY TOPIC
AI
Software Development
DevOps
Security
View all topics
EXPLORE BY TYPE
Customer stories
Events & webinars
Ebooks & reports
Business insights
GitHub Skills
SUPPORT & SERVICES
Documentation
Customer support
Community forum
Trust center
Partners View all resources
Open Source
COMMUNITY
GitHub Sponsors Fund open source developers
PROGRAMS
Security Lab
Maintainer Community
Accelerator
GitHub Stars
Archive Program
REPOSITORIES
Topics
Trending
Collections
Enterprise
ENTERPRISE SOLUTIONS
Enterprise platform AI-powered developer platform
AVAILABLE ADD-ONS
GitHub Advanced Security Enterprise-grade security features
Copilot for Business Enterprise-grade AI features
Premium Support Enterprise-grade 24/7 support
Pricing
Search or jump to...
Search code, repositories, users, issues, pull requests...
Search
Clear
Search syntax tips
Provide feedback
We read every piece of feedback, and take your input very seriously. [-]
Include my email address so I can be contacted
Cancel Submit feedback
Saved searches
Use saved searches to filter your results more quickly
Name
Query
To see all available qualifiers, see our documentation.
Cancel Create saved search
Sign in
Sign up
Appearance settings
Resetting focus
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert
ddd-crew / bounded-context-canvas Public
Notifications You must be signed in to change notification settings
Fork 191
Star 2k
Code
Issues 7
Pull requests 1
Actions
Projects
Security and quality 0
Insights
Additional navigation options
Code
Issues
Pull requests
Actions
Projects
Security and quality
Insights 
ddd-crew/bounded-context-canvas
master
2 Branches 0 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
License
The Bounded Context Canvas
The Bounded Context Canvas is a collaborative tool for designing and documenting the design of a single bounded context.
If you're not sure what a bounded context is you may want to check out Eric Evans DDD Reference and Martin Fowler's article.
The canvas guides you through the process of designing a bounded context by requiring you to consider and make choices about the key elements of its design, from naming to responsibilities, to its public interface and dependencies.
Download the blank canvas template.
Summary
How to Use
Section Definition
Example
Tools
Design Tips
Additional Resources
Translations
Contributors
Contributions and Feedback
How to Use
To quickly get started with the Bounded Context Canvas, complete the canvas in the order the sections are presented in Section Definitions
Start with the name and description of the canvas to clarify its reason for existing and key responsibilities in a sentence or two. Then you can fill in the other sections of the canvas in any order. You could design outside-in starting with inbound communication or inside out starting with the business rules and domain language.
You may not have all the information you need to complete certain sections of the canvas. In such a case, you'll need to use other modelling techniques to find the information you require.
Alternative Formats
The default Bounded Context Canvas format shown above is not the only format, below are others. Feel free to also experiment with new and novel formats.
Use Case Swimlanes: This style organizes the communication section into swimlanes showing the sequence in which interactions occur using the format: message in -> decision(s) made -> message(s) out
Section Definitions
Here is a short explanation of each section of the canvas.
Name
Naming is hard. Writing down the name of your context and gaining agreement as a team will frame how you design the context.
Purpose
A few sentences describing the why and what of the context in business language. No technical details here.
Writing down the purpose forces you to clearly articulate fuzzy thoughts and ensure everybody in the team is on the same page.
Describe the purpose from a business perspective, you may also name key actors for whom the bounded context provides value.
Strategic Classification
How important is this context to the success of your organisation?:
core domain: a key strategic initiative
supporting domain: necessary but not a differentiator
generic: a common capability found in many domains
What role does the context play in your business model:
revenue generator: people pay directly for this
engagement creator: users like it but they don't pay for it
compliance enforcer: protects your business reputation and existence
How evolved is the concept (see Wardley Maps):
genesis: new unexplored domain
custom built: companies are building their own versions
product: off-the-shelf versions exist with differentiation
commodity: highly-standardised versions exist
For detailed descriptions of genesis, custom built, product, and commodity see Wardley Maps Evolution definitions.
For help filling in this section of the canvas, see Core Domain Charts.
Domain Roles
How can you characterise the behaviour of this bounded context? Does it receive high volumes of data and crunch them into insights - an analysis context? Or does it enforce a workflow - an execution context? Identifying the different roles a context plays can help to avoid coupling responsibilities.
Check out Alberto Brandolini's Bounded Context Archetypes and Rebecca Wirfs-Brock's Object Role Stereotypes for a deeper analysis of this space. The Model Traits worksheet contains community-generated examples of roles (model traits was the former name for domain roles).
Inbound Communication
Inbound communication represents collaborations that are initiated by other collaborators.
Messages
Messages are the information that one collaborator sends to another. There are three types of conversation that can occur between bounded contexts. A request to do something (a command), a request for some information (a query), or notification that something has happened (an event).
The word message is used in the general sense and not tied to any implementation. No message bus or asynchronous workflow is obligatory. A command, for example, could simply be posting data from an HTML form as a HTTP POST command.
Collaborators
Collaborators are other systems or sub-systems that send messages to this context. They can be other bounded contexts, frontends (web or mobile), or something else.
If the Bounded Context owns the user interface (e.g. micro-frontend) then the collaborator type is direct user interaction.
Relationship Type
The relationship type between two bounded contexts indicates how the models and teams influence each other. See Context Mapping to learn about relationship types.
Organising Into Swimlanes
Collaborators can be organised into horizontal swim lanes showing the messages that they send.
Outbound Communication
Outbound communication represents collaborations that are initiated by this context to interact with other collaborators. The same message types and notations apply as inbound communication.
Ubiquitous Language
What are the key domain terms that exist within this context, and what do they mean?
Business Decisions
What are the key business rules and policies within this context?
Assumptions
You will never make design decisions having a full knowledge about everything in your domain. Most design happens based on assumptions and it is highly recommended to make them explicit. This can be done in this section of the Bounded Context Design Canvas.
Verification Metrics
Domain Driven Design is about an iterative approach towards modelling and design based on continuous learning. Metrics can help you gathering valuable input for those learnings (think about build-measure-learn). Think about metrics that you and your team can define in order to gather learnings if the chosen boundaries of your bounded context are a good fit or not.
You can collect those metrics for instance from:
Your CI / CD environments
Tools like JIRA
From your live systems
Open Questions
If you have questions that no one in the room can answer while running a workshop you can enter them into this section of the canvas. This way you can make sure that no open questions get lost but you can also get a visual indicator how certain the team is regarding the design of a given bounded context. Many questions are a good indicator towards a high degree of uncertainty.
Example
Below a filled-in version of the Bounded Context Canvas.
Tools
Here are some tools that can help you to use the Bounded Context Canvas.
HTML Version
A HTML version of the canvas you can edit in a browser and version in source control alongside your code. Contributed by Nelson da Costa.
Miro Version
A free MiroHQ template of the Bounded Context Canvas.
The current version of the template on Miroverse is v4 at the moment. In the meantime, you can download a Miro board backup here from this repository
draw.io Version
A draw.io template of the canvas containing the Bounded Context Canvas as template.
Excalidraw Version
A Excalidraw template of the canvas containing the Bounded Context Canvas as template.
Lucidchart Version
A Lucidchart template of the canvas containing the Bounded Context Canvas as template.
Design Tips
By making the important elements of a bounded context's design visible on the canvas, you can more easily challenge and improve the design. Here are some tips help you challenge and improve a design.
Please feel free to create a Pull Request sharing your tips.
General Tips
Experiment by moving something on the canvas to another context. How is the design affected?
Interface Design Tips
The public interface of a bounded context is its contract with the rest of the system. Contracts have a big impact on collaborators and are hard to change, so good design is vital. Here are some tips to help you critique the design of a bounded context's interface.
Are the names of messages coherent with each other and the description of the context?
Is each message type optimal (e.g. should a command be an event)?
Is the interface too big (too many unique message types)?
Is the context exposing too much of its internals?
Do any messages seem like they should belong elsewhere?
Additional Resources
Bounded Context Canvas V3: Simplifications and Additions
Extending the Bounded Context Canvas with BDD Examples
Translations
All resources are available in French and in Portuguese.
Contributors
Thanks to all existing and future contributors and to the following individuals who have all contributed to the Bounded Context Canvas:
Kenny Baas
Kim Lindhard
Michael Plöd
Maxime Sanglan-Charlier
A significant contribution to the Bounded Context Canvas was the inspiration of the Business Model Canvas.
Contributions and Feedback
The Bounded Context Canvas is freely available for you to use. In addition, your feedback and ideas are welcome to improve the canvas or to create new versions.
Feel free to also send us a pull request with your examples or with new translations.
This work is licensed under a Creative Commons Attribution 4.0 International License.
About
A structured approach to designing and documenting each of your bounded contexts
Topics
domain-driven-design
Resources
Readme
License
CC-BY-SA-4.0 license
Uh oh!
There was an error while loading. Please reload this page.
Activity
Custom properties
Stars
2k stars
Watchers
82 watching
Forks
191 forks
Report repository
Releases
No releases published
Packages 0
No packages published
Uh oh!
There was an error while loading. Please reload this page.
Contributors 19
+ 5 contributors
Languages
HTML 100.0%
Footer
© 2026 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Community
Docs
Contact
Manage cookies
Do not share my personal information
You can't perform that action at this time.
