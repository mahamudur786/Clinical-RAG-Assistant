# Clinical RAG Assistant
GenAI Capstone – LLaMA-Based Clinical RAG System (TCS Internal Initiative)
•	Designed and implemented end-to-end Retrieval-Augmented Generation (RAG) architecture using LLaMA (Ollama backend) for domain-grounded medical query support.
•	Built custom FAISS vector index with SentenceTransformers embeddings and metadata persistence for efficient semantic retrieval.
•	Implemented document ingestion pipeline (PDF/TXT), recursive chunking, and contextual retrieval framework.
•	Developed safety guardrails and escalation detection logic for high-risk symptoms.
•	Integrated Streamlit-based user interface for interactive query evaluation and structured response generation.
•	Demonstrated practical enterprise use-case for AI-assisted reporting and knowledge retrieval systems.

1️⃣ Config & Environment Control

You centralized environment configs, embedding models, LLM backend, and safety disclaimer in config.py 

config

That shows:

Environment abstraction

Model configurability

Production-style parameterization

That is strong engineering hygiene.

2️⃣ Document Ingestion & Chunking

You implemented:

PDF + TXT ingestion

Recursive chunking (LangChain splitter)

Overlapping chunk strategy

Processed storage pipeline

From ingest.py 

ingest

This shows:

Document ETL mindset

Structured preprocessing pipeline

Controlled chunking strategy (800 size, 150 overlap)

That is exactly how enterprise RAG systems are built.

3️⃣ Vector Embedding & Indexing

You:

Used SentenceTransformers

Generated embeddings

Built FAISS index

Persisted metadata

From embed_index.py 

embed_index

This is:

Custom FAISS index management

Not relying on managed vector DB

Manual metadata persistence

Full control of retrieval layer

That’s deeper than many "LangChain-only" projects.

4️⃣ RAG Pipeline & LLM Integration

From rag_pipeline.py 

rag_pipeline

You implemented:

Retrieval

Context assembly

Prompt structuring

Ollama LLaMA backend

Structured task instructions

Escalation logic

This is a clean RAG architecture.

Not just "call LLM".

5️⃣ Safety & Escalation Layer

From safety.py 

safety

You implemented:

Guardrails

Escalation triggers

Disclaimer enforcement

Emergency term detection

That is regulated-domain thinking.

Banks LOVE that mindset.

6️⃣ Evaluation Framework

From evaluation.py 

evaluation

You tested structured cases.

That shows:

Controlled testing approach

Deterministic evaluation

System validation

7️⃣ UI Layer

Streamlit front-end for user interaction
From ui_streamlit.py 

ui_streamlit

That shows:

End-to-end system ownership

User interface integration

Deployment awareness