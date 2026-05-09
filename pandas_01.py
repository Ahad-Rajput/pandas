import pandas as pd

# read data from csv file
df = pd.read_csv('data.csv')
# print(df)
# print(df['name'])  # print only 'name' column

# df_1 = df[df['marks'] > 70]  # Filter the data and give only that data where marks greater than 70
# print(df_1)

df_2 = df[df['name'] == 'Ahmad']  # Filter the data and give only data in which name is 'Ahmad'
# print(df_2)

df.to_excel('some_data.xlsx')
# print(df)
"""
df.to_excel() <- This create an excel file and copy our csv data in it
"""

# print(df.info())  # Provide information about the data frame

# print(df.head())  # gives first 5 rows of the data set
"""
U can also specifies the no. rows like this, 'df.head(3)' => This'll print first 3 rows

""" 

# print(df.describe())   # Provide basic statistics about our data

max_std = df[df['marks'] == df['marks'].max()]  # Filter the data of student with maximum marks
print(max_std)