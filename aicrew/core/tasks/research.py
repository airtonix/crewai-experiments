from crewai import Task


def research_topic_in_browser(agent, chunk):
  Task(
    agent=agent,
    description=
    f"""Analyze and summarize the content below, make sure to include the most relevant information in the summary, return only the summary nothing else.

    CONTENT
    ----------
    {chunk}"""
  )
