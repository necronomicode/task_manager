from flask import Flask, request
from database_handler import DatabaseHandler 

class Server:
    """ Class to create a REST API which will receive the actions to perform. """
    
    def __init__(self):
        self.db = DatabaseHandler()
        success, result = self.db.start_database()

        if not success:
            print(f"There was a problem creating the database: {result}")

        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        """ Create the necessary routes in order to manage the petitions. """
        self.app.add_url_rule("/tasks", "new_task", self.new_task, methods=["POST"])
        self.app.add_url_rule("/tasks", "list_tasks", self.list_tasks, methods=["GET"])
        self.app.add_url_rule("/tasks/<int:id>", "complete_task", self.complete_task, methods=["PUT"])
        self.app.add_url_rule("/tasks/<int:id>", "delete_task", self.delete_task, methods=["DELETE"])

    def run(self):
        """ Run the server. """
        self.app.run()
        
    def new_task(self):
        """ Create a new task with the received parameters.
        This method is used to create a new task based on the parameters received in the request.
        The parameters for the new task should be provided as JSON data using the POST method.
        The new task is inserted into the tasks table by generating an appropriate SQL query.

        :return: JSON object with 2 values:
            - success: A boolean indicating if the query has been executed successfully.
            - result: The id of the created registry if the query has been successful, otherwise an error message.
        """
        data = request.json
        title = data['title']
        description = data['description']
        due_date = data['due_date']

        query = "INSERT INTO tasks (title, description, due_date, done)" \
                "VALUES (?, ?, ?, False)"
        parameters = (title, description, due_date)
        success, result = self.db.execute_insert(query, parameters)

        return {"success": success, "result": result}

    def list_tasks(self):
        """ Get all tasks.
        This method is used to query the database for all the tasks and their information

        :return: JSON object with 2 values:
            - success: A boolean indicating if the query has been executed successfully.
            - result: A list of task information represented as dictionaries if the query has been successful, otherwise an error message.
        """

        query = "SELECT * FROM tasks"
        success, result = self.db.execute_select(query)

        return {"success": success, "result": result}

    def complete_task(self, id):
        """ Mark a task as done.
        This method is used to update the registry entry of a specified task by changing the "done" parameter to True.

        :param id: the task identifier.
        
        :return: JSON object with 2 values:
            - success: A boolean indicating if the query has been executed successfully.
            - result: The number of registries updated if the query has been successful, otherwise an error message.
        """
        
        query = "UPDATE tasks SET done = True WHERE id = ?"
        parameters = (id,)

        success, result = self.db.execute_update(query, parameters)
        return {"success": success, "result": result}

    def delete_task(self, id):
        """ Delete a task
        This method is used to remove a task registry entry of the database.

        :param id: the task identifier.
        
        :return: JSON object with 2 values:
            - success: A boolean indicating if the query has been executed successfully.
            - result: The number of registries deleted if the query has been successful, otherwise an error message.
        """
        query = "DELETE FROM tasks WHERE id = ?"
        parameters = (id,)

        success, result = self.db.execute_delete(query, parameters)
        return {"success": success, "result": result}

if __name__ == '__main__':
    server = Server()
    server.run()