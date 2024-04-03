from crewai import Crew

from aicrew.projects.gamedev import agents
from aicrew.projects.gamedev import tasks
from aicrew.core import ui
from aicrew import specs


class GameDevCrew:

    def run(self, game_description:str ):
      senior_engineer_agent = agents.senior_engineer.create_agent()
      qa_engineer_agent = agents.qa_engineer.create_agent()
      chief_qa_engineer_agent = agents.chief_qa_engineer.create_agent()

      write_code_task = tasks.write_code.create_task(senior_engineer_agent, game_description)
      tech_review_code_task = tasks.tech_review_code.create_task(qa_engineer_agent, game_description)
      story_review_code_task = tasks.story_review_code.create_task(chief_qa_engineer_agent, game_description)

      crew = Crew(
        agents=[
          senior_engineer_agent,
          qa_engineer_agent,
          chief_qa_engineer_agent,
        ],
        tasks=[
          write_code_task,
          tech_review_code_task,
          story_review_code_task
        ],
        verbose=True
      )

      result = crew.kickoff()

      # Print results
      print("\n\n########################")
      print("## Here is the result")
      print("########################\n")
      print("final code for the game:")
      print(result)


def main():
  print("## Welcome to GameDev Crew")
  print('-------------------------------')

  instructions = ui.read_file(
    ui.choose_file(
        question="What is the file containing the game specifications?",
        choices=specs.list_files(),
        format=specs.format_file
    )
  )

  crew = GameDevCrew()
  crew.run(instructions)

  print('===================== end of program ===================================')

if __name__ == "__main__":
    main()
