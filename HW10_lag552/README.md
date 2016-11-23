# PUI Homework 10

Contribution: I worked alone on this homework, following along with the provided notebook carefully and adapting its code to Assignment 2.

Assignment 1 Description: 

From the class lab, we imported census tract map data and looked at general population density and learned how to create a map output in python. Then, we imported and looked at time series data for Citibike data and its apparent seasonal trends. We then linked these two datasets and were able to plot citibike rides monthly averages for all the census tracts in the city. We first looked at individual ride differences, then we created lag data which showed how many rides each tract's surrounding tracts averaged. We compared the raw monthly averages with the lag data in maps as well as creating a Moran Scatterplot showing hot (upper right of grid) and cold regions (lower left), showing the best fit I statistic line, and generating the I statistic and its corresponding p-value of significance. We also created KDE density plots to see if they supported our conclusion from the small p-value that the I stat was indeed significant. The KDE supported this conclusion. We also did a LISA Moran scatterplot and analysis, which does the same thing (comparing monthly averages and lag for census tracts) but it does so on an individual basis - in other words, seeing which tracts specifically are significant or not, which was plotted. We then mapped significant hot and cold spots on a map.

Assignnment 2 Description: - describe seasonal effects

For this assignment, the same process as in Assignment 1 was used, but instead of looking at the monthly average of rides for each tract, I pulled the summer and winter months, seperately, from the dataset and took their averages for each tract. Then I went through the above process (twice, essentially) for both summer and winter. 

