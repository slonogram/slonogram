setup_dev:
    poetry install --with docs,test,dev,build --all-extras

shell:
    poetry shell

lint_mypy:
    python -m mypy slonogram                    \
        --strict                                \
        --disable-error-code no-any-return

lint: lint_mypy

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
