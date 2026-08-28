from datetime import datetime
from typing import Literal
from pydantic import BaseModel

class Fact(BaseModel):
    value: float
    source: str
    certainty: Literal["CONFIRMED", "INFERRED", "UNKNOWN"]
    confidence: float | None = None
    timestamp: datetime

class FinancialState(BaseModel):
    bank_balance: Fact
    expected_payment: Fact
    payment_timing: Fact
    rent: Fact
    emi: Fact
    insurance: Fact
    sip: Fact
    emergency_buffer: Fact

class EventTrailItem(BaseModel):
    sequence: int
    message: str
    timestamp: datetime

class RiskFactor(BaseModel):
    category: str
    severity: Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]
    score: float
    explanation: str
    evidence: list[str]

class RecommendationOption(BaseModel):
    action: Literal["DO_NOTHING", "PAUSE_SIP", "REDUCE_DISCRETIONARY_SPENDING"]
    projected_minimum_balance: float
    obligation_safety: bool
    overall_score: float
    explanation: str
