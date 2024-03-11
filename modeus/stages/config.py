from pathlib import Path
from yaml import safe_dump, safe_load
from typing import Any
from adaptix import Retort

from ..utils import to_snake_case
from ..subtypes_group import SubtypesGrouped

from ..config.type import Struct, AnyType, TypeAlias
from ..config import RevisedConfig
from ..spec import Type

REVISED_CONFIG_RETORT = Retort()

def dump(o: Any) -> str:
    return safe_dump(
        o,
        None,
        indent=2,
        sort_keys=False,
    )

def is_dirty(path: Path) -> bool:
    return safe_load(path.read_text())['dirty']

def skipped_dirty(path: Path) -> None:
    print(f'>> {path} skipped (marked as dirty)')

def run(orig: dict[str, Type], group: SubtypesGrouped, out: Path) -> None:
    for name, tp in group.free.items():
        snake_name = to_snake_case(name)
        path = out / f'{snake_name}.yaml'

        if path.exists() and is_dirty(path):
            skipped_dirty(path)
            continue

        revised = RevisedConfig(
            dirty=False, 
            file_name=f'{snake_name}.py',
            data=Struct(tp.description, tp.fields),
        )

        data = REVISED_CONFIG_RETORT.dump(revised, RevisedConfig[Struct])
        path.write_text(dump(data))

    for parent, subtypes in group.subtyped.items():
        snake_parent_name = to_snake_case(parent)
        path = out / f'{snake_parent_name}.yaml'

        if path.exists() and is_dirty(path):
            skipped_dirty(path)
            continue

        types: list[AnyType] = []
        for name, subtype in subtypes.items():
            struct = Struct(
                description=subtype.description,
                fields=subtype.fields,
            )
            types.append(struct)

        parent_tp = orig[parent]
        types.append(TypeAlias(parent_tp.description, list(subtypes.keys())))

        revised_sub: RevisedConfig[list[AnyType]] = RevisedConfig(
            dirty=False,
            file_name=f'{snake_parent_name}.py',
            data=types,
        )

        data = REVISED_CONFIG_RETORT.dump(revised_sub, RevisedConfig[list[AnyType]])
        path.write_text(dump(data))


__all__ = ["run"]
