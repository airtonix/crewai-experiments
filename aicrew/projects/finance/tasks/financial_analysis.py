from crewai import Task
from textwrap import dedent
from aicrew.projects.finance.tasks.core import __tip_section


def create_task(agent):
  return Task(description=dedent(f"""
      Conduct a thorough analysis of the stock's financial
      health and market performance.
      This includes examining key financial metrics such as
      P/E ratio, EPS growth, revenue trends, and
      debt-to-equity ratio.
      Also, analyze the stock's performance in comparison
      to its industry peers and overall market trends.

      Your final report MUST expand on the summary provided
      but now including a clear assessment of the stock's
      financial standing, its strengths and weaknesses,
      and how it fares against its competitors in the current
      market scenario.

      {__tip_section()}

      Make sure to use the most recent data possible.
    """),
    agent=agent
  )
