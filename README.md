# Jupyter-Stuff
## 8. 1/30/2023 - [Movie Data Stuff](https://github.com/zCranking/Jupyter-Stuff/tree/main/Movie%20Data%20Stuff)

## 7. 1/24/2023 - [BMI Data Stuff](https://github.com/zCranking/Jupyter-Stuff/tree/main/BMI%20Data%20Stuff)

## 6. 1/17/2023 - [Bush Fires](https://github.com/zCranking/Jupyter-Stuff/tree/main/Bush%20Fires)

## 5. 1/10/2023 - [Covid Data Stuff](https://github.com/zCranking/Jupyter-Stuff/tree/main/Covid%20Data%20Stuff)
Yes I know, I know. I should have wrote this summary on 1/10/2023 when I uploded the file and finished the homework project. Sooo... keeping that in mind I am going to keep this summary and write up short. Also I don't remember too much about the project but I will do my best to explain what we did in the project and the stuff we did, and also try and share the meaning and what we learned in this project. As per the title of this project we analysed the [covid19.csv](https://github.com/zCranking/Jupyter-Stuff/blob/main/Covid%20Data%20Stuff/covid19.csv), disecting and analyzing this data in multiple dataframes. So looking at the first picture in the repository is [Active Cases.png](https://github.com/zCranking/Jupyter-Stuff/blob/main/Covid%20Data%20Stuff/Active%20Cases.png), it is showing the countries with the most active covid-19 cases. In oreder to achieve this we had to first import and read [covid19.csv](https://github.com/zCranking/Jupyter-Stuff/blob/main/Covid%20Data%20Stuff/covid19.csv) using ```dataframe = pd.read_csv('covid19.csv')```. Then after that we begin to manipulate the data by sorting the data by the total number of cases using ```sort_byCases = df.sort_values(by='total_cases', ascending=False)```. Then I sorted it by the active cases using ```sort_byActive = df.sort_values(by='active_cases', ascending=False)```.Then I got the top 5 countries using ```.head(5)```, and then finally using ```matplotlib``` to graph the data. Moving onto the second picture in the repository [Number of Deaths.png](https://github.com/zCranking/Jupyter-Stuff/blob/main/Covid%20Data%20Stuff/Number%20of%20Deaths.png), showing the number of deaths for covid-19 cases in each country. In order to achieve this I did the same steps and didn't do the active cases step, then finally taking the top 5 using ```.head(5)```. So to sum it up and what I did in the homework project, I sorted and manipulated data about covid-19 and then graphed it using ```matplotlib```.

## 4. 1/10/2023 - [More Satellite Data 3](https://github.com/zCranking/Jupyter-Stuff/tree/main/More%20Satellite%20Data%203)
This was a fun and easy class project. In this class project we went the ```df.groupby()``` function in the pandas library. It was a very good a versatile function, it is more helpful and does something different than the ```df.sort_values(by='Column Name')```. Here is an example of the function in use ```df.groupby('Form of Title Column')['Grouping By'].count().reset_index()```. In this example we first have the dataframe and the ```.grouby()``` function. Then in the first parameter for the function in the paranthesis is the column you wan to get the data from and acts as sort of a title. To elaborate on that if you have a dataframe that had a column with names of companies Then you would put the title of that column in that parameter slot. This would tie into the next parameter in the square brackets which is the data you want to group by. An example for that would be if you have a column holding the following possible data, open and close and the column has a header of projects. So then you data would start to look like:  
  
**Names of Companies** | **Projects**  
Company 1 | 11  
Company 2 | 17  
Company 3 | 8  

Which would basically mean that the parenthesis got the **Names of Companies**, and the square brackets got all the projects with that companies name listed on it and regardless of the status it got the data and with the help of the ```.count()``` it got the count of all of them. The ```.reset_index()``` made sure that it was proccessing the data from the top of the dataframe instead of starting in the middle.  

Another major thing that I learned was the ```df.loc()``` which is the locate function. This function is pretty self explanatory from the name of the function. It is used to locate and find cells in the dataframe that meeet the first parameter of telling the column, and the second parameter of the data inside cell's column. Here is an example code ```df.loc[df['Column Name'] == 'Data/Message'] ```. This is also very familiar with the function ```pd.DataFrame(df, columns =['Column Name 1','Column Name 2'])```. The difference is the ```df.loc()``` function is used for sorting the data of a specific column and whats inside that column by the cell. The ```pd.DataFrame()``` is used for seperating # of column(s) from a current dataframe. This was also a new and fascinating function that we learned. **_That's going to be a wrap for today._**

## 3. 1/6/2023 - [Satellite Data 2](https://github.com/zCranking/Jupyter-Stuff/tree/main/Satellite%20Data%202)
There wasn't too much different in this class and felt like any other class for me, being able to quickly and easily pick up the lesson for the class and apply them to the project in hand. It sort of felt like all the work I put in yesterday with learning how everything works and getting comfortable with Jupyter Notebook and more comfortable with Github payed off with this project. The class wasn't too complex and was just building off what we learning in the last class. Thats usually how the first few classes go when learning a new concept. In the class the concept that we covered was getting data from columns and then sorting our data sets. We also revised plotting data in the form of a bar graph. For getting data from the columns we used ```df = pd.DataFrame(dataframe, columns=["Name of Column"])```. In order to sort the data and specify which column we want it to be sorted by we used ```sorted_df = df.sort_values(by=["Name of Column"])```. Here is the **.csv** [Jupyter-Stuff/Satellite Data 2/C191_satellite_data.csv](https://github.com/zCranking/Jupyter-Stuff/blob/main/Satellite%20Data%202/C191_satellite_data.csv) we took data from to analyze and manipulate. Below is the code that we used to sort out the data from filled and N/A data, removing the N/A data since it won't be useful to use for now.
```
df2.replace(" ", float("NaN"), inplace=True)

df2 = df2.dropna()
```
All in all that sums up the day and what I learned in my coding journey and I can't wait to learn more. **_That's going to be a wrap for today._**

## 2. 1/5/2023 - [Health Graph](https://github.com/zCranking/Jupyter-Stuff/tree/main/Health%20Graph)
Today was my first homework project using Jupyter Notebook on my own. I was able to succesfully complete the project while further establishing my self into the Jupyter Notebook and how it works. I also explored and used many of the features that Jupyter Notebook had to help me complete and understand some of the errors while working on the project. The first thing I want to talk about is the Jupyter Notebook and the features that I used. Having my code seperated into differnet cells helped with testing certain parts of the code instead of running and going throught the whole code. So it made my workflow a bit faster and helped me organize my code much better. The second thing I want to talk about is the with Jupyter Notebook I was able to easily look at the data from my ```.csv``` files and also the varialbe that had data which was exctracted from the original ```.csv``` using the **data viewer** feature that Jupyter Notebeook offers. It helped me understand what was happening with my code and also fix errors more quickly and efficiently. There are more things to talk about and explore but those can be talked about in later talks. The second thing that I want to talk about is something that mey seem simple but is something I discovered today that helps me with my workflow and makes me more effecient. I was able to make my workflow more effecient with updating repositories that are remote and I need to edit them but I don't want to open up the browser and do it from the comfort of my IDE and also have a copy of the file for safety reasons. I would first ```git clone``` the repositories and then I would just ```git sync``` the changes making it a quick and easy process. It was quite a day for me and I am proud of what I was able to accomplish. **_That's going to be a wrap for today._**

## 1. 1/3/2023 - [Satellite Data](https://github.com/zCranking/Jupyter-Stuff/tree/main/Satellite%20Data)
It was my first class after a while and coming back to coding. But I still had my coding energy and was able to start right where I left off in learning coding. This was the first class that I started using Jupyter Notebook. I was very suprised with that change, but I wasn't excited for the upcoming change and argued how thigns were fine the way we were doing. We weren't changing the language and were still using python. The main we changed to using that was because it already had installed some libraries such as panda and numpy. But that was it and me being me, I had a workaround which most people would have guessed. Just using ```pip install```, and then puting the name of the libraries. The only experience I had with Jupyter Notebook before this was when I was first learning python independently and was just exploring the world of python and what the language had to offer. When I first used it, I thought it would be a good way to test small lines of codes and was a good temporary solution for learning. But I thought to myself when using and working on bigger projects having a pythong file would be easier. But I couldn't have been more wrong. I am sure many people have different opinions but this is what I have to say, Jupyter Notebook can still be used for big projects but of course parts of them and having all of the parts work together through various files to build the final product. But it offeres a variety of organization that you might have to do manually, but many things that you still don't get while using a regualr python file and your choice of IDE. This project in class was only the start of my journey of exploring, learning, and hating Jupyter Notebook whilst learning python. It was a great day learning about Jupyter and what is has to offer, and I can't wait to learn more about it. **_That's going to be a wrap for today._**

