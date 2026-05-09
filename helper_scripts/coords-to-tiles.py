import math

def lat_lon_to_tile(lat, lon, zoom):
  """Convert latitude/longitude to Web Mercator tile coordinates"""
  n = 2.0 ** zoom
  x = (lon + 180.0) / 360.0 * n
  y = (1.0 - math.log(math.tan(math.radians(lat)) + 1.0 / math.cos(math.radians(lat))) / math.pi) / 2.0 * n
  return int(x), int(y)

# lat = -16.492981
# lon = -68.147455
# zoom = 15
# http://localhost:8081/data/v3/#15.65/-16.492981/-68.147455

# lat = -16.49964
# lon = -68.123076
# zoom = 17
# # http://localhost:8081/data/v3/#16.91/-16.49964/-68.123076

lat = -16.4916557
lon = -68.1448621
zoom = 17 // closest zoom // mi teleferico on sight
# http://localhost:8080/map/v3/hsl-map/17/40725/71625.png
zoom = 15 // far zoom // mi teleferico not on sight
# http://localhost:8080/map/v3/hsl-map/15/10181/17906.png

x, y = lat_lon_to_tile(lat, lon, zoom)
print(f"Zoom: {zoom}")
print(f"X (tile_column): {x}")
print(f"Y (tile_row): {y}")
print(f"\nRequest URL:")
print(f"http://localhost:8080/map/v3/hsl-map/{zoom}/{x}/{y}.png")
