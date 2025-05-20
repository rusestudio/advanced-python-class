import pandas as pd

#read csv file
from os import path

# Correct the path and file name
root_path = r'C:\Users\user\Desktop\2.1학기\python\p1\titanic_data'
df = pd.read_csv(path.join(root_path, 'titanic.csv'))

# Display the first few rows of the DataFrame
print(df.head())

#use csv data separator
df = pd.read_csv(path.join(root_path,'titanic_sep.csv'))
print(df.head())

#set var sep to "|"
df = pd.read_csv(path.join(root_path,'titanic_sep.csv'),sep='|')
print(df.head())