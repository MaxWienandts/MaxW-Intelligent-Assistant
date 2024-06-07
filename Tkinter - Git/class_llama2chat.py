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
        self.model_path = 'models\llama-2-7b-chat.Q8_0.gguf'  # https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF
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