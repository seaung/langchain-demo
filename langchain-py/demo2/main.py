import os

from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

prompt_template = """你是一个python web全栈工程师
请你以这个要求{}实现一个功能
"""

prompt = PromptTemplate.from_template(prompt_template)

print(prompt)


os.environ["OPNEN_API_KEY"] = "your_open_api_key"


model = OpenAI(model="gpt-3.5-turbo-instruct")


quetions = ["斐波那契数列", "红黑树"]

for _, item in enumerate(quetions):
    input_prompt = prompt_template.format(item)

    output = model(input_prompt)

    print(output)

