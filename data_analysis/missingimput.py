# In the data cleaning, we are going to learn how to
# a) Identify and handle missing values
# b) Data type conversion
# c) String manipulation (cleaning and transforming text data)
# d) Adding, Removing and Modifying Columns Reshaping your dataframe to better suite your analysis
import pandas as pd

file_path = "/Users/chelsea/Documents/local_business_dashboard/data_analysis/kaggle_data/Students_Grading_Dataset.csv"
try:
    df = pd.read_csv(file_path)
    print("\nCheck for missing values in the Dataframe")
    # Check for any missing values in the entire dataframe ()
    # True if any missing values exists
    print("\n Are there any missing values in the dataframe?", df.isnull().any().any())
    # Count the number of missing values in each column
    print("\n Number of missing values per column:")
    print(df.isnull().sum())
    # Get a boolean dataframe indicating where values are missing
    print("\n Dataframe showing missing values (True where missing, False otherwise -first 5 rows) ")
    print(df.isnull().head())

    # In the process of handling missing values and other things that you can do is
    # imputation ( This is substituting the missing values with common values such as mean , median , mode , constant value imputation )
    # in missing values , we can also implement the dropping of rows or columns that contain the missing values

    # Inputting values using mean
    print("\n--Inputting missing value using attendance %--")
    # Calculate the mean of the 'Attendance (%)' column
    mean_attendance = df['Attendance (%)'].mean()
    print(f"Mean Attendance:{mean_attendance:.2f}% ")
    # Fill the missing values in 'Attendance (%) with the mean
    df['Attendance (%)'].fillna(mean_attendance, inplace=True)
    # verify that the missing numbers have been filled
    print("\nNumber of missing values in Attendance (%) after mean imputation:", df['Attendance (%)'].isnull().sum())

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")