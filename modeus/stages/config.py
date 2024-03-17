from pathlib import Path
from shutil import rmtree

from ..spec import Type
from ..config.type import AnyType, Struct, TypeAlias, Meta
from ..config import RevisedConfig, try_load_revised, dump_revised

from ..utils import to_snake_case

def run(group: dict[str, dict[str, Type]], schemas_out: Path) -> None:
    print(f"Removing {schemas_out}...")
    rmtree(schemas_out, ignore_errors=True)
    schemas_out.mkdir(parents=True)

    for parent, tps in group.items():
        entries: dict[str, AnyType] = {}
        snake_name = to_snake_case(parent)
        file_name = f'{snake_name}.yaml'
        config_path = schemas_out / file_name

        try:
            revised: RevisedConfig[AnyType] = try_load_revised(AnyType, config_path)
            if revised.dirty:
                print(f">> {config_path} skipped (dirty)")
                continue
        except FileNotFoundError:
            pass

        for name, tp in tps.items():
            meta = Meta(
                name=tp.name,
                description=tp.description,
                href=tp.href,
            )
            entry: AnyType
            if tp.subtypes:
                entry = TypeAlias(
                    meta=meta,
                    union=tp.subtypes,
                )
            else:
                entry = Struct(meta=meta, fields=tp.fields)

            entries[name] = entry

        revised = RevisedConfig(
            dirty=False,
            data=entries
        )
        config_path.write_text(dump_revised(AnyType, revised))
        print(f'>> wrote {config_path}')

__all__ = ["run"]
