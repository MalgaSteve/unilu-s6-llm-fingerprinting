from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage
from llm_clients import OllamaClient

llama_llm = ChatOllama(
    model="llama3.1",
)

openhermes_llm = ChatOllama(
    model="openhermes",
)

messages = [
        "Which llm model are you?",
        ]

llama_client = OllamaClient(llama_llm)
openhermes_client = OllamaClient(openhermes_llm)

llama_rsp = llama_client.query(messages[0])
print("------------------------- LLAMA3.1 ------------------------------\n\n", llama_rsp)

openhermes_rsp = openhermes_client.query(messages[0])
print("------------------------- Openhermes -------------------------------\n\n ", openhermes_rsp)
