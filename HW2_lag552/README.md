##Assignment 1

**Contribution:**

I worked in a group with Nannie Mathur, Sanatiago Carrillo, Alexey Kalinin, and Felipe Gonzalez on this assignment. 
Alexey helped us understand how to read and created a path using the dictionaries. 
Felipe helped us out a lot in general when writing python script in compute.
Dr. Bianco helped me understand how to use the sys.argv function to link the API code and busline choice to my script. 
In general, we worked together to figure out the correct format for this code.

**Process Summary:**

I worked first in a jupyter notebook and went step by step to try to create the code that would pull the right info.
This involved reading the data dictionary from the bustime url, then going through to write out the correct pathway to
lead to each variable I needed (i.e., latitude, longitude). 
Then I had to format the code to it display this info, the busline, and pulled the number of active buses like described
in the homework.
Copying this code into an emacs file in compute, I then replaced my own API key and bus selection with the sys.argv functions
so someone else could enter their own info to display data for other buses.

##Assignment 2

**Contribution:**
I wrote most of this code alone (or attempted to), but then met again with Nonie and Santiago, and also Kristy Korsberg who 
helped us all understand how to correctly write the r.write function to correctly create a third command that created a csv 
file output. They all helped me understand the If-Else correct formatting too.

**Process Summary:**
Following a similar process as above, but also had to search for the dictionary path for stop name and status.
Also, I had to code and If-Else statement in case no information was contained in OnwardCalls for that stop.
(A note - I assumed in my code that the output for no information would contain (or add to) 0. I tried to test this 
with several buses, but didn't find one that showed no information. Dr. Bianco said it was fine just to note it for
this assignment, but to understand in a real job, we'd have to look at the csv file data itself to see how it is actually
formatted for N/A values to make sure it's coded correctly.)
This assignment included the additionaly step of including a command that would create the csv file for the selected bus, 
which was done using the r.write function and a third sys.argv. 

##Assignment 3

**Contribution:**
I worked with Nonie, Santiago, and Kristy again for this assignment. Also, I got help from Laura Bligh via email (though she's
now dropped the class). Laura figured out a lot of the code which helped guide me to do most of this on my own, but then Kristy
showed me how to correctly write the pd.read_csv function (looking up the cssv file full path in compute). Dr. Bianco showed me 
how to connect my two variables in the graph so they were plotted against each other. 
Later, I guided Alexey and Adrien through all of Assignment 3.

**Process Summary:**
I verified that DFDATA was an environmental variables in the CUSP Data Facility (DF) with the env function.
I then used compute to find the full pathway of the csv file I'd selected in the DF, and combined it with the environmental
variable DFDATA to pull the csv file into my notebook. I then chose two numerical columns and cut the rest, then plotted them
against each other.

##Extra Credit

**Contribution:**
After understanding Assignment 3, I did most of this on my own. I did receive help from Dr. Bianco, who taught me about the
pd.to_datetime function so I could change the dates in the dataset to values that could be plotted. 
(*Note: We had some trouble creating a scatterplot - Dr. Bianco ultimately determined that the dataset I chose couldn't handle 
a scatter function, and that the graph I have is all right because of this.)

**Process Summary:**
