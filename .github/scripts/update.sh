#!/bin/bash

cd docs || exit 1
$(realpath ../tx) pull --languages "$LOCALE" -t --use-git-timestamps --worker 25
