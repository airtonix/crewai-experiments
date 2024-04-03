
from crewai import Agent

from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool

from core.tools.browser_tools import SoupScraperTools
from core.tools.search_tools import GoogleSoupSearchTools
from core.tools.math_tools import CalculatorTools


def create_agent():
  return Agent(
    role='Private Investment Advisor',
    goal="""Impress your customers with full analyses over stocks
    and completer investment recommendations""",
    backstory="""You're the most experienced investment advisor
    and you combine various analytical insights to formulate
    strategic investment advice. You are now working for
    a super important customer you need to impress.""",
    verbose=True,
    tools=[
      SoupScraperTools.scrape_and_summarize_website,
      GoogleSoupSearchTools.search_internet,
      GoogleSoupSearchTools.search_news,
      CalculatorTools.calculate,
      YahooFinanceNewsTool()
    ]
  )
