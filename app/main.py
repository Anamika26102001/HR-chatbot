from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models.employee import EmployeeQuery, EmployeeResponse
from app.core.rag_system import RAGSystem

app = FastAPI(title="HR Resource Query Chatbot")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG system
rag_system = RAGSystem()

@app.post("/chat", response_model=EmployeeResponse)
async def process_chat(query: EmployeeQuery):
    """
    Process a natural language query and return relevant employees
    """
    try:
        result = rag_system.process_query(query.query)
        return EmployeeResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    """
    Root endpoint - health check
    """
    return {"status": "ok", "message": "HR Resource Query Chatbot is running"} 