import pandas as pd 
  
# read an excel file and convert  
# into a dataframe object 
df = pd.DataFrame(pd.read_excel("/mnt/c/Users/김석원/Desktop/python_script/기업코드.xlsx" )) 
df.to_csv('/mnt/c/Users/김석원/Desktop/python_script/compinitial.csv', encoding='utf-8-sig')