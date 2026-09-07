import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_version_endpoint(client):
    response = client.get("/version")
    assert response.status_code == 200
    assert response.get_json()["version"] == "v0.1.0"


def test_regions_endpoint(client):
    response = client.get("/regions")
    assert response.status_code == 200

    data = response.get_json()
    assert "eu-north-1" in data
    assert "price_per_hour_usd" in data["eu-north-1"]
    assert "carbon_intensity_gco2_per_kwh" in data["eu-north-1"]


def test_estimate_valid_request(client):
    response = client.post("/estimate", json={
        "region": "eu-north-1",
        "instance_size": "medium",
        "hours": 720
    })
    assert response.status_code == 200

    data = response.get_json()
    assert data["estimated_cost_usd"] > 0
    assert data["estimated_carbon_grams_co2"] > 0
    assert data["region"] == "eu-north-1"


def test_estimate_invalid_region(client):
    response = client.post("/estimate", json={
        "region": "mars-1",
        "instance_size": "medium",
        "hours": 10
    })
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_estimate_invalid_instance_size(client):
    response = client.post("/estimate", json={
        "region": "eu-north-1",
        "instance_size": "gigantic",
        "hours": 10
    })
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_estimate_invalid_hours(client):
    response = client.post("/estimate", json={
        "region": "eu-north-1",
        "instance_size": "medium",
        "hours": -5
    })
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_estimate_missing_body(client):
    response = client.post("/estimate")
    assert response.status_code == 400


def test_estimate_low_carbon_region_beats_high_carbon(client):
    stockholm = client.post("/estimate", json={
        "region": "eu-north-1", "instance_size": "large", "hours": 100
    }).get_json()

    frankfurt = client.post("/estimate", json={
        "region": "eu-central-1", "instance_size": "large", "hours": 100
    }).get_json()

    assert stockholm["estimated_carbon_grams_co2"] < frankfurt["estimated_carbon_grams_co2"]
