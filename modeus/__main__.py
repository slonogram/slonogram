import sys
import json
from pathlib import Path

from .args import parse_args
from .spec import Specification, SPEC_RETORT

from .subtypes_group import group_by_subtype
from .stages import config, code

args = parse_args(sys.argv[1:])
with open(args.spec, "rb") as fp:
    raw_spec = json.load(fp)
    spec = SPEC_RETORT.load(raw_spec, Specification)


output = args.output
schema_dir = output / "schemas"
methods_dir = output / "methods"
for path in [output, schema_dir, methods_dir]:
    path.mkdir(parents=True, exist_ok=True)

match args.type:
    case "config":
        group = group_by_subtype(spec.types)
        config.run(group, schema_dir)

    case "code":
        root = Path('.modeus')
        code.run(
            root / 'schemas',
            root / 'methods',
            schema_dir,
            methods_dir,
            spec,
        )
