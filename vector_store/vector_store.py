import os
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
load_dotenv()

raw_documents=TextLoader("../sample/data.txt").load()
text_splitter=CharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
documents=text_splitter.split_documents(raw_documents)
db=Chroma.from_documents(documents,OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY")))

query="where does taj mahal located?"
docs=db.similarity_search(query)
print(docs[0].page_content)



