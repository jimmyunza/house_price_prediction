#importing libraries
import pandas as pd
import logging


#setup logging configurations
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s -%(message)s")

#****************************************************************************************
#*******************Abstract Classs  for Handling Missing Values ***********************
#****************************************************************************************

class HandlingMissing():
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        ''' Performs stragesties for handling missing values
        Parameters:
        df(pd.Dataframe): Takes Dataframe as args
        Returns:
        None: 
        '''
        pass

#************************************************************************************
#***************** Drop Missing Values **********************************************
#************************************************************************************

class DropMissingValues(HandlingMissing):
    # Class implements strategy for handling missing values
    def __init__ (self, axis= 0, thresh = None):
        """ 
        parameters:
        axis (int): 0 to drop rows with missing values, 1 to drop column

        thresh (int): the threshold for non-NA values. Rows/ Column
        
        """
        self.axis = axis
        self.thresh = thresh

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:

        ''' 
        Drops rows or columns with missing values based on the axis and thresh
        Parameters:
        df(pd.Dataframe): takes DataFrame as Args
        Returns:
        DataFrame cleaned 
        '''
        logging.info(f"Dropping missing values with axis={self.axis} and thresh = {self.thresh}")
        df_cleaned = df.dropna(axis=self.axis, thresh= self.thresh)
        logging.info("Missing Values Dropped")
        return df_cleaned
    
# ********************************************************************
#**************** Filling Missing Values *****************************
#*********************************************************************

class FillMissingVaulues(HandlingMissing):
    def __init__ (self, method= "mean", fill_value = None):
        """ 
        parameters:
        mean (str): 0 to drop rows with missing values, 1 to drrop column

        fill_value (any): the threshold for non-NA values. Rows/ Column
        
        """
        self.method = method
        self.fill_value = fill_value

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:

        ''' Fill  rows or columns with missing values based on the axis and thresh values
        Parameters:
        df(pd.DataFrame): Takes dataframe as arg
        Returns:
        Dataframe: returns cleaned dataframe 
        '''
        logging.info(f"filling missing values with method = {self.method}")
        
        df_cleaned = df.copy()

        if self.method == "mean":
            numeric_columns = df_cleaned.select_dtypes(include="number").columns
            df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(
                df[numeric_columns].mean()
            )
        elif self.method == "median":
            numeric_columns = df_cleaned.select_dtypes(include="number").columns
            df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(
                df[numeric_columns].median()
            )


        elif self.method ==  'mode':
            for column in df_cleaned.columns:
                df_cleaned[column].fillna(df[column].mode().iloc[0], inplace=True)
        
        elif self.method == 'constant':
            df_cleaned = df_cleaned.fillna(self.fill_value)
        
        else:
            logging.warning(f"Unknown method '{self.method}'. No missing values")

        logging.info('Missing Values filled')
    
        return df_cleaned
    
# *******************************************************************
#************ Context Class for Handling Missing Values *************
#********************************************************************

class MissingValueHandler:
    def __init__(self, strategy:HandlingMissing):
        ''' Initializes the Missing Value Handler with specific data analysis method

        Parameters:
            strategy (HandlingMissng): the strategy to be used

        Returns:
            None
        '''
        
        self._strategy = strategy

    def set_strategy (self, strategy:HandlingMissing):
        ''' Sets new Strategy for the HandlingMissing
        
        Parameters:
        strategy (HandlingMissing ): The new strategy to be implemented

        Returns:
        None
        '''
        logging.info('Switching missing value handling strategy')
        self._strategy = strategy

    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        '''Executes the inspection using the current strategy.

        Parameters:
        df (pd.DataFrame): the dataframe to be inspected

        returns:
        None: Executes the strategys for handling missing data method 
        '''

        logging.info("Executing missing value handling strategy")
        return self._strategy.handle(df)
    
# Example Usage

if __name__ == "__main__":
    
    # df = pd.read_csv("./extracted_data/data.csv")

    # # Initilize muissing value handler with specific strategy

    # missing_value_handler = MissingValueHandler(DropMissingValues(axis=0))
    # df_cleaned = missing_value_handler.handle_missing_values(df)


    # # switch to filling missing values with mean

    # missing_value_handler.set_strategy(FillMissingVaulues(method='mean'))
    # df.filled = missing_value_handler.handle_missing_values(df)

    


    pass