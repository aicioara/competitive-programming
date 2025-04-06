from typing import *

import collections, math, heapq, bisect, functools, itertools

import sys; sys.setrecursionlimit(600000)

class Solution:
    def dummygetMaxVisitableWebpages(self, N: int, L: List[int]) -> int:
        fake = list(range(2, 50000))
        fake[-1] = 1
        return self._getMaxVisitableWebpages(N, fake)

    def _getMaxVisitableWebpages(self, N: int, L: List[int]) -> int:
        seen = set()
        cache = {}

        @functools.lru_cache(maxsize=None)
        def dfs(n):
            if n in seen:
                return 0
            seen.add(n)
            nxt = L[n] - 1
            return dfs(nxt) + 1

        return max(dfs(i) for i in range(len(L)))
