---
name: The Ambiguity of "Simple": Confusing Simplicity with Ease in Software Design - Zenn
keywords: (placeholder)
metadata:
  url: https://zenn.dev/s4k1/articles/aa9ee7f322556c?locale=en
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
The Ambiguity of "Simple": Confusing Simplicity with Ease in Software Design  
Log in
 0y0
目次
i Translated by AI
The content below is an AI-generated translation. This is an experimental feature, and may contain errors. View original article
💬
The Ambiguity of "Simple": Confusing Simplicity with Ease in Software Design
2026/03/30 に公開
4
2   
アーキテクチャ
設計
solid
architecture
YAGNI
idea
Abstract: The phrase "make it simple" fails to distinguish between separation of concerns (Simple) and ease (Easy). This confusion distorts design decisions and misaligns organizational evaluation criteria. Starting with Rich Hickey's distinction, this article organizes YAGNI and SOLID as orthogonal axes and introduces existing means to measure the Simple axis.
Introduction
An article titled " Nobody Gets Promoted for Simplicity" has been circulating recently. Over-engineering is rewarded, while solid, steady work is ignored—this is indeed a problem.
I agree with the core concern of that article. However, by using the word "simple" without a definition, what exactly should be evaluated remains ambiguous. This article is not intended to refute the original's conclusion but to reinforce the definition at its foundation.
This article was written with the assistance of AI.
Simple vs. Easy
Let's clarify the distinction Rich Hickey made in " Simple Made Easy".
Simple — Concerns are not intertwined. The opposite is Complex.
Easy — Close at hand, familiar, quick to do. The opposite is Hard.
These two are independent axes.
Easy/Hard is subjective—it depends on who you are, how close it is to hand, and how familiar you are with it.
Simple/Complex is structural—though not entirely objective. Determining what constitutes a "single concern" involves judgment. Still, compared to Easy/Hard, it is easier to reach a consensus because discussions can be grounded in structure.
Thinking in 4 Quadrants
Where the optimal solution lies depends on the product's lifecycle. In live services where changes occur continuously, the intertwining of concerns bounces back as a cost with every change. For one-off products, the price of "Complex & Easy" may never manifest before the product reaches the end of its life.
This article assumes a product where code continues to change over a long period.
Why the "Simple" in the Original Article is Ambiguous
The original article features Engineer A and B. A ships 50 lines of code in two days, while B introduces an abstraction layer and pub/sub. The article portrays this as a contrast between "simplicity vs. complexity."
The problem is that the original article never defines "simple."
Let's look at the words describing Engineer A's code: 50 lines, ships in two days, easy to read, easy to test, easy for the next person to pick up. These are all features of Easy. In a context praising Simple, the author literally writes "easy" three times. The fact that only Easy vocabulary appears when trying to discuss Simple is evidence of the confusion itself.
Nothing is said about whether it is Simple—whether concerns are separated or whether unrelated parts break during changes.
The author also states, "The issue isn't complexity itself. It's unearned complexity," which seems to increase the resolution of the Complex side at first glance. However, whether the opposite side is Simple or Easy remains undefined. When saying, "avoid unearned complexity," it is not decided whether the destination after avoiding it is Simple (separation of concerns) or Easy (ease).
The claim in the latter half that "The decision not to build something is a decision" is also practically useful. However, if the content of the judgment being visualized is not distinguished between Simple and Easy, it only ends up visualizing the confusion.
In other words, isn't the original article actually comparing Easy and Complex?
This confusion is also reflected in how it was received. The article gathered over 100 points and 40+ comments on Hacker News and spread to various social media. Looking at the reactions, empathy toward the Easy direction is prominent. While some readers were implicitly aware of the Simple/Easy distinction, the article failed to provide that vocabulary, leaving the discussion unorganized.
Because there is no definition, confusion is being reproduced.
Thinking About Structural Differences Through Concrete Examples
For example, suppose an HTTP handler looks like this:
 
It is short and easy to read. However, four concerns—decoding, validation, persistence, and notification—are intertwined in one place. This is Complex & Easy. You cannot even run a test without a database connection just because you want to change the notification logic.
On the other hand, what if we separate them as follows?
refactored.go
 
Concerns are separated. You don't need a database connection to test notifications.
However, one cannot say "this is better" just by looking at this code. The peripheral code—interface definitions for Validator, OrderStore, and Notifier, implementations, DI wiring, and mocks for testing—becomes quite substantial. The cost of "Hard" in Simple & Hard is invisible if you only look at the handler itself.
What matters is not declaring a winner. When the former pattern accumulates in the tens or hundreds across the entire codebase, a single change like "replace the notification infrastructure" ripples through every handler. In the latter, you only need to swap the Notifier implementation. Which cost you tolerate depends on the product's change frequency and the direction of change.
YAGNI and SOLID are Orthogonal
The judgment criterion for YAGNI is "do we need it now?" The axis of judgment lies in the proximity of time. "Close at hand, within reach, needed right now"—that is the very definition of Easy by Hickey. YAGNI says nothing about the Simple/Complex axis. In the 4-quadrant model, it is a principle that optimizes the Easy axis.
The SOLID principles are about not intertwining concerns—a principle that optimizes the Simple axis. OCP says to handle with extension, and DIP says to align the direction of dependencies with interfaces. From the perspective of YAGNI, you don't need them now, but from the perspective of SOLID, they are an investment to keep things Simple.
These two are not in conflict; they are orthogonal. They are looking at different axes.
The Dilemma of Uncertainty—Can SOLID be the Default?
SOLID is a structural hedge against an uncertain future. If concerns are separated, the impact range is limited no matter what change comes. If the future of the product is predictable, the cost of hedging may not be worth it, so it can be relaxed.
In reality, the future of most products is unpredictable. Thus, investment in SOLID is justifiable— or so I would like to say, but there is a pitfall.
If the future is unpredictable, the correct axis of separation is also unpredictable.
In the previous handler, I separated "persistence" and "notification," but if an actual change came in the direction of "swapping the entire order processing flow," this separation would be off-target. Only the maintenance cost (Hard) of the separation structure would remain.
Uncertainty works in both directions.
Risk of not separating — The intertwining of concerns ripples, and the cost of change explodes.
Risk of separating along the wrong axis — The separation structure becomes an obstacle, and only the maintenance cost remains.
Making SOLID the default is not a universal insurance policy; it is a gamble that carries risks of its own.
Conditions Where Investment in the Simple Axis Becomes Advantageous
Just because there is a dilemma does not mean I want to end with "it's a case-by-case basis." Let's narrow down the conditions where investment is advantageous.
First, when there are patterns in the direction of changes. If trends can be read from the history of past changes, there is a basis for the judgment of separation. Uncertainty is a matter of degree, not a binary. For example, if adding payment methods has happened three times in the past year on an e-commerce site, there is a basis to bet on separating payment from order processing. Conversely, if that history does not exist, the separation is mere speculation.
Second, when you can choose a means with low separation costs. Interfaces and DI are not the only ways. Extracting functions, splitting modules, and making data passing explicit can resolve intertwining to some extent. If the degree of Hard is small, the loss from being wrong is also small.
Third, when the same pattern repeats throughout the codebase. If there is only one 50-line handler, you can just rewrite it later. If the same structure propagates in the tens or hundreds, a single separation judgment ripples through the entire codebase. The expected value of the investment increases.
These three conditions can also be used as criteria. In situations where change trends cannot be read, there is no repetition of patterns, and separation costs are high, it is more rational to lean toward YAGNI and review it later. Rather than "always SOLID" or "always YAGNI," making judgments each time based on these three conditions is what seniority, described in the next section, is truly about.
Acknowledge the Risks in Both Directions
Problems arise if you lean too heavily on either axis.
Leaning toward the Easy axis (YAGNI fundamentalism): Complex & Easy piles up. People say, "I'll add it later," but the structure to add it to no longer exists. It leads to a massive rewrite or collapse.
Leaning toward the Simple axis (SOLID fundamentalism): Simple & Hard becomes extreme, falling into Complex & Hard. Even if individual parts are separated, the connections increase too much, causing the whole to intertwine, or the axis of separation is wrong, leaving only maintenance costs.
Neither principle always wins.
Where Does Seniority Reside?
The correct answer is neither Engineer A nor B, but the engineer who can judge which change axis to make Simple and provide the basis for that judgment.
Clues lie in patterns readable from past change history, the product's lifecycle, the cost of separation, and the recovery cost if you are wrong. It is not line counts or lead time. Talking in terms of line counts is itself a reproduction of the confusion of attempting to evaluate the Simple axis with Easy axis metrics.
Can Organizations Evaluate Simple & Hard?
The distortion of incentives pointed out by the original article is real.
However, if we recommend "short and fast," won't Complex & Easy be mass-produced organizationally? Unseparated patterns will be evaluated as "fast and short," and they will propagate through the entire codebase. When you try to swap out the infrastructure half a year later, the code with the same structure is scattered in dozens of places, necessitating a total rewrite. That cost is not on the evaluation of the person who "released it fast" initially.
What should be evaluated is work that is Simple & Hard. The problem is how to measure whether it is Simple.
In software engineering, there are several measurement means to approximate the metric of "Simple"—degree of separation of concerns. These are broadly categorized into two systems: static metrics extracted from source code and dynamic metrics (or process metrics) obtained from the trajectory of the development process.
Static metrics analyze the structural dependencies of code and quantify coupling. Representative examples include Chidamber & Kemerer's CBO (Coupling Between Objects) and LCOM (Lack of Cohesion of Methods) [1]. CBO counts the number of dependencies between classes, and LCOM measures the degree of method and field sharing within a class. If the former is high, concerns are likely leaking externally, and if the latter is high, it is highly likely that multiple concerns are mixed internally. Also, by using Robert C. Martin's stability metric ( I = C e / ( C a + C e ) I = Ce / (Ca + Ce) I= C e/( C a+ C e) ), one can quantitatively determine at the package level whether the direction of dependencies matches the design intent (dependency on abstraction) [2].
However, static metrics have the limitation that the structure on the code does not necessarily match the actual chain of changes. Even if independent in structure, hidden coupling—where constant simultaneous modifications are forced due to shared implicit assumptions—slips through the net of static analysis.
Dynamic metrics fill this gap. Change Coupling, calculated from version control history, detects the fact that file groups that should have no physical dependencies are "always changed together." This is proof that the intertwining of concerns has manifested at the operational level rather than the structural level. Tools like CodeScene automate this analysis to identify "hotspots" with high modification frequency.
A powerful framework for evaluating the "severity" of such coupling and prioritizing improvements is Connascence, advocated by Meilir Page-Jones [3]. This classifies coupling along three axes: strength, locality, and degree. For example, even if coupling is structurally unavoidable, it acts as a triage guideline to maintain the overall simplicity of the system by weakening it from "execution order (dynamic)" to "name (static)" based coupling, thereby localizing the impact range.
By combining these multifaceted indicators, it becomes possible to answer the question, "Is this module Simple?" with objective grounding from both structural and operational perspectives.
However, having tools is a different problem from being able to use them. There are at least two hurdles to incorporating these metrics into an organization's evaluation process. One is that management, who are not engineers, need to be able to interpret what the metric values mean. The other is that in scenes where numerical improvement conflicts with short-term delivery speed, the organization must have a culture that can justify investment in the Simple axis. The original article is touching upon this latter problem, and the presence of tools alone does not solve it.
Nevertheless, it is a step forward to put measurable indicators on the discussion table rather than the current situation where "make it simple" is spoken vaguely.
Stopping the use of the phrase "make it simple" to mean Easy is the first step. When using it to mean Simple, specifying what it is Simple against—which axis of change are we separating concerns for—is the next step. And as tools to support that specification, there are the metrics mentioned here. How to root these tools in an organization is another problem, but at least if the vocabulary and measurement means are available, the discussion surrounding "simplicity" will no longer be an abstract dogfight.
脚注
Chidamber, S.R. and Kemerer, C.F. "A Metrics Suite for Object Oriented Design." IEEE Transactions on Software Engineering, Vol. 20, No. 6, 1994, pp. 476-493. https://ieeexplore.ieee.org/document/295895 ↩
Martin, Robert C. "OO Design Quality Metrics: An Analysis of Dependencies." 1994. https://linux.ime.usp.br/~joaomm/mac499/arquivos/referencias/oodmetrics.pdf ↩
Page-Jones, Meilir. What Every Programmer Should Know About Object-Oriented Design. Dorset House, 1995. https://www.amazon.com/Every-Programmer-Should-Object-Oriented-Design/dp/0932633315 ↩
4
2   
0y0
Game Client Engineer
フォロー  
バッジを贈って著者を応援しよう
バッジを受け取った著者にはZennから現金やAmazonギフトカードが還元されます。
バッジを贈る
Discussion
ログインするとコメントできます
Login
0y0
フォロー  
Game Client Engineer
バッジを贈る
バッジを贈るとは
目次
Introduction
Simple vs. Easy
Thinking in 4 Quadrants
Why the "Simple" in the Original Article is Ambiguous
Thinking About Structural Differences Through Concrete Examples
YAGNI and SOLID are Orthogonal
The Dilemma of Uncertainty—Can SOLID be the Default?
Conditions Where Investment in the Simple Axis Becomes Advantageous
Acknowledge the Risks in Both Directions
Where Does Seniority Reside?
Can Organizations Evaluate Simple & Hard?
Zennからのお知らせ
 個人部門を新設＆ルールを刷新！Microsoft Agent Hackathon
 Zennfes Spring がまもなく始まります。
Read next
🧭
[
今日からできるAIワークフロー設計シリーズ：LLMアプリを本番業務に入れるための設計パターン集
](https://zenn.dev/kanaria007/articles/c74aae44ba99fb)
かなりあ
1日前 7
🐕🦺
[
技術選定で重要なのは正解ではなく説明可能性
](https://zenn.dev/penginpenguin/articles/62e3118e0180a4)
ぺんぎん
1日前 12
🤔
[
問いを持つエンジニア
](https://zenn.dev/marvel/articles/dfaac40c51d360)
 
satak in FLARETECH株式会社
19時間前 3
🤖
[
【Nishika 論文サク読み 第8回】PHOTON: 階層構造で長文脈LLM推論を高速化
](https://zenn.dev/team_nishika/articles/fed725fd5c36a1)
 
ikuo.watanabe in Nishika Tech Blog
3日前 1
📑
[
[EXE] 新しいプロジェクトで品質を上げるときにやること・目指すゴールライン
](https://zenn.dev/tsukimi_soba/articles/exe-how-to-improve-quality-first-step)
つきみ
3日前
↩
[
Human Return Point――HITLと人間監督の再設計
](https://zenn.dev/dantarg/articles/human-return-point)
小野 昭久(PN:古明地ゆとり/ID:dantarg)
15時間前 1
4
2 
エンジニアのための情報共有コミュニティ
About
Zennについて
運営会社
お知らせ・リリース
イベント
Guides
使い方
法人向けメニュー New
Publication / Pro
よくある質問
Links
X(Twitter)
GitHub
メディアキット
Legal
利用規約
プライバシーポリシー
特商法表記
5/20開催! Classmethod Forum 2026 - 事業会社のリアルとAIで描く未来 
