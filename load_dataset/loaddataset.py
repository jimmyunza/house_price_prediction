#***************************************************
#**************** IMPORT LIBRARIES******************
#***************************************************
import os
import zipfile
import pandas as pd 

#***************************************************
#********ABSTRACT CLASS FOR DATASET LOADER**********
#***************************************************

class LoadDataset():
    def loader(self, file_path:str)-> pd.DataFrame:
        #abstract method to ingest data
        """
        Abstract method to load dataset

        Parameters: Takes file path as a string

        Return: None
        """
        pass
#*****************************************************************
#***** implementation of concrete class for .Zip file loader ******
#*****************************************************************
class ZipDataset(LoadDataset):    
    def loader(self, file_path:str)-> pd.DataFrame:
        '''
            Extract .zip files and return a pandas Dataframe
            Parameters:
                Takes file path of .zip files containing datasets as a string
            Returns:
                DataFrame
        
        '''
        # check if file is .zip file
        if not file_path.endswith('.zip'):
            raise ValueError('File not a .zip File')
        
        #Extract the zip file to extracted data directory
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall("extracted_data")

        # Find the extracted supported file
        extracted_files = os.listdir("extracted_data")
        csv_files = [file for file in extracted_files if file.endswith((".csv", ".json",".xlsx"))]

        if len(csv_files)== 0:
            raise FileNotFoundError ('No supported file found in extracted_data. Supported types : ".csv", ".json",".xlsx"')
        elif len(csv_files) >1 :
            raise ValueError("Muiltiple supported files found. Please specify which one to use")
        else:
            # read supported file into DataFrame
            # select the first supported file in the extracted data directory
            csv_files_path = os.path.join('extracted_data', csv_files[0])
        
        # load dataset and return a Dataframe
        if csv_files_path.endswith(".csv"):
            df=pd.read_csv(csv_files_path)
        elif csv_files_path.endswith('.json'):
            df=pd.read_json(csv_files_path)
        elif csv_files_path.endswith(".xlxs"):
            df=pd.read_excel(csv_files_path)

        #Return the Dataframe
        return df
    
#*************************************************************************
#************ Implementation Factory for Dataset Loader ******************
#*************************************************************************
class LoadDataFactory:
    def get_data_loader(file_extension:str)-> LoadDataset:
        ''' Method takes a single parameter and check if it is of correct type and return a correct instanct of LoadData 
            Parameter:
                file extention as a string e.g .zip

            Returns:
                Instance of class LoadDataset (in this case it returns ZipDataset)        
        '''
        if file_extension=='.zip':
            return ZipDataset()
        else:
            raise ValueError(f'No Data Loader available for file extension: {file_extension}')

# Example Usage
if __name__ == "__main__":
    # specify file path
    file_path ="/Users/De/Documents/HexSoftwares/house_price_prediction/houseprice.zip"

    # Determine the file extension
    file_extension = os.path.splitext(file_path)[1]

    ## Get appropriate Data Loader
    data_loader =LoadDataFactory.get_data_loader(file_extension)
    ##  load data into dataframe
    df = data_loader.loader(file_path)

    ## df contains the dataframe from Extracted csv
    print(df.head())
    

