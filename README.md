\# 🏛️ Government Scheme RAG System



An AI-powered question-answering system for Indian Government Schemes built with RAG (Retrieval Augmented Generation).



🌐 \*\*Live Demo\*\*: https://government-schemes-rag.vercel.app



\## 🚀 Features

\- Ask questions about 36 Indian Government Schemes in plain English

\- Instant AI-powered answers using Groq LLaMA 3.1

\- Browse and filter schemes by category

\- Beautiful dark theme React frontend

\- REST API with FastAPI backend



\## 🛠️ Tech Stack



| Layer | Technology |

|-------|-----------|

| Frontend | React + Vite (Vercel) |

| Backend | FastAPI + Uvicorn (Render) |

| LLM | Groq LLaMA 3.1 (free) |

| RAG Framework | LangChain LCEL |

| Vector DB | ChromaDB |

| Embeddings | all-MiniLM-L6-v2 (local) |



\## 📚 Schemes Covered

Agriculture, Health, Housing, Finance, Education, Employment, Insurance, Entrepreneurship, Pension, Digital, Women \& Child, Sanitation, Food Security and more.



\## 🏗️ Project Structure

```

government-scheme-rag/

├── src/              # Core RAG pipeline

│   ├── scraper.py    # 36 scheme data files

│   ├── ingest.py     # Document loading

│   ├── embeddings.py # Sentence transformers

│   ├── vectorstore.py# ChromaDB vector store

│   ├── llm.py        # Groq LLaMA integration

│   └── pipeline.py   # RAG chain

├── api/              # FastAPI backend

│   ├── main.py       # API endpoints

│   └── models.py     # Pydantic models

├── frontend/         # Streamlit UI

├── react-frontend/   # React UI

└── data/             # Scheme text files

```



\## ⚙️ Run Locally

```bash

\# Clone repo

git clone https://github.com/SathwikPabba/Government-Schemes-RAG.git

cd Government-Schemes-RAG



\# Setup environment

python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt



\# Add your Groq API key

echo GROQ\_API\_KEY=your\_key > .env



\# Start API

uvicorn api.main:app --reload --port 8000



\# Start React (new terminal)

cd react-frontend

npm install

npm run dev

```



\## 👨‍💻 Author

\*\*Sathwik Pabba\*\* - Final Year Project

