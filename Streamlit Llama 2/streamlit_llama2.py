# conda activate llamaChat
# cd "C:\Users\014206631\Python\Llama chat\Streamlit Llama 2"
# streamlit run streamlit_llama2.py

import streamlit as st 
from langchain_community.llms import LlamaCpp
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

class llama2Chat:
    def __init__(self, system_prompt):
        # first initialize the parameters for the large language model
        self.model_path = '..\models\llama-2-7b-chat.Q8_0.gguf'  # https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF
        self.temperature = 0
        self.top_p = 1
        self.max_new_tokens = 500
        self.system_prompt = system_prompt
      
    def instantiate_llm(_self):
        # Initialize the LLM
        _self.llm = LlamaCpp(
                    model_path = _self.model_path,
                    temperature = _self.temperature,
                    max_tokens = _self.max_new_tokens,
                    top_p = _self.top_p,
                    n_gpu_layers = -1,
                    n_batch = 512, # Should be between 1 and n_ctx, consider the amount of RAM
                    n_ctx = 4096,
                    f16_kv = True,  # MUST set to True, otherwise you will run into problem after a couple of calls
                    verbose = True, # Verbose is required to pass to the callback manager
                )
        
    def setup_chain(_self, system_prompt):
        # Set conversation chain
        _self.system_prompt = system_prompt
        prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(
                    _self.system_prompt
                ),
                # The `variable_name` here is what must align with memory
                MessagesPlaceholder(variable_name = "chat_history"),
                HumanMessagePromptTemplate.from_template("{question}")
            ]
        )
        memory = ConversationBufferMemory(memory_key = "chat_history", return_messages= True)
        _self.conversation = LLMChain(
            llm = _self.llm,
            prompt = prompt,
            verbose = False,
            memory = memory
        )

    def answer_prompt(_self, user_prompt):
        # Return LLM answer.
        _self.answer = _self.conversation({"question": user_prompt})   


@st.cache_resource # Everythime something changes in the screen, streamlit runs all the script again. This modifier avoid this.
def load_chat(system_prompt):
    llamaChatObj = llama2Chat(system_prompt)
    llamaChatObj.instantiate_llm()
    llamaChatObj.setup_chain(system_prompt)
    return llamaChatObj

if __name__ == "__main__":

    default_system_prompt = """You are a helpful, respectful and honest assistant. 
    Always answer as helpfully as possible.  
    If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. 
    If you don't know the answer to a question, please don't share false information."""
    
    # llamaChatObj = load_chat(default_system_prompt)
    if 'chat_input_placeholder' not in st.session_state:
        st.session_state['llamaChatObj'] = load_chat(default_system_prompt) # Values in this dictionary are not reseted when something changes in the screen.
    
    st.header('Chat with your computer. \nAI powerd by Llama 2.')
    st.markdown('---')
    
    with st.container(): 
        st.write("""System message is used to prime the chat with context, instructions, or other information relevant to your use case. You can use the system message to describe the assistant’s personality, define what it should and shouldn’t answer, and define the format of the responses.
\nSystem message:""")
        # Add possibility to change system message
        new_system_prompt = st.chat_input(placeholder = "Type a new system message? If you change it, the chat history will be lost.")
        if new_system_prompt:
            st.session_state['llamaChatObj'].setup_chain(new_system_prompt)
        st.write(st.session_state['llamaChatObj'].system_prompt)
    
    st.markdown('---')
    with st.container(): 
        user_prompt = st.chat_input(placeholder = "What is in your mind?")
        if user_prompt:
            st.session_state['llamaChatObj'].answer_prompt(user_prompt)
            st.write(st.session_state['llamaChatObj'].answer["text"])
            st.markdown('---')
            
            with st.expander('Click here to display chat history.'):
                for i in range(len(st.session_state['llamaChatObj'].answer["chat_history"])):
                    if i%2 == 0:
                        st.write(f"User: {st.session_state['llamaChatObj'].answer['chat_history'][i].content}")
                    else:
                        st.write(st.session_state['llamaChatObj'].answer['chat_history'][i].content)
                        st.markdown('---')




# To test:
# Tell me a slightly funny story.
# yes, please share one with me?