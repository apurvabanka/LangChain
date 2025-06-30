from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableSequence

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system', "You are an expert that knows facta about animals"),
        ('human', "Give me {fact_number} facts about {animal}"),
    ]
)

transaltion_template = ChatPromptTemplate.from_messages(
    [
        ('system', "You are an expert that knows how to translate text"),
        ('human', "Translate the following text to {language}: {text}"),
    ]
)

prepare_translation = RunnableLambda(
    lambda output: {'text': output, 'language': 'Spanish'}
)

chain = prompt_template | model | StrOutputParser() | prepare_translation | transaltion_template | model | StrOutputParser()

result = chain.invoke({'animal': "elephant", 'fact_number': 3})

print(result)