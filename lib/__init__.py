'''
This initializing function will load the standard libraries for Python data
munging, return to the notebook confirmation that the libraries are loaded, 
give a request to load the inline matplotlib library (must be done separately),
then set a function (`eda`) that will run a standard, but basic, EDA on a 
DataFrame that is loaded previously.

Developed by Ben P. Meredith, Ed.D.
'''

'''
First, let's wake up Python and have her great us.
'''

from datetime import datetime
time = datetime.now().strftime('%H:%M:%S')
print ('The time is ', time, '\n')
if time <= '06:00:00':
    print("😴 GOOD MORNING! You are up and working awfully early!", '\n')
    tod = 'morning'
elif '06:00:00' < time < '11:59:59':
    print("😀 GOOD MORNING!", "\n")
    tod = 'morning'
elif '12:00:00' < time < '18:00:00':
    print('😎 GOOD AFTERNOON!', '\n')
    tod = 'afternoon'
else:
    print('🧐 GOOD EVENING!', '\n')
    tod = 'evening'
    
# print("Are we Data Munging this",tod, '?','\n', '\n')
# print('🤓 You know how I love Data Munging!', '\n','(I just love saying the words "Data MUNGING"! It is such a funny term!)')


'''
Now let's add some pithy and thought provoking sayings with which Python will greet me,
(and show off its intelligence and worldliness).
'''

import random
s = ['Always remember that the toes you step on today may be attached to the ass you have to kiss tomorrow.',
    'Today is a good day to be alive!', 
    'Coffee is the nector of life',
    'Frodo Lives!',
    'Life in a glass house is revealing.', 
    'Experience enables you to recognize a mistake every time you repeat it.',
    'To write with a broken pencil is pointless.',
    'Profanity is the effort of a feeble mind to express itself forcefully.',
    'America is one of the few places you can say what you want without thinking.',
    "Unless you have never been tempted, don't pass judgment on someone who has yielded.",
    "Don't mistake activity for achievement.",
    "It's a great pity the right of free speech isn't based on the obligation to say something sensible.",
    "You can't make anything idiot proof because idiots are so ingenious. ~ Ron Burns",
    'Many would be scantily clad if clothed in their humility. ~ Anonymous',
    "It's great to be great, but it's greater to be human.~ Will Rogers",
    'Some folks get lost in thought because it is unfamiliar territory',
    "If quitters never win, and winners never quit, then who is the fool who said, 'quit while you're ahead?'",
    'If silence is golden, not many people can be arrested for hoarding.',
    'I drink and I know things ~ Tyrion Lannister',
    'You can never make your dreams come true by oversleeping.',
    'Never have a battle of wits with an unarmed man',
    'Pride is the only poison that is good for you when swallowed.',
    'An egotist is a person who thinks that if they had not been born people would have asked why not.',
    'The only fool bigger than the person who knows it all is the person who argues with him.',
    'Never argue with a fool - people may not notice the difference',
    "I’m Mary Poppins Y’all! – Yondu",
    "I'm under no obligation to make sense to you - Python",
    "The best place to find a helping hand is at the end of your arm.",
    "The opinions expressed by the husband of this house do not always represent the views of the management.",
    "Life is a one-way street and you're not coming back.",
    "Tread often the path to thy friend's house lest weeds grow to obscure thy way.",
    "The well-oiled nut behind the steering wheel is the most unreliable part of the car.",
    "A bachelor is a man who has failed to embrace his opportunities.",
    "A friend is one who knows all about you and loves you just the same.",
    "Some people have difficulty in counting calories, and they have figures to prove it.",
    "We are all cast in the same mold, some being moldier than others.",
    "Friendship is the one bright light, that keeps on burning day and night.",
    "No road is long with good company.",
    "Not all men are fools, some are bachelors.",
    "A wife is a great consolation to a man in all the troubles a bachelor never has.",
    "The world is full of willing people, some willing to work, and the rest, willing to let them.",
    "One thorn of experience is worth a whole wilderness of warning.",
    "When the going gets tough, the tough get going.",
    "Money never buys friends, it only hires them.",
    "A bachelor is one who hesitates before all is lost.",
    "Don't despise the little things, often the mosquito is more bothersome than the elephant.",
    "Too many square meals make too many round people.",
    "Age is in the mind, not the calendar.",
    "Man is of clay, but it takes a woman to make a mug of him.",
    "Trusting someone is harder than loving them.",
    "We cannot discover new oceans without loosing sight of the shore.",
    "We cannot become what we want to be by remaining who we are.",
    "Do not fill the room with conversations you aren't having.",
    "The worst loneliness is the kind felt while inside a relationship - Alone Together.",
    "Some people fill the gaps of loneliness and others emphasize the gaps."
    "The highest form of ignorance is when you reject something you don't know anything about.",
    "It is prudent not to place confidence in that by whom we have once been deceived."
    "Never trade respect for attention.",
    "Music and passion are always in fashion at the Copacabana.",
    "Some people never change, and you have to accept that.",
    "Trying to define yourself is like tyrying to bite your own teeth.",
    "Wir begreifen und leben, nur was wir selbst sind oder sein koennen.",
    "A certain darkness is needed to see the stars.", 
    "Assume good intent. Act accordingly.",
    "Don't judge people for the choices they make when you don't know the options they had to choose from.",
    "Be the person your dog thinks you are.",
    "'Clutter' is not just physical stuff. It's old ideas, toxic relationships and bad habits.", '\n', 
"Clutter is anything that does not support your better self.",
    "'No one can make you fell inferior, unless you allow them' is easy to say and to understand. It is even easy to believe. The challenge is in living it.",
    "It takes just a moment to hurt someone, but it often takes years for that person to heal.",    
    "People have the annoying habit of remembering things they shouldn't.",
    "Fear is a reasonable response to life.",
    "When you counsel someone, you should appear to be reminding him of something he had forgotten, not of the light he was unable to see.",
    "The picture in your head of how life should be causes you the most problems.",
    "Get enough sleep.",
    "If someone cannot make the effort to be in your life, they don't deserve to be there.",
    "A good cup of tea can solve just about anything.",
    "Stop talking and listen.",
    "Your level of unhappiness is directly related to the distance between who you are in public and who you are in private.",
    "You don't owe anyone an explanation for your choices or preferences.",  
    "If I have to ask you for your attention, then you don't deserve mine.",
    "We all have one person who hurt us so much that it changed us forever.", 
    "Sometimes our bones feel the weight of all of the lives we are not living.", 
    "Produce a world where a chicken can cross the road without having its motives questioned.",
    "In 100 attempts at solving a problem, you learn 99 ways not to do something.",
    "Reality is just a perception.",
    "Stay close to anything that makes you feel alive.",
    "Life begins when you first realize how soon it will end.",
    "Everyone wants the truth, but no one wants to be honest.",
    "Everyone wants the truth until it is given.",     
    "Happiness exists when you don't know a thing.",
    "Trust is like an eraser, it gets smaller and smaller after every mistake.",
    "At some point in your life, you are going to have to start demanding what you deserve and be willing to walk away if what you need cannot be provided.",
    "Nowadays people know the price of everything and the value of nothing.",
    "Leadership is the ability to translate vision into reality.",
    "The strongest people are not those who show strength in front of us, but those who win battles we know nothing about.",
    "When you are already in pain, when you are already hurt, don't quit. Get a reward from your efforts.",
    "Never, Never, Never give up ~ Winston Churchill",
    "Success is not measured by winning, but by the number of times you were knocked down and got back up.",
    "It takes courage to grow up and be who you are suppose to be.",
    "A ship is always safe in harbor, but that is not what it's built for.", 
    "Who Dares Wins",
    "Breathe",
    "Run",
    "The world lives up to all of your expectations.", 
    "42",     
    ]
r = random.randint(2, (len(s)-1))



print('\n','\n',"_____________________________________________________",'\n','\n',"YOUR FORTUNE COOKIE THOUGHT FOR TODAY: ", 
      '\n','\n', s[r],'\n','\n',"_____________________________________________________",'\n','\n',)

      
'''
Next,  we ask her to load the libraries for work.
'''
 
print('🧐 I am initiating the following for us:', '\n','\n')

import warnings
warnings.filterwarnings('ignore')
print('1.  Warnings: Off')

import pandas as pd
print('2.  Pandas Initiated as pd')

import numpy as np
print('3.  Numpy Initiated as np')

import matplotlib.pyplot as plt
print('4.  Matplotlib.pyplot Initiated as plt')

import seaborn as sns
sns.set(style='darkgrid')
print('5.  Seaborn Initiated as sns. Style is set at \'darkgrid\'.')

# import ggplot as gg
print('6.  ggplot is having problems.')

import matplotlib.style
import matplotlib as mpl
plt.style.use('fivethirtyeight')
print('7.  Matplotlib Initiated as mpl. Matplotlib style set to "fivethirtyeight"')

from tqdm import tqdm
print('8.  tqdm Initiated')

np.random.seed(42)
print('9.  Random Seed set at: 42')

from IPython.display import display
print('10. IPython Display Initiated')

from bs4 import BeautifulSoup
print('11. BeautifulSoup Initiated')

import csv
print('12. Import csv Initiated')

import random
print('13. Import random Initiated','\n')

pd.options.display.max_rows = 10000
pd.options.display.max_columns = 1000

print('14. Any other library that you will need for the functions will be initiated as you call for them.')

print('___________________________________________','\n','\n', '🧐 The following functions are also ready:', '\n')

print('\n', "eda(df) function ready for use.", '\n', 
    '\t', "The eda(df) function will return a basic eda on our DataFrame. This includes the DataFrame's shape,"
      '\n', '\t', "description, data types, statistical information.")

print('\n', "vda(df) function ready for use.", '\n', 
      '\t', 'This function will return a visual data analysis of both the numeric and categorical columns in', 
      '\n', '\t', 'the DataFrame.')

print('\n', 'histogram(df) function ready for use - in the event you want to do a separate one.', '\n',
       '\t', 'This function will return a histogram of both the numeric and categorical columns in', 
      '\n', '\t', 'the DataFrame.')

print('\n', 'two_dimension_histogram(x, y) function is ready for use - in the event you want to do a separate one.', '\n',
      '\t', 'This function will return a two dimensional histogram. This will provide counts of features ',
      '\n', '\t', 'against another feature.')
      
print('\n', 'pairplot(df, feature) function ready for use - in the event you want to do a separate one.', '\n',
       '\t', 'This function will return a pairplot of both the numeric columns in the DataFrame', 
      '\n', '\t', 'against the feature you specify.')

print('\n', 'heatmap(df) function ready for use - in the event you want to do a separate one.', '\n',
       '\t', 'This function will return a heatmap of the numeric columns in the DataFrame.')

print('\n', 'kdeplot(df) function ready for use - in the event you want to do a separate one.', '\n',
       '\t', 'This function will return a kdeplot of the categorical columns in the DataFrame.')

print('\n','correlations(compare_feature, df) function ready for use.', '\n',
       '\t','This function will return a list of the correlations between the numeric columns in the DataFrame.','\n', 
      '\t', 'Additionally, this function will return three evaluations of the correlations (STRONGLY, MILDLY, or','\n', 
      '\t', 'NEGATIVELY). STRONGLY correlated are those greater than 0.50. MILDLY correlated are those between 0.40','\n', 
      '\t', 'and 0.49. NEGATIVELY correlated are any negative correlations.' ,'\n', 
      '\t', 'It will return strong_correlation, mild_correlation, and neg_correlation.', '\n','\n', 
      '\t', 'IT WILL NOT RETURN AN EVALUATION FOR CORRELATIONS BETWEEN 0.0 - 0.39.')  

print('\n', 'do_we_need_to_clean(df) function ready for use.','\n',
       '\t','This function will evaluate our dataset for null values. It will return a recommended_drop_list','\n',
       '\t','of features where more than 10.01% of total values for that feature are null or missing.''\n',
       '\t','When used in conjunction with drop_recommended_list(df), this function makes cleaning data just', '\n',
       '\t','a bit easier. However, IT IS NOT DESIGNED TO DO ALL OF THE DATA CLEANING.')

print('\n', 'drop_recommended_list(df) function ready for use.','\n',
      '\t','This function will delete from the DataFrame the features identified in the "recommended_drop_list"','\n',
      '\t','from the "do_we_need_to_clean(df)" function.')

print('\n', 'break_down_features(df) function ready for use.','\n',
      '\t','This function will split the numeric and categorical features into two sets: num_columns, cat_columns.')

print('\n', 'predictive_strength(df) function ready for use.', '\n',
      '\t', "This function determines the prescriptive strength of numeric features in our dataset. 'Prescriptive",'\n',
      '\t',"Strength' equals the measure of precentage of null values plus skew of the feature's data subtracted ",'\n',
      '\t',"from 100%. The result tells us the feature's value's confidence score. A 100 score says that there are",'\n',
      '\t',"no nulls within the data set and there is no skew to the data.")

print('\n', "pandas_profiling(df) function ready for use.", '\n', 
      '\t', "The pandas_profiling(df) function will return an advanced eda on our DataFrame. This includes the ",'\n',
      '\t', "DataFrame's shape, description, data types, statistical information.")

print('\n', "feature_review(df) function ready for use.", '\n',
      '\t', "The feature_review(df) function will ask the analyst to look at each feature one at a time.", '\n',
      '\t', "During each examination, Python will show the analyst salient aspects of each feature and pose to", '\n',
      '\t', "analyst the ability to change the feature type and delete the feature from the dataset.")

print('\n', "___________________________________________", '\n')



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
Next is the eda function load that includes. 
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
Left off trying to have it delete a column on request and change the dtype on request.

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