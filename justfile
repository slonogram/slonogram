setup_dev:
    python3.11 -m poetry install --with docs,test,dev,build --all-extras

shell:
    python3.11 -m poetry shell

lint_mypy:
    python3.11 -m mypy slonogram                \
        --strict                                \
        --disable-error-code no-any-return

lint: lint_mypy

build:
    rm -f slonogram/schemas.py
    rm -rf slonogram/methods/
    rm -f slonogram/_internal/shortcuts.py
    rm -f slonogram/_internal/api_wrapper.py

    python3.11 -m code_generation                              \
        --methods-output slonogram/methods                     \
        --schemas-output slonogram/schemas.py                  \
        --internals-path slonogram/_internal/                  \
        third-party/telegram-bot-api-spec/api.json
    
    python3.11 -m black slonogram/schemas.py            \
                    slonogram/methods/                  \
                    slonogram/_internal/

test:
    python3.11 -m pytest
