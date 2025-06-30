from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

messsages = [
    SystemMessage(content="You are a programming expert."),
    HumanMessage(content="What is the time complexity of merge sort?")
]

result = llm.invoke(messsages)

print(result.content)