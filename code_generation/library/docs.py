from .type_hint import TypeHint
from dataclasses import dataclass


@dataclass
class DocRaises:
    exception: str
    description: str


class SphinxDoc:
    def __init__(
        self,
        summary: str,
        parameters: list[tuple[str, str]],
        return_doc: str,
        rtype: TypeHint,
        raises: list[DocRaises] | None = None,
    ) -> None:
        self.summary = summary
        self.parameters = parameters
        self.return_doc = return_doc
        self.raises = raises
        self.rtype = rtype

    def __repr__(self) -> str:
        paramlist = "\n".join(
            f":param {name}: {description}" for name, description in self.parameters
        )
        if self.raises:
            raises = (
                "\n"
                + "\n".join(
                    f":raises {d.exception}: {d.description}" for d in self.raises
                )
                + "\n"
            )
        else:
            raises = ""

        return f"{self.summary}\n\n{paramlist}{raises}:return: {self.return_doc}\n:rtype: {self.rtype!r}"
