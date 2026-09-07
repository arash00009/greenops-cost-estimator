REGIONS = {
    "eu-north-1": {
        "name": "EU (Stockholm)",
        "price_per_hour_usd": 0.096,
        "carbon_intensity_gco2_per_kwh": 13,
    },
    "eu-west-1": {
        "name": "EU (Ireland)",
        "price_per_hour_usd": 0.104,
        "carbon_intensity_gco2_per_kwh": 316,
    },
    "eu-central-1": {
        "name": "EU (Frankfurt)",
        "price_per_hour_usd": 0.114,
        "carbon_intensity_gco2_per_kwh": 338,
    },
    "us-east-1": {
        "name": "US East (N. Virginia)",
        "price_per_hour_usd": 0.083,
        "carbon_intensity_gco2_per_kwh": 379,
    },
    "us-west-2": {
        "name": "US West (Oregon)",
        "price_per_hour_usd": 0.083,
        "carbon_intensity_gco2_per_kwh": 91,
    },
}

INSTANCE_MULTIPLIERS = {
    "small": 1.0,
    "medium": 2.0,
    "large": 4.0,
    "xlarge": 8.0,
}

INSTANCE_POWER_WATTS = {
    "small": 15,
    "medium": 30,
    "large": 60,
    "xlarge": 120,
}
