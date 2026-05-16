---
name: What's the difference between permissive and copyleft licenses?
keywords: (placeholder)
metadata:
  url: https://opensource.stackexchange.com/questions/21/whats-the-difference-between-permissive-and-copyleft-licenses
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T23:03:23.186Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
terminology - What's the difference between permissive and copyleft licenses? - Open Source Stack Exchange
By clicking “Sign up”, you agree to our terms of service and acknowledge you have read our privacy policy.
Sign up with Google
OR
Email
Password
Sign up
Already have an account? Log in
Skip to main content
1.
Stack Internal Stack Overflow for Teams is now called Stack Internal. Bring the best of human thought and AI automation together at your work. Try for free Learn more
Stack Internal
Bring the best of human thought and AI automation together at your work. Learn more
Stack Internal
Knowledge at work
Bring the best of human thought and AI automation together at your work.
Explore Stack Internal
Stack Exchange Network
Stack Exchange network consists of 183 Q&A communities including Stack Overflow, the largest, most trusted online community for developers to learn, share their knowledge, and build their careers.
Visit Stack Exchange
Loading…
Tour Start here for a quick overview of the site
Help Center Detailed answers to any questions you might have
Meta Discuss the workings and policies of this site
About Us Learn more about Stack Overflow the company, and our products
current community
Open Source help chat
Open Source Meta
your communities
Sign up or log in to customize your list.
more stack exchange communities
company blog 4. 5. Log in 6. Sign up
Open Source
What's the difference between permissive and copyleft licenses?
Ask Question
Asked 10 years, 10 months ago
Modified 10 years, 4 months ago
Viewed 20k times
This question shows research effort; it is useful and clear
34
This question does not show any research effort; it is unclear or not useful
Save this question. 
Show activity on this post.
I've heard both terms thrown around, but I'm a bit unclear as to how the licenses differ.
How is copyleft different to a permissive license? Is copyleft just the standard for open source licenses?
copyleft
terminology
permissive
Share
Share a link to this question https://opensource.stackexchange.com/q/21
Copy link CC BY-SA 3.0
Short permalink to this question
Improve this question
Follow
Follow this question to receive notifications
edited Dec 22, 2015 at 21:26
Zizouz212
6,770 5 5 gold badges 38 38 silver badges 77 77 bronze badges
asked Jun 23, 2015 at 17:59
Raystafarian
451 1 1 gold badge 5 5 silver badges 9 9 bronze badges
Add a comment |
4 Answers 4
Sorted by: Reset to default
Highest score (default)
Date modified (newest first)
Date created (oldest first)
This answer is useful
30
This answer is not useful
Save this answer.
Loading when this answer was accepted… 
Show activity on this post.
The Free Software Foundation invented the term Copyleft. Here's what they have to say about it:
Copyleft is a general method for making a program or other work free, and requiring all modified and extended versions of the program to be free as well.
The simplest way to make a program free software is to put it in the public domain, uncopyrighted. This allows people to share the program and their improvements, if they are so minded. But it also allows uncooperative people to convert the program into proprietary software. They can make changes, many or few, and distribute the result as a proprietary product. People who receive the program in that modified form do not have the freedom that the original author gave them; the middleman has stripped it away.
So copyleft implies a stronger set of restrictions in the license than the terms "Free software" or "Open Source" imply. Copyleft licenses are both free and open source licenses, but not all licenses that are free software or open source licenses are Copyleft.
Copyleft denotes a type of FOSS license that prevents, through license terms, the "proprietization" of FOSS code. If a license is not Copyleft, but it is FOSS, the user may (depending on the exact terms of the license), be able to release binary-only copies of the software, with limited distribution (e.g. license fees and criminal penalties for those who distribute the binaries without authorization from the developers), and without providing the modified source code.
According to the FSF, the Four Freedoms are:
The freedom to run the program as you wish, for any purpose (freedom 0).
The freedom to study how the program works, and change it so it does your computing as you wish (freedom 1). Access to the source code is a precondition for this.
The freedom to redistribute copies so you can help your neighbor (freedom 2).
The freedom to distribute copies of your modified versions to others (freedom 3). By doing this you can give the whole community a chance to benefit from your changes. Access to the source code is a precondition for this.
A copyleft license ensures that anyone who receives the binary version of the software is entitled to the source version (including any source modifications that went into any binaries they received), and that person, in turn, is also required to pass down the four freedoms to anyone else that they pass said binaries/code on to.
A non-copyleft FOSS license could allow one person to receive the four freedoms as part of obtaining a copy of the code, but then that person can choose whether they want to give the four freedoms (or any individual one of the freedoms) to someone else that they give the software to.
It is important to note that, based on the way the copyleft was defined, a license that requires a recipient of the source or binaries to respect some freedoms, but not all of them, is not a copyleft license. It is only copyleft if each recipient of the software must grant all four freedoms to everyone they give a copy to.
For example, consider these simplistic licenses:
(1) You are given the four freedoms with respect to this software. It's up to you if you want to give others any of the freedoms or not when you distribute it further.
(2) You are given the four freedoms with respect to this software. In addition, if you distribute this software to anyone else, you must grant them Freedom 0 and Freedom 1. It's up to you if you want to give them Freedom 2, and you may not give them Freedom 3.
(3) You are given the four freedoms with respect to this software. In addition, if you distribute this software to anyone else, you must grant them all four Freedoms; otherwise, you violate this license.
The first license is a standard permissive license (similar to the BSD license), and is not copyleft because it does not require all four freedoms to be passed on.
The second license is a weird license (I've never seen one quite like this in practice) that prohibits the passing-on of one freedom; allows (optionally) another; and requires two. But the requiring of the first two isn't enough to make it copyleft. It may be free software for the person receiving a copy initially, but it cannot be free software after that, because freedom 3 is prohibited from that point onwards in the distribution chain.
The third license is a standard, copyleft-compliant license.
It's important to keep in mind that non-copyleft licenses can transform from being free/open source software to non-free, non-open source software licenses, because the enforcement of the preservation of the freedoms is not in place. Consider this distribution chain, where each letter is a person, and "A" is the person who originally wrote the first copy of the software and determined its license.
A -> B -> C -> D -> E
If this is a non-copyleft FOSS license, the only person guaranteed to have all four freedoms is A (well, technically, if he distributed it as FOSS, then B should have gotten all four freedoms, too).
If this is licensed under copyleft, then if every person, all the way down to E, does not have all four freedoms in respect to the software, then someone violated the license terms set forth by A, and is liable for copyright infringement!
Thus, when we talk about non-copyleft FOSS licenses, we have to ask the question, free for whom? -- but in the case of copyleft licensed software, the answer is, free for everyone.
Share
Share a link to this answer https://opensource.stackexchange.com/a/42
Copy link CC BY-SA 3.0
Short permalink to this answer
Improve this answer
Follow
Follow this answer to receive notifications
edited Jun 18, 2020 at 8:31
Community Bot
1
answered Jun 23, 2015 at 18:22
allquixotic
416 3 3 silver badges 5 5 bronze badges
2
There is a common line of thought that the four freedoms are a sufficient condition for free software. However, a license could include these four freedoms along with additional constraints such that one might no longer consider it free. Additionally, freedom 3 becomes an obligation by the addition of "Access to the source code is a precondition for this.", so one can argue that it is not actually a freedom. Because of these issues, it can be a stretch to say that copyleft licensed software is free for everyone. Pixelstix – Pixelstix 2023-06-05 23:02:20 +00:00 Commented Jun 5, 2023 at 23:02
"non-copyleft licenses can transform from being free/open source software to non-free, non-open source software licenses". This is a little deceptive. If someone downloads "WidgetX" off of Github with a permissive open free etc. license that does not require providing source code to others, then creates a software product that uses "WidgetX" and sells that software without the "WidgetX" source, their COPY of "WidgetX" is not free. However, the license for "WidgetX" on Github has not been magically transformed, is still free and available from the original source. Pixelstix – Pixelstix 2023-06-05 23:15:53 +00:00 Commented Jun 5, 2023 at 23:15
Add a comment |
This answer is useful
12
This answer is not useful
Save this answer.
Loading when this answer was accepted… 
Show activity on this post.
Short answer:
Copyleft is a term coined by the FSF and implies that if you distribute a derivative work of a work under a copyleft license, you must distribute the derivative under the same license as the original work (it may however be combined with works under a permissive license that is deemed "compatible", read on). Some people use the pejorative name " viral license" for a copyleft license.
A permissive license is a license that permits re-licensing of derivative works (i.e. the derivative can have a different license than the original, and even be closed source with ARR).
Some comments about the difference:
One important property of a permissive license is that it is sublicensable and GPL compatible. This means that you can legally use a component with a permissive license in a derivative work where the other components are under GPL (or a compatible license such as Apache 2.0) and then the entire work can be made available under the GPL license. This means that you can use a library under the MIT/expat license (permissive) in a project under the GNU GPL (copyleft), and the resulting composite would be GNU GPL (copyleft).
Note that going in the opposite direction (from copyleft to permissive) is not possible. Such a derivative can never be MIT/expat, because that would violate the terms of the GNU GPL.
The FSF has made a handy reference page about what licenses are permissive and allow re-licensing, as well as the chart below specifically for GNU GPL version 3. Note that the direction of flow is always from the permissive licenses to the copyleft licenses, and not the other way.
The dotted arrow from GPLv2 to GPLv3 is for a special version of GPLv2 written "GPLv2 or later" (sometimes abbreviated "GPLv2+"). 
This chart introduces the terms "weak copyleft" and strong copyleft". Briefly, the difference is that "strong copyleft" insists on copyleft for a composite where at least one of the components are copyleft, while "weak copyleft" means that copyleft only apply to derivatives, not sibling components in a composite. "Copyleft" when used without an adjective, usually means "strong copyleft".
Share
Share a link to this answer https://opensource.stackexchange.com/a/1179
Copy link CC BY-SA 3.0
Short permalink to this answer
Improve this answer
Follow
Follow this answer to receive notifications
edited Jul 21, 2015 at 3:26
answered Jul 16, 2015 at 11:58
Free Radical
9,315 3 3 gold badges 32 32 silver badges 63 63 bronze badges
Add a comment |
This answer is useful
7
This answer is not useful
Save this answer.
Loading when this answer was accepted… 
Show activity on this post.
Copyleft emphasises that you can not do everything with the source. The usual example is GPL-style restrictions, which do not allow using the code in a closed-source project  exceptasSAAS . (The “left” is sometimes interpreted as: you have to give your own code back if you want to have the benefits of somebody else's open-source project.)
Permissive licenses do allow this kind of reuse; their main requirement is that of attribution. (But I suppose public-domain / CC0, where not even attribution is necessary, would also be considered permissive.)
Share
Share a link to this answer https://opensource.stackexchange.com/a/25
Copy link CC BY-SA 3.0
Short permalink to this answer
Improve this answer
Follow
Follow this answer to receive notifications
edited Apr 12, 2017 at 7:32
Community Bot
1
answered Jun 23, 2015 at 18:04
leftaroundabout
806 6 6 silver badges 12 12 bronze badges
7
5 "you can not do anything with the source" That is wrong. You can use the code unless you follow the rules and don't deny anybody the four freedoms of Free Software. user114 – user114 2015-06-23 19:27:36 +00:00 Commented Jun 23, 2015 at 19:27
1 @Tichodroma: so, what is wrong then? leftaroundabout – leftaroundabout 2015-06-23 22:32:59 +00:00 Commented Jun 23, 2015 at 22:32
Since you can to what the Copyleft license allows (which is pretty much), you can do something with the source. Your claim that you can't do anything with the source is wrong. user114 – user114 2015-06-24 06:58:21 +00:00 Commented Jun 24, 2015 at 6:58
Oh dear, you could have made it clear that this is a language problem we're talking about... leftaroundabout – leftaroundabout 2015-06-25 18:15:20 +00:00 Commented Jun 25, 2015 at 18:15
"which do not allow using the code in a closed-source project". This is definetively wrong. You can take copyleft code and use it as much as you like in closed source projects, as long as you do not distribute said project to a third party. Closed source in-house and SAAS-use of Copyleft code is allowed. Free Radical – Free Radical 2015-07-24 06:03:48 +00:00 Commented Jul 24, 2015 at 6:03
| Show 2 more comments
This answer is useful
6
This answer is not useful
Save this answer.
Loading when this answer was accepted… 
Show activity on this post.
The other explanations are accurate but here is a simpler version:
Permissive
A permissive license typically lets anyone do anything with the code but cannot sue the author if there are bugs.
Some also require anyone who distributes the code to mention where they got it from.
Copyleft
A copyleft license forces any "derivative" work to also be open source and copyleft.
You cannot use copyleft code in a permiasive licensed project or a closed source project.
You cannot distribute copyleft binaries under any other license. For example Apple's App Store has a single license that all binaries are distributed under and it is not copyleft.
Also there are others but these are the ones most people care about.
The restrictions of a copyleft license do not apply to the cppyright holder, but if they acced third party contributions to the code then the restrictions will apply.
Rivalry
Because copyleft code cannot be used in permissive licensed open source projects there is some tension between people who prefer one type of license over the other.
Share
Share a link to this answer https://opensource.stackexchange.com/a/1351
Copy link CC BY-SA 3.0
Short permalink to this answer
Improve this answer
Follow
Follow this answer to receive notifications
answered Jul 26, 2015 at 21:01
Abhi Beckert
2,924 1 1 gold badge 16 16 silver badges 24 24 bronze badges
2
I don't think the suing the author protection is really the main thing about permissive licenses... in fact such clauses are common for proprietary code too. curiousdannii – curiousdannii 2015-07-27 13:32:00 +00:00 Commented Jul 27, 2015 at 13:32
@curiousdannii protection against liability is the only thing all permissive licenses have. Requiring attribution is the only other clause that many (but not all) permissive licenses have. Abhi Beckert – Abhi Beckert 2015-07-28 00:40:37 +00:00 Commented Jul 28, 2015 at 0:40
Add a comment |
Your Answer
Thanks for contributing an answer to Open Source Stack Exchange!
Please be sure to answer the question. Provide details and share your research!
But avoid …
Asking for help, clarification, or responding to other answers.
Making statements based on opinion; back them up with references or personal experience.
To learn more, see our tips on writing great answers.
Draft saved
Draft discarded
Sign up or log in
Sign up using Google
Sign up using Email and Password
Submit
Post as a guest
Name
Email
Required, but never shown
Post as a guest
Name
Email
Required, but never shown
Post Your Answer Discard
By clicking “Post Your Answer”, you agree to our terms of service and acknowledge you have read our privacy policy.
Start asking to get answers
Find the answer to your question by asking.
Ask question
Explore related questions
copyleft
terminology
permissive
See similar questions with these tags.
Featured on Meta
(Almost) One year of Challenges
Report this ad
Linked
77
Can I license my project with an open-source license but disallow commercial use?
19
GPL-Licensed LaTeX template - implications for resulting work?
18
Does a host application's license apply to plug-ins written for it?
9
Will copyleft help me control what others are able to do with my code?
4
Can I call the Google AI Edge SDK from my Apache2-licensed app?
2
What are the most common open source license options and how do they differ?
1
how do open source licenses affect ecommerce sites?
Related
21
Very permissive license
19
What is copyleft?
9
Why to prefer permissive license over copyleft license?
2
How do Wikipedia licenses, CC-BY-SA and GFDL differ?
1
What are the restrictions in permissive licenses like MIT or Apache 2.0?
4
Copyleft licensed part inside permissive software
2
What's the difference between GPL licence and CECILL-2.1?
6
GPL and Linking Exceptions
2
Dual licensing with copyleft exclusionary licenses like OFL and UFL?
2
Best copyleft (non-permissive/strongly-reciprocal) license for kdenlive files?
Hot Network Questions
Does distributing a GPL program require agreeing to the preamble of the GPL?
Books with multiple proofs of one statement
Two people playing the same PC?
Why does a resistor physical T of 290K make it emit -174 dBm/Hz of noise power, but other circuit elements at 290K don't emit -174dBm/Hz?
Finding the depth of sea very close to shore with a phone
When does a bomb-modifying Alchemist discovery replace bomb damage rather than add to it?
Identification of a certain planetary system?
MSVC don't consider conversion operator when initializing aggregate with parenthesis
Good gzeiras are irreversible, really?
Equilateral triangle packing in square: express length square in terms of angle
Was John the Baptist an Essene and was he a vegetarian?
Is a Familiar (baboon) using Wand of Magic Missile allowed?
Copy the Feature IDs of the selected features to clipboard
Why does this crew member take a photo of Kate Winslet's face and hands during a break in filming?
Tightened shower diverter too much and caused a dent, is this still safe to use?
In Acts 2:2, why would an immaterial "spirit" make the sound of wind blowing?
What is an appropriate role for LLMs in early mathematical research training?
One Thought per Sentence
Why is it likelihood and not likelyhood?
I feel guilt and anxiety for having used AI in my writing and cannot enjoy it as my own work
Multiple entry Schengen Type C visa with two separate trips — confusion
Commutator of the BRST operator with the ghost number operator
How can I present a highly interdisciplinary PhD talk in 15 minutes / 30 minutes?
How to turn "Alt+l+e+up-key+enter" combination into a shortcut?
Question feed
Subscribe to RSS
Question feed
To subscribe to this RSS feed, copy and paste this URL into your RSS reader. https://opensource.stackexchange.com/feeds/question/21 
Why are you flagging this comment?
[-] 20
It contains harassment, bigotry or abuse.
This comment attacks a person or group. Learn more in our Abusive behavior policy. [-] 40
It's unfriendly or unkind.
This comment is rude or condescending. Learn more in our Code of Conduct. [-] 39
Not needed.
This comment is not relevant to the post.
Enter at least 6 characters [-] 19
Something else.
A problem not listed above. Try to be as specific as possible.
Enter at least 6 characters
Flag comment Cancel
You have 0 flags left today
Hang on, you can't upvote just yet.
You'll need to complete a few actions and gain 15 reputation points before being able to upvote. Upvoting indicates when questions and answers are useful. What's reputation and how do I get it?
Instead, you can save this post to reference later.
Save this post for later Not now
Open Source
Tour
Help
Chat
Contact
Feedback
Company
Stack Overflow
Stack Internal
Stack Data Licensing
Stack Ads
About
Press
Legal
Privacy Policy
Terms of Service
Your Privacy Choices
Cookie Policy
Stack Exchange Network
Technology
Culture & recreation
Life & arts
Science
Professional
Business
API
Data
Blog
Facebook
Twitter
LinkedIn
Instagram
Site design / logo © 2026 Stack Exchange Inc; user contributions licensed under CC BY-SA . rev 2026.5.13.43074
By continuing to use this website, you agree Stack Exchange can store cookies on your device and disclose information in accordance with our Cookie Policy. By exiting this window, default cookies will be accepted. To reject cookies, select an option from below.
Necessary cookies only
Customize settings 
Cookie Consent Preference Center
When you visit any of our websites, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences, or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and manage your preferences. Please note, blocking some types of cookies may impact your experience of the site and the services we are able to offer.
Cookie Policy
Accept all cookies
Manage Consent Preferences
Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
Targeting Cookies
[x]
Targeting Cookies
These cookies are used to make advertising messages more relevant to you and may be set through our site by us or by our advertising partners. They may be used to build a profile of your interests and show you relevant advertising on our site or on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device.
Performance Cookies
[x]
Performance Cookies
These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.
Functional Cookies
[x]
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
Cookie List
Clear
[-] checkbox label label
Apply Cancel
Consent Leg.Interest [-]
checkbox label label [-]
checkbox label label [-]
checkbox label label
Necessary cookies only Confirm My Choices
Report this ad 
