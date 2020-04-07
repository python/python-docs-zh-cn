#!/bin/bash

set -e
set -o pipefail

error() {
  while read -r line; do
    echo
    echo ::error::"$line"
  done
}

cd cpython/Doc || exit 1
mkdir -p locales/"$LOCALE"/
ln -sfn "$(realpath ../../docs)" locales/"$LOCALE"/LC_MESSAGES

# make venv
# create venv manually, so we can specify sphinx version
VENVDIR=./venv
python3 -m venv $VENVDIR
$VENVDIR/bin/python3 -m pip install -U pip setuptools
$VENVDIR/bin/python3 -m pip install -U "Sphinx<3.0" blurb python-docs-theme
make html VENVDIR=$VENVDIR SPHINXOPTS="-D language=$LOCALE -D gettext_compact=0 -W --keep-going -j2" 2> >(error)
