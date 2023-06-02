# Task Manager

Task Manager is a CLI program used for task management.

Task manager es una aplicación CLI para la gestión de tareas.

# Installation

Since the program is written in Python, you just need to install the dependencies, which are written in the requirements.txt file.

You can do the installation by using pip:

```
pip install -r requirements.txt
```

It's recommendable to use a virtual environment for the execution of the program.

# Usage

This program is composed of two main components, a backend server and a console program acting as the frontend.

To use Task Manager, you need to start the server first. This can be done by running the command `python3 server.py`. Once the server starts, it will also create the database if it doesn't exist.

Once we have the server up and running, we can open another console and run the frontend by typing `python3 task_manager.py`.

From this frontend, we can send our requests to the API.