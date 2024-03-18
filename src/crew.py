from crewai import Crew
from src.agents import Agents
from src.tasks import Tasks
from dotenv import load_dotenv


load_dotenv()

class AIComradesCrew():
    def run(self, theme, n_roles, n_interactions, n_tasks):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = Agents()
        tasks = Tasks()

        # Define your custom agents and tasks here
        scenario_writer = agents.scenario_writer()
        role_writer = agents.role_writer()

        # Custom tasks include agent name and variables as input
        scenario_task = tasks.write_scenario(scenario_writer, theme, n_roles)
        roles_task = tasks.write_roles(role_writer, n_interactions, n_tasks)

        # Define your custom crew here
        crew_agents = [scenario_writer, role_writer]
        crew_tasks = [scenario_task, roles_task]

        crew = Crew(
            agents=crew_agents,
            tasks=crew_tasks,
            verbose=True,
            full_output=True,
        )

        result = crew.kickoff()
        return result