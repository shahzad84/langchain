# It tries to split on them in order until the chunks are small enough.

with open("../sample/data.txt") as f:
    state_of_the_union=f.read()

from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)

texts=text_splitter.create_documents([state_of_the_union])
# print(texts[0])
print(text_splitter.split_text(state_of_the_union)[:2])