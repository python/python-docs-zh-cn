"""Please note that this script requires a Transifex API token to run."""
import subprocess
from functools import partial
from pathlib import Path
import re

run = partial(subprocess.run, check=True)


def init_project():
    run(["tx", "init"])


def add_files(version: str):
    run(
        [
            "tx",
            "add",
            "remote",
            "--file-filter",
            "trans/<lang>/<resource_slug>.<ext>",
            f"https://www.transifex.com/python-doc/{version}/dashboard/",
        ]
    )


FILTER_PATTERN = re.compile(
    r"^(?P<prefix>file_filter( *)=( *))(?P<resource>.+)$", re.MULTILINE
)


def name_replacer(match: re.Match[str]):
    prefix, resource = match.group("prefix", "resource")
    override_prefix = prefix.replace("file_filter", "trans.zh_CN")
    override_resource = (
        resource.replace("trans/<lang>/", "")
        .replace("--", "/")
        .replace("glossary_", "glossary")
        .replace("_", ".")
    )
    return f"{prefix}{resource}\n{override_prefix}{override_resource}"


def patch_config():
    tx_config_path = Path(".tx", "config")

    config_content = tx_config_path.read_text("utf-8")
    config_content = FILTER_PATTERN.sub(name_replacer, config_content)
    tx_config_path.write_text(config_content, "utf-8")


if __name__ == "__main__":
    from argparse import ArgumentParser
    import os

    parser = ArgumentParser()

    parser.add_argument("--token")
    parser.add_argument("--version")

    params = parser.parse_args()

    os.environ["TX_TOKEN"] = params.token

    init_project()
    add_files(params.version)
    patch_config()
