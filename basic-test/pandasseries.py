#using pandas lib

import pandas as pd

# make dict to series
series_dictionary = pd.Series({'b': 1, 'a': 0, 'c': 2})
series_dictionary.head()

# make array to series
series_array = pd.Series([3, 6, 9], index=['b', 'a', 'c'])
series_array.head()

series_array = pd.Series([3, 6, 9], index=[2, 1, 3])
series_array.head()

#to not put index
series_array = pd.Series([3, 6, 9])
series_array.head()

#one data series
series_single_value = pd.Series(1)
series_single_value.head()

series_single_value = pd.Series(1, index=['b', 'a', 'c'])
series_single_value.head()

#read series
series = pd.Series({'a': 1, 'c': 0, 'b': 2})
series.head()
len(series) #return length

series = pd.Series([1, 2, 3, 5, 6, 7])
series.head(10)
len(series)

#read data through index
series = pd.Series({'a': 1, 'c': 0, 'b': 2})
series.head()
series[0]
series[[0]]
series[[0, 2]]

#use real index
series['a']
series[['a']]
series[['a', 'b']]

#use index range to read
series[:2] #read from (index 0) up to (but not including) the element at index 2
series[1:] #read from index 1 till end
series[:-1] #read all execpt last index
series[-1:] #read last index