from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

template = """Write a {tone} email to {company} expressing 
intrest in the {position} position, mentioning my skills in 
{skills} as a key strength. Keep it to 4 lines max"""

prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.format(
    tone="professional",
    company="Google",
    position="Software Engineer",
    skills="Python and Machine Learning"
)

result = llm.invoke(prompt)

print(result.content)