# The SentenceTransformersTokenTextSplitter is a specialized text splitter for use with the sentence-transformer models. 

from langchain.text_splitter import SentenceTransformersTokenTextSplitter

splitter=SentenceTransformersTokenTextSplitter(chunk_overlap=0)
text="lorem"

count_start_and_stop_tokens=2
text_token_count=splitter.count_tokens(text=text)-count_start_and_stop_tokens
print(text_token_count)
