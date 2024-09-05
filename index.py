class Node:
    def __init__(self, key):
        if key == "null":
            self.data = None
        else:
            self.data = key
        self.left = None
        self.right = None

def sum_levels(lst):
    levels = 0
    for i in range(10):
        if len(lst) == 2**i - 1:
            levels = i + 1
            break

    root = Node(lst[0])
    root.left = Node(lst[1])
    root.right = Node(lst[2])
    root.left.left = Node(lst[3])
    root.left.right = Node(lst[4])
    # root.right.left = Node(lst[5])
    root.right.right = Node(lst[6])

    from collections import deque

    Q = deque() 
    V = []
    M = set()

    Q.appendleft(root)

    while len(Q) != 0:
        cur = Q.pop()
        print(f"Processing node with value: {cur.data}")
        V.append(cur.data)
        for child in [cur.left, cur.right]:
            if child not in M and child is not None:
                Q.append(child)
                M.add(child)

    return V

def max_levels(lst):
    values = sum_levels(lst)
    print("Values at each level:", values)

# Test the function
max_levels([5, 3, 8, 2, 4, "null", 9])
