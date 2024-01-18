# At a high level, this splits into sentences, then groups into groups of 3 sentences, and then merges one that are similar in the embedding space.
# Semantic Chunking

with open("../sample/data.txt") as f:
    state_of_the_union=f.read()

from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
import os

text_splitter=SemanticChunker(OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY")))

docs=text_splitter.create_documents([state_of_the_union])
print(docs[0].page_content)
