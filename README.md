# HR Resource Query Chatbot

An AI-powered chatbot that helps HR teams find suitable employees by answering natural language queries using advanced RAG (Retrieval Augmented Generation) system.

## Overview
This project implements an intelligent HR assistant that can process natural language queries to find relevant employees based on their skills, experience, and project history. It uses modern AI/ML techniques including embeddings, vector search, and language models for accurate and context-aware responses.

## Features
- Natural language query processing
- Advanced employee search using RAG system
- Real-time response generation
- Clean and intuitive chat interface
- Employee data management
- Vector similarity search
- Contextual response generation

## Architecture
The system consists of three main components:
1. **Data Layer**: Employee database with vector embeddings
2. **RAG System**: Query processing pipeline with Retrieval, Augmentation, and Generation
3. **API Layer**: FastAPI backend with Streamlit frontend

## Setup & Installation

### Prerequisites
- Python 3.9+
- pip (Python package manager)

### Local Setup
1. Clone the repository
```bash
git clone <repository-url>
cd hr-resource-chatbot
```

2. Create and activate virtual environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
# Start the FastAPI backend
uvicorn app.main:app --reload

# In a new terminal, start the Streamlit frontend
streamlit run frontend/app.py
```

## API Documentation
### Endpoints
- POST /chat - Process chat queries
- GET /employees/search - Search employees based on criteria

## Technical Stack
- Backend: FastAPI
- Frontend: Streamlit
- ML/AI: sentence-transformers, FAISS, HuggingFace Transformers
- Database: JSON (for demo), can be extended to any database

## Future Improvements
- Integration with real HR databases
- Advanced filtering options
- Performance optimizations
- Multi-language support
- Enhanced security features

## Demo
[Demo link will be added here] 