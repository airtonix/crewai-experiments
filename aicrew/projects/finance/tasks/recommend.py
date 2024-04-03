from crewai import Task
from textwrap import dedent

from aicrew.projects.finance.tasks.core import __tip_section

def create_task(agent):
  return Task(description=dedent(f"""
      Review and synthesize the analyses provided by the
      Financial Analyst and the Research Analyst.
      Combine these insights to form a comprehensive
      investment recommendation.

      You MUST Consider all aspects, including financial
      health, market sentiment, and qualitative data from
      EDGAR filings.

      Make sure to include a section that shows insider
      trading activity, and upcoming events like earnings.

      Your final answer MUST be a recommendation for your
      customer. It should be a full super detailed report, providing a
      clear investment stance and strategy with supporting evidence.
      Make it pretty and well formatted for your customer.
      {__tip_section()}
    """),
    agent=agent
  )
