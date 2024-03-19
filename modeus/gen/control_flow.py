def create_return(expr: str) -> str:
    return f"return {expr}"

def create_break() -> str:
    return "break"

def create_continue() -> str:
    return "continue"

__al__ = [
    "create_return",
    "create_break",
    "create_continue",
]
