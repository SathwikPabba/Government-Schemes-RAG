# api/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import sqlite3
from datetime import datetime
from api.models import QueryRequest, QueryResponse, SchemeSource, HealthResponse
from src.pipeline import GovernmentSchemeRAG

rag_pipeline = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global rag_pipeline
    print("🚀 Starting Government Scheme RAG API...")
    rag_pipeline = GovernmentSchemeRAG()
    setup_database()
    print("✅ API ready!")
    yield
    print("Shutting down...")


app = FastAPI(
    title="Government Scheme RAG API",
    description="AI-powered Q&A system for Indian Government Schemes",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def setup_database():
    conn = sqlite3.connect("queries.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS query_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            num_sources INTEGER,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()


def log_query(question: str, answer: str, num_sources: int):
    conn = sqlite3.connect("queries.db")
    conn.execute(
        "INSERT INTO query_logs (question, answer, num_sources, timestamp) VALUES (?,?,?,?)",
        (question, answer, num_sources, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()


@app.get("/health", response_model=HealthResponse, tags=["System"])
async def health_check():
    schemes = rag_pipeline.get_all_schemes() if rag_pipeline else []
    return HealthResponse(
        status="healthy" if rag_pipeline else "not ready",
        total_schemes=len(schemes),
        vector_db_ready=rag_pipeline is not None
    )


@app.post("/query", response_model=QueryResponse, tags=["RAG"])
async def query_schemes(request: QueryRequest):
    if not rag_pipeline:
        raise HTTPException(status_code=503, detail="RAG pipeline not ready")

    result = rag_pipeline.query(request.question)

    log_query(request.question, result.answer, result.num_sources)

    sources = [
        SchemeSource(
            scheme_name=s.get("scheme_name", "Unknown"),
            ministry=s.get("ministry", "N/A"),
            category=s.get("category", "N/A"),
            preview=s.get("preview", "")
        )
        for s in result.sources[:request.max_sources]
    ]

    return QueryResponse(
        question=result.question,
        answer=result.answer,
        sources=sources,
        num_sources=result.num_sources
    )


@app.get("/schemes", tags=["Schemes"])
async def list_all_schemes():
    if not rag_pipeline:
        raise HTTPException(status_code=503, detail="Pipeline not ready")
    schemes = rag_pipeline.get_all_schemes()
    return {"total": len(schemes), "schemes": schemes}