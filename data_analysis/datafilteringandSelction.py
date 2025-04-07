#Selceting a Single Column 
#Selecting Multiple Columns 
#Filtering Based on a conditon 
#Filtering Row Based on Multiple Conditions (AND)
#Filtering Rows Based on Multiple Conditions (OR)
import pandas as pd 
file_path ="/Users/chelsea/Documents/local_business_dashboard/data_analysis/kaggle_data/Students_Grading_Dataset.csv"
try:
    df=pd.read_csv(file_path)
    print("DataFrame loaded Succesfully")
    print(df.head())
except FileNotFoundError:
    print(f"Error:Filenot found at {file_path}")
    df= None
print("1.Selecting the 'First_Name' ,'Last-Name',and 'Grade' columns:")
print(df['First_Name'].head())
print("\n" +"=" *30 +"\n")
#Selection Multiple Columns 
print("2.Selecting 'First_Name', 'Last_Name' , and 'Grade' columns:")
print(df[['First_Name' ,'Last_Name','Grade']])
print("\n" +"=" *30 +"\n")
#Filtering Rows Based on cONDITION (boolean Indexing)
print("3.Students in the cs department")
cs_students = df[df['Department'] == 'CS']
print(cs_students.head())
print("\nNumber of CS Students:" ,len(cs_students))
print(df['First_Name'].head())
#Filtering Rows based on a Multiple Conditions 
print("4.Female Students in the 'Engineering'department:")
female_engineering=df[(['Gender']== 'Female')& (df['Department']== 'Engineering')]
print(female_engineering.head())
print("\nNumber of Female Engineering Students:" ,len(female_engineering))
print("\n" + "="*30 + "\n")
#Filtering Rows based on Multiple conditions (or)
print("5.Students with Grade of 'A' or 'B'")
ab_grade_students=df[(df['Grade'] == 'A')|(df['Grade']== 'B')]
print("\nNumber of students with Grade A or B " ,len(ab_grade_students))
print(ab_grade_students.head())
print("\n" + "="*30 + "\n")
#Filtering Rows using isin()
print("6.Students in Mathematices of Business Deprtment")
math_business_students =df[df['Department'].isin(['Mathematics','Business'])]
print(math_business_students.head())
print("\n" + "="*30 + "\n")
#Selecting rows and Specific columns using .loc (label based)
print("7.FirstName , graade and totalscore for the first 5 students")
engineering_scores =df.loc[df['Department']== 'Enginnering',['First_Name','Department','Final_Score']]
print(engineering_scores.head())
print(math_business_students.head())
#Selecting rows and sopecific columns using .iloc(integer_based)
print("8.First 3  rows and columns at index 0,2, and 5")
print(df.iloc[0:3,[0,2,5]])
print("\n" + "="*30 + "\n")
#All rows and column from index 6 to 9
print(df.iloc[:,6:10].head())
print("\n" + "="*30 + "\n")
