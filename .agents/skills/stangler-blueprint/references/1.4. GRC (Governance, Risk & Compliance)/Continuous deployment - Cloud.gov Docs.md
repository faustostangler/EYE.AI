---
name: Continuous deployment - Cloud.gov Docs
keywords: (placeholder)
metadata:
  url: https://docs.cloud.gov/platform/management/continuous-deployment/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T19:00:57.430Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
Continuous deployment | Cloud.gov Docs
Skip to main content 
An official website of the United States government
Here's how you know
Here's how you know
Official websites use .gov
A .gov website belongs to an official government organization in the United States.
Secure .gov websites use HTTPS
A lock ( Locked padlock icon ) or https:// means you've safely connected to the .gov website. Share sensitive information only on official, secure websites.
Cloud.gov Docs Platform Pages Workshop News Knowledge base Release Notes
GitHub ctrl K
Cloud.gov Docs
Platform
Pages
Workshop
News
Knowledge base
Release Notes
GitHub
← Back to main menu
Overview
Technology and security
Getting Started
Deploying apps
Services
Managing apps
Cloning applications
Container-to-Container Networking
Continuous deployment
Custom domains
Perform a database backup or restore
Security-related HTTP headers
Leveraging Cloud.gov authentication
Set org, space, and app limits
Moving apps between spaces
Running multiple instances
Running one-off tasks
CF CLI plugins
Production-ready guide
Renaming spaces
Controlling egress traffic
Connect to external services
Deploying static sites
Troubleshooting
Using SSH
Managing orgs
Security and Compliance
Logs
Managing apps
Continuous deployment
On this page
Continuous deployment
Setting up continuous deployment allows you to automatically upload your changes to your desired environment.
Get ready 
Before setting up continuous deployment:
Go through the production-ready guide to ensure your application uses the core best practices and zero-downtime deployment. This will help you use continuous deployment with reduced risk of errors and outages.
The essential requirements: your code needs to be in version control, and it needs to include a manifest.yml file that captures the intended deployment configuration for your application.
Set up continuous integration. This will protect you from deploying a broken application. You can use the same service for continuous integration and continuous deployment — see the list of continuous integration services below for suggestions.
Provision deployment credentials 
Continuous deployment systems require credentials for use in pushing new versions of your application code to Cloud.gov. You should use a restricted set of credentials that can only access a particular target space, rather than credentials tied to a user who has more access, or who may lose access when leaving your team or project. This "least privilege" approach minimizes the harm that is possible if the credentials are compromised in any way.
To create deployer account credentials with permission to deploy to a single space, set up a service account.
Configure your service 
Cloud.gov does not provide a CI/CD (continuous integration/continuous deployment) service, but you can use any CI/CD service of your choice.
You can configure your code repositories, spaces, and CI/CD service together to enable automated or semi-automated deployments to your environments (such as development, staging, and production environments). For deployments in each environment, you can configure access control and testing requirements according to your project's needs.
The core concept is to set up a script that triggers when you update the material that you want to test and deploy (typically your code in your version control system). The script runs your commands, including your deploy command, using your service account credentials.
To illustrate how a CI/CD workflow could be incorporated with cloud.gov:
Cloud.gov
Org
Production space
Staging space
Dev space
Commit code
Automatically notify that a commit happened
If dev branch, deploy
If staging branch, deploy
If prod branch, deploy
App
App
App
Developer
Code repository
Continuous Deployment service
Another example of a CI/CD workflow (this illustration omits the org/space boundaries):
Commit code
Automatically notify that a commit happened
If dev branch, deploy
If prod branch, deploy, run tests
Test results
If preprod tests OK, deploy prod branch
Developer
Code repository
Continuous Deployment service
Dev app on Cloud.gov
Preprod app on Cloud.gov
Prod app on Cloud.gov
Service examples 
Here are examples of how to set up three cloud-based services that have free tiers for open source projects:
Travis
CircleCI
GitHub.
Travis 
See the Travis documentation.
Use api: https://api.fr.cloud.gov
You must encrypt the password, and you must escape any symbol characters in the password, to prevent possible situations where Travis could dump an error message that contains passwords or environment variables.
For more information about configuring Travis, see Customizing the Build.
Using Conditional Deployments with Travis 
A common pattern for team workflows is to use separate development and main branches, along with using a staging or QA deployment with the development branch, and a production deployment with the main branch. This can be achieved in Travis with on: to specify a branch, and using unique manifests for each deployment.
Each manifest should at the very least define an unique name , but can also define an unique host . Also, it may be necessary to define unique services for each application to use. See Cloning Applications for more information.
Jekyll with Travis 
To deploy a Jekyll site, add the following to your .travis.yml :
For details, see Jekyll's Continuous Integration guide.
CircleCI 
See Getting Started with CircleCI -- you'll need to set up a CircleCI account and give it access to your code repository.
In your code repository, use the following template to set up your .circleci/config.yml file.
Replace DEPLOYER_SERVICE_ACCOUNT_USERNAME , ORG , and SPACE with your information. Do not replace $CF_PASS with your deployer service account password -- instead, export the CF_PASS environment variable in the CircleCI interface and put the deployer password there.
You can also review their sample .circleci/config.yml file for more configuration options.
Note: If your manifest.yml describes more than one app, you might want to specify which app to push in the cf push line.
GitHub Actions 
See the GitHub Actions documentation to get started, and this pre-made GitHub Action.
Usage 
After following the instructions for setting up a Cloud.gov service account, store your username (CG_USERNAME) and password (CG_PASSWORD) as encrypted secrets.
Sample workflow 
The following is an example of a workflow that uses this action. This example shows how to deploy a simple .NET Core app to Cloud.gov
Note the reference to cloud-gov/cg-cli-tools@main in the workflow file above. You can use another workflow file as part of your deployment process if you desire, or add additional steps to your workflow by referencing other GitHub actions.
Previous Container-to-Container Networking
Next Custom domains 
GSA.gov
An official website of the U.S. General Services Administration
About GSA
Accessibility statement
FOIA requests
No FEAR Act data
Office of the Inspector General
Performance reports
Privacy policy
Looking for U.S. government information and services?
Visit USA.gov
