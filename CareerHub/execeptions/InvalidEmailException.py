class InvalidEmailException(Exception):
    def __init__(self, message="Invalid email format. Please enter a valid email address."):
        self.message = message
        super().__init__(self.message)
