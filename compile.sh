#!/bin/bash

g++ a.cpp -Wall -g -Wextra -std=c++11 -O0 -o a.out

rc=$?
exit $rc

# Usage ./compile.sh && ./a.out < data.in
