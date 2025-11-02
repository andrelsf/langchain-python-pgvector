# main.py
# flake8: noqa E501
from src.ingest import (
  loading_pdf_content,
  register
)
from src.search import search

def main():
    documents_openai, documents_google = loading_pdf_content("nke-10k-2023.pdf")
    register(documents_openai, documents_google)
    response = search()
    print(response)

if __name__ == "__main__":
    main()
