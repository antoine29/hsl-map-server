import math
import re

def tile_to_lat_lon(x, y, zoom):
    """Convert Web Mercator tile coordinates to latitude/longitude"""
    n = 2.0 ** zoom
    lon = x / n * 360.0 - 180.0
    lat_radians = math.atan(math.sinh(math.pi * (1 - 2 * y / n)))
    lat = math.degrees(lat_radians)
    return lat, lon

# url = "http://localhost:8080/map/v3/hsl-stop-map/17/40730/71627.pbf" // -16.49666566287544,-68.1317138671875 // lpz valid point 404
url = "http://localhost:8080/map/v3/hsl-stop-map/13/4662/2370.pbf" // 60.19615576604439,24.873046875 // helsinki ok


match = re.search(r'/(\d+)/(\d+)/(\d+)\.pbf', url)
if not match:
    raise ValueError(f"Could not parse tile coordinates from URL: {url}")
zoom = int(match.group(1))
x = int(match.group(2))
y = int(match.group(3))

lat, lon = tile_to_lat_lon(x, y, zoom)
print(f"URL: {url}")
print(f"Zoom: {zoom}")
print(f"X (tile_column): {x}")
print(f"Y (tile_row): {y}")
print(f"Latitude: {lat}")
print(f"Longitude: {lon}")
print(f"{lat},{lon}")
