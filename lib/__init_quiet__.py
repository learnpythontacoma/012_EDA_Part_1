'''
This initializing function will load the standard libraries for Python data
munging, give a request to load the inline matplotlib library (must be done separately),
then set functions that will run a standard, but basic, EDAs on a 
DataFrame that is loaded previously.

Developed by Ben P. Meredith, Ed.D.
'''

'''
First, let's wake up Python and have her great us.
'''

from datetime import datetime

import random

import warnings
warnings.filterwarnings('ignore')

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns
sns.set(style='darkgrid')

# import ggplot as gg

import matplotlib.style
import matplotlib as mpl
plt.style.use('fivethirtyeight')

from tqdm import tqdm

np.random.seed(42)

from IPython.display import display

from bs4 import BeautifulSoup

import csv

import random

pd.options.display.max_rows = 10000
pd.options.display.max_columns = 1000

print('\n', '\n', '🙏 🙏 PLEASE INITIATE %matplotlib inline OR %matplotlib notebook before we go further. Thank you!')


def histogram(df):
    fig = plt.figure(figsize = (15,15))
    ax = fig.gca()
    df[df.keys()].hist(ax=ax)
    fig.tight_layout()
    fig.show()

def two_dimension_histogram(x, y):
    plt.hist2d(x, y, bins=30, cmap='Blues')
    color_bar = plt.colorbar()
    color_bar.set_label('counts in bin')
    #plt.show()

def pairplot(df, feature):
    g = sns.PairGrid(df, hue=feature)
    g.map(plt.scatter)
    g.add_legend();
    plt.show()
    
def heatmap(df):
    plt.figure(figsize = (20,20))
    sns.heatmap(df.corr(), cmap='plasma', annot=True)
    plt.title("Confusion Matrix: Coefficients", fontsize = 28)
    plt.show()
    
def kdeplot(df):
    sns.kdeplot(df, data2=None, shade=False, vertical=False, kernel='gau', bw='scott', gridsize=100, cut=3, clip=None, legend=True, cumulative=False, shade_lowest=True, cbar=False, cbar_ax=None, cbar_kws=None, ax=None)
    plt.show()
    
    
'''
Next is the eda functions load. 
'''
    
def eda(df):
    missing_values_count = df.isnull().sum()
    total_cells = np.product(df.shape)
    total_missing = missing_values_count.sum()
    print('\n', 'df total missing values percentage: ', '\n', (total_missing/total_cells) * 100)
    print('_______________________________________________')
    display("df Head: ", df.head())
    print('_______________________________________________')
    obs, features = df.shape
    print("observations (rows): ", obs, '\n',"features (columns): ", features)

    print('_______________________________________________')
    print('\n', 'df keys: ', '\n', df.keys())
    print('_______________________________________________')
    display( 'df describe: ', df.describe())
    print('_______________________________________________')
    print('\n', 'df info: ', '\n', df.info())
    print('_______________________________________________')
    print('\n', 'df types: ', '\n', df.dtypes)
    print('_______________________________________________')
    print('\n', 'df count: ', '\n', df.count())
    print('_______________________________________________')
    print('\n', 'df.isnull() count: ', '\n', df.isnull().sum())
    print('_______________________________________________')
    
    
    num_columns = []
    cat_columns = []
    
    for key in df.keys():
        if df[key].dtypes == 'int64':
            num_columns.append(key)
        elif df[key].dtypes == 'float64':
            num_columns.append(key)
        else:
            cat_columns.append(key)
        
    
    n = num_columns
    c = cat_columns

    if len(n) >= 2: #If there are more than two numeric features, Python will plot a heatmap and suggest a pairplot of the DataFrame
        print ("There are", len(num_columns), " numeric columns in this data set.", '\n',)
        print("The numeric columns are: ", '\n', num_columns, '\n',)
        print('_______________________________________________', '\n')      
        print('________________________________________________', 
              '\n','\n', 
              "Consider using the pairplot(df, feature) for ",
              "this analysis.", '\n','\n', '__________________________________________________')
        
    else: #If there is only one numeric column, Python will not plot it.
        print("There are not enough numerical columns for correlational analyses. Please attempt other VDA techniques.")

    if len(c) >= 2: # If there are two or more categoric features, Python will plot each feature's histogram
        print ("There are", len(cat_columns), " categoric columns in this data set.", '\n')
        print("The categorical columns are: ", '\n', cat_columns, '\n',)
        print('_______________________________________________', '\n')
        
    else:
        print("There are not enough categorical columns for analysis in this initial eda.")
        print('_______________________________________________', '\n')    
    
    print('\n', '\n', 'May I suggest that you run a VDA - vda(df) - next?')
  
    
def vda(df):
    num_columns = []
    cat_columns = []
    
    for key in df.keys():
        if df[key].dtypes == 'int64':
            num_columns.append(key)
        elif df[key].dtypes == 'float64':
            num_columns.append(key)
        else:
            cat_columns.append(key)
        
    
    n = num_columns
    c = cat_columns

    if len(num_columns) >= 2: #If there are more than two numeric features, Python will plot a heatmap and suggest a pairplot of the DataFrame
        print ("There are", len(num_columns), " numeric columns in this data set.", '\n',)
        print("The numeric columns are: ", '\n', num_columns, '\n',)
        print('_______________________________________________', '\n')
        
        # Plot a Confusion Matrix of the DataFrame
        heatmap(df)
        
        print('________________________________________________', '\n','\n', "Consider using the pairplot(df, feature) for this analysis.", '\n','\n', "__________________________________________________")
        
    else: #If there is only one numeric column, Python will not plot it.
        print("There are not enough numerical columns for correlational analyses. Please attempt other VDA techniques.")

    if len(cat_columns) >= 2: # If there are two or more categoric features, Python will plot each feature's histogram
        print ("There are", len(cat_columns), " categoric columns in this data set.", '\n')
        print("The categorical columns are: ", '\n', cat_columns, '\n',)
        print('_______________________________________________', '\n')
        
        print('Categorical Features Plotted:')
        for col in cat_columns:
            plt.hist(df[col])
            plt.title(col)
            plt.legend()
            plt.show()

    else:
        print("There are not enough categorical columns for analysis in this initial eda.")
        print('_______________________________________________', '\n')    
    
    
    print("The next bar charts plot features with less than 10 unique numbers against all other features.",  '\n','\n', "Additionally, I am providing you with the coefficients for each pair (in the event that the visual does not show how strong of a relationship exists between the two features.", '\n','\n', "If I see a mild or strong relationship between two features, I will alert you." '\n','\n',) 
    ca = 'null'
    q = 'null'

    for key in df.keys():
        if (df[key].nunique() <= 10) and (df[key].dtype != 'object'):
            for rkey in df.keys():
                if rkey != key:
                    q = key
                    ca = rkey

                    plt.bar(df[q], df[ca], data=df)
                    plt.xlabel(q)
                    plt.ylabel(ca)
                    plt.show()

                    coef = df[ca].corr(df[q])
                    print("The coefficient between ", q, '&', ca,' is:', coef,  '\n',)
                    if coef <= -0.5:
                        print("There is a strong negative coorelation between these two features. Pay Attention!", '\n','\n',)
                    elif coef >= 0.5:
                        print("There is a strong positive correlation between these two features. Pay Attention!", '\n','\n',)
                    elif (coef >= -0.49) and (coef <= -0.4):
                        print("There is a mild negative correlation between these two features. We need to look at this a bit more.", '\n','\n',)
                    elif (coef <= 0.49) and (coef >= 0.4):
                        print("There is a mild positive correlation between these two features. We need to look at this a bit more.", '\n','\n',)

                else:
                    pass    


def do_we_need_to_clean(df):
    print('_______________________________________________')   
    obs, features = df.shape
    print("observations (rows): ", obs, '\n',"features (columns): ", features)
    print('_______________________________________________')
    
    full_drop_list = []
    recommended_drop_list = []
    
    tenpercent = obs*.101

    for key in df.keys():
        size = df[key].count()
        nulls = df[key].isnull().sum()
        
        if nulls > 0:
            full_drop_list.append(key)
            if nulls > tenpercent:
                recommended_drop_list.append(key)
            
    print('\n', '\t', "The complete drop list is, where there are values missing or there are null values: ",
          '\n', '\n', '\t', full_drop_list)
    print('\n', '\n', '\n', '\t', "The recommended drop list is: ", 
          '\n', '\n', '\t',recommended_drop_list, 
          '\n', '\n', '\t',' as these values have more than a statistical 10.1% missing values.')
    
    answer = input('Would you like me to delete the recommended values? [y or n]')
    if answer == 'y':
        for key in recommended_drop_list:
            del df[key]
        print('\n', '\n', '\t','I have deleted the the following values:', recommended_drop_list)
    else: 
        print('\n', '\n', '\t','I have not delted any values. If you want to do this later, use the \'drop_recommended_list(df)\' function.')
    return recommended_drop_list

def drop_recommended_list(df):
    recommended_drop_list = do_we_need_to_clean(df)
    for key in recommended_drop_list:
        del df[key]

def correlations(compare_feature, df):
    num_columns = []
    cat_columns = []

    for key in df.keys():
        if df[key].dtypes == 'int64':
            num_columns.append(key)
        elif df[key].dtypes == 'float64':
            num_columns.append(key)
        else:
            cat_columns.append(key)
            
    ndf = df[num_columns]
    cdf = df[cat_columns]
        
    strong_correlation = []
    mild_correlation = []
    neg_correlation = []
    
    #compare_feature = 'SalePrice'
    tempdf = pd.DataFrame(columns=['compare feature','feature', 'correlation'])

    counter = 0
    for key in tqdm(num_columns):
        if (ndf[key].corr(df[compare_feature]) >= 0.51) and (key != compare_feature):
            print(compare_feature, ' & ', key, ' are STRONGLY correlated with a ', ndf[key].corr(df[compare_feature]))
            strong_correlation.append(key)
        elif (ndf[key].corr(df[compare_feature]) <= 0.49) and (ndf[key].corr(df[compare_feature]) >= 0.40) and (key != compare_feature):
            print(compare_feature, ' & ', key, ' are MILDLY correlated with a ', ndf[key].corr(df[compare_feature]))
            mild_correlation.append(key)
        elif (ndf[key].corr(df[compare_feature]) <= 0.0) and (key != compare_feature):
            print(compare_feature, ' & ', key, ' are NEGATIVELY correlated with a ', ndf[key].corr(df[compare_feature]))
            neg_correlation.append(key)
            
        tempdf.loc[counter, 'compare feature'] = compare_feature
        tempdf.loc[counter, 'feature'] = key
        tempdf.loc[counter, 'correlation'] = (ndf[key].corr(df[compare_feature]))
        counter += 1

    print('\n', '\n',tempdf.sort_values(by='correlation', ascending=False).head(25))
    print('\n', '\n', 'STRONGLY correlated with', compare_feature, ': ', strong_correlation)
    print('\n', '\n', 'MILDLY correlated with', compare_feature, ': ', mild_correlation)
    print('\n', '\n', 'NEGATIVELY correlated with', compare_feature, ': ', neg_correlation)

    return strong_correlation, mild_correlation, neg_correlation


def break_down_features(df):
    num_columns = []
    cat_columns = []

    for key in df.keys():
        if df[key].dtypes == 'int64':
            num_columns.append(key)
        elif df[key].dtypes == 'float64':
            num_columns.append(key)
        else:
            cat_columns.append(key)
            
    print('There are ', len(num_columns),' numeric columns and ', len(cat_columns), 'categorical columns in this dataset.')
            
    return num_columns, cat_columns

def predictive_strength(df):
    import pandas as pd
    condf = pd.DataFrame(columns = ['feature', 'nulls', 'skewness', 'con_score' ]) 
    counter = 1
    num_columns = []
    cat_columns = []
    
    for key in df.keys():
        if df[key].dtypes == 'int64':
            num_columns.append(key)
        elif df[key].dtypes == 'float64':
            num_columns.append(key)
        else:
            cat_columns.append(key)

    for key in df[num_columns]:
        t = df[key].isnull().sum().sum()
        u = t/len(df[key])
        v = df[key].skew()
        if v < 0:
            condf.loc[counter, 'skewness'] = (v)
            v = v*-1 
        else:
            condf.loc[counter, 'skewness'] = (v)
        c = 100-(t/100) - v
    #     print(key, " : ", t, '/', len(df[key]), '=', u)
        condf.loc[counter, 'feature'] = (key)
        condf.loc[counter, 'nulls'] = (t)
    #     condf.loc[counter, 'skewness'] = (v)
        condf.loc[counter, 'con_score'] = ("%.2f" % round(c,2))
        counter += 1

    print('Feature Predictive Confidence Score:', '\n', 
          "This score for each feature is a measure of that feature's missing values and skewness.", '\n',
          '\n', condf.sort_values(by=['con_score'], ascending=False).head(25))
    

def pandas_profiling(df):
    size = len(df)
    if size >= 10000 and size <=19999:
        print('Your dataset is', size,'entries long. This will take a few minutes to process.','\n',)
        answer = input('Do you wish to continue? [y or n]')
        #input(answer)
        if answer == 'y':    
            import pandas_profiling
            display(pandas_profiling.ProfileReport(df))
        else:
            print('I will not run this function right now.')
    elif size < 10000:
        print('Your dataset is ',size,'entries long. This will run fairly quickly.','\n',)
        answer = input('Do you wish to continue? [y or n]')
        #input(answer)
        if answer == 'y':    
            import pandas_profiling
            display(pandas_profiling.ProfileReport(df))
        else:
            print('I will not run this function at this time.')
    else:
        print('Your dataset is', size,'entries long, which is pretty big.')
        answer = input('Do you wish to continue? [y or n]')
        #input(answer)
        if answer == 'y':
            print('Go get a coffee and visit someone while I process this.','\n')
            import pandas_profiling
            display(pandas_profiling.ProfileReport(df))
        else:
            print('Phew! I am glad I am not running this function right now.')
    

'''
The feature review will look at the specifics of each feature, then ask if you want to 
1. change its dtype,
2. fill in missing values with some value given, or 
3. delete the feature from the dataframe.

'''

def feature_review(df):
    print('_______________________________________________') 
    obs, features = df.shape
    print("observations (rows): ", obs, '\n',"features (columns): ", features)
    print('_______________________________________________')
    
    condf = pd.DataFrame(columns = ['feature', 'nulls', 'skewness', 'con_score' ])
    counter = 1
    num_columns = []
    cat_columns = []
    
    for key in df.keys():
        if df[key].dtypes == 'int64':
            num_columns.append(key)
        elif df[key].dtypes == 'float64':
            num_columns.append(key)
        else:
            cat_columns.append(key)

    for k in df.keys():
        
        # Introduce the feature
        print('____________________________________________________', '\n',
              '\n', k,'=',df[k].dtypes, '\n')
        
        if k in num_columns:
            # Skew, nulls, con_score
            t = df[k].isnull().sum().sum()
            print('nulls:', t)
            u = t/len(df[k])
            print('nulls percentage:', u)
            v = df[k].skew()
            print('skew:', v, '\n', '\n')

            if v < 0:
                condf.loc[counter, 'skewness'] = (v)
                v = v*-1 
            else:
                condf.loc[counter, 'skewness'] = (v)
            c = 100-(t/100) - v
        #     print(key, " : ", t, '/', len(df[k]), '=', u)
            condf.loc[counter, 'feature'] = (k)
            condf.loc[counter, 'nulls'] = (t)
        #     condf.loc[counter, 'skewness'] = (v)
            condf.loc[counter, 'con_score'] = ("%.2f" % round(c,2))
            print('Feature Predictive Confidence Score:', '\n', 
                "This score for the feature is a measure of that feature's missing values and skewness.", '\n',
                '\n', condf.sort_values(by=['con_score'], ascending=False).head(25))
        else:
            pass
              
        print('\n')
        
        # Change the data type
        a = input('Would you like to change its data type? [y or n]')
        print('\n')
        if a == 'y':
            b = input('What type would you like it to be? [int, float64, object]')
            print('\n')
            if b == 'int':
                df[k] = df[k].astype(int)
            elif b == 'float64': 
                df[k] = df[k].astype(float64)
            elif b == 'object':
                df[k] = df[k].astype(object)
            else:
                print('incorrect spelling')
                pass
                
        else:
            pass
    
        # Delete the Feature
        c = input('Would you like me to delete this feature? [y or n]')
        if c == 'y':
            del df[k]
        else:
            pass
        print(k)     