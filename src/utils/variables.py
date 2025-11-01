# src/utils/variables.py
# flake8: noqa E501
from os import environ


class Variables:

    def __init__(self):
        DB_CONFIG = {
          "dbname": environ.get("DB_NAME", None),
          "user": environ.get("DB_USER", None),
          "password": environ.get("DB_PASSWORD", None),
          "host": environ.get("DB_HOST", "localhost"),
          "port": int(environ.get("DB_PORT", "5432")),
        }
        if None in DB_CONFIG.values():
            raise ValueError("As configurações do banco de dados não estão completas.")
        self.connection_string = f"postgresql+psycopg://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
