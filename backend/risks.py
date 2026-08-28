from fastapi import APIRouter
from app.services.financial_engine import risks
router = APIRouter(tags=["Demo"])
@router.get("/risks")
def get_risks(): return {"risks": risks()}
