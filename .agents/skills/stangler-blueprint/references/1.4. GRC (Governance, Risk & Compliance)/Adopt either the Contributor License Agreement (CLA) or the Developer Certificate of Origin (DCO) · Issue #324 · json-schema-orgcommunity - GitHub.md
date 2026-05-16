---
name: Adopt either the Contributor License Agreement (CLA) or the Developer Certificate of Origin (DCO) · Issue #324 · json-schema-org/community - GitHub
keywords: (placeholder)
metadata:
  url: https://github.com/json-schema-org/community/issues/324
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T23:03:23.186Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
Adopt either the Contributor License Agreement (CLA) or the Developer Certificate of Origin (DCO) · Issue #324 · json-schema-org/community
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
json-schema-org / community Public
Sponsor
Sponsor json-schema-org/community
GitHub Sponsors
Learn more about Sponsors  json-schema-org json-schema-org Sponsor
External links
 opencollective.com/ json-schema Learn more about funding links in repositories. Report abuse
Notifications You must be signed in to change notification settings
Fork 75
Star 127
Code
Issues 59
Pull requests 6
Discussions
Actions
Wiki
Security and quality 0
Insights
Additional navigation options
Code
Issues
Pull requests
Discussions
Actions
Wiki
Security and quality
Insights
Adopt either the Contributor License Agreement (CLA) or the Developer Certificate of Origin (DCO) #324
New issue
Copy link
New issue
Copy link
Open
Listed in
#129
Open
Adopt either the Contributor License Agreement (CLA) or the Developer Certificate of Origin (DCO) #324
Listed in
#129
Copy link
Labels
Status: Do not close This is a long term issue with dependant issues. This label prevent it to be closed automatically. This is a long term issue with dependant issues. This label prevent it to be closed automatically.
Description
Relequestual
opened on Feb 8, 2023
· edited by Relequestual
Edits
Member
Issue body actions
I'm going to recommend using DCO, as it is less problematic for potential contributors.
Activity
Relequestual
mentioned this on Feb 8, 2023
Complete OpenJSF onboard #129
Relequestual commented on Feb 8, 2023
Relequestual
on Feb 8, 2023
Member Author
More actions
I am going to query re the OpenJS Foundations IP Policy...
Except as may be approved by the Board:
All new code contributions to any Project shall be made under the Project Code License accompanied by a Developers Certificate of Origin (DCO, available at http://developercertificate.org/), which will bind the individual contributor and, if applicable, their employer to the Project Code License.
All outbound code files will be made available under the Project Code License.
All documentation, image, and audiovisual files (e.g., .txt., .rtf, .doc, .pdf, .jpg, .tif, .mp3, .wav, and some .html files) (including without limitation code that is intended as sample code if included in a documentation file) will be contributed to the Project and made available under one of the following licenses selected by the Project's technical governing body (the “Project Documentation License”):
Creative Commons Attribution 4.0 International License (CC BY 4.0) (available at http://creativecommons.org/licenses/by/4.0/), or
The MIT License (available at https://opensource.org/licenses/MIT).
Are our specification documents "code" here?
I don't think they would be "documentation".
Julian commented on Feb 8, 2023
Julian
on Feb 8, 2023
· edited by Julian
Edits
Member
More actions
I can't 100% be sure what the first line there means ("Except as may be approved by the Board:") but I think it means we can ask for an exception to all of that. If it does, I would probably love it if we did so -- CLAs are IMHO (and in the O of at least a few more knowledgeable other folks I think) at best somewhat useless and at worst actively scare away contributors. I certainly know of places where you cannot contribute to a project with a CLA if you're employed somewhere where it'd be otherwise ok.
See also e.g. (random first google links though I've seen all of these previously):
https://ben.balter.com/2018/01/02/why-you-probably-shouldnt-add-a-cla-to-your-open-source-project/
https://www.linuxjournal.com/content/contributor-agreements-considered-harmful
https://drewdevault.com/2018/10/05/Dont-sign-a-CLA.html
https://sfconservancy.org/blog/2014/jun/09/do-not-need-cla/
(If we really must, fine, but otherwise for our own purposes, I don't think we should have a reason why we want to have this. My 0.02 though.)
Relequestual commented on Feb 9, 2023
Relequestual
on Feb 9, 2023
Member Author
More actions
I somewhat agree @Julian! I don't think we would want a CLA. I do think that having a DCO avoids potential problems later.
Drew has a follow up article on DCOs: https://drewdevault.com/2021/04/12/DCO.html
CLA is "easier" for people to do, clicking a few buttons, but probably results in more people not actually getting legal involved.
DCO is "harder", but doesn't require legal involvement. Autoamtion has been made easier.
A common compliant was each commit needs to be signed, but one automation tool got updated to enable the retroactive signing of previous commits: dcoapp/app#147 - "Individual remediation commit support".
@Julian if you'd like to make a case to the OpenJS Foundation board that we should be exempt, then let's discuss.
I guess first we need to work out/find specific reasons for wanting it, and consider if we align with those situations or not.
benjagm commented on Feb 9, 2023
benjagm
on Feb 9, 2023
Collaborator
More actions
I agree in everything said. DCO will fit much better for JSON Schema. The only possible side effect of choosing DCO vs CLA is how the organization is implementing it. It can be done learning from Node.js and Electron (both Impact projects at OpenJS). They implemented DCO as simple as: "Contributor only has to add the Signed-off-by line in their commits".
Choose DCO or CLA electron/governance#441 (comment)
Guidance for DCO (and DCO vs. CLA) openjs-foundation/cross-project-council#387 (comment)
Git provides the -s flag for git commit, which adds the following text to your commit message: Signed-off-by: John Doe <johndoe@acme.com>
Other findings on my research:
CLAs tends to create a contribution-hostile developer experience.
CLAs shifts legal blame to the party least equipped to defend against it
Orgs choosing CLA purposely choose to prioritize minimizing legal risk vs over maximizing the project's potential community.
DCO offers the maintainers the same rights that they extended to the community themselves.
The DCO gives developers greater flexibility and portability for their contributions.
The DCO 'fixes' two issues with the typical CLA. Firstly, it does not contain a separate license. Secondly, the DCO does not involve a lengthy, one-time, signature process but is instead covered in every commit by the “Signed-off-by” phrase.
The aspects of executing a DCO that make the process heavier than a CLA seem to be side-effects of how organizations implement DCOs, not intrinsic aspects of them.
References:
https://drewdevault.com/2021/04/12/DCO.html
https://ben.balter.com/2018/01/02/why-you-probably-shouldnt-add-a-cla-to-your-open-source-project/
https://about.gitlab.com/blog/2017/11/01/gitlab-switches-to-dco-license/
https://opennebula.io/switching-from-cla-to-a-dco-for-source-code-contributions/
https://medium.com/@flamefew/clas-and-using-dco-clearly-e46b09a4c048
Choose to use a CLA, a DCO, or neither ampproject/meta-tsc#25 (comment)
Guidance for DCO (and DCO vs. CLA) openjs-foundation/cross-project-council#387 (comment)
kevinswiber commented on Feb 9, 2023
kevinswiber
on Feb 9, 2023
More actions
I certainly know of places where you cannot contribute to a project with a CLA if you're employed somewhere where it'd be otherwise ok.
They are relying on a gray area in case they ever want to claim ownership over and revoke their commits. A CLA makes all this explicit and clear.
Orgs choosing CLA purposely choose to prioritize minimizing legal risk vs over maximizing the project's potential community.
This is different when the organization is a non-profit that's community-centered. It's one thing to explicitly sign-off on rights and property transferring to a big tech company, and it's another thing when they're being transferred to the community itself.
The aspects of executing a DCO that make the process heavier than a CLA seem to be side-effects of how organizations implement DCOs, not intrinsic aspects of them.
And the reality is... you'll probably never have an issue around this.
I would think the DCO is good for JSON Schema, and yet the CLA might actually offer better protection against unsavory litigators. Again, though, how likely is this to be an issue on a project that's run by a non-profit? That's the risk that needs to be weighed.
gregsdennis commented on Feb 9, 2023
gregsdennis
on Feb 9, 2023
Member
More actions
How do people here know what these things are? As a person wholly uneducated on this topic, where can I find information comparing the two concepts without having to read through all of the linked literature above?
benjagm commented on Feb 9, 2023
benjagm
on Feb 9, 2023
Collaborator
More actions
How do people here know what these things are? As a person wholly uneducated on this topic, where can I find information comparing the two concepts without having to read through all of the linked literature above?
I found these 2 videos very insightful:
https://youtu.be/M9czSZMPCMA
https://youtu.be/TV9EhzfjepA
👍 React with 👍 2 gregsdennis and Relequestual
benjagm commented on Feb 9, 2023
benjagm
on Feb 9, 2023
Collaborator
More actions
Found this cool GitHub automation to easily implement DCO: https://github.com/dcoapp/app
Source: https://opensource.guide/legal/#does-my-project-need-an-additional-contributor-agreement
github-actions commented on Jan 11, 2025
github-actions bot
on Jan 11, 2025 – with GitHub Actions
More actions
Hello! 👋
This issue has been automatically marked as stale due to inactivity 😴
It will be closed in 180 days if no further activity occurs. To keep it active, please add a comment with more details.
There can be many reasons why a specific issue has no activity. The most probable cause is a lack of time, not a lack of interest.
Let us figure out together how to push this issue forward. Connect with us through our slack channel : https://json-schema.org/slack
Thank you for your patience ❤
github-actions
added
Status: Stale It's believed that this issue is no longer important to the requestor. It's believed that this issue is no longer important to the requestor.
on Jan 11, 2025
littledan commented on Jan 12, 2025
littledan
on Jan 12, 2025
More actions
The issue here is more about minimizing liability for the organization using the licensed software/standard, not just the host org. Guaranteeing legal certainty is an important goal to promote adoption. Companies are increasingly checking the underlying IP of open source software they use. For standards, a good CLA can provide this certainty.
If the idea is to standardize JSON Schema via OpenJSF, it may be easiest to use the LF's common schemes for publishing standards, around the Community Specification License, which uses a CLA for this purpose of ensuring limited liabilty for downstream users. The whole process can be easily automated by reusing some bots. Would this option be attractive for the group?
Relequestual
added
Status: Do not close This is a long term issue with dependant issues. This label prevent it to be closed automatically. This is a long term issue with dependant issues. This label prevent it to be closed automatically.
and removed
Status: Stale It's believed that this issue is no longer important to the requestor. It's believed that this issue is no longer important to the requestor.
on Jan 13, 2025
Sign up for free to join this conversation on GitHub. Already have an account? Sign in to comment
Metadata
Metadata
Assignees
No one assigned
Labels
Status: Do not close This is a long term issue with dependant issues. This label prevent it to be closed automatically. This is a long term issue with dependant issues. This label prevent it to be closed automatically.
Type
No type
Fields
Give feedback
No fields configured for issues without a type.
Projects
No projects
Milestone
No milestone
Relationships
None yet
Development
No branches or pull requests
Participants
    
+1
Issue actions
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
