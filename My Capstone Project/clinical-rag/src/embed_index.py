import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
from src.config import DATA_PROCESSED_DIR, INDEX_DIR, EMBED_MODEL_NAME
import numpy as np
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def load_chunks():
    texts = []
    metadata = []

    for fname in os.listdir(DATA_PROCESSED_DIR):
        if fname.endswith(".txt"):
            path = os.path.join(DATA_PROCESSED_DIR, fname)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            texts.append(text)
            metadata.append({"source": fname})

    return texts, metadata


def build_index():
    os.makedirs(INDEX_DIR, exist_ok=True)

    print("Loading chunks...")
    texts, metadata = load_chunks()

    print("Loading embedding model...")
    model = SentenceTransformer(EMBED_MODEL_NAME)

    print("Embedding chunks...")
    embeddings = model.encode(texts, show_progress_bar=True)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    print("Saving FAISS index...")
    faiss.write_index(index, os.path.join(INDEX_DIR, "faiss.index"))

    print("Saving metadata...")
    with open(os.path.join(INDEX_DIR, "metadata.pkl"), "wb") as f:
        pickle.dump(metadata, f)

    print("Index built successfully!")


if __name__ == "__main__":
    build_index()
