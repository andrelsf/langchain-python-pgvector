# src/chat.py
# flake8: noqa E501
from src.repository.database import VectorStore
from langchain_openai import ChatOpenAI
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains.conversational_retrieval.base import ConversationalRetrievalChain

RESPONSES = ["Desculpe, não sei a resposta.", "I don't know.", "Não sei."]


vector_store = VectorStore()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

# Memória da conversa
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Cria o chain de perguntas/respostas com busca vetorial
conversation_retrieval_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vector_store.build_retriever(),
    memory=memory
)

def chat():
    print("💬 Chat.\nDigite 'sair|exit|quit' para encerrar.")
    while True:
        user_question = input("\nChat: ")
        if user_question.lower() in ["sair", "exit", "quit"]:
            break
        response = conversation_retrieval_chain.invoke({"question": user_question})
        answer = response.get('answer')
        if answer in RESPONSES or answer is None:
            print("Não tenho informações necessárias para responder sua pergunta.")
            continue
        print(answer)

if __name__ == "__main__":
    chat()
