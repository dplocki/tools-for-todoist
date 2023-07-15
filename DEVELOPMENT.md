# Development notes

Initially the tools were 

## Using

* Python 3
* Todoist Python libraries
* Docker
* Flask

## Changes in project

* Introduce docker image, both for working on tools 
* I have decide to introduce the web GUI for tools

    The docker image and VS Code settings are base on article [Dockerize a Flask app and debug with VSCode](https://dev.to/pacheco/dockerize-a-flask-app-and-debug-with-vscode-34i1).

## Development

Use the command:

```sh
docker compose up -d
```

Docker image will run the web on address: [localhost:5000](http://localhost:5000/).
