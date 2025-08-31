from .agent import Agent       
from my_config.gemini_config import GEMINI_MODEL
from tools.tavily_tool import tavily_search


def tavily_tool(query: str):
    results = tavily_search(query, max_results=5)
    formatted = "\n\n".join(
        [f"{i+1}. {r['title']}\n{r['url']}\n{r['content'][:200]}..."
         for i, r in enumerate(results)]
    )
    return formatted


search_agent = Agent(
    name="Gemini Web Search Bot",
    instructions="You are a helpful assistant. Use Tavily tool for real-time web information.",
    model=GEMINI_MODEL,
    tools=[tavily_tool]
)
