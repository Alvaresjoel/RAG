import os
from fastapi import HTTPException
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROK_API_KEY"))

def call_grok(context: str, question: str) -> str:
    """
    Call Groq API (LLama model) to generate a response using retrieved context
    """
    if not os.getenv("GROK_API_KEY"):
        raise HTTPException(status_code=500, detail="GROK_API_KEY not configured")

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant. Answer questions based only on the provided context."
                },
                {
                    "role": "user",
                    "content": f"Context: {context}\n\nQuestion: {question}"
                }
            ],
            model="llama-3.3-70b-versatile",  # ✅ You can swap to another Groq-supported model
            max_tokens=500,
            temperature=0.7
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calling Groq API: {str(e)}")
