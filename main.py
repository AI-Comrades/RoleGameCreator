from src.crew import AIComradesCrew
from textwrap import dedent
import os

def main():
    print("## Welcome to RoleGameCreateor")
    print("-------------------------------")
    theme = input(dedent("""Specify the theme of the game in 2-3 sentences: """))
    n_roles = int(input(dedent("""Specify the number of characters in the game: """)))
    n_interactions = int(input(dedent("""Specify the number of interactions every character will have: """)))
    n_tasks = int(input(dedent("""Specify the number of tasks every character has to complete during the game: """)))
    filename = input(dedent("""Specify the filename to save the game to (e.g. game.md): """))

    crew = AIComradesCrew()
    result = crew.run(theme, n_roles, n_interactions, n_tasks)

    os.makedirs('created_games', exist_ok=True)
    with open(f'created_games/{filename}', 'w') as f:
        print("\n\n########################")
        print(f"## Here is the game! The output has also been saved to {filename} file!")
        for task_out in result['tasks_outputs']:
            f.write(task_out.exported_output)
            print(task_out.exported_output)

if __name__ == "__main__":
    main()