null = None

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


def LinkedList(list) -> ListNode:
    nodes = [ListNode(d) for d in list] + [None]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    return nodes[0]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val} [{self.left}, {self.right}])"

    def __str__(self):
        return self.__repr__()


def BTree(list) -> TreeNode:
    from collections import deque

    if len(list) == 0:
        return None

    dq = deque()
    head = TreeNode(list[0])
    dq.append((head, 'left'))
    dq.append((head, 'right'))

    for d in list[1:]:
        curr, direction = dq.popleft()

        if d is None:
            continue
        else:
            n = TreeNode(d)
            dq.append((n, 'left'))
            dq.append((n, 'right'))
            if direction == 'left':
                curr.left = n
            else:
                curr.right = n

    return head

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"Node({self.val} [{len(self.neighbors)}])"

    def __str__(self):
        return self.__repr__()


def Edges(edges) -> Node:
    nodes = dict()
    for l, r in edges:
        if l not in nodes:
            newnode = Node(l)
            nodes[l] = newnode
        if r not in nodes:
            newnode = Node(r)
            nodes[r] = newnode
        nodes[l].neighbors.append(nodes[r])
        nodes[r].neighbors.append(nodes[l])
    for key in sorted(nodes.keys()):
        return nodes[key]
    return None


def AdjList(list) -> Node:
    nodes = [Node(d) for d in range(len(list))]
    for i, edges in enumerate(list):
        for edge in edges:
            nodes[i].neighbors.append(nodes[edge])
    return nodes[0]
