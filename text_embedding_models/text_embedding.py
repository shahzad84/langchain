from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()
embeddings_model=OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))

embeddings=embeddings_model.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ]
)

print(len(embeddings),len(embeddings[0]))


# embed_query
# Embed single query
# Embed a single piece of text for the purpose of comparing to other embedded pieces of texts.


# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# embedded_query[:5]