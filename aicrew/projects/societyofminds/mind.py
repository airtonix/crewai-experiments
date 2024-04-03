import ast
import json
from typing import List

from crewai import Agent, Task, Crew, Process
from pydantic import BaseModel
from aicrew.core import models
from rich.pretty import Pretty
from rich.panel import Panel
from rich import print

class Agents(BaseModel):
    agent_name: str
    role: str
    goal: str
    backstory: str
    task: str
    taskoutput: str

class AgentList(BaseModel):
    agents: List[Agents]

    class Config:
        arbitrary_types_allowed = True


def create_agent_tasks(agent_info):
    crew_agents:list[Agent] = []
    crew_tasks:list[Task] = []

    for agent in agent_info:
        agent_name = agent["agent_name"]

        role_name = agent["role"]
        goal = agent["goal"]
        backstory = agent["backstory"]
        task = agent["task"]
        task_output = agent["taskoutput"]
        crew_agent = Agent(
            role=role_name,
            goal=goal,
            verbose=False,
            memory=True,
            backstory=backstory,
            tools=[],
            allow_delegation=False,
            llm=models.llama2_uncensored,
        )
        crew_agents.append(crew_agent)

        print(
            Panel(
                Pretty({
                    "agent_name": agent_name,
                    "role": role_name,
                    "goal": goal,
                    "backstory": backstory,
                }),
                title=f"[green]Agent"
            )
        )

        crew_task = Task(
            description=(
                task
            ),
            expected_output=task_output,
            tools=[],
            agent=crew_agent
        )
        crew_tasks.append(crew_task)

        print(
            Panel(
                Pretty({
                    "task": task,
                    "task_expected_output": task_output,
                }),
                title=f"[green]Task"
            )
        )

    return crew_agents, crew_tasks

def create_society(task: str):
    # creates the smaller agents in the Mind
    print(Panel('Creating the society of minds'))

    society_of_minds = Agent(
        role='Mind Creator',
        goal='Create smaller process to achieve a complex task',
        verbose=False,
        memory=True,
        backstory=(
            "You are the creator of Mind. Each mind is made of many smaller processes which we call agents. "
            "You know that each mental agent by itself can only do some simple thing that needs no mind or thought at all."
            "Yet when we join these agents in societies, in certain very special ways, this leads to intelligence. "
            "Your job is to create a series of agents based on a provided complex task."),
        tools=[],
        llm=models.llama2_uncensored,
        allow_delegation=True
    )
    print(Panel('Mind Created'))

    # creates the tasks for the agents
    society_of_minds_task = Task(
        description=(
            "{task}"
        ),
        expected_output=(
            "A list of agents with their name, role, goal, backstory, task and task output in a JSON format."
            "Only output the JSON."
            "Keys in the JSON must be lower case and named as agent_name,role,goal,backstory,task and taskoutput Do not add anything else."
        ),
        tools=[],
        agent=society_of_minds,
        output_json=AgentList,
    )
    print(Panel('Tasks Created'))


    crew = Crew(
        agents=[society_of_minds],
        tasks=[society_of_minds_task],
        verbose=False,
        process=Process.sequential  # Optional: Sequential task execution is default
    )

    print(Panel('Generating Agents'))

    agents = crew.kickoff(inputs={'task': task})

    # try:
    #   agents = ast.literal_eval(agents)
    # except Exception as e:
    #   print(Panel(str(e), title='Error'))
    #   return [], []

    print(Panel('Generating Tasks'))
    # crew_agents, crew_tasks = create_agent_tasks(agents['agents'])
    print(Panel(json.dumps(agents), title='Agents'))
    # print(
    #     Panel(
    #         Pretty({
    #             "agents": len(crew_agents),
    #             "tasks": len(crew_tasks)
    #         }),
    #         title='Society of Minds'
    #     )
    # )

    # return crew_agents, crew_tasks
