from crewai import Agent
from core.models import mistral_model

def create_agent():
  return Agent(
    role='analyse',
    goal='''
    You will distill all arguments from all discussion members.
    Identify who said what.
    You can reword what they said as long as the main discussion points remain.
    ''',
    backstory='You are an expert discussion analyst.',
    llm=mistral_model,
    verbose=True,
    allow_delegation=False
  )
