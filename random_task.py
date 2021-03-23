import random
from todoist.api import TodoistAPI
import config

api = TodoistAPI(config.todoist_api_key)
api.sync()

project = next((p for p in api.state['projects'] if p['name'] == 'Może kiedyś'))
project_id = project['id']

project_items = list(
        item
        for item in api.items.state['items']
        if item['project_id'] == project_id and item['parent_id'] == None and item['in_history'] == 0
    )

print(random.choice(project_items).data['content'])
