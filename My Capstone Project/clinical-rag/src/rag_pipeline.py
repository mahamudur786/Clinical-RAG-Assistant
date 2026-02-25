import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
from ollama import chat
from src.config import INDEX_DIR, EMBED_MODEL_NAME, TOP_K, OLLAMA_MODEL
from src.safety import safety_prefix, format_escalation


def load_index():
    index = faiss.read_index(os.path.join(INDEX_DIR, "faiss.index"))

    with open(os.path.join(INDEX_DIR, "metadata.pkl"), "rb") as f:
        metadata = pickle.load(f)

    return index, metadata


def retrieve(query: str):
    index, metadata = load_index()
    model = SentenceTransformer(EMBED_MODEL_NAME)

    q_emb = model.encode([query])
    distances, indices = index.search(q_emb, TOP_K)

    results = []
    for i in indices[0]:
        results.append(metadata[i]["source"])

    return results


def load_chunk_texts(chunk_files):
    texts = []
    for fname in chunk_files:
        path = os.path.join("data/processed", fname)
        with open(path, "r", encoding="utf-8") as f:
            texts.append(f.read())
    return texts


def generate_answer(query: str):
    retrieved_files = retrieve(query)
    chunks = load_chunk_texts(retrieved_files)

    context = "\n\n".join(chunks)

    escalation = format_escalation(query)

    prompt = f"""
{safety_prefix()}

User symptoms:
{query}

Retrieved medical references:
{context}

Task:
1. Provide top 3 possible differential diagnoses (NOT definitive).
2. Provide supporting citations from the text.
3. Suggest next diagnostic steps (tests, exams).
4. Include safety disclaimer.
5. Use structured bullet points.
"""

    response = chat(
        model=OLLAMA_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return escalation, response["message"]["content"]
