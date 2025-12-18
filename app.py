import streamlit as st
import requests
from datetime import datetime

# Page configuration with custom theme
st.set_page_config(
    page_title="Customer Support AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
    <style>
    /* Main background gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Chat container styling */
    .stChatMessage {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Input box styling */
    .stChatInputContainer {
        border-radius: 25px;
        background-color: rgba(255, 255, 255, 0.9);
        padding: 10px;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] li {
        color: white !important;
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 25px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
    }
    
    /* Title styling */
    h1 {
        color: white;
        text-align: center;
        font-size: 3em;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        margin-bottom: 10px;
    }
    
    /* Subtitle styling */
    .subtitle {
        color: white;
        text-align: center;
        font-size: 1.2em;
        margin-bottom: 30px;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
    }
    
    /* Chat container */
    .chat-container {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 20px;
        margin: 20px auto;
        max-width: 800px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    
    /* Feature cards */
    .feature-card {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    /* Status indicators */
    .status-online {
        color: #00ff00;
        font-weight: bold;
    }
    
    .status-offline {
        color: #ff4444;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>🤖 AI Customer Support</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Your 24/7 Intelligent Assistant</p>", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Welcome message
    st.session_state.messages.append({
        "role": "assistant",
        "content": "👋 Hello! I'm your AI customer support assistant. How can I help you today?"
    })

# Sidebar
with st.sidebar:
    st.markdown("### 🎯 Quick Actions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🕐 Working Hours", use_container_width=True):
            prompt = "What are your working hours?"
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.rerun()
    
    with col2:
        if st.button("📦 Track Order", use_container_width=True):
            prompt = "I want to track my order"
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.rerun()
    
    if st.button("💰 Request Refund", use_container_width=True):
        prompt = "I need a refund"
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.rerun()
    
    st.markdown("---")
    
    # Features section
    st.markdown("### ✨ Features")
    st.markdown("""
    <div class='feature-card'>
        <strong>🎯 Smart Responses</strong><br>
        Powered by advanced AI
    </div>
    <div class='feature-card'>
        <strong>⚡ Instant Help</strong><br>
        Get answers in seconds
    </div>
    <div class='feature-card'>
        <strong>🌐 Always Available</strong><br>
        24/7 support
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Status check
    st.markdown("### 📊 System Status")
    try:
        health_check = requests.get("http://localhost:5005/", timeout=2)
        if health_check.status_code == 200:
            st.markdown("<p class='status-online'>● Online</p>", unsafe_allow_html=True)
            st.success("All systems operational")
        else:
            st.markdown("<p class='status-offline'>● Offline</p>", unsafe_allow_html=True)
            st.error("Chatbot unavailable")
    except:
        st.markdown("<p class='status-offline'>● Offline</p>", unsafe_allow_html=True)
        st.error("Connection failed")
    
    st.markdown("---")
    
    # Clear chat button
    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.messages.append({
            "role": "assistant",
            "content": "👋 Hello! I'm your AI customer support assistant. How can I help you today?"
        })
        st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown(f"<small>Last updated: {datetime.now().strftime('%H:%M')}</small>", unsafe_allow_html=True)

# Main chat area with container
with st.container():
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    
    # Display chat messages
    for message in st.session_state.messages:
        avatar = "🧑" if message["role"] == "user" else "🤖"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])
    
    st.markdown("</div>", unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("💬 Type your message here..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get bot response
    with st.spinner("🤔 Thinking..."):
        try:
            response = requests.post(
                "http://localhost:5005/webhooks/rest/webhook",
                json={"sender": "streamlit_user", "message": prompt},
                timeout=10
            )
            
            if response.status_code == 200 and response.json():
                bot_message = response.json()[0].get("text", "I didn't understand that.")
            else:
                bot_message = "⚠️ I'm having trouble connecting right now. Please make sure the Rasa server is running."
                
        except requests.exceptions.Timeout:
            bot_message = "⏱️ Request timed out. The server might be busy. Please try again."
        except Exception as e:
            bot_message = f"❌ Connection error. Please ensure:\n1. Rasa server is running on port 5005\n2. Actions server is running on port 5055"
        
        st.session_state.messages.append({"role": "assistant", "content": bot_message})
    
    st.rerun()

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("🔒 **Secure**")
with col2:
    st.markdown("⚡ **Fast**")
with col3:
    st.markdown("🎯 **Accurate**")