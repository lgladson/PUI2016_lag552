# PUI Homework 10

*Contribution: I worked alone on this homework, following along with the provided notebook carefully and adapting its code to Assignment 2.*

*Note: As explained in Dr. Bianco's email, I worked in a normal Python 2 notebook due to the issue with PySal library on PUI2016 kernals, and stored my files in my local directory.*

### Assignment 1 Description: 

From the class lab, we imported census tract map data and looked at general population density and learned how to create a map output in python. Then, we imported and looked at time series data for Citibike data and its apparent seasonal trends. We then linked these two datasets and were able to plot citibike rides monthly averages for all the census tracts in the city. We first looked at individual ride differences, then we created lag data which showed how many rides each tract's surrounding tracts averaged. We compared the raw monthly averages with the lag data in maps as well as creating a Moran Scatterplot showing hot (upper right of grid) and cold regions (lower left), showing the best fit I statistic line, and generating the I statistic and its corresponding p-value of significance. We also created KDE density plots to see if they supported our conclusion from the small p-value that the I stat was indeed significant. The KDE supported this conclusion. We also did a LISA Moran scatterplot and analysis, which does the same thing (comparing monthly averages and lag for census tracts) but it does so on an individual basis - in other words, seeing which tracts specifically are significant or not, which was plotted. We then mapped significant hot and cold spots on a map.

### Assignnment 2 Description:

For this assignment, the same process as in Assignment 1 was used, but instead of looking at the monthly average of rides for each tract, I pulled the summer and winter months, seperately, from the dataset and took their averages for each tract. Then I went through the above process (twice, essentially) for both summer and winter. 

**Seasonal Effects:** First off, there are generally more riders during the summer than during the winter. From my notebook's data I could calculate that the average number of summer and winter rides per census tract was 17276 and 6860, respectively. In other words, there are only about 40% of the number of rides in winter that there are in summer, on average. Already, there is a clear increase in ridership between the two seasons. 

Looking at this geographically, both winter and summer maps of ridership show concentrations in southern Manhattan (below Central Park) which rides decreasing drastically once you go into the other boroughs. This, of course, makes sense since Citibikes are only located for rent inside Manhattan. 

Since heat maps for both summer and winter ride averages and their lags were made independent of the other, it was difficult to tell how much they differed by raw numbers of rides; however, I could see that some changes were occuring between seasons. Most significantly, areas around the southeastern piers in Manhattan and around Central Park went up during the summers, likely due to tourism in these popular spots. 

The Moran scatterplots gave more indication of the differinng averages - since the winter plot had smaller ranges along the axis. Both summer and winter, however, show an I line with a slope of around 0.6, showing a positive correlation between tracts with high ridership in each season and having neighbors with high ridership during that same season. This was determined to be significant from the p-value and KDE plots. LISA autocorrelation allowed me to see that for both seasons, only census tracts with higher lags (which lag was higher for summer, since there were more rides overall that season) were deemed significant hotspots. 

As explained in my notebook, it seems the hotspots (indicating areas where both the census tract and its neighboring tracts have high ridership during a given season) trend in southern Manhattan (and moreso along the western shore than the east), whereas cold spots (indicating areas where both the census tract and its neighboring tracts have low ridership during a given season) trend moreso in Queens along the East River and near where the Queensboro bridge connects in Queens (which makes sense - I see folks biking along this bridge quite often), and in more central areas in Brooklyn. Visually, it is difficult to compare the two seasons - from close inspection, one may notice that a new cold spot appears around where the Brooklyn Bridge connects to Brooklyn during the winter, but it is otherwise very similar. 

I would thus conclude that while ridership certainly decreases in the winter, the actual distribution of where people are riding during these two seasons stays fairly consistent. 
