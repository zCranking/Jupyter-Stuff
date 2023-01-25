# %%
print("Name : Arav Gupta")
print("This is a CSV of more than 1300 rows which has bmi data.")
print("The task is to find out what is the percentage of people who are underweight and healthy. And plot a pie chart around it")
print("Another task is to find out what is the percentage of male and female who are underweight and healthy. And plot a pie chart around it")



# %%
#BMI Data

#predefine code
import pandas as pd
import matplotlib .pyplot as plt

dataframe = pd.read_csv("bmi.csv")
df = dataframe.dropna()
bmi = df['bmi']
df


# %%
#Task 1
#How many people are underweight and create a dataframe out of it
underweight_df = df.loc[bmi < 18.5]['gender'].reset_index(name='gender')
underweight_count = underweight_df['index'].count()

print(underweight_df)
print(underweight_count)


# %%
#Task 2
#How many people have normal weight and create a dataframe out of it
healthy_weight = df.loc[(bmi > 18.5) & (bmi < 24.9)]['gender'].reset_index(name='gender')
print(healthy_weight)
healthy_count = healthy_weight['index'].count()
print(healthy_count)

# %%
#Task 3
#Plot a pie chart as per the percentage of people who are underweight and healthy. 
value = [underweight_count, healthy_count]
label = ["underweight", "healthy weight"]
plt.pie(value, labels = label, autopct='%0.1f%%', radius=2)
plt.show




# %%
#Task 4
#Group by the gender from underweight dataframe and create another data frame out of it
group_underweight = underweight_df.groupby('gender')['gender'].count().reset_index(name='number')
print(group_underweight)


# %%
#Task 5
#Plot a pie chart as per the percentage of male and female who are underweight
value = group_underweight['number']
label = group_underweight['gender']

plt.pie(value, labels = label, autopct='%0.1f%%', radius=2)
plt.show


# %%
#Task 6
#Group by the gender from healthy weight dataframe and create another data frame out of it
group_underweight2 = healthy_weight.groupby('gender')['gender'].count().reset_index(name='number')
print(group_underweight2)


# %%
#Task 7
#Plot a pie chart as per the percentage of male and female who are healthy
value = group_underweight2['number']
label = group_underweight2['gender']

plt.pie(value, labels = label, autopct='%0.1f%%', radius=2)
plt.show

# %%



