from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools

def get_company_symbol(company: str) -> str:
    """
    Use this function to get the symbol for a company
    Args:
        company (str): The name of the company
    Returns:
        str: The symbol for the company
    """
    symbols={
        "AIwithHassan": "AAPL",
        "Tesla": "TSLA",
        "Google": "GOOGL"
    }
    return symbols.get(company, "Unknown")



test_agent=Agent(
    #model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True
        ), get_company_symbol],
    show_tool_calls=True,
    markdown=True,
    instructions=["Always take the symbols from the get_company_symbol tool and only use that symbol for further analysis, if the symbol doesnot exist, abort",
                  "Always create tables for comparisons"],
    debug_mode=True
)

test_agent.print_response("Summarise and compare the analyst recommendations for the stocks of AIwithHassan and Tesla")

