---
name: CloudFront flat-rate pricing plans - AWS Documentation - Amazon.com
keywords: (placeholder)
metadata:
  url: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.html
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
CloudFront flat-rate pricing plans - Amazon CloudFront
Select your cookie preferences
We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.
If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”
Accept Decline Customize
Customize cookie preferences
We use cookies and similar tools (collectively, "cookies") for the following purposes.
Essential
Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.
Performance
Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes. [x]
Allowed
Functional
Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly. [x]
Allowed
Advertising
Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising. [x]
Allowed
Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the AWS Cookie Notice .
Cancel Save preferences
Unable to save cookie preferences
We will only store essential cookies at this time, because we were unable to save your cookie preferences.
If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.
Dismiss
Skip to main content
English
Preferences
Contact Us
Feedback
Get started
Service guides
Developer tools
AI resources
Create an AWS Account
Amazon CloudFront
Developer Guide
What is Amazon CloudFront?
Ways to use CloudFront
How CloudFront delivers content
CloudFront edge servers
Working with AWS SDKs
Get started
Set up your AWS account
Get started with a standard distribution
Get started (AWS CLI)
Get started with a secure static website
CloudFront flat-rate pricing plans
Configure distributions
Understand how multi-tenant distributions work
Distribution tenant customizations
Request certificates (distribution tenant)
Create custom connection group (optional)
Migrate to a multi-tenant distribution
Create a distribution
Add a domain to your CloudFront standard distribution
Preconfigured distribution settings
All distribution settings
Origin settings
Cache behavior settings
Distribution settings
Custom error pages and error caching
Geographic restrictions
Test a distribution
Update a distribution
Tag a CloudFront resource
Delete a distribution
Use various origins
Enable IPv6
Use continuous deployment to safely test changes
CloudFront continuous deployment workflow
Work with a staging distribution and continuous deployment policy
Monitor a staging distribution
Learn how continuous deployment works
Quotas and other considerations for continuous deployment
Use custom URLs
Add an alternate domain name
Move an alternate domain name
Set up the target standard distribution or distribution tenant
Find the source standard distribution or distribution tenant
Move the alternate domain name
Remove an alternate domain name
Use wildcards in alternate domain names
Use WebSockets
Request Anycast static IPs to use for allowlisting
Bring your own IP to CloudFront using IPAM
Using gRPC
Working with shared resources in CloudFront
Caching and availability
Improve your cache hit ratio
Use Origin Shield
Increase availability with origin failover
Manage cache expiration
Caching and query string parameters
Cache content based on cookies
Cache content based on request headers
Control the cache key with a policy
Understand cache policies
Create cache policies
Use managed cache policies
Understand the cache key
Control origin requests with a policy
Understand origin request policies
Create origin request policies
Use managed origin request policies
Add CloudFront request headers
Understand how origin request policies and cache policies work together
Add or remove response headers with a policy
Understand response headers policies
Create response headers policies
Use managed response headers policies
Request and response behavior
How CloudFront processes HTTP and HTTPS requests
Request and response behavior for Amazon S3 origins
Request and response behavior for custom origins
Request and response behavior for origin groups
Add custom headers to origin requests
How CloudFront processes range GETs
How CloudFront processes HTTP 3xx status codes from your origin
How CloudFront processes HTTP 4xx and 5xx status codes from your origin
Generate custom error responses
Configure error response behavior
Create a custom error page for specific HTTP status codes
Store objects and custom error pages in different locations
Change response codes returned by CloudFront
Control how long CloudFront caches errors
Add, remove, or replace content
Use file versioning to update or remove existing content
Customize file URLs
Specify a default root object
Invalidate files to remove content
Determine which paths to invalidate
What you need to know when invalidating paths
Invalidating content by cache tags
What you need to know when invalidating tags
Invalidate files
Pay for file invalidation
Serve compressed files
Use AWS WAF protections
Enable AWS WAF for distributions
Manage AWS WAF security protections for CloudFront
Set up rate limiting
Disable AWS WAF security protections
Configure secure access and restrict access to content
Use HTTPS with CloudFront
Require HTTPS between viewers and CloudFront
Require HTTPS to a custom origin
Require HTTPS to an Amazon S3 origin
Supported protocols and ciphers between viewers and CloudFront
Supported protocols and ciphers between CloudFront and the origin
Use alternate domain names and HTTPS
Choose how CloudFront serves HTTPS requests
Requirements for using SSL/TLS certificates with CloudFront
Quotas on using SSL/TLS certificates with CloudFront (HTTPS between viewers and CloudFront only)
Configure alternate domain names and HTTPS
Determine the size of the public key in an SSL/TLS RSA certificate
Increase the quotas for SSL/TLS certificates
Rotate SSL/TLS certificates
Revert from a custom SSL/TLS certificate to the default CloudFront certificate
Switch from a custom SSL/TLS certificate with dedicated IP addresses to SNI
Mutual TLS authentication with CloudFront (Viewer mTLS)
Trust stores and certificate management
Enable mutual TLS for CloudFront distributions
Associate a CloudFront Connection Function
Configuring additional settings
Viewer mTLS headers for cache policies and forwarded to origin
Revocation using CloudFront Connection Function and KVS
Observability using connection logs
Origin mutual TLS with CloudFront
Certificate management with AWS Certificate Manager
Enable origin mutual TLS for CloudFront distributions
Using CloudFront Functions with origin mutual TLS
Restrict content with signed URLs and signed cookies
Restrict access to files
Specify trusted signers
Decide to use signed URLs or signed cookies
Use signed URLs
Create a signed URL using a canned policy
Create a signed URL using a custom policy
Use signed cookies
Set signed cookies using a canned policy
Set signed cookies using a custom policy
Create signed cookies using PHP
Linux commands and OpenSSL for base64 encoding and encryption
Code examples for signed URLs
Create a URL signature using Perl
Create a URL signature using PHP
Create a URL signature using C# and the .NET Framework
Create a URL signature using Java
Restrict access to an AWS origin
Restrict access to an AWS Elemental MediaPackage v2 origin
Restrict access to an AWS Elemental MediaStore origin
Restrict access to an AWS Lambda function URL origin
Restrict access to an Amazon S3 origin
Restrict access with VPC origins
Restrict access to Application Load Balancers
Geographic restriction
Use field-level encryption to help protect sensitive data
Video on demand and live streaming video
Deliver video on demand
Deliver video streaming
Media quality-aware resiliency
Use functions to customize at the edge
Differences between CloudFront Functions and Lambda@Edge
Customize with CloudFront Functions
Tutorial: Create a simple CloudFront function
Tutorial: Create a CloudFront function that uses key values
Write function code
Determine function purpose
Event structure
JavaScript runtime features
JavaScript runtime 1.0 features
JavaScript runtime 2.0 features
Helper methods for key value stores
Helper methods for origin modification
Helper methods for CloudFront SaaS Manager properties
Use async and await
CWT support for CloudFront Functions
General helper methods
Create functions
Test functions
Update functions
Publish functions
Associate functions with distributions
CloudFront KeyValueStore
Work with key value store
Create a key value store
Associate a key value store with a function
Update a key value store
Get a reference to a key value store
Delete a key value store
File format for key-value pairs
Work with key value data
Customize with CloudFront Connection Functions
Overview and workflow
Configuration and limits
Create CloudFront Connection Functions for mutual TLS (viewer) validation
Write CloudFront Connection Function code for mutual TLS (viewer) validation
Test CloudFront Connection Functions before deployment
Associate Connection Functions with distributions
Implement certificate revocation for mutual TLS (viewer) with CloudFront Functions and KeyValueStore
Step 1: Create a KeyValueStore for revoked certificates
Step 2: Create the revocation Connection Function
Step 3: Test your revocation function
Step 4: Associate the function to your distribution
Advanced revocation scenarios
Customize with Lambda@Edge
How Lambda@Edge works with requests and responses
Ways to use Lambda@Edge
Get started with Lambda@Edge
Tutorial: Basic Lambda@Edge function
Set up IAM permissions and roles
Write and create a Lambda@Edge function
Create a Lambda@Edge function
Edit a Lambda function
Add triggers for a Lambda@Edge function
CloudFront events as triggers
Choose the trigger event
Add triggers to a Lambda@Edge function
Test and debug
Delete functions and replicas
Event structure
Work with requests and responses
Example functions
Restrictions on edge functions
Restrictions on all edge functions
Restrictions on CloudFront Functions
Restrictions on Lambda@Edge
Reports, metrics, and logs
AWS billing and usage reports for CloudFront
Interpret your AWS bill and usage reports for CloudFront
View CloudFront console reports
View CloudFront cache statistics reports
View CloudFront popular objects reports
View CloudFront top referrers reports
View CloudFront usage reports
View CloudFront viewers reports
Monitor CloudFront metrics with Amazon CloudWatch
View CloudFront and edge function metrics
Create alarms
Download metrics data
CloudFront metrics
CloudFront and edge function logging
Access logs (standard logs)
Configure standard logging (v2)
Configure standard logging (legacy)
Standard logging reference
Use real-time access logs
Edge function logs
AWS CloudTrail logs
Track configuration changes with AWS Config
Security
Data protection
Identity and Access Management
How Amazon CloudFront works with IAM
Identity-based policy examples
AWS managed policies
Use service-linked roles
Troubleshoot CloudFront identity and access
Logging and monitoring
Compliance validation
Resilience
Infrastructure security
Troubleshooting
Troubleshooting distribution issues
Troubleshooting error response status codes
HTTP 400 status code (Bad Request)
HTTP 401 status code (Unauthorized)
HTTP 403 status code (Invalid method)
HTTP 403 status code (Permission Denied)
HTTP 404 status code (Not Found)
HTTP 412 status code (Precondition Failed)
HTTP 500 status code (Internal Server Error)
HTTP 502 status code (Bad Gateway)
HTTP 503 status code (Service Unavailable)
HTTP 504 status code (Gateway Timeout)
Load testing CloudFront
Quotas
Code examples
Basics
Actions
CreateDistribution
CreateFunction
CreateInvalidation
CreateKeyGroup
CreatePublicKey
DeleteDistribution
GetCloudFrontOriginAccessIdentity
GetCloudFrontOriginAccessIdentityConfig
GetDistribution
GetDistributionConfig
ListCloudFrontOriginAccessIdentities
ListDistributions
UpdateDistribution
Scenarios
Create a multi-tenant distribution and distribution tenant
Delete signing resources
Get started with a basic CloudFront distribution
Getting started with WAF
Sign URLs and cookies
CloudFront Functions examples
Add HTTP security headers
Add a CORS header
Add a cache control header
Add a true client IP header
Add an origin header
Add index.html to request URLs
Normalize query string parameters
Redirect to a new URL
Rewrite a request URI
Select origin closer to the viewer
Use key-value pairs
Validate a simple token
Document history
Documentation
...
Amazon CloudFront
Developer Guide
Documentation
Amazon CloudFront
Developer Guide
CloudFront flat-rate pricing plans
PDF
RSS
Markdown [-]
Focus mode
On this page
Benefits of CloudFront flat-rate pricing plans
Features by pricing plan tier
Monthly usage allowances
Costs covered by your plan
Reduce overall AWS costs with pricing plans
Manage your flat-rate pricing plans
Permissions
Flat-rate pricing plan quotas
Unsupported features
Documentation Amazon CloudFront Developer Guide Benefits of CloudFront flat-rate pricing plans Features by pricing plan tier Monthly usage allowances Costs covered by your plan Reduce overall AWS costs with pricing plans Manage your flat-rate pricing plans Permissions Flat-rate pricing plan quotas Unsupported features CloudFront flat-rate pricing plans combine the Amazon CloudFront global content delivery network (CDN) with multiple AWS services and features into a monthly price with no overage charges, regardless of traffic spikes or attacks. Flat-rate pricing plans include the following features for a simple monthly price:
CloudFront CDN
AWS WAF and DDoS protection
Bot management and analytics
Amazon Route 53 DNS
Amazon CloudWatch Logs ingestion
TLS certificate
Serverless edge compute
Amazon S3 storage credits each month Plans are available in Free, Pro, Business, and Premium tiers to match your application's needs. Plans don't require an annual commitment to get the best available rates. Start with the Free plan and upgrade to access more capabilities and larger usage allowances.
Topics
Benefits of CloudFront flat-rate pricing plans
Features by pricing plan tier
Monthly usage allowances
Costs covered by your plan
Reduce overall AWS costs with pricing plans
Manage your flat-rate pricing plans
Permissions
Flat-rate pricing plan quotas
Unsupported features
Benefits of CloudFront flat-rate pricing plans
The CloudFront pricing plan provides several key benefits:
Consolidated services and pricing Combine multiple AWS services and features into a single plan for one flat rate. Designed to eliminate separate service purchases and upfront pricing calculations.
No overages There are no overage charges regardless of traffic spikes or attacks.
Clear usage allowances Each plan includes published usage allowances designed for optimal performance at that tier. Monitor your usage, receive proactive notifications, and upgrade based on your application's needs, with no long-term commitments.
Protect against DDoS attacks CloudFront and AWS WAF absorb and block attacks before they reach your infrastructure. Reserves your compute, database, and infrastructure utilization only for legitimate traffic. Blocked DDoS attacks and requests blocked by AWS WAF never count against your usage allowance.
Reduce your overall AWS costs Data transfer from AWS applications running on services such as Amazon S3, AWS Application Load Balancer (ALB), or Amazon API Gateway to CloudFront continues to be free. When you serve your AWS applications through CloudFront instead of directly to the internet, your flat-rate plan covers the data transfer costs between your applications and your viewers for a simple monthly price without the worry of overages. Fewer requests reaching your origin also reduces your costs on services that charge based on usage.
Features by pricing plan tier
Each pricing plan covers one CloudFront distribution with up to one apex (root) domain that combines essential features and services into one monthly price. Each plan also includes additional S3 storage credits. Plans on higher tiers include all features from lower tier plans as well as additional features.
Free – For hobbyists, learners, and developers getting started.
Pro – Launch and grow small websites, blogs, and applications.
Business – Protect and accelerate business applications.
Premium – Scale and protect business and mission-critical applications. Select a plan tier that includes features and configurations that you need for your applications. See the following features per pricing plan.
Pricing plan features
The following table shows the CloudFront, AWS WAF and DDoS, Amazon Route 53, Amazon CloudWatch, and Amazon S3 features included in each pricing plan tier. Performance and Delivery Free Pro Business Premium Global CDN Use CloudFront's 750+ global edge locations as a massive, distributed, single point of entry for your web application. Accelerate static, dynamic, and non-cacheable applications. Yes Yes Yes Yes Content caching Store copies of your content in CloudFront's 750+ edge locations worldwide, delivering it to users from the nearest location. Reduces load times, protects your application from traffic spikes, and saves costs by serving repeated requests locally instead of from your application servers. Yes Yes Yes Yes Fast cache invalidations Remove or update cached content across all edge locations within seconds. Yes Yes Yes Yes Invalidations by cache tag Assign custom tags to your content and remove all cached content sharing a specific tag, without tracking individual file paths. Yes Yes Yes Smart routing Intelligently routes users to the optimal edge location using real-time network data, and connects to your AWS origin through the AWS private network for better performance. Yes Yes Yes Yes Tiered caching Regional edge caches sit between edge locations and your application to store content longer, reducing load on your application and maintaining fast delivery. Yes Yes Yes Yes Default caching rules Makes effective caching decisions to cache most web applications without custom configuration. Yes Yes Yes Yes Custom caching rules Control how CloudFront caches content by specifying which request values to use, optimizing for your application's performance, personalization, and freshness needs using cache policies. Yes Yes High-speed origin routing With Origin Shield, dynamic requests are routed from edge locations to your origin using CloudFront's private network for high-performance path to your origin. Yes Origin load reduction Adds an additional caching layer close to your web application using Origin Shield. Origin Shield consolidates requests from all edge locations, reducing load on your application particularly during traffic spikes. Yes Automatic origin failover Automatically routes traffic to a backup origin if your primary origin fails, maintaining high availability without disrupting users. Yes Default origin request rules Control which information from viewer requests is automatically included in requests to your origin, using AWS managed origin request policies optimized for common scenarios. Yes Yes Yes Yes Default response header rules Use AWS managed response header policies to add or remove HTTP headers in responses to viewers, preconfigured for common security headers, CORS settings, and other standard use cases. Yes Yes Yes Yes Custom origin request rules Create your own origin request policies to specify exactly which URL query strings, headers, and cookies are forwarded to your origin, enabling custom analytics and request handling. Yes Yes Custom response header rules Create your own response header policies to control exactly which HTTP headers CloudFront adds or removes in responses to viewers, such as security headers, Content Security Policy (CSP), CORS settings, and custom application headers. Yes Yes Number of cache behaviors Configure cache behaviors to control how CloudFront handles requests for specific URL patterns, including which origin serves the content, how content is cached, and whether HTTPS or signed URLs are required. 5 10 50 100 Security and Protection Always-on DDoS protection Protect against DDoS attacks that target your websites or applications. Yes Yes Yes Yes Advanced DDoS Protection Identify and block DDoS attacks in seconds using the AntiDDoS AMR. AWS learns your unique application patterns to distinguish between attacks and natural surges from legitimate users. Yes Yes Web Application Firewall (WAF) Protect against common application vulnerabilities and potential threats based on Amazon internal threat intelligence. Requests are blocked before reaching your servers. Yes Yes Yes Yes Number of WAF rules Total number of security rules you can create and enable in your WAF configuration, including both custom rules and AWS Managed Rules. 5 25 50 75 Protections for WordPress, PHP, and SQL databases Use-case based security rules to protect common applications and operating systems like WordPress, PHP, SQL databases, Linux, and Windows. Yes Yes Yes AI traffic analytics Monitor access patterns, request volumes, and popular paths of AI bots interacting with your content. AI bots are classified based on intent to detect activities like potentially unauthorized scraping used for training. Yes Yes Yes IP-based rate limiting Automatically block IP addresses that exceed a configurable number of requests over a 5-minute period, protecting against HTTP flood attacks and Denial of Service (DoS) attempts. Yes Yes Yes Yes Geographic traffic blocking Block requests from selected countries or regions. Yes Yes Yes Yes CAPTCHA challenge Require requests matching specific security rules to solve a CAPTCHA puzzle to prove that a human being is sending the request. Yes Yes Yes Header-based threat filtering Create WAF security rules that filter threats based on HTTP request headers. Yes Yes Yes Regex-based threat filtering Create WAF security rules using regular expressions to match URI paths and HTTP request attributes. Yes Yes JavaScript challenge Block automated threats by requiring browsers to complete JavaScript challenges that verify legitimate users. Yes Yes Bot management and analytics (+AI bots) Detect and analyze bot traffic with AWS WAF Bot Control for common bots. Provides controls to block, challenge, or allow unverified bots while identifying and distinguishing verified bots like search engines. Monitor AI bots and take action based on bot intent. Yes Yes Custom WAF response Set a specific HTTP status code and optional custom HTML, plain text, or JSON response when requests are blocked by a rule. Yes Yes Yes Header Insertion Add custom HTTP headers to requests that pass WAF inspection, enabling downstream applications to process requests differently or flag them for analysis. Yes Yes Yes Yes Request body inspection Maximum size of HTTP request body content that can be inspected by AWS WAF for threats and malicious patterns. 16 KB 16 KB 64 KB 64 KB Private origins within VPC Enhance security by keeping your application in a VPC private subnet, accessible only through your CloudFront distributions and hidden from the public internet, using VPC origins. Yes Yes Mutual TLS (origin) Restrict unauthorized access to your application (origin) using TLS-based client certificates, ensuring only your authorized CloudFront distributions can establish connections to your application. Yes Yes Origin Access Control (OAC) Maintain a private S3 bucket and only allow access through your designated CloudFront distribution, ensuring your content is protected by your WAF rules, rate limits, and other security controls configured in your CloudFront distribution. Yes Yes Yes Yes Free TLS certificate Free TLS certificate for your domain with automatic renewal through AWS Certificate Manager. Yes Yes Yes Yes Signed URLs Create secure URLs that provide temporary access to private content for specific users. Commonly used to share private documents with authorized users or grant secure access to protected content after payment verification. Yes Yes Yes Yes Mutual TLS (mTLS) Restrict access to your application using mTLS authentication, ensuring only trusted clients with valid certificates can connect. Yes Edge Compute Serverless edge compute Run lightweight JavaScript at the edge to modify URLs, HTTP headers, and request/response elements in milliseconds using CloudFront Functions. Lambda@Edge can also be used with all plan tiers, but unlike CloudFront Functions, Lambda@Edge invocations are billed on a pay-as-you-go basis. Yes Yes Yes Yes Edge key-value store Store data at the edge using KeyValueStore for fast and dynamic content customization with CloudFront Functions. Yes Yes Yes Network and Protocol Support IPv6 Deliver content over both modern IPv6 and traditional IPv4 connections from CloudFront to viewers and origins. Enables end-to-end IPv6 support for your applications. Yes Yes Yes Yes HTTP/2 Enable faster page loads through modern protocol features like multiplexing, header compression, and stream prioritization. Automatically used when supported by browsers and clients. Yes Yes Yes Yes HTTP/3 Deliver content using QUIC to browsers and clients that support it, enabling faster connections and improved performance. Particularly benefits mobile users and maintains connections when network conditions change. Yes Yes Yes Yes TLS 1.3 Deliver faster HTTPS connections through a handshake process that requires one round-trip compared to two in TLS 1.2. Reduces first byte latency by up to 33% compared to previous TLS versions. Enabled end-to-end for your applications. Yes Yes Yes Yes WebSockets Enable real-time, persistent two-way communication between browsers and servers. Ideal for AI chat applications, multi-player gaming, collaborative workspaces, and real-time data feeds like financial trading platforms. Yes Yes Yes Yes Logging and Monitoring Access Logs Access detailed CloudFront request logs to understand security and delivery traffic patterns, with Amazon CloudWatch Logs ingestion is included at no extra cost. Yes Yes Yes WAF request logs Access detailed AWS WAF request logs to understand security and delivery traffic patterns. Amazon CloudWatch Logs ingestion is included at no extra cost. Yes Yes Yes Security dashboard Monitor security events, investigate threats, and take immediate blocking actions using visual analytics without writing security rules. Pro and above includes visual log analyzer to quickly understand traffic patterns without querying logs. Yes Yes Yes Yes DNS Amazon Route 53 DNS Fast, reliable public authoritative DNS service using Route 53. Yes Yes Yes Yes Records per Hosted Zone The maximum number of DNS records allowed in the hosted zone. 50 100 1000 5000 DNSSEC Protect your domain against DNS spoofing and man-in-the-middle attacks where attackers intercept DNS queries and redirect visitors to fake websites. Secures DNS traffic by cryptographically signing your DNS records. Yes Yes Yes Yes Storage Amazon S3 storage Amazon S3 storage credits that offset any S3 Standard storage costs in your AWS account. Not limited to CloudFront content or subject to plan usage allowances. 5 GB 50 GB 1 TB 5 TB Support and Reliability 24x7 account and billing support One-on-one responses to account and billing questions. If you have a paid support plan, you're eligible to receive support on all flat-rate plans. Yes Yes Yes Yes Documentation and AWS Support forums Access product documentation, technical papers, best practices guides, AWS re:Post community forums, and service health information to help you plan and troubleshoot. Yes Yes Yes Yes Uptime SLA Service Level Agreements (SLA) for Amazon CloudFront, AWS WAF, Amazon Route 53, and Amazon CloudWatch provide service availability commitments. In the event AWS does not meet the associated SLA's commitment, you will be eligible to receive a service credit. Yes Yes
Monthly usage allowances
Each flat-rate plan includes a monthly usage allowance designed for optimal performance at that tier. Usage allowances are not hard limits—they represent the baseline usage your plan is designed to support. You can track your usage in the CloudFront console at any time and will receive automatic email notifications when you reach 50%, 80%, and 100% of your allowance.
What counts toward your usage allowance
Blocked DDoS attacks and requests blocked by AWS WAF never count against your usage allowance. Only traffic that makes it past your AWS WAF security rules counts towards your allowance. This means attacks and unwanted traffic won't count against you, and you maintain the ability to define exactly what traffic your application blocks or allows.
What happens when usage exceeds the allowance
Plans are designed to be flexible and accommodate real-world traffic patterns like traffic variability, organic growth, and viral events. Most importantly: you will not incur overage charges, regardless of how much you exceed your allowance. If your usage exceeds your allowance through sustained growth over multiple months or through unusually high usage in a single month, we may adjust how we deliver your traffic. Most customers never experience performance adjustments. Here's how it works:
Your first traffic spike up to 3x your monthly allowance won't affect your service that month. This one-time accommodation handles unexpected events like viral content or successful product launches without penalizing your success.
Sustained usage above your allowance is evaluated over 2-3 months or more, not immediately. Minor fluctuations and moderate growth are expected and accommodated. Only substantial, sustained excess usage indicate your application has outgrown your tier.
You'll receive notifications each month as you approach and exceed your allowance. If your usage consistently and significantly exceeds your plan, we recommend upgrading to a tier that matches your growth and ensures optimal performance as you scale. You control your performance by upgrading when your baseline usage patterns change.
If you continue to substantially exceed your plan's usage allowance without upgrading, we may adjust how we deliver your traffic. For example, we might serve your traffic from fewer or more distant edge locations or adjust performance. The degree of adjustment is proportional—small excess usage sees minimal changes, larger sustained excess sees more noticeable changes. Upgrading restores full performance. Most customers never experience performance adjustments. Plans are designed to accommodate normal growth patterns. Monthly usage allowances per plan tier
Eligibility based on historical usage
Your historical CloudFront usage may affect your eligibility to sign up for or downgrade to specific plan tiers. If your recent usage exceeds a plan tier's usage allowances, you may need to select a higher tier that better aligns with your workload.
Costs covered by your plan
Your plan covers costs for:
Your CloudFront distribution
The AWS WAF web ACL, custom rules, AWS Managed Rules, and request fees for the web ACL associated with your distribution
CloudWatch Logs ingestion for your distribution's CloudFront access logs and associated WAF logs
The Route 53 hosted zone, DNS records, and DNS queries when attached to your distribution's plan You will also receive S3 credits to offset S3 Standard storage usage in your payer account, whether or not an S3 bucket is used as an origin for your CloudFront distribution.
Route 53 DNS management and your plan
If you use Route 53 for DNS and attach the zone to your plan, your flat-rate plan can include your Route 53 hosted zone costs. You can attach the zone to your plan in the Manage Plan section of your CloudFront distribution. When your zone is attached to the plan, your plan covers your hosted zone's standard costs, including the monthly hosted zone fee, DNS records, and DNS query fees subject to respective allowances per tier, provided below. The hosted zone must meet the following requirements:
Exist in the same AWS account as your CloudFront distribution
Maintain the number of records allowed per hosted zone for your plan tier
Cover the domain used by your CloudFront distribution If your hosted zone is not attached to your plan, it will remain on pay-as-you-go pricing, where you're responsible for all standard Route 53 costs.
Understanding monthly DNS query allowances
When your hosted zone is attached to your plan, you get:
Note
To maximize your plan benefits, use ALIAS records to point to your CloudFront distribution. ALIAS records pointing to CloudFront and other supported AWS services don't count against your monthly DNS query allowance. All other DNS queries, including CNAME records to CloudFront, count against your DNS query allowance.
Exceeding DNS query allowances
If your DNS query usage exceeds your plan's monthly allowance, AWS may notify you. At that point, you can detach your hosted zone from the plan in the Manage Plan section of your CloudFront distribution to return the hosted zone to pay-as-you-go pricing. If you do not detach your hosted zone after receiving this notification, AWS may automatically transition the hosted zone to pay-as-you-go pricing. When a hosted zone moves to pay-as-you-go pricing, you are responsible for all standard Route 53 costs. Your CloudFront distribution and all other plan benefits continue unchanged.
Reduce overall AWS costs with pricing plans
CloudFront flat-rate pricing plans can reduce your overall AWS costs in three ways: First, data transfer costs between CloudFront and your AWS applications running on services such as Amazon S3, AWS Application Load Balancer (ALB), or Amazon API Gateway are automatically waived. When you serve your AWS applications through CloudFront instead of directly to the internet, your flat-rate plan covers the data transfer costs between your applications and your viewers for a simple monthly price without the worry of overages. Second, CloudFront reduces your compute and database costs by protecting your application infrastructure and reducing the number of requests reaching your origin. It serves cached content from edge locations or regional edge caches, collapses duplicate requests, and blocks malicious and unwanted traffic before it reaches your backend services. This means fewer requests hitting your application servers, databases, and other AWS services that charge based on usage, which reduces your costs. Finally, each plan includes Amazon S3 Standard storage credits to offset storage usage for your AWS account. To maximize these savings, configure your AWS origins to only accept traffic from CloudFront. For S3, use Origin Access Control OAC with private buckets to grant access to your designated CloudFront distribution. For Application Load Balancer, Network Load Balancer, and Amazon EC2 instances in private subnets, restrict access to your designated CloudFront distribution using VPC Origins.
Manage your flat-rate pricing plans
Follow these procedures in the CloudFront console to subscribe, upgrade, downgrade, or cancel a pricing plan for your distributions.
Subscribe a new distribution to a pricing plan
When you create a new distribution, you can subscribe to a pricing plan.
To subscribe a new distribution to a pricing plan
Subscribe an existing distribution to a pricing plan
When you update a distribution, you can subscribe to a pricing plan. Before choosing a pricing plan, ensure that your distribution configuration is compatible with the plan that you want.
Tip
If your current distribution uses any unsupported features, you must disable those features before you can subscribe to the pricing plan. This includes disabling features like real-time access logs. Once your distribution configuration is compatible, you can choose your desired pricing plan while update a distribution.
To subscribe an existing distribution to a pricing plan
Upgrade a pricing plan
We recommend that you upgrade a plan if you're approaching or have exceeded your monthly usage allowance, or if you want to enable a feature that is available in the next tier. When you upgrade to a higher plan tier, changes take effect immediately. Your price and usage allowance are prorated. Your distribution and associated resources will have access to the available features and higher usage allowance of your new plan.
To upgrade a pricing plan
Downgrade a pricing plan
We recommend that you downgrade to a lower plan tier if you don't need the additional features on your existing tier. For example, you might downgrade if you expect your application will experience lower traffic. If you downgrade to a lower tier, your billing changes will take effect at the beginning of the next billing cycle. If your distribution currently exceeds the usage allowance for a plan, you can downgrade once your usage is within the usage allowance for your desired tier. To avoid being charged for your existing plan tier at the next billing cycle, downgrade before the end of the month.
To downgrade a pricing plan
Cancel a pricing plan
When you cancel a pricing plan, you will maintain your flat-rate price through the end of your current billing cycle. Your distribution and all associated plan resources will then switch to pay-as-you-go pricing at the start of the next billing cycle.
To cancel a pricing plan
Cancel a pending plan change
If you downgraded or canceled your flat-rate pricing plan, you must wait until the end of the current billing cycle before your changes are in effect. To keep your existing flat-rate pricing plan, upgrade, or downgrade your pricing plan again, you must first cancel your pending plan change.
To cancel a pending pricing plan change
Deleting a distribution with a pricing plan
You can't delete a distribution that is subscribed to a pricing plan. You must first cancel the pricing plan and then after the current billing cycle, delete the distribution.
To delete a distribution with a pricing plan
Note
You can disable a distribution that is subscribed to a pricing plan, but you will still incur charges for that plan. To stop incurring charges for your plan, you must first cancel it.
Permissions
To view or manage pricing plan subscriptions for your CloudFront distributions, you must have the required permissions. For more information, see AWS managed policy: CloudFrontFullAccess and AWS managed policy: CloudFrontReadOnlyAccess.
Flat-rate pricing plan quotas
The following table shows the quotas and restrictions for CloudFront flat-rate pricing plans.
Note
These quotas can't be increased for your AWS account.
Unsupported features
Before you can associate a distribution with a pricing plan, you must ensure that certain features are disabled and associations are removed.
Notes
If your distribution or account has any of these restrictions, you must resolve them before you can use pricing plans. After you make changes to your distribution, wait for the changes to propagate to all edge locations.
You must have a AWS WAF Web ACL associated with your distribution if you're using a pricing plan. This resource cannot be removed or disassociated from your distribution unless you switch to pay-as-you-go pricing for that distribution.
Unsupported features
You can't subscribe distributions to a pricing plan if their configuration contains the following unsupported features. You can disable the unsupported feature and use an alternative option, or keep pay-as-you-go for your distribution.
Unsupported associations
You can't subscribe a distribution to a pricing plan if the distribution is already associated with any of the following resources that are already associated with other distributions. Resources that are associated to a distribution that is subscribed to a pricing plan can only be used for that distribution. For example, if you have a CloudFront function that is using a key value store, neither the function nor the key value store can be shared for a distribution that is on a pricing plan.
CloudFront Functions
CloudFront Functions associated with a key value store
AWS WAF Web ACLs To subscribe a distribution to a pricing plan, either remove the associated resource or replace it with another one.
Account-level constraints
AWS accounts are not eligible for pricing plans if they meet any of the following conditions:
You reached the maximum number of subscriptions allowed. See Flat-rate pricing plan quotas.
Your account is using AWS Free Tier.
Resource-level constraints
Distributions are not eligible for pricing plans if they meet any of the following conditions:
Your distribution has enabled AWS Shield Advanced
Your distribution has enabled the Firewall Manager Service for your web ACL. Firewall Manager won't manage your CloudFront distribution's WebACL in a pricing plan.
Additional features that can affect your pricing plan
Flat-rate pricing plans enable you to pay a flat-rate for your CloudFront distribution and the features listed above that are both included in your plan and associated with your CloudFront distribution. All other features may incur additional charges, including but not limited to the following:
CloudFront
Lambda@Edge function invocations
AWS WAF
CAPTCHA puzzles created using the JavaScript API are billed using pay-as-you-go pricing. CAPTCHA responses configured in your AWS WAF rules (the most common use case) are included in your plan at no additional charge.
Route 53
Route 53 DNSSEC has an AWS KMS cost
Route 53 IP (CIDR) blocks (the first 1,000 are free per AWS account)
Route 53 Health Checks (the first 50 are free per AWS account)
Logging features
Route 53 DNS Query Logs, CloudFront Functions logs, and CloudFront Connection Function Logs
AWS WAF log delivery to Amazon S3
CloudFront or AWS WAF log delivery to Amazon Data Firehose
Additional CloudWatch metrics for CloudFront
CloudFront access logs in Parquet format
Note
Your plan includes Amazon CloudWatch Logs ingestion for CloudFront standard logs (access logs) and WAF logs for no added costs. All other CloudWatch costs such as storage and querying are not covered by your plan. All other logs are also billed separately.
Note
Your plan includes public authoritative DNS from Route 53. When your Route 53 hosted zone is attached to your pricing plan, your plan covers your hosted zone's standard costs, including the monthly hosted zone fee, DNS records, and DNS query fees subject to respective allowances per tier. All other costs from Route 53 usage and features not listed above as included in your plan are not covered by your plan.
Pricing plans vs. pay-as-you-go pricing
Flat-rate plans and pay-as-you-go pricing offer different advantages based on your needs. With flat-rate plans, you pay one price that includes multiple AWS services like CloudFront, AWS WAF, Route 53, and CloudWatch Logs ingestion and never face overage charges, even during traffic spikes or attacks. With pay-as-you-go pricing, you're billed separately for each service and feature based on your actual usage. While this provides complete flexibility in service selection and configuration, your costs can vary month to month based on traffic patterns, and you will need to monitor usage across multiple services to manage costs. Flat-rate plans are ideal if you want combined monthly billing, simplified service configuration, and built-in security features without worrying about overage charges. Pay-as-you-go pricing is a better choice if you need complete control over individual service features, custom configurations, access to features not available in flat-rate plans, or if you expect to handle large, predictable traffic spikes. Amazon CloudFront flat-rate pricing plans may not be combined with any other offers, promotions, or discounts. Javascript is disabled or is unavailable in your browser. To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions. Document Conventions Get started with a secure static website Configure distributions Did this page help you? - Yes Thanks for letting us know we're doing a good job! If you've got a moment, please tell us what we did right so we can do more of it. Did this page help you? - No Thanks for letting us know this page needs work. We're sorry we let you down. If you've got a moment, please tell us how we can make the documentation better.
Did this page help you? Yes No Provide feedback
Next topic:
Configure distributions
Previous topic:
Get started with a secure static website
Get Started
AWS Hands-On Tutorials
AWS Solutions Library
AWS Decision Guides
Service Guides
Choosing a generative AI service
AWS service guides
AWS CLI Tutorials on GitHub
Developer Tools
AWS Code Example Library
AWS CLI
AWS Builder Center
AWS Developer Tools Blog
Helpful Links
Download the AWS Docs MCP Server
Sign into the AWS Console
AWS re:Post
Privacy
Site terms
Cookie preferences
© 2026, Amazon Web Services, Inc. or its affiliates. All rights reserved.
English
Language selector
Top
