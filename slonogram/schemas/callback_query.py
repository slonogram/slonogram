import dataclasses as dtc


@dtc.dataclass(slots=True)
class CallbackQuery:
    data: str
