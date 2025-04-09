class SalaryCalculationException(Exception):
    def __init__(self, message="Invalid salary data. Salary values must be non-negative."):
        self.message = message
        super().__init__(self.message)
