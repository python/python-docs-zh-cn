#!/bin/bash

tx=$(realpath ./tx)
cd docs || exit 1
$tx pull --languages "$LOCALE" -t --use-git-timestamps
