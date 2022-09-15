from pydantic import BaseModel
from typing import (List)

class QueryFilter(BaseModel):
    id: str
    operator: str
    value: str

class ResponseSummary(BaseModel):
    numTotalResults: int
    exists: bool

class Response(BaseModel):
    responseSummary: ResponseSummary

class Meta(BaseModel):
    apiVersion: str

class Query(BaseModel):
    filters: List[QueryFilter] = None

class Request(BaseModel):
    meta: Meta
    query: Query