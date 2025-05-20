import pandas as pd
from os import path

#read from excel
root_path = r'C:\Users\user\Desktop\2.1학기\python\p1\titanic_data'
df = pd.read_excel(path.join(root_path, 'titanic.xlsx'))
print(df.head())

#read specific sheet in excel
df = pd.read_excel(path.join(root_path,'titanic.xlsx'), sheet_name=1)
print(df.head())

df = pd.read_excel(path.join(root_path,'titanic.xlsx'), sheet_name='Pclass3')
print(df.head())