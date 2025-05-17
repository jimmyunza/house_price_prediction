# analysis of each feature

from pydantic import BaseModel

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class BivariateAnalysis(BaseModel):
    def analyze(self, df:pd.DataFrame, feature:str):
        pass

# this strategy analyzes numerical features by plotting their distribution
class NumericalVsNumerical (BivariateAnalysis):
    def analyze(self, df: pd.DataFrame, feature1:str, feature2:str):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x = df[feature1], y = df[feature2])
        plt.title(f'Distribution of {feature1}  VS {feature2}')
        plt.xlable(feature1)
        plt.ylabel(feature2)
        plt.show()


# this strategy analyzes numerical features by plotting their distribution
class CategoricalVsNumerical (BivariateAnalysis):
    def analyze(self, df: pd.DataFrame, feature1:str, feature2:str):
        plt.figure(figsize=(10, 6))
        sns.boxplot(x =df[feature1], y= df[feature2])
        plt.title(f'Distribution of {feature1} vs {feature2}')
        plt.xlable(feature1)
        plt.ylabel(feature2)
        plt.show()

# context class that uses a BivariateAnalysisStrategy
#  this class allows you you to switch differnt bivariate strategies

class BivariateAnalyzer:
    def __init__(self, strategy: BivariateAnalysis):
        '''
        Initilizes the BivariateAnalyzer with a specific analysis

        Parameters:
         strategy(BivariateAnalysesStrategy) The strategy to be analyzed

        Returns:
        None
        '''
        self._strategy = strategy
    
    def set_strategy( self, strategy: BivariateAnalysis):
        '''
        Sets a nes strategy for the BivariateAnalyzer

        Parameters:
        strategy(BivariateAnalysisstrategy) the new strategy to be analyzed

        '''
        self._strategy= strategy

    def execute_analysis( self, df: pd.DataFrame,  feature1:str, feature2:str):
        '''
            Executes the bivariate analysis using the current strategy

            Parameters:
            df (pd.DataFrame) The dataframe containing the data to be analyzed
            feature1 (str): the name of the first feature/ column to be analyzed
            feature2 (str): the name of the second feature/ column to be analyzed
            
            Returns:
            None Executes the strategies analysis method and visuals

        '''
        self._strategy.analyze(df, feature1, feature2)


#Example Usage

if __name__ == "__main__":

    # Example usage of the BivariateAnalyzer with different

    # load data
    '''
    df = pd.read_csv('../extracted_data/data.csv')

    analyze relationship  between 2 numerical features
    analyzer = BivariateAnalyzer(NumericalVsNumericalAnalyzder())
    analyzer.execute_analysys(df, 'Gr Liv Area', 'SalePrice')

    analyze relationship  between categorical and numerical features
    analyzer = BivariateAnalyzer(CategoricalVsNumericalAnalyzder())
    analyzer.execute_analysys(df, 'Location', 'SalePrice')
    
    '''
        