import threading
from app.models.schemas import EventTrailItem
from app.services.demo_data import get_initial_demo_state

class StateStore:
    def __init__(self):
        self._lock = threading.Lock(); self._baseline = get_initial_demo_state(); self._current = self._baseline.model_copy(deep=True); self._events = []; self._projections = {}; self._active_event = None
    def snapshot(self):
        with self._lock: return self._current.model_copy(deep=True)
    def baseline(self):
        with self._lock: return self._baseline.model_copy(deep=True)
    def set_delay(self, state, events, projections):
        with self._lock: self._current = state.model_copy(deep=True); self._events = events; self._projections = projections; self._active_event = "PAYMENT_DELAYED"
    def events(self):
        with self._lock: return [item.model_copy() for item in self._events]
    def simulation(self):
        with self._lock: return {"is_active": self._active_event is not None, "active_event_type": self._active_event, "projections": self._projections}
    def reset(self):
        with self._lock: self._current = self._baseline.model_copy(deep=True); self._events = []; self._projections = {}; self._active_event = None
state_store = StateStore()
