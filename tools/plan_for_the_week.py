import random


def generate():
    maximum = 5
    distribute_table = [
        i
        for multiplayer in range(1, maximum)
        for i in [multiplayer] * (maximum - multiplayer)
    ]

    while True:
        yield distribute_table[random.randint(0, 9)]


def run(api, project_name):
    projects = api.get_projects()
    print(projects)
    project = next(p for p in projects if p.name == project_name)
    project_id = project.id

    pass_in_next_day = False
    for number_of_elements, number_of_day in zip(generate(), range(7)):
        if not pass_in_next_day:
            api.add_task(
                content=f"Poświęć mroku {number_of_elements}",
                project_id=project_id,
                due_string=f"+{number_of_day + 1} day",
            )

        pass_in_next_day = number_of_elements >= 3
