from crewai import Task, Agent


def create_task(agent:Agent, dialogue:str):
  return Task(
    description=f"""
    Read the following dialogue.
    Then score the script on a scale of 1 to 10.
    Only give the score as a number, nothing else.
    Do not give an explanation.

    ### DIALOGUE:
    {dialogue}
    """,
    agent=agent
  )
