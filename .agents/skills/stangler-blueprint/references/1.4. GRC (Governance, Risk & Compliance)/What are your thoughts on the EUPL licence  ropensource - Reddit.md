---
name: What are your thoughts on the EUPL licence? : r/opensource - Reddit
keywords: (placeholder)
metadata:
  url: https://www.reddit.com/r/opensource/comments/1eht9p0/what_are_your_thoughts_on_the_eupl_licence/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T23:03:23.186Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
What are your thoughts on the EUPL licence? : r/opensource
Skip to main content What are your thoughts on the EUPL licence? : r/opensource
Open menu
Open navigation 
Go to Reddit Home 
r/opensource
Sign Up
Sign up for Reddit
Log In
Log in to Reddit
Expand user menu
Open settings menu
Skip to Navigation Skip to Right Sidebar
Back
Go to opensource
r/opensource
•
2y ago
dani1025
Locked post
Stickied post
Archived post
Report
What are your thoughts on the EUPL licence?
Discussion
While trying to pick a licence for my project I came across the EUPL licence. I've never heard of it and I found it interesting that the EU had its own OSS licence.
What I like about it:
Quite explicit.
SaaS is considered distribution
The source code for distributions has to be made public
Available in multiple languages
Copyleft
Heve you used it in one (or more) of your projects?
What drawbacks do you see, why have you decided against using it?
Upvote 41 Downvote 25 Go to comments Share
Sort by: Best
Open comment sort options
Best
Top
New
Controversial
Old
Q&A
Search Comments Expand comment search
Cancel
Comments Section
PurpleYoshiEgg
•
2y ago
I have not used it, having just learned about it today.
The primary advantage it has over the AGPLv3 is that it is provided in 23 languages, and each language version is considered an official language version:
The EUPL is the sole really multilingual open source licence, where all 23 versions are original and have equal value;
Contrast with the AGPL translations:
The FSF does not approve license translations as officially valid. The reason is that checking them would be difficult and expensive (needing the help of bilingual lawyers in other countries). Even worse, if an error did slip through, the results could be disastrous for the whole free software community. As long as the translations are unofficial, they can't do any legal harm.
I think this is great, because that means you don't have to read at an English level that is formal, legal-focused, and US-centric, but one of the 23 languages provided as an official translation. Additionally, I'd presume it also opens up legal access to lawyers in the EU who can help convey understanding to a language the license hasn't been translated to. It's currently missing 1 official EU language (Irish), so there's a ton of potential for expanding open source internationally.
I either couldn't find or possibly didn't understand any specific technical differences between the AGPLv3 and EUPL 1.2, but I do believe there might be a couple of small differences.
As far as I'm aware, the AGPL hasn't been tested in court, but I do like that the EUPL has been made by a government entity rather than a private nonprofit, so at least in the EU, it should hold up very well in courts covered by the EU.
Upvote 14 Downvote Reply Award Share
Report
Award
Share
NatoBoram
•
2y ago
What's the difference with AGPLv3?
Upvote 11 Downvote Reply Award Share
Report
Award
Share 
Traditional_Wafer_20
•
2y ago
Probably "common law" vs "civil law" problem. AGPL has never been tested in court, but court decisions are central in common law systems. so we don't know how it would really go. EU is civil law-centric, so the license is kind of already approved by the government, result in court is pretty already known. In the end it's probably exactly the same, it's just that the philosophy of justice is different between Europe and US so they had to publish something official for their own use.
Upvote 8 Downvote Reply Award Share
Report
Award
Share
ssddanbrown
•
2y ago 
Top 1% Poster
Never used it but like that it's easier to read/understand than GPL licenses IMO. I'm not a fan of the advisory to target the current/latest version or later, since that somewhat gives licensing control to an external entity, but I guess you don't have to follow that.
The source code for distributions has to be made public
What part of the licence text enforces this out of interest? I don't think I've seen such a requirement in an open source license and I would wonder if it interferes with free rights of distribution somewhat.
Upvote 5 Downvote Reply Award Share
Report
Award
Share
dani1025
OP
• 2y ago
The source code for distributions has to be made public
That is how I interpreted this part.
Communication of the Source Code
The Licensor may provide the Work either in its Source Code form, or as Executable Code. If the Work is provided as Executable Code, the Licensor provides in addition a machine-readable copy of the Source Code of the Work along with each copy of the Work that the Licensor distributes or indicates, in a notice following the copyright notice attached to the Work, a repository where the Source Code is easily and freely accessible for as long as the Licensor continues to distribute or communicate the Work.
Upvote 1 Downvote Reply Award Share
Report
Award
Share
More replies
The-Malix
•
2y ago
• Edited 2y ago
It is very close to AGPL
In theory :
EUPL requires "compatible licensing"
AGPL requires "same licensing"
In Practice :
"compatible licensing" is enough compared to "same licensing"
Hence,
EUPL is explicitly compatible with AGPL
AGPL is implicitly compatible with EUPL
Upvote 4 Downvote Reply Award Share
Report
Award
Share
The-Malix
•
2y ago
The replier blocked me, I cannot see any of their previous or future comments anymore
Upvote 1 Downvote Reply Award Share
Report
Award
Share
Qwert-4
•
2y ago
https://joinup.ec.europa.eu/collection/eupl/matrix-eupl-compatible-open-source-licences
Upvote 1 Downvote Reply Award Share
Report
Award
Share
More replies 
passiveobserver012
•
10mo ago
It is a weak copyleft license.
It is OK with static linking and incorporation of the code in contrast to GPLv3 for example.
source: https://interoperable-europe.ec.europa.eu/collection/eupl/matrix-eupl-compatible-open-source-licences
This makes it more accessible for businesses.
I just put it here since this seems to confuse people (Google for example: https://opensource.google/documentation/reference/thirdparty/licenses#european_union_public_licence_eupl_not_allowed ).
Upvote 1 Downvote Reply Award Share
Report
Award
Share
AtjonTV
•
4mo ago
For anyone who stumbles upon this thread, and thinks that they can "relicense" EUPL code into GPL (or any other Compatible License), here is some important information.
The EUPL does NOT allow you to "relicense" (aka changing the license of the code without being the owner of said code). It DOES allow you to distribute a combined work under a different license.
In the official EUPL FAQ ( https://interoperable-europe.ec.europa.eu/collection/eupl/faqs) under Is the use of a compatible licence a "re-licensing"? it reads:
The original code will stay covered by the EUPL. It is the combined work only that could be, when needed, covered by the compatible licence. In this framework, a combined work results from merging functional codes covered by two (or more) different licenses. The simple action of "linking" does not merge functional codes and in such case the various linked parts will keep their primary licences. [...]
To be legitimate, the use of the compatibility clause must result from necessity: using it for the sole purpose of relicensing a copy of the original work would be a copyright infringement.
So in effect:
When you have a EUPL licensed application and add a GPLv3-only licensed component to it, you CAN redistribute the whole (EUPL+GPL-3) under the GPL. BUT, all of the EUPL code stays EUPL. So as soon as a user comes to know that parts of the GPL product are EUPL licensed, they have the right to get that code under the EUPL.
My opinion on how it works:
What I also think is that the network-use-is-distribution part of the EUPL stays in effect as the licenses says that only those parts of the compatible license that conflict, override the EUPL:
Should the Licensee's obligations under the Compatible Licence conflict with his/her obligations under this Licence, the obligations of the Compatible Licence shall prevail.
So unless any of the compatible licenses force upon you that network-use is NOT distribution and that you MUST NOT publish the code, you MUST do so under the EUPL for all of the EUPL parts (not the GPL parts, as the GPL does not have such a network-use clause).
Upvote 2 Downvote Reply Award Share
Report
Award
Share
RepulsiveRaisin7
•
2y ago
EUPL allows relicensing to a bunch of other licenses, which means it has rather weak copyleft. I think you're better off with a license that matches your intention, either (A)GPL for strong copyleft or MPL for mild copyleft.
Upvote 1 Downvote Reply Award Share
Report
Award
Share
The-Malix
•
2y ago
EUPL allows relicensing to a bunch of other licenses
Can you quote the part about that ?
As far as I'm aware, licenses cannot change how you are allowed of "relicensing"as in "changing a licence"
In my opinion, EUPL is virtually the same as AGPL
Upvote 6 Downvote Reply Award Share
Report
Award
Share
More replies
New to Reddit?
Create your account and connect with a world of communities.
Continue with Email
Continue with Phone Number
By continuing, you agree to our User Agreement and acknowledge that you understand the Privacy Policy.
Related Answers Section
Related Answers
Thoughts on the EUPL license in open source
Top open source projects to watch in 2024
Best open source tools for developers
How to start contributing to open source
Most impactful open source licenses explained
I found out that Europe has its own software license (EUPL). For developers, please check it out! It's copy-left (like GPL) but it's available in many more languages and is designed to be compatible with the legal frameworks of all EU member states. r/europe • 8mo ago [
I found out that Europe has its own software license (EUPL). For developers, please check it out! It's copy-left (like GPL) but it's available in many more languages and is designed to be compatible with the legal frameworks of all EU member states.
](https://www.reddit.com/r/europe/comments/1nhtwkz/i_found_out_that_europe_has_its_own_software/) 130 upvotes · 13 comments
What is your opinion on the European Union Public License? r/opensource • 4y ago [
What is your opinion on the European Union Public License?
](https://www.reddit.com/r/opensource/comments/sgdjzg/what_is_your_opinion_on_the_european_union_public/) 18 upvotes · 8 comments
This is where me being a software developer all started r/zxspectrum • 2mo ago [
This is where me being a software developer all started
](https://www.reddit.com/r/zxspectrum/comments/1ro29w7/this_is_where_me_being_a_software_developer_all/)  598 upvotes · 66 comments
Jurgened! r/postcrossing • 21d ago [
Jurgened!
](https://www.reddit.com/r/postcrossing/comments/1styh0k/jurgened/)  103 upvotes · 9 comments
What are your thoughts on PWAs? r/ios • 2y ago [
What are your thoughts on PWAs?
](https://www.reddit.com/r/ios/comments/1dpz14m/what_are_your_thoughts_on_pwas/) 1 upvote · 1 comment
Concept... r/LandscapeArchitecture • 9mo ago [
Concept...
](https://www.reddit.com/r/LandscapeArchitecture/comments/1n3qd4v/concept/)  823 upvotes · 57 comments
Landscape r/LandscapeArchitecture • 1mo ago [
Landscape
](https://www.reddit.com/r/LandscapeArchitecture/comments/1sjk7z5/landscape/)  9 44 upvotes · 18 comments
What are your thoughts on wp-env? r/ProWordPress • 2y ago [
What are your thoughts on wp-env?
](https://www.reddit.com/r/ProWordPress/comments/1ec12rn/what_are_your_thoughts_on_wpenv/) 7 upvotes · 12 comments
Légendes r/MemeFrancais • 27d ago [
Légendes
](https://www.reddit.com/r/MemeFrancais/comments/1snx7qc/l%C3%A9gendes/)  203 upvotes · 6 comments
what are you're thoughts on Measured Irrigation ? r/Irrigation • 2y ago [
what are you're thoughts on Measured Irrigation ?
](https://www.reddit.com/r/Irrigation/comments/1dii3lt/what_are_youre_thoughts_on_measured_irrigation/) 1 upvote
What are your thoughts on tge european continent? r/climatechange • 2y ago [
What are your thoughts on tge european continent?
](https://www.reddit.com/r/climatechange/comments/1dqmkyz/what_are_your_thoughts_on_tge_european_continent/) 3 upvotes · 11 comments
What are your thoughts on TOP ( The Odin project) ? r/developersIndia • 2y ago [
What are your thoughts on TOP ( The Odin project) ?
](https://www.reddit.com/r/developersIndia/comments/1dot96w/what_are_your_thoughts_on_top_the_odin_project/) 3 upvotes
What's your opinion on the current draft of right to development treaty ? r/GlobalTribe • 2y ago [
What's your opinion on the current draft of right to development treaty ?
](https://www.reddit.com/r/GlobalTribe/comments/1d9n365/whats_your_opinion_on_the_current_draft_of_right/) 6 upvotes · 1 comment
What do you think about Ceefax? r/AskUK • 2y ago [
What do you think about Ceefax?
](https://www.reddit.com/r/AskUK/comments/1e08wts/what_do_you_think_about_ceefax/) 16 upvotes · 46 comments
View Post in
Português (Brasil)
日本語
繁體中文
简体中文
Français
Русский
See more See fewer
한국어
Dansk
Українська
Español (Latinoamérica)
Deutsch
Ελληνικά
Türkçe
Community Info Section
r/opensource
Join
Open Source on Reddit
A subreddit for everything open source related (for this context, we go off the definition of open source here http://en.wikipedia.org/wiki/Open_source)
Show more
Public
Anyone can view, post, and comment to this community
Top Posts
Reddit reReddit: Top posts of August 1, 2024
Reddit reReddit: Top posts of August 2024
Reddit reReddit: Top posts of 2024
Reddit Rules Privacy Policy User Agreement Your Privacy Choices Accessibility Reddit, Inc. © 2026. All rights reserved.
Expand Navigation
Expand Navigation
Collapse Navigation
Collapse Navigation 
0cAFcWeA46lF6pejC9oWe6EtsorlMfQ_hYohrg7mhoAtnYBwtwVSzwn3-x6tLXcPD7VhdLEPGurMR10Rr136ci9A05BCBc08-yXerWOdkBhov1Y4TQtrTFd0ddhmn16XF-bB3Y8yTDluDnN4OIlnleldr0GE56bY9xSXzHvTWBwQ-rhpIBK0N8l-q6U3MVqzJCDu5BI8EnlUh7U0hSlxeroAFolhTvURnoglRsBYwuuk-zrUJv31VDtcbCu6X9vd3eqfv1K7mrYZJ5LtkixnQ6BdaxynXlNrVvz47PFij1Y6veZynhHN1IU4-tfH5KgAPgK-aItqQxxmuolYZcp9anvYKYVSJJ0ekmipdcRvepS0qUNrRakpuoTPVTkZ5dYdj1novWH2ku5X0ISeKtr1J8S1WhkBgteaJ5sThGrftA_KPAkb1GFGGhM5PFnJy1TzVaq2LsXBbIoYQzYp3fLX_9fy1fWGs-4EAu1DmAAgNJTrtjWi-soifiwLBNZZyQ37OjU8kV83fwMGS0eVuDQp4pkMlQNIOXerUmpCF4_Fs3cGJ3Q6TgbogwkzO5P6rrAF6wgruXwaZnp66xr930wcjkHM6JqCpkbGHpvdXm4Wtt-HP0ZciRRlz8UfvSmGv-LaKyZT-IsYE2jcI31znZbzdEuRGpHnBbD_F9UjuPR3EGRZYzJ5VRwvdDiPUiiq3Ghpl0Cprp6mUVyEco9mdoXEtqioBNdPliNWqY45WdoPU5uUbkoYynuPOKgKzMAvBpLhEk8x-FtVi6-HVyDhwYM4qfdl-yro60SmZzq2J-EkaE8B4pFuKflAYQuUf5rzoQpY6EIU-MAav2WwWDel81bHCphusco5s_zJLbUprs5hG_KQQ1ghwefoBYnMOo0A-zUkq4GFkt9BFw1_fRkDhRwW3TN-qj04njsOF6idJA5Zy2NxFkoGn9zSf8AIfS9VgmBNU9XIZj7JmSUq2TQDVASjvkr-MXeZIf42MVxvZkDikeP5zQNr1uMGFDG47mhxw6mfLG-i-s6lO_nhg359o4ZBaRrhajQqd0-vhRXKYgCcUgrsp6xdc_Sz5Y1hgcbFTOS_rcJ0McGQFCbsfJmDAQ5znMmdHPLpSym4Rj6sPSqkdYEZvnLHaisT5z6_lnWV7maBxIh6NH0wXyXADJfSzi6xb7qyXAqi52f2OnwA6PE5p4JwOm_0PqkVHJuP_my_ge5YYQYoSXGWiAh1DpdeFocZlYzrwAp4URYExbRdBpuy10aNGheesg4E2UzXMJGo6putSO8oKJd-DkyhtJOXbgScQSeBi5h-aRb8d7l3YxSNG-iR3F_5imCyhcwmzXQamVpxzH1lMgo30tk4nGxyNtmXUMkDlY4P5znkwLT_NxBqJyVURq9VD9_zwPX19d3LSeLdQ7dVfonulh09n02kt_bIVVOsQ43fvYcjIIDmwtGDaKcm1n5lSxjg6fXOVc79A3R3dhQZnktKK29OnmT8VUJYh0OoOL-G096hCq4eDJPHHIlOnlOPtdBHVnIi7MY0YLHdXoN51YCUGzgb3GpHPd6kaOvZ8_INR0al-OmNqVBb5UuFxo6B-SusrWAGl9dj_Fmsg8qPiEC-nFYBxkRrd_LVUCU5Kmt5LopzIckapyANraMHLcy5qwbjtKy5LYgP97hkY2g6IA2aCmaNdXJC9ISqDHpjhNFN7Yyo1Rvs2v4UZ1aYuWpmsXJIRmkB5uJV0p6--FoJcy9SamG-Nhsv5KfS3yjeoSWqUHzbr2GnNt5IofZpSQ0YtTBVaqM8lilH-vMCFDsE9cIz6WrjPNDfUH7N8RmPbKK8rueVRkTkhZte_PuA8-uFtC5iBpFhL5b1SRWrZyADyyKHy5CWwa56SOVD3QzZx6GZwU5u3OXjkCfBLckHvEhxpZ4cQaKp1sky5bkH5mL8otsat3cCp_RPKLQYbDwAWekiW0EANe0Bq97xOc3hdNoopZsuDSe6nF1OSyjw51bjuD_1zmQYqZIgpHEhxbLC9O0yjhymn3Pir05uODDNL5EPOiZWSdzPWyaIi45q1Pp46dblAx0z7DJZEi6KWXLZo4ZrwUiNdehmlNO6d9-GqreCvF8SVNj3eg2lR7Prb2TdrU_NsCkBpwDKlZuN8bjt7lhwZv-s8g
