import pandas as pd

# Each column in the DataFrame is a Pandas Series
file_path = "/Users/chelsea/Documents/local_business_dashboard/data_analysis/kaggle_data/Students_Grading_Dataset.csv"  # Make sure this is correct

try:
    # Load the data into a DataFrame and assign it to 'df'
    df = pd.read_csv(file_path)

    # Now you can work with the 'df' DataFrame and its Series (columns)
    gender_series = df['Gender']
    print(type(gender_series))
    #printed the first five rows 
    print(gender_series.head())

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")