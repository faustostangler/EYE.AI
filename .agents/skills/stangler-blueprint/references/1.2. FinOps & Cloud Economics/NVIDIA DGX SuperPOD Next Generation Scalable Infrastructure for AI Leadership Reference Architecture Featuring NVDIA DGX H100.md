---
name: NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX H100
keywords: (placeholder)
metadata:
  url: https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-h100/latest/dgx-superpod-architecture.html
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
DGX SuperPOD Architecture — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX H100
Skip to main content 
Back to top Ctrl + K
 NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX H100
Search Ctrl + K
Search Ctrl + K
 NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX H100
Table of Contents
Reference Architecture
Abstract
Key Components of the DGX SuperPOD
DGX SuperPOD Architecture
Network Fabrics
Storage Architecture
DGX SuperPOD Software
Summary
Major Components
Notices
Notices
DGX SuperPOD Architecture
Is this page helpful?
DGX SuperPOD Architecture#
The DGX SuperPOD architecture is a combination of DGX systems, InfiniBand and Ethernet networking, management nodes, and storage. Figure 2 shows the rack layout of a single SU. In this example, power consumption per rack exceeds 40 kW. The rack layout can be adjusted to meet local data center requirements, such as maximum power per rack and rack layout between DGX systems and supporting equipment to meet local needs for power and cooling distribution.
Figure 2. Complete single SU rack layout 
Figure 3 shows an example management rack configuration with networking switches, management servers, storage arrays, and UFM appliances. Sizes and quantities will vary depending upon models used.
Figure 3. Management rack configuration 
This reference architecture is focused on 4 SU units with 128 DGX nodes. DGX SuperPOD can scale to much larger configurations up to and beyond 64 SU with 2000+ DGX H100 nodes. See Table 3 for more information.
Table 3 Larger SuperPOD component counts#
| SU Count | Node Count | GPU Count | InfiniBand Switch Counts ||| Cable Counts ||| | ^^ | ^^ | ^^ | Leaf | Spine | Core | Node-Leaf | Leaf-Spine | Spine-Core | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 4 | 128 | 1024 | 32 | 16 | – | 1024 | 1024 | 1024 | | 8 | 256 | 2048 | 64 | 32 | – | 2048 | 2048 | 2048 | | 16 | 512 | 4096 | 128 | 128 | 64 | 4096 | 4096 | 4096 | | 32 | 1024 | 8192 | 256 | 256 | 128 | 8192 | 8192 | 8192 | | 56 | 2048 | 16384 | 512 | 512 | 256 | 16384 | 16384 | 16384 |
Contact NVIDIA for more information regarding DGX SuperPOD solutions beyond four scalable units.
previous Key Components of the DGX SuperPOD
next Network Fabrics
Privacy Policy | Your Privacy Choices | Terms of Service | Accessibility | Corporate Policies | Product Security | Contact
Copyright © 2024-2025, NVIDIA Corporation.
Last updated on Nov 19, 2025.
NVIDIA uses cookies to improve your experience on our web site. We and our third-party partners also use cookies and other tools to collect and record information you provide as well as information about your interactions with our websites for performance improvement, analytics, and to assist in marketing efforts. By continuing to use this site or by clicking one of the buttons below, you agree to the use of cookies and other tools as described in our Privacy Policy and Cookie Policy (subject to your settings) and accept our Terms of Service (which contains important waivers). Please see our Privacy Policy for more information on our privacy practices.
We have detected the Global Privacy Control (GPC) signal and have opted you out of all optional cookies on this site for this browser. You can manage your cookie settings by clicking on "Manage Settings". Please see our Cookie Policy for more information. To opt out of non-cookie personal information "sales" / "sharing" for targeted advertising purposes, please visit the NVIDIA Preference Center. Please see our Privacy Policy for more information on our privacy practices.
We have detected the Global Privacy Control Signal (GPC) and have opted you out of all optional cookies on this browser. You can manage your cookie settings by clicking on "Manage Settings". Please see our Cookie Policy for more information. We have also opted you out of "sharing"/"sales" of personal information outside of cookies. You can manage these settings in the NVIDIA NVIDIA Preference Center. Please see our Privacy Policy for more information.
We have detected the Global Privacy Control Signal (GPC) and have opted you out of all optional cookies on this browser. You can manage your cookie settings by clicking on "Manage Settings". Please see our Cookie Policy for more information. We have also opted you out of "sharing"/"sales" of personal information outside of cookies which overrides at least one of your previous settings. You can manage them in the NVIDIA Preference Center. Please see our Privacy Policy for more information.
Manage Settings
Turn Off Optional Cookies Agree 
Cookie Settings
We and our third-party partners (including social media, advertising, and analytics partners) use cookies and other tracking technologies to collect, store, monitor, and process certain information about you when you visit our website. The information collected might relate to you, your preferences, or your device. We use that information to make the site work, analyze performance and traffic on our website, provide a more personalized web experience, and assist in our marketing efforts.
Under certain privacy laws, you have the right to direct us not to "sell" or "share" your personal information for targeted advertising. To opt-out of the "sale" and "sharing" of personal information through cookies, you must opt-out of optional cookies using the toggles below. To opt out of the "sale" and "sharing" of data collected by other means (e.g., online forms) you must also update your data sharing preferences through the NVIDIA Preference Center.
Click on the different category headings below to find out more and change the settings according to your preference. You cannot opt out of Required Cookies as they are deployed to ensure the proper functioning of our website (such as prompting the cookie banner and remembering your settings, etc.). By clicking "Save and Accept" or "Decline All" at the bottom, you consent to the use of cookies and other tools as described in our Cookie Policy in accordance with your settings and accept our Terms of Service (which contains important waivers). For more information about our privacy practices, please see our Privacy Policy.
Required Cookies
Always Active
These cookies enable core functionality such as security, network management, and accessibility. These cookies are required for the site to function and cannot be turned off.
Cookies Details
Performance Cookies [-]
Performance Cookies
These cookies are used to provide quantitative measures of our website visitors, such as the number of times you visit, time on page, your mouse movements, scrolling, clicks and keystroke activity on the websites; other browsing, search, or product research behavior; and what brought you to our site. These cookies may store a unique ID so that our system will remember you when you return. Information collected with these cookies is used to measure and find ways to improve website performance.
Cookies Details
Personalization Cookies [-]
Personalization Cookies
These cookies collect data about how you have interacted with our website to help us improve your web experience, such as which pages you have visited. These cookies may store a unique ID so that our system will remember you when you return. They may be set by us or by third party providers whose services we have added to our pages. These cookies enable us to provide enhanced website functionality and personalization as well as make the marketing messages we send to you more relevant to your interests. If you do not allow these cookies, then some or all of these services may not function properly.
Cookies Details
Advertising Cookies [-]
Advertising Cookies
These cookies record your visit to our websites, the pages you have visited and the links you have followed to influence the advertisements that you see on other websites. These cookies and the information they collect may be managed by other companies, including our advertising partners, and may be used to build a profile of your interests and show you relevant advertising on other sites. We and our advertising partners will use this information to make our websites and the advertising displayed on it, more relevant to your interests.
Cookies Details
Cookie List
Clear
[-] checkbox label label
Apply Cancel
Consent Leg.Interest [-]
checkbox label label [-]
checkbox label label [-]
checkbox label label
Decline All Save and Accept
   
