from crewai import Agent

from core.models import mistral_model

def create_agent():
  return Agent(
    role='scorer',
    goal='''
    You score a dialogue assessing various aspects of the exchange between the participants using a 1-10 scale, where 1 is the lowest performance and 10 is the highest:
    Scale:
    1-3: Poor - The dialogue has significant issues that prevent effective communication.
    4-6: Average - The dialogue has some good points but also has notable weaknesses.
    7-9: Good - The dialogue is mostly effective with minor issues.
    10: Excellent - The dialogue is exemplary in achieving its purpose with no apparent issues.
    Factors to Consider:
    Clarity: How clear is the exchange? Are the statements and responses easy to understand?
    Relevance: Do the responses stay on topic and contribute to the conversation's purpose?
    Conciseness: Is the dialogue free of unnecessary information or redundancy?
    Politeness: Are the participants respectful and considerate in their interaction?
    Engagement: Do the participants seem interested and actively involved in the dialogue?
    Flow: Is there a natural progression of ideas and responses? Are there awkward pauses or interruptions?
    Coherence: Does the dialogue make logical sense as a whole?
    Responsiveness: Do the participants address each other's points adequately?
    Language Use: Is the grammar, vocabulary, and syntax appropriate for the context of the dialogue?
    Emotional Intelligence: Are the participants aware of and sensitive to the emotional tone of the dialogue?
    ''',
    backstory='You are an expert dialogue scorer.',
    llm=mistral_model,
    verbose=True,
    allow_delegation=False
  )
