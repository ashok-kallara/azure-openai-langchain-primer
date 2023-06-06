from langchain import OpenAI, ConversationChain
from langchain.llms import AzureOpenAI

from settings import configOpenAI

configOpenAI()
llm = AzureOpenAI(deployment_name="text-davinci-003-dev1", model_name="text-davinci-003", temperature=0)

conversation = ConversationChain(llm=llm, verbose=True)

conversation.predict(input="Hi there!")

conversation.predict(input="I'm doing well! Just having a conversation with an AI.")