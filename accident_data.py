import pandas as pd
import folium
from folium.plugins import HeatMapWithTime

df1 = pd.read_csv('traffic_accidents_2014.csv', header=0)
# df1.columns = column_names
print(df1)
df1.shape
df1.head()
# convert date for pandas
df1['date'] = pd.to_datetime(df1["date"], format='%Y-%m-%d')
print(df1.dtypes)
df1.head()
print(df1['date'])
cols_to_convert = ['Latitude', 'Longitude']
for col in cols_to_convert:
    df1[col] = pd.to_numeric(df1[col], errors='coerce')
print(df1['Latitude'])
print(df1.dtypes)
df1.isna().sum(axis=0)
df2 = df1.loc[df1.Latitude.isnull()]
df2.shape
df1 = df1.dropna(subset=['Latitude', 'Longitude'])
df1.shape
df2.shape
print(df1.loc[(df1['num_of_fatalities'] >= 1.0), [
    'district_commune', 'Latitude', 'Longitude', 'num_of_fatalities']])
df3 = df1[df1['num_of_fatalities'] < 0]
df3.shape
from folium.plugins import HeatMap

df_map = df1.copy()
df_map['count'] = 1
df_map[['Latitude', 'Longitude', 'count']].groupby(
    ['Latitude', 'Longitude']).sum().sort_values('count', ascending=False).head(10)

df_map.shape
print(df1['type_of_injury'].unique())


def generateBaseMap(default_location: object = [51.519120, 21.281183], default_zoom_start: object = 12) -> object:
    return folium.Map(location=default_location,
                      control_scale=True, zoom_start=default_zoom_start)


base_map = generateBaseMap()
base_map
m = HeatMap(data=df_map[['Latitude', 'Longitude', 'count']].groupby(
    ['Latitude', 'Longitude']).sum().reset_index().values.tolist(), radius=7, max_zoom=10).add_to(base_map)
m.save('/home/michalm/Projects/Python/ACCIDENTS/heatmap.html')

df_map.head()

print(df1['weather_conditions'].unique())
df_map[['weather_conditions', 'date', 'count']].groupby(
    ['weather_conditions', 'date']).sum().sort_values('count', ascending=False)

print('hello')
print(df2.head(3))

df2['count'] = 0
df5 = df2[['district_commune', 'count']].groupby(['district_commune']).sum().sort_values('count', ascending=False)
df5.shape
df5.head
pd.DataFrame(df5).to_csv('/home/michalm/Projects/Python/ACCIDENTS/towns.csv')


def f(var):
    if isinstance(var, pd.DataFrame):
        print('dataframe')
    else:
        print('not a dataframe, prob a list')


f(df5)
town_names = []
df2.dropna(subset=['district_commune'])
town_names = df2['district_commune'].unique()
print(town_names)
