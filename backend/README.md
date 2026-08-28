# Financial AI Command Center — Backend

## Overview

This backend provides the financial intelligence and decision-support layer for the Financial AI Command Center.

Built using FastAPI, the backend is responsible for managing financial state, processing financial events, running simulations, evaluating risks, generating future projections, and producing structured recommendations.

The backend exposes REST APIs consumed by the frontend dashboard.

---

# Backend Architecture

```text
                         CLIENT APPLICATION
                                │
                                │ HTTP / REST API
                                ▼
                 ┌──────────────────────────────┐
                 │       FASTAPI BACKEND        │
                 │                              │
                 │         API ROUTERS          │
                 │                              │
                 │  /state                      │
                 │  /events                     │
                 │  /simulate                   │
                 │  /simulation                 │
                 │  /risks                      │
                 │  /recommendation             │
                 └───────────────┬──────────────┘
                                 │
                                 ▼
              ┌────────────────────────────────────┐
              │      FINANCIAL STATE MANAGEMENT    │
              │                                    │
              │  Confirmed Balance                 │
              │  Expected Income                   │
              │  Payment Confidence                │
              │  Financial Obligations             │
              │  Emergency Buffer                  │
              │  Risk Tolerance                    │
              │  Event History                     │
              └──────────────────┬─────────────────┘
                                 │
                ┌────────────────┼────────────────┐
                │                │                │
                ▼                ▼                ▼

      ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
      │  EVENT ENGINE   │ │ SIMULATION      │ │   RISK ENGINE   │
      │                 │ │ ENGINE          │ │                 │
      │                 │ │                 │ │                 │
      │ PAYMENT_DELAYED │ │ Financial       │ │ Liquidity Risk  │
      │                 │ │ Projections     │ │ Income Risk     │
      │ State Updates   │ │                 │ │ Obligation Risk │
      │ Event Tracking  │ │ Pessimistic     │ │ Buffer Risk     │
      │                 │ │ Expected        │ │                 │
      │                 │ │ Optimistic      │ │                 │
      └────────┬────────┘ └────────┬────────┘ └────────┬────────┘
               │                   │                   │
               └───────────────────┼───────────────────┘
                                   │
                                   ▼

                    ┌──────────────────────────────┐
                    │    RECOMMENDATION ENGINE     │
                    │                              │
                    │ Evaluates Alternatives:      │
                    │                              │
                    │ • DO_NOTHING                 │
                    │ • PAUSE_SIP                  │
                    │ • REDUCE_DISCRETIONARY       │
                    │   SPENDING                   │
                    │                              │
                    │ Evaluation Factors:          │
                    │                              │
                    │ • Minimum Balance            │
                    │ • Obligation Safety          │
                    │ • Emergency Buffer           │
                    │ • Long-Term Goal Impact      │
                    │ • Overall Decision Score     │
                    │                              │
                    │ Output:                      │
                    │                              │
                    │ • Recommended Action         │
                    │ • Reasoning                  │
                    │ • Confidence                 │
                    │ • Trade-offs                 │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                        STRUCTURED API RESPONSE
                                   │
                                   ▼
                           FRONTEND DASHBOARD
```

---

# Financial Processing Flow

The backend processes financial events through the following pipeline:

```text
Financial Event
      │
      ▼
API Endpoint
      │
      ▼
Event Validation
      │
      ▼
Financial State Update
      │
      ├──────────────────────┐
      │                      │
      ▼                      ▼
Risk Analysis          Simulation Engine
      │                      │
      │                      ▼
      │               30-Day Projection
      │                      │
      └───────────┬──────────┘
                  │
                  ▼
          Alternative Evaluation
                  │
                  ▼
         Recommendation Generation
                  │
                  ▼
            Structured Response
```

---

# Core Responsibilities

The backend is responsible for:

- Managing the financial state
- Tracking financial events
- Processing payment disruptions
- Modeling income uncertainty
- Running financial simulations
- Generating deterministic scenario projections
- Evaluating financial risks
- Comparing possible interventions
- Generating structured recommendations
- Providing REST APIs to the frontend

---

# Financial State

The system maintains a representation of the user's financial situation.

```text
Financial State
│
├── Confirmed Balance
│
├── Expected Income
│     └── Payment Confidence
│
├── Financial Obligations
│     ├── Rent
│     ├── EMI
│     ├── Insurance
│     └── SIP
│
├── Emergency Buffer
│
├── Risk Tolerance
│
└── Event History
```

A key distinction in the financial model is:

```text
Confirmed Financial Information
        ≠
Expected or Uncertain Financial Information
```

This prevents the system from treating uncertain future income as immediately available cash.

---

# Event Processing

The backend processes financial events that can change the user's financial situation.

The current prototype includes the following event:

```text
PAYMENT_DELAYED
```

When this event is triggered:

```text
Expected Payment
      │
      ▼
Payment Delay Event
      │
      ▼
Financial State Updated
      │
      ▼
Income Certainty Recalculated
      │
      ▼
Financial Risk Recalculated
      │
      ▼
Future Scenarios Generated
      │
      ▼
Alternatives Compared
      │
      ▼
Recommendation Generated
```

---

# Simulation Engine

The simulation engine evaluates the possible future impact of financial events.

The system generates deterministic 30-day projections for multiple scenarios.

## Pessimistic Scenario

Represents an extended delay or continued uncertainty.

## Expected Scenario

Represents the most likely outcome based on the current financial model.

## Optimistic Scenario

Represents an improvement in the payment situation.

```text
Financial Position

        │
        │                         Optimistic
        │                       /
Balance │                 Expected
        │                 /
        │          Pessimistic
        │
        └─────────────────────────────────
             Day 1                 Day 30
```

---

# Risk Engine

The risk engine evaluates the financial impact of the current state.

The current risk model considers:

```text
Financial Risk
│
├── Liquidity Risk
│
├── Income Certainty Risk
│
├── Obligation Risk
│
└── Emergency Buffer Risk
```

These risks are recalculated when a financial event changes the underlying financial state.

---

# Recommendation Engine

The recommendation engine compares possible actions.

Current alternatives include:

```text
DO_NOTHING
PAUSE_SIP
REDUCE_DISCRETIONARY_SPENDING
```

Each alternative is evaluated against:

- Projected minimum balance
- Financial obligation safety
- Emergency buffer impact
- Long-term financial impact
- Overall decision score

The backend returns a structured recommendation containing:

```text
Recommendation
│
├── Recommended Action
│
├── Explanation
│
├── Confidence
│
├── Identified Risks
│
├── Alternative Actions
│
└── Trade-offs
```

---

# API Architecture

```text
                         FRONTEND

                            │
                            │ REST API
                            ▼

                    ┌───────────────┐
                    │    FastAPI    │
                    └───────┬───────┘
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼

      STATE API         EVENT API       SIMULATION API

          │                 │                 │
          └─────────────────┼─────────────────┘
                            │
                            ▼

                      SERVICE LAYER

                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼

        STATE STORE    FINANCIAL      DEMO DATA
                       ENGINE

                            │
                            ▼

                    DECISION OUTPUT
```

---

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/state` | Returns the current financial state |
| `GET` | `/events` | Returns the financial event history |
| `POST` | `/simulate/PAYMENT_DELAYED` | Simulates a delayed payment event |
| `GET` | `/simulation` | Returns the active simulation and projections |
| `POST` | `/simulation/reset` | Restores the baseline financial state |
| `GET` | `/risks` | Returns the current financial risk analysis |
| `GET` | `/recommendation` | Returns the recommendation and alternatives |

---

# Backend Structure

```text
backend/
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── models/
│   │   └── Financial data models
│   │
│   ├── routers/
│   │   ├── state.py
│   │   ├── events.py
│   │   ├── simulation.py
│   │   ├── risks.py
│   │   └── recommendation.py
│   │
│   └── services/
│       ├── state_store.py
│       ├── financial_engine.py
│       └── demo_data.py
│
├── tests/
│
├── requirements.txt
│
├── run.py
│
└── README.md
```

---

# Running the Backend

## 1. Navigate to the Backend Directory

```bash
cd backend
```

## 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

## 3. Start the Server

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8765 --reload
```

The backend will start on:

```text
http://127.0.0.1:8765
```

---

# API Documentation

FastAPI automatically provides interactive API documentation.

Once the server is running, open:

```text
http://127.0.0.1:8765/docs
```

This interface can be used to inspect and test the available API endpoints.

---

# Example Request Flow

```text
POST /simulate/PAYMENT_DELAYED
              │
              ▼
      Validate Event Type
              │
              ▼
       Update State
              │
              ▼
     Create Event Record
              │
              ▼
       Recalculate Risks
              │
              ▼
      Generate Projections
              │
              ▼
     Evaluate Alternatives
              │
              ▼
    Generate Recommendation
              │
              ▼
      Return JSON Response
```

---

# Current Implementation

The backend currently supports:

- Financial state management
- Event tracking
- Payment delay simulation
- Income certainty modeling
- Financial risk analysis
- Deterministic scenario generation
- 30-day financial projections
- Alternative action comparison
- Structured recommendation generation
- REST API integration

---

# Future Development

Potential extensions include:

- Persistent database storage
- Multi-user financial profiles
- Authentication and authorization
- Real-time event processing
- Webhook integration
- n8n workflow automation
- AI-assisted explanation generation
- Notification services
- Banking data integration
- Cloud deployment

---

# Disclaimer

This backend is part of a hackathon prototype developed for demonstration and educational purposes.

The system is intended to provide financial decision support and does not constitute professional financial, investment, legal, or tax advice.
