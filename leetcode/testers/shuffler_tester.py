import functools, itertools
import inspect
import random
import sys
from typing import *


def run():
    sys.path.append(".."); from solution import Solution

    methods = inspect.getmembers(Solution, predicate=inspect.isfunction)
    candidate_methods = [(name, m) for name, m in methods if not name.startswith('_')]
    if len(candidate_methods) != 1:
        sys.stderr.writelines([f"Expected exactly 1 method, but found {len(candidate_methods)} ({candidate_methods})"])
        return 1
    _, method = candidate_methods[0]

    solution = functools.partial(method, Solution())
    slow_solution = SlowSolution().solve

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
            print(f"Success {i+1}: {params}")

def generate_test_cases():
    yield (0, [100] * 4000, 90, 0.5)
    yield (0, [13, 15, 16], 8, 0.44)
    while True:
        min_val = random.randint(1, 20)
        max_val = random.randint(1, 20)
        if min_val >= max_val:
            continue
        total = random.randint(1, 3)
        V = [random.randint(min_val, max_val) for _ in range(total)]
        C = random.randint(1, 10)
        S = random.randint(0, 100) / 100
        yield 0, V, C, S


class SlowSolution:
    def solve(self, N: int, V: List[int], C: int, S: float):
        best = 0
        indices = list(range(len(V)))
        for i in range(1, len(V) + 1):
            for picks in itertools.combinations(indices, i):
                curr = get_total(V, C, S, set(picks))
                if curr > best:
                    best = curr
        return best

def get_total(V, C, S, picks):
    total = 0
    cum = 0.0
    for i, v in enumerate(V):
        cum += v
        if i in picks and cum - C > 0:
            total += cum - C
            cum = 0
        cum = cum * (1-S)
    return total
