#data pipeline
#data pipeline process: data cleaning->transformation->
#                       Missing_Value_dimension->EV_filter->PCA_dimension

#read data from documents
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_selection import VarianceThreshold
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/mmy/LearnSpace/PythonSpace/python_data_pipeline/initial_data.csv')

def data_clean(df):

    #clean data
    #delete "ID number" column, which is useless for analysis
    df=df.drop(columns=['ID number'])
    #delete "Name" column, which is useless for analysis
    df=df.drop(columns=['Name'])
    #delete "Offers Other degree" column, because no one offer other degree,so this column is useless
    df=df.drop(columns=['Offers Other degree'])
    # drop data rows with missing values of Applicants total
    #The reason that why don't use df.dropna(), is that this method deletes too many data rows:from about 1500 to 350
    for i in range(len(df)):
        if str(df['Applicants total'][i]) == 'nan':
            df=df.drop([i])
            #print('Row:'+str(i)+'is None, Droped')
    #reset data index, because after dropna(), the index is really confused
    df=df.reset_index(drop=True)
    #data transformation, transform string:'yes','no' to '1','0', which can be calculated later
    df=df.replace('Yes',1)
    df=df.replace('No',0)
    #swap the data where applicants total is miner than total enrollment
    for i in range(len(df)):
        if df['Applicants total'][i] < df['Total  enrollment'][i]:
            temp=df['Applicants total'][i]
            df['Applicants total'][i]=df['Total  enrollment'][i]
            df['Total  enrollment'][i]=temp


    df.to_csv('/Users/mmy/LearnSpace/PythonSpace/python_data_pipeline/cleaned_data.csv')
    return df


def Missing_Value_dimension(df):
    #df = pd.read_csv('/Users/mmy/LearnSpace/PythonSpace/python_data_pipeline/initial_data.csv')
    #Output missing values to a file and determine how appropriate the threshold is
    a=df.isnull().sum()/len(df)*100
    with open("/Users/mmy/LearnSpace/PythonSpace/python_data_pipeline/Missing_Value_dimension_result.txt","w") as f:
        for i in range(len(a)):
            f.write(str(a[i]))
            f.write('\n')
    #After observing the results, it was found that there are a lot of non-missing values, so directly retain the values that are not missing, and discard the missing values
    delete=[]
    for i in range(len(a)):
        if a[i]!=0:
            #print(str(a[i]))
            delete.append(i)
    df=df.drop(df.columns[delete],axis=1,inplace=False)
    #print(delete)
    #print(df)
    df.to_csv('/Users/mmy/LearnSpace/PythonSpace/python_data_pipeline/Missing_Value_Dimension_data.csv')
    return df

def EV_filter(df):
    #Variance selection method, return the data after feature selection
    #Only keep columns with variance greater than 1000
    var=df.var()
    df_columns=df.columns
    df_temp=[]
    for i in range(len(var)):
        if var[i]>=1000:
            df_temp.append(df_columns[i])
    df=df[df_temp]
    print(df)
    df.to_csv('/Users/mmy/LearnSpace/PythonSpace/python_data_pipeline/EV_filter_result.csv')
    return df

def PCA_dimension(df):
    #df = pd.read_csv('/Users/mmy/LearnSpace/PythonSpace/python_data_pipeline/EV_filter_result.csv')
    from sklearn.decomposition import PCA
    pca = PCA(n_components=3)
    pca_result = pca.fit_transform(df)
    #Reference：https://zhuanlan.zhihu.com/p/43225794
    #After observing the plot, it is found that only 3 principal components can retain almost all the data.
    plt.plot(range(3), pca.explained_variance_ratio_)
    plt.plot(range(3), np.cumsum(pca.explained_variance_ratio_))
    plt.title("Component-wise and Cumulative Explained Variance")
    plt.show()
    print("finished")
    return df


PCA_dimension(EV_filter(Missing_Value_dimension(data_clean(df))))
