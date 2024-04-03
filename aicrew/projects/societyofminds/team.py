import os
from crewai import Crew, Process, Task
from argparse import ArgumentParser
from rich.pretty import Pretty
from rich.panel import Panel
from rich.tree import Tree
from rich.live import Live
from rich import print

from aicrew.core import ui
from aicrew.projects.societyofminds import mind


def project(task:str):
  print(Panel(task, title="Task"))

  crew_agents, crew_tasks = mind.create_society(task)

  print(Panel({
    "agents": len(crew_agents),
    "tasks": len(crew_tasks)
  }))

  crew = Crew(
    agents=crew_agents,
    tasks=crew_tasks,
    verbose=False,
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
