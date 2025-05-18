# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#****************************************************************
#***************** Features Analyses*****************************
#****************************************************************
class FeatureAnalysis():
    # This class defines common interface for Feature Analysis 
    def analyze(self, df:pd.DataFrame, feature:str):
        """ 
        Perform  specific feature analysis

        Parameters:
            df:(pd.Dataframe), feature(str): the method takes 2 arguments which are DataFrame and feature to be analyzed

        Returns:
            None: this prints plots of the results directly

        """
        pass

#*************************************************************************
#***************** Numerical features distribution Plots *****************
#*************************************************************************

class NumericalFeature(FeatureAnalysis):
    # this method analyzes numerical features by plotting their distribution
    def analyze(self, df: pd.DataFrame, feature:str):
        """ 
        Perform  specific feature analysis

        Parameters:
            df:(pd.Dataframe), feature(str): the method takes 2 arguments which are DataFrame and numerical feature name to be analyzed

        Returns:
            None: this prints plots of the results directly

        """
        plt.figure(figsize=(10, 6))
        sns.histplot(df[feature], kde=True, bins=30)
        plt.title(f'Distribution of {feature}')
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        plt.show()

#*************************************************************************
#**************** Categorical features distribution Plots ****************
# ************************************************************************

class CategoricalFeature(FeatureAnalysis):
    # this strategy analyzes numerical features by plotting their distribution
    def analyze(self, df: pd.DataFrame, feature:str):
        """ 
        Perform  specific feature analysis

        Parameters:
            df:(pd.Dataframe), feature(str): the method takes 2 arguments which are DataFrame and Categorical feature name to be analyzed

        Returns:
            None: this prints plots of the results directly

        """
        plt.figure(figsize=(10, 6))
        sns.countplot(x=df[feature], data=df, hue= feature, legend=False, palette="muted")
        plt.title(f'Distribution of {feature}')
        plt.xlabel(feature)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.show()

#******************************************************************************
#*************context class that uses a Feature Analysis **********************
#******************************************************************************

class FeatureAnalyzer:
    #  this class allows you you to switch differnt feature analysis methods
    def __init__(self, strategy: FeatureAnalysis):
        '''
        Initilizes the FeatureAnalyzer with a specific analysis Categorical feature or Numerical feature

        Parameters:
         strategy(FeatureAnalysis) The strategy to be analyzed

        Returns:
        None
        '''
        self._strategy = strategy
    
    def set_strategy( self, strategy: FeatureAnalysis):
        '''
        Sets a new strategy for the Feature Analyzer

        Parameters:
        strategy(FeatureAnalyis) the new strategy to be analyzed

        '''
        self._strategy= strategy

    def execute_analysis( self, df: pd.DataFrame,  feature:str,):
        '''
            Executes the  feature analysis using the current strategy

            Parameters:
                df (pd.DataFrame) The dataframe containing the data to be analyzed
                feature (str): the name of the first feature/ column to be analyzed
        
            Returns:
                None Executes the strategies analysis method and visuals

        '''
        self._strategy.analyze(df, feature)


#Example Usage

if __name__ == "__main__":

    # Example usage of the BivariateAnalyzer with different

    # load data

    # df = pd.read_csv('./extracted_data/data.csv')

    # # analyze numerical features
    # analyzer = FeatureAnalyzer(NumericalFeature())
    # analyzer.execute_analysis(df, 'price')

    # # analyze categorical features
    # analyzer = FeatureAnalyzer(CategoricalFeature())
    # analyzer.execute_analysis(df,  'country')

    pass
    
    