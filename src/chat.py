# src/chat.py
# flake8: noqa E501
from asyncio import run
from langchain_openai import ChatOpenAI
from src.repository.database import VectorStore
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.retrieval import create_retrieval_chain 
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

RESPONSES = ["Desculpe, não sei a resposta.", "I don't know.", "Não sei."]


vector_store = VectorStore()
llm = ChatOpenAI(
    model="gpt-5-nano",
    temperature=0,
    use_responses_api=False
)

system_prompt = ("""
CONTEXTO:
{context}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
"Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{input}

RESPONDA A "PERGUNTA DO USUÁRIO"
""")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# Criar o chain de resposta de perguntas
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(vector_store.build_retriever(), question_answer_chain)

def chat():
    print("💬 Chat.\nDigite 'sair|exit|quit' para encerrar.")
    while True:
        user_question = input("\nChat: ")
        if user_question.lower() in ["sair", "exit", "quit"]:
            break
        docs = run(vector_store.similarity_search(user_question))
        context = "\n".join([doc.page_content for doc, _ in docs])
        response = rag_chain.invoke({"context": context, "input": user_question})
        answer = response.get('answer')
        if answer in RESPONSES or answer is None:
            print("Não tenho informações necessárias para responder sua pergunta.")
            continue
        print(answer)

if __name__ == "__main__":
    chat()
