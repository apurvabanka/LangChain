from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain.agents import tool
from datetime import datetime

load_dotenv()

@tool
def get_current_time():
    """Get the current time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

llm = ChatOpenAI(model="gpt-4o-mini")

query = "What is the current date and time?"

prompt_template = hub.pull("hwchase17/react")

tools = [get_current_time]

agents = create_react_agent(llm, tools, prompt_template)

agent_executor = AgentExecutor(agent=agents, tools=tools, verbose=True)

result = agent_executor.invoke({"input": query})
