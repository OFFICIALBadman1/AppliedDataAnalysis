import pandas as pd

df = pd.read_excel('gobal_superstore_2016.xlsx', sheet_name='Orders', header=0, nrows=5) 

print(df.head())
print(df.columns)