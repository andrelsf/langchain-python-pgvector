# src/search.py
# flake8: noqa E501
from asyncio import run
from src.repository.database import VectorStore

vectorstore = VectorStore()


def search():
    query = "Qual é a capital da França?"
    results = run(vectorstore.similarity_search(query))
    if not results:
      return "Não tenho informações necessárias para responder sua pergunta."
    # escolher o resultado com maior score e garantir que o score seja float
    doc, score = max(results, key=lambda x: x[1]) 
    return f"Content: {doc.page_content}, Source: {doc.metadata.get('source')}, Score: {score}"
