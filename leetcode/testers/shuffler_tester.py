#!/usr/bin/env python

import functools, itertools
import inspect
import random
import sys
from typing import *


def run():
    sys.path.append(".."); from solution import Solution
    from testers.slow_solution import SlowSolution

    solution = _bind_primary_method(Solution)
    slow_solution = _bind_primary_method(SlowSolution)

    for i, params in enumerate(generate_test_cases()):
        expected = slow_solution(*params)
        actual = solution(*params)
        if actual != expected:
            print(f"\n\n\n---------------\n\n\n")
            print(f"Found one case for {params}")
            print(f"Expected {expected}")
            print(f"Got {actual}")
            break
        else:
            print(f"✅ Success {i+1}: {params}")


def _bind_primary_method(cls):
    methods = inspect.getmembers(cls, predicate=inspect.isfunction)
    candidate_methods = [(name, m) for name, m in methods if not name.startswith('_')]
    if len(candidate_methods) != 1:
        sys.stderr.writelines([f"Expected exactly 1 method, but found {len(candidate_methods)} ({candidate_methods})"])
        return 1
    _, method = candidate_methods[0]
    return functools.partial(method, cls())


def generate_test_cases():
    yield (1, 2)
    yield (-1, -5)
    while True:
        min_val = random.randint(1, 20)
        max_val = random.randint(1, 20)
        if min_val >= max_val:
            continue
        total = random.randint(2, 5)
        V = [random.randint(min_val, max_val) for _ in range(total)]
        yield V[0], V[1]


if __name__ == "__main__":
    run()
