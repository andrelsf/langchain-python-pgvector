# src/chat.py
# flake8: noqa E501
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

system_prompt = (
    "Você é um assistente para tarefas de perguntas e respostas somente do retriever PDF Nike. "
    "Use os seguintes trechos de contexto recuperado para responder "
    "à pergunta. Se você não souber a resposta, diga que "
    "não tenho informações necessárias para responder sua pergunta.. "
    "Use no máximo três frases e mantenha a resposta concisa."
    "\n\n"
    "{context}"
)

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
        response = rag_chain.invoke({"input": user_question})
        answer = response.get('answer')
        if answer in RESPONSES or answer is None:
            print("Não tenho informações necessárias para responder sua pergunta.")
            continue
        print(answer)

if __name__ == "__main__":
    chat()
