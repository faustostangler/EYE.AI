---
name: 2026-05-10 The Unit Economics of the Payments Business | by Milan Radics | Fintech | Payment Solutions | POS Systems | Digital Payments | Medium
keywords: (placeholder)
metadata:
  url: None
  source: SOURCE_TYPE_TEXT
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
WebSync metadata
title: The Unit Economics of the Payments Business | by Milan Radics | Fintech | Payment Solutions | POS Systems | Digital Payments | Medium
url: https://medium.com/fintech-payment-solutions-pos-systems-digital/the-unit-economics-of-the-payments-business-72752cfa5946
date: 2026-05-10T23:07:55.134Z
parsing method: defuddle
Sitemap
Fintech | Payment Solutions | POS Systems | Digital Payments
FinTech • Payment Solutions Management (POS, Transaction Services, Payment Gateways) • Strategic Leadership in Fintech and Payment Systems • Organizational Leadership • Service Management and SLA Compliance
In fintech and payments, unit economics means analyzing the revenue and cost on a “per unit” basis — typically per transaction or per customer. In other words, one asks: “How much do I earn from each payment or user, and how much does it cost?” [1]. This analysis helps determine if each payment yields profit after covering all associated costs. For example, a common unit is a single card transaction: one would sum all fees earned per transaction and subtract all costs (network fees, fraud losses, infrastructure) to find the net profit per payment.
Payment providers earn revenue from fees on each transaction — interchange, processing fees, service charges, FX fees, etc. Interchange fees are a core component: they are the fees paid by the acquiring bank to the issuing bank on every card transaction [2]. In practice, card networks (Visa/Mastercard) set these interchange rates so that the issuer recovers risk and cost, while merchants and acquirers cover these fees. As BIS research explains, in four-party card schemes the interchange fee “plays a crucial role” by flowing from the acquirer to the issuer, allowing issuers to offer attractive card services while keeping cardholder fees lower [3]. In effect, interchange income helps fund the payment ecosystem. For instance, Stripe notes that Visa alone processed over 212 billion card transactions in 2023 [4] — even a small percentage fee on each of these yields huge revenue. (Fintech firms such as neobanks often rely heavily on interchange income: one industry guide notes that some firms, like Chime, earn almost all their revenue from interchange [5].)
On the cost side, providers incur expenses for each transaction: network access fees, fraud-protection costs, and technology infrastructure. According to an ECB study, the average social cost of retail payments is nearly 1% of GDP, shared equally between banks/infrastructures and merchants [6]. Importantly, that study found cash and debit cards have the lowest cost per transaction [6]. This underscores that efficient electronic payments can be relatively cheap — but the payment provider’s unit economics must factor in all backend costs, not just the marginal transaction cost.
Key metrics in payment unit economics include gross margin per transaction and lifetime value (LTV) versus customer acquisition cost (CAC). For example, if a provider charges merchants a fee of 1% per payment, but pays 0.3% in network fees and 0.5% in interchange, the gross margin is 0.2% of the transaction value. In absolute terms, a $100 payment might yield only $0.20 profit before fixed costs. Given such thin margins, high volumes and scale are usually required. Fintech executives monitor LTV:CAC ratios to ensure growth is profitable: as Wise explains, an LTV:CAC around 3:1 is a healthy benchmark [7]. Payment companies calculate LTV based on the expected number of transactions (and related fees) per customer over time, while CAC includes marketing and sales costs to onboard new merchants or users.
In summary, understanding unit economics in payments means breaking down per-transaction revenue and cost. For instance, Stripe’s API documentation highlights that idempotent requests are used so that retrying a transaction won’t charge a customer twice [8] — reflecting the importance of getting each payment (unit) right the first time. By tracking interchange income per transaction [2], subtracting fixed and variable costs (e.g. fraud prevention, network fees), and comparing to acquisition costs, a payments business can determine if each unit of sale is truly profitable. This guides pricing and growth: as Wise points out, unit economics analysis “tells you whether you’re on the right track” and whether “pricing is sustainable” [1] [9]. In practice, successful fintech payments providers strive to keep per-transaction costs low (through automation and scale) while maximizing fee revenue (through smart pricing and interchange capture) to ensure each unit contributes positive profit.
References: European Central Bank, The Social and Private Costs of Retail Payment Instruments, ECB Occasional Paper No 137 [6]; Stripe Docs, What is Interchange Income?[2] [4]; BIS (Aurazo et al. 2024), Interchange Fees, Access Pricing and Sub-acquirers in Payment Markets [3]; Unit (Embedded Finance guide), The Ultimate Guide to Interchange Revenue [5]; Wise Blog, Unit Economics 101 [1].
[1] [7] [9] Unit Economics 101: A Guide for Growing Businesses — Wise
https://wise.com/us/blog/unit-economics
[2] [4] What is interchange income? | Stripe
https://stripe.com/resources/more/what-is-interchange-income-what-it-is-and-how-businesses-can-make-the-most-of-it
[3] Interchange fees, access pricing and sub-acquirers in payment markets
https://www.bis.org/publ/work1163.pdf
[5] The ultimate guide to interchange revenue
https://www.unit.co/guides/ultimate-guide-interchange-revenue
[6] The social and private costs of retail payment instruments: a European perspective
https://www.ecb.europa.eu/pub/pdf/scpops/ecbocp137.pdf
[8] Idempotent requests | Stripe API Reference
https://docs.stripe.com/api/idempotent%5Frequests
Last published Apr 1, 2026
FinTech • Payment Solutions Management (POS, Transaction Services, Payment Gateways) • Strategic Leadership in Fintech and Payment Systems • Organizational Leadership • Service Management and SLA Compliance
Head of Service & Operations in Fintech | Payment Solutions | POS Systems | Digital Payments @ Cardnet Zrt. https://www.linkedin.com/in/milanradics/
