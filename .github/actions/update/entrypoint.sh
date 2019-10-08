#!/bin/bash

set -ex

pythonVersion="$1"
locale="$2"

echo "Python Version: $pythonVersion"
echo "Locale: $locale"

cur=$(pwd)
git clone --depth=1 --branch="$pythonVersion" https://github.com/python/cpython cpython
git clone --branch="$pythonVersion" https://github.com/"$GITHUB_REPOSITORY" docs

if [[ -n "$TRANSIFEX_APIKEY" ]]; then
  cat > ~/.transifexrc << EOF
[https://www.transifex.com]
api_hostname = https://api.transifex.com
hostname = https://www.transifex.com
password = $TRANSIFEX_APIKEY
username = api
EOF
fi

# Pull Transifex translation
pushd docs || exit 1
tx pull --force --parallel --language "$locale"
popd || exit 1

# Test building docs
pushd cpython/Doc || exit 1
mkdir -p locales/"$locale"/
ln -sfn "$cur"/docs locales/"$locale"/LC_MESSAGES
make venv
make html SPHINXOPTS="-D language=$locale -D gettext_compact=0 -j4 -W --keep-going"
popd || exit 1
