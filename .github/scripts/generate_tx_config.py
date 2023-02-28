"""Please note that this script requires a Transifex API token to run."""
import glob
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
    pattern = (
        resource.replace("trans/<lang>/", "")
        .replace("glossary_", "glossary")
        .replace("--", "/")
        .replace("_", "?")
    )
    matches = list(glob.glob(pattern.replace(".po", ".rst")))
    if not matches:
        print("missing", pattern)
        return f"{prefix}{resource}\n{override_prefix}{pattern}"
    elif len(matches) == 1:
        filename = matches[0].replace(".rst", ".po").replace("\\", "/")
    else:
        raise ValueError("multi match", resource, pattern, matches)
    return f"{prefix}{resource}\n{override_prefix}{filename}"


def patch_config(path: str):
    tx_config_path = Path(".tx", "config")

    config_content = tx_config_path.read_text("utf-8")

    cwd = os.getcwd()
    os.chdir(path)
    config_content = FILTER_PATTERN.sub(name_replacer, config_content)
    os.chdir(cwd)

    tx_config_path.write_text(config_content, "utf-8")


if __name__ == "__main__":
    from argparse import ArgumentParser
    import os

    parser = ArgumentParser()

    parser.add_argument("--token", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--doc-path", required=True)

    params = parser.parse_args()

    os.environ["TX_TOKEN"] = params.token

    init_project()
    add_files(params.version)
    patch_config(params.doc_path)
