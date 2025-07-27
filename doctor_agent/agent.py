import os
import requests
from typing import Optional
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

from dotenv import load_dotenv

load_dotenv()

def search_medical_info(query: str) -> dict:
    """Search for medical information using Google Programmable Search API.
    
    Args:
        query (str): The medical query to search for.
        
    Returns:
        dict: Search results or error message.
    """
    try:
        # Get API key from environment variable
        api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
        search_engine_id = os.getenv("GOOGLE_SEARCH_ENGINE_ID")
        
        if not api_key or not search_engine_id:
            return {
                "status": "error",
                "error_message": "Google Search API credentials not configured. Please set GOOGLE_SEARCH_API_KEY and GOOGLE_SEARCH_ENGINE_ID environment variables."
            }
        
        # Google Custom Search API endpoint
        url = "https://customsearch.googleapis.com/customsearch/v1"
        
        params = {
            "key": api_key,
            "cx": search_engine_id,
            "q": query,
            "num": 5  # Number of results to return
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        if "items" in data:
            results = []
            for item in data["items"]:
                results.append({
                    "title": item.get("title", ""),
                    "snippet": item.get("snippet", ""),
                    "link": item.get("link", "")
                })
            
            return {
                "status": "success",
                "results": results,
                "query": query
            }
        else:
            return {
                "status": "success",
                "results": [],
                "message": "No results found for the query."
            }
            
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "error_message": f"Failed to search: {str(e)}"
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"An error occurred: {str(e)}"
        }


def get_medical_guidelines(condition: str) -> dict:
    """Get medical guidelines for a specific condition.
    
    Args:
        condition (str): The medical condition to search for guidelines.
        
    Returns:
        dict: Medical guidelines or error message.
    """
    query = f"medical guidelines treatment {condition}"
    return search_medical_info(query)


def get_drug_information(drug_name: str) -> dict:
    """Get information about a specific drug or medication.
    
    Args:
        drug_name (str): The name of the drug to search for.
        
    Returns:
        dict: Drug information or error message.
    """
    query = f"drug information side effects dosage {drug_name}"
    return search_medical_info(query)


def get_symptom_analysis(symptoms: str) -> dict:
    """Analyze symptoms and provide potential causes.
    
    Args:
        symptoms (str): Description of symptoms to analyze.
        
    Returns:
        dict: Symptom analysis or error message.
    """
    query = f"symptoms causes diagnosis {symptoms}"
    return search_medical_info(query)


def get_emergency_advice(emergency: str) -> dict:
    """Get emergency medical advice for urgent situations.
    
    Args:
        emergency (str): Description of the emergency situation.
        
    Returns:
        dict: Emergency advice or error message.
    """
    query = f"emergency medical advice first aid {emergency}"
    return search_medical_info(query)


def get_health_tips(category: str) -> dict:
    """Get general health tips for a specific category.
    
    Args:
        category (str): Health category (e.g., nutrition, exercise, mental health).
        
    Returns:
        dict: Health tips or error message.
    """
    query = f"health tips {category} wellness"
    return search_medical_info(query)


root_agent = Agent(
    name="doctor_agent",
    model="gemini-2.5-flash",
    description=(
        "A medical assistant agent that can search for medical information, "
        "provide health advice, analyze symptoms, and offer medical guidance "
        "using internet search capabilities."
    ),
    instruction=(
        "You are a helpful medical assistant agent who can answer user questions "
        "about health, medical conditions, medications, and provide general "
        "medical information. You can search the internet for the latest medical "
        "information and guidelines. Always remind users that you are not a "
        "substitute for professional medical advice and encourage them to consult "
        "with healthcare professionals for serious medical concerns."
    ),
    tools=[
        search_medical_info,
        get_medical_guidelines,
        get_drug_information,
        get_symptom_analysis,
        get_emergency_advice,
        get_health_tips
    ],
)