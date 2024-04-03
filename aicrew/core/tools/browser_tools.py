import os

import requests
import json
from unstructured.partition.html import partition_html
from langchain.tools import tool
from bs4 import BeautifulSoup

from core.agents.research import BrowserAnalystAgents
from core.tasks.research import research_topic_in_browser


class IScrapingTools():
  """
  The interface class for scraping the internet
  all methods here throw to indicate that they should be implemented by the subclass
  """

  def __init__(self, *args, **kwargs):
    self.researcher = kwargs.get('researcher', BrowserAnalystAgents.researcher)

  def scrape_and_summarise(self, website):
    raise NotImplementedError("This method should be implemented by the subclass")


class BrowserlessScraperTools(IScrapingTools):

  @tool("Scrape website content")
  def scrape_and_summarise(self, website):
    """Useful to scrape and summarize a website content"""
    url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
    payload = json.dumps({"url": website})
    headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    elements = partition_html(text=response.text)
    content = "\n\n".join([str(el) for el in elements])
    content = [content[i:i + 8000] for i in range(0, len(content), 8000)]

    summaries = []
    for chunk in content:
      agent = self.researcher(),
      task = research_topic_in_browser(agent, chunk)
      summary = task.execute()
      summaries.append(summary)

    return "\n\n".join(summaries)


class SoupScraperTools(IScrapingTools):

    @tool("Scrape website content")
    def scrape_and_summarise(self, website):
      """Useful to scrape and summarize a website content"""
      response = requests.get(website)
      soup = BeautifulSoup(response.text, 'html.parser')
      elements = partition_html(text=soup.text)
      content = "\n\n".join([str(el) for el in elements])
      content = [content[i:i + 8000] for i in range(0, len(content), 8000)]

      summaries = []
      for chunk in content:
        agent = self.researcher(),
        task = research_topic_in_browser(agent, chunk)
        summary = task.execute()
        summaries.append(summary)

      return "\n\n".join(summaries)
