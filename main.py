from classes import *

tempTree = RedBlackTree()
tempTree.insert(10)
tempTree.insert(1)
tempTree.insert(12)
tempTree.insert(4)
tempTree.insert(8)
tempTree.insert(19)
tempTree.insert(2)
tempTree.insert(21)
tempTree.insert(22)
tempTree.insert(23)
tempTree.insert(24)

print(f"tree height: {tempTree.get_tree_height(tempTree.root)}")
print(f"tree black height: {tempTree.get_black_height(tempTree.root)}")
print(f"tree size: {tempTree.get_size(tempTree.root)}")