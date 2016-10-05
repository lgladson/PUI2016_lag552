#Homework 4

#Assignment 1
**Contribution:** I worked on this assignment independently, as directed.

**Assignnment Scope:** I provided feedback to Sanz Gonzalez Enrique (netID: esg336; github: esanzglez) and sent a pull request, which was accepted. The README.md file is titled CitibikeReview_lag552.md and is contained inside their HW3_esg335 folder in their repo. I think the most important suggestion I gave was about being more specific in the hypothesis and putting their data into ratios to compare male and female commuting habits in mornings vs. evenings. **For sake of convenience, I've copied my review below:**

##Peer Review of Citi Bike Assignment

###a. Verify that Null and alternative hypotheses are formulated correctly
First off, very interesting  idea! Regarding the hypothesis statements, I would suggest including more detail, and making sure
to state the "equal to or smaller" component in the null hypothesis and the "larger" component in the alternative hypothesis (instead
of just saying "no difference"). It would also be good to specify the time frame and the hypothesis in equation form. 

Additionally, I would be careful to distinguish if you're looking at the gender groups seperately or together - it was a little unclear, 
but what I got from reading your description was that you want to look at them seperately (i.e., in the female group, a higher 
percentage bike in the evening than in the morning, compared to a similar ratio in the male group). I feel this is an important 
distinction, simply because you could have a situation where there are a lot less women bikers overall which would skew the comparison 
if not normalized with a ratio of sorts. So I would suggest comparing the ratio of women biking in the evening over in the morning to
the ratio fo men biking in the evening over in the morning. My suggestions for these changes are below:

**H0:** In 2015, there was an equal or smaller ratio of female Citi Bike users commuting in the evening vs. the morning 
compared to their male counterparts, significance level = 0.05.

**H0 Equation:** (Evening Female Commuters/Morning Female Commuters) =< (Evening Male Commuters/Morning Male Commuters)

**Ha:** In 2015, a larger ratio of female Citi Bike users commuting in the evening vs. the morning compared to their male 
counterparts. 

**Ha Equation:** (Evening Female Commuters/Morning Female Commuters) > (Evening Male Commuters/Morning Male Commuters)

###b. Verify that the data supports the project

Really good job pulling out the correct variables (i.e., start times, gender, and creating the codes for morning, evening, or neither
and pulling out the correct times for those). I'm unsure, however, if "day of week" (Monday, Tuesday, etc) is needed, since this 
wasn't a componenet of your hypothesis. I thinkin your figures/the data you organized, you could have simplified it to just show 
morning and evening categories along the x-axis, and then the ratio value along the y-axis. I realize the ratio was my suggestion 
from above, so it's understandable that you guys did number of rides. Though I do think you have to be careful looking at raw numbers 
alone, since the numbers in each gender groupdiffer. But it looks like you tried to address this in the last normalized figure, so 
props for that! Regarding that last figure, I'm just a little confused because the label says "fraction" but the axis units are in 
the large numbers. I think if it's a fraction it should only span from 0 to 1 along the y-axis. But I think you had the right idea 
here to separate morning and eveningriders. Generally, I think you need to simplify the process and just look for the ratios of the 
two gender groups and compare those.

###c. Chose an appropriate test

I would suggest using a chi-square test to test this hypothesis. Chi-square tests compare only 1 independent variable (gender, here)
and 1 dependent variable (commute time). Also, the data type for both the independent and dependent variables are categorical, which
matches with your hypothesis (gender is the categorical IV; morning vs. evening commute time is the categorical DV). Also, chi-square 
tests compare observed to expected frequencies (expected being that the ratios named above are equal), so this fits with our hypothesis
comparing the ratios of the two genders regarding commute time.

*It might be tempting to use a t-test, since t-tests look at differences between only two groups of independent variables
(males and females, in this case) to test their effect on the dependent variable. However, a t-test's dependent variable is continuous,
not categorical, which does NOT fit in this case.*

##**End of peer review**

#Assignment 2
**Contribution:** I worked on this assignment independently (due to scheduling restraints). 

**Assignnment Scope:** This literature review involved finding two scientific articles using a test to see the difference betweeen groups and using a test to look for relationships between the IV and DVs, respectively. I chose a t-test for my first paper, and looked at an article about how bacterial diversity varies between asthmatic smokers and healthy non-smokers, and also how bacterial diversity varies amoung asthmatic smokers who quit smoking and those who do not. This study was technically an exploratory one, though they did perform analysis in their results, so it was a little difficult to determine hypothesis and alpha values, but I explain this in the table below. As a notes, their conclusion was that asthmatic smokers do have more bacterial diversity, but there was no significant difference in this group between quitters and non-quitters. My second study was one using multiple linear regression to look at the relationship between a specific peptide level and bone mineral density in U.S. citizens. It ultimately determined a significant negative linear relationship between these variables. 

| **Statistical Analyses	|  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var | Control Var type  | Question to be answered | _H0_ | alpha | link to paper **|
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
T-test	| 2, Health/Smoking Status (Tobacco smokers with asthma vs. non-smoking healthy controls); Cessation Status (Cigarette quitting vs. non-quitting asthma patients) | categorical | 1, bacterial diversity (count) | continuous | 2, patients had not experienced lower respiratory tract infections in the last 3 months; patients had not received treatment with inhaled or systemic corticosteroids in the last 3 months | categorical | 1. Does bacterial diversity differ between asthmatic smokers and healthy non-smokers? 2. Does bacterial diversity decrease in cigarette-quitting asthmatic smokers vs. non-quitting asthmatic smokers? | This was an exploratory study, so no pre-specified null hypothesis was stated; only said "smoking cessation is associated with changes in bacterial diversity"; if stated, the null would likely be: bacterial diversity after cessation >= bacterial diversity without cessation | Used p-value = 0.05 in analysis | [Smoking Cessation and the Microbiome in Induced Sputum Samples from Cigarette Smoking Asthma Patients](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0158622) |
Multiple Regression	| 1, serum C-peptide level | continous | 1, bone mineral density (BMD) (in g/cm^2) | continuous | 4, age; sex; ALP, FPG, and serum insulin levels; and BMI | both categorical (sex; ALP, FBG, and insulin levels; possibly age and BMI) and continous (possibly age and BMI) | Is serum C-peptide level associated with bone mineral density (BMD) in residents of the United States? | No significant correlation (specifically, linear relationship) between serum c-peptide levels and BMD; H0: β1 (the slope of the linear relationship) = 0 | None stated in the beginning, but used p = 0.01 in analysis | [The Association between the Serum C-Peptide Level and Bone Mineral Density](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0083107) |

#Assignment 3
**Group/Contribution:** I worked on this assignment mainly with Nonie Mathurand Kristi Korsburg and also with Santiago Carillo. Nonie and I worked through most of the code together. My contribution was explaining the observed/expected tables and where those calculations were coming from. Nonie, Kristi, and I talked through what the statistics meant, and I believe I showed the group how to use the statistics tables. 

**Assignnment Scope:** The two tests in this assignnment (z and chi-square) were essentially testing whether the program group (who went through an employment program) differed in one direction from the control group of convicts (who didn't go through the program). This was done separately for two different variables: whether they were enrolled in a CEO transitional job, and then whether they committed a felony within 3 years of release. The z- and chi-tests both revealed the same thing for each variable. The null was rejected in the first case, and it was concluded the program group convicts were significantly more likely to be employed in a CEO job. We failed to reject the null in the second case, which stated program group convicts commited the same or more felonies over three years than the controls.

#Assignment 4
**Group/Contribution:** I worked on this assignment mainly with Nonie Mathur and Kristi Korsburg, and also with Santiago Carillo. Kristi, Nonie, and I brainstormed together how to code the pairing and sorting aspect of the Pearson's test. Kristi helped me with the code to get my date/time values correct so I could display the data in tables in the beginning. We all talked through what the statistics/p-values meant and what that meant for the null hypothesis. I went through and actually wrote this all up on my own later.

**Assignnment Scope:** All these tests (K-S, Pearson's, Spearman's) were testing whether correlations existed between the ages of the two gender groups. K-S specifically looks at if the two groups have the same age distributions, while the other two tests see if and what kind of linear relationship exists between the genders regarding their ages. In all cases, the null was rejected, implying that there is a correlation between the ages among male and female Citi Bike users.
