codegen:
    python -m modeus -s telegram-bot-api-spec/api.min.json -t code slonogram/
    ruff format slonogram/schemas
    ruff format slonogram/dispatching/interested.py
