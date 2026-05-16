---
name: Quantitative Risk Assessment Using Monte Carlo Simulations and ...
keywords: (placeholder)
metadata:
  url: https://hernanhuwyler.wordpress.com/quantitative-risk-assessment-using-monte-carlo-simulations-and-convolution-methods-in-r/
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-14T23:05:07.687Z
  notebook: 1.4. GRC (Governance, Risk & Compliance)
---
Quantitative Risk Assessment Using Monte Carlo Simulations and Convolution Methods in R – AI Governance and Risk Management
Skip to content 
Search
Search for: Search
AI Governance and Risk Management
Prof. Hernan Huwyler, MBA CAIO CPA AI GRC Director | AI Risk Manager | Compliance Officer and Auditor | Quantitative Risk Lead | Speaker and Corporate Trainer | Executive Advisor
Menu
Prof. Hernan Huwyler, MBA, CPA, CAIO
Who Writes This
Open Search
Quantitative Risk Assessment Using Monte Carlo Simulations and Convolution Methods in R
Why Probabilistic Risk Modeling Matters for GRC Professionals
Most risk assessments in practice still rely on subjective evaluations and risk matrices. Multiplying ordinal likelihood scores by ordinal impact scores produces a number that has no mathematical validity and no connection to financial planning. Research has repeatedly demonstrated that these traditional approaches are inherently flawed and predisposed to misinterpretation (Cox, 2008; Krisper, 2021; Thomas et al., 2014).
The alternative exists. Monte Carlo simulations allow you to model uncertainty as probability distributions, run thousands or millions of scenarios, and produce statistically grounded estimates of potential losses. Combined with convolution techniques that properly integrate impact distributions with probability distributions, these methods produce risk profiles that finance teams can use for reserve setting, capital allocation, and insurance decisions.
The barrier has traditionally been cost and complexity. Commercial risk simulation software is expensive. Statistical programming requires skills most risk practitioners don't have. Huwyler (2025) addresses both barriers with an open-source R script that executes Monte Carlo simulations with convolution in under five seconds for 100,000 scenarios, published freely on GitHub and executable in Google Colaboratory without any local installation.
This guide provides practical implementation tips for GRC professionals who want to move from qualitative risk matrices to quantitative probabilistic models using this methodology. 
Understanding the Core Methodology
Monte Carlo Simulation for Risk Assessment
Monte Carlo simulation generates thousands of random scenarios based on probability distributions you define for each risk variable. Instead of producing a single “expected loss” number, it produces a full distribution of possible outcomes showing the range, shape, and likelihood of different loss levels.
How it works in practice:
You define two inputs for each risk. The expected number of events in a given time period (modeled as a discrete probability distribution, typically Poisson). The expected financial loss per event (modeled as a continuous probability distribution, typically lognormal for operational risks).
The simulation runs thousands of iterations. In each iteration, it randomly samples from both distributions and combines the results. After all iterations complete, you have a dataset of possible total losses that you can analyze statistically.
Original implementation tip: Start with 100,000 simulations. Huwyler's testing shows this runs in approximately 4 seconds on Google Colaboratory. For initial assessments and scenario comparisons, 10,000 simulations (0.54 seconds) provide adequate precision. Reserve 1,000,000 simulations (approximately 35 seconds) for final calculations where precision matters, such as regulatory capital calculations or board-level reserve recommendations. The marginal accuracy improvement from 100,000 to 1,000,000 simulations is small for most practical purposes. Don't wait 35 seconds for every exploratory run during a workshop.
Why Convolution Matters
Traditional risk simulation multiplies a single impact value by a single probability value, producing a point estimate. Convolution is mathematically superior because it combines the full distribution of impacts with the full distribution of event frequencies, preserving the information contained in both distributions.
Without convolution, risk assessments tend to overestimate total exposures, particularly in extreme scenarios. This overestimation leads to excessive capital allocation, misallocated resources, and disproportionate responses. The mathematical reason is that simple multiplication of expected values ignores the distributional shape. Two risks with the same expected loss can have dramatically different tail profiles, and only convolution captures this difference.
Huwyler's R script implements convolution by generating separate samples from the impact and probability distributions for each simulation iteration, then combining them using a convolution function that accounts for the interaction between the two distributions. The result is a more accurate representation of the aggregate loss distribution.
Original implementation tip: The convolution approach produces lower aggregate loss estimates than simple multiplication in most cases, particularly in the tails. If you're transitioning from a non-convolutional model, expect your loss estimates at high percentiles (90th, 95th, 99th) to decrease. This is not an error. It's a more accurate calculation. Document the methodological change and explain to stakeholders that previous estimates were systematically conservative due to the mathematical limitations of the prior approach. Frame it as increased precision, not reduced risk.
Setting Up Your Environment
Option 1: Google Colaboratory (Recommended for Getting Started)
Google Colaboratory provides a cloud-based Jupyter Notebook environment that runs R code without any local installation. This eliminates the most common barrier to adoption: IT approval for software installation.
How to implement:
Access Google Colaboratory at colab.research.google.com. Create a new notebook. Change the runtime type to R. Copy the R script blocks from the published GitHub repository into notebook cells. Execute each cell sequentially.
You need a Google account. You need an internet connection. You need nothing else.
Original implementation tip: Google Colaboratory sessions time out after periods of inactivity and don't persist your data between sessions. Save your customized scripts to your Google Drive or download them locally after each session. For production use where you run assessments regularly, set up a saved notebook with your organization's standard distributions and parameters pre-configured. This way, when you open the notebook for a new assessment, you only need to change the input variables, not rebuild the entire script. I maintain one template notebook per risk domain (operational risk, compliance risk, cybersecurity risk) with distribution types and typical parameter ranges pre-configured. Customizing a pre-built template for a specific assessment takes five minutes. Building from scratch takes 30 minutes.
Option 2: Local R Studio Installation
For regular use and integration with organizational workflows, install R locally.
How to implement:
Download R version 4.3.2 or later from cran.rstudio.com. Install RStudio as the integrated development environment. Install the required libraries specified in the script's library installation block.
R runs on Windows (64-bit, Windows 7 and later), MacOS, and Linux. The base installation is free. All required libraries are open source.
Original implementation tip: If your organization restricts software installation, make the case by comparing the cost of R (free) against commercial risk simulation tools (typically $15,000 to $50,000 per user per year for enterprise licenses). The R script published in this methodology produces the same statistical outputs as commercial tools for the specific use case of Monte Carlo simulation with convolution. It doesn't have a graphical user interface for non-technical users, and it doesn't include the full feature set of commercial platforms. But for risk quantification, reserve calculation, and loss exceedance analysis, it delivers equivalent results at zero license cost. Present this comparison to your IT and procurement teams alongside a security review of R's open-source licensing.
Configuring the Risk Model: Input Variables
Block 1: Setting Your Parameters
The model requires five input parameters. Each parameter should be informed by historical loss data or calibrated expert estimates, not by assumption.
Simulations: The number of scenarios to generate. Start with 100,000 for standard assessments.
Events: The expected number of loss events per year. This parameter feeds the Poisson distribution, which models the frequency of discrete events occurring in a fixed time period. Derive this from your incident database, near-miss records, or calibrated expert estimates.
Loss: The expected average financial loss per event. This parameter feeds the lognormal distribution, which models continuous positive values with a right skew, typical of operational losses where most events are small but some are very large. Derive this from historical loss data or calibrated expert estimates.
Mean (Standard Deviation): The variability of losses around the expected value, expressed as a proportion of the mean. A value of 0.2 means losses vary by approximately 20% around the average. Higher values produce wider distributions with heavier tails. Derive this from the observed variance in your historical loss data.
Reserve: The percentile at which you want to set your reserve or risk tolerance. A value of 0.8 means the reserve will cover 80% of simulated scenarios. A value of 0.95 means 95% coverage. Your organization's risk appetite statement should inform this parameter.
How to implement:
The set.seed(123) line ensures reproducibility. Anyone running the same script with the same seed will get identical results, which is essential for audit trail integrity and peer review.
Original implementation tip: The standard deviation parameter (Mean in the code, which represents the sdlog parameter of the lognormal distribution) has an outsized impact on tail risk. A small change from 0.2 to 0.4 dramatically increases the probability and magnitude of extreme losses. Before running your assessment, conduct a sensitivity analysis on this parameter. Run the simulation with standard deviation values of 0.1, 0.2, 0.3, 0.4, and 0.5, holding all other parameters constant. Plot the 95th percentile loss for each run. This shows you how sensitive your reserve calculation is to uncertainty about loss variability. I've seen risk teams set the standard deviation to a round number without checking how much the output changes if that assumption is wrong by even 10%. The sensitivity analysis takes five minutes and prevents false confidence in the precision of your results.
Choosing the Right Distributions
Frequency Distribution: Poisson
The Poisson distribution models the number of events occurring in a fixed time period. It assumes events occur independently and at a constant average rate. It's appropriate for most operational risk event frequencies: fraud incidents per year, data breaches per quarter, compliance violations per period.
When to use it: When you have a reasonable estimate of the average number of events per period, events are independent of each other, and the probability of an event in any small time interval is roughly constant.
When to question it: When events cluster (one breach increases the probability of another), when the event rate is changing over time, or when the average frequency is very high (above 30 events per period, where the normal distribution may be more appropriate).
Original implementation tip: Derive the Events parameter from at least three years of incident data if available. A single year's count can be anomalous. If you experienced 2 events last year, 6 the year before, and 3 the year before that, your average is approximately 3.7 events per year. Use that average, not last year's count. If you have no historical data, use calibrated expert estimates following the structured elicitation protocol. Document the basis for the Events parameter in your assessment methodology. When an auditor asks “why did you assume 4 events per year?” you need a documented answer grounded in evidence, not “it seemed reasonable.”
Impact Distribution: Lognormal
The lognormal distribution models positive-only values with a right skew. Most losses are moderate, but some are very large. This matches the empirical pattern observed in operational, compliance, and cybersecurity losses.
When to use it: For financial losses, fine amounts, remediation costs, and other positive-value impacts where the distribution is right-skewed.
When to question it: When losses have a known upper bound (use a truncated distribution), when the distribution is bimodal (use a mixture distribution), or when losses are approximately symmetric around the mean (use a normal distribution).
How to implement:
The meanlog = log(Loss) parameter transforms the dollar amount into the log scale required by the lognormal distribution. The sdlog = Mean parameter controls the spread.
Original implementation tip: Validate your distribution choice against historical data whenever possible. Plot your actual loss history as a histogram. Does it look right-skewed with a long tail? If so, lognormal is appropriate. If your losses cluster around two distinct values (for example, small procedural fines and large enforcement actions), a single lognormal distribution won't capture the bimodal pattern. In that case, consider using a mixture of two lognormal distributions, one for each cluster. The R script can be modified to sample from a mixture distribution by randomly selecting which distribution to sample from in each iteration based on the relative frequency of each cluster. This modification adds three lines of code and dramatically improves model fit for bimodal loss patterns.
Other Distribution Options
The R script can be modified to use alternative distributions by changing the simulation functions in Block 2.
For impact distributions: use rnorm() for normal distributions when losses are symmetric, rgamma() for gamma distributions when you want more flexible skewness control, rweibull() for Weibull distributions common in reliability analysis, or runif() for uniform distributions when you only know the minimum and maximum.
For frequency distributions: use rbinom() for binomial distributions when modeling the probability of a fixed number of independent trials, or rnbinom() for negative binomial distributions when event frequency shows more variance than the Poisson assumption allows (overdispersion).
Original implementation tip: Distribution selection should be driven by data, not convenience. If you have historical loss data, fit multiple candidate distributions to the data and compare them using goodness-of-fit tests (Kolmogorov-Smirnov, Anderson-Darling, or chi-square). R provides the fitdistrplus library for this purpose. Run fitdist(your_data, "lnorm") and fitdist(your_data, "gamma") and compare the AIC (Akaike Information Criterion) values. Lower AIC indicates better fit. Document the distribution selection process and the fit statistics. This transforms distribution selection from an assumption into a defensible analytical choice. When presenting results to a board or regulator, the statement “we selected the lognormal distribution based on Kolmogorov-Smirnov goodness-of-fit testing against historical loss data” carries significantly more weight than “we used lognormal because it's commonly used for operational risk.”
Understanding the Convolution Process
What the Code Does
The convolution block combines the frequency and impact distributions for each simulation iteration.
For each of the 100,000 iterations, the code samples a number of events from the Poisson distribution and a loss amount from the lognormal distribution. The convolution combines these samples, and the total loss for that iteration is the sum of the convolution output.
The variable x contains 100,000 total loss values, one for each simulated scenario. This is your aggregate loss distribution.
Original implementation tip: The convolution approach used in this code produces materially different results from simple multiplication of expected values, particularly at high percentiles. Run both approaches on the same inputs and compare. Take the simple multiplication result (Events × Loss = 4 × $20,000 = $80,000 expected loss) and compare it to the simulation output. In the illustrative example, the mean simulated loss is $81,599, close to the simple expected value. But the 80th percentile is $115,867, which is 44% higher than the mean. The 95th percentile will be even higher. The simple multiplication gives you the center of the distribution. The Monte Carlo simulation with convolution gives you the full distribution, including the tails where the risk actually lives. When you present results, show the full distribution, not just the mean. The mean tells a risk committee that everything is manageable. The 95th percentile tells them what happens when things go wrong. Both are essential context.
Interpreting Model Outputs
Statistical Summary
Block 3 of the code produces the key statistics from the summary(x) function.
Based on the illustrative example with 4 expected events, $20,000 average loss, and 20% standard deviation:
Minimum: $0 (scenarios where zero events occurred)
25th Percentile: $49,383
Median: $75,715
Mean: $81,599
75th Percentile: $107,206
Maximum: $408,113
80th Percentile (Reserve): $115,867
How to interpret for business decisions:
The median ($75,715) tells you the most typical outcome. In half of all scenarios, total losses are below this amount.
The mean ($81,599) is higher than the median, confirming a right-skewed distribution. Some high-loss scenarios pull the average above the typical outcome. This skewness pattern is standard for operational risk.
The interquartile range ($49,383 to $107,206) represents the “normal range” of outcomes. Your baseline planning should accommodate this range.
The reserve level ($115,867 at the 80th percentile) covers 80% of scenarios. There is a 20% probability that actual losses will exceed this amount. Your risk appetite and regulatory requirements determine whether 80% coverage is adequate or whether you need to reserve at the 90th or 95th percentile.
The maximum ($408,113) represents the most extreme scenario generated in the simulation. This is your tail risk indicator. While the probability of reaching this level is very low, its existence informs your insurance and catastrophic loss planning.
Original implementation tip: Report the reserve calculation with explicit statement of coverage probability. Don't say “the reserve should be $115,867.” Say “a reserve of $115,867 covers 80% of simulated loss scenarios. There is a 20% probability that actual losses will exceed this amount. To cover 95% of scenarios, the reserve would need to be $X.” Then let the risk committee decide what coverage level they're comfortable with. I produce a reserve table showing the dollar amount at the 50th, 75th, 80th, 90th, and 95th percentiles. This gives decision-makers a menu of options with explicit risk-reward tradeoffs. Setting reserves is a business decision, not a statistical one. The model provides the options. Leadership chooses the coverage level. Document their choice and the rationale.
Risk Visualization
Histogram of Expected Losses
The histogram shows the distribution shape of simulated outcomes. You can visually identify the most common loss range, the skewness (right tail extending toward extreme losses), and the spread of outcomes.
How to use it: Present histograms to stakeholders who need to understand the range of possible outcomes intuitively. The visual shows that risk is not a single number but a distribution of possibilities. This is the most effective way to communicate why a single “expected loss” number is insufficient for decision-making.
Original implementation tip: Customize the histogram for your audience. For technical risk committee presentations, use the default output with statistical annotations. For board presentations, add vertical lines marking the mean, the reserve level, and the risk tolerance threshold. Use color to highlight the tail beyond the reserve level, making the “uncovered” scenarios visually prominent. R makes this straightforward:
The red line shows the reserve level. The blue line shows the mean. Everything to the right of the red line is the 20% of scenarios your reserve doesn't cover. This single visual communicates more about risk exposure than a 30-page qualitative risk report.
Loss Exceedance Curve
The loss exceedance curve plots the probability of exceeding different loss thresholds. It shows the relationship between coverage level and required reserve across the entire distribution.
How to use it: Use loss exceedance curves for insurance analysis, reserve setting, and risk tolerance calibration. The curve allows you to read off the loss amount at any desired confidence level and to compare different risk scenarios on the same chart.
Original implementation tip: Overlay multiple loss exceedance curves on a single chart to compare scenarios. For example, plot the curve for the current risk profile, then overlay curves for scenarios with additional controls (reduced event frequency or reduced average loss) and scenarios without controls (increased frequency or severity). The visual difference between the curves quantifies the value of your controls in dollar terms at any confidence level. This is how you justify control investments to a CFO: “Implementing this control shifts the 95th percentile loss from $X to $Y, reducing potential exposure by $Z. The control costs $W. The return on this control investment is $(Z-W).” That calculation comes directly from comparing two loss exceedance curves. No qualitative risk matrix can produce this insight.
Practical Use Cases Across Risk Domains
Financial Risk Assessment
Use the model to quantify potential losses from market movements, credit defaults, or liquidity events. Set the Events parameter to the expected number of adverse events per period. Set the Loss parameter to the average financial impact per event. Use the output to inform capital allocation, reserve calculations, and stress testing.
Original implementation tip: For credit risk, use historical default rates and loss-given-default data to parameterize the model. For a loan portfolio, Events might be the expected number of defaults per year and Loss might be the average loss per default. Run the simulation separately for each risk grade in your portfolio, then aggregate the results. The aggregated loss distribution becomes your portfolio-level credit loss estimate. Compare this to your current loan loss provisions. If the 90th percentile of your simulated loss distribution significantly exceeds your current provisions, you have a quantitative basis for recommending an increase.
Compliance and Regulatory Risk Assessment
Use the model to estimate potential regulatory fines, remediation costs, and enforcement action expenses. The GDPR fine estimation case study demonstrates this application: historical fine data provides the distribution parameters, and the simulation produces a range of potential financial exposures.
Original implementation tip: For compliance risk, parameterize the model using enforcement data from your relevant regulatory authority. Most regulators publish enforcement actions with fine amounts. Build a database of enforcement actions in your jurisdiction, for your industry, for the specific regulation you're assessing. Use this database to calculate the Events parameter (how many enforcement actions per year against comparable organizations) and the Loss parameter (average fine amount). The standard deviation comes from the spread in the fine data. For GDPR fines in Spain, the data shows a mean of €72,941 with a standard deviation of €154,431, indicating extreme variability. The lognormal distribution with appropriate parameters captures this pattern. Present the output to your compliance committee as: “Based on historical enforcement patterns, there is an X% probability that a fine exceeding €Y could be imposed. Our recommended reserve is €Z at the 90th percentile.”
Cybersecurity Risk Assessment
Use the model to quantify potential financial impact from security incidents. Events represents the expected number of breaches, ransomware attacks, or data loss events per year. Loss represents the average cost per incident including response, remediation, notification, legal fees, and business interruption.
Original implementation tip: Parameterize cybersecurity loss distributions using data from the Ponemon Institute's Cost of a Data Breach Report, the Verizon Data Breach Investigations Report, or your own incident database. Industry-specific breach cost data provides reasonable starting points when you lack sufficient internal data. However, adjust external benchmarks for your organization's size, data volume, regulatory environment, and response capabilities. A global bank's breach cost profile differs dramatically from a regional retailer's. Use external data to inform the distribution shape and your internal data to calibrate the scale. If you've experienced incidents, use your actual costs to validate or adjust the external benchmarks.
Operational Risk Assessment
Use the model for any operational risk where you can estimate event frequency and impact: equipment failure, supply chain disruption, employee errors, process failures, or project overruns.
Original implementation tip: For project risk, replace the single Loss parameter with a multivariate model where each project risk factor has its own distribution. Run separate simulations for cost overrun risk, schedule delay risk, and quality failure risk, then aggregate the results for total project risk exposure. The R script can be duplicated and run sequentially for each risk factor, with results combined using the c() function to merge the output vectors. This gives you a project-level aggregate loss distribution that accounts for the different risk profiles of each contributing factor.
Back-Testing and Model Validation
Comparing Predictions to Actual Outcomes
The model is only useful if it produces accurate predictions. Back-testing compares historical model outputs to actual losses to assess and improve model accuracy.
How to implement:
After each assessment period (quarterly or annually), record the actual total loss and compare it to the simulated distribution. Determine where the actual outcome falls in the distribution. If actual outcomes consistently fall in the tails (above the 95th percentile or below the 5th percentile), the model is miscalibrated.
Track back-testing results over time. Calculate what percentage of actual outcomes fall within the model's interquartile range, within the 90th percentile, and within the 95th percentile. For a well-calibrated model, approximately 50% of actual outcomes should fall within the interquartile range, 90% within the 90th percentile band, and 95% within the 95th percentile band.
Original implementation tip: Build a back-testing log that records, for each assessment, the date, the risk being assessed, the model parameters used (Events, Loss, Standard Deviation), the predicted distribution statistics (mean, median, key percentiles), and the actual outcome when it materializes. After accumulating 8 to 12 periods of data, calculate your model's calibration metrics. If actual losses consistently exceed the 80th percentile prediction, your model is underestimating risk and you need to adjust your input parameters upward. If actual losses consistently fall below the 25th percentile, you're overestimating and over-reserving. Present back-testing results to the risk committee as evidence of model accuracy. A model that demonstrates back-tested accuracy over multiple periods earns credibility that a new, untested model cannot claim. This is the same validation principle that SR 11-7 requires for financial models, applied to operational risk assessment.
Integrating With Organizational Decision-Making
Reserve Setting and Capital Allocation
The model's primary business application is informing reserve calculations. The percentile output directly translates to reserve recommendations at different confidence levels.
How to implement:
Produce a reserve table for each material risk showing the dollar amount required at the 50th, 75th, 80th, 90th, and 95th percentiles. Present the table to the risk committee with a recommendation for the appropriate confidence level based on your organization's risk appetite, regulatory requirements, and capital position.
For aggregate risk across the portfolio, run the model separately for each material risk and combine the results. Note that simple addition of individual reserves overestimates the total because it assumes all risks realize their worst case simultaneously. For portfolio-level reserves, consider running a combined simulation that accounts for correlation between risks, or apply a diversification factor to the summed individual reserves.
Original implementation tip: Connect the reserve table directly to your organization's risk appetite statement. If your risk appetite statement says “the organization maintains reserves sufficient to cover 90% of potential loss scenarios,” the 90th percentile output from the model is your recommended reserve. If the current reserve is below the model's 90th percentile output, you have a quantified gap between appetite and capacity. Present this gap in dollar terms. “Our risk appetite requires reserves covering 90% of scenarios, which the model estimates at $X. Our current reserve is $Y. The gap is $(X-Y).” This statement converts an abstract risk appetite into a concrete funding decision. It's the difference between “we need more reserves” (which gets deferred) and “we're $Z short of our own stated risk tolerance” (which gets funded).
Scenario Analysis and Sensitivity Testing
Use the model for comparing alternatives and testing assumptions.
How to implement:
Run the baseline scenario with current parameters. Then modify one parameter at a time and compare outputs. What happens to the 80th percentile loss if event frequency doubles? What if average loss increases by 50%? What if you implement a control that reduces frequency from 4 to 2 events per year?
Document each scenario with its parameter changes and output comparison. Present scenarios side by side showing the baseline and each alternative.
Original implementation tip: Use scenario analysis to quantify the value of proposed controls. Run the model twice: once with current parameters (before control) and once with the parameters you expect after implementing the control (reduced frequency, reduced impact, or both). The difference in the reserve requirement at your chosen percentile is the financial value of the control. Compare this value to the control's cost. If a control costs $50,000 per year and reduces the 90th percentile reserve requirement by $200,000, the return on control investment is 4x. This financial framing transforms risk management discussions from “we should implement this control because it reduces risk” (qualitative) to “this control delivers a 4x return on investment in reduced reserve requirements” (quantitative). The second framing gets approved.
Common Implementation Failures and How to Avoid Them
Failure: Using assumed parameters instead of data. The model produces precise-looking outputs regardless of whether the inputs are data-driven or invented. A Monte Carlo simulation based on made-up parameters is just computational fiction. Always document the source of each input parameter and the evidence supporting it.
Failure: Ignoring the distribution choice. Defaulting to lognormal without checking whether it fits your actual loss data produces systematically biased results. Test distribution fit against historical data whenever possible.
Failure: Reporting only the mean. The mean of the simulation output is the least useful statistic for risk management. The tails are where decisions happen. Always report percentile-based statistics alongside the mean.
Failure: Running the model once and filing the report. Risk profiles change as the business environment, control effectiveness, and threat landscape evolve. Re-run the model quarterly with updated parameters. Compare results across periods to identify trends.
Failure: Not setting a random seed. Without set.seed() , every run of the model produces slightly different results. This makes comparison between runs unreliable and creates audit trail problems. Always set and document the random seed.
Failure: Treating the model output as truth. The model output is only as good as its inputs and assumptions. Present results as “given these assumptions, the model estimates…” not as “the loss will be $X.” Uncertainty in the inputs produces uncertainty in the outputs. Acknowledge and quantify this uncertainty through sensitivity analysis.
Original implementation tip: Build a model documentation template that records every element a reviewer or auditor would need to evaluate the assessment. Include the risk being assessed, the data sources for each parameter, the distribution types selected and the justification for each selection, the number of simulations, the random seed, the software version and platform used, the date of the assessment, the author, the statistical outputs, the sensitivity analysis results, and the back-testing history. This template serves as your model card for risk simulations. When an auditor asks how you calculated the reserve, you hand them the documentation template. It should be self-contained and comprehensible without additional verbal explanation. Build it once. Use it for every assessment.
Extending the Model
Python Refactoring
Huwyler provides a refactored Python version of the R code in the GitHub repository. Python may be preferable for organizations that have existing Python infrastructure, want to integrate risk modeling with machine learning pipelines, or need to embed risk calculations in web applications or automated workflows.
Original implementation tip: If your organization's data science team works primarily in Python, use the Python version from the start. Don't force R adoption for the sake of following the original paper if your existing infrastructure and expertise are Python-based. The mathematical methodology is identical regardless of language. The practical adoption rate will be dramatically higher if you use the language your team already knows. Conversely, if your team already uses R for statistical analysis, stick with R. The tool that gets used is better than the tool that's theoretically superior.
Integration With AI and Machine Learning
The quantitative risk modeling framework can feed into and benefit from AI/ML approaches. Predictive models can forecast event frequency parameters based on leading indicators. Natural language processing can extract loss data from incident reports to parameterize the impact distribution. Reinforcement learning agents can optimize control portfolios based on simulation outputs.
Original implementation tip: Start with the basic Monte Carlo model. Prove its value by producing quantified reserve recommendations and back-testing them against actual outcomes. Then layer AI/ML capabilities on top of a proven foundation. Organizations that jump directly to AI-driven risk prediction without establishing basic quantitative risk modeling first build systems that produce sophisticated outputs from untested assumptions. The Monte Carlo model provides the quantitative foundation. AI/ML provides refinement and automation. The sequence matters.
From Risk Matrices to Probability Distributions: Making the Transition
Change Management for Quantitative Risk Assessment
Moving from qualitative risk matrices to quantitative probabilistic models requires changes in skills, processes, and culture.
How to implement:
Start with one risk domain where you have the best historical loss data. Financial risks or cybersecurity incidents often have the most complete data. Implement the model for that domain. Produce results. Compare them to the previous qualitative assessment. Show stakeholders where the quantitative approach provides insights the qualitative approach couldn't, particularly in the tails and in reserve calculations.
Don't try to replace every risk matrix overnight. Run the quantitative model alongside the existing qualitative assessment for two to three cycles. Let stakeholders see both outputs and compare them. The quantitative model's superiority becomes self-evident when actual losses fall within the simulated distribution and outside the qualitative assessment's predicted range.
Train risk analysts in basic R or Python programming, probability distributions, and statistical interpretation. This is a skill development investment that pays returns across every risk domain. A two-day training program covering the fundamentals is sufficient to enable a risk analyst to run and customize the model.
Original implementation tip: The biggest resistance to quantitative risk assessment comes not from technical complexity but from the loss of subjective control. With a risk matrix, a senior risk officer can set the rating wherever their judgment suggests. With a quantitative model, the data drives the output and personal judgment applies only to the input parameters, which are documented and testable. Some risk professionals experience this as a loss of influence. Frame the transition as an upgrade in credibility, not a reduction in authority. The risk professional's expertise shifts from rating risks subjectively to selecting appropriate distributions, interpreting model outputs, designing scenarios, and translating quantitative results into business decisions. This is a higher-value contribution that commands more respect from finance and executive teams. The CFO who ignored your red-yellow-green matrix will engage with your probability-weighted loss distribution because it speaks the language they use for every other financial decision.
Key References
Methodology:
Huwyler, H. (2025). “Quantitative Risk Assessment in R: An Open-Source Convolutional Framework for Modeling Uncertainty and Reserves.” Quantitative Finance and Risk Management, Volume 10.
Cox, A.L. (2008). “What's Wrong with Risk Matrices?” Risk Analysis, 28(2), 497-512.
Krisper, M. (2021). “Problems with Risk Matrices Using Ordinal Scales.” arXiv:2103.05440.
Thomas, P., Bratvold, R., Bickel, E. (2014). “The Risk of Using Risk Matrices.” SPE Economics & Management, 6(2), 56-66.
Monte Carlo Methods:
Ferrero, A. et al. (2023). “General Monte-Carlo Approach to Consider a Maximum Admissible Risk in Decision-Making Procedures.” Acta IMEKO, 12(4).
Burtescu, E. (2012). “Decision Assistance in Risk Assessment: Monte Carlo Simulations.” Informatica Economică, 16(4), 86-92.
Young, H.K., Ingall, L. (2009). “Exploring Monte Carlo Simulation Applications for Project Management.” IEEE Engineering Management Review, 37(2).
Convolution in Risk Management:
Yam, W.S. (2022). “Convolution Approach for Value at Risk Estimation.” Review of Pacific Basin Financial Markets and Policies.
Giuseppina Bruno, M., Tomassetti, A. (2006). “On the Calculation of Convolution in Actuarial Applications.” ACM.
Code Repository:
GitHub: github.com/hwyler/Paper2024/blob/main/RBaseModel
Published under open-source license for free use
Software:
R: cran.rstudio.com (free, open source)
Google Colaboratory: colab.research.google.com (free, cloud-based)
The gap between qualitative risk assessment and quantitative risk assessment is not a matter of sophistication. It's a matter of utility. A risk matrix tells you a risk is “high.” A Monte Carlo simulation tells you there's a 15% probability that losses will exceed $250,000 in the next 12 months and that reserving $180,000 covers 90% of scenarios. The first statement informs a discussion. The second statement informs a decision.
The tools to make this transition are free, the methodology is published, and the code runs in under five seconds. The only remaining barrier is the willingness to replace familiar but flawed methods with unfamiliar but accurate ones. The organizations that make this transition build risk functions that speak the language of finance, earn board-level credibility, and produce assessments that survive regulatory scrutiny. The ones that don't will continue filling out colorful matrices and wondering why nobody uses them for actual decisions.
Share this:
Share on X (Opens in new window) X
Share on Facebook (Opens in new window) Facebook
Like Loading...
Related
A 12-Step Procedure Merging ISO 27005, ISO 23894, ISO 42001, and FAIR March 12, 2026 In "ai"
AI Risk Modeling Beyond “Is AI Accurate?” March 12, 2026 In "AI governance"
Career Topics The Quantitative Risk Architect March 12, 2026 In "ai" 
Published by Hernan Huwyler
About Prof. Hernan Huwyler, MBA, CPA, CAIO AI Governance Director | Quantitative Risk Lead | Executive Advisor & Speaker Welcome. I am Hernan Huwyler. I help Fortune 500 leaders turn AI governance from a regulatory burden into a competitive advantage. This page tells you who I am, what I do, and how I can help your organization. Who I Am I am an AI Governance and Risk Management executive with over two decades of global experience. I currently serve as Senior Manager of AI Governance and Digital Compliance at Capgemini, where I also lead the Applied AI Lab. I am an Executive Professor at IE Business School and IE Law School, where I have directed the Advanced Program in Compliance since 2016. My work sits at the intersection of three worlds. Artificial intelligence. Quantitative risk. Regulatory compliance. Most people specialize in one. I built my career bridging all three. What I Actually Do I design and implement AI governance frameworks that work in the real world. Not theoretical constructs. Systems that survive regulatory scrutiny, board oversight, and actual operational pressure. My practice focuses on six core areas: AI Governance & EU AI Act Advisory I help organizations design enterprise-wide AI governance aligned with the EU AI Act, ISO 42001, and NIST AI RMF. This means lifecycle governance, policy design, approval gates, risk classification, and board-level strategy. If regulators come knocking, you want to be prepared. I help you get there. Quantitative Risk Modeling for AI I build probabilistic risk models using Monte Carlo simulation, Bayesian networks, and scenario analysis in Python and R. The goal is simple. Replace subjective heat maps with data-driven decisions. Quantify AI-related operational, compliance, and reputational risks in dollars. Calculate risk-adjusted ROI and Value-at-Risk for AI investments. This is how you talk to CFOs and boards. Algorithmic Auditing & AI Assurance I design and execute algorithmic auditing programs for ML models, GenAI systems, and third-party AI solutions. This includes bias detection, fairness testing, model drift monitoring, adversarial robustness evaluation, and explainability assessments. The output is audit-defensible documentation for regulators and internal audit committees. Responsible AI & Digital Compliance I implement responsible AI principles across organizations: fairness, transparency, accountability, privacy, and safety. This means building digital compliance programs spanning GDPR, EU AI Act, DORA, NIS 2, SOX, and FCPA. I integrate AI ethics into existing GRC frameworks and design KRIs, control matrices, and monitoring dashboards that actually get used. Keynote Speaking & Executive Workshops I deliver engaging keynote presentations and half or full-day executive workshops on AI Governance, Responsible AI, Quantitative Risk for AI, Algorithmic Auditing, and Digital Compliance. Conference keynotes. Corporate board briefings. Leadership offsites. University masterclasses. Delivered in English and Spanish. Executive Training & Certification Programs I design and deliver custom executive education programs in AI Governance, AI Risk Management, and Digital Compliance. I lead the Certified Chief AI Officer program. I train corporate teams in risk, compliance, audit, and technology functions. To date, I have trained more than 1,500 chief compliance officers, privacy officers, AI officers, ISO auditors, and risk managers. Why Organizations Work With Me I bring three things that are harder to find than they should be. First, I speak multiple languages fluently. Not Spanish and English, though I do. I speak data science, risk management, and executive strategy. I translate between teams that normally talk past each other. This saves months of friction. Second, I have been in the room when things go wrong. I have sat through regulatory hearings. I have explained to executives why their projects needed to die. I have signed documents that kept me up for weeks. That experience shapes every recommendation I make. Third, I build things that last. Not slide decks that gather dust. Governance systems that survive personnel changes, regulatory shifts, and the natural entropy of large organizations. If it cannot function without me, I have failed. View all posts by Hernan Huwyler
March 12, 2026
Uncategorized
ai, artificial-intelligence, business, convolutions, hernan-huwyler, iso-31000, machine-learning, monte-carlo-methond, monte-carlo-simulation, monte-carlo-technique, python, Quantative Risk Management, r, risk-models, technology
Post navigation
Implementation Tips for Expert Calibration and AI-Augmented Risk Estimation
A 12-Step Procedure Merging ISO 27005, ISO 23894, ISO 42001, and FAIR
Leave a comment Cancel reply
Write a comment...
Log in or provide your name and email to leave a comment. [-]
Email me new posts [x] instantly
Instantly [-] daily Daily [-] weekly Weekly [-]
Email me new comments [-]
Save my name, email, and website in this browser for the next time I comment.
Comment
Δ
Copenhagen Metropolitan Area, Denmark
Zurich Geneve, Switzerland, Madrid, Spain, Berlin, Germany
My GitGub
My LinkedIn Profile 
Create a website or blog at WordPress.com
Up ↑
Comment
Reblog
Subscribe Subscribed
AI Governance and Risk Management Sign me up
Already have a WordPress.com account? Log in now.
AI Governance and Risk Management
Subscribe Subscribed
Sign up
Log in
Copy shortlink
Report this content
View post in Reader
Manage subscriptions
Collapse this bar
Loading Comments...
Write a Comment...
Email (Required) Name (Required) Website Post Comment
%d  
Design a site like this with WordPress.com
Get started 
Search results
Search
No results found
Filters Show filters
Sort by:
Relevance
• Newest
• Oldest
Filter options
Close Search
Search powered by Jetpack
