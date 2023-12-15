from argparse import ArgumentParser
from datetime import datetime
from json import load


from .spec.parser import parse_spec_from

from .library.simple import MultilineComment, Collection
from .library.statement import Statement
from .impl import (
    schemas as impl_schemas,
)


parser = ArgumentParser(
    prog="code_generation",
    description="generates code for the Telegram API",
)

parser.add_argument("spec_file")

parser.add_argument("-m", "--methods-output", required=True)
parser.add_argument("-s", "--schemas-output", required=True)
parser.add_argument("-o", "--shortcuts-output", required=True)

ns = parser.parse_args()

with open(ns.spec_file) as fp:
    spec = parse_spec_from(load(fp))

header = MultilineComment(
    [
        f"This file was automatically @generated via code_generation package",
        f"Do not edit it directly",
        f"",
        f"Version: {spec.version}",
        f"Changelog: {spec.changelog}",
        f"Release date: {spec.release_date}",
        f"Generated at: {datetime.now()!s}",
    ]
)


def _with_header(stmt: Statement) -> str:
    return Collection((header, stmt)).generate()


schemas = impl_schemas.generate_schemas(spec)

with open(ns.schemas_output, "w") as fp:
    no_wrote = fp.write(_with_header(schemas))
    print(f">> Wrote {no_wrote} bytes to the {ns.schemas_output}")
