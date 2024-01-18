# CodeTextSplitter allows you to split your code with multiple languages supported.

from langchain.text_splitter import (Language,RecursiveCharacterTextSplitter,)

# Full list of supported languages
[e.value for e in Language]

['cpp',
 'go',
 'java',
 'kotlin',
 'js',
 'ts',
 'php',
 'proto',
 'python',
 'rst',
 'ruby',
 'rust',
 'scala',
 'swift',
 'markdown',
 'latex',
 'html',
 'sol',
 'csharp',
 'cobol']


# You can also see the separators used for a given language
RecursiveCharacterTextSplitter.get_separators_for_language(Language.PYTHON)

['\nclass ', '\ndef ', '\n\tdef ', '\n\n', '\n', ' ', '']


# python code 

PYTHON_CODE="""
    def hello_world():
    print("Hello, World!")

    # Call the function
    hello_world()
"""

python_splitter=RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON,chunk_size=50,chunk_overlap=0)

python_docs=python_splitter.create_documents([PYTHON_CODE])
print(python_docs)
