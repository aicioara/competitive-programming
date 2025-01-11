class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"N({self.val})"

    def __str__(self):
        return self.__repr__()

    def __lt__(self, obj):
        return self.val < obj.val

    def all(self):
        s = []
        curr = self
        while curr is not None:
            s.append(curr.val)
            curr = curr.next
        return str(s)


def LinkedList(list):
    nodes = [ListNode(d) for d in list] + [None]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    return nodes[0]
