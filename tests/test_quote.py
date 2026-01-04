from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_quote():
    response = client.post("/quote", json={
        "client": {"name": "Gulf Eng.", "contact": "omar@x.com", "lang": "en"},
        "currency": "SAR",
        "items": [
            {"sku": "ALR-SL-90W", "qty": 10, "unit_cost": 100, "margin_pct": 20}
        ],
        "delivery_terms": "DAP Dammam",
        "notes": "Test"
    })
    assert response.status_code == 200
    assert response.json()["grand_total"] == 1200.0
