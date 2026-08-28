# Financial AI Command Center

## Intelligent Financial Decision Support Under Uncertainty

Financial AI Command Center is a full-stack financial decision-support prototype designed to help individuals with uncertain income, recurring financial obligations, and changing financial circumstances understand the potential consequences of financial events before making decisions.

Unlike traditional financial dashboards that primarily display balances and transaction history, the system models uncertainty, simulates financial events, evaluates financial risks, projects possible outcomes, and compares alternative actions.

The objective is to move from passive financial tracking toward proactive financial decision support.

---

# Problem Statement

Traditional financial applications can show users how much money they currently have, but financial decision-making often requires a deeper understanding of uncertainty.

Individuals with variable or uncertain income may face situations involving:

- Delayed payments
- Irregular income
- Fixed recurring obligations
- Loan or EMI commitments
- Insurance payments
- Investment commitments
- Unexpected expenses
- Insufficient emergency reserves

A current bank balance alone does not provide enough information to determine whether a financial decision is safe.

The more important question is:

> Given the current financial state, upcoming obligations, and uncertainty surrounding future income, what action should be taken?

Financial AI Command Center addresses this problem through financial state modeling, event simulation, risk analysis, scenario projection, and structured recommendation generation.

---

# Solution Overview

The system maintains a financial state consisting of confirmed facts, uncertain financial information, recurring obligations, emergency reserves, and risk preferences.

When a financial event occurs, the system:

1. Updates the relevant financial state.
2. Represents changes in certainty or payment timing.
3. Recalculates the financial impact.
4. Identifies potential financial risks.
5. Generates deterministic future projections.
6. Compares possible financial actions.
7. Produces a structured recommendation.

The overall decision flow is:

```text
Financial State
      |
      v
Financial Event
      |
      v
State and Certainty Update
      |
      v
Risk Analysis
      |
      v
30-Day Scenario Projection
      |
      v
Alternative Evaluation
      |
      v
Recommended Action
```

---

# Core Use Case

The current prototype models a variable-income individual with recurring financial obligations.

## Baseline Financial State

| Financial Component | Value |
|---|---:|
| Confirmed Bank Balance | ₹32,000 |
| Expected Income | ₹22,000 |
| Payment Confidence | 78% |
| Rent | ₹15,000 |
| EMI | ₹6,000 |
| Insurance | ₹2,500 |
| SIP | ₹5,000 |
| Emergency Buffer Target | ₹15,000 |
| Risk Tolerance | Conservative |

The system explicitly distinguishes between confirmed financial information and uncertain financial information.

```text
Confirmed Balance != Expected Income
```

This distinction is important when evaluating liquidity and financial safety.

---

# Event Simulation

The current prototype supports financial event simulation.

## Payment Delayed

A delayed payment triggers changes to the financial model.

```text
Expected Payment
       |
       v
Payment Delay Detected
       |
       v
Payment Timing Becomes Uncertain
       |
       v
Income Certainty Changes
       |
       v
Risk Profile Recalculated
       |
       v
Financial Alternatives Evaluated
       |
       v
Recommendation Generated
```

The objective is not simply to record that an event occurred, but to evaluate its consequences across the user's financial position.

---

# Financial Health Assessment

The dashboard presents multiple indicators representing different aspects of financial stability.

These include:

- Liquidity
- Income Certainty
- Obligation Safety
- Emergency Buffer
- Overall Financial Health

These indicators provide a structured representation of the user's financial position rather than relying solely on a single account balance.

---

# Financial Risk Analysis

The system evaluates multiple dimensions of financial risk, including:

- Liquidity Risk
- Income Certainty Risk
- Obligation Risk
- Emergency Buffer Risk

Risk evaluation considers the relationship between available financial resources, expected income, recurring obligations, emergency reserves, and uncertainty.

---

# 30-Day Scenario Projection

The system generates deterministic 30-day financial projections based on different scenarios.

## Pessimistic Scenario

Represents continued uncertainty or an extended delay in expected income.

## Expected Scenario

Represents the most likely outcome based on the current financial model.

## Optimistic Scenario

Represents an improvement in the payment or income situation.

```text
Financial Position

        |
        |                         Optimistic
        |                       /
Balance |                 Expected
        |                 /
        |          Pessimistic
        |
        +--------------------------------
             Day 1                 Day 30
```

The purpose of scenario projection is to help users understand possible future outcomes instead of assuming that a single future outcome is guaranteed.

---

# Decision Engine

When a financial disruption occurs, the system evaluates multiple possible actions.

## DO_NOTHING

Continue the existing financial plan without intervention.

## PAUSE_SIP

Temporarily pause the current SIP contribution in order to preserve short-term liquidity.

## REDUCE_DISCRETIONARY_SPENDING

Reduce non-essential expenditure to improve the available financial buffer.

Each alternative is evaluated using factors such as:

- Projected minimum balance
- Obligation safety
- Emergency buffer impact
- Long-term goal impact
- Overall decision score
- Associated trade-offs

The system selects the alternative with the strongest balance between immediate financial safety and long-term financial impact.

---

# Recommendation Engine

The recommendation engine provides structured and interpretable output.

Each recommendation includes:

- Current financial situation
- What changed
- Identified risks
- Competing financial priorities
- Available alternatives
- Recommended action
- Reasoning
- Confidence
- Uncertainties
- Intervention level

This structure allows recommendations to remain explainable rather than functioning as an unexplained black-box output.

---

# System Architecture

The system is organized into customer, application, financial intelligence, automation, and administration layers.

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│                              SYSTEM OVERVIEW                                 │
│                                                                              │
│                    FINANCIAL AI COMMAND CENTER                              │
└──────────────────────────────────────────────────────────────────────────────┘


                               CUSTOMER LAYER
════════════════════════════════════════════════════════════════════════════════

      ┌────────────────┐       ┌────────────────┐       ┌────────────────┐
      │   CUSTOMER 1   │       │   CUSTOMER 2   │       │   CUSTOMER 3   │
      │                │       │                │       │                │
      │  Mobile Device │       │  Mobile Device │       │  Mobile Device │
      │                │       │                │       │                │
      │ Financial App  │       │ Financial App  │       │ Financial App  │
      └───────┬────────┘       └───────┬────────┘       └───────┬────────┘
              │                        │                        │
              └────────────────────────┼────────────────────────┘
                                       │
                                       │ HTTP / REST
                                       ▼


                         APPLICATION AND API LAYER
════════════════════════════════════════════════════════════════════════════════

                   ┌──────────────────────────────────┐
                   │        APPLICATION SERVER        │
                   │                                  │
                   │          Next.js Frontend        │
                   │                                  │
                   │  Financial Dashboard             │
                   │  Financial Health Score          │
                   │  Cash Flow Visualization         │
                   │  Risk Visualization              │
                   │  30-Day Projections              │
                   │  Decision Lab                    │
                   │  Recommendations                 │
                   │                 │                │
                   │                 │ API Calls      │
                   │                 ▼                │
                   │  ┌────────────────────────────┐  │
                   │  │      FastAPI Backend       │  │
                   │  │                            │  │
                   │  │ Financial API              │  │
                   │  │ State Management           │  │
                   │  │ Event Processing           │  │
                   │  │ Simulation API             │  │
                   │  │ Risk API                   │  │
                   │  │ Recommendation API         │  │
                   │  └──────────────┬─────────────┘  │
                   └─────────────────┼────────────────┘
                                     │
                                     ▼


                         FINANCIAL INTELLIGENCE LAYER
════════════════════════════════════════════════════════════════════════════════

        ┌────────────────────────────────────────────────────────────┐
        │                  FINANCIAL STATE STORE                     │
        │                                                            │
        │  Confirmed Balance                                         │
        │  Expected Income                                           │
        │  Payment Timing                                            │
        │  Financial Obligations                                     │
        │  Emergency Buffer                                          │
        │  Risk Tolerance                                            │
        │  Event History                                             │
        └───────────────────────────┬────────────────────────────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼

     ┌─────────────────┐   ┌─────────────────┐   ┌──────────────────┐
     │ EVENT ENGINE    │   │ FINANCIAL       │   │ RISK ENGINE      │
     │                 │   │ SIMULATION      │   │                  │
     │ PAYMENT_DELAYED │   │ ENGINE          │   │ Liquidity Risk   │
     │ Income Changes  │   │                 │   │ Income Risk      │
     │ Expense Events  │   │ 30-Day Model    │   │ Obligation Risk  │
     │ State Updates   │   │                 │   │ Emergency Buffer │
     │                 │   │ Pessimistic     │   │ Risk             │
     │                 │   │ Expected        │   │                  │
     │                 │   │ Optimistic      │   │                  │
     └────────┬────────┘   └────────┬────────┘   └─────────┬────────┘
              │                     │                      │
              └─────────────────────┼──────────────────────┘
                                    │
                                    ▼

                     ┌─────────────────────────────┐
                     │    RECOMMENDATION ENGINE    │
                     │                             │
                     │ Evaluates Alternatives:     │
                     │                             │
                     │ DO_NOTHING                  │
                     │ PAUSE_SIP                   │
                     │ REDUCE_DISCRETIONARY        │
                     │ SPENDING                    │
                     │                             │
                     │ Evaluates:                  │
                     │                             │
                     │ Minimum Balance             │
                     │ Obligation Safety           │
                     │ Emergency Buffer Impact     │
                     │ Goal Impact                 │
                     │ Overall Score               │
                     │                             │
                     │ Produces:                   │
                     │ Recommended Action          │
                     │ Reasoning                   │
                     │ Confidence                  │
                     │ Trade-offs                  │
                     └──────────────┬──────────────┘
                                    │
                                    │ Financial Event
                                    │ or High-Risk Trigger
                                    ▼


                    AUTOMATION AND WORKFLOW LAYER
                         PLANNED / IN PROGRESS
════════════════════════════════════════════════════════════════════════════════

                    ┌─────────────────────────────────┐
                    │              n8n                │
                    │                                 │
                    │  Workflow Automation Layer      │
                    │                                 │
                    │  Webhook Trigger                │
                    │          │                      │
                    │          ▼                      │
                    │  Financial Event Received       │
                    │          │                      │
                    │          ▼                      │
                    │  Workflow / Risk Processing     │
                    │          │                      │
                    │          ▼                      │
                    │  AI-Assisted Analysis           │
                    │          │                      │
                    │          ▼                      │
                    │  Alert Generation               │
                    └───────────────┬─────────────────┘
                                    │
                     ┌──────────────┴──────────────┐
                     │                             │
                     ▼                             ▼

                CUSTOMER UPDATE                ADMIN ALERT
                     │                             │
                     │                             │
                     ▼                             ▼


                          ADMINISTRATION LAYER
                            PLANNED / IN PROGRESS
════════════════════════════════════════════════════════════════════════════════

                    ┌─────────────────────────────────┐
                    │          ADMIN SYSTEM           │
                    │                                 │
                    │  Customer Monitoring            │
                    │                                 │
                    │  Customer Financial State       │
                    │  Financial Health Score         │
                    │  Active Financial Events        │
                    │  Detected Risks                 │
                    │  Workflow Alerts                │
                    │  Recommended Intervention       │
                    │                                 │
                    │  Alert and Monitoring View      │
                    └─────────────────────────────────┘
```

---

# Architecture Flow

The end-to-end flow of the system is:

```text
Customer Device
      |
      v
Next.js Financial Dashboard
      |
      | REST API
      v
FastAPI Backend
      |
      +-----------------------------+
      |                             |
      v                             v
Financial State                Event Processing
      |                             |
      +-------------+---------------+
                    |
                    v
          Financial Intelligence
                    |
      +-------------+-------------+
      |             |             |
      v             v             v
Simulation      Risk Engine   Recommendation
Engine
      |             |             |
      +-------------+-------------+
                    |
                    v
             Financial Decision
                    |
                    v
             Updated Dashboard
                    |
                    |
          Future Integration
                    |
                    v
                 n8n Workflow
                    |
                    +-------------+
                    |             |
                    v             v
             Customer Update   Admin Alert
```

---

# Multi-Device Demonstration Architecture

The proposed physical demonstration environment uses multiple devices to represent different actors in the financial ecosystem.

```text
                         SAME LOCAL NETWORK

   ┌──────────────┐
   │   PHONE 1    │
   │              │
   │  Customer A  │
   └──────┬───────┘
          │

   ┌──────────────┐
   │   PHONE 2    │
   │              │
   │  Customer B  │
   └──────┬───────┘
          │
          ├─────────────────────────────┐
          │                             │
   ┌──────┴───────┐                     │
   │   PHONE 3    │                     │
   │              │                     │
   │  Customer C  │                     │
   └──────┬───────┘                     │
          │                             │
          │                             ▼
          │              ┌──────────────────────────┐
          │              │      MAIN LAPTOP         │
          │              │                          │
          └─────────────►│  Next.js Frontend        │
                         │            +             │
                         │  FastAPI Backend          │
                         │            +             │
                         │  Financial Intelligence   │
                         └─────────────┬────────────┘
                                       │
                                       │ Event Trigger
                                       ▼
                         ┌──────────────────────────┐
                         │      n8n LAPTOP          │
                         │                          │
                         │ Workflow Automation      │
                         │ Webhook Processing       │
                         │ Alert Generation         │
                         │ AI Integration           │
                         └─────────────┬────────────┘
                                       │
                                       │ Alerts / Events
                                       ▼
                         ┌──────────────────────────┐
                         │      ADMIN LAPTOP        │
                         │                          │
                         │ Customer Monitoring      │
                         │ Financial Risk Alerts    │
                         │ Intervention Overview    │
                         └──────────────────────────┘
```

---

# Repository Structure

```text
FinancialAI/
|
|-- frontend/
|   |
|   |-- src/
|   |   |-- app/
|   |   |-- components/
|   |   `-- services/
|   |
|   |-- public/
|   |-- package.json
|   |-- tsconfig.json
|   `-- ...
|
|-- backend/
|   |
|   |-- app/
|   |   |
|   |   |-- models/
|   |   |
|   |   |-- routers/
|   |   |   |-- state.py
|   |   |   |-- events.py
|   |   |   |-- simulation.py
|   |   |   |-- risks.py
|   |   |   `-- recommendation.py
|   |   |
|   |   |-- services/
|   |   |   |-- demo_data.py
|   |   |   |-- financial_engine.py
|   |   |   `-- state_store.py
|   |   |
|   |   `-- main.py
|   |
|   |-- tests/
|   |-- requirements.txt
|   `-- run.py
|
`-- README.md
```

---

# Technology Stack

## Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS
- Framer Motion
- Recharts

## Backend

- Python
- FastAPI
- Pydantic
- Uvicorn

## Workflow Automation

- n8n (planned/in-progress integration)

---

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/state` | Returns the current financial state |
| GET | `/events` | Returns the financial event trail |
| POST | `/simulate/PAYMENT_DELAYED` | Simulates a delayed payment event |
| GET | `/simulation` | Returns the active simulation and projections |
| POST | `/simulation/reset` | Restores the baseline financial state |
| GET | `/risks` | Returns the current financial risk analysis |
| GET | `/recommendation` | Returns alternatives and the recommended action |

---

# Running the Project

## Prerequisites

Ensure the following are installed:

- Python
- Node.js
- npm

## Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the backend:

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8765 --reload
```

The API will be available at:

```text
http://127.0.0.1:8765
```

Interactive API documentation:

```text
http://127.0.0.1:8765/docs
```

## Frontend Setup

Open a separate terminal and navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Create a `.env.local` file:

```env
NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8765
```

Start the frontend:

```bash
npm run dev
```

Open the URL displayed by the Next.js development server.

---

# Demonstration Flow

The current demonstration follows this sequence:

```text
Initial Financial State
        |
        v
Payment Delay Event
        |
        v
Income Certainty Changes
        |
        v
Payment Timing Becomes Uncertain
        |
        v
Financial Risks Are Recalculated
        |
        v
30-Day Scenarios Are Generated
        |
        v
Alternative Actions Are Compared
        |
        v
Recommended Intervention Is Presented
```

---

# Current Implementation

The current implementation includes:

- Financial state management
- Confirmed and uncertain financial information
- Payment delay simulation
- Event tracking
- Risk analysis
- Deterministic 30-day scenario projections
- Recommendation alternatives
- Structured recommendation generation
- Financial health visualization
- Interactive frontend dashboard
- FastAPI backend
- Frontend and backend API integration

---

# Future Development

Planned extensions include:

- n8n workflow automation
- AI-assisted financial explanations
- Multi-user customer simulation
- Administrator dashboard
- Real-time event alerts
- Persistent database storage
- Banking and financial data integrations
- Personalized financial models
- Cloud deployment

---

# Key Design Principle

Traditional financial dashboards answer:

> What is my current financial position?

Financial AI Command Center is designed to additionally answer:

> What could happen next, what risks does that create, and what action best balances immediate financial safety with long-term financial objectives?

The system combines:

```text
Financial Facts
        +
Uncertainty
        +
Event Simulation
        +
Risk Analysis
        +
Scenario Projection
        +
Alternative Comparison
        +
Explainable Recommendations
        =
Financial Decision Support
```

---

# Disclaimer

This project is a hackathon prototype intended for demonstration and educational purposes.

The system is designed as a financial decision-support tool and does not provide professional financial, investment, legal, or tax advice.

---

# Project Status

The core financial simulation and decision-support system is operational.

Current development is focused on extending the prototype with workflow automation, multi-device interaction, and administrative monitoring capabilities.
