# import libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#**************************************************************************
#***************** Abstract Class for Muilti feature ananlysis *****************
#**************************************************************************

class MultiFeatureAnalysis():
    def analyze(self, df:pd.DataFrame):
        
        '''
        Performs a comprehensive multi_feature analysis by generating a heatmap and pair plots

        Parameters:
        df (pd.DataFrame) The DataFrame containing the data 

        Returns 
        None: This message dispays the multivariate analysis
        '''
        self.generate_correlation_heatmap(df)
        self.generate_pairplot(df)

    # Abstract method for heat map
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        '''
        Generate and display a heatmap of he correlations
        Parameters:
        df (pd.DataFrame): The dataframe containing the data

        Returns:
        None: This methods generate and display a correlation map

        '''
        pass

    # Abstract method pair plots
    def generate_pairplot(self, df: pd.DataFrame):
        '''
        Generate and display a pair plot of the selected features
        Parameters:
        df (pd.DataFrame): The dataframe containing the data

        Returns:
        None: This methods generate and displayd a correlation map

        '''
        pass

#**************************************************************************
#***************** Implementation of multi feature ananlysis *****************
#**************************************************************************

# this strategy analyzes numerical features by plotting their distribution
class MultiFeatureAnalyzer (MultiFeatureAnalysis):
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        '''Plots a heatmap for all the features in the DataFrame
        Parameters:
        df(pd.DataFrame): takes DataFrame and two features for anaylsis
        Return:
        None: Plots a heatmap for all the DataFrame features'''
        plt.figure(figsize=(12, 10))
        sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='coolwarm', linewidths=1.5)
        plt.title(f'Correlation Heatmap')
        plt.show()

    def generate_pairplot(self, df: pd.DataFrame):
        '''Plots a heatmap for all the features in the DataFrame
        Parameters:
        df(pd.DataFrame): takes DataFrame and two features for anaylsis
        Return:
        None: Plots a heatmap for all the DataFrame features'''
        sns.pairplot(df)
        plt.suptitle(f'Pair Plot of Selected Features', y= 1.02)
        plt.show()


if __name__ == "__main__":

    # Example usage of the Multi Feature Analysis with different

    # load data
    
    df = pd.read_csv('./extracted_data/data.csv')

    # pair plots analysis
    analyzer = MultiFeatureAnalyzer()
    analyzer.generate_pairplot(df)

    # heatmap anaysis
    analyzer = MultiFeatureAnalyzer()
    analyzer.generate_correlation_heatmap(df)
    
    
        