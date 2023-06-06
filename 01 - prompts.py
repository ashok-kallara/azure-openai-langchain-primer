from langchain.llms import AzureOpenAI

from settings import configOpenAI

configOpenAI()
llm = AzureOpenAI(deployment_name="text-davinci-003-dev1", model_name="text-davinci-003", temperature=0)
text = "Tell me a hackathon joke"

print(llm(text))