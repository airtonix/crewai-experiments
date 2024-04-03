from textwrap import dedent
from crewai import Agent
from aicrew.core import models

def create_agent():
  return Agent(
    role="Senior Software Engineer",
    goal="Create software as needed",
    backstory=dedent("""\
      You are a Senior Software Engineer at a leading tech think tank.
      Your expertise in programming in python. and do your best to
      produce perfect code"""
    ),
    allow_delegation=False,
    verbose=True,
    llm=models.llama2_uncensored,
  )
