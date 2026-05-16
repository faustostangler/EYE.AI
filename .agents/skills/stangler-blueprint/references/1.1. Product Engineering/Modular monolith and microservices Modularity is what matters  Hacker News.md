---
name: Modular monolith and microservices: Modularity is what matters | Hacker News
keywords: (placeholder)
metadata:
  url: https://news.ycombinator.com/item?id=45810482
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Modular monolith and microservices: Modularity is what matters | Hacker News 
Hacker News new | past | comments | ask | show | jobs | submit
login
kstrauser 6 months ago | next [–]
I feel like there are competent, competing visions talking past each other on the subject. There's kind of a spectrum:
Everything is a monolith. Frontend, backend, dataplane, processing, whatever: it's all one giant, tightly coupled vertically-scaled ball of mud. (This is insane.)
Everything is a monolith, but parts are horizontally scaled. Imagine a big Flask app where there are M frontend servers, and N backend async task queue processors, all running the same codebase but with different configurations for each kind of deployment. (This is perfectly reasonable.)
There are a small number of separate services. That frontend Flask server talks to a Go or Rust or Node or whatever backend, each appropriate to the task at hand. (This is perfectly reasonable.)
Everything is a separate service. There are N engineers and N+50% servers written in N languages, and a web page load hits 8 different internal servers that do 12 different things. The site currently handles 23 requests per day, but it's meant to vertically scale to Google size once it becomes popular. Also, everything is behind a single load balancer, but the principle engineer (who interned at Netflix) handwaves it away a "basically infinitely scalable". (This is insane.)
These conversations seem to devolve into fans of 1 and 4 arguing that the other is wrong. People in 2 and 3 make eye contact with each other, shrug, and get back to making money.  
nine_k 6 months ago | parent | next [–]
Logical separation, the modules, is what allows to preserve developer sanity. Physical separation, the (micro-)services is what allows you to ship things flexibly. Somewhere on the distant high end, microservices also play a role in enabling scalability to colossal scales, only needed by relatively few very huge companies.
The key problem of developing a large system is allowing many people to work on it, without producing a gridlock. A monolith, by its nature, produces a gridlock easily once a sufficient number of people need to work on it in parallel. Hence modules, "narrow waist" interfaces, etc.
But the key thing is that "you ship your org chart" 1. Modules allow different teams to work in parallel and independently, as long as the interfaces are clearly defined. Modules deployed separately, aka services, allow different teams to ship their results independently, as long as they remain compatible with the rest of the system. Solving these organizational problems is much more important for any large company than overcoming any technical hurdles.
 
bluGill 6 months ago | root | parent | next [–]
If you are willing to pay a price. Once you allow things to ship separately are are locked into the API Hyrum's law mistakes of the past until you can be 100% that all uses of the old thing are gone in the real world. This is often hard. By shipping things together you can verify they all work together before you ship, and more importantly when you realize something was a mistake there is a set time where you can say "that is no longer allowed" (this is a political problem - sometimes they will tell you no we won't change, but at least you have options).
Everything else is spot on, but I am feeling enough pain from mistakes made 15 years ago (that looked reasonable at the time!) such that I feel the need to point it out.  
xorcist 6 months ago | root | parent | prev | next [–]
Scale? At what "scale" runs Linux, perhaps the most well known monolith software ever?
(And also the subject of perhaps the most well studied flamew^Wdiscussion about mono- versus microservice architecture.)
It only runs most of all servers and most of all the mobile terminals in the world. Where is that distant higher end, where microservices unlock colossal scale, exactly?
Architecture matters. Just not always the way you think. But it serves as catnip for everyone who loves a good debate. Anyone who gets tired of writing code can always make a good living writing about software architecture. And good for them. There's a certain artistry to it, and they have diagrams and everything.  
nine_k 6 months ago | root | parent | next [–]
Linux can scale to a machine with hundreds of cores; the largest is 1000+ cores IIRC. It's because it scales horizontally, in a way, and can run kernel threads on multiple cores. But a NUMA configuration feels increasingly like a cluster the more cores you add, just because a single-memory-bus architecture can't scale too much; accessing a far node's memory introduces much more latency that accessing local RAM.
It's easy to run a thousand independent VMs. It's somehow more challenging to run a thousand VMs that look externally as one service, and can scale down to 500 VMs, or up to 2000 VMs, depending on the load. It's really quite challenging to scale a monolith app to service tens of millions of users on one box, without horizontal scaling. But it definitely can be done, see the architecture of Stackoverflow.com. (Well, this very site is served by a monolith, and all logged-in users are served by a single-threaded monolith, unless they rewrote the engine. Modern computers are absurdly powerful.)  
ivanjermakov 6 months ago | parent | prev | next [–]
I also laugh at 30+ microservice projects where almost every service connects to a single oracle database with no sharding/partitioning. Inb4 aws dynamodb outage.  
connicpu 6 months ago | root | parent | next [–]
The number of services at my job that are just grpc wrappers for a database with endpoints that are only accessed by services that have their own connections open to the same database has been driving me insane.  
4ndrewl 6 months ago | root | parent | prev | next [–]
Isn't that a microservices 101? No shared databases?  
kstrauser 6 months ago | root | parent | next [–]
An important and common exception would be for performance critical reasons, as mentioned elsewhere. Say most of your code's in Python, but you rewrote parts in a faster language. There you're not necessaryily separating them for isolation or encapsulation purposes. It'd be as much of a mistake to force them to hit separate DBs.  
xorcist 6 months ago | root | parent | prev | next [–]
Wasn't it two pizza teams and using the right tools for the right job?  
Spivak 6 months ago | parent | prev | next [–]
Once you open the door to 3 it's a lot harder to stop the slide into 4. Devs love greenfield codebases and once that's an acceptable way to solve a problem they'll reach for it more and more. Especially if your setup has low friction to "just" spinning up a new service.  
kstrauser 6 months ago | root | parent | next [–]
True, and some org-level discipline is important here. I'm all for polyglot architectures, but only for reasonably small values of poly. Like if you wrote the frontend in Python, but really some performance critical Rust, fine. Or maybe you merged with another shop that already had a bunch of Go, far out.
Resist the urge to roll out that Prolog-driven inference service that your VP Eng vibe coded after reading an article about cool and strange programming languages.  
bluGill 6 months ago | root | parent | next [–]
I generally think the right rule of thumbs is about 10 languages - but that includes the build system, CI system... Not everyone needs to know all 10, but you need a good set of options for that that need it. Most people should be using the same 2 or 3 of that 10, but a few teams need to do something weird and so need the other options that are overall rarely used.  
kstrauser 6 months ago | root | parent | next [–]
That's very scale-dependent. I can imagine why a FAANG might need 10 languages, between Python APIs and Java services and Rust and Go things and a Node system and a smattering of Perl and some ETL in Scala and BI in C#, etc. A startup with less than 50 employees almost certainly does not.
Maybe I'd compromise on no more than, say, 2-3 language per department. If you're small enough that "engineering" is 1 department, then there you go: choose wisely. If you have a whole department for frontend, and one for backend, and one for ops, and one for analytics, etc., then you can somewhat treat those as encapsulation boundaries and have more flexibility.  
svieira 6 months ago | root | parent | next [–]
Depends on what you consider a language. There are a lot of DSLs out there and once you add a couple of configuration files for Jenkins / Git{Hub, Lab} / Bazel / Buck and Vagrant / Docker / Bash and so on you're already at 5 languages and you haven't even added the lethal trifecta of HTML+CSS+JS for your web front-end or Swift+Kotlin if you only want to roll on mobile.  
kstrauser 6 months ago | root | parent | next [–]
Yeah, that's a rabbit hole to be sure. I personally only count languages that you write a non-trivial amount of production executable code in. Examples of things I wouldn't count: HTML and CSS, JS in the browser, Bash used in the build system. If you wrote your webserver in Bash for some wild reason, it's included. Mise and Just and Makefiles aren't.  
bluGill 6 months ago | root | parent | next [–]
If you exclude HTML/CSS/JS/Makefiles that means you are giving your people an excuse to make a mess of them. You have to count everything. You can say that HTML/CSS/JS are all one since they are tightly coupled and you have to know all 3 if that is what it takes to get under the 10 limit, but you should make it clear you are breaking the spirit of the rule to do that just because of an external factor - and you are not happy about that.
If you write even one line of something you need at least one person who is an expert and takes responsibility to ensure the code written in the language is good.  
bluGill 6 months ago | root | parent | prev | next [–]
Not department, project. If you can get to 10 across a whole company that would be good, but project unreasonable in the largest companies. Even with only 50 people in a startup staying under 10 will need some effort as there is always some cool new toy. (don't let them replace languages with frameworks either)
This is important. Sometimes you have multiple departments working on a single project (a large embedded system). Sometimes a department will work on multiple projects - the department needs to be careful that people don't need to know too many languages (which is hard - if often make sense for a department to develop for all apps, so you have to know the language of iPhone, android, Window)
People should stay mostly in their lanes (department), but they should have the ability to cross to others when that is needed instead of just throwing APIs over a wall and accusing the other side of using it wrong.  
solumos 6 months ago | parent | prev | next [–]
1 Could maybe make sense for a proof of concept, but realize that you're probably throwing it away (sooner better than later).
Start with 2, and think about the separation of deployable targets and shared libraries/plugins. You can eventually carve out separate infra for deployable targets when resource contention becomes a problem (e.g. DB load is affecting unrelated services)
3 is rarely the right first step for a small team
4 is never the right first step for a small team  
notfed 6 months ago | parent | prev | next [–]
Why is #1 insane (no horizontal scaling) if you only have 23 requests per day?  
default-kramer 6 months ago | root | parent | next [–]
It's not insane. The best codebase I ever inherited was about 50kloc of C# that ran pretty much everything in the entire company. One web server and one DB server easily handled the ~1000 requests/minute. And the code was way more maintainable than any other nontrivial app I've worked on professionally.  
geodel 6 months ago | root | parent | next [–]
I work(ed) on something similar in Java. And it still works quite well. But last few years are increasingly about getting berated by management on why things are not modern Kubernetes/ micro services based by now.  
Spivak 6 months ago | root | parent | prev | next [–]
I feel like people forget just how fast a single machine can be. If your database is SQLite the app will be able to burn down requests faster than you ever thought possible. You can handle much more than 23 req/day.  
kstrauser 6 months ago | root | parent | next [–]
In the not-too-distant past I was handling many thousands of DB-backed requests per hour in a Python app running plain PostgreSQL.
You can get really, really far with a decent machine if you mind the bottlenecks. Getting into swap? Add RAM. Blocked by IO? Throw in some more NVMe. Any reasonable CPU can process a lot more data than it's popular to think.  
bluGill 6 months ago | root | parent | next [–]
Anytime someone talks about scale I remember just how much data the low mhz CPUs used to process. Sure the modern stuff has nicer UIs, but the UIs of the past where not bad, and we a lot of data was processed. Almost nobody has more data than what the busiest 200mhz CPU on 1999 used to handle alone, so if you can't do it that isn't a scaling problem it is a people problem. (don't get me wrong, this might be a good trade off to make - but don't say you couldn't do it on a single computer)  
kstrauser 6 months ago | root | parent | prev | next [–]
It's not. It's kind of bonkers to pursue that when you have a lot of traffic, but it's a perfectly sane starting point until you know where the pain points are.
In general, the vast number of small shops chugging away with a tractably sized monolith aren't really participating in the conversation, just idly wondering what approach they'd take if they suddenly needed to scale up.  
bunderbunder 6 months ago | root | parent | next [–]
I'm not even sure it's bonkers if you have a lot of traffic. It depends on the nature of the traffic and how you define "a lot". In general, though, it's amazing how low latency a function call that can handle passing data back and forth within a memory page or a few cache lines is compared to inter-process communication, let alone network I/O.
The corollary to that is, it's amazing how far you can push vertical scaling if you're mindful of how you use memory. I've seen people scale single-process, single-threaded systems multiple orders of magnitude past the point where many people would say scale-out is an absolute necessity, just by being mindful of things like locality of reference and avoiding unnecessary copying.  
notatoad 6 months ago | root | parent | prev | next [–]
if you have 23 requests per day the insane thing is wondering whether or not you've chosen the correct infrastructure, becuase it really doesn't matter.
do whatever you want, you've already spent more time than it's worth considering it.  
simianwords 6 months ago | root | parent | prev | next [–]
most productive applications have more RPS than that. we should ideally be speaking about how to architect productive applications and not just mocks and prototypes  
bkanuka 6 months ago | root | parent | prev | next [–]
Don't know if this is sarcasm or not. If you have 23 req/day, then there's no tech problem to solve. Whatever you have is good enough, and increasing traffic will come from solving problems outside tech (marketing, etc)  
mytailorisrich 6 months ago | parent | prev | next [–]
"Tightly coupled" is the sticking point. Tight coupling is bad architecture whether you have a monolith or microservices, which is the general point of the article.  
abalone 6 months ago | parent | prev | next [–]
Or there's 3.5: separate services where it makes sense, but not necessarily small in number. "Makes sense" would entail things like, does it have distinct resource utilization or scaling characteristics, or do you want to enable your service to more gracefully degrade if that module becomes unavailable.
(This is basically the definition of 3 without the implication that it will be rare.)
As opposed to 4 which is about proactively breaking everything down into the smallest possible units on the expectation that the added complexity is always worth it.  
Sammi 6 months ago | parent | prev | next [–]
Lots and lots and lots of people make no. 1 work. The issue isn't whether it is a monolith or not. The issue is whether it has good or poor internal architecture.
No 1 can scale to 1000 requests per second. One machine, one db, one application. It is totally doable because so many people do it.
It's just not sexy and doesn't pad you resume. It's boring stuff that just works.  
foobarian 6 months ago | root | parent | next [–]
I wish our app only got 1krps. Maybe these conversations should be bucketed by the traffic volume people are handling - it really leads to completely different designs.  
383toast 6 months ago | parent | prev | next [–]
you can get pretty far with (2) and (3), haven't really understood the need for (4) unless you're FAANG  
amarant 6 months ago | root | parent | next [–]
4 doesn't really work for serious big load applications either: nobody will be able to understand the codebase. You want 3.
During my days at mojang we did some variation of 3. We had ~250k requests/second, and handled it just fine (we had 4 nines availability forever chasing the fifth, and sub 20ms response times)
I think even among those who do see big loads, few see as much malicious traffic as we did. This was one of the arguments for a micro service architecture. If a DDOS took down our login service, already logged in players would be unaffected (until their tokens expired anyway)
Well, that was a long winded way to say, 3 is about as micro as you want to go. I've only seen 4 done once, and that site actually went under whenever they had more than 30 request per minute. (Admittedly they had made a bunch of other really bad decisions not covered in the above description, but having ~30 services on a team of 12, in order to handle a handful of requests per hour was certainly their biggest mistake.)  
yearolinuxdsktp 6 months ago | root | parent | prev | next [–]
Facts! #1 is not insane as long as you keep your internals modular (all-in-one deployment doesn't mean ball of mud... you can avoid putting service calls into your domain objects or your data plane code). And you can go from #1 to #2 once you see the need and slice the services out that need it (such as decoupling async batch processing into a 2nd service that shares the domain and the data plane code and does not include the front-end).  
kstrauser 6 months ago | root | parent | next [–]
In fairness, it being a tightly coupled ball of mud is part of my definition of #1 here. What you describe is basically #2 waiting to happen, just that no one's needed to do it yet.  
yearolinuxdsktp 6 months ago | root | parent | next [–]
Makes sense, I agree then that #1 as you exactly define it is insane.  
ecshafer 6 months ago | prev | next [–]
I feel like this misses too much real world context and caveats.
What is the problem with Monoliths? Nothing. Until there is. The problem with monoliths is when you have a million LoC Java application that is on Java 6, and will take months of work to get up to date, take 20 minutes to load on a dev machine, starts to fail because its getting too big for a dev machine to handle, can't bring in any new dependencies because of how old the Java version is, and has an old bespoke Ant + Maven + Jenkins + Bash + Perl build and deploy system that has been built up over the last 30 years.
So what do you do? Breaking off pieces of the code into microservices that can run on a new Spring boot and can run on a newer nice IaC set up is an easy win. Sure you basically have a microlith, but it increases your dev velocity.
I think Monolith issues are typically a symptom of a few other things: 1. accumulated deferred maintenance and tech debt 2. Inadequate developer tooling 3. Inadequate CICD tooling 4. Rarely scale until you really start to hit the size of like Google, Uber, Facebook, etc.  
netdevphoenix 6 months ago | parent | next [–]
a million LoC Java application that is on Java 6 -> Congrats, now you have two half a million LoC Java application on two different Java versions. And if the set up is like most apps, you will likely need both running to debug most issues because most issues happen at the system to system interface
take 20 minutes to load on a dev machine -> that is fair enough, I have only ever seen an app that takes that long on a modern machine once, most shops doing micro services don't have apps that big
has an old bespoke Ant + Maven + Jenkins + Bash + Perl build and deploy system that has been built up over the last 30 years -> you can have the same problem on a micro service architecture, you can actually have that problem multiplied by 10 and now you can spend a whole sprint updating dependencies. Fun!
Breaking off pieces of the code into microservices that can run on a new Spring boot and can run on a newer nice IaC set up is an easy win -> You conveniently forget to mention the additional team to fix issues related to system to system communication  
tracker1 6 months ago | root | parent | next [–]
Definitely true... Not to mention when your entire orchestration becomes too big to run anything locally, that's where the real fun and complexity starts. There's definitely such a thing as too many micro-services, or too micro for that matter...  
simianwords 6 months ago | root | parent | prev | next [–]
wrong. well architected services would have a good interface and problems rarely span multiple services.
this is no un-nuanced. the point is if you have decomposed the codebase into smaller ones - migrations are easier.  
netdevphoenix 6 months ago | root | parent | next [–]
Surely if your monolith codebase is good enough, migrations will be easy too. And a well architected system can be run on a single machine. If you don't believe me, try running windows 95 on your machine. These are True Scotsman fallacies that devs often use to justify whatever paradigm/philosophy they believe in. Most code in the wild is not perfectly designed or if it is, it doesn't stay so for long. Paradigms that rely on optimal conditions to work decently aren't universally useful imo.
If your car only works on pristine, smooth roads, it's not a good car, no matter how many cool features it has or how fast you can ride it.  
jimbokun 6 months ago | root | parent | prev | next [–]
You are focusing on the hyperbole to ignore the basic point: being unable to change, build and release different parts of the code independently can and eventually will bring your development velocity to a crashing halt.  
netdevphoenix 6 months ago | root | parent | next [–]
Sure you can release quickly, but when your whole constellation of services is too big to be run on a local machine, your development velocity will also come to a crashing halt  
Scubabear68 6 months ago | parent | prev | next [–]
I think the big problem no one speaks about is the name "microservices" was incredibly poorly named.
Your design goal should not be "create the smallest service you can to satisfy the 'micro' label". Your design goal should be to create right-sized services aligned to your domain and organization.
The deployment side is of course a red herring. People can and do deploy monoliths with multiple deployments and different endpoints. And I've seen numerous places do "microservices" which have extensive shared libraries where the bulk of the code actually lives. Technically not a monolith - except it really is, just packaged differently.  
mikepurvis 6 months ago | root | parent | next [–]
Another key is that you should always be able to reasonably hack on just one of the "services" at once— everything else should be able to be excluded completely or just run a minimal mock, for example an auth mock that just returns a dummy token.
If you've got "microservices" but every dev still has to run a dozen kubernetes pods to be able to develop on any part of it, then I'm pretty sure you ended up with the worst of both worlds.  
Sohcahtoa82 6 months ago | root | parent | prev | next [–]
A place I worked at years ago did what I effectively called "nano-services".
It was as if each API endpoint needed its own service. User registration, logging in, password reset, and user preference management were each their own microservice.
When I first saw the repo layout, I thought maybe they were just using a bunch of Lambdas that would sit behind an AWS API Gateway, but I quickly learned the horror as I investigated. To make it worse, they weren't using Kubernetes or any sort of containers for that matter. Each nanoservice was running on its own EC2 instance.
I swear the entire thing was designed by someone with AWS stock or something.  
Scubabear68 6 months ago | root | parent | next [–]
I know one place that did all of their transactional payment flow through lambdas. There were about 20 lambdas in the critical auth path, and they regularly hit the AWS per-global-account limits.
Another place did all their image processing via lambdas, about fifty of them. They literally used lambdas and REST calls where anyone sane would have done it in one process with library calls. It cost them tens of thousands of dollars a month to do basic image processing that should have cost about $100 or so.  
ecshafer 6 months ago | root | parent | prev | next [–]
I agree with this. Personally I think the two pizza team model, single responsibility isnot a great idea. Most successful "microservices" model I've worked on actually had 100ish devs on the service. Enough to make on-call, upgrades, maintenance, etc. really spread out.  
bikelang 6 months ago | root | parent | prev | next [–]
Agreed. This is why I prefer the term “service oriented architecture” instead. A service should be whatever size its domain requires - but the purpose is to encapsulate a domain. A personal litmus test I have for “is the service improperly encapsulating the domain” is if you need to handle distributed transactions. Sometimes they are necessary - but usually it's an architectural smell.  
huherto 6 months ago | root | parent | prev | next [–]
This is my take too. Just because of the name, people try to make them as small as possible and we end up with too many of them.  
zelphirkalt 6 months ago | parent | prev | next [–]
I think updating dependencies is maybe the most important point. Different microservices can have different versions of libraries and frameworks, as long as their APIs return and do what they should, other microservices don't need to care about what version of some library is used. Being able to update dependencies for a smaller amount of code at a time can make all the difference between "no, that will be too much work right now" and "it's doable".
But, if you have a modular monolith, it will be easy to split it up into separate services, whether microservices or just services. It will be a good test to see how modular your system/monolith really is.  
vjvjvjvjghv 6 months ago | parent | prev | next [–]
Then your beautiful microservice gets old and requirements change. Now you have to fix 15 different services, rework interfaces, coordinate with multiple teams. My golden rule is: if you can't do a monolith right, you will fail even more at microservices. I think moving some parts into services but I see a lot of simplistic “we have users, so let's do a user service. Then we have files, so let's do a file service”. This will become a maintenance nightmare in my view.  
jimbokun 6 months ago | root | parent | next [–]
No you can update ONLY the micro services that are impacted by the new requirements without impacting the other micro services.
Agreed that this is not a useful heuristic for deciding how many services you need.  
SAI_Peregrinus 6 months ago | root | parent | next [–]
Only if the new requirements don't require a breaking API change. Microservices make API breaks more difficult, since they're loosely coupled it's harder to find all users of an old API & ensure they're updated than it is with a tightly-coupled system. Microservices make non-breaking changes easier, and help ensure all access is gated through an API.  
vacuity 6 months ago | parent | prev | next [–]
I think the framing of "monoliths vs. microservices", with the implication that you must either have a mountain of a codebase or a beach of grains of code-sand, is not helpful. Good modularity means that different levels of tradeoffs can be made without huge effort.  
BinaryIgor 6 months ago | root | parent | next [–]
True, that's why I titled the article "Modular Monolith and Microservices: Modularity is what truly matters". Modularity is crucial here - you can mix it up on multiple levels; having a single modular monolith, a few bigger services that have many modules inside each or finally, microservices where you treat each service itself as a module.
Modularization is what's primary here and gives you flexibility; not having one vs multiple units of deployment  
9rx 6 months ago | root | parent | next [–]
> microservices where you treat each service itself as a module.
Microservices is where you treat each team of people as their own independent business unit. It models services found in the macro economy and applies the same patterns in the micro economy of a single organization. Hence the name.
The clearest and probably simplest technical road to achieving that is to have each team limit exposure to their work to what can be provided over a network, which is I guess how that connotation was established. But theoretically you could offer microservices with, for example, a shared library or even a source repository instead.  
Scubabear68 6 months ago | root | parent | next [–]
Sorry, you lost me at "hence the name".
Microservices was originally envisioned to literally create the smallest possible service you could, with canonical Netflix use cases being literally only one or two endpoints per microservice.
Which is great I guess for FAANGs. But makes no sense for just about anyone else.  
9rx 6 months ago | root | parent | next [–]
> Microservices was originally envisioned to literally create the smallest possible service you could
"Micro web services" was coined at one time, back when Netflix was still in the DVD business, to refer to what you seem to be speaking about — multiple HTTP servers with narrow functional scope speaking REST (or similar) that coordinate to build something bigger in a Unix-style fashion.
"Microservices" emerged when a bunch of people at a tech conference discovered that they were all working in similar ways. Due to Conway's Law that does also mean converging on similar technical approaches, sure, but because of Conway's Law we know that team dynamics comes first. "Microservices" wasn't envisioned — it was a label given to an observation.  
Scubabear68 6 months ago | root | parent | next [–]
That's a nice narrative but very revisionist.
Microservices came about because Netflix and soon some other FAANGS found they were so big that it made sense to make single-function "micro"-services. They literally chose to massively duplicate functionality across services because their scale was so big it made sense for them.
This is great for FAANG-scale companies.
It makes little sense for most other companies, and in fact incurs all of the overhead you would expect - overly complex architecture, an explosion of failure points, a direct elongation of latency as microservices chain calls to each other, chicken-and-egg circular references among services, and all of the mental and physical work to maintain those dozens (or hundreds, or thousands!) of services.
The funny thing to me is people point to monoliths and say "see, problem waiting to happen, and it will be so hard to undo it later!". But I see microservices, and usually the reality is "We have problems right now due to this architecture, and making it sane basically means throwing most or all of it away".
In reality, unraveling monoliths is not as hard as many people have made out, while reasoning about microservices is much harder than advertised.
Tooling in particular makes this a very hard nut to crack. Particularly in the statically typed world, there are great tools to verify large code bases.
The tooling for verifying entire architectures - like a huge set of microservices - is way behind. Of course this lack of tooling impacts everyone, but it makes microservices even harder to bear in the real world.
Forget about convenient refactoring, and a thousand other things....  
9rx 6 months ago | root | parent | next [–]
> Microservices came about because Netflix
Nah. You've made up a fun story, but "microservices" is already recognized as being in the lexicon in 2011, while Netflix didn't start talking about said system until 2012.
> This is great for FAANG-scale companies.
Certainly. FAANG-scale employees need separation. There are so many that there isn't enough time in the day for the teams to stay in close communication. You'd spend 24 hours a day just in meetings coordinating everyone. Thus microservices says instead of meetings, cut off direct communication, publish a public API with documentation, and let others figure it out — just like how services from other companies are sold.
If you are small company you don't have that problem. Just talk to the people you work with. It is much more efficient at normal scale.  
BinaryIgor 6 months ago | parent | prev | next [–]
If you go up to this scale then yes - it probably makes sense to have a few - reasonably amount - services. But I would ask - why does it take for this kind of app to be up and running so long? It's rather not because of its code size - something else has gone wrong :)  
foldr 6 months ago | parent | prev | next [–]
Even in this hypothetical scenario, you're radically rearchitecting your entire product to save “months of work” and the cost of some beefier dev machines. How can that be rational?  
j45 6 months ago | parent | prev | next [–]
There's no reason monoliths can't have modularity that can be packaged as microservices.  
antonvs 6 months ago | root | parent | next [–]
There is a reason, which is the overall capabilities of the development org at a company. It takes more discipline and skill to do that consistently. Separate services are a forcing function for modularity.  
jimbokun 6 months ago | root | parent | prev | next [–]
But there are reasons for having more than one repo in a company, past a certain number of engineers.  
j45 6 months ago | root | parent | next [–]
I don't disagree.
My statement is that monoliths are capable of containing microservices and modular code to power them.  
andoando 6 months ago | root | parent | prev | next [–]
This is the way. Best of both worlds  
jimbokun 6 months ago | parent | prev | next [–]
I was with you until this part.
The correct answer is:
rTX5CMRXIfFG 6 months ago | parent | prev | next [–]
I'm not sure why that's your first instinct as opposed to splitting up your monolith into multiple Java packages that only have a downstream dependency relationship. (This is the second option in the article.) Spinning up microservices is hardly an easy win compared to this approach.  
andoando 6 months ago | parent | prev | next [–]
The other big advantage is you can monitor and scale your services independently and decouple outages.
If one endpoint needs to scale to handle 10x more traffic, its wholefully inefficient to 10x your whole cluster.
Ideally you write the code as services/modules in a monolith imo. Then you can easily run those services as separate deployments later down the line if need be  
j45 6 months ago | root | parent | next [–]
You also have to determine how much traffic for monitoring is due to microservices itself - where the messaging and logging might happen in memory, it now has to be read, and written, in much more expensive exectuions.
There's not one silver bullet. It's not 100% monoliths, or 100% microservices for all.
Learning from the things we don't do, haven't done yet, in the ways you haven't yet thought of also helps expand one's skills.
This is because clever architecture, will always beat clever coding.  
andoando 6 months ago | root | parent | next [–]
Im not sure what you mean. Whats the difference in messaging and logging? What you mean by messaging?
Like through network versus code running on the same machine? Cause that should already be distributed unless you can really fit your whole needs on a single machine  
nitwit005 6 months ago | root | parent | prev | next [–]
There isn't that much difference between an application and a library. You can always create multiple deployments of the same code configured differently.
We have an app with two different deployments. One is serving HTTP traffic, and the other is handling kafka messages. The code is exactly the same, but they scale based on different metrics. It works fine.  
jimbokun 6 months ago | root | parent | next [–]
In other words: when to split services and when to split repos are orthogonal concerns.  
loglog 6 months ago | parent | prev | next [–]
stavros 6 months ago | parent | prev | next [–]
If the monolith takes 20 minutes to load, just wait until you see how long it takes for all the microservices to start up.  
netdevphoenix 6 months ago | root | parent | next [–]
Indeed! And getting odd behaviour and trying to see what went wrong and takes you ages until your realise that one of the 10 micro services was failing rather than it being an actual bug in the micro service you were playing with. Plus, upgrade and maintenance gets multiplied by 10.  
nine_k 6 months ago | root | parent | prev | next [–]
I watched 1000-node microservice systems start up. Most nodes start really fast, and most of the system is up in seconds, maybe 15-20 seconds, as the flurry of service registration passes. A few nodes would take inordinate time to start up, apparently because they are unlucky and repeatedly get less CPU, less I/O, more retries on congested links, etc.
But you don't need to do this on your dev machine. Nearly a decade ago at GrubHub we already had a setup that allowed to run a few microservices under development locally, while relegating the rest to the staging environment that just runs every microservice, like prod, but in small quantities.
A JVM-based microservice used to take, say, 16-20 MiB of RAM; a 50-MiB service was considered a behemoth that may need slimming down. You could run quite a number of 20-MiB containers on a laptop with 16 GiB, along with all your dev setup, some local databases, etc.  
ecshafer 6 months ago | root | parent | prev | next [–]
Well in my experience, you only need to have 2-3 microservices running to do work locally.  
yearolinuxdsktp 6 months ago | parent | prev | next [–]
Being saddled with an old code base with a mountain of tech debt does not invalidate the OP's argument about modularity and microservices. I feel for your pain. You describe a great approach of how to tackle a monolith with mountains of tech debt by breaking out a microservice.
However, having a monolith does not automatically mean you abandon all addressing of tech debt. I worked on a large monolith that went from Java 7 to Java 21, it was never stuck, had excellent CI tooling, including heavy integration/functional testing, and a good one-laptop DX, where complex requests can be stepped through in your IDE all the way thru in one process.
Your argument dooes not invalidate a service-oriented approach with large (non-micro) services. You can have a large shared code base (e.g. domain objects, authentication and authorization logic, scheduling and job execution logic) that consists of modular service objects that you can compose into one or three or four larger services. If I had to sell that to the microservice crowd, I would call them "virtualized microservices", combined into one or many several deployment units.
In fact, if I were to start a new project today, I would keep it a monolith with internal modularity until there was a clear value to break out a 2nd service.
Also, it is completely valid to break out into microservices things that make absolute sense and are far detached from your normal services. You can run a monolith + a microservice when it makes sense.
What doesn't make sense is microservices-by-default.
The danger of microservices-by-default is that you are forced to do big design up-front, as refactoring microservices at their network boundaries is much more difficult than refactoring your internal modules.
Also, microservices-by-default means you now have so many more network boundaries and security boundaries to worry about. You now have to threat-model many microservices because of the significantly increased number of boundaries and network surface. You are now forcing your team to deal with significantly more distributed computing aspects right away--so now inter-service boundaries are network calls instead of in-process calls, requiring more careful design that has to account for latency, bandwidth and failure. You now have to worry about the availability and latency of many services, and risk a weakest-link-in-chain service bring your end-user availability down. You waste considerably more computing resources by not being able to share memory or CPU across all these services. You will end up writing microservice caches to serve over the network that which could've been an in-process read. Or if you're hardcore about having stateless microservices (another dogmatic delusion), you will now be standing up Redis instances or Memcached for your caches--to be transferred over the network.  
ninetyninenine 6 months ago | parent | prev | next [–]
No you completely missed his point.
He's saying instead of using "microservices" to modularize your shit, you can use folders to modularize your shit. Folders? Files? When someone told me that I could use folders to modularize stuff instead of entire microservices the concept was so foreign to me that it opened up a hole new world.  
drob518 6 months ago | prev | next [–]
IMO, 99.999% of apps should just use monoliths with basic 1+1 redundancy. Unless you're working at a FANG and require just insane scale, you really don't need microservices or even lots of modularity. Just keep it simple. If you need more resources, buy a bigger system and scale up, not out. Only consider scaling out when you have exhausted scaling up.  
sokoloff 6 months ago | parent | next [–]
I probably agree more than this comment might suggest, but I think that you run into organizational dynamics limits before you run out of vertical scaling limits.
Shipping a monolith worked on by 250+ devs in 30 teams is slow due to the coordination needed as compared to 30 teams shipping 50-75 services.
Vertical scaling can take you really, really far operationally.  
BinaryIgor 6 months ago | root | parent | next [–]
That's the strongest argument I can see; once you can get above 5 - 10 teams, you run into the organizational issues.
But again, most systems will never be there ;)  
3uler 6 months ago | root | parent | prev | next [–]
I've always maintained that microservices are more for scaling people than scaling systems.  
cedws 6 months ago | parent | prev | next [–]
I want to frame this and put it on my wall.
Coming up with a greenfield microservice design with arbitrary responsibilities and intercommunication feels so stupid to me. Why not build the thing as a monolith and split parts out when you actually have scaling problems, instead of solving theoretical problems? Development velocity is going to be way higher and it gives developers a chance to discover problems without having to deal with the mental overhead of shipping N services all at once.
The value of fast iteration cannot be overstated. Build the minimum viable version of the project first, then stress test it and break parts out when needed. This is much easier if you write modular code.  
xnx 6 months ago | root | parent | next [–]
I sometimes think programmers are the last people who should be writing software.
The personality type that likes writing code is the exact type that likes tinkering around the edge and working on hypotheticals instead of addressing the problem at hand.  
hunter2_ 6 months ago | root | parent | next [–]
One solution is to have the senior ones (who have already been-there-done-that and lost interest in those possibly low quality outcomes or low velocities from a business perspective) handle architectural decisions and keep things on the rails by way of writing issue specs that the juniors (with those green personalities) will implement, reviewing their code, mentoring them, etc. -- carefully matching an ideal threshold of autonomy for each programmer which will relax over time.  
drob518 6 months ago | root | parent | prev | next [–]
I often see technologies adopted simply because they are the “latest and greatest” and “I want to stay relevant for my next job interview,” rather than sound technical reasoning. Unfortunately, these decisions are made by humans and those humans have lots of cross-cutting decision criteria. It's a rare and highly mature engineer who can look at a problem and say “This old technology is a perfect fit.”  
yearolinuxdsktp 6 months ago | root | parent | prev | next [–]
This is an organizational/tech leadership problem. Good technical leadership will put a kibosh on working on hypotheticals, because what you don't do is as important as what you do.
Good programmers pride themselves on striking compromises and shipping a smaller thing sooner and they love iterating. The ones that are working on hypotheticals unchecked are not bad--just nobody has educated them.  
zerop 6 months ago | parent | prev | next [–]
Microservices created the need for more teams, devs, coordination, meetings, scrum teams, scrum master, Jira, CI CD tools, cloud market and so on.. It is very well planned :)  
9rx 6 months ago | root | parent | next [–]
It was — until developers started shouting "You don't need microservices. Just build a monolith."
Then, uncoincidentally, they started crying about how they couldn't find work anymore.  
drob518 6 months ago | root | parent | next [–]
There are a lot of people who shouldn't be doing software engineering.  
9rx 6 months ago | root | parent | next [–]
2015:
"I'm struggling to find work and need to make money. What can I do?"
"Learn to code, good buddy! Software engineering solves all problems."
2025:
"I learned to code and am still struggling to find work and need to make money."
"You shouldn't be doing software engineering."  
drob518 6 months ago | root | parent | next [–]
Yep, exactly.  
9rx 6 months ago | root | parent | next [–]
Exactly.  
antonvs 6 months ago | parent | prev | next [–]
This happens at all sorts of companies that are not FAANGs, and don't have "insane scale". There's an extremely large spectrum between the web site for Joe's Coffee Bar and Amazon. On commodity hardware, you hit issues with scaling up a monolith long before you reach FAANG level or "insane scale".
I've worked with multiple startups that have hit scaling limits with their monoliths. Inevitably, dealing with that is a huge problem because the monolith was developed with few resources under heavy time pressure. Modularity is lacking, breaking it up is difficult. Individual devs are often inclined to say that's just a skill issue, and that may have some truth to it, but managing those skill issues is a big part of what corporate software development is about.
This can have a huge impact on a company's funding, ability to deliver new features, ability to scale development, and of course ability to scale the user base. Typically, by the time they hit that wall, scaling the monolith horizontally is not a great option, because it wasn't designed to support that.
It's often been observed that microservices are a primarily an organizational tool, and that's true. But organization is critical if you have multiple development teams.
That doesn't necessarily mean every app should consist of hundreds of tiny microservices. But there can be enormous benefits from implementing an app from the start as independent services based on its natural divisions between modules.  
drob518 6 months ago | root | parent | next [–]
Without knowing what the cause of those scaling problems were (CPU, memory, IOPS, etc.), I'll have to take your word for it. But having worked at several startups, I can say that it's a common disease that engineers start to optimize for the “we're going to have a jillion customers” case long before they even have one customer, and that adds a whole bunch of complexity, cost, and schedule to the development, which increases burn and stands between the company and its cash-flow positive date. In fact, if it forces another round of funding, it can wash out the original employees or even kill the company. On the other hand, it's easy to raise money when you have customers and are near cash flow positive. You can do a HUGE amount with a modern server with 100+ cores, TB of RAM, etc. IOPS are the one thing which hasn't scaled quite as well. So yea, I'm being a bit hyperbolic in saying you need to be a FANG to consider it, but I think the main point still stands: most applications, if well-written, can be run well on today's hardware and scaled up if they need it while eliminating most of the complexity associated with scaling out. Yes, there are exceptions to that rule of thumb.  
nyrikki 6 months ago | parent | prev | next [–]
The problem being, most people are in the cloud, and 'basic 1+1 redundancy' simply doesn't work well in that distributed model and scaled up instances are expensive.
The tooling is good enough to scale out, but micro services are mostly beneficial for organizational scaling.
The value for other concerns is mostly situational.  
cedws 6 months ago | root | parent | next [–]
Big instances are cheap relative to the cost of implementing horizontal scaling (at the app layer), plus engineering cost of Kubernetes or whatever your preferred orchestrator is, plus the heavy cloud tax on going "cloud native."  
nyrikki 6 months ago | root | parent | next [–]
Even in the old days we were horizontal at the app layer, the persistence layer is what is hard.
Unless you have some very specific need, I was horizontally scaling the app layer in 1996 even in true monoliths.
K8s can be too much, but even when tooling and costs forced us to segment by technology layers, you never tried two node failovers.
If you are trying to share state at the app level you would most reduce availability, because of split brain etc…
The persistence layer was bad enough with shared quorum drives, heartbeat networks etc…
It sounds like you are just spinning up to app servers or are you talking about active/passive or active/active two node clusters?
That is vertically scaling in the way I understand the term, not just scaling out two instances.  
cedws 6 months ago | root | parent | next [–]
I'm talking about true horizontal scaling where load is sharded across replicas. Active-passive is easy. Handling web traffic is also easy. Backend business logic is not so easy.
If you're message driven you can maybe have a set of replicas consume off of a message bus like Kafka or NATS, but now you need to maintain that cluster, as well as build a messaging layer. What protocol do you use, etc?
Then there's the question of what triggers scaling up/down. The simple way is scale on CPU utilisation but then you get flapping issues. Or if load isn't completely evenly distributed you get one replica starving for CPU whilst the rest have too much.
All of these questions go away if you can just provision a big node and be comfortable that it will be able to handle anything within reason.  
BinaryIgor 6 months ago | parent | prev | next [–]
100%; and if you have a solid structure in your modular monolith - it's trivial to take one or two problematic/performance sensitive modules and turn them into independent services. But most of the systems will never get up to this scale  
drob518 6 months ago | root | parent | next [–]
Right. Launch it, get customers, see what needs to be scaled up, buy a new server, and only then, carve out that problematic piece and scale it as a separate service. But by then you have the data to justify it and you have sidestepped a lot of complexity.  
vb-8448 6 months ago | parent | prev | next [–]
The 1 + 1 setup can make it up even on FAANG level, it's not more about how much a single machine can do but more about how i you organize teams and what kind of swe you want ... bigger companies want "fungible" like SWEs, and it's easier to swap a swe in a microservices architecture vs monoliths.  
drob518 6 months ago | root | parent | next [–]
It's easier swapping an engineer into a module associated with a well-architected monolith than swapping them into a microservice. Given a monolith uses function calls that are fast and don't fail when the network cable is unplugged or DNS gets misconfigured, it's arguably a lot easier. There are fewer failure modes and overall lower complexity. No circuit breakers, back offs, retries, etc.  
netbioserror 6 months ago | prev | next [–]
Modularity is how we put out some long-running fires at my company. Our old infrastructure, from people who had long-since left, was a cross-cutting mish-mash of monoliths that each tried to do everything. Data analysis to web serving to PDF generation. Written in everything from C to Perl to PHP to VBA. All were supported because different clients depended on different monoliths depending on when they were brought aboard. Basically, each language was intended to serve on whatever walled-garden platform any given employee or client was expecting to use it. They didn't even talk to each other, reimplemented the same algorithms, it was a mess.
We spun out the specialized tasks (data analysis and PDF generation key among them) to native-compiled binaries or containerized packages like Gotenberg, started moving data around between modules via JSON, isolated the legacy monoliths to containers, unified on our now-modularized PHP backend, and have been working on updating or replacing any other pieces with new modules that can serve the task better. Our clients and non-engineering employees get antsy, but as a smaller company and a smaller programming team, we simply cannot maintain multiple 20-year-old codebases with near-total overlap. It makes no sense now, it didn't make sense when they were each created.  
barishnamazov 6 months ago | prev | next [–]
I recommend checking out concept design [0] from Daniel Jackson 1. It provides a framework to enforce modularity while building meaningfully designed software.
I have done a bit of work implementing a prototype framework for coding concepts using TypeScript [2], and it has worked beautifully for the Software Design class at MIT Daniel teaches. I think the newest iteration of class this semester uses a different approach to code concepts, but it's still a research space.
[0] https://essenceofsoftware.com/tutorials/
1 https://people.csail.mit.edu/dnj/
[2] https://61040-fa24.github.io/pages/concept-implementations.h...  
bunderbunder 6 months ago | prev | next [–]
My annoying critique of this article is that I don't think the author made their case strongly enough.
I've discovered that their taxonomy at the opening of the article ("single unit of deployment - monolith, multiple units of deployment - microservices/services") is a bit optimistic. Because, when it comes to making things unnecessarily complicated, human ingenuity knows no limits.
I've now worked on a project that somehow managed to be monolithic despite having multiple units of deployment. We weren't good about contract/API change management, so in practice it was rare that you could separately deploy "independent" services.
And I've also worked on a project that had a single unit of deployment but was somehow still more microservice-like. Everything was packaged into a single giant Docker image that contained the binaries for all the services. (You'd pick which one a container was running with run-time configuration.) But they were well-modularized and services from different versions of the image could talk to each other just fine, so in practice working on it often felt more like successful microservice implementations in development and production. It's just that getting things from development to production was an unholy nightmare because the CI pipeline for that "mono-image" was such a monstrosity.  
BinaryIgor 6 months ago | parent | next [–]
Thanks for the feedback :) I'm working on follow-ups, splitting it into multiple articles where I will try to elaborate more on various dimensions of modular monolith vs (micro)services debate/issue/decision and their various tradeoffs. Will try to make it clearer there!  
bunderbunder 6 months ago | root | parent | next [–]
I realize looking back that my opening sentence isn't quite right. I didn't mean to say that your article wasn't convincing. I meant that I thought that an even bolder version of your premise might also be true. The article is great as-is.  
Pxtl 6 months ago | prev | next [–]
Imho the web and SQL brought us to the ridiculous point that the most obvious way to "modularize" was to use fully separate isolated apps and servers.
This is because web and SQL are both dominant platforms for enterprise and are both allergic to modularization. Everything is global, everything is shared. Isolation and private interfaces are either impossible or late-added afterthoughts on a global-first platform.
So faced with this, it made sense that the only way to provide modularization was to use isolated computers that only talk over sluggish HTTP.  
dragonwriter 6 months ago | parent | next [–]
That's not actually true of SQL-based RDBMSs (except embedded ones like SQLite), and hasn't been for longer than the median developer has been alive, but it is probably fairly accurate of the average app developers understanding of SQL.  
asimpletune 6 months ago | prev | next [–]
The real thing that forces one to choose micro services over modules is when data isolation is a requirement, e.g. security.
Capabilities based programming could come along way though to help with closing that gap.  
lunias 5 months ago | prev | next [–]
This is exactly what I see all the time in the wild:
users service
quotes service depends on users service
notes service depends on quotes service
So... notes depends on users. Unless I'm missing something, I would not distribute this example ever in a million years. Most requests probably pull back all three pieces of data, so just do it in a single query. Do not introduce unnecessary extra network latency to aggregate the data. If you want to scale this horizontally then just add a load balancer in front of n copies of the single service.
Now, let's look at an example you might want to distribute:
web service (API)
video encode service (Running on specialized hardware)
Now we have an actual reason to separate our services, we want to take advantage of specialized hardware for our long-running, async video encode tasks while leaving our standard synchronous API responsive.
Another reason to distribute:
Team A works on API A
Team B works on API B
This allows each team to reduce the scope of their knowledge by focusing on a single API, but comes at the expense of extra network calls, serde, API negotiation, and versioning.
It cannot be overstated the convenience of:
Jump to code definition, update function, compile, fix compilation errors, code works.  
mdhb 6 months ago | prev | next [–]
I always thought Google had some interesting insights and ideas when they were playing around with the now abandoned service weaver project: https://opensource.googleblog.com/2023/03/introducing-servic...?
More academic and language neutral introduction here if that's your thing: https://arxiv.org/pdf/2404.09357  
mlhpdx 6 months ago | prev | next [–]
In modular systems, monolithic or distributed, the nuance of "depends on" is often the crux of complexity. A C++ binary interface dependency is more likely to create work than a string correlated via convention.  
dboreham 6 months ago | prev | next [–]
Yes, but no once you factor in Conway. Teams deploy and are responsible for their own running services. The line of demarcation is via TCP connections, not the call stack inside some process owned by 9 teams.  
BinaryIgor 6 months ago | parent | next [–]
Unless you have a lot of teams - like 10 and more - it's quite manageable to work on a solidly modularized monolith. But in general you're right; after your reach certain threshold of teams, it makes sense to have a few, not one, units of deployment  
efitz 6 months ago | prev | next [–]
Microservices embody a concepts that the article overlooks or downplays:
modularity - yes - but even better than what the article describes, there is little or no ability to cheat the modularity - the microservice has an api as a contract and is isolated in execution so there's no trivial way to go around the api.
Independently committable/deployable. One reason to consider microservices is organizational- maybe you don't want to or can't share a repro with another team.
Now of course microservices have lots of downsides and are not a panacea and may be a bad fit for your project.  
dennisy 6 months ago | prev | next [–]
The suggested “_contracts” folder lives at the top level of the modules or inside each feature/module?
My guess is it's a top level folder which shows the cross module deps.  
bognition 6 months ago | prev | next [–]
Hard agree with this article. Split up your application by domains, create public apis between modules, understand your dep tree and keep it clean.
The devil in the details is how you pull something like this off. At the end of the day is boils down to how do you enforce that your team does the right thing. You can have a single person that enforces standards with an iron fist, but this doesn't scale. You can teach everyone how this should work, but you're going to experience drift over time as people come and go. Or you can enforce it using technology and automation.
In the cases of the first choice, its going to restrict how big your team can get and will end up eating all of the time of your one person.
In the case of the second choice, a combination of the tragedy of the commons and regression to mean will degrade the system to spaghetti code.
For the third scenario language choice matters here a lot. In Java with multi maven modules you can setup maven to forbid imports of specific module types allowing you to make modules as private/public. In Python you can't do any of this.  
stingraycharles 6 months ago | parent | next [–]
As with all of these things, it needs to come from the very, very top, otherwise it doesn't work.
In the end, AWS only happened because of Jeff Bezos' infamous “all intra-team communication now goes over HTTP, no exceptions, or you're fired”-email.
The decision to prefer modules whenever they do the job, and defer only to microservices whenever they don't, seems like the kind of mantra that needs to come from the CTO and made part of the company culture's DNA.  
kevstev 6 months ago | parent | prev | next [–]
I think the real win with microservices is that when you are air-gapped between services, it really forces modularity and independence. Almost all the time in monoliths things slowly degrade into tangled dependencies. Once clean interfaces that just required a few specific parameters got lazy at some point and now the entire customer or order (or whatever) object is passed in and oops now the two are coupled.
This is of course still possible with a microservices architecture, but the barrier to changing a rest contract/API is usually much higher, and people think a lot more about what is being passed across the interface since that data is going to be sent over a wire.
Theoretically there is no difference, but its just far easier to slip when its one codebase and all it takes is someone a little too "LGTM" happy to let it through.  
CharlieDigital 6 months ago | prev | next [–]
I find it relatively easy to build "modular monoliths" by starting from "vertical slices"[0] at the outset. Vertical slices being primarily a feature organization strategy scales well pragmatically over time, IME. So when first starting out, you can keep it simple and just one monolith and one unit of deployment, but keep everything separated into their own feature folders with common things in a shared folder. When you get further along, it is possible to consider splitting things out by feature teams (if that's what works best) and still keep one runtime (just enabling/disabling different features at startup).
The common bits can eventually be moved into a package dependency and referenced. Separate features if they become large enough can also be moved into separate packages, but part of the same monolithic codebase.
In some cases, it can be easier still and just ship the entire runtime as-is (without any additional work to enable modularity) and simply route different endpoints (e.g. https://feature1.domain.com -> node set 1, https://feature2.domain.com -> node set 2) so you still have the option to monitor and scale the features differently based on their load profile and needs. This works great as long as cold starts are not a big concern (thereby adding a requirement for minimizing package size).
I find this particularly easy on AWS, especially when deploying with Copilot CLI1 because it makes it relatively easy to just route different sub-domains to different target groups. Now you have one singular container image that just gets scaled differently by route (e.g. a high volume feature gets bigger nodes and a dedicated route in Route 53).
I find some teams have trouble thinking this way because devs many times are not involved enough in the deploy time considerations. For more involved app-level partitioning of modules, I have a practical example in C#[2] that would work equally well with something like Nest.js (or Elysia or Hono) by simply using environment variables to declare a "feature role" for the instance and dynamically enabling/disabling feature modules.
[0] https://www.jimmybogard.com/vertical-slice-architecture/
1 https://aws.github.io/copilot-cli/
[2] https://github.com/CharlieDigital/dn8-modular-monolith  
ReflectedImage 6 months ago | prev | next [–]
So originally software development used micro-services rather than modules. A lot of software developers get this wrong and think modules were first. They were not. The software developers just grew up during the module fad caused by the personal computer before everything circled back around to micro-services.
The purpose of OOP was to replicate the benefits of micro-services in single user environments. A class corresponds to a service type and an object an physical instance of the service.
So why did Monoliths/modules fail? Some pretty simple issues, incomplete isolate between the modules, memory corruption and performance issues easily propagate between the "isolated" modules.
But the main killer is compile times. Monoliths/module based programs require massive compile times that grow quickly with the size of the program.  
jillesvangurp 6 months ago | parent | next [–]
As soon as functions were invented, we had modules. And as soon as we had the ability to call those over a network, people started building the same stuff over and over again. It's eery how much of the stuff that Kubernetes does maps almost one to one to the same kind of stuff that for example CORBA used to do. Naming, discovery, security, events, configuration etc. You'll find CORBA specific ways of doing all that. Except that stuff dates back 35 years. There is probably a bunch of stuff before CORBA that could be added to this list but that's before my time.
DCOM (MS) replicated some of that but never really caught on. You'll find quite a bit of that kind of stuff in OSGI (Java) that was somewhat popular in the early 2000s. And there was of course the whole SOAP / Web Services / SOA mess that people got into around the same time. Docker emerged early 2010s and Kubernetes soon followed and fast forward ten years and we're neck deep into the same shit all over again via micro services.
Part of this is just stuff you kind of need if you want to do a distributed system (like service discovery, auditing, security, etc.). And part of that is a lot of complexity resulting from that. Especially when you are distributing for organizational rather than technical reasons (Conway's law). Which is a major driving force in larger organizations.
The point here is that none of this is new. Also this stuff did not really fail but just seamlessly morphed into the next thing. People keep on making the mistake of believing that buzzword compliance makes things better/easier when in reality you are paying a largish price in terms of complexity and overhead for not that much gain. There's a lot of wheel reinvention happening here as well. And a lot of the exact same naivity being projected on the latest and greatest framework or thing. The same type of people that are cheer leading microservices now would have been cheer leading web services twenty years ago. In some cases these literally are the same people. Or companies. There's a reason IBM is all over this stuff, for example.  
BinaryIgor 6 months ago | parent | prev | next [–]
If you have each module as independently versioned package, the compile times are not slow, since you only need to compile modules that have changed and modules are provided as compiled dependencies.
Each individual module is fast to compile.  
antonvs 6 months ago | parent | prev | next [–]
This is not even remotely true, in any conceivable sense. But I'd love to hear what you were thinking of.  
ReflectedImage 6 months ago | root | parent | next [–]
The concept of a module comes from the concept of a service. Services have small public interfaces that conceal their private internal workings.
I understand it's a very surprising thing to learn.  
antonvs 6 months ago | root | parent | next [–]
You wrote “originally software development used…”
But originally, software development used or supported neither modules nor services. The original versions of languages like FORTRAN or COBOL had no such concepts. They had functions, procedures, or subroutines as the highest level of abstraction below the program level. And earlier computing systems were even lower level.  
bloppe 6 months ago | parent | prev | next [–]
Is there somewhere I could read more about this take?  
ReflectedImage 6 months ago | root | parent | next [–]
Of course: https://www.youtube.com/watch?v=wo84LFzx5nI  
foobarian 6 months ago | root | parent | prev | next [–]
Sounds like some mystical time during mainframe heyday era.  
strken 6 months ago | parent | prev | next [–]
Sorry, what? Are you claiming that ENIAC was using microservices? That's a claim that needs some kind of supporting evidence, or at least a better explanation.  
ReflectedImage 6 months ago | root | parent | next [–]
Procedure, functional and Entity Component Systems (Sketchpad, 1963) programs came first.
Micro-services then came along (Distributed computing).
Then OOP was then invented to replicate the benefits of micro-services in single user environments.  
antonvs 6 months ago | root | parent | next [–]
Sorry, but this is laughably wrong and bears no resemblance to how the history of computing actually developed.
The first systems that could reasonably be described as distributed computing weren't developed until the 1970s. The object-oriented language Simula was developed a decade earlier.
And those early 1970s distributed computing systems were not, by any stretch of the imagination, microservices. It wasn't until around the 1990s that the precursors to what we call microservices today appeared, in systems like CORBA, DCOM, and RMI. And the actual term “microservice” didn't appear until after 2010.
(You may be conflating “service” with “microservice”. Not all distributed networked services qualify as microservices.)  
twodave 6 months ago | prev | next [–]
I think if you build modules expecting the dependencies to not eventually include most other modules then you either have a trivial application or you're one PM monkey wrench away from a bad time.  
simianwords 6 months ago | prev | next [–]
i keep seeing "but this is only relevant if you are working at FAANG scale" but most productive applications work at similar scale. there's little fun or education just speaking about mocks or prototypes.
sure there are a lot of startups that start off and don't have much traffic. but i don't like that we dismiss real world productive applications because not many companies hit that scale. but most productive applications hit that scale!!  
default-kramer 6 months ago | parent | next [–]
What do you mean by "productive" here? The overwhelming majority (probably >99%) of billed/salaried software development hours are not spent working on FAANG-scale software. Does none of that count as "productive"?  
simianwords 6 months ago | root | parent | next [–]
Yes but the vast majority of applications that make money doing productive things have scale and complexity high enough that a monolith with sql won't cut it.  
default-kramer 6 months ago | root | parent | next [–]
I think you're underestimating the huge variety of productive apps in existence. For every system that handles >1M requests per second, there are probably at least 10 systems that won't even see 1M requests per hour. For example: Twice I've worked on apps for configuring motor control centers. I think you would consider these "productive" apps, but even if we had 100% market share there just aren't that many people in the world who need to configure a motor control center on any given day. The world is full of such apps.  
simianwords 5 months ago | root | parent | next [–]
People using and suggesting service oriented architecture are concerned with not just scale in terms of rps but also complexity in terms of lines of code and how much the code changed.
The number of apps that are also productive, also low rps, also not that complex, also not dynamic are few in number.
I guess this website is such an example.  
bullen 6 months ago | prev | next [–]
It's about the database, you need to make your own database!
As long as your bottom dependency is fixed, you cannot progress!
http://root.rupy.se  
tuhgdetzhh 6 months ago | prev | next [–]
Modular monolith is a pipe dream. Great idea, but it gets messed up in reality (similar to communism). You just need a bit of time pressure and project deadlines and the devs will crack and throw the modularity over board with just a few merges. Multiply that over a decade, then you end up with a monster and fight dragons.  
4ndrewl 6 months ago | parent | next [–]
I mean, it's stood the (multi-decade) test of time, but it's how Drupal works. Modularised components which interact with a common core. Not perfect, but gives you plenty of real world intel about the benefits, pitfalls and environment that you need to make it work.  
0xbadcafebee 6 months ago | prev | next [–]
Unfortunately this is not very useful. 'Modularity' is not a guarantee of good software design or operational practice.
You can develop a "module" that is tightly integrated with other "modules", making it unusable without the other "modules". This means you have one software component that's effectively split into two, and at least one is unusable on its own. This creates dependency issues, and design issues, as now the second component needs to closely track development of the first component. What's the point of the second module? None from the application's perspective; but it helps with Conway's Law (the worst reason for a software design decision).
In addition, "deployment" is not a singular concept. How is a monolith a "single unit of deployment" if it depends on a database with a changing schema? You have to deploy schema changes intentionally, and typically first, but with code that is backwards/forwards compatible. What's a deployment then? Is it a multiple stage process with multiple components? Or is the monolith somehow a "single unit of deployment", even though it entirely depends on the database which has its own "single unit of development", with the first being dependent on the second? (the answer is: a 'deployment' isn't a fixed concept; there is merely systems, and their components, and an order of operations to make changes without impairing system function)
Good system design depends on other, more specific concepts, like loose coupling, high cohesion, single responsibility, encapsulation, backwards-compatibility, immutability, versioning, and change management, to name a few. Merely making modules doesn't mean much; monoliths (like microservices), if not mindful, meander into mudballs.
It's also an overstatement to claim that microservices are inherently more complex than monoliths. You can easily end up with an overcomplicated monolith too. In fact you can easily end up with an overcomplicated anything. The difference with microservices is you're not [supposed to] make assumptions about data relationships, and you do have to preserve whatever functionality you expose that others depend on.
And please remember that monoliths and microservices aren't competing, as if one is supposed to be better than the other. They are just different, like apples and oranges. They have specific [and different] design and function implications. Use them properly as needed. You should be mixing them, not just making one thing in one way as if your whole company must do all things "the one twue way". (Examples [not canonical]: dhcpd is a microservice; dns is a collection of microservices; your browser is a monolith; a web app may be a microservice or monolith (or both); etc) 
Guidelines | FAQ | Lists | API | Security | Legal | Apply to YC | Contact
Search:
