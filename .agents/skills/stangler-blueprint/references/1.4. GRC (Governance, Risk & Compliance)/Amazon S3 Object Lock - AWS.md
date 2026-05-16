---
name: Amazon S3 Object Lock - AWS
keywords: (placeholder)
metadata:
  url: https://aws.amazon.com/s3/features/object-lock/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T19:00:57.430Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
S3 Object Lock – Amazon S3 – Amazon Web Services
Select your cookie preferences
We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.
If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”
Accept Decline Customize
Customize cookie preferences
We use cookies and similar tools (collectively, "cookies") for the following purposes.
Essential
Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms. [x]
Allowed
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
Your privacy choices
We and our advertising partners (“we”) may use information we collect from or about you to show you ads on other websites and online services. Under certain laws, this activity is referred to as “cross-context behavioral advertising” or “targeted advertising.”
To opt out of our use of cookies or similar technologies to engage in these activities, select “Opt out of cross-context behavioral ads” and “Save preferences” below. If you clear your browser cookies or visit this site from a different device or browser, you will need to make your selection again. For more information about cookies and how we use them, read our Cookie Notice . [x] allowed
Allow cross-context behavioral ads [-] not allowed Opt out of cross-context behavioral ads
To opt out of the use of other identifiers, such as contact information, for these activities, fill out the form here .
For more information about how AWS handles your information, read the AWS Privacy Notice .
Cancel Save preferences
Unable to save cookie preferences
We will only store essential cookies at this time, because we were unable to save your cookie preferences.
If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.
Dismiss
Skip to main content 
Filter: All
English
Contact us
AWS Marketplace
Support
My account
More
Search Filter: All
Sign in to console
Create account
Amazon S3
Amazon S3
Amazon S3 Features
Amazon S3 Object Lock
Amazon S3 Object Lock
Data protection from ransomware events with object-level immutability to protect objects from accidental or malicious deletions and overwrites
Protect data on Amazon S3 getting started tutorial
Overview
Amazon S3 is the trusted primary storage for millions of customers from all around the world. With 99.999999999% (11 9s) of data durability, customers can store and protect business-critical data for virtually any use case, including cloud-native applications, data lake analytics output, and media files. As with any data, it is best practice to have a backup and to put safeguards in place against malicious or accidental deletion. S3 Object Lock blocks permanent object deletion during a customer-defined retention period so that you can enforce retention policies as an added layer of data protection or for regulatory compliance. With S3 Object Lock, S3 Versioning is automatically enabled, and these features work together to prevent locked object versions from being permanently deleted (accidental or intentional) or overwritten using a write-once-read-many (WORM) model. S3 Object Lock is the industry standard for object storage immutability for ransomware protection and is used in cloud storage, backup and data protection solutions by AWS Storage partners such as Cohesity, Commvault, Rubrik, Veeam, and Veritas.
Play  
Video Player is loading.
Play Video
Play Skip Backward Skip Forward
Mute
Current Time 0:00
/
Duration 12:54
Loaded: 0.00%
00:00
Stream Type LIVE
Seek to live, currently behind live LIVE
Remaining Time - 12:54
1x
Playback Rate
Chapters
Chapters
Descriptions
descriptions off, selected
Captions
captions settings, opens captions settings dialog
captions off, selected
Audio Track
Picture-in-Picture Fullscreen
This is a modal window.
Beginning of dialog window. Escape will cancel and close the window.
Text Color
White
Black
Red
Green
Blue
Yellow
Magenta
Cyan
Opacity
Opaque
Semi-Transparent
Text Background Color
Black
White
Red
Green
Blue
Yellow
Magenta
Cyan
Opacity
Opaque
Semi-Transparent
Transparent
Caption Area Background Color
Black
White
Red
Green
Blue
Yellow
Magenta
Cyan
Opacity
Transparent
Semi-Transparent
Opaque
Font Size
50%
75%
100%
125%
150%
175%
200%
300%
400%
Text Edge Style
None
Raised
Depressed
Uniform
Drop shadow
Font Family
Proportional Sans-Serif
Monospace Sans-Serif
Proportional Serif
Monospace Serif
Casual
Script
Small Caps
Reset Done
Close Modal Dialog
End of dialog window.
Benefits
Data protection from ransomware events and accidental changes
Data immutability is a core aspect of data protection planning because it prevents unintended changes or deletions by authorized users, changes by unauthorized users. This helps prevent ransomware events from deleting or altering your data. S3 Object Lock prevents data from being altered or deleted by any person or process, whether unintended or because of malicious activity.
Meet compliance and regulatory requirements
You can use S3 Object Lock to help meet regulatory requirements that require WORM storage, or to add another layer of protection against object changes and deletion. Cohasset Associates have assessed S3 Object Lock for environments that are subject to SEC 17a-4, CFTC, and FINRA regulations. You can use compliance mode, which cannot be overridden, to help your data meet regulated compliance monitoring. For more information about how Object Lock relates to these regulations, see the Cohasset Associates Compliance Assessment.
Restore versions of objects
You can use the S3 Versioning feature to preserve, retrieve, and restore every version of every object stored in your buckets. With versioning you can recover more easily from both unintended user actions and application failures. S3 Versioning, which is automatically enabled with S3 Object Lock, provides data resiliency with the ability to fall back to a previous version. Learn more.
Managing object retention with S3 Object Lock
S3 Object Lock provides two ways to manage object retention: retention periods and legal holds. With S3 Object Lock enabled on a bucket, an object version can have both a retention period and a legal hold, one but not the other, or neither.
Retention period — Specifies a fixed period of time during which an object remains locked. During this period, your object is WORM-protected and can't be overwritten or deleted. When you place a retention period on an object version, Amazon S3 stores a timestamp in the object version's metadata to show when the retention period expires. After the retention period expires, the object version can be overwritten or deleted unless you also placed a legal hold on the object version. Using a bucket policy, you can set minimum and maximum allowable retention periods for a bucket to help you establish a range of allowable retention periods. For more information, see retention periods.
Legal hold — Provides the same protection as a retention period, but it has no expiration date. Instead, a legal hold remains in place until you explicitly remove it. Legal holds are independent from retention periods. For more information, see legal holds.
Retention periods and retention modes are always configured in tandem, unlike legal holds, which are configured independently. S3 Object Lock provides two retention modes that apply different levels of protection to your objects. You can apply either retention mode to any object version that is protected by Object Lock.
Governance mode — In governance mode, users can't overwrite or delete an object version or alter its lock settings unless they have special permissions. With governance mode, you protect objects against being deleted by most users, but you can still grant some users permission to alter the retention settings or delete the object if necessary. You can also use governance mode to test retention-period settings before creating a compliance-mode retention period.
Compliance mode — In compliance mode, a protected object version can't be overwritten or deleted by any user, including the root user in your AWS account. When an object is locked in compliance mode, you cannot change the retention mode, and you cannot shorten the retention period. Compliance mode helps ensure that an object version can't be overwritten or deleted for the duration of the retention period. S3 Object Lock has been assessed for SEC Rule 17a-4(f), FINRA Rule 4511, and CFTC Regulation 1.31 by Cohasset Associates.
Show more
Using S3 Object Lock at scale with S3 Batch Operations
S3 Object Lock can be enabled easily on the bucket for all new objects with a default lock. For existing objects, you can use S3 Batch Operations with S3 Object Lock to place a lock or extend any existing retention, or enable or remove a legal hold for up to billions of objects at once. You specify the list of target objects in your manifest and submit it to Batch Operations for completion.
Like all other S3 Object Lock settings, retention periods apply to individual object versions. Different versions of a single object can have different retention modes and periods.
For example, suppose that you have an object that is 15 days into a 30-day retention period, and you upload a new object into Amazon S3 with the same name and a 60-day retention period. In this case, your upload succeeds, and Amazon S3 creates a new version of the object with a 60-day retention period. The older version maintains its original retention period and becomes deletable in 15 days.
You can extend a retention period after you've applied a retention setting to an object version. To do this, submit a new lock request using S3 Batch Operations for the object version with a Retain Until Date that is later than the one currently configured for the object version. Amazon S3 replaces the existing retention period with the new, longer period. Learn more.
How does AWS Data Exchange use S3 Access Points?
AWS Data Exchange for Amazon S3 accelerates time to insight with direct access to data providers' Amazon S3 data. AWS Data Exchange for Amazon S3 helps you easily find, subscribe to, and use third-party data files for storage cost optimization, simplified data licensing management, and more.
Once subscribed, you are automatically granted access to the provider's S3 bucket through a dedicated S3 Access Point managed by AWS Data Exchange. You can use the S3 Access Point alias to easily analyze the shared files with AWS services, such as Amazon Athena, Amazon SageMaker Feature Store, and Amazon EMR, without needing to create or manage data copies.
Visit the AWS Data Exchange for Amazon S3 product page to learn more.
Partners
  
  
  
How does AWS Data Exchange use S3 Access Points?
AWS Data Exchange for Amazon S3 accelerates time to insight with direct access to data providers' Amazon S3 data. AWS Data Exchange for Amazon S3 helps you easily find, subscribe to, and use third-party data files for storage cost optimization, simplified data licensing management, and more.
Once subscribed, you are automatically granted access to the provider's S3 bucket through a dedicated S3 Access Point managed by AWS Data Exchange. You can use the S3 Access Point alias to easily analyze the shared files with AWS services, such as Amazon Athena, Amazon SageMaker Feature Store, and Amazon EMR, without needing to create or manage data copies.
Visit the AWS Data Exchange for Amazon S3 product page to learn more.
Get started with S3 for data protection
For data stored in Amazon S3, best practices start with Amazon S3 Versioning, which allows you to preserve, retrieve, and restore every version of every object stored in an Amazon S3 bucket. You can then add Amazon S3 Object Lock to prevent data from being deleted or overwritten for a fixed amount of time, or indefinitely. For creating additional copies of your data in another AWS Region for multi-Region protection, you can enable Amazon S3 Replicatio n to a bucket with S3 Object Lock turned on. Then you can use S3 Replication with both S3 Versioning and S3 Object Lock to automatically copy objects across AWS Regions and separate AWS accounts. In order to use S3 Object Lock with existing objects or to extend the lock period on existing objects that are nearing the lock expiration, you can use S3 Batch Operations and S3 Inventory Reports. Finally, you can bring visibility of your current data protection levels and the usage of these features all together into a single dashboard with Amazon S3 Storage Lens.
To learn more about how you can protect your data on Amazon S3, visit the Getting Started tutorial on S3 data protection.
Get started with Amazon S3 Object Lock
[
Read the S3 Object Lock user guide
Learn More](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)
[
Sign up for a free account
Sign up](https://console.aws.amazon.com/s3/home)
[
Start building in the console
Sign in](https://console.aws.amazon.com/s3/home)
Create an AWS account
Learn
What Is AWS?
What Is Cloud Computing?
What Is Agentic AI?
Cloud Computing Concepts Hub
AWS Cloud Security
What's New
Blogs
Press Releases
Resources
Getting Started
Training
AWS Trust Center
AWS Solutions Library
Architecture Center
Product and Technical FAQs
Analyst Reports
AWS Partners
Developers
Builder Center
SDKs & Tools
.NET on AWS
Python on AWS
Java on AWS
PHP on AWS
JavaScript on AWS
Help
Contact Us
File a Support Ticket
AWS re:Post
Knowledge Center
AWS Support Overview
Get Expert Help
AWS Accessibility
Legal
English
Back to top
Amazon is an equal opportunity employer and does not discriminate on the basis of protected veteran status, disability or other legally protected status.        
Privacy
Site terms
Your Privacy Choices
Cookie Preferences
© 2026, Amazon Web Services, Inc. or its affiliates. All rights reserved.
