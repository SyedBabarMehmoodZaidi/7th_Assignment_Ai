class Agent:
    def __init__(self, name, instructions, model, tools=[]):
        self.name = name
        self.instructions = instructions
        self.model = model
        self.tools = tools

    def run(self, query: str):
       
        if self.tools:
            tool = self.tools[0]  
            return tool(query)
        else:
            return f"[{self.name}] No tools available. Query: {query}"
