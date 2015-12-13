#!/bin/sh

set -ev

cd $TRAVIS_BUILD_DIR
echo "Current directory" `pwd`

bin/merou -t test_project.json

python -m unittest discover -s merou -p "*.py"
