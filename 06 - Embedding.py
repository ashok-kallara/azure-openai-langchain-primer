from click.core import batch
from langchain import OpenAI, ConversationChain
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import AzureOpenAI

from settings import configOpenAI

configOpenAI()
embeddings = OpenAIEmbeddings(chunk_size=1)

issue_desc_embeddings = embeddings.embed_documents(["Hello World!", "Make trust your competitive advantage"])

print(issue_desc_embeddings)