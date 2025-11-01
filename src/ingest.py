# src/ingest.py
# flake8: noqa E501
from os import path
from langchain_openai import OpenAIEmbeddings
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


def build_embeddings(chunks: list):
    embeddings = []
    embeddings_model = OpenAIEmbeddings()
    for chunk in chunks:
        vector = embeddings_model.embed_query(chunk.page_content)
        embeddings.append({
            "text": chunk.page_content,
            "embedding": vector
        })
    return embeddings
