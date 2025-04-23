import streamlit as st
import requests
import time

# Set up the page
st.set_page_config(page_title="AI Chat Agent", layout="centered")
st.write("💬 AI Chat Agent")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for settings
with st.sidebar:
    st.header("⚙️ Settings")
    
    # System prompt selection
    SYS_PROMPTS = [
        "Act as a financial adviser",
        "Act as a travel guide", 
        "Act as a personal trainer",
        "Act as a chef",
        "Act as a therapist",
        "Act as a teacher",
        "Act as a lawyer",
        "Act as a doctor"
    ]
    selected_prompt = st.selectbox("Select AI Role:", SYS_PROMPTS)
    
   
    provider = st.radio("AI Provider:", ("Groq",))
    if provider == "Groq":
        selected_model = st.selectbox("Model:", ["llama3-8b-8192"])
    
    # Features
    st.subheader("Features")
    allow_web_search = st.checkbox("Enable Web Search", value=True)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Prepare API request
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": selected_prompt,
            "messages": [prompt],
            "allow_search": allow_web_search
        }
        
        try:
            with st.spinner("Thinking..."):
                response = requests.post(
                    "http://127.0.0.1:1000/chat",
                    json=payload,
                    timeout=30
                )
                
                if response.status_code == 200:
                    response_data = response.json()
                    
                    if "error" in response_data:
                        full_response = f"❌ Error: {response_data['error']}"
                    else:
                        # Stream the response
                        for chunk in response_data.split():
                            full_response += chunk + " "
                            time.sleep(0.05)
                            message_placeholder.markdown(full_response + "▌")
                        
                        message_placeholder.markdown(full_response)
                else:
                    full_response = f"API Error: {response.status_code}"
                    message_placeholder.markdown(full_response)
                    
        except Exception as e:
            full_response = f"Connection error: {str(e)}"
            message_placeholder.markdown(full_response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})