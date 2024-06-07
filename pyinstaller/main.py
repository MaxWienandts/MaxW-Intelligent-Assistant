# conda activate llamaChat
# cd "C:\Users\014206631\Python\Llama chat\pyinstaller"
# python main.py

import streamlit as st 
import langchain_community
# import LlamaCpp
from langchain_community.llms import LlamaCpp
# from llamacpp import LlamaCpp  # PyInstaller could not find LlamaCpp from langchain_community.llms.

from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

import langchain_core
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from streamlit.web import cli 
#this uri depends based on version of your streamlit
if __name__ == '__main__':
    cli._main_run_clExplicit('streamlit_llama2.py', 'streamlit run')