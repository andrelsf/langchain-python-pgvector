# src/ingest.py
# flake8: noqa E501
from os import path
from langchain_openai import OpenAIEmbeddings
from src.repository.database import VectorStore
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter

current_dir = path.dirname(path.abspath(__file__))

def loading_pdf_content(pdf_name: str):
    try:
        file_path = path.join(current_dir, '..', pdf_name)
        contents = PyPDFLoader(file_path).load()
        return RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150) \
            .split_documents(contents)
    except Exception as ex:
        print(f"Erro ao carregar o arquivo PDF: {ex}")
        return []


def register(documents: list[Document]):
    print("Registering embeddings...")
    vectorstore = VectorStore()
    vectorstore.persist_documents(documents)