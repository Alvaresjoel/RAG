from fastapi import APIRouter, Depends, HTTPException
from models.request_models import AskRequest
from chroma_connection import get_chroma_collection
from chromadb.api.models.Collection import Collection
from sentence_transformers import SentenceTransformer
from llm import call_grok

router = APIRouter(prefix="/api/ask", tags=["Ask"])

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

@router.post("/")
async def ask_question(request: AskRequest, col: Collection = Depends(get_chroma_collection)):
    try:
        query_embedding = embedding_model.encode([request.question]).tolist()

        results = col.query(
            query_embeddings=query_embedding,
            n_results=request.top_k,
            include=["documents", "metadatas"]
        )

        if not results["documents"] or not results["documents"][0]:
            return {"answer": "No relevant documents found.", "question": request.question}

        docs_text = "\n\n".join(results["documents"][0])

        answer = call_grok(docs_text, request.question)

        return {
            "question": request.question,
            "answer": answer,
            "sources": results["metadatas"][0]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
