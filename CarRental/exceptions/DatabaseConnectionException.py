class DatabaseConnectionException(Exception):
    def __init__(self, message="Failed to connect to the database. Please try again later."):
        self.message = message
        super().__init__(self.message)
