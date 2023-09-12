import streamlit as st
from gradio_client import Client

# Headings
st.markdown("# Welcome to Summarizer-Pro")
st.write("Hi! I am your Assistant Summarizer! Give me any text and I'm going to summarize it for you!")

# Create a summarizer model
if "gradio-model" not in st.session_state:
    st.session_state["gradio-model"] = 'summarizer-101'

# Create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history when app is rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown("content")

# Accept user input for chat
if prompt := st.chat_input("Enter text to be summarized"):

    # Add user input to chat history
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    # Display user message in chat container
    with st.chat_message('user'):
        st.markdown(prompt)

    # Display summarizer response in chat container
    with st.chat_message('assistant'):
        message_placeholder = st.empty()
        full_response = " "
        # Get summary from Summarizer
        client = Client("https://theosphil-meta-llama-llama-2-13b-hf.hf.space/")
        result = client.predict(
                        prompt,	 # str in 'Input' Textbox component
                        api_name="/predict"
        )
        full_response += result
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({'role': 'assistant', 'content': full_response})
