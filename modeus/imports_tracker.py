class ImportsTracker:
    sources: dict[str, set[str]]

    def __init__(self, sources: dict[str, set[str]] | None = None) -> None:
        self.sources = sources or {}
    
    def __call__(self, source: str, value: str) -> None:
        if (tracked := self.sources.get(source)) is not None:
            tracked.add(value)
        else:
            self.sources[source] = {value}
    
    def add_schema(self, tp: str) -> None:
        self('slonogram.schemas', tp)

    def add_typing(self, tp: str) -> None:
        self('typing', tp)
    
    def generate(
        self,
    ) -> str:
        return '\n'.join(
            'from {} import {}'.format(source, ', '.join(
                f'{name} as _{name}' if source == 'slonogram.schemas' else name for name in names
            ))
            for source, names in self.sources.items()
        )

__all__ = ["ImportsTracker"]
