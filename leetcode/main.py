import inspect
import sys

from mytypes import *

import_statement = "from typing import *\n"

def main():
    with open('solution.py', 'r') as fd:
        lines = fd.readlines()
    if lines[0] != import_statement:
        with open('solution.py', 'w') as fd:
            fd.writelines([import_statement] + lines)

    from solution import Solution

    methods = inspect.getmembers(Solution, predicate=inspect.isfunction)
    candidate_methods = [(name, m) for name, m in methods if not name.startswith('_')]
    if len(candidate_methods) != 1:
        sys.stderr.writelines([f"Expected exactly 1 method, but found {len(candidate_methods)} ({candidate_methods})"])
        return 1
    name, method = candidate_methods[0]
    sig = inspect.signature(method)
    params_sets = get_params(len(sig.parameters) - 1)
    solution = Solution()
    for params in params_sets:
        print(f"Calling {name}({params})")
        print("-" * 50)
        result = method(solution, *params)
        print("-" * 50)
        print(result)
        print('=' * 50)
        print("\n\n")


def get_params(n):
    with open('input_single.txt', 'r') as fd:
        lines = [line.strip() for line in fd.readlines() if len(line.strip()) != 0]
    if len(lines) == 0:
        with open('input.txt', 'r') as fd:
            lines = [line.strip() for line in fd.readlines() if len(line.strip()) != 0]
    if len(lines) % n != 0:
        raise RuntimeError(f"Input should have multiple of {n} lines, but it has {len(lines)} lines")

    params = []
    curr = []
    for line in lines:
        curr.append(eval(line))
        if len(curr) == n:
            params.append(curr)
            curr = []
    return params


if __name__ == "__main__":
    main()
