import pandas as pd
from os import path

#read from json
root_path = r'C:\Users\user\Desktop\2.1학기\python\p1\titanic_data'
df = pd.read_json(path.join(root_path, 'titanic.json'))
print(df.head())