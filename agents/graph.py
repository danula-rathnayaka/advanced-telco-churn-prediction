from dotenv import load_dotenv
from langchain_groq import ChatGroq

from prompts import *
from states import *

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-120b")

user_prompt = "Create a calculator application"

prompt = planner_prompt(user_prompt)
print(llm.with_structured_output(Plan).invoke(prompt))
