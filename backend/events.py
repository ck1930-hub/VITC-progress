from fastapi import APIRouter
from app.models.schemas import EventTrailItem
from app.services.state_store import state_store
router = APIRouter(tags=["Demo"])
@router.get("/events", response_model=list[EventTrailItem])
def get_events(): return state_store.events()
