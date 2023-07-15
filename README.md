# Tools for Todoist

My tools for [Todoist](https://todoist.com/). Based on [Todoist API Python Client](https://pypi.org/project/todoist-api-python/) package.

Language: **Python 3**

## Tools

### 🎲 Random task

Selecting a random task from the Project given by name.

### 🗓️ Plan for the week

Create a week plan of daily task, with random number.

### 📉 Reproduce by forgetting curve

Finding all tasks with specyfied label and add copy x times (x is provided by enduser). Each task is away from previous with raising interval.

## Notes

* [Developing with Todoist](https://developer.todoist.com/rest/v2/)
* Minimum Python is 3.9 (in case of lower, the TodoistAPI will not work, due to the fact, the version 2.0 is using v2 of API, and version v1 is no longer supported)
