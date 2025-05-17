# analysis of each feature

from pydantic import BaseModel

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class MultivariateAnalysis(BaseModel):
    def analyze(self, df:pd.DataFrame):
        
        '''
        Performs a comprehensive multivariate analysis by generating a heatma and pair plots

        Parameters:
        df (pd.DataFrame) The DataFrame containing the data 

        Returns 
        None: This mesage orchestrates the multivariate analysis


        '''
        self.generate_correlation_heatmap(df)
        self.generate_pairplot(df)

    # Abstract method
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        '''
        Generate and display a heatmap of he correlations
        Parameters:
        df (pd.DataFrame): The dataframe containing the data

        Returns:
        None: This methods generate and display a correlation map

        '''
        pass

    # Abstract method
    def generate_pairplot(self, df: pd.DataFrame):
        '''
        Generate and display a pair plot of the selected features
        Parameters:
        df (pd.DataFrame): The dataframe containing the data

        Returns:
        None: This methods generate and displayd a correlation map

        '''
        pass

# this strategy analyzes numerical features by plotting their distribution
class SimpleMultivariateAnalysis (MultivariateAnalysis):
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        '''Doc string'''
        plt.figure(figsize=(12, 10))
        sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='coolwarm', linewidths=1.5)
        plt.title(f'Correlation Heatmap')
        plt.show()

    def generate_pairplot(self, df: pd.DataFrame):
        '''Doc string'''
        sns.pairplot(df)
        plt.suptitle(f'Pair Plot of Selected Features', y= 1.02)
        plt.show()


if __name__ == "__main__":

    # Example usage of the MultivariateAnalyzer with different

    # load data
    '''
    df = pd.read_csv('../extracted_data/data.csv')

    analyze relationship  between 2 numerical features
    analyzer = SimpleMultivariateAnalyzer(MultivariateAnalyzer())
    analyzer.generate_pairplot(df, 'Gr Liv Area', 'SalePrice')

    analyze relationship  between categorical and numerical features
    analyzer = MultivariateAnalyzer(MultivariateAnalyzder())
    analyzer.generate_correlation_heatmap(df, 'Location', 'SalePrice')
    
    '''
        