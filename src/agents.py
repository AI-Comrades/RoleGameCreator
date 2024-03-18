from crewai import Agent
from textwrap import dedent

class Agents():
    def example_agent(self):
        return Agent(
            role=dedent(f"""TODO"""),
            backstory=dedent(f"""TODO"""),
            goal=dedent(f"""TODO"""),
            allow_delegation=False,
            verbose=True,
        )