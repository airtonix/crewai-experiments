import os
import sys

from crewai import Crew

from aicrew.projects.finance import agents
from aicrew.projects.finance import tasks

sys.path.append(os.path.realpath("."))
import inquirer

class FinancialCrew:
  def __init__(self, company):
    self.company = company

  def run(self):

    research_analyst_agent = agents.research_analyst.create_agent()
    financial_analyst_agent = agents.financial_analyst.create_agent()
    investment_advisor_agent = agents.investment_advisor.create_agent()

    research_task = tasks.research.create_task(research_analyst_agent, self.company)
    financial_task = tasks.financial_analysis.create_task(financial_analyst_agent)
    filings_task = tasks.filings_analysis.create_task(financial_analyst_agent)
    recommend_task = tasks.recommend.create_task(investment_advisor_agent)

    crew = Crew(
      agents=[
        research_analyst_agent,
        financial_analyst_agent,
        investment_advisor_agent
      ],
      tasks=[
        research_task,
        financial_task,
        filings_task,
        recommend_task
      ],
      verbose=True
    )

    result = crew.kickoff()
    return result

def main():
  print("## Welcome to Financial Analysis Crew")
  print('-------------------------------')

  questions = [
    inquirer.Text('company', message="What is the company you want to analyze?")
  ]
  answers = inquirer.prompt(questions)

  financial_crew = FinancialCrew(answers['company'])

  result = financial_crew.run()

  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)

if __name__ == "__main__":
  main()
