# map server

This is a map tiles service that uses DigiTransit hsl-map-server project fork.

## Local setup

1. Clone the forked repo:

```
git clone git@github.com:antoine29/hsl-map-server.git
```

2. Create a `hsl-map-server/data` folder. This folder should contain the required data files.

  ```
  finland.mbtiles
  hsl-stations.geojson
  hsl-stops.geojson
  ```

  Copy and rename the city files accordingly

3. build and run the container (mounting the data/ folder as a volume)

  ```
  docker build . -t map-server

  docker run -d \
    -p 8080:8080 \
    -v ${PWD}/data/:/opt/hsl-map-server/data \
    -e HSL_OTP_URL=172.17.0.3:8080/otp/gtfs/v1 \
    map-server:latest
  ```

## Testing the service

The following should download png tile images:

```
http://localhost:8080/map/v3/hsl-map/15/10181/17906.png
http://localhost:8080/map/v3/hsl-map/17/40733/71628.png
```

The following should download a pbf file:

```
curl -o pbf http://localhost:8080/map/v3/hsl-stop-map/14/5091/8954.pbf
```

## Getting the map data files

### mbtiles file

This is a file to render tile images for the city. Multiple approaches to get this file are available:

- Trimming down a country level osm.pbf file (not working):

  Geofabrik offers country level extracts:

  ```
  https://openmaptiles.org/docs/generate/create-custom-extract/
  https://download.geofabrik.de/south-america/bolivia.html
  ```

  Run the container:

  ```
  docker run -it \
    -v $(PWD)/data:/data \
    --entrypoint /bin/sh \
    ghcr.io/systemed/tilemaker:master
  ```

  Open a container shell and extract a city level file:

  ```
  ./tilemaker /data/bolivia-latest.osm.pbf \
    --bbox=-68.5,-17,-68,-16.3 --output lpz.mbtiles
  ```

  You can see/edit the delimiting bbox on `https://bboxfinder.com/#-17.239555,-69.206561,-15.751656,-67.281207`

  Check the generated mbtiles running the following container:

  ```
  docker run -it \
    -v $(pwd)/lpz.mbtiles:/data/lpz.mbtiles \
    -p 8081:8080 maptiler/tileserver-gl:latest
  ```

- Direct download (working, but it requires registration)

  Download the mbtiles directly from:

  ```
  https://www.maptiler.com/on-prem-datasets/dataset/osm/south-america/bolivia/la-paz/#9.26/-16.4295/-68.116
  ```

### geojson files

This map-server can also serve pbf files using geojson files with information about the stops. These pbf files are requested by the FE application. Editing/updating the existing geojson files is the easiest, if generating new files is required, check `data-fetcher.md`

## Notes

- If after stopping and restarting the map-server container, you just need to run a new service container

