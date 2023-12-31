import streamlit as st
from gradio_client import Client

# Headings
st.markdown("# Welcome to Summarizer-Pro")
st.write("Hi! I am your Assistant Summarizer! Give me any text and I'm going to summarize it for you!")

# Create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history when app is rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input for chat
if prompt := st.chat_input("Enter text to be summarized"):

    # Add user input to chat history
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    # Display user message in chat container
    with st.chat_message('user'):
        st.markdown(prompt)

    # Display summarizer response in chat container
    with st.chat_message('assistant'):
        message_placeholder = st.markdown("Summarizing... |")
        full_response = " "
        # Get summary from Summarizer
        try:
            client = Client("https://theosphil-facebook-bart-large-cnn.hf.space/")
            result = client.predict(
                            prompt,	 # str in 'Input' Textbox component
                            api_name="/predict"
            )
            full_response += result
            message_placeholder.markdown(full_response)
        except:
            full_response = "Error while generating summary. Try checking your connection or reload browser."
            message_placeholder.markdown(full_response)

    # Add summarizer reply to chat history
    st.session_state.messages.append({'role': 'assistant', 'content': full_response})
