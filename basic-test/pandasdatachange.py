import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A': ['df1_A0', 'df1_A1', 'df1_A2'],
                    'B': ['df1_B0', 'df1_B1', 'df1_B2'],
                    'C': ['df1_C0', 'df1_C1', 'df1_C2']},
                   index=[0, 1, 2])

df2 = pd.DataFrame({'E': ['df2_E4', 'df2_E3', 'df2_E2'],
                    'D': ['df2_D4', 'df2_D3', 'df2_D2'],
                    'C': ['df1_C4', 'df1_C3', 'df1_C2']},
                   index=[4, 3, 2])

df3 = pd.DataFrame({'F': [np.nan, np.nan, np.nan],
                    'G': [np.nan, 'df3_G6', 'df3_G7'],
                    'C': ['df3_C6', 'df3_C6', 'df3_C7']},
                   index=[5, 6, 7])

#pandas concat
#combine col and data
result = pd.concat([df1,df2]) #sort=true, axis by default which is 0
print(result)

#axis=0 stack data vertically, allign by col |, sort= false
result = pd.concat([df1,df2], axis=0, sort=False)
print(result)

#axis=1 stack data horizontally, align by index/row
result = pd.concat([df1,df2], axis=1)
print(result)

#data frame append
#same like concate combine data
#result = df1.append(df2)
#print(result)
#df3 = pd.DataFrame({'F': ['df2_F5', 'df2_F6', 'df2_F7'],
#                    'G': ['df2_G5', 'df2_G6', 'df2_G7'],
 #                   'H': ['df1_H5', 'df1_H6', 'df1_H7']},
 #                  index=[5, 6, 7])
#result = df1.append([df2, df3])
#print(result)
#cannot use append anymore coz vesion use concat

#delete data
def get_df():
    return pd.concat([df1,df2,df3], sort=True, ignore_index=True)
df = get_df()
print(df)

#delete by col
df = df.drop(columns=['C','D','E','G'])
print(df)

#delete  by row
df = df.drop(index=[1,3,4,8])
print(df)

#delete col that have all nan val
df = df.dropna(axis=1, how='all')
print(df)

#delete data even if only one nan in row
def get_dfs():
    return pd.concat([df1,df2,df3], sort=True, ignore_index=True)
dfs = get_dfs()
print(dfs)

dfs = dfs.dropna(axis=0, how='any')
print(dfs)

###
# axis=0 --> row
# axis=1 --> col
# any = even if one delete all
# all = if all col/row nan delete that col/row