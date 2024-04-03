from crewai import Agent

from core.models import mistral_model

def create_agent():
  return Agent(
    role='formatter',
    goal='''
    Format the text as asked.
    Leave out actions from discussion members that happen between brackets, eg (smiling).
    ''',
    backstory='You are an expert text formatter.',
    llm=mistral_model,
    verbose=True,
    allow_delegation=False
  )
