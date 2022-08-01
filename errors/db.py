class DbError(Exception):
    message = "db error"
    details: str
    
    def __init__(self, details: str) -> None:
        self.details = details