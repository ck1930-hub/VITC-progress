# Financial AI Backend API

A high-performance RESTful backend API built using **FastAPI**, **Pydantic v2**, and **Python**. It provides deterministic financial state calculations, interactive scenario event stress-testing, automated risk assessment, and AI-driven recommendations.

---

## Features & Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Health check & list of available routes. |
| `GET` | `/state` | Returns the current financial state (assets, liabilities, net worth, cashflow, DTI, emergency runway). |
| `GET` | `/events` | Catalog of simulation events (e.g. `market_crash`, `job_loss`, `inflation_surge`, `interest_rate_hike`, `unexpected_medical_expense`, `annual_bonus`). |
| `POST` | `/simulate/{event_type}` | Simulates the deterministic impact of an event on net worth, liquidity, and 1/3/5/10-year projections. Updates active state. |
| `GET` | `/simulation` | Retrieves the active simulation state, baseline vs. simulated metrics, and multi-year projection timeline. |
| `POST` | `/simulation/reset` | Resets active simulation back to the initial baseline state. |
| `GET` | `/risks` | Evaluates risk profile across Liquidity Risk, Debt Service (DTI), Asset Concentration, and Cashflow Margins with scores (0-100). |
| `GET` | `/recommendation` | Generates prioritized financial recommendations (High/Medium/Low) with quantified impact and concrete action steps. |

---

## Tech Stack

- **Framework**: FastAPI
- **Data Validation & Schemas**: Pydantic
- **ASGI Web Server**: Uvicorn
- **Testing**: Pytest & HTTPX TestClient
- **CORS Support**: Enabled for all origin domains (`*`) and local frontend ports (`http://localhost:3000`, `http://localhost:5173`, etc.).

---

## Quick Start & Installation

### 1. Prerequisites
Ensure you have Python 3.10+ installed.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Backend API Server

You can launch the server using either the launcher script:
```bash
python run.py
```
Or directly with Uvicorn:
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be live at:
- **Base URL**: `http://127.0.0.1:8000`
- **Interactive Swagger Docs**: `http://127.0.0.1:8000/docs`
- **ReDoc Documentation**: `http://127.0.0.1:8000/redoc`

---

## Running Automated Tests

To execute the automated unit test suite:
```bash
pytest
```

---

## API Usage Examples

### 1. Fetch Current Financial State
```bash
curl -X GET http://127.0.0.1:8000/state
```

**Sample Response (`200 OK`):**
```json
{
  "liquid_assets": 45000.0,
  "investment_assets": 380000.0,
  "real_estate_assets": 425000.0,
  "total_assets": 850000.0,
  "credit_card_debt": 4500.0,
  "student_loan_debt": 22000.0,
  "mortgage_debt": 253500.0,
  "total_liabilities": 280000.0,
  "net_worth": 570000.0,
  "monthly_income": 12500.0,
  "monthly_fixed_expenses": 4800.0,
  "monthly_variable_expenses": 2400.0,
  "total_monthly_expenses": 7200.0,
  "net_monthly_cashflow": 5300.0,
  "emergency_fund_months": 6.25,
  "savings_rate": 42.4,
  "debt_to_income_ratio": 20.0
}
```

### 2. Simulate a Market Crash Scenario
```bash
curl -X POST http://127.0.0.1:8000/simulate/market_crash \
  -H "Content-Type: application/json" \
  -d '{"magnitude": -0.25}'
```

### 3. Fetch Financial Risk Assessment
```bash
curl -X GET http://127.0.0.1:8000/risks
```

### 4. Fetch AI Recommendations
```bash
curl -X GET http://127.0.0.1:8000/recommendation
```

---

## Directory Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py                  # FastAPI application & CORS configuration
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py           # Pydantic data schemas
│   ├── services/
│   │   ├── __init__.py
│   │   ├── demo_data.py         # Seeded demo dataset & event catalog
│   │   ├── financial_engine.py  # Deterministic simulation, projections & risk rules
│   │   └── state_store.py       # In-memory thread-safe state store
│   └── routers/
│       ├── __init__.py
│       ├── state.py             # GET /state
│       ├── events.py            # GET /events
│       ├── simulation.py        # POST /simulate/{event_type} & GET /simulation
│       ├── risks.py             # GET /risks
│       └── recommendation.py    # GET /recommendation
├── tests/
│   ├── __init__.py
│   └── test_api.py              # Pytest endpoint test suite
├── requirements.txt             # Dependency manifest
├── run.py                       # Uvicorn launcher
└── README.md                    # Project documentation
```
