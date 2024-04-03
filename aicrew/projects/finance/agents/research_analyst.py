
from crewai import Agent

from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool

from core.tools.browser_tools import SoupScraperTools
from core.tools.search_tools import GoogleSoupSearchTools
from aicrew.projects.finance.tools import sec_tools

def create_agent():
  return Agent(
    role='Staff Research Analyst',
    goal="""Being the best at gather, interpret data and amaze
    your customer with it""",
    backstory="""Known as the BEST research analyst, you're
    skilled in sifting through news, company announcements,
    and market sentiments. Now you're working on a super
    important customer""",
    verbose=True,
    tools=[
      SoupScraperTools.scrape_and_summarize_website,
      GoogleSoupSearchTools.search_internet,
      GoogleSoupSearchTools.search_news,
      YahooFinanceNewsTool(),
      sec_tools.search_10q,
      sec_tools.search_10k
    ]
)
