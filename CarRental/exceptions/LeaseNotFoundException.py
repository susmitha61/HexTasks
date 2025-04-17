class LeaseNotFoundException(Exception):
    def __init__(self, message="Lease not found with the given ID"):
        super().__init__(message)
