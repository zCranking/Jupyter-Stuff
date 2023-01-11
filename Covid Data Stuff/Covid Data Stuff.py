# %%


# %%
print("Name : Arav Gupta")
print("This is a CSV of more than 200 rows which has Covide data.")
print("The task is to find out top 5 the countries who are least affected by covid")
print("Another task is to find out top 5 the countries who has the maximum number of deaths")
print("Another task is to find out top 5 the countries who has the maximum number of active cases")


# %%
#Covide Data 
import  numpy as np
import pandas as pd
from matplotlib import pyplot as plt


dataframe = pd.read_csv('covid19.csv')
df = dataframe.dropna()
df

# %%
#Task 1 
#Sort the data as per total number of cases
sort_byCasesD = df.sort_values(by='total_cases', ascending=False)
print(sort_byCasesD)

# %%
#Task 2
#Get top 5 countries who has the least number of cases and plot a bar graph
lowest_5Cases = sort_byCasesD.tail(5)
print(lowest_5Cases)


# %%
#Task 3
#Sort the data as per total number of deaths
sort_byDeaths = df.sort_values(by='total_deaths', ascending=False)
print(sort_byDeaths)

# %%
#Task 4
#Get top 5 countries who has the maximum number of deaths and plot a bar graph
top_5Deaths = sort_byDeaths.head(5)
print(top_5Deaths)

plt.xlabel('Countries')
plt.xticks(rotation='vertical')
plt.ylabel('Number of Deaths')

label= top_5Deaths['country']
value = top_5Deaths['total_deaths']

plt.bar(label, value, width=0.4, color=('red', 'blue', 'yellow', 'green', 'orange'))



# %%
#Task 5
#Sort the data as per active cases
sort_byActive = df.sort_values(by='active_cases', ascending=False)
print(sort_byActive)


# %%
#Task 6
#Get top 5 countries who has the maximum number of active cases and plot a bar graph
top_5Active = sort_byActive.head(5)
print(top_5Active)

plt.xlabel("Countries")
plt.xticks(rotation="vertical")
plt.ylabel("Active Cases")

label = top_5Active['country']
value = top_5Active['active_cases']
plt.bar(label, value, width=0.4, color=('red', 'blue', 'green', 'yellow', 'orange'))


# %%


# %%



