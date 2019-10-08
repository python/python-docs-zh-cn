#!/usr/bin/env python3

from txclib import project
from txclib.utils import perform_parallel_requests


def pull(path, lang):
    skip_decode = False
    params = {}
    parallel = True

    prj = project.Project(path)
    resource_list = prj.get_chosen_resources([])
    for resource in resource_list:
        project_slug, resource_slug = resource.split(".", 1)
        host = prj.get_resource_host(resource)
        prj._set_url_info(host=host, project=project_slug, resource=resource_slug)

        files = prj.get_resource_files(resource)
        url = prj._get_url_by_pull_mode(None)
        local_file = files.get(lang)
        prj.do_url_request(
            url,
            language=lang,
            skip_decode=skip_decode,
            params=params,
            parallel=parallel,
            callback=prj._save_file,
            callback_args={"local_file": local_file},
        )

    perform_parallel_requests()


if __name__ == "__main__":
    import os

    pull(os.getcwd(), os.getenv("LOCALE", "zh_CN"))
