# src/embeddings.py

from langchain_huggingface import HuggingFaceEmbeddings


def get_embeddings():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={
            "normalize_embeddings": True,
            "batch_size": 32
        }
    )
    return embeddings


if __name__ == "__main__":
    print("Loading embedding model...")
    emb = get_embeddings()
    test = emb.embed_query("Who is eligible for PM-KISAN?")
    print(f"✅ Embedding model works!")
    print(f"Embedding dimension: {len(test)}")