# init_search.py
# flake8: noqa E501
from src.search import search

def main():
    response = search()
    print(response)

if __name__ == "__main__":
    main()
