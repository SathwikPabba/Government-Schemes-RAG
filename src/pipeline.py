# src/pipeline.py

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from src.llm import get_llm, RAG_PROMPT_TEMPLATE
from src.vectorstore import load_vectorstore
from dataclasses import dataclass


@dataclass
class RAGResponse:
    question: str
    answer: str
    sources: list
    num_sources: int

    def display(self):
        print(f"\n{'='*60}")
        print(f"Q: {self.question}")
        print(f"{'='*60}")
        print(f"A: {self.answer}")
        print(f"\n📚 Sources ({self.num_sources}):")
        for i, src in enumerate(self.sources, 1):
            print(f"  {i}. {src.get('scheme_name', 'Unknown')}")
        print('='*60)


class GovernmentSchemeRAG:

    def __init__(self):
        print("Initializing RAG Pipeline...")

        self.vectorstore = load_vectorstore()

        self.retriever = self.vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 5,
                "fetch_k": 20,
                "lambda_mult": 0.7
            }
        )

        self.llm = get_llm(temperature=0)

        self.chain = (
            {
                "context": self.retriever | self._format_docs,
                "question": RunnablePassthrough()
            }
            | RAG_PROMPT_TEMPLATE
            | self.llm
            | StrOutputParser()
        )

        print("✅ RAG Pipeline ready!")

    def _format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def query(self, question: str) -> RAGResponse:
        print(f"\n🔍 Processing: {question}")

        try:
            answer = self.chain.invoke(question)
            source_docs = self.retriever.invoke(question)

            seen_schemes = set()
            sources = []
            for doc in source_docs:
                scheme_name = doc.metadata.get("scheme_name", "Unknown")
                if scheme_name not in seen_schemes:
                    seen_schemes.add(scheme_name)
                    sources.append({
                        "scheme_name": scheme_name,
                        "ministry": doc.metadata.get("ministry", "N/A"),
                        "category": doc.metadata.get("category", "N/A"),
                        "preview": doc.page_content[:200] + "..."
                    })

            return RAGResponse(
                question=question,
                answer=answer,
                sources=sources,
                num_sources=len(sources)
            )

        except Exception as e:
            print(f"❌ Error: {e}")
            return RAGResponse(
                question=question,
                answer=f"An error occurred: {str(e)}",
                sources=[],
                num_sources=0
            )

    def get_all_schemes(self) -> list:
        results = self.vectorstore._collection.get()
        schemes = set()
        for meta in results.get("metadatas", []):
            if meta and "scheme_name" in meta:
                schemes.add(meta["scheme_name"])
        return sorted(list(schemes))


if __name__ == "__main__":
    rag = GovernmentSchemeRAG()

    test_questions = [
        "What is PM-KISAN and who is eligible?",
        "How do I apply for Ayushman Bharat?",
        "What schemes are available for women entrepreneurs?",
    ]

    for question in test_questions:
        response = rag.query(question)
        response.display()