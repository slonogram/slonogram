class CannotProvideError(Exception):
    def __init__(self, tp: type) -> None:
        self.tp = tp

        super().__init__(f"Cannot provide type {tp}")


__all__ = ["CannotProvideError"]
