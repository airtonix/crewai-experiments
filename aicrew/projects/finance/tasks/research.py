from crewai import Task
from textwrap import dedent

from aicrew.projects.finance.tasks.core import __tip_section


def create_task(agent, company):
  return Task(description=dedent(f"""
      Collect and summarize recent news articles, press
      releases, and market analyses related to the stock and
      its industry.
      Pay special attention to any significant events, market
      sentiments, and analysts' opinions. Also include upcoming
      events like earnings and others.

      Your final answer MUST be a report that includes a
      comprehensive summary of the latest news, any notable
      shifts in market sentiment, and potential impacts on
      the stock.
      Also make sure to return the stock ticker.

      {__tip_section()}

      Make sure to use the most recent data as possible.

      Selected company by the customer: {company}
    """),
    agent=agent
  )
