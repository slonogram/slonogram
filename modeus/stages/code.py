from pathlib import Path
from typing import Iterable

from ..utils import to_snake_case
from ..spec import Specification

from ..type_parser import (
    Tracker,
    rename,
    apply_tracker,
    TypeParser,
    parse_union,
    strip_array,
    restore_array_of,
)
from ..imports_tracker import ImportsTracker

from ..config import try_load_revised, RevisedConfig
from ..config.type import AnyType, Struct, TypeAlias

from ..codegen.dataclass import create_dataclass
from ..codegen.variable import create_variable
from ..codegen.type_alias import create_type_alias

def _run_type(parser: TypeParser, tracker: Tracker, tp: AnyType) -> str:
    if isinstance(tp, Struct):
        return create_dataclass(
            tp.meta.name,
            '\n'.join(tp.meta.description) + f"\nTelegram docs: {tp.meta.href}",
            list(tp.fields.values()),
            parser,
            tracker,
        )
    elif isinstance(tp, TypeAlias):
        return create_type_alias(
            tp.meta.name,
            parse_union(parser, tp.union),
            tracker,
        )
    else:
        raise NotImplementedError(f"Not implemented converter for {tp!r}")

def _run_types(
    parser: TypeParser,
    tracker: Tracker,
    tps: Iterable[AnyType],
) -> str:
    return "\n".join(map(
        lambda tp: _run_type(parser, tracker, tp),
        tps,
    ))

def get_group_name_if_any(
    spec: Specification,
    item: str,
    tracker: Tracker,
) -> str | None:
    depth, item = strip_array(item)

    if item not in spec.types:
        return None
    tp = spec.types[item]
    if tp.subtype_of:
        parent = to_snake_case(tp.subtype_of[0])
        tracker('slonogram.schemas', parent)

        return restore_array_of(depth, f'_{parent}.{item}')
    return None

def grab_tp_name(tp: AnyType) -> str:
    return repr(tp.meta.name)

def run(
    schemas_in: Path,
    methods_in: Path,

    schemas_out: Path,
    methods_out: Path,
    spec: Specification,
) -> None:
    schemas_imports = {}
    for file in schemas_in.iterdir():
        cfg: RevisedConfig[AnyType] = try_load_revised(AnyType, file)
        values = list(cfg.data.values())
        values.sort(key=lambda x: isinstance(x, TypeAlias))

        pkg = file.with_suffix('').name
        py_file = f'{pkg}.py'
        out = schemas_out / py_file

        base_tracker = ImportsTracker()
        parser = rename(
            apply_tracker(base_tracker),
            lambda item: item if item in cfg.data else get_group_name_if_any(spec, item, base_tracker),
        )
        base_tracker('__future__', 'annotations')

        text = _run_types(parser, base_tracker, values)
        schemas_imports[pkg] = list(map(lambda x: x.meta.name, values))

        out.write_text(
            base_tracker.generate()
            + '\n'
            + text
            + '\n'
            + create_variable(
                '__all__',
                value='[%s]' % ','.join(map(grab_tp_name, values))
            )
        )
        print(f'> Wrote {out}')
    
    imports = ""
    all_items = ""
    for pkg, models in schemas_imports.items():
        imports += f"from slonogram.schemas.{pkg} import %s" % ','.join(models) + "\n"
        all_items += ",".join(map(repr, models)) + ','

    (schemas_out / '__init__.py').write_text(
        imports
        + '\n'
        + create_variable('__all__', f'[{all_items}]')
    )


__all__ = ['run']
