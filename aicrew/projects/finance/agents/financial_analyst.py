
from crewai import Agent

from core.tools.browser_tools import SoupScraperTools
from core.tools.search_tools import GoogleSoupSearchTools
from core.tools.math_tools import CalculatorTools
from aicrew.projects.finance.tools import sec_tools

def create_agent():
  return Agent(
    role='The Best Financial Analyst',
    goal="""Impress all customers with your financial data
    and market trends analysis""",
    backstory="""The most seasoned financial analyst with
    lots of expertise in stock market analysis and investment
    strategies that is working for a super important customer.""",
    verbose=True,
    tools=[
      SoupScraperTools.scrape_and_summarize_website,
      GoogleSoupSearchTools.search_internet,
      CalculatorTools.calculate,
      sec_tools.search_10q,
      sec_tools.search_10k
    ]
  )
