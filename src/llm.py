# src/llm.py

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

RAG_PROMPT = """You are a helpful and knowledgeable assistant specializing
in Indian Government Schemes and welfare programs.

Your job is to answer citizens' questions about government schemes accurately
using ONLY the information provided in the context below.

STRICT RULES:
1. Answer ONLY from the provided context
2. Always mention the scheme name in your answer
3. If the context does not contain the answer, say:
   I don't have specific information about this. Please visit myscheme.gov.in
4. Be concise but complete - include eligibility, benefits, and how to apply
5. If multiple schemes are relevant, mention all of them

CONTEXT (Official Government Scheme Information):
{context}

CITIZEN'S QUESTION: {question}

ANSWER:"""

RAG_PROMPT_TEMPLATE = PromptTemplate(
    template=RAG_PROMPT,
    input_variables=["context", "question"]
)


def get_llm(temperature: float = 0):
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=temperature,
        max_tokens=1024,
    )
    return llm


if __name__ == "__main__":
    llm = get_llm()
    response = llm.invoke("Say LLM connected successfully in one line")
    print(response.content)