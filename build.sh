#!/bin/sh
set -ex

cur=$(dirname "$(readlink -f "$0")")
cd "$cur"/.. || exit 1
if [ -d cpython ]; then
	(cd cpython; git fetch; git checkout origin/3.7)
else
	git clone --depth=1 --branch=3.7 https://github.com/python/cpython.git
fi
cd cpython/Doc
mkdir -p locales/zh_CN/
ln -sfn "$cur" locales/zh_CN/LC_MESSAGES
make venv
make html SPHINXOPTS='-D language=zh_CN -D html_search_language=zh -D gettext_compact=0 -j4 -W'
