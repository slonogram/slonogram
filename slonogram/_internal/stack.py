import inspect

def get_caller_module_name(up_frames: int) -> str | None:
    stack = inspect.stack()
    try:
        module = inspect.getmodule(stack[up_frames + 2].frame)
        if module is None:
            return None

        return module.__name__
    except IndexError:
        return None

