import os

from dotenv import load_dotenv
from fastapi import FastAPI
from google.adk.cli.fast_api import get_fast_api_app


# Load environment variables from .env file
load_dotenv()

AGENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Prepare arguments for get_fast_api_app
app_args = {"agents_dir": AGENT_DIR, "web": True}

# Create FastAPI app with appropriate arguments
app: FastAPI = get_fast_api_app(**app_args)

app.title = "doctor-agent"
app.description = "API for interacting with the Doctor Agent - a medical assistant with internet search capabilities"


# Main execution
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)