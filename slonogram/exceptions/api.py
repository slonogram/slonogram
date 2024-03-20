class APIError(Exception):
    def __init__(self, error_code: int, description: str) -> None:
        self.error_code = error_code
        self.description = description

        super().__init__(f"Telegram API error: {description} (code = {error_code})")


__all__ = ["APIError"]
