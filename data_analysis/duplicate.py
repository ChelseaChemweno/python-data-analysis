#Identifying Duplicate Rows (based on columns)
#Display the actual duplicate rows (based on columns)
#Removing Duplicate Rows (Keeping the first occurence)
#Removing Duplicate ROws (keeping the last occurence )
#Removing Duplicate Rows (dropping all the last occurence )
#Important
print('Remember to choose the right method for handling duplicates based on your specifc analyisis goals')
print('Sometimes duplicate might indicate errors in data entry, while other times they might represent valid repeated data points')

import pandas as pd
file_path= "/Users/chelsea/Documents/local_business_dashboard/data_analysis/kaggle_data/Students_Grading_Dataset.csv"
try:
    df=pd.read_csv(file_path)
    print("Original DataFrame Shape:" ,df.shape)
    print("Print the first rows of the original Dataframe")
    print(df.head())
except FileNotFoundError:
    print("Error:File not found at {file_path}")
    df=None
    if df is not None:
        print("\n" +"=" *30 +"\n")
         #Identifying Duplicate Rows (based on columns)
duplicates_all=df.duplicated()
print("Boolean Series indicating duplicate rows (based on columns):")
print(duplicates_all.head())
print("\nNumber of duplicate rows (based on all columns):",duplicates_all.sum())
print("\n" +"=" *30 +"\n")
#Identifying Duplicate Rows (Based on all columns)
if duplicates_all.sum() > 0:
        print("Actual duplicate rows (based on all columns):")
        print(df[duplicates_all])
        print("\n" + "="*30 + "\n")
        # 2. Identifying Duplicate Rows (based on a subset of columns)
    # Let's consider 'First_Name', 'Last_Name', and 'Email' as potentially identifying a student
duplicates_subset = df.duplicated(subset=['First_Name', 'Last_Name', 'Email'], keep=False)
print("Boolean Series indicating duplicate rows (based on 'First_Name', 'Last_Name', 'Email'):")
print(duplicates_subset.head())
print("\nNumber of duplicate rows (based on 'First_Name', 'Last_Name', 'Email'):", duplicates_subset.sum())
print("\nRows that are duplicates based on 'First_Name', 'Last_Name', 'Email':")
print(df[duplicates_subset].sort_values(by=['First_Name', 'Last_Name', 'Email']))
print("\n" + "="*30 + "\n")
# 3. Removing Duplicate Rows (keeping the first occurrence)
df_no_duplicates_first = df.drop_duplicates()
print("DataFrame shape after removing duplicates (keeping first):", df_no_duplicates_first.shape)
print("\nFirst few rows of DataFrame with duplicates removed (keeping first):")
print(df_no_duplicates_first.head())
print("\n" + "="*30 + "\n")
    # 4. Removing Duplicate Rows (keeping the last occurrence)
df_no_duplicates_last = df.drop_duplicates(keep='last')
print("DataFrame shape after removing duplicates (keeping last):", df_no_duplicates_last.shape)
print("\nFirst few rows of DataFrame with duplicates removed (keeping last):")
print(df_no_duplicates_last.head())
print("\n" + "="*30 + "\n")
  # 5. Removing Duplicate Rows (dropping all occurrences)
df_no_duplicates_all = df.drop_duplicates(keep=False)
print("DataFrame shape after removing all duplicate rows:", df_no_duplicates_all.shape)
print("\nFirst few rows of DataFrame with all duplicates removed:")
print(df_no_duplicates_all.head())
print("\n" + "="*30 + "\n")





