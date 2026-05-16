---
name: K-anonymity - Wikipedia
keywords: (placeholder)
metadata:
  url: https://en.wikipedia.org/wiki/K-anonymity
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T19:00:57.430Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
k-anonymity - Wikipedia
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
1 Methods for k-anonymization
2 Critiques of k-anonymity
3 Attacks
4 See also
5 References [-]
Toggle the table of contents
k-anonymity
[-]
9 languages
Deutsch
Español
Français
Italiano
日本語
한국어
Svenska
Українська
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
Property of certain anonymized data
k-anonymity is a property possessed by certain anonymized data. The term k-anonymity was first introduced by Pierangela Samarati and Latanya Sweeney in a paper published in 1998, [1] although the concept dates to a 1986 paper by Tore Dalenius. [2]
k-anonymity is an attempt to solve the problem "Given person-specific field-structured data, produce a release of the data with scientific guarantees that the individuals who are the subjects of the data cannot be re-identified while the data remain practically useful." [3] [4] [5] A release of data is said to have the k-anonymity property if the information for each person contained in the release cannot be distinguished from at least k − 1 {\displaystyle k-1} 
individuals whose information also appear in the release. The guarantees provided by k-anonymity are aspirational, not mathematical. [vague]
Methods for k-anonymization
[ edit]
To use k-anonymity to process a dataset so that it can be released with privacy protection, a data scientist must first examine the dataset and decide whether each attribute (column) is an identifier (identifying), a non-identifier (not-identifying), or a quasi-identifier (somewhat identifying). Identifiers such as names are suppressed, non-identifying values are allowed to remain, and the quasi-identifiers need to be processed so that every distinct combination of quasi-identifiers designates at least k records.
The example table below presents a fictional, non-anonymized database consisting of the patient records for a fictitious hospital. The Name column is an identifier, Age, Gender, State of domicile, and Religion are quasi-identifiers, and Disease is a non-identifying sensitive value. But what about Height and Weight? Are they also non-identifying sensitive values, or are they quasi-identifiers?
Patients treated in the study on April 30
There are 6 attributes and 10 records in this data. There are two common methods for achieving k-anonymity for some value of k:
Suppression. In this method, certain values of the attributes are replaced by an asterisk "". All or some values of a column may be replaced by "". In the anonymized table below, we have replaced all the values in the Name attribute and all the values in the Religion attribute with a "*".
Generalization. In this method, individual values of attributes are replaced with a broader category. For example, the value "19" of the attribute Age may be replaced by "≤ 20", the value "23" by "20 < Age ≤ 30", etc.
The next table shows the anonymized database.
Patients treated in the study on April 30
This data has 2-anonymity with respect to the attributes Age, Gender and State of domicile, since for any combination of these attributes found in any row of the table there are always at least 2 rows with those exact attributes. The attributes available to an adversary are called quasi-identifiers. Each quasi-identifier tuple occurs in at least k records for a dataset with k-anonymity. [6]
Critiques of k-anonymity
[ edit]
The following example demonstrates a failing with k-anonymity: there may exist other data records that can be linked on the variables that are allegedly non-identifying. For instance, suppose an attacker is able to obtain the log from the person who was taking vital signs as part of the study and learns that Kishor was at the hospital on April 30 and is 180 cm tall. This information can be used to link with the "anonymized" database (which may have been published on the Internet) and learn that Kishor has a heart-related disease. An attacker who knows that Kishor visited the hospital on April 30 may be able to infer this simply knowing that Kishor is 180 cm height, roughly 80–82 kg, and comes from Karnataka.
The root of this problem is the core problem with k-anonymity: there is no way to mathematically, unambiguously determine whether an attribute is an identifier, a quasi-identifier, or a non-identifying sensitive value. In fact, all values are potentially identifying, depending on their prevalence in the population and on auxiliary data that the attacker may have. Other privacy mechanisms such as differential privacy do not share this problem.
Although k-anonymity safeguards against identity revelations, it does not shield against the disclosure of specific attributes. This becomes problematic when attackers possess background knowledge. Additionally, the absence of diversity in sensitive domains may result in the exposure of personal information. In such scenarios, opting for ℓ-Diversity might offer a more robust privacy safeguard.[1]
Meyerson and Williams (2004) demonstrated that optimal k-anonymity is an NP-hard problem, however heuristic methods such as k-Optimize as given by Bayardo and Agrawal (2005) often yield effective results. [7] [8] A practical approximation algorithm that enables solving the k-anonymization problem with an approximation guarantee of O ( log  k ) {\displaystyle O(\log k)} 
was presented by Kenig and Tassa. [9]
Attacks
[ edit]
While k-anonymity is a relatively simple-to-implement approach for de-identifying a dataset prior to public release, it is susceptible to many attacks. When background knowledge is available to an attacker, such attacks become even more effective. Such attacks include:
Homogeneity Attack: This attack leverages the case where all the values for a sensitive value within a set of k records are identical. In such cases, even though the data has been k-anonymized, the sensitive value for the set of k records may be exactly predicted.
Background Knowledge Attack: This attack leverages an association between one or more quasi-identifier attributes with the sensitive attribute to reduce the set of possible values for the sensitive attribute. For example, Machanavajjhala, Kifer, Gehrke, and Venkitasubramaniam (2007) showed that knowing that heart attacks occur at a reduced rate in Japanese patients could be used to narrow the range of values for a sensitive attribute of a patient's disease.
Downcoding Attack: This attack, introduced in 2022 by Aloni Cohen, takes advantage of the way that anonymity algorithms aggregate attributes in separate records. Because the aggregation is deterministic, it is possible to reverse-engineer the original data image, and in many cases reveal the original data that was to be protected. This attack does not require background knowledge, but is strengthened by it. [10]
Because k-anonymization does not include any randomization, attackers can make reliable, unambiguous inferences about data sets that may harm individuals. For example, if the 19-year-old John from Kerala is known to be in the database above, then it can be reliably said that he has either cancer, a heart-related disease, or a viral infection.
K-anonymization is not a good method to anonymize high-dimensional datasets. [11]
It has also been shown that k-anonymity can skew the results of a data set if it disproportionately suppresses and generalizes data points with unrepresentative characteristics. [12] The suppression and generalization algorithms used to k-anonymize datasets can be altered, however, so that they do not have such a skewing effect. [13]
See also
[ edit]
t-closeness
ℓ-diversity
Differential privacy
Quasi-identifier
References
[ edit]
^ Samarati, Pierangela; Sweeney, Latanya (1998). "Protecting privacy when disclosing information: k-anonymity and its enforcement through generalization and suppression" (PDF). Harvard Data Privacy Lab. Retrieved April 12, 2017.
^ Tore Dalenius, "Finding a Needle In a Haystack", Journal of Official Statistics, Vol. 2, No. 3, 1986, pp. 326–336.
^ Samarati, Pierangela (November 2001). "Protecting Respondents' Identities in Microdata Release" (PDF). IEEE Transactions on Knowledge and Data Engineering. 13 (6): 1010– 1027. doi: 10.1109/69.971193. S2CID 561716.
^ Sweeney, Latanya. "Database Security: k-anonymity". Retrieved 19 January 2014.
^ Sweeney, Latanya (2002). " k-anonymity: a model for protecting privacy" (PDF). International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems. 10 (5): 557– 570. doi: 10.1142/S0218488502001648. S2CID 361794.
^ Narayanan, Arvind; Shmatikov, Vitaly. "Robust De-anonymization of Large Sparse Datasets" (PDF).
^ Roberto J. Bayardo; Rakesh Agrawal (2005). "Data Privacy through Optimal k-Anonymization". 21st International Conference on Data Engineering (ICDE'05) (PDF). pp. 217– 228. doi: 10.1109/ICDE.2005.42. ISBN 978-0-7695-2285-2 . ISSN 1084-4627. S2CID 17044848. Data de-identification reconciles the demand for release of data for research purposes and the demand for privacy from individuals. This paper proposes and evaluates an optimization algorithm for the powerful de-identification procedure known as k-anonymization. A k-anonymized dataset has the property that each record is indistinguishable from at least k − 1 others. Even simple restrictions of optimized k-anonymity are NP-hard, leading to significant computational challenges. We present a new approach to exploring the space of possible anonymizations that tames the combinatorics of the problem, and develop data-management strategies to reduce reliance on expensive operations such as sorting. Through experiments on real census data, we show the resulting algorithm can find optimal k-anonymizations under two representative cost measures and a wide range of k. We also show that the algorithm can produce good anonymizations in circumstances where the input data or input parameters preclude finding an optimal solution in reasonable time. Finally, we use the algorithm to explore the effects of different coding approaches and problem variations on anonymization quality and performance. To our knowledge, this is the first result demonstrating optimal k-anonymization of a nontrivial dataset under a general model of the problem.
^ Adam Meyerson; Ryan Williams (2004). "On the complexity of optimal K-anonymity". Proceedings of the twenty-third ACM SIGMOD-SIGACT-SIGART symposium on Principles of database systems (PDF). New York, NY: ACM. pp. 223– 228. doi: 10.1145/1055558.1055591. ISBN 978-1581138580 . S2CID 6798963. Archived from the original (PDF) on 2014-05-28. Retrieved 2014-05-28. The technique of k-anonymization has been proposed in the literature as an alternative way to release public information, while ensuring both data privacy and data integrity. We prove that two general versions of optimal k-anonymization of relations are NP-hard, including the suppression version which amounts to choosing a minimum number of entries to delete from the relation. We also present a polynomial time algorithm for optimal k-anonymity that achieves an approximation ratio independent of the size of the database, when k is constant. In particular, it is a O( k log k)-approximation where the constant in the big- O is no more than 4. However, the runtime of the algorithm is exponential in k. A slightly more clever algorithm removes this condition, but is a O( k log m)-approximation, where m is the degree of the relation. We believe this algorithm could potentially be quite fast in practice.
^ Kenig, Batya; Tassa, Tamir (2012). "A practical approximation algorithm for optimal k-anonymity". Data Mining and Knowledge Discovery. 25: 134– 168. doi: 10.1007/s10618-011-0235-9. S2CID 14158546.
^ Attacks on Deidentification's Defenses, Aloni Cohen, USENIX Security 2022, Distinguished Paper Award Winner. https://www.usenix.org/conference/usenixsecurity22/presentation/cohen
^ Aggarwal, Charu C. (2005). "On k-Anonymity and the Curse of Dimensionality". VLDB '05 – Proceedings of the 31st International Conference on Very large Data Bases. Trondheim, Norway. CiteSeerX 10.1.1.60.3155. ISBN 1-59593-154-6 .
^ Angiuli, Olivia; Joe Blitzstein; Jim Waldo. "How to De-Identify Your Data". ACM Queue. ACM.
^ Angiuli, Olivia; Jim Waldo (June 2016). "Statistical Tradeoffs between Generalization and Suppression in the De-identification of Large-Scale Data Sets". 2016 IEEE 40th Annual Computer Software and Applications Conference (COMPSAC). pp. 589– 593. doi: 10.1109/COMPSAC.2016.198. ISBN 978-1-4673-8845-0 . S2CID 17716908. 
Retrieved from " https://en.wikipedia.org/w/index.php?title=K-anonymity&oldid=1352678854"
Categories:
Data anonymization techniques
Privacy
Hidden categories:
Articles with short description
Short description is different from Wikidata
All Wikipedia articles needing clarification
Wikipedia articles needing clarification from May 2026
This page was last edited on 5 May 2026, at 16:44 (UTC).
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
k-anonymity
9 languages Add topic 
