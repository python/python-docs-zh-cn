#!/bin/bash

cd cpython || exit 1

# Restore git timestamp for enabling build cache
rev=HEAD
for f in $(git ls-tree -r -t --full-name --name-only "$rev") ; do
    touch -d $(git log --pretty=format:%cI -1 "$rev" -- "$f") "$f";
done

cd ..
cd docs || exit 1

# Restore git timestamp for enabling build cache
rev=HEAD
for f in $(git ls-tree -r -t --full-name --name-only "$rev") ; do
    touch -d $(git log --pretty=format:%cI -1 "$rev" -- "$f") "$f";
done

$(realpath ../tx) pull --languages "$LOCALE" -t --use-git-timestamps --workers 25 --silent
