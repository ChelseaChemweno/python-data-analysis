#Data transformation involves modifying the structure , format or values of your data to make it more suitable for analysis 
# 1. Some data transformation techniques 
#a)Creating a new column -combining existing columns , perform calculation or extracting specific information to genrate a new feature that might be insightfull for analysis 
#b)creating a categorical column -This is converting numerical or continious data into discrete categories or labels . Simplifies analysis for certian types of models or visulatizations
#c)Applying a function using built in or user defined functions to modify the vaues within a column(Mathematical functions, string manipulation ,data or time)
#d)Using lamba functions often in methods in python
#e)One hot encoding converting categorical variables into mumerical format that machine learning algorithimns can understand . It creates a new binary column for each unique category 
import pandas as pd 
file_path = "/Users/chelsea/Documents/local_business_dashboard/data_analysis/kaggle_data/Students_Grading_Dataset.csv"
df = pd.read_csv(file_path)
print("Initial data info")
df.info()
print("\nFirst Few rows of the data frame")
print(df.head())
#Creating a New column
df['Average_Exam_Score']=(df['Midterm_Score']+ df['Final_Score'])/2
print("\nDatafarame with average exam score")
print(df[['Student_ID','Midterm_Score','Final_Score','Average_Exam_Score']].head())
#Creating a categorical column (Performance level based on score )
bins=[0,60,80,100]
labels= ['low','Medium','High']
df['Performance_Level']=pd.cut(df['Total_Score'],bins=bins, labels=labels,right=False)
#bins is used to define boundaries for your categories .The values specify where one category ends and the next begins
#Labels is a list of strings that provides the names you want to assign to each if the categories created by the bins
#pd.cut() this is a pandas function that is used for binning continious data into discrete intervals 
#right0False determines which side of the interval is closed 
print("\nDataframe with perfomace level")
print(df[['Student_ID','Total_Score','Performance_Level']].head())
#Applying a function(Rounding Numerical score Colummns)
cols_round=['Attendance (%)','Midterm_Score','Final_Score','Assignments_Avg','Quizzes_Avg','Participation_Score','Projects_Score','Total_Score','Study_Hours_per_Week']
df[cols_round]=df[cols_round].round(2)
print(df[cols_round].head())
#Using lamba function 
df['Passed_Midterm'] = df['Midterm_Score'].apply(lambda x: 1 if x > 60 else 0)
#lamba x defines an anyomous function called x .It takes an arrgument x and aplyies method on the midterm score .
#Checks whether the midterm score x is greater than 60 .if it is true the lamba will return 1 else 0 when false

df['Full_Name'] = df.apply(lambda row: f"{row['First_Name']} {row['Last_Name']}", axis=1)

print("\nDataframe with Passed_Midterm and Fullname")
print(df[['Student_ID','Midterm_Score','Passed_Midterm','First_Name','Last_Name','Full_Name',]].head())

#One-hot-coding(Gender and Department)
#first we create a dummy variable .it takes a Dataframe and a list of of columns as input and returns a new data framewith a specified categorical columns transformed into numerical ones 
df=pd.get_dummies(df,columns=['Gender','Department'],prefix=['Gender','Department'])
print("\nDataFarme with one-hot encoded Gender and Department")
print(df[['Student_ID','Gender_Female','Department_Business','Department_CS','Department_Engineering','Department_Mathematics']].head())
#Many Machine learning algorithims and statistical models can only work with numerical input . Categorically variables need to be transformed into numerical representation. One -hot encoding is a common way to do this without intoducing an ordinal relationship 
#(wHICH MIGTH HAPPEN IF YOU SIMPLY ASSIGN NUMBERS LIKE 0,1,2,TO DIIFERNT DEPARTMENTS)
#Each category gets its own binary column making it easier for models to understand this transformation