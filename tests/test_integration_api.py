from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_analyze_endpoint_success():
    payload = {
        "transaction_id": "tx_req_881",
        "account_id": "acc_551",
        "amount": 350.0,
        "currency": "USD",
        "country": "BO",
        "merchant_category": "retail",
        "device_id": "dev_ios_99"
    }
    response = client.post("/api/v1/transactions/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "decision" in data
    assert "risk_score" in data
    assert data["decision"] == "APPROVED"

def test_analyze_endpoint_validation_error():
    payload = {
        "transaction_id": "tx_req_882",
        "account_id": "acc_551",
        "amount": 350.0,
        "currency": "USD",
        "country": "BO",
        "merchant_category": "retail"
    }
    response = client.post("/api/v1/transactions/analyze", json=payload)
    assert response.status_code == 422
