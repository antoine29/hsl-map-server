# Data fetcher

> [!WARNING]
> The `data-fetcher/` scripts were removed on `352fa4d771f7: Merge pull request #140 from HSLdevcom/develop` commit. If you need to download the geojson files again, checkout to a previous commit and debug/run accordingly.

## Run data-fetcher scripts

The geojson files can be pulled from a running OTP (running at HSL_OTP_URL) instance using the data-fetcher script:

```
node data-fetcher/index.js

or

yarn run data-fetcher
```

## Run the OTP requests manually

data-fetcher/ scripts send requests to OTP. You can run these reqs manually:

Prod example:

```
curl -X POST \
"https://api.digitransit.fi/routing/v2/hsl/gtfs/v1" \
-H "digitransit-subscription-key: 6..." \
-H "Content-Type: application/graphql" \
-H "OTPTimeout: 120000" \
-H "OTPMaxResolves: 100000000" \
-d '
  query stops {
    stops {
      gtfsId
      name
      code
      platformCode
      lat
      lon
      locationType
      desc
      parentStation {
        gtfsId
      }
      patterns {
        headsign
        route {
          mode
          shortName
          gtfsType: type
        }
      }
    }
  }
'
```

Localhost example:

```
curl -X POST \
  "http://172.17.0.2:8080/otp/gtfs/v1" \
  -H "digitransit-subscription-key: undefined" \
  -H "Content-Type: application/graphql" 
  -H "OTPTimeout: 120000" \
  -H "OTPMaxResolves: 100000000" \
  -d '
    query stops {
      stops {
        gtfsId
        name
        code
        platformCode
        lat
        lon
        locationType
        desc
        parentStation {
          gtfsId
        }
        patterns {
          headsign
          route {
            mode
            shortName
            gtfsType: type
          }
        }
      }
    }
  '
```

