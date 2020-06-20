import folium
import pandas

data = pandas.read_csv("volcanoes.csv")

def valencia_map():
    map = folium.Map(location=[39.47, -0.32], zoom_start=14, tiles="Stamen Terrain")

    fg = folium.FeatureGroup(name="Valencia")
    fg.add_child(folium.Marker(location=[39.45, -0.35], popup="Ciutat de les arts i les ciències", icon=folium.Icon(color='green')))
    map.add_child(fg)

    map.save("valencia.html")

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif elevation < 3000:
        return "orange"
    else:
        return "red"

def volcanoes(data):
    name = list(data["NAME"])
    lat = list(data["LAT"])
    lon = list(data["LON"])
    elev = list(data["ELEV"])

    map = folium.Map(location=[38.20, -120.77], zoom_start=6, tiles="Stamen Terrain")

    fg = folium.FeatureGroup(name="Volcanoes")
    for n, lt, ln, el in zip(name, lat, lon, elev):
        popup = f"{n}. {el} m."
        fg.add_child(folium.Marker(location=[lt, ln], popup=popup, icon=folium.Icon(color=color_producer(el))))
        map.add_child(fg)

    map.save("volcanoes.html")

valencia_map()
volcanoes(data)