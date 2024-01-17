from langchain_community.document_loaders import UnstructuredFileLoader
file_path = 'C:\\Users\\hp\\Documents\\Geneai\\langchain\\sample\\data.txt'
loader = UnstructuredFileLoader(file_path)
docs = loader.load()
print(docs[0].page_content)