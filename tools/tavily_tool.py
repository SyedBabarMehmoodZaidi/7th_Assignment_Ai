import os
import requests
from dotenv import load_dotenv

load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def tavily_search(query: str, max_results: int = 3):
    """Fetch results from Tavily API."""
    url = "https://api.tavily.com/search"
    headers = {"Content-Type": "application/json"}
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "max_results": max_results,
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        results = response.json()
        return results.get("results", [])
    else:
        return [{"error": f"Error {response.status_code}: {response.text}"}]
