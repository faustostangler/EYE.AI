---
name: Quality Attributes | Why Software Architecture is Important and Essential Activities - InformIT
keywords: (placeholder)
metadata:
  url: https://www.informit.com/articles/article.aspx?p=3128836&seqNum=3
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Quality Attributes | Why Software Architecture is Important and Essential Activities | InformIT
if(isEnableGA){ if(currentEnvironment == 'QA'){
}else{
} }
Home > Articles
Why Software Architecture is Important and Essential Activities
By Murat Erder, Pierre Pureur, Eoin Woods
May 21, 2021
📄 Contents
␡
Essential Activities Overview
Architectural Decisions
Quality Attributes
Technical Debt
Feedback Loops: Evolving an Architecture
Common Themes in Today's Software Architecture Practice
Summary
⎙ Print
< Back Page 3 of 7 Next >
This chapter is from the book 
This chapter is from the book
Continuous Architecture in Practice: Software Architecture in the Age of Agility and DevOps
Learn More  Buy
This chapter is from the book
This chapter is from the book 
Continuous Architecture in Practice: Software Architecture in the Age of Agility and DevOps
Learn More  Buy
Quality Attributes
For any software system, requirements fall in the following two categories:
Functional requirements: These describe the business capabilities that the system must provide as well as its behavior at runtime.
Quality attribute (nonfunctional) requirements: These describe the quality attributes that the system must meet in delivering functional requirements.
Quality attributes can be viewed as the -ilities (e.g., scalability, usability, reliability, etc.) that a software system needs to provide. Although the term nonfunctional requirements has widespread use in corporate software departments, the increasingly common term used in the industry is quality attributes. This term more specifically addresses the concern of dealing with critical attributes of a software system. 11
If a system does not meet any of its quality attribute requirements, it will not function as required. Experienced technologists can point to several examples of systems that fulfill all of their functional requirements but fail because of performance or scalability challenges. Waiting for a screen to update is probably one of the most frustrating user experiences you can think of. A security breach is not an incident that any technologist would want to deal with. These examples highlight why addressing quality attributes is so critical. Quality attributes are strongly associated with architecture perspectives, where a perspective is reusable architectural advice on how to achieve a quality property. 12
Formal definition of quality attributes is pretty established in the standards world, although few practitioners are aware of them. For example, the product quality model defined in ISO/IEC 25010, 13 part of the SQuaRe model, comprises the eight quality characteristics shown in Figure 2.5.
Figure 2.5 Product quality model
It is difficult to express quality attributes outside of a particular system context. For example, latency may be nice to have in a tax-filing application but disastrous for an autopilot. This makes it challenging to adopt such frameworks in their entirety, and defining a complete list of all quality attributes can be seen as an unnecessary academic exercise.
However, addressing the key quality attributes of your software system is one of the most important architectural considerations. The most important quality attributes need to be selected and prioritized. In practice, we can say that approximately 10 quality attribute scenarios are a manageable list for most software systems. This set is equivalent to what can be considered as architecturally significant scenarios. Architecturally significant implies that the scenarios have the most impact on the architecture of the software system. These are normally driven by the quality attribute requirements that are difficult to achieve (e.g., low latency, high scalability). In addition, these scenarios are the ones that impact how the fundamental components of the system are defined, implying that changing the structure of these components in the future will be a costly and difficult exercise.
Experienced software practitioners know that a given set of functional capabilities can often be implemented by several different architectures with varying quality attribute capabilities. You can say that architectural decisions are about trying to balance tradeoffs to find a good enough solution to meet your functional and quality attribute requirements.
Quality Attributes and Architectural Tactics
Functional requirements are usually well documented and carefully reviewed by the business stakeholders, whereas quality attributes are documented in a much briefer manner. They may be provided as a simple list that fits on a single page and are not usually as carefully scrutinized and tend to be truisms, such as “must be scalable” and “must be highly usable.”
However, our view is that quality attributes drive the architecture design. As stated by Bass, Clements, and Kazman, “Whether a system will be able to exhibit its desired (or required) quality attributes is substantially determined by its architecture.” 14 We need to make architectural decisions to satisfy quality attributes, and those decisions often are compromises, because a decision made to better implement a given quality attribute may have a negative impact on the implementation of other quality attributes. Accurately understanding quality attribute requirements and tradeoffs is one of the most critical prerequisites to adequately architect a system. Architectural decisions are often targeted to find the least-worst option to balance the tradeoffs between competing quality attributes.
Architectural tactics are how we address quality attributes from an architectural perspective. An architectural tactic is a decision that affects the control of one or more quality attribute responses. Tactics are often documented in catalogs in order to promote reuse of this knowledge among architects. We refer to architectural tactics throughout the book, in particular in chapters 5 through 7, that focus on specific quality attributes.
Working with Quality Attributes
In the Continuous Architecture approach, our recommendation is to elicit and describe the quality attribute requirements that will be used to drive architectural decisions. But how do we describe quality attributes? A quality attribute name by itself does not provide sufficiently specific information. For example, what do we mean by configurability? Configurability could refer to a requirement to adapt a system to different infrastructures—or it could refer to a totally different requirement to change the business rules of a system. Attribute names such as “availability,” “security,” and “usability” can be just as ambiguous. Attempting to document quality attribute requirements using an unstructured approach is not satisfactory, as the vocabulary used to describe the quality attributes may vary a lot depending on the perspective of the author.
A problem in many modern systems is that the quality attributes cannot be accurately predicted. Applications can grow exponentially in term of users and transactions. On the flip side, we can overengineer the application for expected volumes that might never materialize. We need to apply principle 3, Delay design decisions until they are absolutely necessary, to avoid overengineering. At the same time, we need to implement effective feedback loops (discussed later in this chapter) and associated measurements so that we can react quickly to changes.
We recommend leveraging the utility tree technique from the architecture tradeoff analysis method, or ATAM. 15 Documenting architecture scenarios that illustrate quality attribute requirements is a key aspect of this technique.
Building the Quality Attributes Utility Tree
We do not go into details of the ATAM utility tree, which is covered in our original book. 16 The most important aspect is to clearly understand the following three attributes for each scenario:
Stimulus: This portion of the architecture scenario describes what a user or any external stimulus (e.g., temporal event, external or internal failure) of the system would do to initiate the architecture scenario.
Response: This portion of the architecture scenario describes how the system should be expected to respond to the stimulus.
Measurement: The final portion of the architecture scenario quantifies the response to the stimulus. The measurement does not have to be extremely precise. It can be a range as well. What is important is the ability to capture the end-user expectations and drive architectural decisions.
Another attribute you can include in defining the scenario is
Environment: The context in which the stimulus occurs, including the system's state or any unusual conditions in effect. For example, is the scenario concerned with the response time under typical load or peak load?
Following is an example of a quality attribute scenario for scalability:
Scenario 1 Stimulus: The volume of issuances of import letters of credit (L/Cs) increases by 10 percent every 6 months after TFX is implemented.
Scenario 1 Response: TFX is able to cope with this volume increase. Response time and availability measurements do not change significantly.
Scenario 1 Measurement: The cost of operating TFX in the cloud does not increase by more than 10 percent for each volume increase. Average response time does not increase by more than 5 percent overall. Availability does not decrease by more than 2 percent. Refactoring the TFX architecture is not required.
As we evolve the case study throughout this book, we provide several more examples using the same technique.
< Back Page 3 of 7 Next >
🔖 Save To Your Account
InformIT Promotional Mailings & Special Offers
⚠
I would like to receive exclusive offers and hear about products from InformIT and its family of brands. I can unsubscribe at any time.
Email Address Submit 
books, eBooks, and digital learning

 View Your Cart
Join | Sign In
Search 🔎
Search 🔎
 View Your Cart
👤 Sign In
Join
Store
Business & Management
Certification
Cloud Computing & Virtualization
Data
Digital Photography
Engineering
Graphics & Web Design
Home & Office Computing
Information Technology
Mobile Application Development & Programming
Networking
Open Source
Operating Systems, Server
Programming
Security
Software Development & Management
Web Development
Web Services
Formats
Books
eBooks
Practice Tests
Software
Video
Web Editions
Deals & Promotions
Video Training
Imprints
Addison-Wesley Professional
Adobe Press
Cisco Press
FT Press
IBM Press
Microsoft Press Store
Oracle Press Books
Peachpit
Pearson IT Certification
Que Publishing
Sams Publishing
Explore
About
Affiliate Program
Authors
Chapters & Articles
Deals & Promotions
Popular Topics
Product Registration
Special Offers & Newsletter
Support
Video Training
Community
Press and Media Relations
Product Review Team
User Groups
About
Affiliates
Cookies
FAQ
Legal Notice
Ordering Information
Pearson+
Privacy
Do Not Sell My Personal Information
Press
Promotions
Support
Write for Us
© 2026 Pearson. All rights reserved, including those for text and data mining and training of artificial intelligence and similar technologies. 
Privacy and cookies
We and our third-party partners use cookies and similar technologies to run the website. Some cookies are strictly necessary. We also use optional cookies to provide a more personalized experience, improve the way our websites work and support our marketing operations. Optional cookies will only be set with your consent. You can manage your cookie preferences through the "Cookie Settings" button. For more information see our Privacy Notice.
Cookie Settings Allow and Continue 
Pearson Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer.
More information
Allow All
Manage Consent Preferences
Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
View Vendor Details
Functional Cookies
[x]
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
View Vendor Details
Performance Cookies
[x]
Performance Cookies
These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.
View Vendor Details
Targeting Cookies
[x]
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
View Vendor Details
Vendors List
Clear [-]
checkbox label label
Apply Cancel
Consent Leg.Interest [-]
checkbox label label [-]
checkbox label label [-]
checkbox label label
Reject All Confirm My Choices
Save to Account Close
