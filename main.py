import pandas as pd
import plotly.express as px

df = pd.read_csv('all.csv')

fig = px.density_mapbox(df,
                        lat='Latitude',
                        lon='Longitude',
                        z='num_of_accidents',
                        radius=7,
                        center=dict(lat=51.5191200, lon=21.281183),
                        zoom=7,
                        mapbox_style="open-street-map")
fig.show()

fig2 = px.scatter_mapbox(df,
                         lat='Latitude',
                         lon='Longitude',
                         hover_name="IDKSIP",
                         hover_data=[
                             "weather_conditions",
                             "lighting",
                             "type_of_accident",
                             "road_category"
                         ],
                         color_discrete_sequence=["fuchsia"],
                         zoom=3,
                         height=300
                         )
fig2.update_layout(mapbox_style="open-street-map")
fig2.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig2.show()
