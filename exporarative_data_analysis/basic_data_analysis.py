# import libraries and packages
import pandas as pd

#***********************************************************
#********abstract  Class for Basic Data Inspection**********
#***********************************************************

class Basic_Data_Analysis():
    # This class defines common interface for Basic Data Analysis 
    # Subclasses must implement the Basic Data Analysis methods such as DataFramr[DESC, Information]
    def basic_analysis(self, df: pd.DataFrame):
        ''' 
        Perform a specific type of data inspection.

        Parameters:
            df(pd.Dataframe): the dataframe on which the inspection strategeis are implemented

        Returns:
            None: this prints the inspection results directly

        '''
        pass

#*************************************************************************************
# ********** create concrete Strategy for data types  inspection *********************
#*************************************************************************************

class DataTypes_Analysis(Basic_Data_Analysis):
    # This  inspects the data types of each column and count from the DataFrame
    def basic_analysis(self, df: pd.DataFrame):
        
        '''Inspects and Prints the data types and non-null counts of the loaded dataset
        
        Parameters:
            df(pd.Dataframe): the DataFrame on which the basic Information of the dataset are implemented

        Returns:
            None: this prints the inspection results directly

        '''
        print('\nData Types and Non-null Counts:')
        print(df.info())

#***********************************************************************************
# **************Concrete Strategies for Summary Statistics Inspections**************
#-**********************************************************************************

class Summary_Statistics_Analysis(Basic_Data_Analysis):
    # This Strategy provides summary statistics for both numerical and non numerical data
    def basic_analysis(self, df: pd.DataFrame):
        '''
            Prints summary statistics for numerical and categorical data
            Parameters:
                df(pd.Dataframe): the dataframe on which the inspection strategeis are implemented

            Returns:
                None: this prints summary statistics to the console
        
        '''
        print('\n Summary Statistics (Numerical Features):')
        print(df.describe())
        print('\n Summary Statistics (Categorical Features):')
        print(df.describe(include='object'))

#************************************************************************************
# *********** Context Class that uses a Basic_Data_Analysis *************************
#************************************************************************************-

class Data_Analyzer:
    #This class allows you to switch between different data inspection 
    def __init__(self, strategy: Basic_Data_Analysis):
        '''
        Initializes the Data_analyzer with specific data analysis method

        Parameters:
            strategy (Basic_Data_Analysis): the strategy to be used

        Returns:
            None
        '''

        self._strategy = strategy
    
    def set_strategy(self, strategy: Basic_Data_Analysis):
        '''Sets new Strategy for the Data_Analayzer
        
        Parameters:
        strategy (Basic_Data_Analysis): The new strategy to be implemented

        Returns:
        None
        '''
        self._strategy= strategy

    def execute_analysis(self, df: pd.DataFrame):
        '''
        Executes the inspection using the current strategy.

        Parameters:
        df (pd.DataFrame): the dataframe to be inspected

        returns:
        None: Executes the strategy's inspection method 
        '''
        self._strategy.basic_analysis(df)

# Example Usage
if __name__ == "__main__":
    # Example usage if the Data_Analyzer with Differnt strategies
    #load Data
    # df = pd.read_csv('/Users/De/Documents/HexSoftwares/house_price_prediction/extracted_data/data.csv')
    df_path ='/Users/De/Documents/HexSoftwares/house_price_prediction/extracted_data/data.csv'
    if df_path.endswith(".csv"):
        df = pd.read_csv(df_path)
    elif df_path.endswith(".json"):
        df = pd.read_json(df_path)
    elif df_path.endswith(".xlsx"):
        df = pd.read_excel(df_path)
    else :
        raise ValueError (" Failed to load DataFrame. Format not Supported")
    

    # Initilize  Data Analyzer with Specific strategy
    analyzer = Data_Analyzer(DataTypes_Analysis())
    analyzer.execute_analysis(df)

    # Change strategy to summary Statistics and execute
    analyzer.set_strategy(Summary_Statistics_Analysis())
    analyzer.execute_analysis(df)


    #pass