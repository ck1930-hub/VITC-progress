from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_demo_flow():
    client.post("/simulation/reset")
    state = client.get("/state").json(); assert state["bank_balance"]["value"] == 32000; assert state["expected_payment"]["confidence"] == 0.78; assert state["emergency_buffer"]["value"] == 15000
    assert client.post("/simulate/PAYMENT_DELAYED").status_code == 200
    state = client.get("/state").json(); assert state["expected_payment"]["confidence"] == 0.45; assert state["payment_timing"]["certainty"] == "UNKNOWN"
    assert [x["message"] for x in client.get("/events").json()] == ["Payment delay message received", "Confidence reduced", "Payment timing unknown", "Financial state recalculated", "Risks detected", "Alternatives evaluated", "PAUSE_SIP selected"]
    assert len(client.get("/risks").json()["risks"]) == 4
    rec = client.get("/recommendation").json(); assert rec["recommended_action"] == "PAUSE_SIP"; assert [x["action"] for x in rec["alternatives"]] == ["DO_NOTHING", "PAUSE_SIP", "REDUCE_DISCRETIONARY_SPENDING"]
    data = client.get("/simulation").json(); assert all(len(data["projections"][name]) == 30 for name in ["pessimistic", "expected", "optimistic"])
    client.post("/simulation/reset"); assert client.get("/events").json() == []
