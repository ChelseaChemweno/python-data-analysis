import kaggle 
kaggle.api.authenticate()
#authenticate with the kaggle API (make sure the kaggle.json file is in ~/.kaggle) 

dataset_name ="mahmoudelhemaly/students-grading-dataset"

#specify the directory to download the files to (optional)
path = "./kaggle_data" #creates a folder named 'kaggel_data' in your current directory
try :
    #Download the datset files 
    kaggle.api.dataset_download_files(dataset_name, path=path,unzip=True)
    print(f"Dataset '{dataset_name}' downloaded and unzipped to '{path}'")
except Exception as e:
    print (f"An error occured :{e}")
    print ("Please ensure that the dataset name is correct and you have the necessary permissions")