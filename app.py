import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()

llm_model = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response=llm_model.invoke("how can langsmith help")
print(response)