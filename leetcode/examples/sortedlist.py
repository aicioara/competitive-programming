from typing import *
from sortedcontainers import SortedList

class AVL:
    def __init__(self, vals=None):
        if vals is not None:
            self.q = SortedList(vals)
        else:
            self.q = SortedList()

    def add(self, val): self.q.add(val)
    def push(self, val): self.q.add(val)

    def discard(self, val): self.q.discard(val)
    def remove(self, val): self.q.discard(val)

    def pop(self): return self.q.pop()

    def __str__(self): return str(self.q)
    def __repr__(self): return repr(self.q)
