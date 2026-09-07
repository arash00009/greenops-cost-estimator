from flask import Flask, jsonify, request
from regions_data import REGIONS, INSTANCE_MULTIPLIERS, INSTANCE_POWER_WATTS


app = Flask(__name__)

__version__ = "v0.1.0"


@app.route("/version", methods=["GET"])
def version():
    return jsonify({"version": __version__})


@app.route("/regions", methods=["GET"])
def regions():
    return jsonify(REGIONS)


@app.route("/estimate", methods=["POST"])
def estimate():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    region_id = data.get("region")
    instance_size = data.get("instance_size")
    hours = data.get("hours")

    if region_id not in REGIONS:
        return jsonify({
            "error": f"Unknown region '{region_id}'",
            "available_regions": list(REGIONS.keys())
        }), 400

    if instance_size not in INSTANCE_MULTIPLIERS:
        return jsonify({
            "error": f"Unknown instance_size '{instance_size}'",
            "available_sizes": list(INSTANCE_MULTIPLIERS.keys())
        }), 400

    if not isinstance(hours, (int, float)) or hours <= 0:
        return jsonify({"error": "hours must be a positive number"}), 400

    region = REGIONS[region_id]
    multiplier = INSTANCE_MULTIPLIERS[instance_size]
    power_watts = INSTANCE_POWER_WATTS[instance_size]

    cost_usd = round(region["price_per_hour_usd"] * multiplier * hours, 4)

    energy_kwh = (power_watts / 1000) * hours
    carbon_grams = round(energy_kwh * region["carbon_intensity_gco2_per_kwh"], 2)

    return jsonify({
        "region": region_id,
        "region_name": region["name"],
        "instance_size": instance_size,
        "hours": hours,
        "estimated_cost_usd": cost_usd,
        "estimated_carbon_grams_co2": carbon_grams,
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
