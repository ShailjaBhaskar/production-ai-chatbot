# Production AI Chatbot

Production-ready AI chatbot using:

- FastAPI
- LangChain
- RAG
- ChromaDB
- OpenAI
- Conversational Memory
- LangGraph

## Features

- Retrieval-Augmented Generation (RAG)
- Conversational memory
- Vector database search
- FastAPI backend
- Modular architecture
- Production-ready structure

## Tech Stack

- Python
- FastAPI
- LangChain
- ChromaDB
- OpenAI API
- LangGraph

## Setup

### Clone Repository

```bash
git clone <repo-url>
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

```bash
.venv\Scripts\activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Add Environment Variables

Create `.env`

```env
OPENAI_API_KEY=your_key
```

### Run FastAPI

```bash
uvicorn app.api:app --reload
```

## API Docs

```text
http://127.0.0.1:8000/docs
```