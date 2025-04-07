#With string manipulation one  can perform different forms of manipulation 
#a)Combining the first and the last name .str.cat(othe,sep'')
#b)Extracting information from the student id .str[index] and .str[start:end]string indexing to extract specific characters from each string in the series 
#c)Case Conversion of names .str.lower() .str.upper()
#d) Anlyzing Family income level .str.contains(pattern,case=True , na=False)
#e)Checking for specific First and last letter names 



import pandas as pd
file_path = "/Users/chelsea/Documents/local_business_dashboard/data_analysis/kaggle_data/Students_Grading_Dataset.csv"
df = pd.read_csv(file_path)
#display the first few rows of the dataframe
print(df.head())

df['Full_Name']=df['First_Name'].str.cat(df['Last_Name'],sep='')#creates a new column named Full_Name in the dataframe 'df' .It concatenates the strings from the first name colunm to that of the last name using a ('')as the seperator
print('\nCombined Fullname')
print(df[['First_Name','Last_Name','Full_Name']].head())
 #Extracting information from the student id
 #Example of extractingpotential cohort (Asumming s and the next few digits indicate a cohort)
df['Cohort']= df['Student_ID'].str[:5]
print('\n Extracted Student_ID Prefix')
print(df[['Student_ID', 'Cohort']].head())
#Case conversio of names 
df['FirstName_Lower']= df['First_Name'].str.lower()
df['Last_Name_Upper']=df['Last_Name'].str.upper()
print(df[['First_Name','FirstName_Lower','Last_Name','Last_Name_Upper']].head())
#Analyzing family income level 
df['isHighIncome']= df['Family_Income_Level'].str.contains('High',case=False , na=False)
df['isLowIncome']=df['Family_Income_Level'].str.contains('low',case=False ,na=False)
print(df[['Family_Income_Level','isHighIncome','isLowIncome']])
#Checking for specific First and last letters names 
#Checks whether the first name starts with 'A' (case -insentive)
df['FirstNameStartsWith_A']=df['First_Name'].str.startswith('a' )
#Checks last name ending with 'n' 
df['LastNameEndsWith_n']=df['Last_Name'].str.endswith('n')
print(df[['FirstNameStartsWith_A' ,'LastNameEndsWith_n']])