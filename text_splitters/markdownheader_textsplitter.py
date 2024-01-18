# When a full paragraph or document is embedded, the embedding process considers both the overall context and the relationships between the sentences and phrases within the text. This can result in a more comprehensive vector representation that captures the broader meaning and themes of the text.


from langchain.text_splitter import MarkdownHeaderTextSplitter

markdown_document = "# Foo\n\n    ## Bar\n\nHi this is Jim\n\nHi this is Joe\n\n ### Boo \n\n Hi this is Lance \n\n ## Baz\n\n Hi this is Molly"

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

markdown_splitter=MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

md_header_splits=markdown_splitter.split_text(markdown_document)

print(md_header_splits)

