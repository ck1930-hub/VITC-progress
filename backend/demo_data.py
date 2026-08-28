from datetime import datetime, timezone
from app.models.schemas import Fact, FinancialState

def get_initial_demo_state() -> FinancialState:
    now = datetime.now(timezone.utc)
    confirmed = lambda value, source: Fact(value=value, source=source, certainty="CONFIRMED", confidence=1.0, timestamp=now)
    return FinancialState(bank_balance=confirmed(32000, "bank_statement"), expected_payment=Fact(value=22000, source="client_invoice", certainty="INFERRED", confidence=0.78, timestamp=now), payment_timing=Fact(value=0, source="client_commitment", certainty="INFERRED", confidence=0.78, timestamp=now), rent=confirmed(15000, "lease_agreement"), emi=confirmed(6000, "loan_statement"), insurance=confirmed(2500, "insurance_policy"), sip=confirmed(5000, "investment_account"), emergency_buffer=confirmed(15000, "personal_goal"))
