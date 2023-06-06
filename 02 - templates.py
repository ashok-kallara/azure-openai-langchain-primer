from langchain.prompts import PromptTemplate

from settings import configOpenAI

configOpenAI()
prompt = PromptTemplate(
    input_variables=["joke_type"],
    template="Tell me a {joke_type} joke.",
)

print(prompt.format(joke_type="openai hackathon"))