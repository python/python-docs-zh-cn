#!/bin/bash

set -ex

script_dir="$(dirname "$(realpath "$0")")"

if [[ -n "$TRANSIFEX_APIKEY" ]]; then
  cat > ~/.transifexrc << EOF
[https://www.transifex.com]
api_hostname = https://api.transifex.com
hostname = https://www.transifex.com
password = $TRANSIFEX_APIKEY
username = api
EOF
fi

cd docs || exit 1
"$script_dir"/transifex_pull.py
