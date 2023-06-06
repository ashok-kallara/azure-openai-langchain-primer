from langchain.chains import LLMChain
from langchain.llms import AzureOpenAI
from langchain.prompts import PromptTemplate

from settings import configOpenAI

configOpenAI()
llm = AzureOpenAI(deployment_name="text-davinci-003-dev1", model_name="text-davinci-003", temperature=0)

prompt = PromptTemplate(
    input_variables=["joke_type"],
    template="Tell me a {joke_type} joke.",
)

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("azure openai hackathon"))