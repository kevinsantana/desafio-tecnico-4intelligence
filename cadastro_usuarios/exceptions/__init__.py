class UserRegistrationException(Exception):
    def __init__(self, status: int, message: str):
        self.status = status
        self.message = message
