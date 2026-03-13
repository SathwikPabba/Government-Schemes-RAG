# src/vectorstore.py

from langchain_chroma import Chroma
from src.embeddings import get_embeddings
import os

CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "government_schemes"


def build_vectorstore(chunks: list):
    embeddings = get_embeddings()

    print(f"\n🔢 Embedding {len(chunks)} chunks...")
    print("This may take 2-3 minutes...")

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH,
        collection_name=COLLECTION_NAME,
    )

    count = vectorstore._collection.count()
    print(f"\n✅ Vector store built! {count} vectors stored.")
    print(f"📁 Saved to: {CHROMA_PATH}/")

    return vectorstore


def load_vectorstore():
    if not os.path.exists(CHROMA_PATH):
        raise FileNotFoundError(
            f"Vector store not found at {CHROMA_PATH}. "
            "Run build_vectorstore() first!"
        )

    embeddings = get_embeddings()

    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings,
        collection_name=COLLECTION_NAME
    )

    count = vectorstore._collection.count()
    print(f"✅ Loaded vector store: {count} vectors")
    return vectorstore


if __name__ == "__main__":
    from src.ingest import load_all_documents, chunk_documents

    print("=== BUILDING VECTOR STORE ===")
    docs = load_all_documents()
    chunks = chunk_documents(docs)
    vs = build_vectorstore(chunks)

    # Test retrieval
    results = vs.similarity_search_with_score("Who is eligible for PM-KISAN?", k=3)
    for i, (doc, score) in enumerate(results):
        print(f"\nResult {i+1} (score: {score:.4f})")
        print(f"Scheme: {doc.metadata.get('scheme_name', 'Unknown')}")
        print(f"Preview: {doc.page_content[:200]}...")