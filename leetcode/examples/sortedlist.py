from sortedcontainers import SortedList # type: ignore
from typing import *

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.q = SortedList()
        self.d = {}

        for t in tasks:
            userId, taskId, priority = t
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        task = [priority, taskId, userId]
        self.d[taskId] = task
        self.q.add(task)


    def edit(self, taskId: int, newPriority: int) -> None:
        task = self.d[taskId]
        self.rmv(taskId)
        self.add(task[2], task[1], newPriority)

    def rmv(self, taskId: int) -> None:
        task = self.d[taskId]
        self.q.discard(task)


    def execTop(self) -> int:
        if len(self.q) == 0:
            return -1
        task = self.q.pop()
        return task[2]
