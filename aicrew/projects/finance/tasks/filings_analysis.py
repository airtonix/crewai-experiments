from crewai import Task
from textwrap import dedent
from aicrew.projects.finance.tasks.core import __tip_section


def create_task(agent):
  return Task(description=dedent(f"""
      Analyze the latest 10-Q and 10-K filings from EDGAR for
      the stock in question.
      Focus on key sections like Management's Discussion and
      Analysis, financial statements, insider trading activity,
      and any disclosed risks.
      Extract relevant data and insights that could influence
      the stock's future performance.

      Your final answer must be an expanded report that now
      also highlights significant findings from these filings,
      including any red flags or positive indicators for
      your customer.

      {__tip_section()}
    """),
    agent=agent
  )
