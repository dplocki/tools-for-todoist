import random


def run(api, project_name):
    project = next(p for p in api.get_projects() if p.name == project_name)
    project_id = project.id

    project_items = list(
        item
        for item in api.get_tasks()
        if item.project_id == project_id
        and item.parent_id == None
        and item.completed == False
    )

    return random.choice(project_items)
