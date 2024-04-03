from textwrap import dedent
from crewai import Task


def create_task(agent, game):
  return Task(
    description=dedent(f"""\
      You are helping create a game using python, these are the instructions:

      Instructions
      ------------
      {game}

      Using the code you got, check for errors. Check for logic errors,
      syntax errors, missing imports, variable declarations, mismatched brackets,
      and security vulnerabilities.

      Your Final answer must be the full python code, only the python code and nothing else.
    """),
    agent=agent
  )
