from textwrap import dedent
from crewai import Agent
from aicrew.core import models

def create_agent():
  return Agent(
    role="Chief Software Quality Control Engineer",
    goal="Ensure that the code does the job that it is supposed to do",
    backstory=dedent("""\
      You feel that programmers always do only half the job, so you are
      super dedicate to make high quality code."""
    ),
    allow_delegation=True,
    verbose=True,
    llm=models.llama2_uncensored,
  )
