import folium
from pprint import pprint
from igc_parse import Flight, dms2dec

a = Flight(
    "/Users/christianmiles/Documents/egh400-2/EGH400/2023-01-02-XCT-LVY-01.igc"
)

m = folium.Map(
    location=[dms2dec(a.nav_data[0]["lat"]), dms2dec(a.nav_data[0]["lon"])],
    zoom_start=12,
    tiles="Stamen Terrain",
)

points = []
for i in a.nav_data:
    points.append([dms2dec(i["lat"]), dms2dec(i["lon"])])

folium.PolyLine(points, color="red").add_to(m)

m.save("map.html")
