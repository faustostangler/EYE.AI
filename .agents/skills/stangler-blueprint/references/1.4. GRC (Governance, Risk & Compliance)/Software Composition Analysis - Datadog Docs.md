---
name: Software Composition Analysis - Datadog Docs
keywords: (placeholder)
metadata:
  url: https://docs.datadoghq.com/security/code_security/software_composition_analysis/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T23:03:23.186Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
Software Composition Analysis
For AI agents: A markdown version of this page is available at https://docs.datadoghq.com/security/code_security/software_composition_analysis.md. A documentation index is available at /llms.txt.
Join Datadog at DASH in NYC, June 9-10. | The future of AI + Observability starts here. DASH NYC, June 9-10 | AI + Observability
Product The integrated platform for monitoring & security
Observability
Security
Digital Experience
Software Delivery
Service Management
AI
Platform Capabilities View Product Pricing Observability End-to-end, simplified visibility into your stack's health & performance Infrastructure
Infrastructure Monitoring
Metrics
Network Monitoring
Container Monitoring
Kubernetes Autoscaling
Serverless
Cloud Cost Management
Cloudcraft
Storage Management
GPU Monitoring Applications
Application Performance Monitoring
Universal Service Monitoring
Continuous Profiler
Dynamic Instrumentation
LLM Observability Data
Database Monitoring
Data Streams Monitoring
Quality Monitoring
Jobs Monitoring Logs
Log Management
Sensitive Data Scanner
Audit Trail
Observability Pipelines
Error Tracking
BYOC Log Management Infrastructure Applications Data Logs Security Detect, prioritize, and respond to threats in real-time Code Security
Code Security
Software Composition Analysis
Static Code Analysis (SAST)
Runtime Code Analysis (IAST)
IaC Security
Secret Scanning Cloud Security
Cloud Security
Cloud Security Posture Management
Cloud Infrastructure Entitlement Management
Vulnerability Management
Compliance Threat Management
Cloud SIEM
Workload Protection
App and API Protection
Sensitive Data Scanner Security Labs
Security Labs Research
Open Source Projects Digital Experience Optimize front-end performance and enhance user experiences Digital Experience
Browser Real User Monitoring
Mobile Real User Monitoring
Product Analytics
Experiments
Session Replay
Synthetic Monitoring
Mobile App Testing
Error Tracking Related Products
Continuous Testing
Dashboards
Application Performance Monitoring Software Delivery Build, test, secure and ship quality code faster Software Delivery
Internal Developer Portal
CI Visibility
Test Optimization
Continuous Testing
IDE Plugins
DORA Metrics
Feature Flags
Code Coverage Related Products
Software Composition Analysis
Application Performance Monitoring
Synthetic Monitoring
Browser Real User Monitoring
Workflow Automation
integrations Service Management Integrated, streamlined workflows for faster time-to-resolution Service Management
Incident Response
Software Catalog
Service Level Objectives
Case Management Actions
Workflow Automation
App Builder Agentic & Embedded
Bits AI SRE
Watchdog
Event Management AI Monitor and improve model performance. Pinpoint root causes and detect anomalies AI Observability
LLM Observability
GPU Monitoring
AI Integrations Agentic & Embedded
Bits AI Agents
Bits AI SRE
Bits AI Security Analyst
MCP Server
Agent Directory
Watchdog
Event Management Related Products
Incident Response
Workflow Automation
Application Performance Monitoring
Universal Service Monitoring
Log Management Platform Capabilities Built-in features & integrations that power the Datadog platform Built-in Features
Bits AI Agents
Metrics
Watchdog
Alerts
Dashboards
Notebooks
Mobile App
Fleet Automation
Governance Console
Access Control
DORA Metrics Workflows & Collaboration
Incident Response
Case Management
Event Management
Workflow Automation
App Builder
Cloudcraft
CoScreen
Teams Extensibility
OpenTelemetry
integrations
IDE Plugins
MCP Server
Agent Directory
API
Marketplace
Customers
Pricing
Solutions Industry
Financial Services
Manufacturing & Logistics
Healthcare/Life Sciences
Retail/E-Commerce
Government
Education
Media & Entertainment
Technology
Gaming Technology
Amazon Web Services Monitoring
Azure Monitoring
Google Cloud Monitoring
Oracle Cloud Monitoring
Kubernetes Monitoring
Red Hat OpenShift
Pivotal Platform
OpenAI
SAP Monitoring
OpenTelemetry Use-case
Application Security
Cloud Migration
Monitoring Consolidation
Unified Commerce Monitoring
SOAR
DevOps
FinOps
Shift-Left Testing
Digital Experience Monitoring
Security Analytics
Compliance for CIS Benchmarks
Hybrid Cloud Monitoring
Edge Device Monitoring
Real-Time BI
On-Premises Monitoring
Log Analysis & Correlation
CNAPP
Docs
 Looking for Datadog logos? You can find the logo assets on our press page. Download Media Assets
About
Contact
Partners
Newsroom
Events & Webinars
Leadership
Careers
Analyst Reports
Investor Relations
ESG Report
Trust Hub
Blog
The Monitor
Engineering
AI
Security Labs
Login
GET STARTED FREE FREE TRIAL
Toggle navigation
 Home
 Docs
 API
search
Agents
Essentials
Getting Started
Agent
API
APM Tracing
Containers
Autodiscovery
Datadog Operator
Dashboards
Database Monitoring
Datadog
Datadog Site
DevSecOps
Incident Management
Integrations
AWS
Azure
Google Cloud
OCI
Terraform
Internal Developer Portal
Logs
Monitors
Notebooks
OpenTelemetry
Profiler
Search
Product-Specific Search
Session Replay
Security
App and API Protection
Cloud Security
Cloud SIEM
Code Security
Serverless for AWS Lambda
Software Delivery
CI Visibility
Feature Flags
Test Optimization
Test Impact Analysis
MCP Tools
Synthetic Monitoring and Testing
API Tests
Browser Tests
Mobile App Tests
Continuous Testing
Private Locations
Tags
Assigning Tags
Unified Service Tagging
Using Tags
Teams
Organization Topology
Workflow Automation
Learning Center
Support
Glossary
Standard Attributes
Guides
Agent
Architecture
IoT
Supported Platforms
AIX
Linux
Ansible
Chef
Heroku
MacOS
Puppet
SaltStack
SCCM
Windows
From Source
Log Collection
Log Agent tags
Advanced Configurations
Proxy
Transport
Multi-Line Detection
Configuration
Commands
Configuration Files
Log Files
Status Page
Network Traffic
Proxy Configuration
FIPS Compliance
Dual Shipping
Secrets Management
Fleet Automation
Remote Agent Management
Troubleshooting
Container Hostname Detection
Debug Mode
Agent Flare
Agent Check Status
NTP Issues
Permission Issues
Integrations Issues
Site Issues
Autodiscovery Issues
Windows Container Issues
Agent Runtime Configuration
High CPU or Memory Consumption
Guides
Data Security
Integrations
Guides
Client SDKs
Setup
Advanced Configuration
Data Collected
Integrated Libraries
Troubleshooting
Extend Datadog
Authorization
OAuth2 in Datadog
Authorization Endpoints
DogStatsD
Datagram Format
Unix Domain Socket
High Throughput Data
Data Aggregation
DogStatsD Mapper
Custom Checks
Writing a Custom Agent Check
Writing a Custom OpenMetrics Check
Integrations
Build an Integration with Datadog
Create an Agent-based Integration
Create an API-based Integration
Create a Log Pipeline
Integration Assets Reference
Build a Marketplace Offering
Create an Integration Dashboard
Create a Monitor Template
Create a Cloud SIEM Detection Rule
Install Agent Integration Developer Tool
Service Checks
Submission - Agent Check
Submission - DogStatsD
Submission - API
Community
Libraries
Guides
OpenTelemetry
Getting Started
Datadog Example Application
OpenTelemetry Demo Application
Feature Compatibility
Instrument Your Applications
Using OTel SDK
Using Datadog SDK
Send Data to Datadog
DDOT Collector (Recommended)
Other Setup Options
Semantic Mapping
Resource Attribute Mapping
Metrics Mapping
Infrastructure Host Mapping
Hostname Mapping
Service-entry Spans Mapping
Ingestion Sampling
Correlate Data
Logs and Traces
Metrics and Traces
RUM and Traces
DBM and Traces
Integrations
Apache Metrics
Apache Spark Metrics
Collector Health Metrics
Datadog Extension
Docker Metrics
HAProxy Metrics
Host Metrics
IIS Metrics
Kafka Metrics
Kubernetes Metrics
MySQL Metrics
PostgreSQL Metrics
NGINX Metrics
Podman Metrics
Runtime Metrics
SQL Server Metrics
Trace Metrics
Troubleshooting
Guides and Resources
Produce Delta Temporality Metrics
Visualize Histograms as Heatmaps
Instrument Unsupported Runtimes
Migration Guides
Reference
Terms and Concepts
Trace Context Propagation
Trace IDs
OTLP Metric Types
Administrator's Guide
Getting Started
Plan
Build
Run
API
Partners
Datadog Mobile App
Enterprise Configuration
Datadog for Intune
Shortcut Configurations
Push Notifications
Widgets
Guides
DDSQL Reference
Data Directory
CoScreen
Troubleshooting
CoTerm
Install
Using CoTerm
Configuration Rules
Remote Configuration
Cloudcraft (Standalone)
Getting Started
Account Management
Components: Common
Components: Azure
Components: AWS
Advanced
FAQ
API
AWS Accounts
Azure Accounts
Blueprints
Budgets
Teams
Users
In The App
Dashboards
Configure
Dashboard List
Widgets
Configuration
Widget Types
Querying
Functions
Algorithms
Arithmetic
Count
Exclusion
Interpolation
Rank
Rate
Regression
Rollup
Smoothing
Timeshift
Beta
Graph Insights
Metric Correlations
Watchdog Explains
Template Variables
Overlays
Annotations
Guides
Sharing
Shared Dashboards
Secure Embedded Dashboards
Share Graphs
Scheduled Reports
Notebooks
Analysis Features
Getting Started
Guides
DDSQL Editor
Reference Tables
Sheets
Functions and Operators
Guides
Monitors and Alerting
Draft Monitors
Configure Monitors
Monitor Templates
Monitor Types
Notifications
Notification Rules
Variables
Downtimes
Examples
Manage Monitors
Search Monitors
Check Summary
Monitor Status
Status Graphs
Status Events
Monitor Settings
Monitor Quality
Guides
Service Level Objectives
Monitor-based SLOs
Metric-based SLOs
Time Slice SLOs
Error Budget Alerts
Burn Rate Alerts
Guides
Metrics
Custom Metrics
Metric Type Modifiers
Historical Metrics Ingestion
Submission - Agent Check
Submission - DogStatsD
Submission - Powershell
Submission - API
OpenTelemetry Metrics
OTLP Metric Types
Query OpenTelemetry Metrics
Metrics Types
Distributions
Overview
Explorer
Metrics Units
Summary
Volume
Advanced Filtering
Nested Queries
Reference Table Joins with Metrics
Derived Metrics
Metrics Without Limits™
Guides
Watchdog
Alerts
Impact Analysis
RCA
Insights
Faulty Deployment Detection
Faulty Cloud & SaaS API Detection
Bits AI
Bits AI SRE
Investigate Issues
Take Action
Bits AI SRE Integrations and Settings
Knowledge Sources
Chat with Bits AI SRE
Bits AI Dev Agent
Setup
Bits AI Security Analyst
Bits Assistant
MCP Server
Setup
MCP Tools
Agent Builder
Internal Developer Portal
Software Catalog
Set Up
Entity Model
Troubleshooting
Scorecards
Scorecard Configuration
Custom Rules
Using Scorecards
Self-Service Actions
Software Templates
Engineering Reports
Reliability Overview
Scorecards Performance
DORA Metrics
Custom Reports
Developer Homepage
Campaigns
External Provider Status
Plugins
Integrations
Use Cases
API Management
Cloud Cost Management
App and API Protection
Developer Onboarding
Dependency Management
Production Readiness
Incident Response
CI Pipeline Visibility
Onboarding Guide
Error Tracking
Explorer
Issue States
Regression Detection
Suspected Causes
Error Grouping
Bits AI Dev Agent
Monitors
Issue Correlation
Identify Suspect Commits
Auto Assign
Issue Team Ownership
Track Browser and Mobile Errors
Browser Error Tracking
Collecting Browser Errors
Mobile Crash Tracking
Replay Errors
Real User Monitoring
Logs
Track Backend Errors
Getting Started
Exception Replay
Capturing Handled Errors
APM
Logs
Manage Data Collection
Ticketing Systems
Jira
Case Management
Link Pull Requests
Troubleshooting
Guides
Change Tracking
Feature Flags
Event Management
Ingest Events
Pipelines and Processors
Aggregation Key Processor
Arithmetic Processor
Date Remapper
Category Processor
Grok Parser
Lookup Processor
Remapper
Service Remapper
Status Remapper
String Builder Processor
Explorer
Searching
Navigate the Explorer
Customization
Facets
Attributes
Notifications
Analytics
Saved Views
Triage Inbox
Correlation
Configuration
Triaging & Notifying
Analytics
Maintenance Windows
Guides
Incident Response
Incident Management
Incident Investigation
Declare an Incident
Describe an Incident
Response Team
Notification
Timeline
Incident AI
Setup and Configuration
Information
Property Fields
Responder Types
Automations
Notification Rules
Templates
Variables
Integrations
Post Incident
Follow-ups
Postmortems
Analytics and Reporting
Guides
On-Call
Onboard a Team
Pages
Live Call Routing
Cross-org Paging
Routing Rules
Escalation Policies
Schedules
Handover automation
Profile Settings
Guides
Status Pages
Case Management
Projects
Settings
Create a Case
Customization
View and Manage Cases
Notifications and Integrations
Case Automation Rules
MCP Server
Troubleshooting
Actions & Remediations
Agent Builder
Workflow Automation
Build Workflows
Access and Authentication
Trigger Workflows
Variables and parameters
Actions
Workflow Logic
Save and Reuse Actions
Test and Debug
Expressions
Track Workflows
Limits
Apps
App Builder
Build Apps
Access and Authentication
Queries
Variables
Events
Components
Custom Charts
React Renderer
Tables
Reusable Modules
JavaScript Expressions
Embedded Apps
Input Parameters
Save and Reuse Actions
Datastores
Create and Manage Datastores
Use Datastores with Apps and Workflows
Automation Rules
Access and Authentication
Forms
Action Catalog
Connections
HTTP Request
AWS Integration
Google Workspace
Private Actions
Use Private Actions
Run a Script
Update the Private Action Runner
Private Action Credentials
Infrastructure
Cloudcraft
Overlays
Infrastructure
Observability
Security
Cloud Cost Management
Monitors
APM
Resource Catalog
Cloud Resources Schema
Policies
Resource Changes
Universal Service Monitoring
Setup
Guides
End User Device Monitoring
Hosts
Host List
Containers
Container Monitoring
Containers Explorer
Container Images Explorer
Kubernetes Explorer
Amazon ECS Explorer
Autoscaling
Cluster
Docker-based
APM
Log collection
Tag extraction
Integrations
Prometheus
Data Collected
Kubernetes
Installation
Migrate to the Datadog Operator
Further Configuration
Distributions
APM
App and API Protection
Log collection
Tag extraction
Integrations
Prometheus & OpenMetrics
Control plane monitoring
Data collected
kubectl Plugin
Datadog CSI Driver
Data security
Cluster Agent
Setup
Commands & Options
Cluster Checks
Endpoint Checks
Admission Controller
Amazon ECS
APM
Log collection
Tag extraction
Data collected
Managed Instances
AWS Fargate with ECS
Datadog Operator
Migrate to the Datadog Operator
Advanced Install
Configuration
Custom Checks
Data Collected
Secret Management
DatadogDashboard CRD
DatadogMonitor CRD
DatadogSLO CRD
Troubleshooting
Duplicate hosts
Cluster Agent
Cluster Checks
HPA and Metrics Provider
Admission Controller
Log Collection
Guides
Processes
Increase Process Retention
Serverless
AWS Lambda
Instrumentation
Managed Instances
Lambda Metrics
Distributed Tracing
Log Collection
Remote Instrumentation
Advanced Configuration
Continuous Profiler
Securing Functions
Deployment Tracking
OpenTelemetry
Troubleshooting
Lambda Web Adapter
FIPS Compliance
AWS Step Functions
Installation
Merge Step Functions and Lambda Traces
Enhanced Metrics
Redrive Executions
Distributed Map States
Troubleshooting
AWS Fargate
Azure App Service
Linux - Code
Linux - Container
Windows - Code
Azure Container Apps
In-Container
Sidecar
Azure Functions
Azure Logic Apps
Google Cloud Run
Containers
Jobs (Preview)
Functions
Functions (1st generation)
Libraries & Integrations
Glossary
Guides
Network Monitoring
Cloud Network Monitoring
Setup
Network Health
Network Analytics
Network Map
Guides
Supported Cloud Services
Terms and Concepts
DNS Monitoring
Network Device Monitoring
Setup
Integrations
Profiles
Configuration Management
Maps
SNMP Metrics Reference
Troubleshooting
Guides
Terms and Concepts
NetFlow Monitoring
Monitors
Network Path
Setup
List View
Path View
Monitors
Guides
Terms and Concepts
Storage Management
Amazon S3
Google Cloud Storage
Azure Blob Storage
Cloud Cost
Cloud Cost
Datadog Costs
Setup
Permissions
AWS
Azure
Google Cloud
Oracle
SaaS Integrations
Custom
Tags
Tag Explorer
Multisource Querying
Allocation
Tag Pipelines
Container Cost Allocation
BigQuery Costs
Custom Allocation Rules
AI Costs
Reporting
Scheduled Reports
Explorer
Dashboard
Recommendations
Custom Recommendations
Planning
Budgets
Forecasting
Commitment Programs
Cost Changes
Monitors
Anomalies
Real-Time Costs
Application Performance
APM
APM Terms and Concepts
Application Instrumentation
Single Step Instrumentation
Manually managed SDKs
Code-based Custom Instrumentation
Dynamic Instrumentation
Library Compatibility
Library Configuration
Configuration at Runtime
Trace Context Propagation
Serverless Application Tracing
Proxy Tracing
Span Tag Semantics
Span Links
APM Metrics Collection
Trace Metrics
Runtime Metrics
Trace Pipeline Configuration
Ingestion Mechanisms
Ingestion Controls
Adaptive Sampling
Processing Pipelines
Generate Metrics
Trace Retention
Usage Metrics
Correlate Traces with Other Telemetry
Correlate DBM and Traces
Correlate Logs and Traces
Correlate RUM and Traces
Correlate Synthetics and Traces
Correlate Profiles and Traces
Trace Explorer
Search Spans
Query Syntax
Trace Queries
Span Tags and Attributes
Span Visualizations
Trace View
Tag Analysis
Recommendations
Code Origin for Spans
Service Observability
Software Catalog
Service Page
Resource Page
Deployment Tracking
Service Map
Inferred Services
Remapping Rules for Inferred Entities
Service Remapping Rules
Tag Enrichment
Integration Override Removal
APM Monitors
Endpoint Observability
Explore Endpoints
Monitor Endpoints
Live Debugger
Error Tracking
Issue States
Error Tracking Explorer
Error Grouping
Monitors
Identify Suspect Commits
Exception Replay
Troubleshooting
Data Security
Guides
Troubleshooting
Agent Rate Limits
Agent APM metrics
Agent Resource Usage
Correlated Logs
PHP 5 Deep Call Stacks
.NET diagnostic tool
APM Quantization
Go Compile-Time Instrumentation
Tracer Startup Logs
Tracer Debug Logs
Connection Errors
SDK Configurations
Continuous Profiler
Enabling the Profiler
Supported Language and SDK Versions
Profile Types
Profile Visualizations
Investigate Slow Traces or Endpoints
Compare Profiles
Automated Analysis
Profiler Troubleshooting
Java
Python
Go
Ruby
Node.js
.NET
PHP
C/C++/Rust
Guides
Database Monitoring
Agent Integration Overhead
Setup Architectures
Setting Up Postgres
Self-hosted
RDS
Aurora
Google Cloud SQL
AlloyDB
Azure
Supabase
Heroku
Advanced Configuration
Troubleshooting
Setting Up MySQL
Self-hosted
RDS
Aurora
Google Cloud SQL
Azure
Advanced Configuration
Troubleshooting
Setting Up SQL Server
Self-hosted
RDS
Azure
Google Cloud SQL
Troubleshooting
Setting Up Oracle
Self-hosted
RDS
RAC
Exadata
Autonomous Database
Troubleshooting
Setting Up Amazon DocumentDB
Amazon DocumentDB
Troubleshooting
Setting Up MongoDB
Self-hosted
MongoDB Atlas
Troubleshooting
Setting Up ClickHouse
Self-hosted
ClickHouse Cloud
Connecting DBM and Traces
Data Collected
Collecting Custom Metrics
Exploring Custom Metrics
Exploring Database Hosts
Exploring Query Metrics
Exploring Query Samples
Exploring Database Schemas
Exploring Recommendations
Database Investigator
Troubleshooting
Guides
Data Streams Monitoring
Setup
Kafka
Setup
Schema Tracking
Dead Letter Queues
Metrics and Tags
Business Transaction Tracking
Data Observability
Data Observability Overview
Data Catalog
Quality Monitoring
Data Warehouses
Snowflake
Databricks
BigQuery
Redshift
Data Lakes
Iceberg Tables (AWS Glue)
ELT Integrations
Fivetran
Business Intelligence Integrations
Looker
Tableau
Sigma
Metabase
Power BI
Jobs Monitoring
Databricks
Airflow
Troubleshooting DAG
dbt
Spark on Kubernetes
Spark on Amazon EMR
Spark on Google Dataproc
AWS Glue
Custom Jobs (OpenLineage)
Datadog Agent for OpenLineage Proxy
Digital Experience
Real User Monitoring
Application Monitoring
Browser
Android and Android TV
iOS and tvOS
Flutter
Kotlin Multiplatform
React Native
Roku
Unity
Platform
Dashboards
Monitors
Generate Custom Metrics
Exploring RUM Data
Search RUM Events
Search Syntax
Group
Visualize
Events
Export
Saved Views
Watchdog Insights for RUM
Correlate RUM with Other Telemetry
Correlate LLM with RUM
Correlate Logs with RUM
Correlate Profiling with RUM
Correlate Synthetics with RUM
Correlate Traces with RUM
Feature Flag Tracking
Setup
Using Feature Flags
Error Tracking
Explorer
Issue States
Track Browser Errors
Track Mobile Errors
Error Grouping
Monitors
Identify Suspect Commits
Troubleshooting
AI Investigations
Single-View AI Investigation
RUM Without Limits
Metrics
Retention Filters
Retention Quotas
Operations Monitoring
Managed Archive
Ownership of Views
Guides
Data Security
Synthetic Testing and Monitoring
API Testing
HTTP
SSL
DNS
WebSocket
TCP
UDP
ICMP
GRPC
Error codes
Multistep API Testing
Browser Testing
Recording Steps
Browser Testing Results
Advanced Options for Steps
Authentication in Browser Testing
Network Path Testing
Terms and Concepts
Mobile Application Testing
Testing Steps
Testing Results
Advanced Options for Steps
Supported Devices
Restricted Networks
Settings
Test Suites
Platform
Dashboards
Metrics
Test Coverage
Private Locations
Connect APM
Settings
Scheduled Downtime
Exploring Synthetics Data
Saved Views
Results Explorer
Guides
Notifications
Template Variables
Conditional Alerting
Advanced Notifications
Integrate with Statuspage
Troubleshooting
Data Security
Continuous Testing
Local and Staging Environments
Testing Multiple Environments
Testing With Proxy, Firewall, or VPN
CI/CD Integrations
Configuration
Azure DevOps Extension
CircleCI Orb
GitHub Actions
GitLab
Jenkins
Bitrise (Upload Application)
Bitrise (Run Tests)
Settings
Results Explorer
Metrics
Guides
Troubleshooting
Experiments
Create Experiment Metrics
Plan and Launch Experiments
Read Experiment Results
Minimum Detectable Effects
Guides
Troubleshooting
Product Analytics
Charts
Chart Basics
Pathways Diagram
Funnel Analysis
Retention Analysis
Analytics Explorer
Dashboards
Segments
Managing Profiles
Data Collected
Guides
Troubleshooting
Session Replay
Browser
Setup
Privacy Options
Developer Tools
Troubleshooting
Mobile
Setup and Configuration
Privacy Options
Developer Tools
Impact on App Performance
Troubleshooting
Playlists
Heatmaps
Guides
Software Delivery
CI Visibility
Pipeline Visibility
AWS CodePipeline
Azure Pipelines
Buildkite
CircleCI
Codefresh
GitHub Actions
GitLab
Jenkins
TeamCity
Other CI Providers
Automatic Job Retries
Custom Commands
Custom Tags and Measures
Search and Manage
Explorer
Search Syntax
Search Pipeline Executions
Export
Saved Views
Monitors
Guides
Troubleshooting
CD Visibility
Deployment Visibility
Argo CD
CI Providers
Explore Deployments
Search Syntax
Facets
Saved Views
Features
Code Changes Detection
Rollback Detection
Monitors
Deployment Gates
Setup
Explore
Test Optimization
Setup
.NET
Java and JVM Languages
JavaScript and TypeScript
Python
Ruby
Swift
Go
JUnit Report Uploads
Network Settings
Tests in Containers
Explorer
Search Syntax
Search Test Runs
Export
Saved Views
Monitors
Test Health
Flaky Test Management
Working with Flaky Tests
Early Flake Detection
Auto Test Retries
Test Impact Analysis
How It Works
Troubleshooting
Setup
Developer Workflows
Code Coverage
Instrument Browser Tests with RUM
Instrument Swift Tests with RUM
Correlate Logs and Tests
Guides
Troubleshooting
Code Coverage
Setup
Configuration
Monorepo Support
Flags
Data Collected
PR Gates
Setup
DORA Metrics
Setup
Change Failure Detection
DORA Metrics Calculation
Data Collected
Feature Flags
Client SDKs
Android and Android TV
Angular
iOS and tvOS
JavaScript
React
React Native
Unity
Server SDKs
.NET
Go
Java
Node.js
Python
Ruby
Flag History
MCP Server
Guides
Developer Integrations
Source Code Integration
Source Code Management Providers
Service Mapping
Resource Mapping
Features
IDE Plugins
JetBrains IDEs
Error Tracking
Logs
Live Debugger
Code Security
VS Code & Cursor
Logs
Code Insights
Code Security
Exception Replay
Live Debugger
Security
Security Overview
Detection Rules
OOTB Rules
Notifications
Rules
Variables
Suppressions
Automation Pipelines
Mute
Add to Security Inbox
Set Due Date Rules
Security Inbox
Threat Intelligence
Events Forwarding
Audit Trail
Access Control
Account Takeover Protection
Ticketing Integrations
Research Feed
Security MCP Tools
Guides
Cloud SIEM
Ingest and Enrich
Content Packs
Bring Your Own Threat Intelligence
Open Cybersecurity Schema Framework
Detect and Monitor
OOTB Rules
Custom Detection Rules
Version History
Suppressions
Critical Assets
Historical Jobs
MITRE ATT&CK Map
Triage and Investigate
Investigate Security Signals
Risk Insights
IOC Explorer
Investigator
Respond and Report
Security Operational Metrics
Guides
Data Security
Code Security
Static Code Analysis (SAST)
Setup
Configuration
GitHub Actions
Generic CI Providers
AI-Enhanced Static Code Analysis
SAST Custom Rule Creation Tutorial
SAST Custom Rules
SAST Custom Rules Guide
Static Code Analysis (SAST) rules
Software Composition Analysis (SCA)
Static Setup
Runtime Setup
Configuration
Library Inventory
CVE Explorer
Secret Scanning
GitHub Actions
Generic CI Providers
Secret Validation
Runtime Code Analysis (IAST)
Setup
Security Controls
Infrastructure as Code (IaC) Security
Setup
GitHub Actions
Exclusions
Rules
Developer Tool Integrations
Pull Request Comments
PR Gates
IDE Plugins
Git Hooks
MCP Server
Troubleshooting
Guides
Cloud Security
Setup
Supported Deployment Types
Agentless Scanning
Deploy the Agent
Container Image Scanning in CI/CD
Set Up CloudTrail Logs
Set Up without Infrastructure Monitoring
Deploy using Cloud Integrations
Security Graph
Misconfigurations
Manage Compliance Rules
Create Custom Rules
Manage Compliance Posture
Explore Misconfigurations
Kubernetes Security Posture Management
Identity Risks
Vulnerabilities
Hosts and Containers Compatibility
OOTB Rules
Review and Remediate
Mute Issues
Automate Security Workflows
Severity Scoring
Guides
Troubleshooting
Vulnerabilities
Agentless Scanning
App and API Protection
Terms and Concepts
How It Works
Threat Intelligence
Trace Qualification
User Monitoring and Protection
Setup
Overview
Security Signals
Attackers Explorer
Attacker Fingerprint
Attacker Clustering
Users Explorer
Policies
Custom Rules
OOTB Rules
In-App WAF Rules
Tracing Library Configuration
Exploit Prevention
WAF Integrations
API Security Inventory
Guides
Troubleshooting
AI Guard
Get Started with AI Guard
Set Up AI Guard
Automatic Integrations
Manual Integrations
SDK
HTTP API
Security Signals
Workload Protection
Setup
Deploy the Agent
Workload Protection Agent Variables
Detection Rules
OOTB Rules
Custom Rules
Investigate Security Signals
Investigate Agent Events
Creating Agent Rule Expressions
Writing Custom Rule Expressions
Linux Syntax
Windows Syntax
Coverage and Posture Management
Hosts and Containers
Serverless
Coverage
Guides
Troubleshooting
Sensitive Data Scanner
Setup
Telemetry Data
Cloud Storage
Scanning Rules
Library Rules
Custom Rules
Guides
AI Observability
LLM Observability
Quickstart
Instrumentation
Automatic
SDK Reference
HTTP API
OpenTelemetry
Tracing Proxy Services
Monitoring
Querying spans and traces
Correlate with APM
Patterns
Agent Monitoring
MCP Clients
Prompt Tracking
Metrics
Automation Rules
Cost
Evaluations
Managed Evaluations
Custom LLM-as-a-Judge
External Evaluations
Annotation Queues
Compatibility
Export API
Developer Guide
Experiments
Setup and Usage
Datasets
Analyzing Results
Advanced Experiment Runs
Experiments API
Prompt Optimization
Playground
MCP Server
Data Security and RBAC
Terms and Concepts
Guides
GPU Monitoring
Setup
Summary Page
Fleet Page
Agent Console
Log Management
Observability Pipelines
Configuration
Explore Templates
Set Up Pipelines
Install the Worker
Secrets Management
Live Capture
Update Existing Pipelines
Export Pipeline
Access Control
Sources
Akamai DataStream
Amazon Data Firehose
Amazon S3
Azure Event Hubs
Cloudflare Logpush
Datadog Agent
Datadog Lambda Extension
Datadog Lambda Forwarder
Filebeat
Fluent
Google Pub/Sub
HTTP Client
HTTP Server
OpenTelemetry
Kafka
Logstash
MySQL
Okta
Socket
Splunk HEC
Splunk TCP
Sumo Logic Hosted Collector
Syslog
Processors
Add Environment Variables
Add hostname
Custom Processor
Deduplicate
Edit fields
Enrichment Table
Filter
Generate Metrics
Grok Parser
Parse JSON
Parse XML
Quota
Reduce
Remap to OCSF
Sample
Sensitive Data Scanner
Split Array
Tag Control
Throttle
Destinations
Amazon OpenSearch
Amazon S3
Amazon Security Lake
Azure Storage
CrowdStrike NG-SIEM
Datadog Archives
Datadog BYOC Logs
Datadog Logs
Datadog Metrics
Elasticsearch
Google Cloud Storage
Google Pub/Sub
Google SecOps
HTTP Client
Kafka
Microsoft Sentinel
New Relic
OpenSearch
SentinelOne
Socket
Splunk HEC
Sumo Logic Hosted Collector
Syslog
Packs
Akamai CDN
Amazon CloudFront
Amazon VPC Flow Logs
AWS Application Load Balancer Logs
AWS CloudTrail
AWS Elastic Load Balancer Logs
AWS Network Load Balancer Logs
Cisco ASA
Cloudflare
F5
Fastly
Fortinet Firewall
HAProxy Ingress
Istio Proxy
Juniper SRX Firewall Traffic Logs
Netskope
NGINX
Okta
Palo Alto Firewall
Windows XML
ZScaler ZIA DNS
Zscaler ZIA Firewall
Zscaler ZIA Tunnel
Zscaler ZIA Web Logs
Search Syntax
Scaling and Performance
Buffering and Backpressure
Scaling Best Practices
Monitoring and Troubleshooting
Worker CLI Commands
Monitoring Pipelines
Pipeline Usage Metrics
Troubleshooting
Guides and Resources
Upgrade Worker Guide
Log Management
Log Collection & Integrations
Browser
Android
iOS
Flutter
React Native
Roku
Kotlin Multiplatform
C#
Go
Java
Node.js
PHP
Python
Ruby
OpenTelemetry
Agent Integrations
Other Integrations
Log Configuration
Pipelines
Processors
Parsing
Pipeline Scanner
Attributes and Aliasing
Generate Metrics
Indexes
Flex Logs
Archives
Rehydrate from Archives
Archive Search
Forwarding
Log Optimizer
Log Explorer
Live Tail
Search Logs
Search Syntax
Advanced Search
Facets
Calculated Fields
Analytics
Patterns
Transactions
Visualize
Log Side Panel
Export
Watchdog Insights for Logs
Saved Views
Error Tracking
Error Tracking Explorer
Issue States
Track Browser and Mobile Errors
Track Backend Errors
Error Grouping
Manage Data Collection
Dynamic Sampling
Monitors
Identify Suspect Commits
Troubleshooting
Reports
Guides
Data Security
Troubleshooting
Live Tail
BYOC Logs
Introduction
Architecture
Network
Supported Features
Quickstart
Install
AWS EKS
Azure AKS
GCP GKE
Docker (Local)
Custom Kubernetes
Ingest
Datadog Agent
Observability Pipelines
REST API
Configure
Indexes
Ingress
Lambda Search Offloading
Operate
Sizing
Monitoring
Troubleshooting
Search Logs
Guides
Release Notes
Administration
Account Management
Switching Between Orgs
Organization Settings
User Management
Login Methods
Mobile and Third-Party Access
Custom Organization Landing Page
Service Accounts
IP Allowlist
Domain Allowlist
Cross-Organization Visibility
Access Control
Granular Access
Permissions
Data Access
SSO with SAML
Configuring SAML
Renewing SAML Certificates
User Group Mapping
Active Directory
Auth0
Entra ID
Google
LastPass
Okta
SafeNet
Troubleshooting
SCIM
Okta
Microsoft Entra ID
API and Application Keys
Personal Access Tokens
Teams
Team Management
Provision with GitHub
Governance Console
Controls
Multi-Factor Authentication
Audit Trail
Events
Forwarding
Guides
Safety Center
Plan & Usage
Bill Overview
Cost Details
Usage Details
Partner Experience
Billing
Pricing
Credit Card
Product Allotments
Usage Metrics
Usage Attribution
Custom Metrics
Containers
Log Management
APM
Serverless
Real User Monitoring
CI Visibility
Incident Response
AWS Integration
Azure Integration
Google Cloud Integration
OCI Integration
Alibaba Integration
vSphere Integration
Workflow Automation
Multi-org Accounts
Organization Groups
Guides
Cloud-based Authentication
Data Security
Agent
Cloud SIEM
Kubernetes
Log Management
Real User Monitoring
Synthetic Monitoring
Tracing
PCI Compliance
HIPAA Compliance
Data Retention Periods
Guides
Help
Widget Public URLs
Datadog Docs
Essentials
Getting Started
Agent
API
APM Tracing
Containers
Autodiscovery
Datadog Operator
Dashboards
Database Monitoring
Datadog
Datadog Site
DevSecOps
Incident Management
Integrations
AWS
Azure
Google Cloud
OCI
Terraform
Internal Developer Portal
Logs
Monitors
Notebooks
OpenTelemetry
Profiler
Search
Product-Specific Search
Session Replay
Security
App and API Protection
Cloud Security
Cloud SIEM
Code Security
Serverless for AWS Lambda
Software Delivery
CI Visibility
Feature Flags
Test Optimization
Test Impact Analysis
MCP Tools
Synthetic Monitoring and Testing
API Tests
Browser Tests
Mobile App Tests
Continuous Testing
Private Locations
Tags
Assigning Tags
Unified Service Tagging
Using Tags
Teams
Organization Topology
Workflow Automation
Learning Center
Support
Glossary
Standard Attributes
Guides
Agent
Architecture
IoT
Supported Platforms
AIX
Linux
Ansible
Chef
Heroku
MacOS
Puppet
SaltStack
SCCM
Windows
From Source
Log Collection
Log Agent tags
Advanced Configurations
Proxy
Transport
Multi-Line Detection
Configuration
Commands
Configuration Files
Log Files
Status Page
Network Traffic
Proxy Configuration
Squid proxy configuration
FIPS Compliance
Dual Shipping
Secrets Management
Fleet Automation
Remote Agent Management
Troubleshooting
Container Hostname Detection
Debug Mode
Agent Flare
Agent Check Status
NTP Issues
Permission Issues
Integrations Issues
Site Issues
Autodiscovery Issues
Windows Container Issues
Agent Runtime Configuration
High CPU or Memory Consumption
Guides
Data Security
Integrations
Guides
Client SDKs
Setup
Advanced Configuration
Data Collected
Integrated Libraries
Troubleshooting
Extend Datadog
Authorization
OAuth2 in Datadog
Authorization Endpoints
DogStatsD
Datagram Format
Unix Domain Socket
High Throughput Data
Data Aggregation
DogStatsD Mapper
Custom Checks
Writing a Custom Agent Check
Writing a Custom OpenMetrics Check
Integrations
Build an Integration with Datadog
Create an Agent-based Integration
Create an API-based Integration
Create a Log Pipeline
Integration Assets Reference
Build a Marketplace Offering
Create an Integration Dashboard
Create a Monitor Template
Create a Cloud SIEM Detection Rule
Install Agent Integration Developer Tool
Service Checks
Submission - Agent Check
Submission - DogStatsD
Submission - API
Community
Libraries
Guides
OpenTelemetry
Getting Started
Datadog Example Application
OpenTelemetry Demo Application
Feature Compatibility
Instrument Your Applications
Using OTel SDK
Using Datadog SDK
Configuration
APIs
Instrumentation Libraries
Send Data to Datadog
DDOT Collector (Recommended)
Install the DDOT Collector
Use Custom OTel Components
Migrate to the DDOT Collector
Other Setup Options
OpenTelemetry Collector
OTLP Ingest in the Agent
Direct OTLP Ingest
Semantic Mapping
Resource Attribute Mapping
Metrics Mapping
Infrastructure Host Mapping
Hostname Mapping
Service-entry Spans Mapping
Ingestion Sampling
Correlate Data
Logs and Traces
Metrics and Traces
RUM and Traces
DBM and Traces
Integrations
Apache Metrics
Apache Spark Metrics
Collector Health Metrics
Datadog Extension
Docker Metrics
HAProxy Metrics
Host Metrics
IIS Metrics
Kafka Metrics
Kubernetes Metrics
MySQL Metrics
PostgreSQL Metrics
NGINX Metrics
Podman Metrics
Runtime Metrics
SQL Server Metrics
Trace Metrics
Troubleshooting
Guides and Resources
Produce Delta Temporality Metrics
Visualize Histograms as Heatmaps
Instrument Unsupported Runtimes
Migration Guides
Migrate to OTel Collector v0.120.0+
Migrate to OTel Collector v0.95.0+
New Operation Name Mappings
Agent with DDOT Collector
Reference
Terms and Concepts
Trace Context Propagation
Trace IDs
OTLP Metric Types
Administrator's Guide
Getting Started
Plan
Build
Run
API
Partners
Datadog Mobile App
Enterprise Configuration
Datadog for Intune
Shortcut Configurations
Push Notifications
Widgets
Guides
DDSQL Reference
Data Directory
CoScreen
Troubleshooting
CoTerm
Install
Using CoTerm
Configuration Rules
Remote Configuration
Cloudcraft (Standalone)
Getting Started
Account Management
Components: Common
Components: Azure
Components: AWS
Advanced
FAQ
API
AWS Accounts
List AWS accounts
Add an AWS account
Delete an AWS account
Update an AWS account
Snapshot an AWS account
Get my AWS iam role parameters
Azure Accounts
List Azure accounts
Add an Azure account
Delete an Azure account
Update an Azure account
Snapshot an Azure account
Blueprints
List my blueprints
Create a blueprint
Delete a blueprint
Retrieve a blueprint
Update a blueprint
Export blueprint as image
Budgets
Export budget for a blueprint
Teams
List teams
Users
Get user profile
In The App
Dashboards
Configure
Dashboard List
Widgets
Configuration
Widget Types
Querying
Functions
Algorithms
Arithmetic
Count
Exclusion
Interpolation
Rank
Rate
Regression
Rollup
Smoothing
Timeshift
Beta
Graph Insights
Metric Correlations
Watchdog Explains
Template Variables
Overlays
Annotations
Guides
Sharing
Shared Dashboards
Secure Embedded Dashboards
Share Graphs
Scheduled Reports
Notebooks
Analysis Features
Getting Started
Guides
DDSQL Editor
Reference Tables
Sheets
Functions and Operators
Guides
Monitors and Alerting
Draft Monitors
Configure Monitors
Monitor Templates
Monitor Types
Notifications
Notification Rules
Variables
Downtimes
Examples
Manage Monitors
Search Monitors
Check Summary
Monitor Status
Status Graphs
Status Events
Monitor Settings
Monitor Quality
Guides
Service Level Objectives
Monitor-based SLOs
Metric-based SLOs
Time Slice SLOs
Error Budget Alerts
Burn Rate Alerts
Guides
Metrics
Custom Metrics
Metric Type Modifiers
Historical Metrics Ingestion
Submission - Agent Check
Submission - DogStatsD
Submission - Powershell
Submission - API
OpenTelemetry Metrics
OTLP Metric Types
Query OpenTelemetry Metrics
Metrics Types
Distributions
Overview
Explorer
Metrics Units
Summary
Volume
Advanced Filtering
Nested Queries
Reference Table Joins with Metrics
Derived Metrics
Metrics Without Limits™
Guides
Watchdog
Alerts
Impact Analysis
RCA
Insights
Faulty Deployment Detection
Faulty Cloud & SaaS API Detection
Bits AI
Bits AI SRE
Investigate Issues
Take Action
Bits AI SRE Integrations and Settings
Knowledge Sources
Chat with Bits AI SRE
Bits AI Dev Agent
Setup
Bits AI Security Analyst
Bits Assistant
MCP Server
Setup
MCP Tools
Agent Builder
Internal Developer Portal
Software Catalog
Set Up
Discover Entities
Create Entities
Import Entities
Define Ownership
Entity Model
Native Entities
Custom Entities
AI-generated Systems
Troubleshooting
Scorecards
Scorecard Configuration
Custom Rules
Using Scorecards
Self-Service Actions
Software Templates
Engineering Reports
Reliability Overview
Scorecards Performance
DORA Metrics
Custom Reports
Developer Homepage
Campaigns
External Provider Status
Plugins
Integrations
Use Cases
API Management
Cloud Cost Management
App and API Protection
Developer Onboarding
Dependency Management
Production Readiness
Incident Response
CI Pipeline Visibility
Onboarding Guide
Error Tracking
Explorer
Issue States
Regression Detection
Suspected Causes
Error Grouping
Bits AI Dev Agent
Monitors
Issue Correlation
Identify Suspect Commits
Auto Assign
Issue Team Ownership
Track Browser and Mobile Errors
Browser Error Tracking
Collecting Browser Errors
Mobile Crash Tracking
Replay Errors
Real User Monitoring
Logs
Track Backend Errors
Getting Started
Using Single Step Instrumentation
Using Datadog Tracing Libraries
Exception Replay
Capturing Handled Errors
APM
Logs
Manage Data Collection
Ticketing Systems
Jira
Case Management
Link Pull Requests
Troubleshooting
Guides
Change Tracking
Feature Flags
Event Management
Ingest Events
Pipelines and Processors
Aggregation Key Processor
Arithmetic Processor
Date Remapper
Category Processor
Grok Parser
Lookup Processor
Remapper
Service Remapper
Status Remapper
String Builder Processor
Explorer
Searching
Navigate the Explorer
Customization
Facets
Attributes
Notifications
Analytics
Saved Views
Triage Inbox
Correlation
Configuration
Triaging & Notifying
Analytics
Maintenance Windows
Guides
Incident Response
Incident Management
Incident Investigation
Declare an Incident
Describe an Incident
Response Team
Notification
Timeline
Incident AI
Setup and Configuration
Information
Property Fields
Responder Types
Automations
Notification Rules
Templates
Variables
Integrations
Post Incident
Follow-ups
Postmortems
Analytics and Reporting
Guides
On-Call
Onboard a Team
Pages
Live Call Routing
Cross-org Paging
Routing Rules
Escalation Policies
Schedules
Handover automation
Profile Settings
Guides
Status Pages
Case Management
Projects
Settings
Create a Case
Customization
View and Manage Cases
Notifications and Integrations
Case Automation Rules
MCP Server
Troubleshooting
Actions & Remediations
Agent Builder
Workflow Automation
Build Workflows
Access and Authentication
Trigger Workflows
Variables and parameters
Actions
Workflow Logic
Save and Reuse Actions
Test and Debug
Expressions
Track Workflows
Limits
Apps
App Builder
Build Apps
Access and Authentication
Queries
Variables
Events
Components
Custom Charts
React Renderer
Tables
Reusable Modules
JavaScript Expressions
Embedded Apps
Input Parameters
Save and Reuse Actions
Datastores
Create and Manage Datastores
Use Datastores with Apps and Workflows
Automation Rules
Access and Authentication
Forms
Action Catalog
Connections
HTTP Request
AWS Integration
Google Workspace
Private Actions
Use Private Actions
Run a Script
Update the Private Action Runner
Private Action Credentials
Infrastructure
Cloudcraft
Overlays
Infrastructure
Observability
Security
Cloud Cost Management
Monitors
APM
Resource Catalog
Cloud Resources Schema
Policies
Resource Changes
Universal Service Monitoring
Setup
Guides
End User Device Monitoring
Hosts
Host List
Containers
Container Monitoring
Containers Explorer
Container Images Explorer
Kubernetes Explorer
Configuration
Resource Utilization
Remediation
Amazon ECS Explorer
Autoscaling
Cluster
Docker-based
APM
Log collection
Tag extraction
Integrations
Prometheus
Data Collected
Kubernetes
Installation
Migrate to the Datadog Operator
Further Configuration
Distributions
APM
App and API Protection
Log collection
Tag extraction
Integrations
Prometheus & OpenMetrics
Control plane monitoring
Data collected
kubectl Plugin
Datadog CSI Driver
Data security
Cluster Agent
Setup
Commands & Options
Cluster Checks
Endpoint Checks
Admission Controller
Amazon ECS
APM
Log collection
Tag extraction
Data collected
Managed Instances
AWS Fargate with ECS
Datadog Operator
Migrate to the Datadog Operator
Advanced Install
Configuration
Custom Checks
Data Collected
Secret Management
DatadogDashboard CRD
DatadogMonitor CRD
DatadogSLO CRD
Troubleshooting
Duplicate hosts
Cluster Agent
Cluster Checks
HPA and Metrics Provider
Admission Controller
Log Collection
Guides
Processes
Increase Process Retention
Serverless
AWS Lambda
Instrumentation
Managed Instances
Lambda Metrics
Distributed Tracing
Log Collection
Remote Instrumentation
Advanced Configuration
Continuous Profiler
Securing Functions
Deployment Tracking
OpenTelemetry
Troubleshooting
Lambda Web Adapter
FIPS Compliance
AWS Step Functions
Installation
Merge Step Functions and Lambda Traces
Enhanced Metrics
Redrive Executions
Distributed Map States
Troubleshooting
AWS Fargate
Azure App Service
Linux - Code
Linux - Container
Windows - Code
Azure Container Apps
In-Container
Sidecar
Azure Functions
Azure Logic Apps
Google Cloud Run
Containers
Jobs (Preview)
Functions
Functions (1st generation)
Libraries & Integrations
Glossary
Guides
Network Monitoring
Cloud Network Monitoring
Setup
Network Health
Network Analytics
Tags Reference
Network Map
Guides
Supported Cloud Services
Terms and Concepts
DNS Monitoring
Network Device Monitoring
Setup
Supported Devices
SNMP Metrics
SNMP Traps
Ping
Syslog
VPN Monitoring
Integrations
Profiles
Getting Started
Advanced
Configuration Management
Maps
SNMP Metrics Reference
Troubleshooting
Guides
Terms and Concepts
NetFlow Monitoring
Monitors
Network Path
Setup
List View
Path View
Monitors
Guides
Terms and Concepts
Storage Management
Amazon S3
Google Cloud Storage
Azure Blob Storage
Cloud Cost
Cloud Cost
Datadog Costs
Setup
Permissions
AWS
Azure
Google Cloud
Oracle
SaaS Integrations
Snowflake
Databricks
OpenAI
Anthropic
GitHub
Confluent Cloud
MongoDB
Elastic Cloud
Fastly
Twilio
Custom
Tags
Tag Explorer
Multisource Querying
Allocation
Tag Pipelines
Container Cost Allocation
BigQuery Costs
Custom Allocation Rules
AI Costs
Reporting
Scheduled Reports
Explorer
Dashboard
Recommendations
Custom Recommendations
Planning
Budgets
Forecasting
Commitment Programs
Cost Changes
Monitors
Anomalies
Real-Time Costs
Application Performance
APM
APM Terms and Concepts
Application Instrumentation
Single Step Instrumentation
Linux
Docker
Kubernetes
Windows IIS
Manually managed SDKs
Java
Python
Ruby
Go
Node.js
PHP
C++
Rust
.NET Core
.NET Framework
Android
iOS
Code-based Custom Instrumentation
Server-Side Languages
Client-Side Languages
Dynamic Instrumentation
Enabling
Autocomplete and Search
Expression Language
Sensitive Data Scrubbing
Library Compatibility
Library Configuration
Configuration at Runtime
Trace Context Propagation
Serverless Application Tracing
Proxy Tracing
Apache HTTP Server
Envoy
Istio
Kong
NGINX
Amazon API Gateway
Azure API Management
Span Tag Semantics
Span Links
APM Metrics Collection
Trace Metrics
Runtime Metrics
Trace Pipeline Configuration
Ingestion Mechanisms
Ingestion Controls
Adaptive Sampling
Processing Pipelines
Generate Metrics
Trace Retention
Usage Metrics
Correlate Traces with Other Telemetry
Correlate DBM and Traces
Correlate Logs and Traces
Correlate RUM and Traces
Correlate Synthetics and Traces
Correlate Profiles and Traces
Trace Explorer
Search Spans
Query Syntax
Trace Queries
Span Tags and Attributes
Span Visualizations
Trace View
Tag Analysis
Recommendations
Code Origin for Spans
Service Observability
Software Catalog
Service Page
Resource Page
Deployment Tracking
Service Map
Inferred Services
Remapping Rules for Inferred Entities
Service Remapping Rules
Tag Enrichment
Integration Override Removal
APM Monitors
Endpoint Observability
Explore Endpoints
Monitor Endpoints
Live Debugger
Error Tracking
Issue States
Error Tracking Explorer
Error Grouping
Monitors
Identify Suspect Commits
Exception Replay
Troubleshooting
Data Security
Guides
Troubleshooting
Agent Rate Limits
Agent APM metrics
Agent Resource Usage
Correlated Logs
PHP 5 Deep Call Stacks
.NET diagnostic tool
APM Quantization
Go Compile-Time Instrumentation
Tracer Startup Logs
Tracer Debug Logs
Connection Errors
SDK Configurations
Continuous Profiler
Enabling the Profiler
Supported Language and SDK Versions
Profile Types
Profile Visualizations
Investigate Slow Traces or Endpoints
Compare Profiles
Automated Analysis
Profiler Troubleshooting
Java
Python
Go
Ruby
Node.js
.NET
PHP
C/C++/Rust
Guides
Database Monitoring
Agent Integration Overhead
Setup Architectures
Setting Up Postgres
Self-hosted
RDS
RDS Quick Install
Aurora
Google Cloud SQL
AlloyDB
Azure
Supabase
Supabase Cloud
Supabase Self-Hosted
Heroku
Advanced Configuration
Troubleshooting
Setting Up MySQL
Self-hosted
RDS
Aurora
Google Cloud SQL
Azure
Advanced Configuration
Troubleshooting
Setting Up SQL Server
Self-hosted
RDS
Azure
Google Cloud SQL
Troubleshooting
Setting Up Oracle
Self-hosted
RDS
RAC
Exadata
Autonomous Database
Troubleshooting
Setting Up Amazon DocumentDB
Amazon DocumentDB
Troubleshooting
Setting Up MongoDB
Self-hosted
MongoDB Atlas
Troubleshooting
Setting Up ClickHouse
Self-hosted
ClickHouse Cloud
Connecting DBM and Traces
Data Collected
Collecting Custom Metrics
Exploring Custom Metrics
Exploring Database Hosts
Exploring Query Metrics
Exploring Query Samples
Exploring Database Schemas
Exploring Recommendations
Database Investigator
Troubleshooting
Guides
Data Streams Monitoring
Setup
Kafka
Setup
Schema Tracking
Dead Letter Queues
Metrics and Tags
Business Transaction Tracking
Data Observability
Data Observability Overview
Data Catalog
Quality Monitoring
Data Warehouses
Snowflake
Databricks
BigQuery
Redshift
Data Lakes
Iceberg Tables (AWS Glue)
ELT Integrations
Fivetran
Business Intelligence Integrations
Looker
Tableau
Sigma
Metabase
Power BI
Jobs Monitoring
Databricks
Airflow
Troubleshooting DAG
dbt
Spark on Kubernetes
Spark on Amazon EMR
Spark on Google Dataproc
AWS Glue
Custom Jobs (OpenLineage)
Datadog Agent for OpenLineage Proxy
Digital Experience
Real User Monitoring
Application Monitoring
Browser
Setup
Advanced Configuration
Build Plugins
Data Collected
Monitoring Page Performance
Optimizing Performance
Monitoring Resource Performance
Collecting Browser Errors
Tracking User Actions
Frustration Signals
Error Tracking
Troubleshooting
Android and Android TV
Setup
Crash Reporting
Monitoring App Launch
Monitoring App Performance
Advanced Configuration
Data Collected
Mobile Vitals
Frustration Signals
Web View Tracking
Integrated Libraries
Jetpack Compose Instrumentation
Troubleshooting
SDK Performance Impact
iOS and tvOS
Setup
Crash Reporting
Monitoring App Launch
Mobile App Performance
Advanced Configuration
Data Collected
Mobile Vitals
Frustration Signals
Web View Tracking
Integrated Libraries
Troubleshooting
Supported Versions
SDK Performance Impact
Flutter
Setup
Crash Reporting
Advanced Configuration
Data Collected
Mobile Vitals
Frustration Signals
Web View Tracking
Integrated Libraries
Troubleshooting
Kotlin Multiplatform
Setup
Crash Reporting
Advanced Configuration
Data Collected
Mobile Vitals
Frustration Signals
Web View Tracking
Integrated Libraries
Troubleshooting
React Native
Setup
Crash Reporting
Advanced Configuration
Data Collected
Mobile Vitals
Frustration Signals
Web View Tracking
Integrated Libraries
Troubleshooting
Roku
Setup
Crash Reporting
Advanced Configuration
Data Collected
Web View Tracking
Unity
Setup
Crash Reporting
Advanced Configuration
Data Collected
Mobile Vitals
Troubleshooting
Platform
Dashboards
Performance
Testing and Deployment
Usage
Errors
Monitors
Generate Custom Metrics
Exploring RUM Data
Search RUM Events
Search Syntax
Group
Visualize
Events
Export
Saved Views
Watchdog Insights for RUM
Correlate RUM with Other Telemetry
Correlate LLM with RUM
Correlate Logs with RUM
Correlate Profiling with RUM
Correlate Synthetics with RUM
Correlate Traces with RUM
Feature Flag Tracking
Setup
Using Feature Flags
Error Tracking
Explorer
Issue States
Track Browser Errors
Track Mobile Errors
Error Grouping
Monitors
Identify Suspect Commits
Troubleshooting
AI Investigations
Single-View AI Investigation
RUM Without Limits
Metrics
Retention Filters
Retention Quotas
Operations Monitoring
Managed Archive
Ownership of Views
Guides
Data Security
Synthetic Testing and Monitoring
API Testing
HTTP
SSL
DNS
WebSocket
TCP
UDP
ICMP
GRPC
Error codes
Multistep API Testing
Browser Testing
Recording Steps
Browser Testing Results
Advanced Options for Steps
Authentication in Browser Testing
Network Path Testing
Terms and Concepts
Mobile Application Testing
Testing Steps
Testing Results
Advanced Options for Steps
Supported Devices
Restricted Networks
Settings
Test Suites
Platform
Dashboards
Test Summary
API Testing
Browser Testing
Metrics
Test Coverage
Private Locations
Configuration
Dimensioning
Monitoring
Connect APM
Settings
Scheduled Downtime
Exploring Synthetics Data
Saved Views
Results Explorer
Search Test Batches
Search Test Runs
Search Syntax
Export Test Runs
Saved Views
Guides
Notifications
Template Variables
Browser
Mobile
Multistep API
API
Conditional Alerting
Advanced Notifications
Integrate with Statuspage
Troubleshooting
Data Security
Continuous Testing
Local and Staging Environments
Testing Multiple Environments
Testing With Proxy, Firewall, or VPN
CI/CD Integrations
Configuration
Azure DevOps Extension
CircleCI Orb
GitHub Actions
GitLab
Jenkins
Bitrise (Upload Application)
Bitrise (Run Tests)
Settings
Results Explorer
Metrics
Guides
Troubleshooting
Experiments
Create Experiment Metrics
Plan and Launch Experiments
Read Experiment Results
Minimum Detectable Effects
Guides
Troubleshooting
Product Analytics
Charts
Chart Basics
Pathways Diagram
Funnel Analysis
Retention Analysis
Analytics Explorer
Dashboards
Segments
Managing Profiles
Data Collected
Guides
Troubleshooting
Session Replay
Browser
Setup
Privacy Options
Developer Tools
Troubleshooting
Mobile
Setup and Configuration
Privacy Options
Developer Tools
Impact on App Performance
Troubleshooting
Playlists
Heatmaps
Guides
Software Delivery
CI Visibility
Pipeline Visibility
AWS CodePipeline
Azure Pipelines
Buildkite
CircleCI
Codefresh
GitHub Actions
GitLab
Jenkins
TeamCity
Other CI Providers
Automatic Job Retries
Custom Commands
Custom Tags and Measures
Search and Manage
Explorer
Search Syntax
Search Pipeline Executions
Export
Saved Views
Monitors
Guides
Troubleshooting
CD Visibility
Deployment Visibility
Argo CD
CI Providers
Explore Deployments
Search Syntax
Facets
Saved Views
Features
Code Changes Detection
Rollback Detection
Monitors
Deployment Gates
Setup
Explore
Test Optimization
Setup
.NET
Java and JVM Languages
JavaScript and TypeScript
Python
Ruby
Swift
Go
JUnit Report Uploads
Network Settings
Tests in Containers
Explorer
Search Syntax
Search Test Runs
Export
Saved Views
Monitors
Test Health
Flaky Test Management
Working with Flaky Tests
Early Flake Detection
Auto Test Retries
Test Impact Analysis
How It Works
Troubleshooting
Setup
.NET
JavaScript and TypeScript
Python
Swift
Java
Ruby
Go
Developer Workflows
Code Coverage
Instrument Browser Tests with RUM
Instrument Swift Tests with RUM
Correlate Logs and Tests
Guides
Troubleshooting
Code Coverage
Setup
Configuration
Monorepo Support
Flags
Data Collected
PR Gates
Setup
DORA Metrics
Setup
Change Failure Detection
DORA Metrics Calculation
Data Collected
Feature Flags
Client SDKs
Android and Android TV
Angular
iOS and tvOS
JavaScript
React
React Native
Unity
Server SDKs
.NET
Go
Java
Node.js
Python
Ruby
Flag History
MCP Server
Guides
Developer Integrations
Source Code Integration
Source Code Management Providers
Service Mapping
Resource Mapping
Features
IDE Plugins
JetBrains IDEs
Error Tracking
Logs
Live Debugger
Code Security
VS Code & Cursor
Logs
Code Insights
Code Security
Exception Replay
Live Debugger
Security
Security Overview
Detection Rules
OOTB Rules
Notifications
Rules
Variables
Suppressions
Automation Pipelines
Mute
Add to Security Inbox
Set Due Date Rules
Security Inbox
Threat Intelligence
Events Forwarding
Audit Trail
Access Control
Account Takeover Protection
Ticketing Integrations
Research Feed
Security MCP Tools
Guides
Cloud SIEM
Ingest and Enrich
Content Packs
Bring Your Own Threat Intelligence
Open Cybersecurity Schema Framework
OCSF Processor
Detect and Monitor
OOTB Rules
Custom Detection Rules
Create Rule
Anomaly
Content Anomaly
Impossible Travel
New Value
Sequence
Version History
Suppressions
Critical Assets
Historical Jobs
MITRE ATT&CK Map
Triage and Investigate
Investigate Security Signals
Risk Insights
IOC Explorer
Investigator
Respond and Report
Security Operational Metrics
Guides
Data Security
Code Security
Static Code Analysis (SAST)
Setup
Configuration
GitHub Actions
Generic CI Providers
AI-Enhanced Static Code Analysis
SAST Custom Rule Creation Tutorial
SAST Custom Rules
SAST Custom Rules Guide
Static Code Analysis (SAST) rules
Software Composition Analysis (SCA)
Static Setup
Runtime Setup
Library Compatibility
Configuration
Library Inventory
CVE Explorer
Secret Scanning
GitHub Actions
Generic CI Providers
Secret Validation
Runtime Code Analysis (IAST)
Setup
Security Controls
Infrastructure as Code (IaC) Security
Setup
GitHub Actions
Exclusions
Rules
Developer Tool Integrations
Pull Request Comments
PR Gates
IDE Plugins
Git Hooks
MCP Server
Tools Reference
Troubleshooting
Troubleshooting
Guides
Cloud Security
Setup
Supported Deployment Types
Agentless Scanning
Compatibility
Deployment Methods
Enable Agentless Scanning
Update Agentless Scanning
Deploy the Agent
Container Image Scanning in CI/CD
Set Up CloudTrail Logs
Set Up without Infrastructure Monitoring
Deploy using Cloud Integrations
Security Graph
Misconfigurations
Manage Compliance Rules
Create Custom Rules
Manage Compliance Posture
Create Custom Frameworks
Supported Frameworks
Explore Misconfigurations
Export Misconfigurations
Kubernetes Security Posture Management
Identity Risks
Vulnerabilities
Hosts and Containers Compatibility
OOTB Rules
Review and Remediate
Mute Issues
Automate Security Workflows
Severity Scoring
Guides
Troubleshooting
Vulnerabilities
Agentless Scanning
App and API Protection
Terms and Concepts
How It Works
Threat Intelligence
Trace Qualification
User Monitoring and Protection
Setup
Overview
Security Signals
Attackers Explorer
Attacker Fingerprint
Attacker Clustering
Users Explorer
Policies
Custom Rules
OOTB Rules
In-App WAF Rules
Tracing Library Configuration
Exploit Prevention
WAF Integrations
API Security Inventory
Guides
Troubleshooting
AI Guard
Get Started with AI Guard
Set Up AI Guard
Automatic Integrations
Manual Integrations
SDK
HTTP API
Security Signals
Workload Protection
Setup
Deploy the Agent
Workload Protection Agent Variables
Detection Rules
OOTB Rules
Custom Rules
Investigate Security Signals
Investigate Agent Events
Creating Agent Rule Expressions
Writing Custom Rule Expressions
Linux Syntax
Windows Syntax
Coverage and Posture Management
Hosts and Containers
Serverless
Coverage
Guides
Troubleshooting
Sensitive Data Scanner
Setup
Telemetry Data
Cloud Storage
Scanning Rules
Library Rules
Custom Rules
Guides
AI Observability
LLM Observability
Quickstart
Instrumentation
Automatic
SDK Reference
HTTP API
OpenTelemetry
Tracing Proxy Services
Monitoring
Querying spans and traces
Correlate with APM
Patterns
Agent Monitoring
MCP Clients
Prompt Tracking
Metrics
Automation Rules
Cost
Evaluations
Managed Evaluations
Quality Evaluations
Security and Safety Evaluations
Custom LLM-as-a-Judge
Connect Your LLM Provider
Template Evaluations
Trace-Level Evaluations
Prompt Templating
External Evaluations
NeMo
DeepEval Evaluations
Pydantic Evaluations
Annotation Queues
Compatibility
Export API
Developer Guide
Experiments
Setup and Usage
Datasets
Analyzing Results
Advanced Experiment Runs
Experiments API
Prompt Optimization
Playground
MCP Server
Data Security and RBAC
Terms and Concepts
Guides
GPU Monitoring
Setup
Summary Page
Fleet Page
Agent Console
Log Management
Observability Pipelines
Configuration
Explore Templates
Set Up Pipelines
Install the Worker
Advanced Worker Configuration
Run Multiple Pipelines on a Host
Secrets Management
Live Capture
Update Existing Pipelines
Export Pipeline
Access Control
Sources
Akamai DataStream
Amazon Data Firehose
Amazon S3
Azure Event Hubs
Cloudflare Logpush
Datadog Agent
Datadog Lambda Extension
Datadog Lambda Forwarder
Filebeat
Fluent
Google Pub/Sub
HTTP Client
HTTP Server
OpenTelemetry
Kafka
Logstash
MySQL
Okta
Socket
Splunk HEC
Splunk TCP
Sumo Logic Hosted Collector
Syslog
Processors
Add Environment Variables
Add hostname
Custom Processor
Deduplicate
Edit fields
Enrichment Table
Filter
Generate Metrics
Grok Parser
Parse JSON
Parse XML
Quota
Reduce
Remap to OCSF
Sample
Sensitive Data Scanner
Split Array
Tag Control
Throttle
Destinations
Amazon OpenSearch
Amazon S3
Amazon Security Lake
Azure Storage
CrowdStrike NG-SIEM
Datadog Archives
Datadog BYOC Logs
Datadog Logs
Datadog Metrics
Elasticsearch
Google Cloud Storage
Google Pub/Sub
Google SecOps
HTTP Client
Kafka
Microsoft Sentinel
New Relic
OpenSearch
SentinelOne
Socket
Splunk HEC
Sumo Logic Hosted Collector
Syslog
Packs
Akamai CDN
Amazon CloudFront
Amazon VPC Flow Logs
AWS Application Load Balancer Logs
AWS CloudTrail
AWS Elastic Load Balancer Logs
AWS Network Load Balancer Logs
Cisco ASA
Cloudflare
F5
Fastly
Fortinet Firewall
HAProxy Ingress
Istio Proxy
Juniper SRX Firewall Traffic Logs
Netskope
NGINX
Okta
Palo Alto Firewall
Windows XML
ZScaler ZIA DNS
Zscaler ZIA Firewall
Zscaler ZIA Tunnel
Zscaler ZIA Web Logs
Search Syntax
Scaling and Performance
Buffering and Backpressure
Scaling Best Practices
Monitoring and Troubleshooting
Worker CLI Commands
Monitoring Pipelines
Pipeline Usage Metrics
Troubleshooting
Guides and Resources
Upgrade Worker Guide
Log Management
Log Collection & Integrations
Browser
Android
iOS
Flutter
React Native
Roku
Kotlin Multiplatform
C#
Go
Java
Node.js
PHP
Python
Ruby
OpenTelemetry
Agent Integrations
Other Integrations
Log Configuration
Pipelines
Processors
Parsing
Pipeline Scanner
Attributes and Aliasing
Generate Metrics
Indexes
Flex Logs
Archives
Rehydrate from Archives
Archive Search
Forwarding
Log Optimizer
Log Explorer
Live Tail
Search Logs
Search Syntax
Advanced Search
Facets
Calculated Fields
Formulas
Extractions
Analytics
Patterns
Transactions
Visualize
Log Side Panel
Export
Watchdog Insights for Logs
Saved Views
Error Tracking
Error Tracking Explorer
Issue States
Track Browser and Mobile Errors
Track Backend Errors
Error Grouping
Manage Data Collection
Dynamic Sampling
Monitors
Identify Suspect Commits
Troubleshooting
Reports
Guides
Data Security
Troubleshooting
Live Tail
BYOC Logs
Introduction
Architecture
Network
Supported Features
Quickstart
Install
AWS EKS
Azure AKS
GCP GKE
Docker (Local)
Custom Kubernetes
Ingest
Datadog Agent
Observability Pipelines
REST API
Configure
Indexes
Ingress
Lambda Search Offloading
Operate
Sizing
Monitoring
Troubleshooting
Search Logs
Guides
Release Notes
Administration
Account Management
Switching Between Orgs
Organization Settings
User Management
Login Methods
Mobile and Third-Party Access
Custom Organization Landing Page
Service Accounts
IP Allowlist
Domain Allowlist
Cross-Organization Visibility
Access Control
Granular Access
Permissions
Data Access
SSO with SAML
Configuring SAML
Renewing SAML Certificates
User Group Mapping
Active Directory
Auth0
Entra ID
Google
LastPass
Okta
SafeNet
Troubleshooting
SCIM
Okta
Microsoft Entra ID
API and Application Keys
Personal Access Tokens
Teams
Team Management
Provision with GitHub
Governance Console
Controls
Multi-Factor Authentication
Audit Trail
Events
Forwarding
Guides
Safety Center
Plan & Usage
Bill Overview
Cost Details
Usage Details
Partner Experience
Billing
Pricing
Credit Card
Product Allotments
Usage Metrics
Usage Attribution
Custom Metrics
Containers
Log Management
APM
Serverless
Real User Monitoring
CI Visibility
Incident Response
AWS Integration
Azure Integration
Google Cloud Integration
OCI Integration
Alibaba Integration
vSphere Integration
Workflow Automation
Multi-org Accounts
Organization Groups
Guides
Cloud-based Authentication
Data Security
Agent
Cloud SIEM
Kubernetes
Log Management
Real User Monitoring
Synthetic Monitoring
Tracing
PCI Compliance
HIPAA Compliance
Data Retention Periods
Guides
Help
Software Composition Analysis
Docs > Datadog Security > Code Security > Software Composition Analysis
This product is not supported for your selected Datadog site. ( US1).
Overview
Software Composition Analysis (SCA) detects open source libraries in both your repositories and running services, providing end-to-end visibility of library vulnerabilities and license management from development to production.
Using Software Composition Analysis provides organizations with the following benefits:
Identification of emerging and known vulnerabilities affecting open source libraries
Risk-based prioritization and remediation based on runtime detection of vulnerabilities
Identification of malicious packages, end-of-life libraries, and library riskiness based on OpenSSF standards
Export a Software Bill of Materials (SBOM) of detected libraries in CycloneDX 1.6 or SPDX 2.3 format
How it works
SCA supports two complementary detection modes:
Static detection scans repositories by analyzing dependency files (lockfiles and manifests). By default, scans run when a commit updates a supported dependency manifest or lockfile in an enabled repository. You can also run SCA in your CI/CD pipeline (CI jobs are supported for push events). See Set up Static SCA to get started.
Runtime detection identifies libraries that are loaded and used by your services at runtime using instrumentation from Datadog APM. See Set up Runtime SCA to get started.
When Datadog ingests a new advisory, it is matched against your last known library inventory and appears in the Vulnerabilities Explorer even if you have not rescanned the repository. The Repositories Explorer is commit-scoped and reflects what was known at the time the scan ran—so a scan that executed before Datadog ingested the advisory will not show that newly published advisory in the Repositories Explorer for that commit. See Understanding SCA views for more details.
Vulnerability database
Datadog SCA draws from multiple public and private sources to build a curated proprietary database. These sources include the National Vulnerability Database (NVD), the GitHub Advisory Database, osv.dev, ecosystem-specific advisories such as PyPA's Advisory Database and the Global Security Database, Datadog GuardDog, and Datadog Security Research.
Datadog uses these sources to identify known vulnerabilities, malicious packages, and emerging supply chain threats across supported ecosystems. There is a maximum of 1 hour between when a new vulnerability is published and when it appears in Datadog, with emerging vulnerabilities typically appearing in Datadog within minutes. Malicious packages are reported in Datadog within 6 hours.
Public exploit sources
Datadog identifies whether a vulnerability has a known public exploit by aggregating data from multiple public sources, including CISA (Known Exploited Vulnerabilities Catalog), Exploit-DB, NIST (National Vulnerability Database), and GitHub (public exploit references).
When Datadog identifies a public exploit for a vulnerability from any of these sources, it flags the finding to help you prioritize remediation.
Key capabilities
Review and prioritize vulnerabilities
The Vulnerabilities Explorer provides a vulnerability-centric view of library vulnerabilities detected by SCA, alongside vulnerabilities detected by other Code Security capabilities (SAST, IAST, Secrets Scanning, and IaC). All vulnerabilities in the explorer are either detected on the default branch at the last commit of a scanned repository, or are affecting a running service.
Datadog severity score
To assist in prioritizing remediation, Datadog modifies the base CVSS score into the Datadog Severity Score by incorporating runtime context and exploitability signals. These factors help distinguish theoretical risk from vulnerabilities that are more likely to be exploited in real-world environments. The table below describes how each factor influences the final score.
View findings by repository
The Repositories Explorer provides a repository-centric view of all scan results across Static Code Analysis (SAST), Software Composition Analysis (SCA), Secrets Scanning, and Infrastructure as Code (IaC). Click on a repository to analyze Library Vulnerabilities and Library Catalog results from SCA scoped to your chosen branch and commit.
The Library Vulnerabilities tab contains the vulnerable library versions found by Datadog SCA
The Library Catalog tab contains all of the libraries (vulnerable or not) found by Datadog SCA.
Recommended steps for remediating detected vulnerabilities can be found in the side panel for each vulnerability in SCA. Steps are provided for upgrading the library to the safest (non-vulnerable) version, as well as the closest version.
To filter your results, use the facets to the left of the list or the search bar at the top. Results can be filtered by service or team facets. For more information about how results are linked to Datadog services and teams, see Link findings to Datadog services and teams.
Every row represents a unique library and version combination. Each combination is associated with the specific commit and branch that is selected in the filters at the top of the page (by default, the latest commit on the default branch of the repository you selected).
Click on a library with a vulnerability to open a side panel that contains information about remediation steps.
Automatically block risky changes with PR Gates
Use PR Gates to enforce security standards for open source libraries before changes are merged. Datadog scans the dependencies introduced in each pull request, identifies vulnerabilities or license violations that exceed your configured severity threshold, and reports a pass or fail status to GitHub or Azure DevOps.
You can configure PR Gates to block on:
Security vulnerabilities: libraries with known CVEs above a configured severity threshold.
License violations: libraries using licenses that do not comply with your organization's policy.
PR Gates marks a PR check as failed only if the developer introduces a new violation in that PR. Violations that already existed in the codebase before the PR branch was created do not cause the check to fail. By default, failed checks are informational and do not block merging, but you can configure them as blocking in GitHub or Azure DevOps to prevent merges when critical issues are detected. For setup instructions, see Set up PR Gate Rules.
Manage your library inventory
The Library Inventory provides visibility into the third-party libraries detected across your codebase. Datadog collects this information from:
Static SCA, which identifies all libraries referenced in your repositories, and
Runtime SCA, which detects libraries that are actually loaded and used by your services at runtime.
Use the Library Inventory to understand which dependencies you rely on, where they are used, and whether they contain known vulnerabilities or license risks.
To learn more about how the inventory is generated, how Static and Runtime data differ, and how to interpret the library details (usage, vulnerabilities, licenses, versions, and OpenSSF score), see Library Inventory.
Export a Software Bill of Materials
Export a SBOM of your third-party libraries directly from the Library Inventory. The exported SBOM includes libraries detected both statically (with Static SCA) and at runtime (with Runtime SCA), giving you a single, comprehensive view of your software supply chain.
Datadog supports the following SBOM formats:
CycloneDX 1.6
SPDX 2.3
Use the exported SBOM to share dependency data with downstream consumers, satisfy compliance and regulatory requirements, or feed into other supply chain tooling.
For details on how to generate and download an SBOM, see Library Inventory.
Explore the full CVE catalog
Use the CVE Explorer to search every CVE and security advisory tracked by Datadog, including those that do not affect your environment. This helps you assess exposure to newly published vulnerabilities before they appear in your findings.
For CVEs that affect packages detected in your scanned repositories and services, Datadog automatically marks them as impacted. Assets that have not been scanned do not show an impacted status.
For each CVE, you can view the severity score, exploit availability, EPSS score, CISA KEV status, impacted packages, and fix versions. See CVE Explorer for more details.
Create tickets from findings
You can create a bidirectional ticket in Jira or ServiceNow directly from any finding to track and remediate issues in your existing workflows. Ticket status remains synced between Datadog and your ticketing tool. For more information, see Ticketing integrations.
Ticket creation is only available for library vulnerability findings detected in repositories (Static SCA). Findings detected exclusively in running services do not support ticket creation.
Mute findings
To suppress a finding, click Mute in the finding details panel. This opens a workflow where you can create an Automation Rule for context-aware filtering by tag values (for example, by repository ). Muting a finding hides it and excludes it from reports.
Muting is only available for library vulnerability findings detected in repositories (Static SCA). Findings detected exclusively in running services cannot be muted.
To restore a muted finding, click Unmute in the details panel. You can also use the Status filter on the Vulnerabilities Explorer to review muted findings.
Library vulnerability context in APM
SCA enriches the information that Application Performance Monitoring (APM) already collects by flagging libraries that match current vulnerability advisories. Potentially vulnerable services are highlighted directly in the Security view in the APM Software Catalog.
Understanding SCA views
The Repositories Explorer and Vulnerabilities Explorer serve complementary but distinct purposes.
Repositories Explorer reflects a point-in-time snapshot of the libraries and vulnerabilities detected at the time of the scan. It shows which libraries were present in a given repository at a specific commit, along with any vulnerabilities that were known at scan time. This view does not update retroactively if new advisories are published after the scan runs.
Vulnerabilities Explorer provides a live view that is continuously matched against the latest advisory database. If a new vulnerability advisory is published after a repository scan, it automatically appears in the Vulnerabilities Explorer, even if the repository has not been rescanned or if your last scan was on an older commit. This ensures your vulnerability exposure is always up to date.
Example: If a scan runs at 10:00 AM and a CVE advisory for a library in your repository is published at 4:00 PM, the Repositories Explorer for that commit will not show the CVE, but the Vulnerabilities Explorer will reflect it as soon as the advisory is available in Datadog's database.
Retroactive advisory matching
Datadog continuously matches newly published advisories against the stored library inventory from past scans. This updates vulnerability records in the Vulnerabilities Explorer without altering the original Repositories Explorer snapshots. This means:
You do not need to trigger a new scan for a newly published CVE to appear in the Vulnerabilities Explorer.
The Vulnerabilities Explorer reflects the most current risk based on your last known library inventory, even for older commits.
The Repositories Explorer remains a fixed, point-in-time record of what was known at scan time and does not update when new advisories are published.
Vulnerability lifecycle
Datadog tracks SCA vulnerabilities differently depending on where they are detected. Static SCA findings are scoped to a repository and are based on repository scans. Runtime SCA findings are scoped to a service and are based on libraries that are loaded and used by running services.
A vulnerability is opened when Datadog detects a vulnerable library in the relevant scope. A vulnerability is closed when Datadog no longer detects it according to the life cycle rules for that product.
SCA language support
Software Composition Analysis (SCA) supports the following languages:
Customize your configuration
You can exclude paths from Static SCA analysis by configuring ignore-paths in Datadog or in a code-security.datadog.yaml file. For the full SCA configuration reference, see Software Composition Analysis (SCA) Configuration. For information on configuration locations, precedence, and merging, see Code Security Configuration Reference.
Next steps
Set up Static SCA to scan your repositories.
Set up Runtime SCA to detect libraries loaded by your running services.
Review and triage findings in the Vulnerabilities Explorer.
Configure PR Gates to block risky changes before they are merged.
Use the CVE Explorer to proactively assess exposure to newly published vulnerabilities.
Further Reading
Additional helpful documentation, links, and articles:
Detect and block exposed credentials with Datadog Secret Scanning BLOG
Set up Static SCA DOCUMENTATION
Set up Runtime SCA DOCUMENTATION
Library Inventory DOCUMENTATION
CVE Explorer DOCUMENTATION
PR Gates DOCUMENTATION
Remediate transitive vulnerabilities faster with Datadog Software Composition Analysis BLOG
Key learnings from the 2026 State of DevSecOps study BLOG
Language
English
English Français 日本語 한국어 Español
Datadog Site
US1
US1 US3 US5 EU AP1 AP2 US1-FED US2-FED
 Edit
 Copy Copied
On this Page
Overview
How it works
Vulnerability database
Public exploit sources
Key capabilities
Review and prioritize vulnerabilities
View findings by repository
Automatically block risky changes with PR Gates
Manage your library inventory
Export a Software Bill of Materials
Explore the full CVE catalog
Create tickets from findings
Mute findings
Library vulnerability context in APM
Understanding SCA views
Retroactive advisory matching
Vulnerability lifecycle
SCA language support
Customize your configuration
Next steps
Further Reading 
Copy
Can't find something?
Our friendly, knowledgeable solutions engineers are here to help!
Contact Us
Free Trial
Download mobile app  
Product
Infrastructure Monitoring Network Monitoring Container Monitoring Serverless Cloud Cost Management Cloudcraft Kubernetes Autoscaling Application Performance Monitoring Software Catalog Universal Service Monitoring Data Streams Monitoring Jobs Monitoring Quality Monitoring Database Monitoring Continuous Profiler Dynamic Instrumentation Log Management Sensitive Data Scanner Audit Trail Observability Pipelines Cloud Security Cloud Security Posture Management Workload Protection Cloud Infrastructure Entitlement Management Vulnerability Management Compliance App and API Protection Software Composition Analysis Code Security Static Code Analysis (SAST) Runtime Code Analysis (IAST) IaC Security Cloud SIEM Browser Real User Monitoring Mobile Real User Monitoring Product Analytics Experiments Session Replay Synthetic Monitoring Mobile App Testing Continuous Testing Error Tracking
BYOC Log Management Internal Developer Portal CI Visibility Test Optimization Feature Flags Code Coverage Service Level Objectives Incident Response Event Management Case Management Bits AI Agents Bits AI SRE Bits AI Security Analyst MCP Server Agent Directory Metrics Watchdog LLM Observability AI Integrations Workflow Automation App Builder CoScreen Teams Dashboards Notebooks Mobile App Fleet Automation Governance Console Access Control OpenTelemetry Alerts integrations IDE Plugins API Marketplace Security Labs Research Open Source Projects Storage Management GPU Monitoring DORA Metrics Secret Scanning
resources
Pricing Documentation Support Services & Enablement Product Preview Program Certification
Open Source Events and Webinars Security Privacy Center Knowledge Center Learning Resources
About
Contact Us Partners Press Leadership Careers Legal
Investor Relations Analyst Reports ESG Report Vendor Help Trust Hub
Blog
The Monitor Engineering
AI Security Labs
Created with Sketch. English
English English
Français French
日本語 Japanese
한국어 Korean
Español Spanish    
© Datadog 2026 Terms | Privacy | Your Privacy Choices
Request a personalized demo
×
First Name*
Last Name*
Business Email*
Company*
Job Title*
Phone Number
How are you currently monitoring your infrastructure and applications?
By submitting this form, you agree to the Privacy Policy and Cookie Policy.
Request a Demo
Get Started with Datadog
Ask AI 
Ask AI 
AI-generated responses may be inaccurate. Verify important info. 
New Question
How can I help you today?
Ask me anything about Datadog documentation
How do I enable Continuous Profiler for a Java service? Which OpenTelemetry semantic conventions should I use for LLM traces in Datadog? How do I send OpenTelemetry traces to Datadog?
Your use of this AI-powered assistant is subject to our Privacy Policy. Please do not submit sensitive or personal information.   
