# import Libraries

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#**************************************************************************
#***************** Abstract Class for 2 feature ananlysis *****************
#**************************************************************************

class FeaturesAnalysis():
    def analyze(self, df:pd.DataFrame, feature1:str, feature2:str):
        """
        Performs specific anaysis by comparing two (2) features

        Paramaters:
        df(pd.DataFrame) ,df[feature1], df[feature2]: it takes 3 arguments which are the Dataframe and 2 features of the DataFrame to be analyzed

        Returns:
        None
        """
        pass

#*****************************************************************************
#*********** Numerical Feature Vs Numerical Feature **************************
#*****************************************************************************

class NumericalVsNumerical (FeaturesAnalysis):
    # this strategy analyzes numerical features by plotting their distribution
    def analyze(self, df: pd.DataFrame, feature1:str, feature2:str):
        """ Plots scatter plots of any numerical features passed as arguments to be analyzed
        Parameters:
        df(pd.DataFrame), feature1(str), feature2(str): takes DataFrame and two features for anaylsis
        Return:
        None: Plots scatter plot for the 2 features
        """
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x = df[feature1], y = df[feature2])
        plt.title(f'Distribution of {feature1}  VS {feature2}')
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()

#*****************************************************************************
#*********** Categorical Feature Vs Numerical Feature ************************
#*****************************************************************************

class CategoricalVsNumerical (FeaturesAnalysis):
    # this strategy analyzes numerical features by plotting their distribution
    def analyze(self, df: pd.DataFrame, feature1:str, feature2:str):
        """ Plots scatter plots of any numerical features passed as arguments to be analyzed
        Parameters:
        df(pd.DataFrame), feature1(str), feature2(str): takes DataFrame and two features for anaylsis
        Return:
        None: Plots scatter plot for the 2 features
        """
        plt.figure(figsize=(10, 6))
        sns.boxplot(x =df[feature1], y= df[feature2])
        plt.title(f'Distribution of {feature1} vs {feature2}')
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()

#*****************************************************************************
#**********-******* Features Analyzer Implementation  ************************
#*****************************************************************************

class FeaturesAnalyzer:
    #  this class allows you you to switch differnt Analysis strategies
    def __init__(self, strategy: FeaturesAnalysis):
        '''
        Initilizes the Features Analyzer with a specific analysis method

        Parameters:
         strategy(FeaturesAnalsis) The strategy to be analyzed

        Returns:
        None
        '''
        self._strategy = strategy
    
    def set_strategy( self, strategy: FeaturesAnalysis):
        '''
        Sets a new strategy for the FeaturesAnalyzer

        Parameters:
        strategy(FeaturesAnalsis) the new strategy to be analyzed

        '''
        self._strategy= strategy

    def execute_analysis( self, df: pd.DataFrame,  feature1:str, feature2:str):
        '''
            Executes the Feature analysis using the current strategy

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

    # Example usage of the FeaturesAnalyzer with different

    # load data
    
    # df = pd.read_csv('./extracted_data/data.csv')

    # #analyze relationship  between 2 numerical features
    # analyzer = FeaturesAnalyzer(NumericalVsNumerical())
    # analyzer.execute_analysis(df, 'bedrooms', 'price')

    # #analyze relationship  between categorical and numerical features
    # analyzer = FeaturesAnalyzer(CategoricalVsNumerical())
    # analyzer.execute_analysis(df, 'country', 'price')
    pass
    
        