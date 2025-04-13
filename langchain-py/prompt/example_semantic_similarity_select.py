from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings


examples = [
    {"question": "", "answer": ""}
]

example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    OllamaEmbeddings(),
    Chroma,
    k=1
)

question = "python是什么?"

selected_examples = example_selector.select_examples({"question": question})

for item in selected_examples:
    for k, v in item.items():
        print(f"{k} - {v}")
