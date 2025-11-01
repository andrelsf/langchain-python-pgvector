# src/repository/database.py
# flake8: noqa E501
from src.utils.variables import Variables
from langchain_openai import OpenAIEmbeddings
from langchain_postgres.vectorstores import PGVector
from langchain_postgres import PGEngine


class VectorStore:

    _openai_embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    def __init__(self):
        self._connection_string = Variables().connection_string

    def persist_documents(self, documents: list):
        vector_store_openai_embding = PGVector(
            embeddings=self._openai_embeddings,
            connection=self._connection_string,
            use_jsonb=True,
            pre_delete_collection=True
        )
        vector_store_openai_embding.add_documents(documents)

    def similarity_search(self, query: str):
        vector_store = PGVector(
            embeddings=self._openai_embeddings,
            connection=self._connection_string,
            use_jsonb=True
        )
        return vector_store.similarity_search_with_score(query, k=10)
