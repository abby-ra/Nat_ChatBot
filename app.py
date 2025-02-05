import streamlit as st
from langchain_ollama import ChatOllama
# from langchain.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate


from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

from langchain_core.output_parsers import BaseOutputParser


class CustomOutputParser(BaseOutputParser):
    def parse(self, text: str):
        return text


# Custom CSS styling
st. markdown("""
<style>
    / * Existing styles * /
    .main { 
        background-color: #lalala;
        color: #ffffff;
    }
    . sidebar . sidebar-content {
        background-color: #2d2d2d;
    }
    . stTextInput textarea {
        color: #ffffff ! important;
    }
    
    / * Add these new styles for select box * /
    
    .stSe1ectbox div[data-baseweb="select"] {
        color: white ! important;
        background-color: #3d3d3d ! important;
    }
    .stSe1ectbox svg {
        fill: white ! important;
    }
    . stSe1ectbox option {
        background-color: #2d2d2d ! important;
        color: white ! important;
    }
    
    .stSe1ectbox svg {
        fill: white ! important;
    }
    .stSe1ectbox option {
        background-color: #2d2d2d ! important;
        color: white ! important;
    }
    
    / * For dropdown menu items * /
    
    div[role="listbox"] div {
        background-color: #2d2d2d ! important;
        color: white ! important;
    }
</style>
""", unsafe_allow_html=True)

st.title("DeepSeek Code Companion")
st.caption("Your AI Pair Programmer with Debugging Superpowers")
# Sidebar configuration

# with st.sidebar:
#     st.header( " Configuration " )
#     selected_model= st.selectbox(
#         "Choose Model" ,
#         [ "deepseek-rl:1.5b" ,  "deepseek-rl : 3btI" ],
#         index=0
#     )
#     st.divider()
#     st.markdown( "### Model Capabilities")
#     st . markdown("""
#         -Python Expert
#         - Debugging Assistant
#         -Code Documentation
#         -Solution Design
#     """)
#     st.divider()
#     st.markdown("Bui1t with [01 lama] (https://ollama.ai/) | [ LangChain] (https : / / python . langchain.com/) " )


with st.sidebar:
    st.header("Configuration")
    selected_model = st.selectbox(
        "Choose Model",
        ["deepseek-r1:latest"],  # Use the correct model name
        index=0
    )
    # st.divider()
    st.markdown( "### Model Capabilities")
    st . markdown("""
        -Python Expert
        - Debugging Assistant
        -Code Documentation
        -Solution Design
    """)

#initiate the chat engine
llm_engine = ChatOllama(
    model=selected_model,  
    base_url="http://localhost:11434",
    temperature=0.3
)


#System prompt configuration

system_prompt = SystemMessagePromptTemplate.from_template(
    "Your system message here..."
)

# Session state management

if "message_log" not in st.session_state:
    st.session_state.message_log = [ {"role": "ai" ,"content": "Hi! I'm DeepSeek.How can I help you to code"} ]
    
    
#chat container

chat_container = st.container()

#Display chat messages

with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
            
# Chat input and processing
user_query = st.chat_input("Type your coding question here...")

def generate_ai_response (prompt_chain):
    processing_pipeline = prompt_chain | llm_engine | CustomOutputParser()
    return processing_pipeline.invoke({})

def build_prompt_chain():
    prompt_sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user" :
            prompt_sequence.append(HumanMessagePromptTemp1ate.from_template(msg["content"]))
        elif msg["role"] == "ai" :
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
        return ChatPromptTemplate.from_messages(prompt_sequence)

if user_query:
    # Add eser message to log 
    st.session_state.message_log.append({"role": "user", "content" : user_query}) 
    # Generate AI response
    with st.spinner(" Processing... "):
        prompt_chain= build_prompt_chain()
        ai_response = generate_ai_response(prompt_chain)
    # Add AI response to log
    st.session_state.message_log.append({"role": "ai", "content": ai_response})
    # Rerun to update chat display
    st.rerun()
