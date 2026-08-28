from datetime import datetime, timedelta, timezone
from app.models.schemas import EventTrailItem, RiskFactor, RecommendationOption

def projections():
    return {"pessimistic": [{"day": d, "balance": 32000-d*950} for d in range(1,31)], "expected": [{"day": d, "balance": 32000-d*300} for d in range(1,31)], "optimistic": [{"day": d, "balance": 32000+d*100} for d in range(1,31)]}
def trigger_payment_delay(state):
    now = datetime.now(timezone.utc); state.expected_payment.confidence = 0.45; state.expected_payment.timestamp = now; state.payment_timing.certainty = "UNKNOWN"; state.payment_timing.confidence = 0.0; state.payment_timing.timestamp = now
    messages = ["Payment delay message received", "Confidence reduced", "Payment timing unknown", "Financial state recalculated", "Risks detected", "Alternatives evaluated", "PAUSE_SIP selected"]
    return state, [EventTrailItem(sequence=i+1, message=m, timestamp=now+timedelta(seconds=i)) for i,m in enumerate(messages)], projections()
def risks():
    return [RiskFactor(category="INCOME_UNCERTAINTY", severity="HIGH", score=85, explanation="The expected ₹22,000 payment now has only 0.45 confidence and no known arrival date.", evidence=["expected_payment.confidence=0.45", "payment_timing=UNKNOWN"]), RiskFactor(category="ESSENTIAL_OBLIGATION_RISK", severity="HIGH", score=80, explanation="Rent, EMI, and insurance total ₹23,500 and depend on uncertain income.", evidence=["rent=15000", "emi=6000", "insurance=2500"]), RiskFactor(category="LOW_EMERGENCY_BUFFER", severity="HIGH", score=75, explanation="The ₹32,000 balance is only modestly above the ₹15,000 emergency buffer.", evidence=["bank_balance=32000", "emergency_buffer=15000"]), RiskFactor(category="GOAL_CONFLICT", severity="MEDIUM", score=68, explanation="Continuing the ₹5,000 SIP competes with preserving cash for essential obligations.", evidence=["sip=5000", "payment_timing=UNKNOWN"])]
def options():
    return [RecommendationOption(action="DO_NOTHING", projected_minimum_balance=23000, obligation_safety=False, overall_score=35, explanation="Keeps investing while income timing is unknown."), RecommendationOption(action="PAUSE_SIP", projected_minimum_balance=28000, obligation_safety=True, overall_score=92, explanation="Preserves ₹5,000 of near-term liquidity without changing essential commitments."), RecommendationOption(action="REDUCE_DISCRETIONARY_SPENDING", projected_minimum_balance=26000, obligation_safety=True, overall_score=71, explanation="Improves cash position, but needs behavioral cuts and preserves SIP outflow.")]
