class CarNotFoundException(Exception):
    def __init__(self, message="Car not found with the given ID"):
        super().__init__(message)
