from pydantic import BaseModel
from typing import List, Dict, Optional

class DocumentRequest(BaseModel):
    ids: List[str]
    documents: List[str]
    metadatas: List[Dict]

class QueryRequest(BaseModel):
    question: str
    top_k: Optional[int] = 3

class AskRequest(BaseModel):
    question: str
    top_k: Optional[int] = 3
