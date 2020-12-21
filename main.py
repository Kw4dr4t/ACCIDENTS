import pandas as pd
df = pd.read_csv('all.csv')

import plotly.express as px
fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='num_of_accidents',
                        radius=7, center=dict(lat=51.5191200, lon=21.281183), zoom =7,
                        mapbox_style="stamen-terrain")
fig.show()
