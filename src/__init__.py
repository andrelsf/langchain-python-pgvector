# flake8: noqa E501
from os import environ
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = environ.get("OPENAI_API_KEY", None)
if OPENAI_API_KEY is None:
  raise ValueError("A variável de ambiente OPENAI_API_KEY não está definida.")
