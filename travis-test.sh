#!/usr/bin/env bash

set -e
if [ "$USE_CYTHON" == "true" ]
then
    pip install cython
    python setup.py develop --use-cython
else
    python setup.py develop
fi
nosetests --with-doctest --doctest-tests --cover-package=proj --with-coverage --cover-tests --cover-erase --cover-min-percentage=100
