import os
from wcmatch import glob

herepath = os.path.realpath(os.path.dirname(__file__))

# provides a list of specs in this directory

FILTER_GLOBS: list[str] = [
  '__*',
  '*.py'
]

def list_files():
  files = os.listdir(herepath)

  # an array of strings
  output: list[str] = []

  for file in files:
    matches = glob.globmatch(file, FILTER_GLOBS)
    if matches:
      continue

    # if none of the globs match continue
    output.append(file)

  return output

def format_file(file: str):
  return os.path.join(herepath, file)
