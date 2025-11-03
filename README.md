# LangChain Python and PostgreSQL extension PGVector

Ingestão e Busca Semântica com LangChain e PostgreSQL com extensao pgVector

## Tecnologias

- Docker|Podman
- Docker Compose (docker-compose.yml)
- Python3.12
- Terminal Linux/GitBash (Windows) - (uso do makefile)

## Como usar

**[Required]**
> Copie ou renomei o arquivo de exemplo `src/.env.example` para `src/.env`
> Preencha as variaveis referente aos tokens de API `OPENAI_API_KEY` e `GOOGLE_API_KEY`

**[Required] Start container**
```shell
docker-compose up -d
```
> NOTA: O arquivo `.docker/docker-entrypoint-initdb.d/initial-database.sh` contem script de inicializacao das tabelas de contexto do langchain e ativacao da extensao `pgVector`.

**Stop and remove container**
```shell
docker-compose down
```

**Debug logs container**
```shell
docker-compose logs -f
```
---

## [Required] Com conteiner inicializado

Preparando Virtual Environment Python3

```shell
python3 -m venv .venv
source .venv/bin/activate
```

1. Ingestão do PDF
```shell
python3 init_ingest.py
```

2. [Optional] Pesquisa
```shell
python3 init_search.py
```

3. Iniciar CHAT
```shell
python3 init_chat.py
```

> **Nota**: para desativar o virtualEnv do Python basta usar o cmd `deactivate`

## Referencias

- [Github PGVector](https://github.com/pgvector/pgvector)
- [Github PGVector Docker](https://github.com/pgvector/pgvector?tab=readme-ov-file#docker)
- [Text Embedding OpenAI](https://docs.langchain.com/oss/python/integrations/text_embedding/openai)
- [Langchain PGVector](https://docs.langchain.com/oss/python/integrations/vectorstores/pgvector)
- [Langchain knowledge Base](https://docs.langchain.com/oss/python/langchain/knowledge-base#pgvector)
