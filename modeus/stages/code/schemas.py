from typing import Callable
from pathlib import Path

from modeus.typing.tracking import Tracker
from modeus.typing.parser import TypeParser, parse_union, apply_tracker
from modeus.typing.collector import Collector
from modeus.typing.layers import AndMappable, do_not_track, map_item

from modeus.config import RevisedConfig, try_load_revised
from modeus.config.type import (
    Meta,
    Enum,
    Struct,
    AnyType,
    TaggedUnion,
)
from modeus.spec import Type, Specification

from modeus.gen.type_alias import create_type_alias
from modeus.gen.dataclass import create_dataclass
from modeus.gen.stmts import create_stmts
from modeus.gen.all import create_all
from modeus.gen.variable import create_variable

from modeus.utils import to_snake_case

def run(
    note: str,
    schemas_in: Path,
    schemas_out: Path,
    spec: Specification,
) -> None:
    base_schemas = Collector()
    schemas_collector = (
        AndMappable(base_schemas)
        & map_item('<schemas>', track_schema(spec.types, dotted=False))
    )
    for schema_file in schemas_in.iterdir():
        config: RevisedConfig[AnyType] = try_load_revised(AnyType, schema_file)
        
        snake_name = schema_file.with_suffix('').name
        py_file = f'{snake_name}.py'
        out_path = schemas_out / py_file

        for tp in config.data.values():
            type_name = tp.meta.name
            schemas_collector('<schemas>', type_name)

        base = Collector()
        collector = (
            AndMappable(base)
            & map_item('<schemas>', track_schema(spec.types))
            & do_not_track('<schemas>', lambda name: name in config.data)
        )
        collector('__future__', 'annotations')
        type_parser = apply_tracker(collector)

        code = '\n'.join(
            _run_type(collector, type_parser, tp)
            for tp_name, tp in sorted(
                config.data.items(),
                key=lambda pair: isinstance(pair[1], TaggedUnion)
            )
        )

        out_path.write_text(create_stmts((
            note,
            base.generate(),
            code,
            create_all(config.data.keys())
        )))
        print(f'> Wrote {out_path}')
    
    (schemas_out / '__init__.py').write_text(create_stmts((
        note,
        base_schemas.generate(),
        create_variable('__all__', base_schemas.generate_all())
    )))

# Utils

def _make_docs(meta: Meta) -> str:
    return (
        '\n'.join(meta.description)
        + '\n\n'
        + f'Telegram documentation: {meta.href}'
    )

def track_schema(types: dict[str, Type], dotted: bool = True) -> Callable[[str, Tracker], str]:
    def inner(name: str, tracker: Tracker) -> str:
        type_in_spec = types[name]
        if type_in_spec.subtype_of:
            base = type_in_spec.subtype_of[0]
            module = to_snake_case(base)
        else:
            module = to_snake_case(name)

        if dotted:
            return tracker('slonogram.schemas', module) + f'.{name}'
        return tracker(f'slonogram.schemas.{module}', name)

    return inner

def _run_enum(tracker: Tracker, enum: Enum) -> str:
    raise NotImplementedError

def _run_struct(
    tracker: Tracker,
    parser: TypeParser,
    struct: Struct,
) -> str:
    return create_dataclass(
        struct.meta.name,
        _make_docs(struct.meta),
        list(struct.fields.values()),
        parser,
        tracker,
    )

def _run_type_alias(
    tracker: Tracker,
    parser: TypeParser,
    alias: TaggedUnion,
) -> str:
    tp = parse_union(parser, alias.union)
    return create_type_alias(
        alias.meta.name,
        tp,
        _make_docs(alias.meta),
        tracker,
    )

def _run_type(
    tracker: Tracker,
    parser: TypeParser,
    tp: AnyType,
) -> str:
    if isinstance(tp, TaggedUnion):
        return _run_type_alias(tracker, parser, tp)
    elif isinstance(tp, Enum):
        return _run_enum(tracker, tp)
    elif isinstance(tp, Struct):
        return _run_struct(tracker, parser, tp)
    else:
        raise NotImplementedError(f'Not implemented runner for {tp!r}')
