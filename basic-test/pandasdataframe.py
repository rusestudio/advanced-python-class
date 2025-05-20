import pandas as pd
import numpy as np

#make data frame

#make data frame from dict
df1 = pd.DataFrame({'a': [2, 4, 8], 
                    'b' : [3, 6, 9], 
                    'c':[5, 10, 15], 
                    'd':[7, 14, 21]})
df1.head()

#make 2d array to dataframe
df2 = pd.DataFrame(data=[[2, 3, 5, 7],
                         [4, 6, 10, 14],
                         [8, 9, 15, 21]], 
                         columns=['a', 'b', 'c', 'd'])
df2.head()

#use col name to make df
df2 = pd.DataFrame(data=[[2, 3, 5, 7],
                         [4, 6, 10, 14],
                         [8, 9, 15, 21]],
                           columns=['a', 'b', 'c', 'd'])
df2.head()

#use index to make df
df1 = pd.DataFrame({'a': [2, 4, 8], 
                    'b' : [3, 6, 9], 
                    'c':[5, 10, 15], 
                    'd':[7, 14, 21]}, 
                    index=['r1', 'r2', 'r3'])
df1.head()

df2 = pd.DataFrame(data=[[2, 3, 5, 7],
                         [4, 6, 10, 14],
                         [8, 9, 15, 21]], 
                         columns=['a', 'b', 'c', 'd'], 
                         index=['r1', 'r2', 'r3'])
df2.head()

#if no index or col it will be auto start with 0
df2 = pd.DataFrame(data=[[2, 3, 5, 7],
                         [4, 6, 10, 14],
                         [8, 9, 15, 21]])
df2.head()

#use np.nan for none or no data
df3 = pd.DataFrame(data=[[2, 3, 5, 7],
                         [4, 6, np.nan, np.nan],
                         [8, 9, 15, 21]], 
                         columns=['a', 'b', 'c', 'd'], 
                         index=['r1', 'r2', 'r3'])
df3.head()


#read dataframe
df1 = pd.DataFrame({'a': [2, 4, 8], 
                    'b' : [3, 6, 9], 
                    'c':[5, 10, 15], 
                    'd':[7, 14, 21], 
                    'e':[7, 14, 21]})
df1.head()

#read length row size data
len(df1)

#read col size
len(df1.columns)

#read col
df1.columns

#read dataframe use col
df1 = pd.DataFrame({'a': [2, 4, 8], 
                    'b' : [3, 6, 9], 
                    'c':[5, 10, 15], 
                    'd':[7, 14, 21]})
df1.head()

df1['a'] #data in col a
df1[['a', 'b']] #data in col a and b

#read dataframe use row/index
df3 = pd.DataFrame(data=[[2, 3, 5, 7],
                         [4, 6, np.nan, np.nan],
                         [8, 9, 15, 21]], 
                         columns=['a', 'b', 'c', 'd'], 
                         index=['r0', 'r1', 'r2'])
df3.head()

df3.iloc[0] #data at row index 0, only row
df3.iloc[[2, 0]] #data at row index 2 and 0, inc col
df3[0:2] #data start at i0 till i2 include col
df3[-3:-1]
df3.loc['r2'] #use serial to read row, only row
df3.loc[['r2', 'r1']]

#read specific data or one data 
df3.iat[1, 1] #use index
df3.at['r0', 'a'] #use index, col

