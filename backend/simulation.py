from fastapi import APIRouter, HTTPException
from app.services.state_store import state_store
from app.services.financial_engine import trigger_payment_delay
router = APIRouter(tags=["Demo"])
@router.post("/simulate/{event_type}")
def simulate(event_type: str):
    if event_type != "PAYMENT_DELAYED": raise HTTPException(400, "Only PAYMENT_DELAYED is available in this demo")
    state, events, data = trigger_payment_delay(state_store.baseline()); state_store.set_delay(state, events, data)
    return {"event_type": event_type, "current_state": state, "events": events}
@router.get("/simulation")
def simulation(): return state_store.simulation()
@router.post("/simulation/reset")
def reset():
    state_store.reset(); return {"status": "reset", "message": "Baseline restored; events and simulation cleared."}
