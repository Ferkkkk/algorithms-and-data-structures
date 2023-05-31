class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def CreateTree(data):
    if data is None:
        return None
    root = Node(data[0])
    queue = [root]
    i = 1
    while queue:
        current = queue.pop(0)
        if i < len(data) and data[i] is not None:
            current.left = Node(data[i])
            queue.append(current.left)
        i += 1
        if i < len(data) and data[i] is not None:
            current.right = Node(data[i])
            queue.append(current.right)
        i += 1
    return root

def ShowTree(root):
    if root is None:
        return
    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

def PrefixOrder(root):
    if root is None:
        return
    print(root.data)
    PrefixOrder(root.left)
    PrefixOrder(root.right)

def PostfixOrder(root):
    if root is None:
        return
    PostfixOrder(root.left)
    PostfixOrder(root.right)
    print(root.data)

def InfixOrder(root):
    if root is None:
        return
    InfixOrder(root.left)
    print(root.data)
    InfixOrder(root.right)