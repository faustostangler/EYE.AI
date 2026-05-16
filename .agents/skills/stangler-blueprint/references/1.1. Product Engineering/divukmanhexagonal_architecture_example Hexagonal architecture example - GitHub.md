---
name: divukman/hexagonal_architecture_example: Hexagonal architecture example - GitHub
keywords: (placeholder)
metadata:
  url: https://github.com/divukman/hexagonal_architecture_example
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
GitHub - divukman/hexagonal_architecture_example: Hexagonal architecture example · GitHub
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
divukman / hexagonal_architecture_example Public
Notifications You must be signed in to change notification settings
Fork 0
Star 1
Code
Issues 0
Pull requests 0
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
divukman/hexagonal_architecture_example
main
1 Branch 0 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
GPL-3.0 license
Hexagonal Architecture With Spring Boot
Hexagonal architecture example
WIP project that aims to have a basic structure of hexagonal infrastructure setup with spring boot example...
Ports: Interfaces in core (domain)
Adapters: Implementations of ports
API: that which drives the core (web api for example)
SPI (Service provider interface): that which is driven by core (database for example)
Example
Core defines interfaces (ports) for the input (API) and for the output (SPI)
Input adapters (API)
Web input adapter implements one of the ports and exposes a web api that drives the core
Different input adapters can drive the logic, for example pubsub subscription etc...
Output adapters (SPI)
Firebase output adapter implements one of the ports and provides means for persisting the data (in firebase)
Different output adapters can implement output port, for example Postgres adapter to store data into the database...
Config
If you are using a firebase project: https://firebase.google.com/docs/admin/setup
Or you can have a dummy adapter that stores data into h2 for example...
Update the application-dev.properties file with following:
Run the project
About
Hexagonal architecture example
Resources
Readme
License
GPL-3.0 license
Uh oh!
There was an error while loading. Please reload this page.
Activity
Stars
1 star
Watchers
1 watching
Forks
0 forks
Report repository
Releases
No releases published
Packages 0
No packages published
Contributors 2
 dimitarvukman
 divukman Dimitar
Languages
Java 100.0%
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
