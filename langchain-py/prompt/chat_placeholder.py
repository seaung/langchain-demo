from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


chat_prompt_template = ChatPromptTemplate.from_messages([
    AIMessage(content="你好呀"),
    SystemMessage(content="你是一个聊天机器人，你的名字为: {name}"),
    HumanMessage(content="{user_input}"),
    MessagesPlaceholder("question"),
])

template = chat_prompt_template.invoke({"question": [
    HumanMessage(content="我非常的好"), ]},
    name="lihua", user_input="你好，很高兴认识你!!!", )

print(template)
