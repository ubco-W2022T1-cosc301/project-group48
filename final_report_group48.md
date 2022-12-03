
# Introduction 

Our dataset consists of people killed by law enforcement in the United States, both on duty and off duty. Although Congress instructed the Attorney General in 1994 to compile and publish annual statistics on police use of excessive force, this was never carried out, and the Federal Bureau of Investigation does not collect these data. Therefore, we believe that it is crucial to examine this dataset and explore it to find any inconsistencies with the way the law enforcement uses its power. This helps maiantain transparency within the country and accounts for the actions of the law enforcement. 

In this project, we will we exploring three research questions:
1. Are there any trends between the race & age of the victim and the number of shootings by law enforcement in the United States? 
1. Sahil Research Question
1. Sahraj Research Question

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


## RQ 2:
## RQ 3:

# Conclusion

