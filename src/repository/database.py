# src/repository/database.py
# flake8: noqa E501
from asyncio import run
from langchain_postgres import PGEngine
from src.utils.variables import Variables
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVectorStore
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings


class VectorStore:

    _amount_results = 10
    _openai_embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    _google_embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    def __init__(self):
        self._connection_string = Variables().connection_string
        self._pg_engine = PGEngine.from_connection_string(url=self._connection_string)
        self._vector_store_openai = run(
            self._build_pg_vector_store("langchain_openai", self._openai_embeddings))
        self._vector_store_google = run(
            self._build_pg_vector_store("langchain_google_genai", self._google_embeddings))

    async def _build_pg_vector_store(self, table_name, embeddings) -> PGVectorStore:
        vector_store = await PGVectorStore.create(
            engine=self._pg_engine,
            table_name=table_name,
            embedding_service=embeddings
        )
        return vector_store

    async def persist_documents(self, documents_openai: list[Document], documents_google: list[Document]):
        await self._vector_store_openai.aadd_documents(documents_openai)
        await self._vector_store_google.aadd_documents(documents_google)

    def build_retriever(self):
        openai_as_retriever = self._vector_store_openai.as_retriever(
            search_type="similarity",
            search_kwargs={"k": self._amount_results}
        )
        return openai_as_retriever

    async def similarity_search(self, query: str):
        openai_result = await self._vector_store_openai.asimilarity_search_with_score(query, k=self._amount_results)
        google_result = await self._vector_store_google.asimilarity_search_with_score(query, k=self._amount_results)
        return openai_result + google_result

    async def question(self, query: str):
        results = await self.similarity_search(query)
        return results
