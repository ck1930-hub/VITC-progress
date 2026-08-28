from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import state, events, simulation, risks, recommendation

app = FastAPI(
    title="Financial AI Backend API",
    description=(
        "Deterministic financial engine exposing REST endpoints for "
        "financial state management, scenario stress-testing, risk analysis, "
        "and automated financial recommendations."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS: allow your frontend laptop on the same Wi-Fi network
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001",
        "http://192.168.1.30:3000",  # replace with frontend laptop IP
        "http://192.168.1.30:3001",  # replace with frontend laptop IP
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(state.router)
app.include_router(events.router)
app.include_router(simulation.router)
app.include_router(risks.router)
app.include_router(recommendation.router)


@app.get("/", summary="Root / Health Check", tags=["Health Check"])
def root():
    return {
        "status": "online",
        "service": "Financial AI Backend API",
        "version": "1.0.0",
        "documentation": "/docs",
        "endpoints": [
            "GET /state",
            "GET /events",
            "POST /simulate/{event_type}",
            "GET /simulation",
            "GET /risks",
            "GET /recommendation",
        ],
    }