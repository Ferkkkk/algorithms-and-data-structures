class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

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

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_value = self.right.find_min()
                self.data = min_value
                self.right = self.right.delete(min_value)
        return self

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def prefix_order(self):
        if self:
            print("Prefix: {}".format(self.data))
            if self.left:
                self.left.prefix_order()
            if self.right:
                self.right.prefix_order()

    def postfix_order(self):
        if self:
            if self.left:
                self.left.postfix_order()
            if self.right:
                self.right.postfix_order()
            print("Postfix: {}".format(self.data))

    def infix_order(self):
        if self:
            if self.left:
                self.left.infix_order()
            print("Infix: {}".format(self.data))
            if self.right:
                self.right.infix_order()

    def display_tree(self, prefix='', is_left=False):
        if self.right:
            self.right.display_tree(prefix + ('    ' if is_left else '│   '), False)

        print(prefix + ('└── ' if is_left else '┌── ') + str(self.data))

        if self.left:
            self.left.display_tree(prefix + ('│   ' if is_left else '    '), True)


first_element = int(input('Введіть перший елемент: '))
root = Node(first_element)
while True:
    action = input("Введіть значення або одну з команд ('Exit','Prefix','Postfix','Infix','Delete <значення>'): ")
    exit_command, prefix_command, postfix_command, infix_command, delete_command = 'Exit', 'Prefix', 'Postfix', 'Infix', 'Delete'
    if action == exit_command:
        break
    elif action == prefix_command:
        root.display_tree()
        root.prefix_order()
    elif action == postfix_command:
        root.display_tree()
        root.postfix_order()
    elif action == infix_command:
        root.display_tree()
        root.infix_order()
    elif action.startswith(delete_command):
        value = int(action.split(' ')[1])
        root.delete(value)
        root.display_tree()
    else:
        root.insert(int(action))
        root.display_tree()
