# GreenOps Cost & Carbon Estimator

![CI](https://github.com/arash00009/greenops-cost-estimator/actions/workflows/ci.yml/badge.svg)

Ett litet REST-API som uppskattar molnkostnad (USD) och koldioxidavtryck (gram CO2) för olika cloud-instanser och regioner. Byggt som ett Capstone-projekt för att visa hur regionval och instansstorlek påverkar både kostnad och klimatpåverkan — en central idé bakom [GreenOps Sweden](https://greenops.se).

## API-endpoints

### GET /version
Returnerar appens version.

### GET /regions
Listar tillgängliga regioner med pris per timme och carbon intensity (g CO2/kWh).

### POST /estimate
Beräknar uppskattad kostnad och CO2-avtryck.

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

Tillgängliga `instance_size`: `small`, `medium`, `large`, `xlarge`

## Köra lokalt

```bash
python3 app.py
```

## Köra med Docker

```bash
docker build -t greenops-cost-estimator:v0.1.0 .
docker run --rm -p 5000:5000 greenops-cost-estimator:v0.1.0
```

## Tester

```bash
pip install -r requirements.txt
pytest -v
```

## Linting

```bash
flake8 app.py test_app.py regions_data.py --max-line-length=100
```

## Om datan

Pris- och carbon-siffrorna i `regions_data.py` är **illustrativa uppskattningar** baserade på offentligt kända mönster (Norden har generellt lägre carbon intensity tack vare vatten- och kärnkraft). De är inte hämtade live från något leverantör-API, för att hålla projektet enkelt, pålitligt testbart och oberoende av externa tjänster.

## Tech stack

Python (Flask), Docker, GitHub Actions, pytest, flake8
