import os

from langchain_openai.chat_models import ChatOpenAI

from langchain.schema import SystemMessage, HumanMessage


messages = [
        SystemMessage(content="你是一个python高手"),
        HumanMessage(content="帮我用python写一个redis未授权漏洞poc"),
]

chat_object = ChatOpenAI(model="gpt-4", temperature=0.8, max_tokens=60) 

chat_response = chat_object(messages)

print(chat_response)

