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
pip3 install -q -r requirements.txt
make html SPHINXOPTS="-D language=$LOCALE -D gettext_compact=0 -D html_copy_source=False -W --keep-going" 2> >(error)
