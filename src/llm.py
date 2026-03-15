# src/llm.py

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

RAG_PROMPT = """You are an expert assistant on Indian Government Schemes helping Indian citizens.

CONTEXT (Official Government Scheme Information):
{context}

CITIZEN'S QUESTION: {question}

INSTRUCTIONS:
- Answer the EXACT question asked — nothing more, nothing less
- Give a comprehensive answer covering benefits, eligibility and how to apply
- Use EXACT figures from context (Rs. 20, Rs. 2 lakh, 35%, 100 days)
- Keep answer to 4-6 sentences maximum
- Mention scheme name once clearly
- Never use phrases like "based on context" or "according to information"
- Never add unsolicited advice or extra information
- If not in context: "Please visit myscheme.gov.in for details"

PRECISE ANSWER:"""

RAG_PROMPT_TEMPLATE = PromptTemplate(
    template=RAG_PROMPT,
    input_variables=["context", "question"]
)


def get_llm(temperature: float = 0):
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=temperature,
        max_tokens=2048,
    )
    return llm


if __name__ == "__main__":
    llm = get_llm()
    response = llm.invoke("Say LLM connected successfully in one line")
    print(response.content)