import inspect
import sys

from utils.mytypes import *
from utils import colors

import_statement = "from typing import *"
extra_imports = """

import bisect, collections, functools, heapq, itertools, math, re

# import numpy as np
# from sortedcontainers import SortedList

"""


def main():
    fix_solution()
    import solution
    for name, _ in inspect.getmembers(solution, inspect.isclass):
        if name == "Solution":
            regular_solution()
            break
    else:
        class_solution()


def regular_solution():
    import solution

    methods = inspect.getmembers(solution.Solution, predicate=inspect.isfunction)
    candidate_methods = [(name, m) for name, m in methods if not name.startswith('_')]
    if len(candidate_methods) != 1:
        sys.stderr.writelines([f"Expected exactly 1 method, but found {len(candidate_methods)} ({candidate_methods})"])
        sys.exit(0)
    name, method = candidate_methods[0]
    sig = inspect.signature(method)

    nparams = len(sig.parameters) - 1
    actual_nparams = len_input_txt()

    if actual_nparams == nparams:
        allparams, _ = get_params(nparams)
        allanswers = [[]]
    else:
        allparams, allanswers = get_params(nparams, get_answers=True)

    if len(allparams) != len(allanswers):
        sys.stderr.writelines([f"Cardinality of allparams and allanswers does not match {len(allparams)} vs {len(allanswers)}"])
        sys.exit(0)

    for i, (params, answers) in enumerate(zip(allparams, allanswers)):
        if len(answers) == 0: # Single tests
            solution = solution.Solution()
            print(f"Calling {name}({params})")
            print("-" * 50)
            result = method(solution, *params)
            print("-" * 50)
            print(result)
            print('=' * 50)
            print("\n")
        else:
            sol = solution.Solution()
            result = method(sol, *params)
            ans = answers[0]
            if result != ans:
                print(colors.red("="*50))
                print(colors.red(f"❌ Test {i+1} Failed"))
                print(colors.red(f"{name}({params})) -> {result}"))
                print(f"Expected: {ans}")
                print(f"Actual: {result}")
                sys.exit(0)
            else:
                print(colors.green(f"✅ Test {i+1} Success"))


def class_solution():
    import solution

    classmap = {name: obj for name, obj in inspect.getmembers(solution, inspect.isclass)}

    nparams = 2 # Defined by leetcode
    actual_nparams = len_input_txt()
    if actual_nparams == nparams:
        allparams, _ = get_params(nparams)
        allanswers = [[]]
    else:
        allparams, allanswers = get_params(nparams, get_answers=True)

    if len(allparams) != len(allanswers):
        sys.stderr.writelines([f"Cardinality of allparams and allanswers does not match {len(allparams)} vs {len(allanswers)}"])
        sys.exit(0)

    for i, (params, answers) in enumerate(zip(allparams, allanswers)):
        if len(params[0]) != len(params[1]):
            sys.stderr.writelines(["Param length is incorrect", f"Expected {len(params[0])} == {len(params[1])}"])
            sys.exit(0)
        if len(answers[0]) != 0 and len(answers[0]) != len(params[0]):
            sys.stderr.writelines(["Answers length is incorrect\n", f"Expected {len(params[0])}. Got {len(answers[0])}"])
            sys.exit(0)

        if len(answers) == 0: # Single tests
            tests = zip(params[0], params[1])
            classname, classparams = next(tests)
            obj = classmap[classname](*classparams)
            for methodname, methodparams in tests:
                print("-" * 50)
                print(f"Calling {classname}.{methodname}({methodparams})")
                print("-" * 50)
                result = getattr(obj, methodname)(*methodparams)
                print("-" * 50)
                print(result)
                print("=" * 50)
                print("\n")
        else: # Test Suite
            tests = zip(params[0], params[1], answers[0])
            classname, classparams, ans = next(tests)
            obj = classmap[classname](*classparams)
            printout = []
            for methodname, methodparams, ans in tests:
                result = getattr(obj, methodname)(*methodparams)
                if result != ans:
                    print(colors.red("="*50))
                    print(colors.red(f"❌ Test {i+1} Failed"))
                    for p in printout:
                        print(p)
                    print(colors.red(f"{classname}.{methodname}({methodparams}) -> {result}"))
                    print(f"Expected: {ans}")
                    sys.exit(0)
                else:
                    printout.append(colors.green(f"✅ {classname}.{methodname}({methodparams}) -> {result}"))
            else:
                print(colors.green(f"✅ Test {i+1} Success"))



def fix_solution():
    with open('solution.py', 'r') as fd:
        lines = fd.readlines()
    if lines[0].strip() != import_statement:
        with open('solution.py', 'w') as fd:
            fd.writelines([import_statement, extra_imports] + lines)


def len_input_txt():
    with open('input.txt', 'r') as fd:
        lines = [line.strip() for line in fd.readlines() if len(line.strip()) != 0]
    return len(lines)


def get_params(n, get_answers=False):
    with open('input.txt', 'r') as fd:
        lines = [line.strip() for line in fd.readlines() if len(line.strip()) != 0]

    if len(lines) % (n+get_answers) != 0:
        sys.stderr.write(f"Input should have multiple of {n+get_answers} lines, but it has {len(lines)} lines")
        sys.exit(0)

    params = []
    answers = []
    curr_params = []
    curr_answers = []
    for i, line in enumerate(lines):
        try:
            curr = eval(line)
        except:
            sys.stderr.writelines([f"input.txt evaluation error on line {i+1}\n", line])
            sys.exit(0)

        if len(curr_params) < n:
            curr_params.append(curr)
        elif get_answers and len(curr_answers) == 0:
            curr_answers.append(curr)

        if len(curr_params) == n and (not get_answers or len(curr_answers) == 1):
            params.append(curr_params)
            curr_params = []
            answers.append(curr_answers)
            curr_answers = []
    return params, answers


def run_tester():
    from testers.shuffler_tester import run
    run()


if __name__ == "__main__":
    main()
    # run_tester()
