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
    return "plan_for_the_week"


@app.route("/")
def hello_world():
    return f"""<!doctype html>
<body>
    <h1>Tool for Todoist</h1>

    <ul>
        <li><a href="{url_for('random_task')}">Random task</a></li>
        <li><a href="{url_for('plan_for_the_week')}">Plan for the week</a></li>
    </ul>
</body>
"""


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
