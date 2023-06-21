class ApiError(Exception):
    def __init__(self, code: int, description: str) -> None:
        self.code = code
        self.description = description

        super().__init__(f"{description} (code = {code})")
