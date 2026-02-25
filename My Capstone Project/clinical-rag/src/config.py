import os
# Directory Configuration
DATA_RAW_DIR = "/home/labuser/clinical-rag/data/raw"
DATA_PROCESSED_DIR = "/home/labuser/clinical-rag/data/processed"
INDEX_DIR = "/home/labuser/clinical-rag/index/"

# Embedding Model
EMBED_MODEL_NAME = os.getenv(
    "EMBED_MODEL_NAME",
    "sentence-transformers/all-MiniLM-L6-v2"
)
# Retrieval
TOP_K = int(os.getenv("TOP_K", "4"))

# LLM (Ollama)
LLM_BACKEND = "ollama"
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "Llama3.2:latest")

# Safety Disclaimer
SAFETY_DISCLAIMER = (
    "This assistant provides informational support only. "
    "It does NOT provide medical diagnosis, prescriptions, or treatment advice. "
    "For urgent, severe, or life-threatening symptoms, seek immediate medical care."
)
print("This is a config.py file that defines the configuration variables used throughout the project and It ran fine.")