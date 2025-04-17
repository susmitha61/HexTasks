class CustomerNotFoundException(Exception):
    def __init__(self, message="Customer not found with the given ID"):
        super().__init__(message)
