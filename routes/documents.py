from fastapi import APIRouter, Depends, HTTPException
from models.request_models import DocumentRequest
from chroma_connection import get_chroma_collection
from chromadb.api.models.Collection import Collection

router = APIRouter(prefix="/api/documents", tags=["Documents"])

@router.post("/")
async def add_documents(request: DocumentRequest, col: Collection = Depends(get_chroma_collection)):
    try:
        col.add(
            ids=request.ids,
            documents=request.documents,
            metadatas=request.metadatas
        )
        return {"message": "Documents added successfully", "ids": request.ids}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
