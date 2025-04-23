# AI Chat Agent with LangGraph and Groq

## Project Overview

This project implements a conversational AI agent using LangGraph, Groq's LLM API, and Tavily search functionality. The system provides a web-based chat interface with configurable AI roles and web search capabilities.

## Key Features

- **Multi-role AI Chatbot**: Choose from 8 different professional roles (financial adviser, travel guide, etc.)
- **Web Search Integration**: Optional real-time web search for up-to-date information
- **Fast Backend API**: Built with FastAPI for high performance
- **Streamlit Frontend**: Clean, interactive chat interface
- **Serverless Ready**: Includes Mangum handler for Vercel deployment
- **LangGraph Agent**: Uses the latest agent architecture for intelligent responses

## Technology Stack

- **Backend**: FastAPI, Pydantic, Uvicorn
- **AI**: LangGraph, Groq API (Llama3-8b), Tavily Search
- **Frontend**: Streamlit

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-chat-agent.git
   cd ai-chat-agent


2. Set up the environment:
   ```bash
   pip install pipenv  # If you don't have pipenv installed
   pipenv install
   pipenv install -r requirements.txt
   pipenv shell


3. Run the backend server:
   ```bash
   python backend.py  # This will start the Uvicorn server


4. In a new terminal (while keeping backend running), run the frontend:
   ```bash
   pipenv shell  # If not already in the virtual environment
   streamlit run frontend.py

