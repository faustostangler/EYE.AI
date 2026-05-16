---
name: Cloud Pricing Comparison: AWS vs. Azure vs. Google Cloud Platform in 2025 - Cast AI
keywords: (placeholder)
metadata:
  url: https://cast.ai/blog/cloud-pricing-comparison/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Cloud Pricing Comparison: AWS, Azure, GCP - Cast AI
The 2026 State of Kubernetes Optimization Report is here 🎉 Download it to learn how teams are fighting waste.
Skip to content 
Blog
News and insights
Cloud cost optimization
Kubernetes security
Cloud management
LLM cost optimization
Cut your cloud bill
Platform
Platform
Application Performance Automation Platform
AutoScaler
For Karpenter
Advanced
Infrastructure optimization
Kubernetes workload optimization
Kubernetes cost monitoring
GPU optimization – OMNI compute
AI optimization
LLM optimization for AIOps
Application optimization
Database optimization
Solutions
By industry
Automotive
Software & IT
AI & ML Startups
By cloud provider
AWS
GCP
Azure
Oracle Cloud
Customers
Pricing
Resources
DevOps
Docs
Environments
Integrations
Spot Instance Availability Map
Community
APA Hero program
Captain program
Slack community
KubeAuto Day
Learn
Blog
Case studies
Webinars
Events
Reports
Company
About us
Careers
Newsroom
Partner program
Contact us
Book a demo
Sign in
Get started
Cloud cost optimization
Cloud Pricing Comparison: AWS vs. Azure vs. Google Cloud Platform in 2025
This cloud pricing comparison covers storage and compute pricing across top three cloud providers AWS, Azure, and Google Cloud, as well as Oracle.
Laurent Gil
Mar 17, 2026 
Table of contents
Cloud landscape today: What are the unique strengths of AWS, Azure, and Google Cloud Platform?
Billing in AWS vs. Azure vs. Google Cloud Platform
Cloud storage pricing comparison
Compute pricing comparison
AWS vs. Azure vs. Google Cloud Platform: comparing On-Demand pricing
AWS vs. Azure vs. Google Cloud: comparing discounted pricing with a 1-year upfront commitment
AWS vs. Azure vs. Google Cloud: comparing Spot Instances/Preemptible VMs
Optimizing cloud costs is a real-time activity
That's why you need automation to optimize cloud costs
Choosing between AWS, Azure, Google Cloud Platform, and Oracle can be challenging, whether planning a move to the public cloud or optimizing your cloud project.
They all offer flexible compute, storage, and networking along with everything engineers love about the cloud: self-service, instant provisioning, and autoscaling.
However, these providers often differ in areas that may have a massive impact on your cloud bill.
Selecting one vendor over another comes down to knowing what your teams, applications, and workloads need. It's essential to fully understand your requirements before exploring the cloud landscape.
This cloud pricing comparison covers storage and compute pricing across the top three cloud providers AWS, Azure, and Google Cloud, as well as Oracle, to show you the nuanced differences between them.
Cloud landscape today: What are the unique strengths of AWS, Azure, and Google Cloud Platform?
AWS
Companies choose to build their applications on AWS because of its breadth and depth of services. The rich array of tools, including databases, analytics, management, IoT, security, and enterprise applications, makes AWS the right solution for many teams. No wonder AWS has the most significant slice of the cloud market.
Azure
According to one survey, Azure adoption slightly surpasses AWS: 80% Azure vs. 78% AWS. Azure offers various services for enterprises, and Microsoft's longstanding relationship with this segment makes it an easy choice for some customers. Azure, Office 365, and Microsoft Teams enable organizations to provide employees with enterprise software while leveraging cloud computing resources.
Google Cloud Platform
Azure and AWS have strong machine-learning capabilities. However, the Google Cloud Platform stands out thanks to its almost limitless internal research and expertise – the magic that has been powering the search engine giant for years.
What makes GCP different is its role in developing various open-source technologies. We're talking especially about containers and Google's central role in building Kubernetes for orchestration and Istio service mesh, which are practically industry-standard technologies today.
Google's innovation culture lends itself well to startups and companies prioritizing such approaches and technologies.
Billing in AWS vs. Azure vs. Google Cloud Platform
In addition to per-minute billing, AWS, Azure, and Google Cloud support per-second billing for various services. AWS first introduced per-second billing in 2017 for EC2 Linux-based instances and EBS volumes – but today, it applies to many other services.
Per-second billing works with a minimum 60-second limit in AWS. Azure allows per-second charges on its cloud platform, but this billing model isn't available for all instances – only some container-based ones.
Google Cloud followed AWS in introducing per-second billing and now offers it for more than just Linux instances. This form of billing applies to all VM-based instances.
Cloud storage pricing comparison
How do these major cloud providers differ in terms of storage pricing?
Here's a comparison of prices in similar regions: AWS US East (Northern Virginia), Azure East US, and Northern Virginia (us-east4) in Google Cloud Platform. 
These cloud service providers compete closely and set similar price ranges for storage services, with Azure being the most cost-effective alternative. However, check out other cost dimensions before choosing a storage service, such as data transfer or operations charges.
Also, pay attention to the provider's approach to pricing changes. Google Cloud Platform recently introduced significant price increases across various core storage services, which may affect other services and cloud providers.
Compute pricing comparison
Compute often racks up the most in a cloud bill but presents the greatest opportunity for cost optimization. That's why it's an essential element in every cloud pricing comparison.
We prepared this case study to show the incredible impact optimizing compute costs can have on your bottom line.
Comparing cloud pricing: our example setup
To better understand the pricing differences, we will compare virtual machines within similar regions and with the same operating system.
The services analyzed are:
AWS – Amazon Elastic Compute Cloud (EC2)
Azure – Virtual Machines
Google Cloud Platform – Compute Engine
Oracle – Virtual Machines
Our example setup:
Region: AWS US East (Northern Virginia), Azure East US, and Northern Virginia (us-east4) in Google Cloud Platform.
Operating System: Linux.
Number of vCPUs: 4.
Types of instances/VMs analyzed:
General purpose
Compute optimized
We picked instances with four vCPUs and similar memory (the only exception is the compute-optimized machine from the Google Cloud Platform).
Here are the instances/VMs we selected for our cloud pricing comparison: 
AWS vs. Azure vs. Google Cloud Platform: comparing On-Demand pricing
Here's the hourly On-Demand pricing for these cloud services across AWS, Azure, and Google Cloud Platform.
Cloud pricing based on On-Demand rates
General purpose 
Compute optimized 
Takeaways:
While Azure offers the most expensive general purpose instance analyzed, it offers a good deal on the compute-optimized instance example.
Google Cloud Platform offers the highest price for compute optimized instances, but this machine has double the RAM of AWS, Azure, and Oracle alternatives.
x86 vs. Arm: impact on pricing
In the 2025 Kubernetes Cost Benchmark Report, we compared hourly Spot and On-Demand pricing for x86 and Arm CPUs across AWS, GCP, and Azure. 
Our comparison showed some interesting trends:
Arm CPUs consistently offer better value than x86 CPUs in both On-Demand and Spot pricing. This presents a significant cost-saving opportunity for those able to leverage Arm architecture.
Azure stands out with the largest pricing gap between x86 and Arm CPUs—65% for On-Demand and 69% for Spot. For flexible, cost-sensitive workloads, Arm on Azure is particularly attractive.
If you want to trim cloud costs, Arm CPUs are worth considering, especially when using Spot Instances.
AWS vs. Azure vs. Google Cloud: comparing discounted pricing with a 1-year upfront commitment
All three providers offer price discounts if you commit to using them for at least one year. This pricing model is called Reserved Instances in AWS, Reserved Savings in Azure, and Committed Use Discounts in Google Cloud.
The following tables compare the discounted pricing among AWS, Azure, and Google Cloud cloud services with a one-year commitment period with an all-upfront payment.
Cloud pricing with a 1-year commitment
General purpose 
Compute optimized 
Takeaways:
AWS and Azure offer similar discount rates for general purpose instances with a one-year commitment.
Google Cloud Platform offers the biggest discounts on both general purpose and compute–optimized instances—still, it's not the cheapest option. Note that the compute-optimized GCP instance we picked has 16 GB RAM, not 8 GB like the other instances.
If you're unsure how Reserved Instances work and whether they bring discounts, take a look here: Do AWS Reserved Instances and Savings Plans really reduce costs?
AWS vs. Azure vs. Google Cloud: comparing Spot Instances/Preemptible VMs
Another way to get discounts and reduce your cloud bill is to take advantage of capacity currently not used by anyone else. Cloud providers sell excess capacity at incredible discounts. AWS Spot Instances offer up to 90% off the On-Demand rates, and Preemptible VMs in Google can be even 80% cheaper than regular ones.
Here's a quick overview of the potential savings you can get for these instances in the US East (Northern Virginia) region:
Cloud pricing with Spot Instances/Preemptible VMs
General purpose 
*Note that we changed the machine type to a similar one with 4 vCPU and 8 GB RAM because Azure's machines in Bs-series aren't available as Spot Instances!
Compute optimized 
Takeaways:
Azure offers the greatest discounts for both general and compute-optimized instances.
Oracle offers Preemptible VMs at a flat 50% discount.
To take advantage of Spot Instances, you must ensure your application can handle interruptions. How? Here's a step-by-step guide: Spot Instances: How to reduce AWS, Azure, and GCP costs by 90%
Optimizing cloud costs is a real-time activity
Cloud providers change Spot Instance prices regularly. According to the 2025 Kubernetes Cost Benchmark Report, Azure and GCP offer more predictable pricing, with changes happening only a few times a month.
On average, GCP sees a new price every three months (0.35 times/month), and Azure changes prices slightly less than once a month (0.76 times/month).
AWS, on the other hand, is much more dynamic. Spot prices fluctuate continuously, and AWS averages 197 distinct monthly price changes for GPU and non-GPU instances.
This means that teams relying on Spot Instances need to monitor prices and be flexible enough to change their setups. 
That's why you need automation to optimize cloud costs
Choosing the best compute instance for your workload is never a one-time exercise. Your requirements may change, and cloud providers may increase their prices. Having an automation solution make these decisions in real-time is a game-changer.
For example, the video creation platform PlayPlay used automation to move its Kubernetes workloads to more cost-efficient compute instances. The screenshot below illustrates a rebalancing operation in which Cast AI replaced 13 nodes without impacting service availability, saving PlayPlay $1,430 monthly. 
If you're running your applications on Kubernetes, you can start with a free cluster savings report and see the instance type and resource amount Cast AI would automatically implement if it managed your cluster.
Kubernetes cost optimization
Monitor organization-wide and cluster-level resource spending. Automate resource allocation and scale instantly with zero downtime.
Learn more 
Cast AI › Blog › Cloud Pricing Comparison: AWS vs. Azure vs. Google Cloud Platform in 2025
Cut Kubernetes costs with automation
Rightsize workloads
Reduce overprovisioning
Scale clusters efficiently
See how it works
Start free
More articles
 Cloud management, Engineering
How In-Place Pod Resizing Works in Kubernetes and Why Cast AI Makes It Better
Kubernetes 1.33+ introduces in-place pod resizing, allowing teams to change pod CPU and memory without…
 Cloud cost optimization
Only 13% of Provisioned CPUs End Up Being Used
We're thrilled to share our 2024 Kubernetes Cost Benchmark Report! 🎉 The annual report is…
 News and insights
Azure Cost Calculator: How to Estimate Azure Costs Accurately
Estimating Azure costs can be complex, with variables like scaling, storage, and pricing plans quickly… 
4.8/5 50+ reviews
Boost Kubernetes performance, security, and cost optimization
Start free
Book a demo 
Cast AI is the leading Application Performance Automation platform, enabling customers to cut cloud costs, improve performance, and boost productivity.
Facebook
GitHub
Slack Community
LinkedIn
X    
Solutions
Kubernetes cluster optimization
Kubernetes cost monitoring
Kubernetes workload optimization
LLM optimization for AIOps
Database optimization
OMNI Compute for AI
Cast AI For Karpenter
Resources
Blog
Events
Webinars
Reports
Customer stories
Documentation
Release notes
Pricing
Company
About us
Careers
Contact us
Slack community
Newsroom
Brand assets
Partner program
APA Hero program
Referral program  
© 2026 CAST AI Group Inc.
Privacy policy
Terms of service
Customer data processing
EU Projects
Information security policy
Try it out
Book a demo
Book a demo
See how Cast AI can transform your cloud-native operations and maximize Kubernetes cost savings.
First name(Required)
Last name(Required)
Work email(Required)
Job title(Required)
Country(Required)
Select country
United States
Canada
Israel
United Kingdom
India
Germany
Albania
Algeria
Andorra
Angola
Anguilla
Antarctica
Antigua and Barbuda
Argentina
Armenia
Aruba
Australia
Austria
Azerbaijan
Bahamas
Bahrain
Bangladesh
Barbados
Belarus
Belgium
Belize
Benin
Bermuda
Bhutan
Bolivia
Bonaire
Bosnia and Herzegovina
Botswana
Bouvet Island
Brazil
British Indian Ocean Territory
Brunei Darussalam
Bulgaria
Burkina Faso
Burundi
Cambodia
Cameroon
Cayman Islands
Central African Republic
Chad
Chile
China
Christmas Island
Cocos (Keeling) Islands
Colombia
Comoros
Congo
Congo,
Cook Islands
Costa Rica
Croatia
Cuba
Curaçao
Cyprus
Czech Republic
Côte d'Ivoire
Denmark
Djibouti
Dominica
Dominican Republic
Ecuador
Egypt
El Salvador
Equatorial Guinea
Eritrea
Estonia
Ethiopia
Falkland Islands (Malvinas)
Faroe Islands
Fiji
Finland
France
French Guiana
French Polynesia
French Southern Territories
Gabon
Gambia
Georgia
Ghana
Gibraltar
Greece
Greenland
Grenada
Guadeloupe
Guam
Guatemala
Guernsey
Guinea
Guinea-Bissau
Guyana
Haiti
Heard Island and McDonald Islands
Holy See
Honduras
Hong Kong
Hungary
Iceland
Indonesia
Iran
Iraq
Ireland
Isle of Man
Italy
Jamaica
Japan
Jersey
Jordan
Kazakhstan
Kenya
Kiribati
Kuwait
Kyrgyzstan
Lao People's Democratic Republic
Latvia
Lebanon
Lesotho
Liberia
Libya
Liechtenstein
Lithuania
Luxembourg
Macao
Madagascar
Malawi
Malaysia
Maldives
Mali
Malta
Marshall Islands
Martinique
Mauritania
Mauritius
Mayotte
Mexico
Micronesia
Moldova
Monaco
Mongolia
Montenegro
Montserrat
Morocco
Mozambique
Myanmar
Namibia
Nauru
Nepal
Netherlands
New Caledonia
New Zealand
Nicaragua
Niger
Nigeria
Niue
Norfolk Island
Macedonia
Norway
Oman
Pakistan
Palau
Palestine
Panama
Papua New Guinea
Paraguay
Peru
Philippines
Pitcairn
Poland
Portugal
Qatar
Romania
Russian Federation
Rwanda
Réunion
Saint Barthélemy
Saint Helena, Ascension and Tristan da Cunha
Saint Kitts and Nevis
Saint Lucia
Saint Martin (French part)
Saint Pierre and Miquelon
Saint Vincent and the Grenadines
Samoa
San Marino
Sao Tome and Principe
Saudi Arabia
Senegal
Serbia
Seychelles
Sierra Leone
Singapore
Sint Maarten (Dutch part)
Slovakia
Slovenia
Solomon Islands
Somalia
South Africa
South Georgia and the South Sandwich Islands
South Korea
South Sudan
Spain
Sri Lanka
Sudan
Suriname
Svalbard and Jan Mayen
Sweden
Switzerland
Syrian Arab Republic
Taiwan
Tajikistan
Tanzania
Thailand
Timor-Leste
Togo
Tokelau
Tonga
Trinidad and Tobago
Tunisia
Turkmenistan
Turks and Caicos Islands
Tuvalu
Turkey
US Minor Outlying Islands
Uganda
Ukraine
United Arab Emirates
Uruguay
Uzbekistan
Vanuatu
Venezuela
Viet Nam
Virgin Islands, British
Wallis and Futuna
Western Sahara
Yemen
Zambia
Zimbabwe
Aland Islands
State(Required)
Alabama
Alaska
American Samoa
Arizona
Arkansas
California
Colorado
Connecticut
Delaware
District of Columbia
Florida
Georgia
Guam
Hawaii
Idaho
Illinois
Indiana
Iowa
Kansas
Kentucky
Louisiana
Maine
Maryland
Massachusetts
Michigan
Minnesota
Mississippi
Missouri
Montana
Nebraska
Nevada
New Hampshire
New Jersey
New Mexico
New York
North Carolina
North Dakota
Northern Mariana Islands
Ohio
Oklahoma
Oregon
Pennsylvania
Puerto Rico
Rhode Island
South Carolina
South Dakota
Tennessee
Texas
Utah
U.S. Virgin Islands
Vermont
Virginia
Washington
West Virginia
Wisconsin
Wyoming
Armed Forces Americas
Armed Forces Europe
Armed Forces Pacific
Canada State(Required)
Alberta
British Columbia
Manitoba
New Brunswick
Newfoundland and Labrador
Nova Scotia
Ontario
Quebec
Saskatchewan
India State(Required)
Andaman and Nicobar
Andhra Pradesh
Arunachal Pradesh
Assam
Bihar
Chandigarh
Chhattisgarh
Dadra and Nagar Haveli
Delhi
Goa
Gujarat
Haryana
Himachal Pradesh
Jammu and Kashmir
Jharkhand
Karnataka
Kerala
Ladakh
Lakshadweep
Madhya Pradesh
Maharashtra
Manipur
Meghalaya
Mizoram
Nagaland
Odisha
Puducherry
Punjab
Rajasthan
Sikkim
Tamil Nadu
Telangana
Tripura
Uttar Pradesh
Uttarakhand
West Bengal
Daman and Diu
Germany State(Required)
Berlin
Brandenburg
Bremen
Hamburg
Hesse
Mecklenburg-Vorpommern
Lower Saxony
North Rhine-Westphalia
Saxony-Anhalt
Saxony
Schleswig-Holstein
Thuringia
Baden-Württemberg
Bavaria
Rhineland-Palatinate
Saarland
UK Location(Required)
Aberdeen City
Abergavenny
Aberystwyth
Abingdon
Accrington
Addlestone
Alderley Edge
Alnwick
Altrincham
Amersham
Andover
Ashby de la Zouch
Ashford
Aylesbury
Ayr
Bagshot
Banbury
Barnsley
Basildon
Basingstoke
Bath
Bedford
Belfast
Bescot
Beverley
Birmingham
Blackpool
Blaenau Gwent
Bolton
Borehamwood
Bracknell
Bradford
Brentford
Brentwood
Bridgwater
Brighton
Bristol
Burnley
Bury
Bury Saint Edmunds
Caerdydd
Camberley
Cambridge
Cardiff
Carlisle
Ceredigion
Cheadle
Chelmsford
Cheltenham
Chertsey
Chester
Chichester
Chippenham
Christchurch
Cirencester
Clifton
Coalville
Colchester
Cossington
Coventry
Craigavon
Crawley
Crewe
Cumbria
Datchet
Denham
Derby
Derbyshire
Derry
Didcot
Diss
Doncaster
Dorchester
Dundee
Dunstable
Durham
Eastleigh
Edinburgh
Egham
Elland
Ely
Enderby
Epsom
Ewell
Exeter
Farnborough
Farnham
Feltham
Fleet
Folkestone
Frimley
Glasgow
Gloucester
Gloucestershire
Godalming
Goole
Goonhavern
Goring-by-Sea
Great Malvern
Guildford
Gurgaon
Halton
Hampshire
Handforth
Harpenden
Harrogate
Havant
Haywards Heath
Hemel Hempstead
Hereford
Hertford
Hertfordshire
High Wycombe
Hinckley
Hook
Horley
Horsforth
Huddersfield
Hungerford
Huntingdon
Hythe
Inverness
Ipswich
Keele
Kent
Kingston upon Hull
Knowsley District (B)
Krakow
Lancashire
Lancaster
Larbert
Lasswade
Leeds
Leicester
Leicestershire
Leominster
Lewes
Lichfield
Lincoln
Liverpool
Livingston
Loughborough
London
Lowestoft
Luton
Maidenhead
Maidstone
Malmesbury
Manchester
Marlow
Melton Mowbray
Milton Keynes
Mold
Motherwell
Nelson
Newbury
Newcastle upon Tyne
Newport
Newry
Newtownabbey
Normanton
North Yorkshire
Northampton
Norwich
Nottingham
Oakham
Oxford
Oxfordshire
Paisley
Perth
Peterborough
Petersfield
Pontypridd
Poole
Preston
Purfleet
Reading
Redditch
Redhill
Reigate
Renfrewshire
Rickmansworth
Rochdale
Rode
Royal Leamington Spa
Royal Tunbridge Wells
Royston
Runcorn
Saint Albans
Sale
Salford
Sandwell
Sevenoaks
Sheffield
Shirebrook
Shrewsbury
Skipton
Slough
Smethwick
Snodland
Solihull
Somerset
Southampton
Southport
Stafford
Staffordshire
Staines-upon-Thames
Stevenage
Stockton-on-Tees
Stoke-on-Trent
Stone
Stroud
Suffolk
Sunderland
Surrey
Swindon
Taunton
Telford and Wrekin
Thames Ditton
Trafford
Trowbridge
Truro
Twyford
Wakefield
Walsall
Warrington
Warwick
Warwickshire
Welwyn Garden City
West Bromwich
West End
West Malling
Weston-super-Mare
Weybridge
Winchester
Windermere
Windsor
Witney
Wokingham
Worcester
Worcestershire
Yate
York
Which Kubernetes cloud services do you use?(Required) [-] EKS
EKS [-] GKE
GKE [-] AKS
AKS [-] ROSA
OpenShift on AWS [-] migration
Migrating to Kubernetes
How did you hear about us?(Required)
By submitting this form, you acknowledge and agree that Cast AI will process your personal information in accordance with the Privacy Policy.
This field is hidden when viewing the form
UTM Source Current cast.ai
This field is hidden when viewing the form
UTM Medium Current direct
This field is hidden when viewing the form
UTM Campaign Current
This field is hidden when viewing the form
UTM Term Current
This field is hidden when viewing the form
UTM Content Current
This field is hidden when viewing the form
Ref ID Current
This field is hidden when viewing the form
gclid Current
This field is hidden when viewing the form
Current URL https://cast.ai/blog/cloud-pricing-comparison/ Select time and date  
Want to ask us a question?
Our AI can help you get answers quickly.
Ask me Anything
Notifications   
