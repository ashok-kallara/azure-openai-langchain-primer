from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import AzureOpenAI
from langchain.agents import AgentType
from langchain.tools import DuckDuckGoSearchRun

from settings import configOpenAI

configOpenAI()
llm = AzureOpenAI(deployment_name="text-davinci-003-dev1", model_name="text-davinci-003", temperature=0)

# Load the tools
tools = [DuckDuckGoSearchRun()]

# Initialize an agent with the tools, the language model, and the type of agent we want to use.
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Now let's test it out!
agent.run("What's the weather like tomorrow?")