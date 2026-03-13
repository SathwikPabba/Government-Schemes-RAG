# api/models.py

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class QueryRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=5,
        max_length=500,
        description="The question about government schemes",
        example="Who is eligible for PM-KISAN scheme?"
    )
    max_sources: int = Field(
        default=3,
        ge=1,
        le=10,
        description="Number of source documents to return"
    )


class SchemeSource(BaseModel):
    scheme_name: str
    ministry: str
    category: str
    preview: str


class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: list[SchemeSource]
    num_sources: int
    timestamp: datetime = Field(default_factory=datetime.now)


class HealthResponse(BaseModel):
    status: str
    total_schemes: int
    vector_db_ready: bool