from collections import deque


class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def CreateTree(self, array):
        for element in array:
            if element is array[0]:
                self = Node(element)
            else:
                self.insert(element)

    def insert(self, data):
        if self.data is None:
            self.data = data
        elif data < self.data:
            if self.left is None:
                self.left = Node(data)
            else: 
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else: 
                self.right.insert(data)

    def display_tree(self, prefix='', is_left=False):
        if self.right:
            self.right.display_tree(prefix + ('    ' if is_left else '│   '), False)

        print(prefix + ('└── ' if is_left else '┌── ') + str(self.data))

        if self.left:
            self.left.display_tree(prefix + ('│   ' if is_left else '    '), True)


# Приклад використання:
first_element = int(input('Введіть перший елемент:'))
root = Node(first_element)
while True:
    action = input("Введіть елемент що бажаєте додати, або якщо бажаєте вийти введіть 'Exit': ")
    exit = 'Exit'
    if action is exit:
        break
    else:
        root.insert(int(action))
        root.display_tree()
    