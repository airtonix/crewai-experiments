from crewai import Agent


class BrowserAnalystAgents():

  def researcher():
    return Agent(
      role='Principal Researcher',
      goal=
      'Do amazing research and summaries based on the content you are working with',
      backstory=
      "You're a Principal Researcher at a big company and you need to do research about a given topic.",
      allow_delegation=False
    )
