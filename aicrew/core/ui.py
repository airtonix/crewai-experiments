import os
import sys
import inquirer
from argparse import Namespace

from rich import print, panel, pretty
def choose_file(question:str, choices:list, format=None):
    chosen_file = sys.argv[1] if len(sys.argv) > 1 else None

    if chosen_file is None:
      questions = [
          inquirer.List(
              "file",
              message=question,
              choices=choices
          )
      ]

      answers = inquirer.prompt(questions)
      if answers is None:
          sys.exit(0)

      chosen_file = answers["file"]

    if format:
        chosen_file = format(chosen_file)

    print(
        panel.Panel(
            "Chosen File",
            title="Chosen File",
            expand=False
        )
    )

    return chosen_file

def read_file(file:str):
  try:
    print(
        panel.Panel(
            file,
            title="Reading File",
            expand=False
        )
    )
    with open(file, 'r') as f:
      return f.read()
  except:
    return None

def get_task_input(args: Namespace):
  task = None

  if args.task:
    return args.task

  if args.task_file:
    task = read_file(args.task_file)

  if task == None and not args:
    task = text_input(question="What is the task?")

  return task

def text_input(question:str):
    questions = [
        inquirer.Text('text', message=question)
    ]

    answers = inquirer.prompt(questions)
    if answers is None:
        sys.exit(0)

    return answers['text']
