---
name: Open-source license - Wikipedia
keywords: (placeholder)
metadata:
  url: https://en.wikipedia.org/wiki/Open-source_license
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T23:03:23.186Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
Open-source license - Wikipedia
Jump to content [-]
Main menu
Main menu
move to sidebar hide
Navigation
Main page
Contents
Current events
Random article
About Wikipedia
Contact us
Contribute
Help
Learn to edit
Community portal
Recent changes
Upload file
Special pages
Search
Search [-]
Appearance
Donate
Create account
Log in [-]
Personal tools
Donate
Create account
Log in
Contents
move to sidebar hide
(Top)
1 Background
2 Types Toggle Types subsection
2.1 Permissive
2.2 Copyleft
2.3 Compatibility
3 Enforcement
4 Public-domain software
5 Use in proprietary software
6 See also
7 Notes
8 References [-]
Toggle the table of contents
Open-source license
[-]
15 languages
العربية
বাংলা
Català
Čeština
Español
فارسی
Magyar
Italiano
日本語
한국어
Português
ไทย
Українська
Tiếng Việt
中文
Edit links
Article
Talk [-]
English
Read
Edit
View history [-]
Tools
Tools
move to sidebar hide
Actions
Read
Edit
View history
General
What links here
Related changes
Upload file
Permanent link
Page information
Cite this page
Get shortened URL
Expand all
Edit interlanguage links
Print/export
Download as PDF
Printable version
In other projects
Wikidata item
Appearance
move to sidebar hide
Text
[-] 0 Small [x] 1 Standard [-] 2 Large
This page always uses small font size
Width
[x] 1 Standard [-] 0 Wide
The content is as wide as possible for your browser window.
Color
[-] os Automatic [x] day Light [-] night Dark
This page is always in light mode.
From Wikipedia, the free encyclopedia
Software license allowing source code to be used, modified, and shared
Popular open source licenses include the Apache License, the MIT License, the GNU General Public License (GPL), the BSD Licenses, the GNU Lesser General Public License (LGPL) and the Mozilla Public License (MPL).
Open-source licenses are software licenses that allow content to be used, modified, and shared. They facilitate free and open-source software (FOSS) development. Intellectual property (IP) laws restrict the modification and sharing of creative works. Free and open-source licenses use these existing legal structures for an inverse purpose. They grant the recipient the rights to use the software, examine the source code, modify it, and distribute the modifications. These criteria are outlined in The Open Source Definition (OSD).
After 1980, the United States began to treat software as a literary work covered by copyright law. Richard Stallman founded the free software movement in response to the rise of proprietary software. The term "open source" was used by the Open Source Initiative (OSI), founded by free-software developers Bruce Perens and Eric S. Raymond. "Open source" emphasizes the strengths of the open development model rather than software freedoms. While the goals behind the terms are different, open-source licenses and free-software licenses describe the same type of licenses. [1]
The two main categories of open-source licenses are permissive and copyleft. Both grant permission to change and distribute software. Typically, they require attribution and disclaim liability. Permissive licenses come from academia. Copyleft licenses come from the free software movement. Copyleft licenses require derivative works to be distributed with the source code and under a similar license. Since the mid-2000s, courts in multiple countries have upheld the terms of both types of license. Software developers have filed cases as copyright infringement and as breaches of contract.
Background
[ edit]
Main article: History of free and open-source software  
Legal scholar Eben Moglen on the history of copyright
Intellectual property (IP) is a legal category that treats creative output as property, comparable to private property. [2] Legal systems grant the owner of an IP the right to restrict access in many ways. [3] Owners can sell, lease, gift, or license their properties. [4] Multiple types of IP law cover software including trademarks, patents, and copyrights. [4]
Most countries, including the United States (US), have created copyright laws in line with the Berne Convention with slight variations. [5] These laws assign a copyright whenever a work is released in any fixed format. [6] Under US copyright law, the initial release is considered an original work. [7] The creator, or their employer, holds the copyright to this original work and therefore has the exclusive right to make copies, release modified versions, distribute copies, perform publicly, or display the work publicly. Modified versions of the original work are derivative works. [8] When a creator modifies an existing work, they hold the copyright to their modifications. [9] Unless the original work was in the public domain, a derivative work can only be distributed with the permission of every copyright holder. [10]
In 1980, the US government amended the law to treat software as a literary work. Software released after this point was restricted by IP laws. [11] At that time, American activist and programmer Richard Stallman was working as a graduate student at the MIT Computer Science and Artificial Intelligence Laboratory. Stallman witnessed fragmentation among software developers. He blamed the spread of proprietary software and closed models of development. To push back against these trends, Stallman founded the free software movement. [12] Throughout the 1980s, he started the GNU Project to create a free operating system, wrote essays on freedom, founded the Free Software Foundation (FSF), and wrote several free-software licenses. [13] The FSF used existing intellectual property laws for the opposite of their intended goal of restriction. Instead of imposing restrictions, free software explicitly provided freedoms to the recipient. [14]
Bruce Perens, author of the Open Source Definition
In the 90s, the term "open source" was coined as an alternative label for free software, and specific criteria were laid out to determine which licenses covered free and open-source software. [15] [16] Two active members of the free-software community, Bruce Perens and Eric S. Raymond, founded the Open Source Initiative (OSI). [17] At Debian, Perens had proposed the Debian Free Software Guidelines (DFSG). [18] The DFSG were drafted to provide a more specific and objective standard for the FOSS that Debian would host in their repositories. [19] The OSI adopted the DSFG and used them as the basis for their Open Source Definition. [20] The Free Software Foundation maintains a rival set of criteria, the Free Software Definition. [21] Historically, these three organizations and their sets of criteria have been the notable authorities in determining whether a license covers free and open-source software. [22] There is significant diversity among individual licenses but little difference between the rival definitions. [16] The three definitions each require that people receiving covered software must be able to use, modify, and redistribute the covered work. [23]
Eric S. Raymond was a proponent of the term " open source" over "free software". He viewed open source as more appealing to businesses and more reflective of the tangible advantages of FOSS development. One of Raymond's goals was to expand the existing hacker community to include large commercial developers. [24] In The Cathedral and the Bazaar, Raymond compared open-source development to the bazaar, an open-air public market. [25] He argued that aside from ethics, the open model provided advantages that proprietary software could not replicate. [26] [27] Raymond focused heavily on feedback, testing, and bug reports. [28] He contrasted the proprietary model where small pools of secretive workers carried out this work with the development of Linux where the pool of testers included potentially the entire world. [29] He summarized this strength as "Given enough eyeballs, all bugs are shallow." [30] The OSI succeeded in bringing open-source development to corporate developers including Sun Microsystems, IBM, Netscape, Mozilla, Apache, Apple Inc., Microsoft, and Nokia. These companies released code under existing licenses and drafted their own to be approved by the OSI. [31] [32]
Types
[ edit]
See also: Comparison of free and open-source software licenses
Open-source licenses are categorized as copyleft or permissive. [33] Copyleft licenses require derivative works to include source code under a similar license. Permissive licenses do not, and therefore the code can be used within proprietary software. Copyleft can be further divided into strong and weak depending on whether they define derivative works broadly or narrowly. [34] [35]
Licenses focus on copyright law, but code is also covered by other forms of IP. [36] Major open-source licenses written since the late 1990s contain patent grants. These open-source patent grants cover the patents held by the developers. [37] Software patents cover ideas and, rather than a specific implementation, cover any implementation of a claim. Patent claims give the holder the right to exclude others from making, using, selling, or importing products based on the idea. Because patents grant the right to exclude rather than the right to create, it is possible to have a patent on an idea but still be unable to legally implement it if the invention relies on another patented idea. Thus, open-source patent grants can offer permission only from covered patents. They cannot guarantee that a third party has not patented any concepts embodied in the code. [36] The older permissive licenses do not discuss patents directly and offer only implicit patent grants in their offers to use or sell covered material. [38] Newer copyleft licenses and the 2004 Apache License offer explicit patent grants and limited protection from patent litigation. [39] These patent retaliation clauses protect developers by terminating grants for any party who initiates a patent lawsuit regarding covered software. [39]
Trademarks are the only form of IP not shared by free and open-source software. Trademarks on FOSS function the same as any other trademark. [40] A trademark is a design that identifies the distinct source of a product. Because they distinguish products, the same designs can be used in different fields where there is no risk of confusing similar sources. [41] To give up control of a trademark would result in the loss of that trademark. Therefore, no open-source license freely offers the use of a trademark. [42]
Trademark restrictions can overlap copyrights and affect material otherwise freely available. [43] The US Supreme Court described using trademark law to restrict public domain content as "mutant copyright". [44] In Dastar Corp. v. Twentieth Century Fox Film Corp., the court "caution[ed] against misuse or over-extension of trademark" law without providing a firm decision on those mutant copyrights. [45] [46] Trademark overlap can leave open-source and free content projects vulnerable to a "hostile takeover" if outside parties file for trademarks on derivative works. [47] Notably, Andrey Duskin applied for trademarks on the SCP Foundation, a collaborative writing project, when creating derivative works based on SCP stories. [48]
Permissive
[ edit]
Main article: Permissive software license
Permissive licenses generally originate in academic institutions like the Massachusetts Institute of Technology.
Permissive licenses, also known as academic licenses, [49] allow recipients to use, modify, and distribute software with no obligation to provide source code. Institutions created these licenses to distribute their creations to the public. [49] Permissive licenses are usually short, often less than a page of text. They impose few conditions. Most include disclaimers of warranty and obligations to credit authors. A few include explicit provisions for patents, trademarks, and other forms of intellectual property. [50]
The University of California, Berkeley created the first open-source license when they began distributing their Berkeley Software Distribution (BSD) operating system. The BSD license and its later variations permit modification and distribution of the covered software. The licenses brought the concept of academic freedom of ideas to computing. Early academic software authors had shared code based on implied promises. Berkeley made these concepts explicit with clear disclaimers for liability and warranty along with conditions, or clauses, for redistribution. The original had four clauses, but subsequent versions have further reduced the restrictions. As a result, it is common to specify if the covered software uses a 2-clause or 3-clause version. [51] [52]
The Massachusetts Institute of Technology (MIT) created an academic license based on the BSD original. The MIT license clarified the conditions by making them more explicit. [53] For example, the MIT license describes the right to sublicense. [54] One of the strengths of open-source development is the continual process where developers can build on the derivative works of each other and combine their projects into collective works. Explicitly making covered code sublicensable provides a legal advantage when tracking the chain of authorship. [53] The BSD and MIT are template licenses that can be adapted to any project. They are widely adapted and used by many FOSS projects. [51]
The Apache License is more comprehensive and explicit. The Apache Software Foundation wrote it for their Apache HTTP Server. Version 2, published in 2004, offers legal advantages over simple licenses and provides similar grants. [55] While the BSD and MIT licenses offer an implicit patent grant, [56] the Apache License includes a section on patents with an explicit grant from contributors. [57] Additionally, it is one of the few permissive licenses with a patent retaliation clause. [58] Patent retaliation, or patent suspension, clauses take effect if a licensee initiates patent infringement litigation on covered code. In that situation, the patent grants are revoked. These clauses protect against patent trolling. [59]
Copyleft
[ edit]
Main article: Copyleft
The Copyleft sticker from an envelope Don Hopkins mailed to Richard Stallman in 1984
Copyleft licenses require source code to be distributed with software and require the source code to be made available under a similar license. [34] [60] Like the permissive licenses, most copyleft licenses require attribution. [61] Most, including the GPL, disclaim implied warranties. [62]
Copyleft uses the restrictions of IP law—contrary to their usual purpose—to mandate that the code remain open. [63] The term and its related slogan, "All rights reversed", had been previously used in a playful manner by the Principia Discordia and Tiny BASIC; the modern usage begins with Richard Stallman's efforts to create a free operating system. In 1984, programmer Don Hopkins mailed a manual to Stallman with a "Copyleft Ⓛ" sticker. Stallman, who was working on the GNU operating system, adopted the term. [64] An early version of copyleft licensing was used for the 1985 release of GNU Emacs. [14] [65] The term became associated with the FSF's later reciprocal licenses, notably the GNU General Public License (GPL). [66]
Traditional, proprietary software licenses are written with the goal of increasing profit, but Stallman wrote the GPL to increase the body of available free software. His reciprocal licenses offer the rights to use, modify, and distribute the work on the condition that people must release derivative works under a license offering these same freedoms. Software built on a copyleft base must come with the source code, and the source code must be available under the same or a similar license. This offers protection against proprietary software consuming code without giving back. [67] [68] Richard Stallman stated that "the central idea of copyleft is to use copyright law, but flip it over to serve the opposite of its usual purpose: instead of a means of privatizing software, [copyright] becomes a means of keeping software free." [69] Free-software licenses are also open-source software licenses. [70] The separate terms free software and open-source software reflect different values rather than a legal difference. [71] Both movements and their formal definitions require the covered work to be made available with source code and with permission for modification and redistribution. [16] There are occasional edge cases where only one of the FSF or the OSI accept a license, but the popular free-software licenses are open source, including the GPL. [72]
Mitchell Baker drafted the Mozilla Public License while on Netscape's legal team. [73]
Practical benefits to copyleft licenses have attracted commercial developers. Corporations have used and written reciprocal licenses with a narrower scope than the GPL. [74] For example, Netscape drafted their own copyleft terms after rejecting permissive licenses for the Mozilla project. [32] The GPL remains the most popular license of this type, but there are other significant examples. The FSF has crafted the Lesser General Public License (LGPL) for libraries. Mozilla uses the Mozilla Public License (MPL) for their releases, including Firefox. IBM drafted the Common Public License (CPL) and later adopted the Eclipse Public License (EPL). A difference between the GPL and other reciprocal licenses is how they define derivative works covered by the reciprocal provisions. The GPL, and the Affero License (AGPL) based on it, use a broad scope to describe affected works. The AGPL extends the reciprocal obligation in the GPL to cover software made available over a network. [74] [32] They are called strong copyleft in contrast to the weaker copyleft licenses often used by corporations. Weak copyleft uses narrower, explicit definitions of derivative works. [75] [35] The MPL uses a file-based definition, the CPL and EPL use a module-based definition, and the FSF's own LGPL refers to software libraries. [76]
Compatibility
[ edit]
Main article: License compatibility
Open-source software licenses and how they interact
License compatibility determines how code with different licenses can be distributed together. The goal of open-source licensing is to make the work freely available, but this becomes complicated when working with multiple terminologies imposing different requirements. [77] There are many uncommonly used licenses and some projects write their own bespoke agreements. As a result, this causes more confusion than other legal aspects. When releasing a collection of applications, each license can be considered separately. However, when attempting to combine software, code from another project can only be in-licensed if the project uses compatible terms and conditions. [78]
When combining code bases, the original licenses can be maintained for separate components, and the larger work released under a compatible license. [79] This compatibility is often one-way. Public domain content can be used anywhere as there is no copyright claim, but code acquired under any almost any set of terms cannot be waved to the public domain. Permissive licenses can be used within copyleft works, but copyleft material cannot be released under a permissive license. Some weak copyleft licenses can be used under the GPL and are said to be GPL-compatible. GPL software can only be used under the GPL or AGPL. [77] Permissive licenses are broadly compatible because they can cover separate parts of a project. Multiple licenses including the GPL and Apache License have been revised to enhance compatibility. [80]
Translation issues, ambiguity in licensing terms, and incompatibility of some licenses with the law in certain jurisdictions compound the problem of license compatibility. [81] Downloading an open-source module is straightforward, but complying with the licensing terms can be more difficult. [82] Because of the amount of software dependencies, engineers working on complex projects often rely on license management software to achieve compliance with the licensing terms of open-source components. [83] Many open-source software files do not unambiguously state the license, increasing the difficulties of compliance. [82]
Enforcement
[ edit]
Main article: Open source license litigation
Early legal victories by programmer Harald Welte established a precedent for open-source software litigation in Germany. [84]
Free and open-source software licenses have been successfully enforced in civil court since the mid-2000s. [85] In a pair of early lawsuits— Jacobsen v. Katzer in the United States and Welte v. Sitecom in Germany—defendants argued that open-source licenses were invalid. [86] [87] Sitecom and Katzer separately argued that the licenses were unenforceable. Both the US and German courts rejected these claims. They ruled that the defendants could not have legally distributed the software if the licenses were unenforceable. [85] [84]
Courts have found that distributing software indicates acceptance of the license's terms. [88] Physical software releases can obtain the consumer's assent with notices placed on shrinkwrap. Online distribution can use clickwrap, a digital equivalent where the user must click to accept. [89] Open-source software has an additional acceptance mechanism. Without permission from the copyright holder, the law prohibits redistribution. [90] Therefore, courts treat redistribution as acceptance of the license terms. These can include attribution provisions or source code provisions for copyleft licenses. [91] [92]
Developers typically achieve compliance without lawsuits. Social pressures, like the potential for community backlash, are often sufficient. [93] Cease and desist letters are a common method to bring companies back into compliance, especially in Germany. [94] A standard process has developed in the German legal system. FOSS developers present companies with a cease and desist letter. These letters outline how to come back into compliance from a violation. German judges can issue a court-mandated cease and desist order to unresponsive companies. Civil cases proceed if these first steps fail. The German procedural laws are clear and favorable to claimants. [95]
Uncertainties remain in how different courts will handle certain aspects of licensing. [96] For software in general, there are debates about what can be patented and what can be copyrighted. Regarding an application programming interface (API), the European Court of Justice noted in the 2012 SAS Institute case that "ideas and principles which underlie [computer program] interfaces are not protected by copyright". [97] In a similar 2021 case, the US Supreme Court permitted the recreation of an API in a transformative product under fair use. [98]
A long-debated subject within the FOSS community is whether open-source licenses are "bare licenses" or contracts. [96] A bare license is a set of conditions under which actions otherwise restricted by IP laws are permitted. [85] Under the bare license interpretation, advocated by the FSF, a case is brought to court by the copyright holder as copyright infringement. [85] Under the contract interpretation, a case can be brought to court by an involved party as a breach of contract. [99] US and French courts have tried cases under both interpretations. [100] Non-profit organizations like FSF and the Software Freedom Conservancy offer to hold the rights to developers' projects to enforce compliance. [95]
Public-domain software
[ edit]
Main article: Public-domain software
Early computer programs like the pioneering video game Spacewar! are in the public domain. [101]
When a copyright expires, the work enters the public domain, and is freely available to anyone. [102] Some creative works are not covered by copyright and enter directly into the public domain. In the early history of computing, this applied to software. [11] Early computer software was often given away with hardware. [103] Developed initially at MIT, the pioneering video game Spacewar! was used to market and test the PDP-1 computer. [104]
According to attorney Lawrence Rosen, copyright laws were not written with the expectation that creators would place their work into the public domain. Thus intellectual property laws lack clear paths to waive a copyright. Highly permissive licenses described as "public domain" may legally function as unilateral contracts that offer something but impose no terms. [105] [106]
A public-domain-equivalent license, like the Creative Commons CC0, provides a waiver of copyright claims into the public domain along with a permissive software license as a fallback. In jurisdictions that do not accept a public domain waiver, the permissive license takes effect. [107] Public domain waivers share limitations with simple academic licenses. This creates the possibility that an outside party could attempt to control a public domain work via patent or trademark law. [108] Public domain waivers handle warranties differently from any type of license. Even very permissive ones, like the MIT license, disclaim warranty and liability. Anyone using the free software must accept this disclaimer as a condition. Because public domain content is available to everyone, the copyright waiver cannot impose a disclaimer. [102]
Use in proprietary software
[ edit]
Open-source licenses allow other businesses to commercialize covered software. [109] Work released under a permissive license can be incorporated into proprietary software. [110] Permissive licenses permit the addition of new terms, including proprietary ones. [111] [112] Proprietary software has heavily integrated open-source code released under the Apache, BSD, and MIT licenses. [113] Open core is a business model where developers release a core piece of software as open source and monetize a product containing it as proprietary software. [114] The strong copyleft GPL is written to prevent distribution within proprietary software. [115] [116] Weak copyleft licenses impose specific requirements on derivative works that may allow the covered code to be distributed within proprietary software in certain circumstances. [77]
Cloud computing relies on free and open-source software and avoids the distribution that triggers most licenses. Cloud software is hosted rather than distributed. [117] A vendor hosts the software online, and their end users do not have to download, access, or even know about the code in use. [118] The copyleft GNU Affero General Public License (AGPL) is triggered when covered code is hosted or distributed. [119] Some developers have adopted the AGPL, and others have switched to proprietary licenses with features of open-source licensing. [120] For example, open-core developer Elastic switched from the Apache license to the "source-available" Server Side Public License. [121] Source-available software comes with source code as a reference. [122]
Since 2010, the cloud model has grown in prominence. [117] Developers have criticized cloud companies that profit from hosting open-source software without contributing money or code upstream, comparing the practice to strip mining. [123] Cloud computing leader Amazon Web Services has stated they comply with licenses and act in their customers' best interests. [123] [124]
See also
[ edit]
Beerware
Comparison of free and open-source software licenses
Contributor License Agreement
List of free-content licenses
Multi-licensing
Software Composition Analysis
List of free and open-source software licenses
List of copyleft software licenses
List of open-source programming languages
List of permissive software licenses
Notes
[ edit]
^ Byfield 2008.
^ Rosen 2005, p. 22.
^ Rosen 2005, pp. 22–23.
^ Jump up to: a  b Rosen 2005, p. 15.
^ Smith 2022, sec. 3.1.2.
^ Fagundes & Perzanowski 2020, p. 529.
^ Rosen 2005, p. 17.
^ Rosen 2005, pp. 27–28.
^ Rosen 2005, pp. 28–29.
^ Rosen 2005, p. 28.
^ Jump up to: a  b Oman 2018, pp. 641–642.
^ Williams 2002, ch. 1.
^ Williams 2002, ch. 7.
^ Jump up to: a  b Williams 2002, ch. 9.
^ Greenbaum 2016, sec. I.A.
^ Jump up to: a  b  c Maracke 2019, sec. 2.2.
^ Carver 2005, pp. 448–450.
^ Perens 1999.
^ Greenbaum 2016, pp. 1302–1303.
^ Greenbaum 2016, pp. 1304–1305.
^ Greenbaum 2016, p. 1305.
^ Fontana 2010, p. 2.
^ Coleman 2004, "Political Agnosticism".
^ Raymond 1999, "Memes and Mythmaking".
^ Meeker 2020, 2:33–3:06.
^ Raymond 2001, "The Cathedral and the Bazaar".
^ Brock 2022, sec. 16.3.4.
^ Raymond 2001.
^ Raymond 2001, "The Social Context of Open-Source Software".
^ Raymond 2001, p. 19.
^ Onetti & Verma 2009, p. 69.
^ Jump up to: a  b  c Hammerly, Paquin & Walton 1999.
^ Smith 2022, sec. 3.2.
^ Jump up to: a  b Sen, Subramaniam & Nelson 2008, pp. 211–212.
^ Jump up to: a  b Meeker 2020, 16:13.
^ Jump up to: a  b Rosen 2005, pp. 22–24.
^ Bain & Smith 2022, sec. 10.4.3.
^ Bain & Smith 2022, sec. 10.4.2.
^ Jump up to: a  b Bain & Smith 2022, sec. 10.4.4.
^ Chestek 2022, p. 30.
^ Chestek 2022, pp. 184–185.
^ Rosen 2005, p. 38.
^ Joy 2022, p. 986.
^ Joy 2022, p. 989.
^ Dastar Corp. v. Twentieth Century Fox Film Corp. , 539 U.S. 23, 34 (2003).
^ Joy 2022, pp. 987–988.
^ Joy 2022, pp. 1004–1006.
^ Joy 2022, pp. 979, 1002.
^ Jump up to: a  b Rosen 2005, p. 69.
^ Rosen 2005, pp. 101–102.
^ Jump up to: a  b Smith 2022, sec. 3.2.1.1.
^ OSI 2023.
^ Jump up to: a  b Rosen 2005, pp. 73–90.
^ OSI 2023, "The MIT License".
^ Smith 2022, sec. 3.2.1.2.
^ Bain & Smith 2022, sec. 10.4.2.
^ OSI 2023, "Apache License, Version 2.0".
^ Bain & Smith 2022, ch. 10.
^ Bain & Smith 2022, sec. 10.4.4.
^ St. Laurent 2004, pp. 38–39.
^ Ballhausen 2019, p. 86.
^ Rosen 2005, p. 135.
^ Rosen 2005, pp. 103–106.
^ Keats 2010, p. 64.
^ "Full Text of GNU Emacs Copying Permission Notice". 1985.
^ Keats 2010, pp. 63–67.
^ Rosen 2005, pp. 103–109.
^ Meeker 2020, 6:00–7:22.
^ Joy 2022, pp. 990–992.
^ Onetti & Verma 2009, p. 71.
^ St. Laurent 2004, pp. 81–83, 114.
^ Ballhausen 2019, p. 82.
^ St. Laurent 2004, pp. 68, 75.
^ Jump up to: a  b Tsai 2008, pp. 564–570.
^ Sen, Subramaniam & Nelson 2008, pp. 212–213.
^ Rosen 2005, refer to corresponding chapters.
^ Jump up to: a  b  c Smith 2022, sec. 3.3.
^ Rosen 2005, pp. 243–247.
^ St. Laurent 2004, pp. 159–163.
^ See Smith 2022, p. 102 for: Apache License version 2.0 in 2004, GPL version 3 in 2007, LGPL version 3 in 2007, and AGPL version 3 in 2007. See Smith 2022, pp. 95–101 for: MPL version 2.0 in 2012 and EPL version 2 in 2017.
^ Bernelin 2020, pp. 100, 102.
^ Jump up to: a  b Ombredanne 2020, p. 105.
^ Ombredanne 2020, p. 106.
^ Jump up to: a  b Ballhausen 2022, sec. 5.3.
^ Jump up to: a  b  c  d Smith 2022, sec. 3.4.1.
^ Jacobsen v. Katzer , 535 F.3d 1373 ( Fed. Cir. 2008).
^ Welte v. Sitecom (District Court of Munich 2004), No. 21 O 6123/04.
^ Smith 2022, p. 106.
^ Rosen 2005, p. 137.
^ Rosen 2005, p. 138.
^ Rosen 2005, ch. 6.
^ Meeker 2020, 17:04.
^ St. Laurent 2004, pp. 158–159.
^ Ballhausen 2022, p. 127.
^ Jump up to: a  b Ballhausen 2022, sec. 5.4.
^ Jump up to: a  b Walden 2022, sec. 1.1.
^ Smith 2022, sec. 3.1.3.
^ Google LLC v. Oracle America, Inc. , 593 U.S., 1203 (2021).
^ Smith 2022, sec. 3.4.2.
^ Smith 2022, sec. 3.4.
^ Ross 2021, "Spacewar: End of Development".
^ Jump up to: a  b Rosen 2005, p. 36.
^ Walden 2022, p. 3.
^ Smith 2019, pp. 55–56.
^ Rosen 2005, pp. 74–77.
^ St. Laurent 2004, p. 98.
^ Fagundes & Perzanowski 2020, p. 524.
^ Joy 2022, pp. 1008–1010.
^ Brock 2022, sec. 16.3.3.
^ St. Laurent 2004, p. 14.
^ St. Laurent 2004, p. 22.
^ Onetti & Verma 2009, p. 81.
^ St. Laurent 2004, p. 30.
^ Brock 2022, sec. 16.4.2.3.
^ Tsai 2008, p. 550.
^ St. Laurent 2004, p. 39.
^ Jump up to: a  b Brock 2022, sec. 16.5.2.
^ Brock 2022, sec. 16.4.2.8.
^ Brock 2022, sec. 16.4.2.2.
^ Brock 2022, sec. 16.5.3.
^ Brock 2022, sec. 16.5.3.8.
^ Kunert 2022.
^ Jump up to: a  b Wakabayashi 2019.
^ Brock 2022, sec. 16.5.3.2.
References
[ edit]
Ballhausen, Miriam (June 2019). "Free and Open Source Software Licenses Explained". Computer. 52 (6): 82– 86. Bibcode: 2019Compr..52f..82B. doi: 10.1109/MC.2019.2907766.
Bernelin, Margo (2020). "The Compatibility of Open/Free Licences: a Legal Imbroglio". International Journal of Law and Information Technology. 28 (2): 93– 111. doi: 10.1093/ijlit/eaaa010.
Brock, Amanda, ed. (2022). Open Source Law, Policy and Practice (Second ed.). Oxford University Press. doi: 10.1093/oso/9780198862345.001.0001. ISBN 978-0-19-886234-5 .
Bain, Malcom; Smith, P McCoy. " Patents and the Defensive Response". In Brock (2022).
Ballhausen, Miriam. " Copyright Enforcement". In Brock (2022).
Chestek, Pamela. " Trademarks". In Brock (2022).
Smith, P McCoy. " Copyright, Contract, and Licensing in Open Source". In Brock (2022).
Walden, Ian. " Open Source as Philosophy, Methodology, and Commerce: Using Law with Attitude". In Brock (2022).
Byfield, Bruce (March 4, 2008). ""Free" and "Open Source" Software: Navigating the Shibboleths". Datamation. Retrieved June 6, 2024.
Carver, Brian W. (2005). "Share and Share Alike: Understanding and Enforcing Open Source and Free Software Licenses". Berkeley Technology Law Journal. 20 (1): 443– 481. ISSN 1086-3818. JSTOR 24117523.
Coleman, Gabriella (2004). "The Political Agnosticism of Free and Open Source Software and the Inadvertent Politics of Contrast". Anthropological Quarterly. 77 (3): 507– 519. doi: 10.1353/anq.2004.0035. hdl: 10524/1583. ISSN 0003-5491. JSTOR 3318232.
DiBona, Chris; Stone, Mark; Ockman, Sam, eds. (1999). Open Sources: Voices from the Open Source Revolution. Sebastopol, California: O'Reilly Media. Archived from the original on January 27, 2023. Retrieved January 21, 2023.
Hammerly, Jim; Paquin, Tom; Walton, Susan. " Freeing the Source: The Story of Mozilla". In DiBona, Stone & Ockman (1999).
Perens, Bruce. " The Open Source Definition". In DiBona, Stone & Ockman (1999).
Raymond, Eric S. " The Revenge of the Hackers". In DiBona, Stone & Ockman (1999).
Fagundes, Dave; Perzanowski, Aaron (November 2020). "Abandoning Copyright". William & Mary Law Review. 62 (2): 487– 569.
Fontana, Richard E. (April 2010). "Open Source License Enforcement and Compliance". The Computer and Internet Lawyer. 27 (4). Aspen.
Greenbaum, Eli (April 2016). "The Non-Discrimination Principle in Open Source Licensing" (PDF). Cardoza Law Review. 37 (4).
Joy, Reagan (2022). "The Tragedy of the Creative Commons: An Analysis of How Overlapping Intellectual Property Rights Undermine the Use of Permissive Licensing". Case Western Reserve Law Review. 72 (4): 977– 1013.
Keats, Jonathon (2010). Virtual Words: Language on the Edge of Science and Technology. Oxford University Press. doi: 10.1093/oso/9780195398540.003.0017. ISBN 978-0-19-539854-0 . Archived from the original on March 26, 2023. Retrieved January 28, 2023.
Kunert, Paul (September 8, 2022). "Open Source Biz Shifts Akka to Business Source License". Archived from the original on October 31, 2022. Retrieved January 25, 2023.
Maracke, Catharina (July 2019). "Free and Open Source Software and FRAND-Based Patent Licenses: How to Mediate Between Standard Essential Patent and Free and Open Source Software". The Journal of World Intellectual Property. 22 ( 3– 4): 78– 102. doi: 10.1111/jwip.12114.
Meeker, Heather (January 2020). Open Source Software Licensing Basics for Corporate Users. Open Source Software Licensing. Retrieved December 7, 2023.
Oman, Ralph (Spring 2018). "Computer Software as Copyrightable Subject Matter: Oracle V. Google, Legislative Intent, and the Scope of Rights in Digital Works". Harvard Journal of Law & Technology. 31 (2): 639– 652.
Ombredanne, Philippe (2020). "Free and Open Source Software License Compliance: Tools for Software Composition Analysis". Computer. 53 (10): 105– 109. Bibcode: 2020Compr..53j.105O. doi: 10.1109/MC.2020.3011082.
Onetti, Alberto; Verma, Sameer (May 1, 2009). "Open Source Licensing and Business Models". ICFAI Journal of Knowledge Management. 7 (1): 68– 94.
OSI (February 2023). "OSI Approved Licenses". opensource.org. Open Source Initiative. Retrieved December 23, 2023.
Raymond, Eric S. (2001). The Cathedral & the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary (Revised ed.). Sebastopol, California: O'Reilly Media. ISBN 978-0-596-00108-7 . Archived from the original on April 24, 2003. Retrieved January 28, 2023.
Rosen, Lawrence (2005). Open Source Licensing: Software Freedom and Intellectual Property Law (Paperback ed.). Upper Saddle River, NJ: Prentice Hall. ISBN 978-0-13-148787-1 . Archived from the original on December 19, 2022. Retrieved January 21, 2023.
Ross, Heather (January 4, 2021). "Spacewar - Guide, History, Origin and More". History-Computer. Retrieved December 23, 2023.
Sen, Ravi; Subramaniam, Chandrasekar; Nelson, Matthew L. (Winter 2008). "Determinants of the Choice of Open Source Software License". Journal of Management Information Systems. 25 (3): 207– 239. doi: 10.2753/MIS0742-1222250306.
Smith, Alexander (2019). They Create Worlds: The Story of the People and Companies That Shaped the Video Game Industry. Vol. 1: 1971 – 1982. Boca Raton, Florida: CRC Press. ISBN 978-1-138-38990-8 .
St. Laurent, Andrew M. (2004). Understanding Open Source and Free Software Licensing. Sebastopol, California: O'Reilly Media. ISBN 978-0596005818 .
Tsai, John (2008). "For Better or Worse: Introducing the Gnu General Public License Version 3". Berkeley Technology Law Journal. 23 (1): 547– 581.
Wakabayashi, Daisuke (December 15, 2019). "Prime Leverage: How Amazon Wields Power in the Technology World". The New York Times. Retrieved May 24, 2024.
Williams, Sam (2002). Free as in Freedom: Richard Stallman's Crusade for Free Software (First ed.). Sebastopol, California : Farnham: O'Reilly Media. ISBN 978-0-596-00287-9 . Archived from the original on February 7, 2023. Retrieved February 6, 2023.
show
v
t
e
Software distribution
Licenses
Beerware
Floating licensing
Free and open-source
Free
Open source
Freely redistributable
License-free
Proprietary
Public domain
Source-available
Compensation models
Adware
Commercial software
Retail software
Crippleware
Crowdfunding
Freemium
Freeware
Pay what you want
Careware
Donationware
Open-core model
Postcardware
Shareware
Nagware
Trialware
Delivery methods
Digital distribution
File sharing
On-premises
Pre-installed
Product bundling
Retail software
Sneakernet
Software as a service
Deceptive and/or illicit
Unwanted software bundling
Malware
Infostealer
Ransomware
Spyware
Trojan horse
Worm
Scareware
Shovelware
Software release life cycle
Abandonware
Long-term support
Software maintenance
Software maintainer
Software publisher
Vaporware
list
Copy protection
Digital rights management
Software protection dongle
License manager
Product activation
Product key
Software copyright
Software license server
Software patent
Torrent poisoning
show
v
t
e
Free and open-source software
General
Alternative terms for free software
Comparison of open-source and closed-source software
Comparison of source-code-hosting facilities
Free software
Free software project directories
Gratis versus libre
Long-term support
Open-source software
Open-source software development
Outline
Timeline
Software packages
Audio
Bioinformatics
Codecs
Configuration management
Drivers
Graphics
Wireless
Health
Mathematics
Office suites
Operating systems
Routing
Television
Video games
Web applications
E-commerce
Android apps
iOS apps
Commercial
Formerly proprietary
Formerly open-source
Community
Free software movement
History
Open-source-software movement
Events
Advocacy
Organisations
Free Software Movement of India
Free Software Foundation
Licenses
AFL
Apache
APSL
Artistic
Beerware
BSD
Creative Commons
CDDL
EPL
Free Software Foundation
GNU GPL
GNU AGPL
GNU LGPL
ISC
MIT
MPL
Python
Python Software Foundation License
Shared Source Initiative
Sleepycat
Unlicense
WTFPL
zlib
Types and
standards
Comparison of licenses
Contributor License Agreement
Copyleft
Debian Free Software Guidelines
Definition of Free Cultural Works
Free license
The Free Software Definition
The Open Source Definition
Open-source license
Permissive software license
Public domain
Challenges
Digital rights management
License proliferation
Mozilla software rebranding
Proprietary device drivers
Proprietary firmware
Proprietary software
SCO/Linux controversies
Software patents
Software security
Tivoization
Trusted Computing
Related
topics
Forking
GNU Manifesto
Microsoft Open Specification Promise
Open-core model
Open-source hardware
Shared Source Initiative
Source-available software
The Cathedral and the Bazaar
Revolution OS
Portal
Category 
Retrieved from " https://en.wikipedia.org/w/index.php?title=Open-source_license&oldid=1348280901"
Categories:
Free and open-source software licenses
Terms of service
Free culture movement
Hidden categories:
Good articles
Articles with short description
Short description is different from Wikidata
Use mdy dates from January 2023
CS1: long volume value
This page was last edited on 11 April 2026, at 19:46 (UTC).
Text is available under the Creative Commons Attribution-ShareAlike 4.0 License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.
Privacy policy
About Wikipedia
Disclaimers
Contact Wikipedia
Legal & safety contacts
Code of Conduct
Developers
Statistics
Cookie statement
Mobile view
Search
Search [-]
Toggle the table of contents
Open-source license
15 languages Add topic 
