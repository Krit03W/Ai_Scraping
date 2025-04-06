from langchain.agents import initialize_agent, AgentType
from langchain.chains.conversation.memory import ConversationBufferMemory
from tools.web_scraper_tool import web_scraper_tool
from llm.gemini import GeminiLLM

def build_agent():
    memory = ConversationBufferMemory(memory_key="chat_history")
    llm = GeminiLLM()
    agent = initialize_agent(
        tools=[web_scraper_tool],
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True,
        memory=memory
    )
    return agent
