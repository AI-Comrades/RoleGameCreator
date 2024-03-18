from crewai import Agent
from textwrap import dedent

class Agents():
    def scenario_writer(self):
        return Agent(
            role="Role-Play Game Scenario Writer",
            backstory=dedent(f"""Known as the BEST scenario writer for role-playing games, you're skilled in writing complex scenarios with immersive experience"""),
            goal=dedent(f"""Create a scenario for role-playing game"""),
            allow_delegation=False,
            verbose=True,
        )

    def role_writer(self):
        return Agent(
            role="Role Writer",
            backstory=dedent(f"""You are a role writer that specializes in writing highly detailed role of the game's characters. The characters you create interact with each other and complete goals together"""),
            goal=dedent(f"""Create a player role that fits the game scenario"""),
            allow_delegation=False,
            verbose=True,
        )