# analysis of each feature

from pydantic import BaseModel

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class UnivariateAnalysis(BaseModel):
    def analyze(self, df:pd.DataFrame, feature:str):
        pass

# this strategy analyzes numerical features by plotting their distribution
class NumericalUnivariate (UnivariateAnalysis):
    def analyze(self, df: pd.DataFrame, feature:str):
        plt.figure(figsize=(10, 6))
        sns.histplot(df[feature], kde=True, bins=30)
        plt.title(f'Distribution of {feature}')
        plt.xlable(feature)
        plt.ylabel("Frequency")
        plt.show()


# this strategy analyzes numerical features by plotting their distribution
class CategoricalUnivariate (UnivariateAnalysis):
    def analyze(self, df: pd.DataFrame, feature:str):
        plt.figure(figsize=(10, 6))
        sns.countplot(df[feature], data=df, palette="muted")
        plt.title(f'Distribution of {feature}')
        plt.xlable(feature)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.show()

# context class that uses a UnivariateAnalysisStrategy
#  this class allows you you to switch differnt bivariate strategies

class UnivariateAnalyzer:
    def __init__(self, strategy: UnivariateAnalysis):
        '''
        Initilizes the UnivariateAnalyzer with a specific analysis

        Parameters:
         strategy(UnivariateAnalysisStrategy) The strategy to be analyzed

        Returns:
        None
        '''
        self._strategy = strategy
    
    def set_strategy( self, strategy: UnivariateAnalysis):
        '''
        Sets a new strategy for the UnivariateAnalyzer

        Parameters:
        strategy(UnivariateAnalysistrategy) the new strategy to be analyzed

        '''
        self._strategy= strategy

    def execute_analysis( self, df: pd.DataFrame,  feature:str,):
        '''
            Executes the bivariate analysis using the current strategy

            Parameters:
            df (pd.DataFrame) The dataframe containing the data to be analyzed
            feature1 (str): the name of the first feature/ column to be analyzed
            feature2 (str): the name of the second feature/ column to be analyzed
            
            Returns:
            None Executes the strategies analysis method and visuals

        '''
        self._strategy.analyze(df, feature)


#Example Usage

if __name__ == "__main__":

    # Example usage of the BivariateAnalyzer with different

    # load data
    '''
    df = pd.read_csv('../extracted_data/data.csv')

    analyze relationship  between 2 numerical features
    analyzer = UnivariateAnalyzer(NumericalAnalyzder())
    analyzer.execute_analysis(df, 'SalePrice')

    analyze relationship  between categorical and numerical features
    analyzer = UnivariateAnalyzer(CategoricalAnalyzder())
    analyzer.execute_analysis(df,  'SalePrice')
    
    '''