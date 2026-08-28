from fastapi import APIRouter
from app.models.schemas import FinancialState
from app.services.state_store import state_store
router = APIRouter(tags=["Demo"])
@router.get("/state", response_model=FinancialState)
def get_state(): return state_store.snapshot()
