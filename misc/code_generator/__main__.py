from pathlib import Path

from os import mkdir
from sys import argv, exit
from json import load

from .schemas_generator import generate_schemas
from .types import CodegenerationConfig, Spec, RETORT

try:
    config_path = Path(argv[1])
    schemas_path = Path(argv[2])
    call_groups_directory = Path(argv[3])
except IndexError:
    print(
        "usage: misc.code_generator <config_path>"
        " <schemas_outpath> <call_groups_directory>"
    )
    exit(1)

config = CodegenerationConfig.read_from(config_path)
spec_root = Path(__file__).parent.parent / "telegram-bot-api-spec"
raw_spec = load(open(spec_root / "api.min.json"))
spec = RETORT.load(raw_spec, Spec)

if not call_groups_directory.exists():
    print(f"> mkdir {call_groups_directory}")
    mkdir(call_groups_directory)

if not (call_groups_directory / "__init__.py").exists():
    print("> creating __init__.py file in the call groups directory")
    open(call_groups_directory / "__init__.py", "wb").close()

schemas = generate_schemas(spec, config)

with open(schemas_path, "w") as fp:
    wrote = fp.write(schemas)
    print(f">>[Schema] Wrote {wrote} bytes to {schemas_path}")
