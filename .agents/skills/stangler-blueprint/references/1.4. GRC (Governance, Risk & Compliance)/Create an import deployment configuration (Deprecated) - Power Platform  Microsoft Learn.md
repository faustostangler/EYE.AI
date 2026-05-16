---
name: Create an import deployment configuration (Deprecated) - Power Platform | Microsoft Learn
keywords: (placeholder)
metadata:
  url: https://learn.microsoft.com/en-us/power-platform/guidance/alm-accelerator/create-import-deployment-configuration
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T19:00:57.430Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
Create an import deployment configuration (Deprecated) - Power Platform | Microsoft Learn
Skip to main content Skip to Ask Learn chat experience
Microsoft Build 2026
June 2-3, 2026
Go deep on real code and real systems in San Francisco and online
Learn more
Dismiss alert
This browser is no longer supported.
Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support.
Download Microsoft Edge More info about Internet Explorer and Microsoft Edge
Learn 
Suggestions will filter as you type
Sign in  
Profile
Analytics
Settings
Sign out 
Learn
Documentation
All product documentation
Azure documentation
Dynamics 365 documentation
Microsoft Copilot documentation
Microsoft 365 documentation
Power Platform documentation
Code samples
Troubleshooting documentation Register now. Spots filling fast Microsoft Build Build, ship, and scale with AI-first tools and platforms.
Training & Labs
All training
Azure training
Dynamics 365 training
Microsoft Copilot training
Microsoft 365 training
Microsoft Power Platform training
Labs
Credentials
Career paths Register now. Spots filling fast Microsoft Build Build, ship, and scale with AI-first tools and platforms.
Q&A
Ask a question
Azure questions
Windows questions
Microsoft 365 questions
Microsoft Outlook questions
Microsoft Teams questions
Popular tags
All questions Register now. Spots filling fast Microsoft Build Build, ship, and scale with AI-first tools and platforms.
Topics
Agents Key concepts and resources for agentic computing
Artificial intelligence Learning hub to build AI skills
DevOps DevOps practices, Git version control and Agile methods
Learn for Organizations Curated offerings from Microsoft to boost your team's technical skills
Platform engineering Tools from Microsoft and others to build personalized developer experiences
Security Guidance to help you tackle security challenges
Assessments Interactive guidance with custom recommendations
Student hub Self-paced and interactive training for students
Educator center Resources for educators to bring technical innovation in their classroom Register now. Spots filling fast Microsoft Build Build, ship, and scale with AI-first tools and platforms.
Suggestions will filter as you type
Sign in  
Profile
Analytics
Settings
Sign out
Power Platform
Get started
Admin guide
ALM guide
Developer guide
Training
Products
Power Apps
Power Automate
Power BI
Power Pages
Copilot Studio
Guidance
Adoption
Architecture
Case studies
Toolkits
Well-Architected
Troubleshooting
Get help and support
Troubleshooting articles
Release plans
Resources
Community
Blog
Geographical availability
Language availability
More
Get started
Admin guide
ALM guide
Developer guide
Training
Products
Power Apps
Power Automate
Power BI
Power Pages
Copilot Studio
Guidance
Adoption
Architecture
Case studies
Toolkits
Well-Architected
Troubleshooting
Get help and support
Troubleshooting articles
Release plans
Resources
Community
Blog
Geographical availability
Language availability
Table of contents Exit editor mode
Learn
Power Platform
Guidance
Learn
Power Platform
Guidance
Ask Learn Ask Learn
Reading mode Table of contents Read in English Add to Collections Add to plan Edit
Copy Markdown Print
Note
Access to this page requires authorization. You can try signing in or changing directories.
Access to this page requires authorization. You can try changing directories.
Create an import deployment configuration
Feedback
Summarize this article for me
In this article
Prerequisites
Create a development environment step in your deployment profile
Create an import deployment configuration for your solution
Commit deployment settings to source control
Validate the import deployment configuration
Note
The ALM Accelerator is deprecated and no new features are being added. Issues are no longer reviewed or addressed.
If you identify a potential security issue, please report it to the Microsoft Security Response Center.
Use Pipelines in Power Platform to bring ALM automation capabilities to Power Platform and Dynamics 365 services. Pipelines can be used with source code integration or extended to integrate with Azure DevOps, GitHub, and other providers.
Makers can use ALM Accelerator components to apply source control strategies with Azure DevOps, including fully automated builds and deployments, without needing intimate knowledge of downstream technologies or manual intervention. The ability to import solutions from source control into a maker environment is a key component of the ALM Accelerator. When makers import a solution from source control, they can select a deployment configuration file that contains connection information, environment variables, and other settings that are used to configure the solution.
Prerequisites
The unmanaged solution must exist in an environment before the deployment configuration is created.
The environment into which the solution is imported must exist and have connections configured, either using the ALM Accelerator when creating the deployment configuration or manually in the environment.
To import a solution from source control into an empty environment, first create a deployment configuration based on the unmanaged solution.
Create a development environment step in your deployment profile
Create a deployment step in the deployment profile for your solution.
Open the ALM Accelerator administration app.
Select Deployment Profiles, and then select the deployment profile for your solution.
Select New Deployment Step, and then provide a unique name for the step, such as My Development Environment.
Set Step Type to Development.
Set Step Number to 4.
Set Build Template Path to, for example, /Pipelines/build-deploy-dev-SampleSolution.yml.
Create a new environment and set the Environment Name and URL based on your development environment.
Save the deployment step.
Create an import deployment configuration for your solution
Open the ALM Accelerator app.
Make sure the profile you updated is selected as the solution deployment profile, and then select Configure Deployment Settings under your solution. Your new deployment step should be listed in the Select an Environment to Configure section.
Select the environment you created.
Configure the deployment settings for the development environment.
Select Save and Close.
Commit deployment settings to source control
On the ALM Accelerator app home page, select Commit Solution in the solution list.
Enter notes and select or create a branch.
Select Commit Solution.
Validate the import deployment configuration
On the ALM Accelerator app home page, select Import Solution.
Select the profile you updated, and then select the branch you committed as the Solution Source.
Select the solution folder. You may need to refresh (Ctrl+F5) the app to see the new solution folder.
Select the deployment configuration you committed to source control, and then select Import Solution.
Feedback
Was this page helpful?
Yes No No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
Additional resources
Training
Module
Explore Infrastructure as Code and Configuration Management - Training
Learn Infrastructure as Code (IaC) foundational concepts, environment deployment strategies, configuration management approaches, and idempotent configuration principles for automated infrastructure operations.
Certification
Microsoft Certified: Azure Developer Associate - Certifications
Build end-to-end solutions in Microsoft Azure to create Azure Functions, implement and manage web apps, develop solutions utilizing Azure storage, and more.
Events
Agent Academy
May 12, 8 AM - May 12, 2 PM
Agent Academy goes live May 12. Level up on Copilot Studio agents.
Register free
Last updated on 02/27/2026
In this article
Prerequisites
Create a development environment step in your deployment profile
Create an import deployment configuration for your solution
Commit deployment settings to source control
Validate the import deployment configuration
Was this page helpful?
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
Ask Learn
Preview
Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
Sign in
English (United States)
Your Privacy Choices
Theme
Light
Dark
High contrast
AI Disclaimer
Previous Versions
Blog
Contribute
Privacy
Consumer Health Privacy
Terms of Use
Trademarks
© Microsoft 2026
