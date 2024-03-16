def decorate(expr: str, value: str) -> str:
    return f'@{expr}\n{value}'

__all__ = ["decorate"]
