from typing import *
import heapq

class Heap:
    def __init__(self, backing=None, *, maxheap=False):
        if maxheap:
            self.h = MaxHeap(backing)
        else:
            self.h = MinHeap(backing)
    def append(self, c): return self.h.heappush(c)
    def push(self, c): return self.h.heappush(c)
    def pop(self): return self.h.heappop()
    def top(self): return self.h.top()
    def _backing(self): return self.h._backing()
    def __getitem__(self, idx): return self.h[idx]
    def __len__(self): return len(self.h)
    def __iter__(self): return iter(self.h)
    def __str__(self): return str(self.h)
    def __repr__(self): return repr(self.h)

class MinHeap(object):
    def __init__(self, arr=None):
        if arr is not None:
            heapq.heapify(arr)
            self.h = arr
        else:
            self.h = []
    def heappush(self, x): heapq.heappush(self.h, x)
    def heappop(self): return heapq.heappop(self.h)
    def top(self): return self.__getitem__(0)
    def _backing(self): return self.h
    def __getitem__(self, i): return self.h[i]
    def __len__(self): return len(self.h)
    def __iter__(self): return iter(self.h)
    def __str__(self): return str(self.h)
    def __repr__(self): return repr(self.h)

class MaxHeap(MinHeap):
    def __init__(self, arr=None):
        if arr is not None:
            arr = [MaxHeapObj(x) for x in arr]
            heapq.heapify(arr)
            self.h = arr
        else:
            self.h = []
    def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))
    def heappop(self): return heapq.heappop(self.h).val
    def __getitem__(self, i): return self.h[i].val

class MaxHeapObj(object):
    def __init__(self, val): self.val = val
    def __lt__(self, other): return self.val > other.val
    def __eq__(self, other): return self.val == other.val
    def __str__(self): return str(self.val)
    def __repr__(self): return repr(self.val)
