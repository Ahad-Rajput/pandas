import pandas as pd

# read data from csv file
df = pd.read_csv('data.csv')
# print(df)
# print(df['name'])  # print only 'name' column

df_1 = df[df['marks'] > 70]  # Filter the data and give only that data where marks greater than 70
# print(df_1)

df_2 = df[df['name'] == 'Ahmad']  # Filter the data and give only data in which name is 'Ahmad'
# print(df_2)

df.to_excel('some_data.xlsx')
print(df)
"""
df.to_excel() <- This create an excel file and copy our csv data in it
"""
