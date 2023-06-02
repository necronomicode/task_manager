import sqlite3

class DatabaseHandler:
    """ Class to encapsulate all the database related functionality. """
    
    def __init__(self):
        self.database = "task_manager.db"
        self.connection = None
        self.cursor = None

    def _connect(self):
        """ Establish a connection with the database. """
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def _disconnect(self):
        """ Close the connection with the database. """
        self.connection.close()

    def execute_select(self, query):
        """ Execute a SELECT query. 
        :param query: Query to be executed. 
        :return success: True if the query has been executed successfully, else False.
        :return result: List of tuples with all the results of the query.
        """
        success = False
        result = None
        try:
            self._connect()      
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            success = True
        except sqlite3.Error as ex:
            result = f"The following sqlite error ocurred while performing a select operation: {str(ex)}"
        except Exception as ex:
            result = f"The following general error ocurred while performing a select operation: {str(ex)}"
        finally:
            self._disconnect()

        return success, result

    def execute_insert(self, query, parameters):
        """ Execute an INSERT query. 
        :param query: Query to be executed.
        :return success: True if the query has been executed successfully, else False.
        :return result: The id of the inserted registry.
        """
        success = False
        result = None
        try:
            self._connect()
            self.cursor.execute(query, parameters)
            self.connection.commit()
            result = self.cursor.lastrowid
            success = True
        except sqlite3.Error as ex:
            result = f"The following sqlite error ocurred while performing an insert operation: {str(ex)}"
        except Exception as ex:
            result = f"The following general error ocurred while performing an insert operation: {str(ex)}"
        finally:
            self._disconnect()

        return success, result

    def execute_update(self, query, parameters):
        """ Execute an UPDATE query. 
        :param query: Query to be executed. 
        :param parameters: Parameters to specify the registry to modify.
        :return success: True if the query has been executed successfully, else False.
        :return result: Count of modified registries
        """
        success = False
        result = None
        try:
            self._connect()      
            self.cursor.execute(query, parameters)
            self.connection.commit()
            result = self.cursor.rowcount
            success = True
        except sqlite3.Error as e:
            result = f"The following sqlite error ocurred while performing an update operation: {str(ex)}"
        except Exception as ex:
            result = f"The following general error ocurred while performing an update operation: {str(ex)}"
        finally:
            self._disconnect()
        return success, result

    def execute_delete(self, query, parameters):
        """ Execute an DELETE query. 
        :param query: Query to be executed. 
        :param parameters: Parameters to specify the registry to delete.
        :return success: True if the query has been executed successfully, else False.
        :return result: Count of modified registries
        """
        success = False
        result = None
        try:
            self._connect()      
            self.cursor.execute(query, parameters)
            self.connection.commit()
            result = self.cursor.rowcount
            success = True
        except sqlite3.Error as e:
            result = f"The following sqlite error ocurred while performing a delete operation: {str(ex)}"
        except Exception as ex:
            result = f"The following general error ocurred while performing a delete operation: {str(ex)}"
        finally:
            self._disconnect()
        return success, result

    def start_database(self):
        """ Create the tasks table if does not exist.
            This method needs to be executed the first time the program is used, this way we
            can make sure the table with the tasks exists.
        """
        success = False
        result = None
        query = """
                CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                due_date DATE,
                done BOOLEAN)
                """
        try:
            self._connect()      
            self.cursor.execute(query)
            self.connection.commit()
            success = True
        except sqlite3.Error as ex:
            result = f"The following sqlite error ocurred while creating the tasks table: {str(ex)}"
        except Exception as ex:
            result = f"The following general error ocurred while creating the tasks table: {str(ex)}"
        finally:
            self._disconnect()
        return success, result



