import functools

class Solution:
    def maximumCandies(self, candies, k):
        return bisector(1, sum(candies), functools.partial(functor, candies, k), default=0)


def functor(candies, k, val):
    total = 0
    for candy in candies:
        total += candy // val
    return total >= k


# left / right are inclusive [left, right]
# f is a function that takes N and returns a bool
# largest is True if we are looking for the largest N for which f is True
def bisector(left, right, f, largest=True, default=-1):
    best = default
    while left <= right:
        mid = (left + right) // 2
        good = f(mid)
        if good:
            best = mid
            if largest:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if largest:
                right = mid - 1
            else:
                left = mid + 1
    return best
