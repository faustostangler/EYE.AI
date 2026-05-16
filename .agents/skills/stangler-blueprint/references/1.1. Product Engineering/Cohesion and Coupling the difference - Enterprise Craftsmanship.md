---
name: Cohesion and Coupling: the difference - Enterprise Craftsmanship
keywords: (placeholder)
metadata:
  url: https://enterprisecraftsmanship.com/posts/cohesion-coupling-difference/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Cohesion and Coupling: the difference · Enterprise Craftsmanship 
[
Enterprise Craftsmanship
](https://enterprisecraftsmanship.com/)
Blog
Book
TDD Course
Pluralsight Courses
About
Archives
Cohesion and Coupling: the difference
September 2, 2015
This is another post on the most valuable principles in software development.
You might have heard of a guideline saying that we should aim to achieve low coupling and high cohesion when working on a code base. In this article, I'd like to discuss what this guideline actually means and take a look at some code samples illustrating it. I also want to draw a line between these two ideas and show the differences in them.
1. Cohesion and Coupling: the difference
While coupling is a pretty intuitive concept, meaning that almost no one has difficulties understanding it, the notion of cohesion is harder to grasp. Moreover, the differences between the two often appear to be obscure. It's not surprising: the ideas behind these terms are indeed similar. Nevertheless, they do differ.
Cohesion represents the degree to which a part of a code base forms a logically single, atomic unit.
It can also be put as the number of connections inside some code unit. If the number is low, then the boundaries for the unit are probably chosen badly, the code inside the unit is not logically related.
A unit here is not necessarily a class. It might be a method, a class, a group of classes, or even a module or an assembly: the notion of cohesion (as well as coupling) is applicable on different levels. We'll talk about it in a minute.
Coupling, on the other hand, represents the degree to which a single unit is independent from others. In other words, it is the number of connections between two or more units. The fewer the number, the lower the coupling.
2. High cohesion, low coupling guideline
In essence, high cohesion means keeping parts of a code base that are related to each other in a single place. Low coupling, at the same time, is about separating unrelated parts of the code base as much as possible.
In theory, the guideline looks pretty simple. In practice, however, you need to dive into the domain model of your software deep enough to understand which parts of your code base are actually related.
It means that unlike such metrics as cyclomatic complexity, the degree to which your code is high cohesive and low coupled cannot be measured directly. It strongly depends on the semantics of the code which itself is an attribute of the domain model.
Perhaps, the lack of objectivity in this guideline is the reason why it's often so hard to follow.
There is a principle to which this guideline highly relates: Separation of Concerns. The two are pretty similar in terms of the best practices they propose. Check out this article to read more about the Separation of Concerns principle.
3. Types of code from a cohesion and coupling perspective
Besides the code which is both highly cohesive and loosely coupled, there are at least three types that fall into other parts of the spectrum. Here are all 4 types: 
Types of code from a cohesion and coupling perspective
Let's step into them, one by one.
1. Ideal is the code that follows the guideline. It is loosely coupled and highly cohesive. We can illustrate such code with this picture: 
Ideal
Here, circles of the same color represent pieces of the code base related to each other.
2. God Object is a result of introducing high cohesion and high coupling. It is an anti-pattern and basically stands for a single piece of code that does all the work at once: 
God Object
Another naming for this kind of code would be Big Ball of Mud.
3. The third type takes place when the boundaries between different classes or modules are selected poorly: 
Poorly selected boundaries
Unlike God Object, code of this type does have boundaries. The problem here is that they are selected improperly and often do not reflect the actual semantics of the domain. Such code quite often violates the Single Responsibility Principle.
4. Destructive decoupling is the most interesting one. It sometimes occurs when a programmer tries to decouple a code base so much that the code completely loses its focus: 
Destructive Decoupling
The last type deserves a more detailed discussion.
4. Cohesion and Coupling: pitfalls
Often, when a developer tries to implement the low coupling, high cohesion guideline, he or she puts too much of effort to the coupling side of the guideline and forgets about the other one completely. It leads to a situation where the code is indeed decoupled but at the same time doesn't have a clear focus. Its parts are separated from each other so much that it becomes hard or even impossible to grasp their meaning. I call this situation destructive decoupling.
Let's look at an example:
This code is a result of destructive decoupling. You can see that on one hand, the Order class is completely decoupled from Product and even OrderLine. It delegates the calculation logic to a special IOrderPriceCalculator interface; the creation of lines is performed by a factory.
At the same time, this code is completely incohesive. The classes whose semantics is closely related are now separated from each other. This is a pretty simple example, so I'm sure you get the idea of what is going on here, but imagine how hard it would be to understand such code describing some unfamiliar domain model. In most cases, the lack of cohesion makes code unreadable.
Destructive decoupling often goes hand in hand with the "interfaces everywhere" attitude. That is, the temptation to substitute every concrete class with an interface, even if that interface does not represent an abstraction.
So how would we rewrite the code above? Like this:
That way, we restored the connections between Order, OrderLine, and Product. This code is concise and cohesive.
It is important to understand the relation between cohesion and coupling. It's impossible to completely decouple a code base without damaging its coherence. Similarly, it's impossible to create fully cohesive code without introducing unnecessary coupling, but this attitude is seldom the case because, unlike cohesion, the concept of coupling is more or less intuitive.
The balance between the two is the key to creating highly (but not fully) cohesive and loosely coupled (but not completely decoupled) code base.
5. Cohesion and coupling on different levels
As I mentioned earlier, cohesion and coupling can be applied on different levels. The class level is the most obvious, but it's not the only one. An example here would be a folder structure inside a project: 
Poorly selected boundaries for a project
At first glance, the project is well-organized: there are separate folders for entities, factories, and so on. However, it lacks cohesion.
It falls into the 3rd category in our diagram: poorly selected boundaries. While the internals of the project are indeed loosely coupled, their boundaries don't reflect their semantics.
A highly cohesive (and loosely coupled) version would be the following: 
Better boundary choice
That way, we keep the related classes together. Moreover, the folders in the project are now structured by the domain model semantics, not by utility purpose. This version falls into the first category, and I highly recommend to maintain such kind of partitioning in your solution.
6. Cohesion and SRP
The notion of cohesion is akin to the Single Responsibility Principle. SRP states that a class should have a single responsibility (a single reason to change), which is similar to what highly cohesive code does.
The difference here is that while high cohesion does imply code have similar responsibilities, it doesn't necessarily mean the code should have only one. I would say SRP is more restrictive in that sense.
7. Summary
Let's summarize with the following:
Cohesion represents the degree to which a part of a code base forms a logically single, atomic unit.
Coupling represents the degree to which a single unit is independent from others.
It's impossible to achieve full decoupling without damaging cohesion, and vise versa.
Try to adhere to the "high cohesion and low coupling" guideline on all levels of your code base.
Don't fall into the trap of destructive decoupling.
8. Other articles in the series
YAGNI revisited
KISS revisited
Encapsulation revisited
Cohesion and Coupling: the difference
DRY revisited
Fail Fast principle
Making implicit assumptions explicit
Most valuable software development principles
← Database versioning tools
DRY revisited →
Subscribe
I don't post everything on my blog. Don't miss smaller tips and updates. Sign up to my mailing list below. Sign up
Comments
We were unable to load Disqus. If you are a moderator please see our troubleshooting guide.
18 comments
1
Login
Disqus
Facebook
X (Twitter)
Google
Microsoft
Apple
G
Join the discussion…
Comment
Log in with
or sign up with Disqus or pick a name
Disqus is a discussion network
Don't be a jerk or do anything illegal. Everything is easier that way.
Read full terms and conditions
This comment platform is hosted by Disqus, Inc. I authorize Disqus and its affiliates to:
Use, sell, and share my information to enable me to use its comment services and for marketing purposes, including cross-context behavioral advertising, as described in our Terms of Service and Privacy Policy, including supplementing that information with other data about me, such as my browsing and location data.
Contact me or enable others to contact me by email with offers for goods or services
Process any sensitive personal information that I submit in a comment. See our Privacy Policy for more information [-]
Acknowledge I am 18 or older [-]
4
Discussion Favorited!
Favoriting means this is a discussion worth sharing. It gets shared to your followers' Disqus feeds, and gives the creator kudos! Find More Discussions Share
Tweet this discussion
Share this discussion on Facebook
Share this discussion via email
Copy link to discussion
Best
Newest
Oldest
−
+
 zlamma 7 years ago edited Excellent article and the illustrations! They make it the best resource I found that clearly maps the concepts of Cohesion and Coupling to the common sense intuition. If I may suggest an improvement to just one image though: I like how the 'poorly selected' keeps the groups of components with unrelated semantics in little swarms, but I think the swarms themselves on that one should have less arrows inside them (using the 'folder structure' example from your article, which you categorize as 'poorly selected', the repositories in there will certainly not talk to each other), while there should be more arrows between the swarms (after all, even on your 4-squares graphs 'poorly selected' is the one that falls into the high values of the 'Coupling' axis). see more
4 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/22z120n
−
+
 Vladimir Khorikov Mod zlamma 7 years ago Indeed, that would be a more accurate representation. see more
1 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/22zwcaz
Show more replies Show more replies
−
+
 Pedro Henrique Calais 4 years ago Excellent article. see more
1 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/2q3qerv
Show more replies
−
+
 Tomas Tulka 6 years ago Thanks for the great article, especially the explanation of destructive decoupling, really helpful! I'm a bit puzzled by your categorization of the God object (aka Big ball of mud): You say, it's an example of high cohesion. But even in your picture, the colors aren't related at all. I understand the God object as a big component doing a lot to everything, having too much responsibilities, which is actually the definition of low cohesion. Similarly, distribution of responsibilities in the Big ball of mud usually leads to a high degree of coupling, as you correctly say. Typical approach to break down the Big ball of mud is to find related components, bring them together and increase the degree of cohesion so. When done right, it usually leads to loosely coupled components, towards the Ideal. As a good example of high cohesion and tight coupling I suggest systems with different cohesion criteria than functionality (domain/business), e.g. systems modularized by technical concerns (Layered architecture). Such systems do have a high degree of (logical) cohesion but suffer from tight coupling as each functionality is spread across multiple layers (modules). Could you please collaborate on this topic little more? see more
1 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/2c4u5ht
−
+
 Tomas Tulka Tomas Tulka 6 years ago Inspired by this discussion I put my thoughts into a post: https://ttulka.medium.com/how-cohesion-and-coupling-correlate-dd1716ca04fa For those who'd appreciate a second view. see more
1 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/2crqn76
Show more replies
−
+
 Vladimir Khorikov Mod Tomas Tulka 6 years ago Interesting suggestion. The topic is quite subjective and comes down to the definition of cohesion and coupling (which may vary). I define it as the number of connections inside a code component (cohesion) and between code components (coupling). This concept has a fractal nature and can be applied on different levels. I don't think layering falls into the category of high cohesion and tight coupling, though. If we take a program feature (e.g user registration) as a component, then all connections inside it can be categorized as cohesion. The Big ball of mud is a better fit for the high cohesion/tight coupling quadrant because it doesn't differentiate between types of components and allows for the connections between any of them. see more
0 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/2cc2zx4
−
+
 Tomas Tulka Vladimir Khorikov 6 years ago edited Your definition of cohesion is pretty general. The important question is: by what key are they connected? Of what kind is the relationship? If we say, the key is a technical concern like " all database-related elements (classes) go into a single component (package/namespace)", then the layered architecture is highly-cohesive. The point is to choose the right key. A feature (functionality/domain/business) is probably the best key for cohesion. Big ball of mud, on the other hand, has the probably worst key for cohesion: none. So the cohesion in a big ball of mud is purely coincidental. That is, the coincidental cohesion is high, but the functional cohesion is very low, because everything is connected to everything and there are many connections between completely functionally unrelated elements. Taking a feature as a key for cohesion (as you propose), the cohesion of the big ball of mud is awful. see more
0 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/2cc743m
−
+
 Vladimir Khorikov Mod Tomas Tulka 6 years ago I agree, the component boundaries are key here. Regarding the big ball of mud -- I also agree that the connections inside the big ball of mud are coincidental and chaotic, but that by definition means that those connections are all over the place; it has a large number of both "good" connections (cohesion) and "bad" ones (coupling). see more
0 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/2cdy83p
−
+
 Tomas Tulka Vladimir Khorikov 6 years ago I understand your conclusion: Regarding your definition of cohesion ( the number of connections inside a code component), the big ball of mud has a high degree of cohesion, indeed. I'm just unhappy with the definition itself, that results in such a conclusion. Let me illustrate my point: Consider a component with elements A, B and C, where A is related to B, but there is no relation between C and A or C and B. The degree of cohesion for such a component is obviously lower than for a similar component that contains only A and B, right? At least in my understanding of cohesion, it is. Your formula is simple to measure, but, unfortunately, I don't think the things are so easy. "Belonging together" is the main takeaway. An amount of connections is easy to measure, but not so the quality (aka cohesion) of them. I agree with you that the topic is subjective. Given multiple views on the same thing it's to consider the most beneficial one. Your definition is easy to measure, that's great, but following it as a metric, it eventually leads to the big ball of mud. Mine is impossible to measure accurately, but it always leads to highly cohesive and loosely coupled code (the Ideal), I believe. see more
0 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/2ce1tlt
Show more replies Show more replies Show more replies Show more replies Show more replies
−
+
C Csaba Faragó 2 years ago The illustration is great, but is it correct? Ideal one: it is correct. God object: according to my understanding it would have low cohesion, because there are many unrelated fields and methods in the same class, but low coupling in the same time, because is has hardly any external dependency, almost everything is present internally. Destructive decoupling: this means that we put hardly anything (less than optimal) into one class, and that results in high cohesion. But there will be too many external dependencies, i.e. the coupling will be high. Poorly selected boundaries: I think that the illustration should contain less internal and more external arrows. So basically the circles of same color should be connected, resulting too much external arrows, i.e. high coupling, while there are hardly any arrows between the colors, resulting low cohesion. see more
0 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/30k9uxs
Show more replies
−
+
 Yuri Cardoso 6 years ago Hi Vladimir, excellent content. You're following the Rich Domain Models approach, right? How would you implement this example if you were to use Services (e.g. ProductService, OrderService and etc) and anemic models. Thanks. see more
0 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/282bdp9
Show more replies
−
+
S Sneha Rathod 6 years ago Great articles! Great for revision :D see more
0 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/262fk70
Show more replies
−
+
 Andriy Chubarev 9 years ago Haha, destructive decoupling is about me right now. see more
0 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/1kp3aeg
Show more replies
−
+
M Michael G. 10 years ago Good post yet again. I have one question though. Doesn't the use of "new OrderLine" inside the AddLine method make it more difficult to unit test the code? The reason why I ask is that an OrderLine could be fairly simple, but often it can be subject to discounts, which follow some business rules. Moving such logic to a factory is usually the prefered method to deal with instantiation of complex objects, rather than put them in the OrderLine constructor. see more
0 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/17t6q8q
−
+
 Vladimir Khorikov Mod Michael G. 10 years ago edited Good question. Generally, it is better to treat a whole aggregate as a unit for testing. Here, OrderLine is part of the Order aggregate (it doesn't have a lot of meaning outside of it) and thus should be tested with the Order itself. The business rules regarding discounts, if implemented inside the Order aggregate, can also be unit tested along with the Order class. Here I touched on this topic in a bit more detail: http://enterprisecraftsmans... see more
1 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/17tplz9
Show more replies Show more replies
−
+
 Uchitha Ranasinghe 11 years ago Excellent post mate thanks. Looking at your example of highly cohesive solution structure, how practical is it to have your repositories (OrderRepository) in your DomainModel project? My repositories usually have their own project (less cohesive). Thanks again. see more
0 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/10yrt2k
−
+
 Vladimir Khorikov Mod Uchitha Ranasinghe 11 years ago edited Thank you! I personally tend to consider repositories part of the domain model. They reside higher than entities but still I think they are part of it: View Hide  This picture reflects how I usually form layers in software projects. The 2 inner layers are parts of the domain model, the other layers belong to other parts of the system. see more
1 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/10z2t8t
−
+
 Chris Dunn Vladimir Khorikov 11 years ago I keep the repository interfaces (IOrderRepository) in my domain layer and the implementations in the infrastructure layer (SqlServerOrderRepository). That's one other way to do it, though you need to be very disciplined and make sure no business logic creeps out of the domain layer into the infrastructure layers. see more
3 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/1199n19
Show more replies Show more replies Show more replies
Load more comments
Subscribe Subscribed
Privacy
Do Not Sell My Data
Powered by Disqus  
Please enable JavaScript to view the comments powered by Disqus.
Top 
Vladimir Khorikov
  
My book
Click here to get a 40% discount
Pluralsight courses
‒ Pragmatic Unit Testing
‒ Domain-Driven Design in Practice
‒ Applying Functional Principles in C#
‒ Database Delivery Best Practices
‒ Specification Pattern in C#
‒ Refactoring from Anemic Domain Model
‒ Domain-Driven Design: Working with Legacy Projects
‒ CQRS in Practice
‒ DDD and EF Core: Preserving Encapsulation
‒ Validation and DDD
‒ Encapsulating EF Core Usage
‒ Prepare for coding interviews with CodeStandard
Citadel Password Manager Privacy first. No data collected, period.
Most Popular Articles
‒ EF Core 2.1 vs NHibernate 5.1: DDD perspective
‒ C# and F# approaches to illegal states
‒ Optimistic locking and automatic retry
‒ Entity vs Value Object: the ultimate list of differences
‒ DTO vs Value Object vs POCO
‒ 3 misuses of ?. operator in C# 6
‒ Specification pattern: C# implementation
‒ Database versioning best practices
‒ Unit testing private methods
‒ Functional C#: Handling failures, input errors
‒ REST API response codes: 400 vs 500
Recent Articles
‒ Storing information in its highest form
‒ Which collection interface to use?
‒ Generic types are for arguments, specific types are for return values
‒ Modeling Relationships in a DDD Way
‒ Encapsulating EF Core Usage: New Pluralsight course
‒ Collections and Primitive Obsession
‒ How to Assert Database State?
‒ Should you Abstract the Database?
‒ Database and Always-Valid Domain Model
‒ Specification Pattern vs Always-Valid Domain Model
» All articles
© 2025 Vladimir Khorikov. Made with Hugo.
BDOW!
