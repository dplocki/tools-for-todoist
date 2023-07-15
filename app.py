from flask import url_for, Flask
from todoist_api_python.api import TodoistAPI
import config


app = Flask(__name__)
api = TodoistAPI(config.todoist_api_key)


@app.route("/random_task")
def random_task():
    from tools.random_task import run

    result = run(api, "Może kiedyś")
    return f"<p>A random task from given project: '{result.content}'</p>"


@app.route("/plan_for_the_week")
def plan_for_the_week():
    from tools.plan_for_the_week import run

    run(api, "Przydzielone")
    return "<p>Done</p>"


@app.route("/test")
def reproduce_by_forgetting_curve():
    from tools.reproduce_by_forgetting_curve import run

    items_count = run(api, "wishtoremember", 5)
    return f"<p>Affacted items: {items_count}</p>"


@app.route("/")
def hello_world():
    return f"""<!doctype html>
<body>
    <h1>Tool for Todoist</h1>

    <ul>
        <li><a href="{url_for('random_task')}">Random task</a></li>
        <li><a href="{url_for('plan_for_the_week')}">Plan for the week</a></li>
        <li><a href="{url_for('reproduce_by_forgetting_curve')}">Reproduce by forgetting curve</a></li>
    </ul>
</body>
"""


if __name__ == "__main__":
    import os

    app.run(debug=os.getenv("DEBUG_MODE") != None, host="0.0.0.0", port=5000)
