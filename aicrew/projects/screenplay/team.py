import re

from crewai import Crew, Process

from aicrew.projects.screenplay import agents
from aicrew.projects.screenplay import tasks

from core import ui
import specs

class ScreenplayCrew:

    def run(self, discussion:str ):
      analyst_agent = agents.analyst.create_agent()
      scriptwriter_agent = agents.scriptwriter.create_agent()
      formatter_agent = agents.formatter.create_agent()
      scorer_agent = agents.scorer.create_agent()

      analyse_discussion_task = tasks.analyse_discussion.create_task(analyst_agent, discussion)
      create_dialogue_task = tasks.create_dialogue.create_task(scriptwriter_agent, discussion)
      format_script_task = tasks.format_script.create_task(formatter_agent)

      crew = Crew(
        agents=[
          analyst_agent,
          scriptwriter_agent,
          formatter_agent,
        ],
        tasks=[
          analyse_discussion_task,
          create_dialogue_task,
          format_script_task
        ],
        # verbose=2, # Crew verbose more will let you know what tasks are being worked on, you can set it to 1 or 2 to different logging levels
        process=Process.sequential # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.
      )

      result = crew.kickoff()

      #get rid of directions and actions between brackets, eg: (smiling)
      result = re.sub(r'\(.*?\)', '', result)

      print('===================== end result from crew ===================================')
      print(result)
      print('===================== score ==================================================')

      task4 = tasks.score_dialouge.create_task(scorer_agent, dialogue=result)
      score = task4.execute()
      score = score.split('\n')[0]  #sometimes an explanation comes after score, ignore
      print(f'Scoring the dialogue as: {score}/10')


def main():
  print("## Welcome to Screenplay Crew")
  print('-------------------------------')

  instructions = ui.read_file(
    ui.choose_file(
        question="What is the file containing the discussion?",
        choices=specs.list_files()
    )
  )

  screenplay_crew = ScreenplayCrew()

  screenplay_crew.run(instructions)

  print('===================== end of program ===================================')

if __name__ == "__main__":
    main()
