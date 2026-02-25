import os
from typing import List, Dict
from PyPDF2 import PdfReader
from src.config import DATA_RAW_DIR, DATA_PROCESSED_DIR
from langchain_text_splitters import RecursiveCharacterTextSplitter


def read_pdf(path: str) -> str:
    reader = PdfReader(path)
    text = []
    for page in reader.pages:
        content = page.extract_text() or ""
        text.append(content)
    return "\n".join(text)


def read_txt_md(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_documents() -> List[Dict]:
    docs = []

    for fname in os.listdir(DATA_RAW_DIR):
        fpath = os.path.join(DATA_RAW_DIR, fname)

        if fname.lower().endswith(".pdf"):
            text = read_pdf(fpath)
            dtype = "pdf"
        elif fname.lower().endswith((".txt", ".md")):
            text = read_txt_md(fpath)
            dtype = "text"
        else:
            continue

        docs.append({
            "source": fname,
            "text": text,
            "type": dtype
        })

    return docs


def chunk_documents(docs: List[Dict]) -> List[Dict]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = []

    for doc in docs:
        split_texts = splitter.split_text(doc["text"])
        for i, chunk in enumerate(split_texts):
            chunks.append({
                "source": doc["source"],
                "chunk_id": i,
                "text": chunk
            })

    return chunks


def save_chunks(chunks: List[Dict]):
    os.makedirs(DATA_PROCESSED_DIR, exist_ok=True)

    for c in chunks:
        fname = f"{c['source']}_chunk_{c['chunk_id']}.txt"
        fpath = os.path.join(DATA_PROCESSED_DIR, fname)

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(c["text"])


if __name__ == "__main__":
    print("Loading documents...")
    docs = load_documents()

    print("Chunking documents...")
    chunks = chunk_documents(docs)

    print("Saving chunks...")
    save_chunks(chunks)

    print(f"Done. Created {len(chunks)} chunks.")
