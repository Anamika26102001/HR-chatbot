import streamlit as st
import requests
import json

# Page config
st.set_page_config(
    page_title="HR Resource Query Chatbot",
    page_icon="👥",
    layout="wide"
)

# Title
st.title("HR Resource Query Chatbot 👥")
st.markdown("""
This chatbot helps you find the right employees based on your requirements.
Try asking questions like:
- Find Python developers with 3+ years experience
- Who has worked on healthcare projects?
- Suggest people for a React Native project
""")

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Chat input
query = st.chat_input("Ask about employee skills, experience, or projects...")

# Backend API URL
API_URL = "http://localhost:8000"

if query:
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": query})
    
    # Send query to backend
    try:
        response = requests.post(
            f"{API_URL}/chat",
            json={"query": query}
        )
        
        if response.status_code == 200:
            result = response.json()
            # Add assistant response to chat
            st.session_state.messages.append({"role": "assistant", "content": result["message"]})
        else:
            st.error(f"Error: {response.text}")
            
    except Exception as e:
        st.error(f"Error connecting to backend: {str(e)}")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Sidebar with information
with st.sidebar:
    st.header("About")
    st.markdown("""
    This HR Resource Query Chatbot uses advanced AI to help you find the right employees based on:
    - Skills
    - Experience
    - Project history
    - Availability
    
    The system uses:
    - Natural Language Processing
    - Semantic Search
    - RAG (Retrieval Augmented Generation)
    """)
    
    # Add example queries
    st.header("Example Queries")
    example_queries = [
        "Find Python developers with 3+ years experience",
        "Who has worked on healthcare projects?",
        "Show me available React developers",
        "Find developers who know both AWS and Docker",
        "Who has machine learning experience?"
    ]
    
    for query in example_queries:
        if st.button(query):
            # Add user message to chat
            st.session_state.messages.append({"role": "user", "content": query})
            try:
                response = requests.post(
                    f"{API_URL}/chat",
                    json={"query": query}
                )
                
                if response.status_code == 200:
                    result = response.json()
                    st.session_state.messages.append({"role": "assistant", "content": result["message"]})
                    st.rerun() 
            except Exception as e:
                st.error(f"Error connecting to backend: {str(e)}") 