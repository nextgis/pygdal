#!/bin/bash
set -e

TMP=`mktemp -d`
cp -LR $1/* $TMP
cd $TMP
python setup.py sdist
twine upload --skip-existing dist/*
cd -