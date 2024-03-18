from crewai import Task
from textwrap import dedent

class Tasks():
    def write_scenario(self, agent, theme, n_roles):
        return Task(
            description=dedent(f"""
            Write a scenario for role-playing game that matches the theme. This is the theme of the game:
                                       
            Theme
            -----
            {theme}

            The scenario has to include {n_roles} different characters. Scenario has to be written in Markdown style and formatted using these rules:

            Formatting rules
            ----------------
            # Game Scenario
            <Text of the game scenario>
            """),
            expected_output=dedent("""The scenario for the role-playing game. Output should be formatted in Markdown and match the provided formatting rules"""),
            agent=agent,
        )

    def write_roles(self, agent, n_interactions, n_tasks):
        return Task(
            description=dedent(f"""
            Create detailed descriptions for the characters of the game. These are the instructions for the descriptions:
                                       
            Instructions
            ------------
            * All characters must be unique
            * Character's name and occupation should match the game scenario
            * Every character has one main goal to achieve during the game
            * Every character has to interact with at least {n_interactions} other characters to achieve his main goal
            * Every character has at least {n_tasks} tasks that will help him achieve his main goal
            * For every task provide a hint on how to complete it

            Using the game scenario you got, write the detailed description for all characters of the game. The description has to be written in Markdown style and formatted using these rules:

            Formatting rules
            ----------------
            ## Name:
            ### Occupation:
            ### Main Goal:
            #### Interactions during the game:
            <List of interactions and the names of characters to interact with. Each interaction has to align with one task of the character.>
            #### Tasks to achieve: 
            <List of tasks to complete during the game.>
            #### Hints:
            <List of hints. Every hint has to align with one task of the character.>
            """),
            expected_output=dedent(f"The list of detailed descriptions for all characters. Output should be formatted in Markdown and match the provided formatting rules"),
            agent=agent,
        )