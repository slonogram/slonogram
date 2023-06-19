class _ShowIsABug(Exception):
    def __init__(self) -> None:
        super().__init__(
            "This exception should never be shown, "
            "this is a bug in `slonogram`"
        )


class SkipLocalSet(_ShowIsABug):
    pass


__all__ = ["SkipLocalSet"]
