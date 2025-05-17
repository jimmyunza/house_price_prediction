
from pydantic import BaseModel
import pandas as pd

# abstract Base Class for Data Inspectiostrategies
#------------------------------------------------
# This class defines common interface for data inpection strategies
# Subclasses must implement the inspect method
class Data_Inspection_Strategy(BaseModel):
    def inspect(self, df: pd.DataFrame):
        ''' Perform a specific type of data inspection.

        Parameters:
        df(pd.Dataframe): the dataframe on which the inspection strategeis are implemented

        Returns:
        None: this prints the inspection results directly

        '''
        pass

# create concrete Strategy for data types  inspection
#--------------------------------------------------
# This strategy inspects the data types of each column and count
class DataTypes_Inspect_Strategy(Data_Inspection_Strategy):
    def inspect(self, df: pd.DataFrame):
        
        '''Inspects and Prints the data types and non-null counts of the dataset
        
        Parameters:
            df(pd.Dataframe): the dataframe on which the inspection strategeis are implemented

        Returns:
            None: this prints the inspection results directly

        '''
        print('\nData Types and Non-null Counts:')
        print(df.info())

# Concrete Strategies for Summary Statistics Inspections
#------------------------------------------------------
# This Strategy provides summary statistics for both numerical and non numerical data
class Summary_Statistics_Inspection_Strategy(Data_Inspection_Strategy):
    def inspect(self, df: pd.DataFrame):
        '''Prints summary statistics for numerical and categorical data
        Parameters:
        df(pd.Dataframe): the dataframe on which the inspection strategeis are implemented

        Returns:
        None: this prints summary statistics to the console
        
        '''
        print('\nSummary Statistics (Numerical Features):')
        print(df.describe())
        print('\nSummary Statistics (Categorical Features):')
        print(df.describe())

# Context Class that uses a Data_Inspection_Strategy
#------------------------------------------------------
#This class allows you to switch between different data inspection 
class Data_Inspector:
    def __init__(self, strategy: Data_Inspection_Strategy):
        '''
        Initializes the Data_inspector with specific inspections

        Parameters:
        strategy (Data_Inspection_Strategy): the strategy to be used

        Returns:
        None
        '''

        self._strategy = strategy
    
    def set_strategy(self, strategy: Data_Inspection_Strategy):
        '''Sets new Strategy for the Data_Inspector
        
        Parameters:
        strategy (Data_Inspection_Strategy): The new strategy to be implemented

        Returns:
        None
        '''
        self._strategy= strategy

    def execute_inspection(self, df: pd.DataFrame):
        '''
        Executes the inspection using the current strategy.

        Parameters:
        df (pd.DataFrame): the dataframe to be inspected

        returns:
        None: Executes the strategy's inspection method 
        '''
        self._strategy.inspect(df)

# Example Usage
if __name__ == "__main__":
    # Example usage if the Data_Inspector with Differnt strategies
    #load Data
    df = pd.read_csv('/Users/De/Documents/HexSoftwares/house_price_prediction/extracted_data/data.csv')

    # Initilize  Data Inspector with Specific strategy
    inspector = Data_Inspector(DataTypes_Inspect_Strategy())
    inspector.execute_inspection(df)

    # Change strategy to summary Statistics and execute
    inspector.set_strategy(Summary_Statistics_Inspection_Strategy())
    inspector.execute_inspection(df)


    pass