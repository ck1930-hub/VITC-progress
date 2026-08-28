from fastapi import APIRouter
from app.services.financial_engine import options
router = APIRouter(tags=["Demo"])
@router.get("/recommendation")
def recommendation():
    alternatives = options(); return {"alternatives": alternatives, "recommended_action": "PAUSE_SIP", "recommendation": alternatives[1]}
