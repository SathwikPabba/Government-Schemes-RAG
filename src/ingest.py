# src/ingest.py

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from pathlib import Path

DATA_DIR = "data/processed"


def load_all_documents():
    print("📂 Loading documents...")
    documents = []

    for filepath in sorted(Path(DATA_DIR).glob("*.txt")):
        loader = TextLoader(str(filepath), encoding="utf-8")
        docs = loader.load()

        scheme_name = filepath.stem
        for doc in docs:
            doc.metadata["scheme_name"] = scheme_name
            doc.metadata["source"] = str(filepath)

        documents.extend(docs)
        print(f"  ✅ Loaded: {filepath.name}")

    print(f"📚 Total documents loaded: {len(documents)}")
    return documents


def chunk_documents(documents):
    print("✂️  Chunking documents...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )

    all_chunks = []
    for doc in documents:
        chunks = splitter.split_documents([doc])
        scheme_name = doc.metadata.get("scheme_name", "unknown")
        print(f"  {scheme_name}: {len(chunks)} chunks")
        all_chunks.extend(chunks)

    print(f"✅ Total chunks created: {len(all_chunks)}")
    return all_chunks


if __name__ == "__main__":
    docs = load_all_documents()
    chunks = chunk_documents(docs)
    print(f"\n🎉 Ingestion complete! {len(chunks)} chunks ready.")