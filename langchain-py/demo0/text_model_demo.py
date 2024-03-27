import os

from langchain_openai.llms import OpenAI

os.environ["OPENAI_API_KEY"] = "your openai api key"

text_model_llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.8, max_tokens=60)

text_response = text_model_llm.predict("你好，能帮我看看python的最新版本好是多少能")

print(text_response)

