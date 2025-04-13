from langchain_core.prompts import PromptTemplate


prompt_template = PromptTemplate.from_template("给我讲一个{content}林黛玉倒拔垂杨柳的故事")

message = prompt_template.format(content="关于")

print(message)
