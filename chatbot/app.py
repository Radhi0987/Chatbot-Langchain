#LANGCHAIN_API_KEY="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"
#OPENAI_API_KEY="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"
#LANGCHAIN_PROJECT="llm1"

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st 
import os
from dotenv import load_dotenv

load_dotenv()

## environment variables call

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
##Langsmith tracking

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

##creating chatbot

prompt=ChatPromptTemplate. from_messages(
    [
        ("system","you are a helpful assistant. please provide response to user queries"),
        ("user","Question:{question}")
    ]
)

#Streanlit framework
st.title("Langchain demo with open ai api")
input_text=st.text_input("search the topic you want")

#open AI LLM call
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()

##chain
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))