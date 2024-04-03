from crewai import Agent

from core.models import mistral_model

def create_agent():
    return Agent(
      role='spamfilter',
      goal='''
      Decide whether a text is spam or not.
      ''',
      backstory='You are an expert spam filter with years of experience. You DETEST advertisements, newsletters and vulgar language.',
      llm=mistral_model,
      verbose=True,
      allow_delegation=False
    )
