from agents.web_search_agent import search_agent

def main():
    print("=== Gemini Web Search Bot (with Tavily) ===")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye 👋")
            break

        response = search_agent.run(user_input)
        print("Bot:", response, "\n")

if __name__ == "__main__":
    main()
