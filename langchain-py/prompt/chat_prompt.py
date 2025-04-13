from langchain_core.prompts import ChatPromptTemplate


chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个聊天机器人, 你的名字是: {name}"),
    ("human", "你好"),
    ("ai", "我很好"),
    ("human", "{user_input}"),
])

messages = chat_prompt_template.format_messages(name="小智", user_input="你好呀")

print(messages)
