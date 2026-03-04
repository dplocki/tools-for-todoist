from itertools import chain
import random


def run(api, project_name):
    projects = chain.from_iterable(api.get_projects())
    project = next(p for p in projects if p.name == project_name)
    project_id = project.id

    project_items = list(
        item
        for item in chain.from_iterable(api.get_tasks())
        if item.project_id == project_id
        and item.parent_id == None
        and item.is_completed == False
    )

    return random.choice(project_items)
