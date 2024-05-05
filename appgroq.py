import os
from typing import List

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import (
    ConversationalRetrievalChain,
)
from langchain_groq import ChatGroq

from langchain.docstore.document import Document
from langchain.memory import ChatMessageHistory, ConversationBufferMemory

import chainlit as cl

print("all_ok")

from dotenv import load_dotenv

load_dotenv() 

GROQAI_API_KEY=os.getenv("GROQAI_API_KEY")

os.environ["GROQAI_API_KEY"] = GROQAI_API_KEY

