from pathlib import Path
from argparse import ArgumentParser
from typing import Literal, TypeAlias, Sequence
from dataclasses import dataclass

GenerationType: TypeAlias = Literal['type'] | Literal['config']

@dataclass(slots=True, frozen=True)
class Args:
    spec: Path
    output: Path

    type: GenerationType


PARSER = ArgumentParser(
    prog='modeus',
    description='code generation for slonogram',
    add_help=True,
)
PARSER.add_argument(
    '-s',
    '--spec',
    type=Path,
    required=True,
    help='Where JSON specification is stored'
)
PARSER.add_argument(
    '-t',
    '--type',
    choices=['config', 'code'],
    required=True,
    help='What type of data needs generation',
)
PARSER.add_argument(
    'output',
    type=Path,
    help='Where store result of generation',
)

def parse_args(args: Sequence[str]) -> Args:
    ns = PARSER.parse_args(args)

    return Args(
        spec=ns.spec,
        output=ns.output,
        type=ns.type,
    )


__all__ = ["parse_args", "Args"]
