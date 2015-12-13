#!/bin/sh

set -ev

cd $TRAVIS_BUILD_DIR
echo "Current directory" `pwd`

python -m unittest discover -s merou -p "*.py"
