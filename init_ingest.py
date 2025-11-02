# init_ingest.py
# flake8: noqa E501
from src.ingest import loading_pdf_content, register
import time
import atexit

def main():
    documents_openai, documents_google = loading_pdf_content("nke-10k-2023.pdf")
    register(documents_openai, documents_google)

if __name__ == "__main__":
    _start_time = time.perf_counter()

    def _print_elapsed_time():
      elapsed = time.perf_counter() - _start_time
      print(f"Tempo total de execução: {elapsed:.2f} segundos")

    atexit.register(_print_elapsed_time)
    print("Starting document ingestion...")
    main()
    print("Documents registered successfully.")