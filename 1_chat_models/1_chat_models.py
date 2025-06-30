from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


llm = ChatOpenAI(model="gpt-4o-mini")

llm.invoke("") # This is the maagic key work to interact with the LLM


result = llm.invoke("What is the capital of France?")

print(result.content)