from itertools import islice


def iterval_generator():
    current = 0
    move = 1

    while True:
        current += move
        yield current
        move += 1


def generate_task_for_given(api, task, label_name: str, how_many_repeats: int):
    for iterval in islice(iterval_generator(), how_many_repeats):
        api.add_task(
            content=task.content,
            project_id=task.project_id,
            description=task.description,
            due_string=f"+{iterval} day",
            labels=remove_label_from_task(task, label_name)
        )


def get_all_task_for_given_label(api, label_name: str):
    yield from (item
    for item in api.get_tasks()
    if label_name in item.labels)


def close_task(api, task):
    return api.close_task(task_id=task.id)


def remove_label_from_task(task, label_name):
    return [label for label in task.labels if label != label_name]


def run(api, label_name: str, how_many_repeats) -> int:
    count = 0

    for task in get_all_task_for_given_label(api, label_name):
        generate_task_for_given(api, task, label_name, how_many_repeats)
        close_task(api, task)
        count += 1

    return count
