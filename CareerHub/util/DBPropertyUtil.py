import configparser
import os
from execeptions.DatabaseConnectionException import DatabaseConnectionException
import pyodbc
class DBPropertyUtil:
        def __init__(self, server, database, username=None, password=None):
            self.server = server
            self.database = database
            self.username = username
            self.password = password
            self.connection = None

        def connect(self):
            try:
                # If username and password are provided, use SQL Server Authentication
                if self.username and self.password:
                    self.connection = pyodbc.connect(
                        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                        f'SERVER={self.server};'
                        f'DATABASE={self.database};'
                        f'UID={self.username};'
                        f'PWD={self.password}'
                    )
                else:
                    # Use Windows Authentication if no username and password are provided
                    self.connection = pyodbc.connect(
                        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                        f'SERVER={self.server};'
                        f'DATABASE={self.database};'
                        f'Trusted_Connection=yes;'
                    )

                print("Database connection established successfully!")
                return self.connection

            except pyodbc.Error as e:
                print(f"Error connecting to database (ODBC error): {e}")
                raise DatabaseConnectionException(f"Failed to connect to database: {str(e)}")
            except Exception as e:
                print(f"Unexpected error: {e}")
                raise DatabaseConnectionException(f"Unexpected error establishing connection: {str(e)}")

        def close(self):
            if self.connection:
                self.connection.close()
                self.connection = None
                print("Connection closed successfully.")
            else:
                print("No active connection to close.")