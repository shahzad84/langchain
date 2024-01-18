from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import HTMLHeaderTextSplitter
url = "https://plato.stanford.edu/entries/goedel/"

headers_to_split_on=[
    ("h1","Header 1"),
    ("h2","Header 2"),
    ("h3","Header 3"),
    ("h4","Header 4"),
]

html_splitter=HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

html_header_splits=html_splitter.split_text_from_url(url)
chunk_size=500
chunk_overlap=30
text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,chunk_overlap=chunk_overlap
)

splits=text_splitter.split_documents(html_header_splits)
print(splits[80:85])