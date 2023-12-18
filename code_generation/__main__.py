from argparse import ArgumentParser
from pathlib import Path
from datetime import datetime
from json import load

from .spec.utils import to_snake_case
from .spec.parser import parse_spec_from

from .library.simple import MultilineComment, Collection, FromImport, AllExports
from .library.statement import Statement
from .impl import (
    schemas as impl_schemas,
    methods as impl_methods,
)
from .impl.shortcuts.impl import generate_shortcuts_def


parser = ArgumentParser(
    prog="code_generation",
    description="generates code for the Telegram API",
)

parser.add_argument("spec_file")

parser.add_argument("-m", "--methods-output", required=True)
parser.add_argument("-s", "--schemas-output", required=True)
parser.add_argument("-i", "--internals-path", required=True)

ns = parser.parse_args()

with open(ns.spec_file) as fp:
    spec = parse_spec_from(load(fp))

header = MultilineComment(
    [
        "This file was automatically @generated via code_generation package",
        "Do not edit it directly",
        "",
        f"Version: {spec.version}",
        f"Changelog: {spec.changelog}",
        f"Release date: {spec.release_date}",
    ]
)


def _with_header(stmt: Statement) -> str:
    return Collection((header, stmt)).generate()


schemas = impl_schemas.generate_schemas(spec)

methods_output = Path(ns.methods_output)
internals_path = Path(ns.internals_path)

methods_output.mkdir(parents=True, exist_ok=True)

with open(ns.schemas_output, "w") as fp:
    no_wrote = fp.write(_with_header(schemas))
    print(f">> Wrote {no_wrote} bytes to the {ns.schemas_output}")


methods_init_body: list[Statement] = []
methods_exports: list[str] = []

for method in spec.methods.values():
    snake_name = to_snake_case(method.name)
    out_path = methods_output / f"{snake_name}.py"
    generated = impl_methods.generate_method(method, spec.models)
    imports = impl_methods.generate_imports_for(generated)

    methods_exports.append(generated.dtc.name)
    methods_init_body.append(FromImport(f".{snake_name}", generated.dtc.name))

    out_path.write_text(
        _with_header(
            Collection(
                [
                    *imports,
                    generated,
                    AllExports([generated.dtc.name]),
                ]
            )
        )
    )

methods_init_body.append(AllExports(methods_exports))
(internals_path / "api_wrapper.py").write_text(
    impl_methods.generate_wrapper(spec.methods).generate()
)
(methods_output / "__init__.py").write_text(_with_header(Collection(methods_init_body)))

shortcuts = generate_shortcuts_def(spec.methods)

(internals_path / "_generated_shortcuts.py").write_text(
    _with_header(
        Collection(
            [
                *impl_methods.generate_imports_for(shortcuts),
                shortcuts,
            ]
        )
    )
)
