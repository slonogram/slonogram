build:
    rm -f slonogram/schemas.py
    rm -rf slonogram/methods/
    rm -f slonogram/_internal/shortcuts.py
    rm -f slonogram/_internal/api_wrapper.py

    python -m code_generation                                  \
        --methods-output slonogram/methods                     \
        --schemas-output slonogram/schemas.py                  \
        --internals-path slonogram/_internal/                  \
        third-party/telegram-bot-api-spec/api.json
    
    python -m black slonogram/schemas.py                \
                    slonogram/methods/                  \
                    slonogram/_internal/

test:
    python -m pytest
