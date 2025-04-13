from langchain.prompts import FewShotPromptTemplate, PromptTemplate


message_examples = [
    {
        "question": "什么是python",
        "result": "python是一门功能强大的解释性编程语言"
    },
    {
        "question": "什么是rust",
        "result": "rust是一门强大的编译型语言"
    },
    {
        "question": "什么是golang",
        "result": "golang是由谷歌于2009年推出的编译型编程语言"
    }
]

example_prompt = PromptTemplate(input_variables=["question", "result"],
                                template="问题: {question}\\n{result}")


prompt = FewShotPromptTemplate(examples=message_examples,
                               example_prompt=example_prompt,
                               suffix="问题: {input}",
                               input_variables=["input"])

print(prompt.format(input="python是什么"))
