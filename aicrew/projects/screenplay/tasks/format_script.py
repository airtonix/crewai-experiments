from crewai import Task, Agent


def create_task(agent:Agent):
  return Task(
    description="""
    Format the script exactly like this:
    ## (person 1):
    (first text line from person 1)

    ## (person 2):
    (first text line from person 2)

    ## (person 1):
    (second text line from person 1)

    ## (person 2):
    (second text line from person 2)
    """,
    agent=agent
  )
