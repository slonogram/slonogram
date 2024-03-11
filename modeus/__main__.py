import sys
import json

from .args import parse_args
from .subtypes_group import group_by_subtype
from .spec import Specification, SPEC_RETORT

from .stages import config

args = parse_args(sys.argv[1:])
with open(args.spec, 'rb') as fp:
    raw_spec = json.load(fp)
    spec = SPEC_RETORT.load(raw_spec, Specification)

types_grouped = group_by_subtype(spec.types)

match args.type:
    case "config":
        output = args.output
        schema_dir = output / 'schemas'
        methods_dir = output / 'methods'
        
        for path in [output, schema_dir, methods_dir]:
            path.mkdir(parents=True, exist_ok=True)
        
        config.run(spec.types, types_grouped, schema_dir)

    case "code":
        pass

