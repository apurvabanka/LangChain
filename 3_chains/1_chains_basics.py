from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system', "You are an expert that knows facta about animals"),
        ('human', "Give me {fact_number} facts about {animal}"),
    ]
)

chain = prompt_template | model | StrOutputParser() #we were able to chain the 

result = chain.invoke({'animal': "elephant", 'fact_number': 3})

print(result)