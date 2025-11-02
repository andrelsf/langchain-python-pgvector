#!/usr/bin/env bash
set -euo pipefail

# Cria extensão no banco inicial
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE IF NOT EXISTS langchain_openai (
    langchain_id VARCHAR PRIMARY KEY,
    content TEXT,
    embedding VECTOR(1536)
);
CREATE TABLE IF NOT EXISTS langchain_google_genai (
    langchain_id VARCHAR PRIMARY KEY,
    content TEXT,
    embedding VECTOR(768)
);
EOSQL