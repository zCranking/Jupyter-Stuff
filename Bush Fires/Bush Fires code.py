# %%
print("Name : ")
print("We will learn how to group by date and plot a line graph for the confidence of the data collected by satellites")
print("Then we will group by date and get the maximum brightness and temperature of the fire")
print("And plot a line graph for showing the correlation between brightness and temperature of fire")

# %%
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('australia_bushfire.csv')
df

# %%
#Activity 1
#Group by data and plot a line graph for the average confidence of the satellites for collecting data

group_by_date = df.groupby('acq_date')['confidence'].mean().reset_index(name='confidence')
group_by_date




# %%
label = group_by_date['acq_date']
value = group_by_date['confidence']

fig = plt.subplots(figsize=(19,8))

plt.plot(label, value, label = "Average confidence as per date" , linewidth=3.0)
plt.xlabel('Dates')
plt.xticks(rotation='vertical')

plt.ylabel('confidence')

plt.title('Average confidence as per date', fontsize=20)

plt.legend()

plt.show()


# %% [markdown]
# Conclusion - The data captured by the satellite is almost 65 percent confident (accurate)
# 

# %%
#Activity 2
#Show a correlation between the brightness of fire and temperature of fire using line graph

#First - group by date, and find out Max Brightness and create a dataframe out of it
group_by_brightness = df.groupby('acq_date')['brightness'].max().reset_index()
group_by_brightness



# %%
#Second - group by date, and find out Max Temperature and create a dataframe out of it
group_by_temperature = df.groupby('acq_date')['bright_t31'].max().reset_index()
group_by_temperature

# %%
#Thrid - get the data and brightness from group by date max brightness and store in respective variable
label=group_by_brightness['acq_date']
value=group_by_brightness['brightness']
#Forth - plot first line graph for max brightness by date
fig = plt.subplots(figsize=(19,8))
plt.plot(label, value , linewidth=3.0)
plt.xticks(rotation='vertical')
plt.title('Brightness and Temprature', fontsize=20)
label = group_by_temperature['acq_date']
value = group_by_temperature['bright_t31']
plt.plot(label, value , linewidth=3.0)
plt.legend()
plt.show()
#Fifth - get the data and Temperature from group by date max Temperature and store in respective variable


# %% [markdown]
# Conclusion - 

# %%



