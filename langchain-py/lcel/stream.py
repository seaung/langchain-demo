from langchain_ollama import ChatOllama


model = ChatOllama(model="qwen2:7b")

chunks = []

for item in model.stream("什么是python!"):
    chunks.append(item)
    print(item.content, end="|", flush=True)
