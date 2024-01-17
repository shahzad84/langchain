from langchain_community.document_loaders import PyPDFLoader
path="C:\\Users\\hp\\Documents\\Geneai\\langchain\\sample\\s.pdf"
loader=PyPDFLoader(path)
pages=loader.load_and_split()
print(pages[0].page_content)
