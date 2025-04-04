import pandas as pd 
file_path = "/Users/chelsea/Documents/local_business_dashboard/data_analysis/kaggle_data/Students_Grading_Dataset.csv"
try:
    df= pd.read_csv(file_path)
    print("Data loaded succesfully into the dataframe 'df'.")
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nDatFrame information:")
    df.info()
except FileNotFoundError:
    print(f"Error:File not fount at {file_path}")
except Exception as e:
    print(f"An error occured:{e}")