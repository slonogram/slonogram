from pathlib import Path
from shutil import rmtree

from modeus.spec import Specification
from modeus.gen.docstring import create_docstring

from . import schemas

def write_specification_note(spec: Specification) -> str:
    return (
        "@generated using `modeus`\n"
        f"BotAPI version: {spec.version}\n"
        f"BotAPI changelog: {spec.changelog}\n"
        f"BotAPI release date: {spec.release_date}\n"
    )

def run(
    stages_input: Path,
    stages_output: Path,

    spec: Specification,
) -> None:
    schemas_in = stages_input / 'schemas'
    methods_in = stages_input / 'methods'

    schemas_out = stages_output / 'schemas'
    methods_out = stages_output / 'methods'

    print(f"Removing {schemas_out}...")
    rmtree(schemas_out, ignore_errors=True)

    print(f"Removing {methods_out}...")
    rmtree(methods_out, ignore_errors=True)

    schemas_out.mkdir(parents=True)
    methods_out.mkdir(parents=True)

    note = create_docstring(write_specification_note(spec), wrap_width=None)

    print("!! Running schemas sub-stage...")
    schemas.run(note, schemas_in, schemas_out, spec)

