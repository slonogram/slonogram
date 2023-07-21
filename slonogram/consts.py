from adaptix import name_mapping, Retort, P
from slonogram import schemas

DEFAULT_API_URL = "https://api.telegram.org/"
COMMAND_REGEX = r"\/([\w\d_\-]+)(@([\w\d_]+))?"
BASE_RECIPES = [
    name_mapping(schemas.Update, map={"id": "update_id"}),
    name_mapping(schemas.Message, map={"id": "message_id"}),
    name_mapping(trim_trailing_underscore=True),
    name_mapping(omit_default=~P["type"]),
]
DEFAULT_RETORT = Retort(recipe=BASE_RECIPES)
MODEL_TYPES = (
    schemas.Message,
    schemas.CallbackQuery,
    schemas.InlineQuery,
)

__all__ = [
    "COMMAND_REGEX",
    "DEFAULT_API_URL",
    "BASE_RECIPES",
    "DEFAULT_RETORT",
    "MODEL_TYPES",
]
