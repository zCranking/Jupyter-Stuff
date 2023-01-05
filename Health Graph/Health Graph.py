# %%
print("Name : Arav Gupta")

# %% [markdown]
# Importing and reading .csv

# %%
#import the libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#Task 1
#Read the bmi.csv
dataframe1 = pd.read_csv('bmi.csv')

# %% [markdown]
# Sorting data and plotting bar graph

# %%
#Task 2
#Data is sorted in descending order in accordance with BMI value
#Find the top 5 age group where the BMI value is the highest, and plot a bar graph out of it
top_5 = dataframe1.head(5)
print(top_5)
age = top_5["Age"]
bmi = top_5["BMI"]

plt.xlabel("Age")
plt.xticks(rotation="vertical")
plt.ylabel("BMI")

age = age
print(age)

bmi = bmi
print(bmi)

plt.bar(age, bmi, width=0.4, color=("red", "blue", "yellow", "green", "orange"))




# %% [markdown]
# Insulin Data read and plot
# 

# %%
#Task 3
#Read blood_pressure.csv
dataframe2 = pd.read_csv("blood_pressure.csv")

# %%
#Task 4
#Data is sorted in ascending order in accordance with Blood Pressure
#Find the top 5 age group where the BloodPressure value is the highest, and plot a bar graph out of it
top_5 = dataframe2.head(5)
print(top_5)
age = top_5["Age"]
bmi = top_5["BMI"]

plt.xlabel("Age")
plt.xticks(rotation="vertical")
plt.ylabel("BMI")

age = age
print(age)

bmi = bmi
print(bmi)

plt.bar(age, bmi, width=0.4, color=("red", "blue", "yellow", "green", "orange"))


# %% [markdown]
# Insulin data read and tell

# %%
#Task 5
#Read the insulin.csv
dataframe3 = pd.read_csv("insulin.csv")


# %%
#Task 6
#Data is sorted in descending order in accordance with Insulin value
#Find out what will be the Glucose and BMI value when the Insulin is highest
top1 = dataframe3.head(1)
glucoseHigh = top1['Glucose']
bmiHigh = top1['BMI']
print("When insulin is the highest Glucoes is: " + str(glucoseHigh))
print("When BMI is the highest BMI value is: " + str(bmiHigh))



# %%


# %%



