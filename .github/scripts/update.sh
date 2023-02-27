#!/bin/bash


cd docs || exit 1
tx pull --languages "$LOCALE"
