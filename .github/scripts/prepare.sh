#!/bin/bash

set -ex

pip3 install --user setuptools
curl -o- https://raw.githubusercontent.com/transifex/cli/master/install.sh | bash
sudo apt-get update
sudo apt-get install -y python3-venv
