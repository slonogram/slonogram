class NoFeatureError(Exception):
    def __init__(self, feature: str, message: str) -> None:
        self.feature = feature

        super().__init__(
            f"{message}, perhaps you forgot to add {feature!r} in the dependency extra?"
        )


__all__ = ["NoFeatureError"]
