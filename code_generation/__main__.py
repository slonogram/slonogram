import json
import adaptix

from datetime import datetime
from typing import Any
from argparse import ArgumentParser

from .spec_models.schemas import Model
from .spec_models.methods import Method
from .codegen.schemas import codegenerate_models


parser = ArgumentParser(
    prog="code_generation",
    description="Code generation script for the slonogram",
)

parser.add_argument("-t", "--type", choices=["schemas", "methods"], required=True)
parser.add_argument("spec_file")

args = parser.parse_args()

with open(args.spec_file, "rb") as fp:
    raw_json: dict[str, Any] = json.load(fp)

print("# This file is automatically generated, do not edit it directly")
print("# version:", raw_json["version"], f"({raw_json['release_date']})")
print("# generated at:", str(datetime.now()))

match args.type:
    case "schemas":
        models = adaptix.Retort().load(raw_json["types"], dict[str, Model])
        print(codegenerate_models(models.values()))
    case "methods":
        methods = adaptix.Retort(
            recipe=[adaptix.name_mapping(Method, map={"arguments": "fields"})]
        ).load(raw_json["methods"], dict[str, Method])