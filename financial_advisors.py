from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

financial_agent=Agent(
    name="Financial Analyst",
    #model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True
        )],
    show_tool_calls=True,
    markdown=True,
    instructions=["Always create tables for comparisons"],
)


web_researcher=Agent(
    name="Web Researcher",
    #model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
    instructions=["Always include sources of the information that you gather"],
)


agents_team=Agent(
    team=[financial_agent, web_researcher],
    #model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o-mini"),
    show_tool_calls=True,
    markdown=True,
    instructions=["Always include source of the information gathered", "Always create tables for comparisons"],
    debug_mode=True
)

agents_team.print_response("Summarise the analyst recommendations and share the latest information about Nvidia?")