**Clinical RAG Assistant: LLaMA-Based Medical Query System**

A sophisticated Retrieval-Augmented Generation (RAG) architecture designed for domain-grounded medical query support. This project, developed as a TCS Internal Initiative, focuses on high-precision retrieval, medical safety guardrails, and deterministic evaluation frameworks.
🚀 Key Features

    Domain-Grounded Retrieval: Utilizes a custom FAISS vector index with SentenceTransformers for high-accuracy semantic search over clinical documentation.

    Safety & Escalation Layer: Integrated logic to detect high-risk symptoms and enforce emergency disclaimers—essential for regulated-domain AI.

    Production-Style ETL: Implements recursive character splitting with controlled overlap to maintain context window integrity.

    Infrastructure Abstraction: Centralized configuration management for seamless environment switching and model parameterization.

    Interactive UI: A Streamlit-based interface providing a clean, professional entry point for clinical researchers and practitioners.

🛠️ Technical Stack
Component	Technology
LLM Backend	LLaMA (via Ollama)
Embeddings	SentenceTransformers
Vector Database	FAISS (with metadata persistence)
Orchestration	LangChain / Python
Frontend	Streamlit
Data Formats	PDF, TXT
📂 Project Structure
Bash

├── config.py           # Environment abstraction & model hyper-parameters
├── ingest.py           # Document ETL: PDF/TXT ingestion & recursive chunking
├── embed_index.py      # Vector embedding generation & FAISS index management
├── rag_pipeline.py     # RAG logic: Context assembly & Ollama integration
├── safety.py           # Guardrails, escalation logic, & disclaimer enforcement
├── evaluation.py       # Framework for deterministic system validation
└── ui_streamlit.py     # Streamlit-based interactive user interface

⚙️ Implementation Details
1. Document Ingestion & Chunking

The pipeline utilizes a Recursive Character Text Splitter with a strategy designed for medical density:

    Chunk Size: 800 tokens

    Chunk Overlap: 150 tokens
    This ensures that clinical nuances are not lost across split boundaries.

2. Vector Indexing

Unlike "black-box" vector database implementations, this system features a manual FAISS index management layer. By persisting metadata locally, the system ensures full control over the retrieval layer without relying on expensive managed services.
3. Safety Guardrails

In a clinical context, "hallucination" can be dangerous. The safety.py module acts as a middleware that:

    Scans queries for emergency keywords.

    Triggers escalation logic for high-risk symptoms.

    Appends mandatory medical disclaimers to every response.

🚦 Getting Started
Prerequisites

    Python 3.9+

    Ollama installed and running locally.

    LLaMA model pulled: ollama pull llama3 (or your preferred version).

Installation

    Clone the repository:
    Bash

    git clone https://github.com/your-repo/clinical-rag-assistant.git

    Install dependencies:
    Bash

    pip install -r requirements.txt

    Initialize the vector store:
    Bash

    python ingest.py
    python embed_index.py

    Launch the application:
    Bash

    streamlit run ui_streamlit.py

📈 Enterprise Validation

This project demonstrates a "Production-First" mindset:

    Deterministic Evaluation: Includes a test suite to validate RAG responses against structured cases.

    Escalation Detection: Ready for deployment in environments where risk mitigation is the top priority (e.g., Banking, Healthcare).
