import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def tavily_search(query: str, max_results: int = 3):
    """Fetch search results from Tavily API."""
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
        raise Exception(f"Error {response.status_code}: {response.text}")


# Example test
if __name__ == "__main__":
    query = "Latest AI trends 2025"
    search_results = tavily_search(query)
    for i, result in enumerate(search_results, start=1):
        print(f"{i}. {result['title']}")
        print(result['url'])
        print(result['content'][:150], "...\n")
