import pandas as pd


df1 = pd.read_csv('/mnt/c/Users/김석원/Desktop/python_script/result.csv')
df2 = pd.read_csv('/mnt/c/Users/김석원/Desktop/python_script/')


result = pd.merge(df1, df2, left_on='cp_name', right_on='cp_name', how='inner')

