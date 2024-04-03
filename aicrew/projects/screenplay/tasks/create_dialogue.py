from crewai import Task, Agent


def create_task(agent:Agent):
  return Task(
    description="""
    Create a dialogue heavy screenplay from the discussion, between two persons.
    Do NOT write parentheticals.
    Leave out wrylies.
    You MUST SKIP directional notes.
    """,
    agent=agent
  )
