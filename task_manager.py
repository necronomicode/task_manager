from datetime import datetime
import requests

class TaskManager:
    """ Overall class to manage the Task Manager program. """

    def __init__(self):
        self.url = "http://127.0.0.1:5000"
        
    def run(self):
        """ Main class to execute the user option.
        This method runs an infinite loop that will ask the user for it's option. Based on what 
        the user wants to do, the program will perform that action.
        """
        running = True
        while running:
            print("Task Manager options:")
            print("\t1. Create a new task")
            print("\t2. List saved tasks")
            print("\t3. Mark a task as done")
            print("\t4. Delete a task")
            print("\t5. Exit")

            option = input("Choose an option (1-5): ")

            if option == "1":
                self._create_task()
            elif option == "2":
                self._list_tasks()
            elif option == "3":
                self._complete_task()
            elif option == "4":
                self._delete_task()
            elif option == "5":
                running = False
            else:
                print("Please, choose an option by writing a number between 1 and 5.")
        

    def _create_task(self):
        """ Create a new task.
        This method asks the user for the parameters of a new task.
        Then it will call the REST API using the POST method and send these parameters as a JSON object.
        Based on the server response, the method will print a message on the screen to indicate if the 
        task has been created correctly.
        """
        title = input("Enter task title: ")
        while title == "":
            print("Title cannot be null.\n")
            title = input("Enter task title: ")

        description = input("Enter task description: ")

        due_date = input("Enter task's due date: ")
        while not self._validate_date(due_date):
            due_date = input("Enter task's due date: ")

        data = {'title': title,
                'description': description,
                'due_date': due_date}

        url = f"{self.url}/tasks"
        response = requests.post(url, json=data)

        if response.status_code == 200:
            data = response.json()
            if data['success']:
                print(f"Task '{title}' has been created with ID '{data['result']}'")
            else:
                print(f"It was not possible to create the task: '{data['result']}'")
        else:
            print(f"An error has ocurred while communicating with the server. Statuts code: {response.status_code}")

    def _list_tasks(self):
        """ Print all the tasks.
        This method calls the REST API without parameters by using the GET method. 
        Based on the server response, the method will print the information of the tasks receieved
        or an error message.
        """
        url = f"{self.url}/tasks"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data['success']:
                for task in data['result']:
                    status = "DONE" if task[4] else "TO DO"
                    print(f"Task {task[0]}:")
                    print(f"\tTitle: {task[1]}")
                    print(f"\tDescription: {task[2]}")
                    print(f"\tDue date: {task[3]}")
                    print(f"\tStatus: {status}")
            else:
                print(f"It was not possible to retrieve the task list: '{data['result']}'")
        else:
            print(f"An error has ocurred while communicating with the server. Statuts code: {response.status_code}")

    def _complete_task(self):
        """ Mark a task as done.
        This method asks the user for a task ID. Then it will call the REST API using the PUT method and sending these
        parameter in the URL.
        Based on the server response, the method will print a message on the screen to indicate if the task 
        has been updated correctly.
        """
        id = input("Enter task ID: ")
        while not self._validate_id(id):
            id = input("Enter task ID: ")

        url = f"{self.url}/tasks/{id}"
        response = requests.put(url)

        if response.status_code == 200:
            data = response.json()
            if data['success']:
                if data['result'] > 0:
                    print(f"The task with ID '{id}' has been marked as done.")
                else:
                    print(f"It was not possible to update the task with ID '{id}' because it was not found in the database.")
            else:
                print(f"It was not possible to update the tas with ID '{id}': '{data['result']}'")
        else:
            print(f"An error has ocurred while communicating with the server. Statuts code: {response.status_code}")

    def _delete_task(self):
        """ Remove a specific task.
        This method asks the user for a task ID. Then it will call the REST API using the DELETE method and sending these
        parameter in the URL.
        Based on the server response, the method will print a message on the screen to indicate if the task 
        has been deleted correctly.
        """
        id = input("Enter task ID: ")
        while not self._validate_id(id):
            id = input("Enter task ID: ")

        sure = ""

        while sure != "yes" and sure != "no" and sure != "y" and sure != "n":
            sure = input(f"You're going to delete the task with ID '{id}'. Are you sure of this operation?(yes/no): ").lower()

        if sure == "no" or sure == "n":
            return False

        url = f"{self.url}/tasks/{id}"
        response = requests.delete(url)

        if response.status_code == 200:
            data = response.json()
            if data['success']:
                if data['result'] > 0:
                    print(f"The task with ID '{id}' has been deleted.")
                else:
                    print(f"It was not possible to delete the task with ID '{id}' because it was not found in the database.")
            else:
                print(f"It was not possible to delete the task with ID '{id}': '{data['result']}'")
        else:
            print(f"An error has ocurred while communicating with the server. Statuts code: {response.status_code}")

    def _validate_date(self, date):
        """ Validate that the user-entered date is in ISO 8601 format. """
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date. Please, use ISO 8601 format (example: 2000-12-31). \n")
            return False
        return True

    def _validate_id(self, id):
        """ Validate that the user-entered ID is an integer. """
        if id == "" or id is None:
            print("An ID is necesary to perform this operation.\n")
            return False
        if not id.isnumeric():
            print("The task ID must be an integer.\n")
            return False                
        return True

if __name__ == "__main__":
    tm = TaskManager()
    tm.run()
    

