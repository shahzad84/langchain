#  In agents, a language model is used as a reasoning engine to determine which actions to take and in which order.

# To best understand the agent framework, let’s build an agent that has two tools: one to look things up online, and one to look up specific data that we’ve loaded into a index.


# Define tools
# We first need to create the tools we want to use. We will use two tools: Tavily (to search online) and then a retriever over a local index we will create

# Tavily

from langchain_community.tools.tavily_search import TavilySearchResults
import os
from dotenv import load_dotenv
load_dotenv()

search = TavilySearchResults(api_key=os.getenv("TAVILY_API_KEY"))
tavil=search.invoke("what is the weather in SF")
# print(tavil)


# Retriever
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
docs = loader.load()
documents = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200
).split_documents(docs)
vector = FAISS.from_documents(documents, OpenAIEmbeddings())
retriever = vector.as_retriever()
ret=retriever.get_relevant_documents("how to upload a dataset")[0]
# print(ret)


#  that we have populated our index that we will do doing retrieval over, we can easily turn it into a tool 

from langchain.tools.retriever import create_retriever_tool
retriever_tool = create_retriever_tool(
    retriever,
    "langsmith_search",
    "Search for information about LangSmith. For any questions about LangSmith, you must use this tool!",
)

# Tools
tools = [search, retriever_tool]


# Create the agent

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0,api_key=os.getenv("OPENAI_API_KEY"))

from langchain import hub
# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/openai-functions-agent")
# print(prompt.messages)


# we can initalize the agent with the LLM, the prompt, and the tools.

from langchain.agents import create_openai_functions_agent

agent = create_openai_functions_agent(llm, tools, prompt)

# we combine the agent (the brains) with the tools inside the AgentExecutor

from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
# output=agent_executor.invoke({"input": "hi!"})
# print(output)

# print(agent_executor.invoke({"input": "whats the weather in sf?"}))


# Adding in memory
# Here we pass in an empty list of messages for chat_history because it is the first message in the chat
output=agent_executor.invoke({"input": "hi! my name is bob", "chat_history": []})
print(output)