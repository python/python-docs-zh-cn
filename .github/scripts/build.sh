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

# Hotfix for #227
sed -i 's|Sphinx==2.3.1|Sphinx==2.3.1 "docutils<0.18"|g'  Makefile
make venv
make html SPHINXOPTS="-D language=$LOCALE -D gettext_compact=0 -W --keep-going -j2" 2> >(error)
