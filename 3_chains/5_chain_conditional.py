from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnableSequence


load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

positive_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("human", "Generae a thank you message for the positive feedback: {feedback}")
    ]
)

negative_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("human", "Generae an apology message for the negetive feedback: {feedback}")
    ]
)

neutral_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("human", "Generae a neutral response for the neutral feedback: {feedback}")
    ]
)

escalate_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("human", "Escalate the following feedback to a human agent: {feedback}")
    ]
)

classfication_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("human", "Classify the following feedback as positive, negative, neutral, or escalate: {feedback}")
    ]
)

branches = RunnableBranch(
    (
        lambda x: "positive" in x,
        positive_feedback_template | model | StrOutputParser(),
    ),
    (
        lambda x: "negetive" in x,
        negative_feedback_template | model | StrOutputParser(),
    ),
    (
        lambda x: "neutral" in x,
        neutral_feedback_template | model | StrOutputParser(),
    ),
    escalate_feedback_template | model | StrOutputParser(),
)

classification_chain = classfication_template | model | StrOutputParser()

chain = classification_chain | branches

result = chain.invoke({"feedback": "The product is excellent. I really enjoyed using it and found it very helpful."})

print(result)