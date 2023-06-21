#!/bin/bash

set -ex

cd docs || exit 1
git config user.email "github-actions[bot]@users.noreply.github.com"
git config user.name "github-actions[bot]"
if ! git status -s|grep '\.po'; then
  echo "Nothing to commit"
  exit 0
fi
git add .
git commit -m '[po] auto sync'
git push
