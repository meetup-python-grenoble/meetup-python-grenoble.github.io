import logging
import subprocess
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
    output_path = Path(output_dir) / "jupyterlite"
    logger.info(f"Building JupyterLite in {output_path}")
    result = subprocess.run(
        ("jupyter", "lite", "build", "--output-dir", output_path),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    result.check_returncode()


def on_post_build(config: MkDocsConfig) -> None:
    jupyterlite_build(config.site_dir)
