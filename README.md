# 📘 RAG Application with ChromaDB + Groq LLM

This project is a **Retrieval-Augmented Generation (RAG) system** built with **FastAPI**, **ChromaDB Cloud**, and **Groq LLM (Llama-3.3-70B-Versatile)**.  

It allows you to:  
1. **Store documents** in ChromaDB Cloud.  
2. **Retrieve relevant chunks** based on user queries.  
3. **Ask natural language questions** and get answers powered by Groq LLM, grounded in your stored knowledge base.  

---

## ⚙️ Tech Stack
- **Backend Framework**: FastAPI  
- **Vector Database**: ChromaDB Cloud  
- **Embeddings Model**: `sentence-transformers/all-MiniLM-L6-v2`  
- **LLM**: Groq (Llama-3.3-70B-Versatile)  
- **Environment Management**: Python + `.env`  

---

## 📂 Project Structure



rag_app/
├── main.py # FastAPI entrypoint
├── chroma_connection.py # Connects to ChromaDB Cloud
├── llm.py # Groq LLM wrapper
├── routes/
│ ├── documents.py # /api/documents → add docs
│ ├── query.py # /api/query → retrieve docs
│ └── ask.py # /api/ask → full RAG pipeline
├── models/
│ ├── request_models.py # Pydantic request schemas
├── docs/ # Folder to store raw text files (optional)
├── requirements.txt # Python dependencies
├── .env.example # Example environment config
└── README.md # Documentation




---

## 🔑 Environment Variables
Create a `.env` file in the root:

```env
# ChromaDB Cloud
CHROMA_API_KEY=your_chroma_api_key
CHROMA_TENANT=your_chroma_tenant
CHROMA_DATABASE=your_chroma_database

# Groq API
GROQ_API_KEY=your_groq_api_key



git clone <your-repo-url>
cd rag_app
pip install -r requirements.txt
pip install sentence-transformers groq python-dotenv fastapi uvicorn chromadb
uvicorn main:app --reload --port 8000



# POST /api/documents/
``` python

  {
    "ids": ["policy_1"],
    "documents": ["Employees get 2 wellness days per month at Acme Corp."],
    "metadatas": [{"source": "company_policies.txt"}]
  }
  Response
  {
  "message": "Documents added successfully",
  "ids": ["policy_1"]
}

```


# POST /api/query/
``` python
Request:

{
  "question": "How many wellness days do employees get?",
  "top_k": 3
}


Response (from ChromaDB):

{
  "results": {
    "documents": [["Employees get 2 wellness days per month at Acme Corp."]],
    "metadatas": [[{"source": "company_policies.txt"}]]
  }
}
``` python
3. Ask Question (RAG)

# POST /api/ask/

Request:

{
  "question": "How many wellness days per month do employees get at Acme Corp?",
  "top_k": 3
}


Response (Groq LLM):

{
  "question": "How many wellness days per month do employees get at Acme Corp?",
  "answer": "Employees at Acme Corp are allowed two wellness days per month in addition to regular vacation days.",
  "sources": [{"source": "company_policies.txt"}]
}