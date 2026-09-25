# GreenOps Cost & Carbon Estimator

![CI](https://github.com/arash00009/greenops-cost-estimator/actions/workflows/ci.yml/badge.svg)

A small REST API that estimates cloud cost (USD) and carbon footprint (grams of CO2) for different cloud instances and regions. Built as a capstone project to show how the choice of region and instance size affects both cost and climate impact, a core idea behind [GreenOps Sweden](https://greenops.se).

## API endpoints

### GET /version
Returns the app version.

### GET /regions
Lists available regions with price per hour and carbon intensity (g CO2/kWh).

### POST /estimate
Calculates estimated cost and CO2 footprint.

**Request body:**
```json
{
  "region": "eu-north-1",
  "instance_size": "medium",
  "hours": 720
}
```

**Response:**
```json
{
  "region": "eu-north-1",
  "region_name": "EU (Stockholm)",
  "instance_size": "medium",
  "hours": 720,
  "estimated_cost_usd": 138.24,
  "estimated_carbon_grams_co2": 280.8
}
```

Available `instance_size` values: `small`, `medium`, `large`, `xlarge`

## Run locally

```bash
python3 app.py
```

## Run with Docker

```bash
docker build -t greenops-cost-estimator:v0.1.0 .
docker run --rm -p 5000:5000 greenops-cost-estimator:v0.1.0
```

## Tests

```bash
pip install -r requirements.txt
pytest -v
```

## Linting

```bash
flake8 app.py test_app.py regions_data.py --max-line-length=100
```

## About the data

The price and carbon figures in `regions_data.py` are **illustrative estimates** based on publicly known patterns (the Nordics generally have lower carbon intensity thanks to hydro and nuclear power). They are not fetched live from any provider API, to keep the project simple, reliably testable and independent of external services.

## Tech stack

Python (Flask), Docker, GitHub Actions, pytest, flake8
