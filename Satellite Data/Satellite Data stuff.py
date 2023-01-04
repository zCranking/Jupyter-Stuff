# %%
print("Name :")
print("We will start learning about data visualization, and fetching the data")
print("Plot bar graphs for the countries who has the highest and lowest number of satellites in space")

# %%
#Activity 1 
#Q - Plot a bar graph for top 5 Country/Organization who has the most number of Satellites In Space

import  numpy as np
import pandas as pd
from matplotlib import pyplot as plt

dataframe = pd.read_csv('country_satellites.csv')

top_5 = dataframe.head(5)
print(top_5)
name = top_5['Country/Organization Name']
number = top_5['Satellites In Orbit']


plt.xlabel("Country/Organization Name")
plt.xticks(rotation='vertical')
plt.ylabel("Satellites In Orbit")


label = name
value = number 
plt.bar(label, value,width=0.4, color=('red','blue','green','pink','yellow')) #bar-grap



# %%
#Activity 2
#Q - Plot a bar graph for 20 Country/Organization who has the least number of Satellites In Space


# %%
import  numpy as np
import pandas as pd
from matplotlib import pyplot as plt

dataframe = pd.read_csv('country_satellites.csv')
removingNA = dataframe.dropna()

bottom_20 = removingNA.tail(20)
print(bottom_20)
name = bottom_20['Country/Organization Name']
number = bottom_20['Satellites In Orbit']


plt.xlabel("Country/Organization Name")
plt.xticks(rotation='vertical')
plt.ylabel("Satellites In Orbit")


label = name
value = number 
plt.bar(label, value,width=0.4, color=('red','blue','green','pink','yellow')) #bar-grap


# %%


# %%


# %%


# %%



