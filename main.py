from fastapi import FastAPI
from routes import documents, query, ask

app = FastAPI(title="RAG Application with ChromaDB + Grok")

# Register routes
app.include_router(documents.router)
app.include_router(query.router)
app.include_router(ask.router)

@app.get("/")
async def root():
    return {"message": "RAG App is running"}
