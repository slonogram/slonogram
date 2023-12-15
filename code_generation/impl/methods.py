from ..spec import Spec
from ..spec.method import Method, Argument

from ..library.statement import Statement
from ..library.simple import (
    Collection,
)
from ..library.class_ import Class


def _generate_method(method: Method) -> Statement:
    raise NotImplementedError


def generate_methods(spec: Spec) -> tuple[Statement, Class]:
    class_name = "Methods"

    class_ = Class(
        class_name,
    )

    return (
        Collection(
            [
                class_,
            ]
        ),
        class_,
    )
