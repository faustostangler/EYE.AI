---
name: Hexagonal Architecture on Spring Boot - Coding Forest
keywords: (placeholder)
metadata:
  url: https://jivimberg.io/blog/2020/02/01/hexagonal-architecture-on-spring-boot/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
Hexagonal Architecture on Spring Boot - Coding Forest 
Hexagonal Architecture on Spring Boot
written February 1, 2020 in architecture, hexagonal, java, spring, spring-boot
In this article, I'll show how to implement a Spring Boot application using Hexagonal Architecture.
We'll build a Bank Account simulation with deposit and withdraw operations exposed through REST endpoints.
Hexagonal Architecture
Hexagonal architecture is an architectural style that focuses on keeping the business logic decoupled from external concerns.
The business core interacts with other components through ports and adapters. This way, we can change the underlying technologies without having to modify the application core. 
Application Core
Domain Model
Let's start with the domain model. Its main responsibility is to model the business rules. It also verifies that the objects are always in a valid state:
BankAccount.java
The domain model should have no dependency on any specific technology. That's the reason why you'll find no Spring annotations here.
Ports
Now it's time to have our business logic interact with the outside world. To achieve this, we'll introduce some ports.
First, let's define 2 incoming ports. These are used by external components to call our application. In this case, we'll have one per use case. One for Deposit:
DepositUseCase.java
And one for Withdraw:
WithdrawUseCase.java
Similarly, we'll also have 2 outgoing ports. These are for our application to interact with the database. Once again, we'll have one per use case. One for Loading the Account:
LoadAccountPort.java
And one for Saving it:
SaveAccountPort.java
Service
Next, we'll create a service to tie all the pieces together and drive the execution:
BankAccountService.java
Note how the service implements the incoming ports. On each method, it uses the Load port to fetch the account from the database. Then, it performs the changes on the domain model. And finally, it saves those changes through the Save port.
Adapters
Web
To complete our application, we need to provide implementations for the defined ports. We call these adapters.
For the incoming interactions, we'll create a REST controller:
BankAccountController.java
The controller uses the defined ports to make calls to the application core.
Persistence
For the persistence layer, we'll use Mongo DB through Spring Data:
SpringDataBankAccountRepository.java
Also, we'll create a BankAccountRepository class that connects the outgoing ports with the SpringDataBankAccountRepository:
BankAccountRepository.java
Infrastructure
Finally, we need to tell Spring to expose the BankAccountService as a bean, so it can be injected in the controller:
BeanConfiguration.java
Defining the beans in the Adapters layer helps us maintain the infrastructure code decoupled from the business logic.
Conclusion
In this article, we've seen how to implement an application using Hexagonal Architecture and Spring Boot. This is what the system ends up looking like: 
The code for this example is available on Github.
This article is based on the highly recommendable “Get Your Hands Dirty on Clean Architecture by Tom Hombergs, and this Baeldung article by Łukasz Ryś. 
Comments
We were unable to load Disqus. If you are a moderator please see our troubleshooting guide.
What do you think?
30 Responses 
Upvote 
Funny 
Love 
Surprised 
Angry 
Sad
8 comments
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
K khmoussi Aouina 2 years ago hi if i may ask in the controller why inject the depositusecase and withdrawusecase when we decalred BankAccountService as a bean shouldn't we inject BankAccountService in the controller ? see more
0 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/2xr5qx4
−
+
 Juan Ignacio Vimberg Mod khmoussi Aouina 2 years ago You're correct, at runtime an instance of BankAccountService will be injected in the controller. We use the *UseCase interfaces so that Controllers are only limited to calling the methods present on these interfaces. This allows us to change the UseCase implementation later without having to change the Controllers see more
0 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/2y0stxc
Show more replies Show more replies
−
+
 Marc Collin 5 years ago don't seem to have 3 layers... user side, business logic, service side (infra) see more
0 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/2dvypfb
Show more replies
−
+
J jwin 6 years ago Hi, nice article... I have looked into hexagonal architecture a while ago (and also read Tom Homberg's book), but somehow I believed that adapters strictly implement ports... so I was a bit surprised to see that the WebController in your example does not implement (in terms ofSomeClass ... implements ... Interface) the incoming port, but _uses_it, and the incoming port is actually implemented (again in Java-technical terms) by the application-service (which btw can be regarded as also belonging to the domain ?). But yes, since WebController uses only the incoming port (interface), this WebController depends on the domain.. so the dependency points inward, which is correct for the architecture. What is your take on this ? That"d be nice to know ! Best, Joerg see more
0 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/2bq9z6j
−
+
 Juan Ignacio Vimberg Mod jwin 5 years ago I think that's true for the Outgoing (persistence adapter in this example) ports but not for the Incoming ones (web adapter in this example). The reason is that in an Incoming port the adapter is calling into the application, so the code implementing the business logic should leave in the application core instead of the Web Adapter. The Adapter still needs to know about the interfaces to be able to make the call. see more
0 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/2dsfpt1
Show more replies Show more replies
−
+
G Guy 6 years ago Thank you nice and clear. How do you avoid having jpa annotations on your domain models? - which invariably seems to happen on the projects I have worked on in the past see more
0 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/29u2ya4
−
+
 Juan Ignacio Vimberg Mod Guy 6 years ago That's a great question! If you're looking to keep things decoupled you can have a persistence model on the adapter component. You'll have to write some boilerplate code to map between the models, or use something like Model Mapper. If the application is simple enough you can get away with having the annotations on the business model. You can start with this approach and move to mapping the models the moment you face the need to write persistence logic in your business entities. The mentioned book Get Your Hands Dirty on Clean Architecture has a whole chapter about mapping strategies. It does a great job covering advantages and disadvantages. You can find some of the content on this talk Play Hide , by the author. see more
0 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/29xp3vr
Show more replies Show more replies
−
+
V Vijaykumar Subramani 6 years ago Thanks see more
0 Press the down arrow key to see users who liked this 0 Press the down arrow key to see users who disliked this
Reply
Share ›
http://disq.us/p/29l6tw2
Show more replies
Load more comments
Subscribe Subscribed
Privacy
Do Not Sell My Data
Powered by Disqus  
« Previous: Book recommendations: Shape Up Next: How to craft effective presentations »
[
Home
](https://jivimberg.io/)   
Powered by Octopress. Designed by Adrian Artiles.
