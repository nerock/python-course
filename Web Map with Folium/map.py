import folium
map = folium.Map(location=[39.47, -0.32], zoom_start=3, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="Valencia")
fg.add_child(folium.Marker(location=[39.45, -0.35], popup="Ciutat de les arts i les ciències", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map.html")