from datetime import datetime

class ApplicationDeadlineException(Exception):
    def __init__(self, message="Application deadline has passed. You cannot apply anymore."):
        self.message = message
        super().__init__(self.message)

def submit_application(deadline):
    current_date = datetime.now()
    if current_date > deadline:
        raise ApplicationDeadlineException()
    print("Application submitted successfully!")

try:
    deadline = datetime(2025, 5, 1)  # Example deadline
    submit_application(deadline)
except ApplicationDeadlineException as e:
    print(e)
