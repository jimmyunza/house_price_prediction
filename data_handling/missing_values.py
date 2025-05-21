
# importing Libraries

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ******************************************************************************
# *****************  Abstract Class for MIssing Values Handling ***************

class Missing_Values_Analysis_template():
    # This class defines a common interface for  missing data inspection
    # sub classes implement the methods to identify and visualize
    def analyze(self, df: pd.DataFrame):
        """ This method implements missing value analysis
        Parameters:
        df(pd.DataFrame): takes a DataFrame as an argument
        Return:
        None: identify and plots the distribution of missing values
        """

        self.identify_missing_values(df)
        self.visualize_missing_values(df)


    def identify_missing_values(self, df: pd.DataFrame):
        """ This method implements missing value analysis
        Parameters:
        df(pd.DataFrame): takes a DataFrame as an argument
        Return:
        None:
        """
        pass


    def visualize_missing_values(self, df: pd.DataFrame):
        """ This method implements missing value analysis
        Parameters:
        df(pd.DataFrame): takes a DataFrame as an argument
        Return:
        None: plots the distribution of missing values
        """
        pass

# *********************************************************************
#************** Handling Missing Values Implemantation class **********
#**********************************************************************

class Missing_Value_Analysis(Missing_Values_Analysis_template):
    def identify_missing_values(self, df: pd.DataFrame):
        '''
        Prints missing values number if found in a DataFrame.

        Parameters:
            df (pd.DataFrame): Input DataFrame to analyze for missing values.

        Returns:
            None: .
        '''

        print('\n Missing Values Count by Column')
        missing_values = df.isnull().sum()
        print(missing_values[missing_values > 0])
    
    def visualize_missing_values(self, df: pd.DataFrame):
        '''
        Visuals for missing values in a DataFrame using a heatmap.

        Parameters:
            df (pd.DataFrame): Input DataFrame to analyze for missing values.

        Returns:
            None: Displays a heatmap where missing values are highlighted.
        '''

        if df.empty:
            raise ValueError("Input DataFrame is empty.")
        
        print('\n Visualizing Missing values...')
        plt.figure(figsize=(12,8))
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
        plt.title('Missing Values Heatmap')
        plt.show()

# Example usage
if __name__ == '__main__':
    
    # load data
    df = pd.read_csv('./extracted_data/data.csv')

    # perfomrm missing value analysis
    missing_value_analyzer = Missing_Value_Analysis()
    missing_value_analyzer.analyze(df)

    

        
