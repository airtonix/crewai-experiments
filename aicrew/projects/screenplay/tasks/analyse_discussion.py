from crewai import Task, Agent


def create_task(agent:Agent, discussion:str):
  return Task(
    description=f"""
      Analyse in much detail the following discussion:

      ### DISCUSSION:
      {discussion}
      """,
    agent=agent
  )
