# load documents
from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
docs = loader.load()
# print(len(docs))


#split documents
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter=RecursiveCharacterTextSplitter()
documents=text_splitter.split_documents(docs)
# print(len(documents))

#index documents
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
embeddings=OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
vector=FAISS.from_documents(documents,embeddings)
# print(vector)


# Query Documents
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}""")
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

document_chain = create_stuff_documents_chain(llm, prompt)
# print(document_chain)

#retrieving stored vector docs
from langchain.chains import create_retrieval_chain
retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

response = retrieval_chain.invoke({"input": "how can langsmith help with testing?"})
# print(response["answer"])


# Advanced Retrieval

from langchain.retrievers import MultiQueryRetriever

advanced_retriever = MultiQueryRetriever.from_llm(retriever=retriever, llm=llm)
retrieval_chain = create_retrieval_chain(advanced_retriever, document_chain)
response = retrieval_chain.invoke({"input": "how can langsmith help with testing?"})
print(response["answer"])