#!/bin/bash

THIS_DIR=$(dirname "$0")
cd ${THIS_DIR}

./save.sh

cp templates/codejam.cpp a.cpp
cp templates/default.py a.py
