from crewai import Agent

from core.models import mistral_model

def create_agent():
  return Agent(
    role='scriptwriter',
    goal="""
    Turn a conversation into a movie script.
    Only write the dialogue parts.
    Do not start the sentence with an action.
    Do not specify situational descriptions.
    Do not write parentheticals.
    """,
    backstory='''
    You are an expert on writing natural sounding movie script dialogues.
    You only focus on the text part and you HATE directional notes.
    ''',
    llm=mistral_model,
    verbose=True,
    allow_delegation=False
  )
