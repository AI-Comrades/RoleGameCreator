from crewai import Task
from textwrap import dedent

class Tasks():
    def example_task(self, agent):
        return Task(
            description=dedent(f"""TODO"""),
            expected_output=dedent(f"""TODO"""),
            agent=agent,
        )