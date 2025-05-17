# missing values.py
#_______________________
# file for  EDA
from pydantic import BaseModel

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Abstract class for missing values analysis
# This class defines a common interface fo data inspection strategies
# sub classes implement the methods to identify and visualize

class Missing_Values_Analysis_template(BaseModel):
    def analyze(self, df: pd.DataFrame):
        """ Doc string"""

        self.identify_missing_values(df)
        self.visualize_missing_values(df)


    def identify_missing_values(self, df: pd.DataFrame):
        """ Doc string"""
        pass


    def visualize_missing_values(self, df: pd.DataFrame):
        '''Doc string'''
        pass

# concrete class for missing values identification
#____________________________________________

class Simple_missing_Value_Analysis(Missing_Values_Analysis_template):
    def identify_missing_values(self, df: pd.DataFrame):
        '''
        Visualizes missing values in a DataFrame using a heatmap.

        Args:
            df (pd.DataFrame): Input DataFrame to analyze for missing values.

        Returns:
            None: Displays a heatmap where missing values are highlighted.
        '''

        print('\n Missing Values Count by Column')
        missing_values = df.isnull().sum()
        print(missing_values[missing_values > 0])
    
    def visualize_missing_values(self, df: pd.DataFrame):
        '''doc string'''

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
    missing_value_analyzer = Simple_missing_Value_Analysis()
    missing_value_analyzer.analyze(df)
    

        
