#!/bin/sh

PRELOAD_PYTHON_FILE="$(mktemp /tmp/XXXXXXXXX.py)" || exit 1

trap 'rm -f $PRELOAD_PYTHON_FILE' EXIT

cp config.py $PRELOAD_PYTHON_FILE
cat >> $PRELOAD_PYTHON_FILE <<EOL
from todoist_api_python.api import TodoistAPI
api = TodoistAPI(todoist_api_key)
EOL

PYTHONSTARTUP=$PRELOAD_PYTHON_FILE python
