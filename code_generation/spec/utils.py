from keyword import kwlist


def to_snake_case(camel: str) -> str:
    if not camel:
        return camel
    snake = ""

    if camel[0].isupper():
        snake += camel[0].lower()
    else:
        snake += camel[0]

    for offset in range(1, len(camel)):
        char = camel[offset]
        if char.isupper():
            snake += "_" + char.lower()
            continue
        snake += char
    return snake


def escape_kw(string: str) -> str:
    if string in kwlist:
        return string + "_"
    return string
