#!/usr/bin/env python3
import glob
import json
import os
import re
import sys
import urllib.request


def list_resources(token, project):
    auth_handler = urllib.request.HTTPBasicAuthHandler()
    auth_handler.add_password(
        realm="api", uri="https://api.transifex.com/", user="api", passwd=token
    )
    opener = urllib.request.build_opener(auth_handler)
    urllib.request.install_opener(opener)
    next_ = (
        "https://api.transifex.com/organizations/python-doc/projects/"
        + project
        + "/resources/"
    )
    resources = []
    while True:
        resp = urllib.request.urlopen(next_)
        result = json.loads(resp.read().decode("utf-8"))
        resources.extend([i["slug"] for i in result])
        link = re.findall('<([^<]*)>; rel="next"', resp.getheader("Link") or "")
        if not link:
            break
        next_ = link[0]
    return resources


def render_config(doc_dir, project, resources):
    os.chdir(doc_dir)
    tpl = """

[{project}.{resource}]
trans.zh_CN = {filename}
source_lang = en
type = PO"""
    conf = """[main]
host = https://www.transifex.com"""
    for resource in sorted(resources):
        if resource == "glossary_":
            filename = "glossary.po"
        elif resource == "sphinx":
            filename = "sphinx.po"
        else:
            pattern = resource.replace("--", "/").replace("_", "?")
            matches = glob.glob(pattern + ".rst")
            if len(matches) == 0:
                print("missing", resource, file=sys.stderr)
                continue
            elif len(matches) == 1:
                filename = matches[0].replace(".rst", ".po")
            else:
                print("multi match", resource, pattern, matches, file=sys.stderr)
        conf += tpl.format(project=project, resource=resource, filename=filename)
    return conf


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--token")
    parser.add_argument("--project")
    parser.add_argument("--doc-dir")
    args = parser.parse_args()

    resources = list_resources(args.token, args.project)
    conf = render_config(args.doc_dir, args.project, resources)
    print(conf)

# vim: set et ts=4 sw=4 sts=4:
