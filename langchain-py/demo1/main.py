import os

from langchain.document_loaders.pdf import PyPDFLoader
from langchain.document_loaders.text import TextLoader
from langchain.document_loaders.word_document import Docx2txtLoader
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.chains import RetrievalQA

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.qdrant import Qdrant
from langchain_openai import OpenAIEmbeddings, ChatOpenAI


base_dir = os.path.dirname(os.path.abspath(__file__))

document_path = os.path.join(base_dir, "documents")

documents = []

for item in os.listdir(document_path):
    file_path = os.path.join(document_path, item)
    if item.endswith(".txt"):
        loader = TextLoader(file_path)
        documents.extend(loader.load())
    if item.endswith(".doc"):
        loader = Docx2txtLoader(file_path)
        documents.extend(loader.load())
    if item.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
        documents.extend(loader.load())


text_splitters = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=10)
chunk_document = text_splitters.split_documents(documents)

vectorstore = Qdrant.from_documents(documents=chunk_document, embedding=OpenAIEmbeddings(), location=":memory:", collection_name="my_collections")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

retriever_from_llm = MultiQueryRetriever.from_llm(retriever=vectorstore.as_retriever(), llm=llm)

qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever_from_llm)


