---
name: 2026-05-14 CLAs and using DCO clearly. Open Source projects often, as they… | by Hen | Medium
keywords: (placeholder)
metadata:
  url: None
  source: SOURCE_TYPE_TEXT
  date: 2026-05-14T23:05:07.687Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
WebSync metadata
title: CLAs and using DCO clearly. Open Source projects often, as they… | by Hen | Medium
url: https://medium.com/@flamefew/clas-and-using-dco-clearly-e46b09a4c048
date: 2026-05-14T22:40:32.214Z
parsing method: defuddle
Sitemap
Open Source projects often, as they grow, move to using a Contributor License Agreement (CLA). There are variants of CLAs, but the common experience is one in which the contributor signs an agreement which determines the license of their contributions and promises the contribution is kosher. That experience is not zero-cost, for contributor or project. Let’s review the pain-points of that experience…
Pain-point #1: CLAs, unlike most Open Source licenses, are not standardized.
The Apache Individual CLA is one such example. It was created to cover contributions from committers to projects under the auspices of the Apache Software Foundation, and like their license, it has often been copied. Unlike the Apache License 2.0, the ICLA is also always modified. Some of those modifications are necessary (changing ‘Foundation’ to ‘Project’ or ‘Company’), but others are the result of legal bugfixes or additional conditions. This makes review of the CLA either an onerous, or overlooked, task.
There was an effort to standardize them. In 2010, after a bit of a public CLA SNAFU at Canonical, a CLA standardization (Project Harmony) was started. Said project reviewed the options for CLAs and created a matrix of new CLAs (like the many Creative Commons licenses). Unfortunately this project was a) a whole bunch of new CLAs; and b) too representative of Open Source projects dominated by a corporate owner. Typically I have only seen this CLA format used when a company wants permission to do whatever they can with your contributions.
Pain-point #2: Corporate CLAs; which are difficult to sign, have to be maintained, and are too broad in scope.
In Apache’s early history there were concerns from some employers that their employees could not sign a CLA. Thus the Apache Corporate CLA (CCLA) was created. Apache do not require that this be signed, but many projects (typically corporate owned in my experience) have also copied the CCLA and require it for contribution. CCLAs are a pain-point in their own right: you have to find someone at your employer who can legally sign for the company; no one really knows to invalidate your CCLA when you change employer; and the CCLA either covers every employee regardless of project involvement, or has a list of employees that must be maintained (though rarely is there a clear procedure on how to notify the project of necessary changes).
Pain-point #3: Contributions aren’t under the project license
Despite the contributor receiving the software from a project owner under one license, the CLA determines a different license for the contribution back to the project owner. With the Apache ICLA, the text is heavily based on the Apache License 2.0 itself. Its. Other CLAs however take greater latitude and the contribution back may lack the scope of the license. This creates an inequality within the community.
While this inequality is often for the purposes of relicensing to future unknown licenses, it is also used to allow for unconditional use of the code in a project owner’s commercial product. Such inequalities are against the spirit of many Open communities.
One plus side of this however is when a project is dual-licensed; be it because it has chosen two or more licenses (for example MIT/GPL dual licensed), or an open-ended license version (for example GPL 2.0 or later). In these cases multiple licenses apply to the contribution and a CLA could be considered to simplify things; especially for the question of whether a contribution to a GPL 2.0 or later licensed project is under GPL 4.0.
Pain-point #4: Signing a document is an oft painful experience
Signing the CLA is also a pain-point. That may be because it involves the old-school approach of signing a physical document, followed by the use of a Fax machine or emailing a scanned copy; or it involves an online e-signature which adds complexity to the project. For Apache the management isn’t too troublesome as it only requires a CLA when a committer account is created, but for the many projects that require a CLA on every commit this can be a management pain (though that pain is often outsourced to https://cla-assistant.io/).
Projects are also often sign-happy. The simplest contribution requires a signed CLA, even if that contribution is not expressive copyright. Want to fix a typo in a project? Sign a CLA.
It perhaps didn’t need to be this way. The Apache License 2.0 contains a condition (clause 5) which states that:
5. Submission of Contributions. Unless You explicitly state otherwise, any Contribution intentionally submitted for inclusion in the Work by You to the Licensor shall be under the terms and conditions of this License, without any additional terms or conditions. Notwithstanding the above, nothing herein shall supersede or modify the terms of any separate license agreement you may have executed with Licensor regarding such Contributions.
Apache relies on this for contributions from contributors (non-committers), so why sign a CLA when the license already covered the topic of contributions? It’s belt-and-suspender legal conservatism; nothing inherently bad as advice in the late 90s, but might not be the same as we approach 2020.
Along these lines, there is a similar no-CLA approach in use with some other projects. The Developer Certificate of Origin (DCO) came out of the Linux Kernel project and involves a contributor saying “Signed-off-by: <name>” in a contribution to imply that their contribution adheres to the statement on https://developercertificate.org/.
The DCO ‘fixes’ two issues with the typical CLA. Firstly, it does not contain a separate license (pain-point #3); instead it considers the contribution under the license of the project itself (as a side note, the Apache License 2.0 also contains this in clause 5, raising the question of whether clause 5, ICLA or CCLA applies to a contribution). Secondly, the DCO does not involve a lengthy, one-time, signature process but is instead covered in every commit by the “Signed-off-by” phrase.
I like the DCO. Contributions should be simple. I think it’s vague in places though, so here are my nitpicks.
DCO Nitpicks
The DCO is a good direction away from CLAs, but it has some problems of its own (these are nitpicks).
Firstly, it relies on the license of the contribution being clear:
“I have the right to submit it under the open source license indicated in the file”
This requires every source file to indicate the license (an open source best practice, but one not often done by projects). It also (as file is undefined) doesn’t work well with patch files as they often don’t include the source header.
Secondly, it relies on a magic phrase (Signed-off-by) which does not indicate what is being signed up to. Viewed grammatically, that text suggests it is signing off on the code (i.e. approval), not signing up to any form of legal statement. This magic phrase also does not appear within the DCO itself. This seems (to me) worryingly akin to having someone sign a blank piece of paper and then claiming later that it related to a legal document.
Thirdly, it talks of an appropriate open source license  without a determination of appropriate. In most ways this is great, it recognizes that a contribution to an open source project is under a plethora of licenses and puts the onus on the contributor; however it doesn’t provide the project with a methodology to educate the contributor on what is considered (by the project) to be appropriate).
Resolving My Nitpicks
I would propose that those using the DCO should also:
Ensure that every source file has a source header.
Host their own copy of the developer certificate (DCO).
Append a list of SPDX licenses under an Appropriate Licenses footer in the DCO file.
Host a file (CONTRIBUTORS) in the root of the project which states that the project is using the Developer Certificate of Origin (see DCO file), that the list of names/logins below have agreed to do this, that the inclusion of ‘Signed-off-by’ in each commit indicates that the commit is considered to fall under this statement, and where each name/login is added as a pull request/contribution by the individual themselves.
This requires contribution review to ensure that a contribution’s Signed-off-by appears in the CONTRIBUTORS file. This can be automated, unlike the current contribution review that is required every time to ensure somebody didn’t contribute as “Ming the Merciless”. Manual review would still be needed for any change to the CONTRIBUTORS file to ensure the Emperor of Mongo isn’t sneaking a pseudonym’d contribution in.
I’m sure many disagree with me:)
— — — — — — — — —
My thanks to @jejb_ and @mjg59 for their published thoughts on the values of the DCO approach.
