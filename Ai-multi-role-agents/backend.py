# Step 1: Setup Pydantic Model (Schema Validation)
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

# Step 2: Setup FastAPI App
ALLOWED_MODEL_NAMES = ["llama3-8b-8192"]
app = FastAPI(title="LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}
    
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    # Create AI Agent and get response
    try:
        response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
        return response
    except Exception as e:
        return {"error": f"Failed to get response from AI agent: {str(e)}"}

# Step 3: Serverless Handler for Vercel
try:
    import mangum
except ImportError:
    mangum = None

if mangum:
    from mangum import Mangum
    handler = Mangum(app, lifespan="off")

# Step 4: Run Locally with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=1000)