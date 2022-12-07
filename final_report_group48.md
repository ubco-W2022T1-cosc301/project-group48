
# Introduction 

Our dataset consists of people killed by law enforcement in the United States, both on duty and off duty. Although Congress instructed the Attorney General in 1994 to compile and publish annual statistics on police use of excessive force, this was never carried out, and the Federal Bureau of Investigation does not collect these data. Therefore, we believe that it is crucial to examine this dataset and explore it to find any inconsistencies with the way the law enforcement uses its power. This helps maiantain transparency within the country and accounts for the actions of the law enforcement. 

In this project, we will we exploring three research questions:
1. Are there any trends between the race & age of the victim and the number of shootings by law enforcement in the United States? 
1. Trends in shooting for people belonging to marginalized communities, example women, people of colour, people with mental issues, people belonging to older age groups. 
1. Trends in differences between races in threat level, number of incidents through the years and level of safety based on location.

----
# Exploratory Data Analysis (EDA)

I will first find out how kany unarmed victims are present in the datatset since I will be focusing on these victims to answer my research question.

![Null Values in the dataset](images/eda2.png)
<br/>
![Null Values in the dataset](images/eda1.png)

Since, this dataset is based on real time events, we expected it to have few null values however, we would not be able to analyse these values. In the above image, you can see the number of null values in each column and therefore, we decided to remove all null values from the dataset. 




----
# Data Analysis


## **Research Question 1:** 
### **Are there any trends between the race & age of the unarmed victim and the number of shootings by law enforcement in the United States? (Manav)**

<br/>

To explore my research question, we would only focus on unarmed victims therefore, I have used a dataset with only victims that were unarmed. First, we would explore the percentage of unarmed victims of each race. To do this I will plot a pie graph which depicts percentages of each race, as seen below.

We would also graph a countplot that depcicts the number of shootings of unarmed victims of each race. 

![Pie chart showing the race of victims in the police shootings](images/race1.png)

![Countplot showing the number of victims of each race](images/race2.png)

With the above visualizations, we can observe that White people have been killed the most followed by Black and Hispanics. Even though, this seems to be coinciding with the population of the country, we can see that 33.80% of the unarmed victims were black even though there are only around 12% of black population in the United States. These could possibly imply some form of racism in the law enforcment of the country. 

We would know look intk the age of the unarmed victims. We will plot a histogram to depict the distribution of age of the unarmed victims. 

![Histogram showing the dsitribution of the age of the victims](images/age.png)

With the above histogram, we can observe that most of the victims are aged between 20-40 years of age. The kde (yellow plotted line) also shows that the distribution of the age between 20-40 years of age as well. This is very believable since generally people between the age of 20-40 years usually commit crimes. 


## Research Question 2:
### **Trends in shooting for people belonging to marginalized communities, example women, people of colour, people with mental issues, people belonging to older age groups.? (Sahil)**
<br/>

To explore my research question, I used various kinds of visualizations to see trends in various scenarious during the shootings. 
![Mental illness plus race vs counts](images/screenshot(40).png)

<br/>
When looking at marginalized communities I looked at people of colour, people who are too young or old, and people who are not mentally well. 
There were approximately 2000 cases in which someone who was not mentally well was involved. When looking at the graph of mentall-ill plus race vs count, the people belonging to hispanic and black communities has the highest counts after white people, even though their population sizes were quite different. After that coming to the graph which compares the gender, bases on counts of shooting, females were involved in a lot less cases than men. 
Lastly when we look at marginalized communities, we looked at the age vs counts of shooting graph from which we can draw out the conclusion that children an elderely were involved in barely any counts of shooting , whereas people belonging to the range of 20 to late 40 had the most counts.

![Gender plus mental illness vs count](images/screenshot(41).png)

![Race vs Age and Race pie chart](images/screenshot(42).png)
## Research Question 3:

### **Trends in differences between races in threat level, number of incidents through the years and level of safety based on location. (Sahraj Singh)**
<br/>

To answer my question I began by gathering some information of basic characteristics namely ratio of incidents with attack level threat victims vs. non-attack threat level and count of incidents by race, by year and by state. Then I combined this data to find correlations between these characteristics.

First, I started by plotting the count of incidents by race and by threat vs non-threat victims to see if there are any difference between perception of the race by the police or of culture between each race.

![Incidents by Race Based on Threat Level](images\A1-1.png)

From this, I made the following observations:
1. Asian people, Native peoples, and people belonging to "Other" races show very little difference in "Attack" vs. "Other" threat level victims. Since about 65% of victims are attackers, this could explain why victim counts for these races are comparatively low.
1. White people have ratio of number of attackers to other victims. This could either mean that a higher number of non-threat white people do not become victims of police shootings compared to other races, or that white people have a higher probability of being an "Attack" level threat.
1. Hispanic people have a small ratio of number of attackers to other victims. From this information we can deduce that unarmed Hispanic people have a higher probability of becoming victims than unarmed people of the other races.
<br/>

Next, I plotted number of incidents against the year by race to see how the treatment of each race has changed throughout the years.

![Count of Threat vs Non-Threat Victims by Race](images\A1-2.png)

We can gather that:
1. Number of Asian victims, Native victims, and people belonging to "Other" races remained somewhat constant through the years.
1. Number of white victims reduced gradually but significantly from 2015-2022.
1. Number of Black and Hispanic victims remained somewhat constant up until 2021 and reduces slightly in 2022. This can be explained by the COVID-19 pandemic.

Then, I plotted number of incidents by state and race to see the differences in the treatment of different races in each state.

![Count of incidents through the time period by Race](images\A1-3.png)

From this heatmap, we can see that:
1. California and Texas have an unnaturaly high number of Hispanic victims.
1. Los Angeles and Maryland have more black victims that white victims which completely goes against the trend of population within these communities.
1. Rhode Island, the state with the lowest number of shootings only has Black and Hispanic victims.

Finally there are a few more visualisations available in the dashboard but to finish off I created a map to show density of incidents by area.

![Map of Incidents](images\A1-4.png)

Here we can see that police shootings are much more widespread in the East than in the West. We can see some highly concentrated areas in the west such as in the states of California, Washington and Arizona and central America such as Texas.Moving from west to east the climate becomes increasingly more unsafe. The East side on the other hand seems to be generally unsafe in the case of police shootings. This might be due to a shift in policing culture and political factors. 







# Conclusion
(Sahraj Singh)

**Is there a difference between the ratio of threatening and non-threat victims of each race?**

Yes, white people have the highest ratio of "Attack" level to non-attack level victims. Black people come second and hispanic people third in that regard. This indicates that Black and Hispanic people have a higher probability of being victmized while not being a threat. Asian people, Native peoples, and people belonging to other races showed even lower ratios, this could be due to differences in culture.

**Has treatment of different races by the police changed through the years?**

Number of white victims involved in police shootings saw a gradual yet significant decrease throughout the time-period. Number of victims of all other races remained somewhat constant except in 2022 where we saw a significant decrease in the number of shootings in general. This can be explained by the COVID-19 pandemic.

**Are some areas(states) safer than others for people of different races?**

Yes, California and Texas are comparatively unsafe for Hispanic people in the span of 8 years about 330 incidents took place in California with Hispanic victims. Los Angeles and Maryland are comparatively unsafe for black people as the ratio of black people involved in incidents is high as compared to other races and their population sizes. Rhode Island, the state with the lowest number of shootings only had black and hispanic victims. A trend of targeting people of color can be seen in certain states that goes completely against intuition based on the populations of these races in the state. Some areas such as the dense clusters of incidents in the west should be avoided, in the east however specific location does not seem to be a deciding factor and the area seems to be unsafe in general.
