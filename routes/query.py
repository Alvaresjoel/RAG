from fastapi import APIRouter, Depends, HTTPException
from models.request_models import QueryRequest
from chroma_connection import get_chroma_collection
from chromadb.api.models.Collection import Collection
from sentence_transformers import SentenceTransformer

router = APIRouter(prefix="/api/query", tags=["Query"])

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

@router.post("/")
async def query_documents(request: QueryRequest, col: Collection = Depends(get_chroma_collection)):
    try:
        query_embedding = embedding_model.encode([request.question]).tolist()
        results = col.query(
            query_embeddings=query_embedding,
            n_results=request.top_k,
            include=["documents", "metadatas"]
        )
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
