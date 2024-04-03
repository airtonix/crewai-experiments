import os

import json
import requests
from langchain_community.vectorstores import FAISS
from langchain.tools import tool



class ISearchTools():
  """
  The interface class for searching the internet
  all methods here throw to indicate that they should be implemented by the subclass
  """

  def __init__(self):
    pass
  def prepare_results(self, results):
    raise NotImplementedError("This method should be implemented by the subclass")

  def search_internet(self, query):
    raise NotImplementedError("This method should be implemented by the subclass")

  def search_news(self, query):
    raise NotImplementedError("This method should be implemented by the subclass")


class SearchResultBase(ISearchTools):

  def prepare_result(self, title, url, content):
      return "\n".join([
          f"Title: {title}",
          f"Link: {url}",
          f"Snippet: {content}",
          "\n-----------------"
      ])


class GoogleSoupSearchTools(SearchResultBase):
  """
  This class contains tools that are useful to search the internet

  it uses the googlesearch library to search the internet.
  """

  @tool('Search the internet')
  def search_internet(self, query):
    """Useful to search the internet
    about a a given topic and return relevant results

    Returns the top 5 results from the search.

    As a multiline string where each result takes the format:
      Title: <title>
      Link: <link>
      Snippet: <snippet>
    """
    from googlesearch import search
    results = search(query, num=5, stop=5, pause=2)

    output = []
    for result in results:
      output.append(self.prepare_result(result['title'], result['url'], result['description']))

    return "\n".join(output)

  @tool('Search news on the internet')
  def search_news(self, query):
    """Useful to search news about a company, stock or any other
    topic and return relevant results"""
    from googlesearch import search
    results = search(query, num=5, stop=5, pause=2, tbs='nrt')
    return "\n".join(results)


class SerperSearchTools(SearchResultBase):

  @tool("Search the internet")
  def search_internet(self, query):
    """Useful to search the internet
    about a a given topic and return relevant results"""
    top_result_to_return = 4
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': os.environ['SERPER_API_KEY'],
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json()['organic']
    string = []
    for result in results[:top_result_to_return]:
      try:
        string.append(self.prepare_result(result['title'], result['link'], result['snippet']))
      except KeyError:
        next

    return '\n'.join(string)

  @tool("Search news on the internet")
  def search_news(self, query):
    """Useful to search news about a company, stock or any other
    topic and return relevant results"""""
    top_result_to_return = 4
    url = "https://google.serper.dev/news"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': os.environ['SERPER_API_KEY'],
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json()['news']
    string = []
    for result in results[:top_result_to_return]:
      try:
        string.append('\n'.join([
            f"Title: {result['title']}", f"Link: {result['link']}",
            f"Snippet: {result['snippet']}", "\n-----------------"
        ]))
      except KeyError:
        next

    return '\n'.join(string)
