from crewai import Task, Agent


def create_task(agent:Agent, discussion:str):
  # Filter out spam and vulgar posts
  return Task(
    description=f"""
    Read the following newsgroup post.
    If this contains vulgar language reply with STOP.
    If this is spam reply with STOP.

    ### NEWGROUP POST:
    {discussion}
    """,
    agent=agent
  )
