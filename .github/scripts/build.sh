#!/bin/bash

set -e
set -u
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
sphinx-build -b dummy -d build/doctrees  -j auto -D language=$LOCALE -D gettext_compact=0 -W --keep-going -W . build/html 2> >(error)
