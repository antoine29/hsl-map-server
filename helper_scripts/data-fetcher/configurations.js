const {
  HSL_OTP_URL,
  FINLAND_OTP_URL,
  WALTTI_OTP_URL,
  PARKANDRIDE_URL,
  TICKET_SALES_URL
} = require("../constants");
const { queries, wranglers } = require("./data");

const layers = [
  {
    name: "hsl-stops",
    sources: [
      {
        url: HSL_OTP_URL,
        gqlQuery: queries.stopQuery,
        wrangler: wranglers.stopWrangler,
        file: "hsl-stops.geojson",
      },
      {
        url: HSL_OTP_URL,
        gqlQuery: queries.stationQuery,
        wrangler: wranglers.stationWrangler,
        file: "hsl-stations.geojson",
      }
    ]
  },
];

module.exports = layers;
