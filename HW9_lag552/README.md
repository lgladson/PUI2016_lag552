# HOMEWORK 9 

### Contribution:

I worked through Tasks 1-2 on my own, and cross-checked my work with Maisha. I received some help, however, from Himanshu and Dr. Bianco on downloading the data, since I was having some technical issues using the ordinary functions (Dr. Bianco  had me use the wget function instead, which worked) I also helped Alexey with some of the downloading issues and coding for Task 1. For Task 3, I was stuck writing the loop and wound up getting help from Maisha, who showed me her code and I looked over her work carefully to make sure I understood as I adopted her method for this task. Before that, I got help from Dr. Bianco on finding the right index to use and understanding the theory behind it, and also worked a bit with Pooneh. Additionally, Kristi showed me her code for Task 3, though I didn't use her method in the end.

### Task 1 Summary: 

For this task, I collapsed my data into a 1-dimensional array of weeks, and found the week where ridership dropped below 3-sigma from the mean. This was a prominent event, and from researching it discovered this was when Hurricane Sandy hit the city. 

### Task 2 Summary: 

For this task, I only collapsed the station portion of the array, so that I had a 2-dimensional array of weeks and card types. I then found the mean rides for the first and last 10 weeks and created ratios for each card type to determine which increased and decreased most in ridership over this time period. Since I was looking for **constant** trends in the data, I looked at the top ratios (for both increasing and decreasing ridership) and skipped those that did not have steady trends. This assessment was done visually, though it could also be done analytically. 

### Task 3 Summary: 

For this task, I had to identify the 4 stations that showed the most prominent periodic trend over annual periods. First, I collapsed the card types data to form a 2-dimensional array of weeks and stations. Then, I found to use the 4th index which correlated to an annual trend (1/52 weeks), using 1 sample station. I created a loop function (from Maisha's code) that pulled the power analysis for the 4th index of each station, then sorted that to get the top 4 stations with the highest power (which indicateds highest periodicity). I plotted these stations period trends over the whole time frame to examine when the trends were occuring - discovering that drops occured consistently in winter months, and increases in summer months (likely due to tourism). 
