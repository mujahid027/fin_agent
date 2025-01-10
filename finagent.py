from phi.model.groq import Groq
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key  = os.getenv("GROQ_API_KEY")

# web search agent
web_search_agent = Agent(
    name ="web search agent",
    role = "search the web for information",
    model =  Groq(id = "Llama-3.3-70b-versatile",api_key="groq_api_key"),
    tools = [DuckDuckGo()],
    instructions = ["always provide source"],
    show_tools_calls= True,
    markdown = True
)

#finacial agent
financial_agent = Agent(
    name = "financial agent",
    model =  Groq(id = "Llama-3.3-70b-versatile",api_key="groq_api_key"),
    tools =[YFinanceTools(stock_price = True , analyst_recommendations = True ,
                           stock_fundamentals = True ,company_news = True,technical_indicators = True)],
    instructions = ["use table to show data"],
    show_tools_calls = True,
    markdown = True
)

#multi ai agent
multi_ai_agent = Agent(
    team = [web_search_agent,financial_agent],
    model =  Groq(id = "Llama-3.3-70b-versatile",api_key="groq_api_key"),
    instructions=["always show sources","use tables to show data"],
    show_tools_calls = True,
    markdown = True
)

multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)
