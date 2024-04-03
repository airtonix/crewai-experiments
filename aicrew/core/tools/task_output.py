from crewai.task import TaskOutput

def on_task_complete(output: TaskOutput):
    # Do something after the task is completed
    # Example: Send an email to the manager
    print(f"""
        Task completed!
        Task: {output.description}
        Output: {output.raw_output}
    """)

def on_task_complete_factory(
  on_load=None,
  on_error=None,
  on_success=None
):
    def on_task_complete(output: TaskOutput):
        if output.error:
            if on_error:
                on_error(output.error)
        else:
            if on_success:
                on_success(output.raw_output)
            if on_load:
                on_load(output.raw_output)

    return on_task_complete
