import logging
import subprocess
import time
import jinja2

from pathlib import Path
from typing import Any
from mkdocs.config.defaults import MkDocsConfig


logger = logging.getLogger("mkdocs.hooks")


def do_startswith(value: str, prefix: str) -> bool:
    return value.startswith(prefix)


def on_env(env: jinja2.Environment, **kwargs: Any) -> None:
    env.tests["startswith"] = do_startswith


def jupyterlite_build(output_dir: str) -> None:
    logger.info(f"Building JupyterLite...")
    output_dir = Path(output_dir) / "jupyterlite"
    lite_dir = Path(__file__).parent / "jupyterlite"

    start = time.monotonic()
    result = subprocess.run(
        ("jupyter", "lite", "build", "--lite-dir", lite_dir, "--output-dir", output_dir),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    result.check_returncode()

    logger.info(f"JupyterLite built in {time.monotonic() - start:.2f} seconds")


def on_post_build(config: MkDocsConfig) -> None:
    jupyterlite_build(config.site_dir)
