from Lab_4.Tree import CreateTree, InfixOrder, PostfixOrder, PrefixOrder, ShowTree


data = [1, 2, 3, 4, None, 5, 6, None, None, None, None, 7]

tree = CreateTree(data)

print("Відображення дерева:")
ShowTree(tree)

print("Префіксний обхід:")
PrefixOrder(tree)

print("Постфіксний обхід:")
PostfixOrder(tree)

print("Інфіксний обхід:")
InfixOrder(tree)