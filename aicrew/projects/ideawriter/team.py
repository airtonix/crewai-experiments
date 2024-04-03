import os
from textwrap import dedent
from crewai import Crew, Process, Task, Agent
from aicrew.core import ui, models
from argparse import ArgumentParser

from rich.pretty import Pretty
from rich.panel import Panel
from rich import print

def project(task:str):
  print(Panel(task))

  write_idea_agent = Agent(
    role='scriptwriter',
    description="",
    goal="Create a story based on the provided idea.",
    backstory='''
    You are an expert on writing game ideas.
    You love creating stories and you are good at it.
    ''',
    llm=models.mistral_model,
    verbose=True,
    allow_delegation=False
  )
  write_idea_task = Task(
    description=dedent(f"""
    Write a story based on the following idea:

    ### IDEA:
    {task}
    """),
    expected_output="A story based on the provided idea.",
    agent=write_idea_agent
  )


  crew = Crew(
    agents=[write_idea_agent],
    tasks=[write_idea_task],
    verbose=True,
    process=Process.sequential,
  )

  result = crew.kickoff()
  print(
    Panel(
      Pretty(result)
    )
  )


if __name__ == "__main__":
    parser = ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

    parser.add_argument('-t', '--task', help='The task to be analyzed', default=None, nargs='?')
    parser.add_argument('-tf', '--task-file', help='The task file to be analyzed', default=None, nargs='?')
    args = parser.parse_args()

    task = ui.get_task_input(args)

    project(task)
