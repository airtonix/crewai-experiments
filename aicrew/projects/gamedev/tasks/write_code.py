from textwrap import dedent
from crewai import Task


def create_task(agent, game):
  return Task(
    description=dedent(f"""\
      You will create a game using python, these are the instructions:

      Instructions
      ------------
      {game}

      Your Final answer must be the full python code, only the python code and nothing else.
    """),
    agent=agent,
  )
