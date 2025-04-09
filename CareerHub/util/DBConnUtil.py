# In util/DBConnUtil.py

import pyodbc

class DBConnUtil:
    def __init__(self, connection=None):
        self.connection = connection

    def connect(self):
        if not self.connection:
            raise Exception("Database connection is not established.")
        return self.connection

    def execute_query(self, query, params=None):
        """
        Executes a query against the connected database.
        """
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query, params or [])
                connection.commit()  # Committing the transaction
                return cursor.fetchall()  # Returning the result of the query (if any)
            except Exception as e:
                print(f"Error executing query: {e}")
                return None
        else:
            print("No connection available.")
            return None

    def fetch_query(self, query, params=None):
        """
        Fetches data from the database.
        """
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query, params or [])
                return cursor.fetchall()  # Returning the result of the query
            except Exception as e:
                print(f"Error fetching query: {e}")
                return None

    def close(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
