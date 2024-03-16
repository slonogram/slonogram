def create_variable(
    name: str,
    value: str | None = None,
    type: str | None = None,
) -> str:
    out = name
    if value is None and type is None:
        raise ValueError(
            "Variable can be either forward declaration (contain type) or assignment (contain value), got neither"
        )
    
    if type is not None:
        out += f': {type}'
    if value is not None:
        out += f' = {value}'
    return out

__all__ = ["create_variable"]
