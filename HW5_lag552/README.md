#Homework 5

##Assignment 1

**Contribution:** Worked with Nonie Mathur, Santiago Carillo, and Alexey Kalinin. Alexey and Santiago helped me understand some of the test code set-up; also Dr. Bianco helped me troubleshoot some of the graphing issues. Santiago, Nonie, and I worked together through most of this. 

**Process:** I used the K-S and A-D tests to see if the age distribution of citibike riders fit either a normal or logistic distribution. Part of the process involved pulling the mean and standard deviation from the age data in order to run the K-S scipy.stats.ks function arguments correctly. I ultimately rejected the null hypotheses for both tests under both model distributions, determining that the age distribution did not fit either a normal or logistic distribution. 

##Assignment 2

**Contribution:** Worked with Kristi Korsberg through most of this, who shared her code with me. I helped her understand the matrix scatterplot interpretation. Also worked with Nonie and Santiago and shared some of what Kristi showed me with them. 

**Process:** Looked at income data by gender and race to examine income disparity between men and women. First, we plotted a scatter matrix of several variables from the dataset against each other, looking for trends in things like income amount and disparity, separated by gender. This exploratory data didn't show much difference between the genders. However, once we plotted income by race of men vs. women, the disparity became clear, and best fit lines and regression models showed that women make less then men in all race groups. 

##Assignment 3

**Contribution:** I worked through on my own first, then discussed it with Nonie and Santiago. I also offered Kristi some guidance on this section.

**Process:** Simply writing null hypothesis and equations for several experimental setups, answers below:

# Null Hypotheses Exercise

**1. Do diets help lose more fat than exercise? Experimental setup: you have a test and a control sample.**

*Null Hypothesis:* An average person who diets loses significantly less or equal fat compared to a person who exercises, alpha = 0.05.

*H0 Formula:* Fat loss (diet group) <= Fat loss (exercise group)

**2. Do Americans trust the president? POLL RESULTS: On May 16, 1994, Newsweek reported the results of a public opinion poll that asked: “From everything you know about Bill Clinton, does he have the honesty and integrity you expect in a president?” (p. 23). Poll surveyed 518 adults and 233, or 0.45 of them answered yes.**

*Null Hypothesis:* The same or lower percentage of Americans trust the president (Bill Clinton) than those who do not, alpha = 0.05.

*H0 Formula:* % Americans who trust Bill Clinton <= % Americans who do not trust Bill Clinton

**3. Effectiveness of nicotine patches to quit smoking. Experimental setup: measure cessation rates for smokers randomly assigned to use a nicotine patch versus a placebo patch.**

*Null Hypothesis:* The cessation rate of smokers using nicotine patches is the same or less than the cessation rate of smokers using placebo patches, alpha = 0.05.

*H0 Formula:* Cessation rate of smokers (nicotine patches) <= Cessation rate of smokers (placebo patches)

**4. Quantify the danger of smoking for pregnant women. Experimemtal setup: measure IQ of children at ages 1, 2, 3, and 4 years of age.**

*Null Hypothesis:* Children born to smoking mothers have the same or higher IQs in early childhood than children born to nonsmoking mothers, alpha = 0.05.

*H0 Formula:* Children's IQ (born to smoking mothers) >= Children's IQ (born to nonsmoking mothers)
