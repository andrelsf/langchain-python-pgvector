# src/ingest.py
# flake8: noqa E501
from os import path
from asyncio import run
from langchain_core.documents import Document
from src.repository.database import VectorStore
from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter

current_dir = path.dirname(path.abspath(__file__))

def loading_pdf_content(pdf_name: str) -> tuple[list[Document], list[Document]]:
    try:
        file_path = path.join(current_dir, '..', pdf_name)
        contents = PyPDFLoader(file_path).load()
        documents_openai = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150) \
            .split_documents(contents)
        documents_google = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150) \
            .split_documents(contents)
        return documents_openai, documents_google
    except Exception as ex:
        print(f"Erro ao carregar o arquivo PDF: {ex}")
        return []


def register(documents_openai: list[Document], documents_google: list[Document]):
    print("Registering embeddings...")
    vectorstore = VectorStore()
    run(vectorstore.persist_documents(documents_openai, documents_google))
    print("Embeddings registered successfully.")
