import pandas as pd

df1 = pd.read_csv('traffic_accidents_2014.csv', header=0)
print(df1)
df1.shape
df1.head()
# convert date for pandas
df1['date'] = pd.to_datetime(df1["date"], format = '%Y-%m-%d')
print(df1.dtypes)
df1.head()
print(df1['date'])

print(df1['Latitude'])
print(df1.dtypes)
