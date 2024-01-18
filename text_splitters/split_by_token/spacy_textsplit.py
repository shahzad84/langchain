# spaCy is an open-source software library for advanced natural language processing, written in the programming languages Python and Cython.

with open("../../sample/data.txt") as f:
    state_of_the_union=f.read()


from langchain.text_splitter import SpacyTextSplitter
# import en_core_web_sm

# nlp = en_core_web_sm.load()
text_splitter=SpacyTextSplitter(chunk_size=1000)
texts=text_splitter.split_text(state_of_the_union)
print(texts[0])
