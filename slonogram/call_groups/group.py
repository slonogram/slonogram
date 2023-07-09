from adaptix import Retort
from typing import TypeVar, Type, Iterable, Tuple, Any, Generic, Optional

from ..utils.json import dumps
from ..types.api_session import (
    ApiSession,
    MethodArgs,
    ScalarSerializable,
)
from ..exceptions.api_error import ApiError

T = TypeVar("T")


class UseRetort(Generic[T]):
    __slots__ = "name", "value"

    def __init__(self, name: str, value: Optional[T]) -> None:
        self.name = name
        self.value = value


class CallsGroup:
    def __init__(self, retort: Retort, session: ApiSession) -> None:
        self._session = session
        self._retort = retort

    async def _call(
        self,
        ty: Type[T],
        method: str,
        args: MethodArgs,
        optional_args: Iterable[
            Tuple[str, Optional[ScalarSerializable]] | UseRetort[Any]
        ] = [],
    ) -> T:
        retort = self._retort
        for arg in optional_args:
            if isinstance(arg, UseRetort):
                i_value = arg.value
                if i_value is None:
                    continue

                name = arg.name
                value = dumps(retort.dump(i_value))

                args[name] = value
            else:
                key, value = arg  # type: ignore
                if value is not None:
                    args[key] = value

        result = await self._session.call_method(method, args)
        if not result["ok"]:
            raise ApiError(
                result["error_code"],
                result["description"],
            )

        # TODO: Do we need ability to "delay" model loading?
        # for example, when result is not used
        return self._retort.load(result["result"], ty)
