from itertools import islice


def iterval_generator():
    current = 0
    move = 1

    while True:
        current += move
        yield current
        move += 1


def generate_task_for_given(api, task):

    pass


def get_all_task_for_given_label(api, label_name: str):
    yield from (item
    for item in api.get_tasks()
    if label_name in item.labels)


def run(api, label_name: str) -> int:
    count = 0

    for task in get_all_task_for_given_label(api, label_name):
        generate_task_for_given(api, task)
        count += 1

    return count
