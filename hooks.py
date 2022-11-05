import jinja2

from typing import Any


def do_startswith(value: str, prefix: str) -> bool:
    return value.startswith(prefix)


def on_env(env: jinja2.Environment, **kwargs: Any) -> None:
    env.tests["startswith"] = do_startswith
