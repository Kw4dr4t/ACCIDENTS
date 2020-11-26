import pandas as pd
# column_names = ['Liczba wypadków', 'Liczba zabitych', 'Liczba rannych', 'Rok',
#                 'Warunki atmosferyczne', 'Rodzaj zdarzenia',
#                 'Warunki atmosferyczne', 'Oświetlenie', 'CHMZ', 'IDKSIP',
#                 'Godzina', ' Dzień', 'Ranny', 'GPS X', 'GPS Y', 'numer drogi',
#                 'Obszar', 'Geometria', 'Kategoria drogi', 'Rodzaj drogi',
#                 'Pijak', 'Powiat', 'Gmina']

df1 = pd.read_csv('traffic_accidents_2014.csv', header=0)
#df1.columns = column_names
print(df1)
df1.shape
df1.head()
# convert date for pandas
df1['date'] = pd.to_datetime(df1["date"], format = '%Y-%m-%d')
print(df1.dtypes)
df1.head()
print(df1['date'])
#cols_to_convert = ['GPS x', 'GPS y']
# for col in cols_to_convert:
#     df1[col] = pd.to_numeric(df1[col], errors='coerce')
print(df1['Latitude'])
print(df1.dtypes)
