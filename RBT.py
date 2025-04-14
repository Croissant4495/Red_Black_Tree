from classes import *

def get_tree_height(root):
    if root is RedBlackTree.nill:
        return -1
    left_height = get_tree_height(root.left_child)
    right_height = get_tree_height(root.right_child)
    return 1 + max(left_height, right_height)


def get_black_height(root):
    if root is RedBlackTree.nill:
        return 1
    if root.color == 0:
        return 1 + get_black_height(root.left_child)
    else:
        return get_black_height(root.left_child)
    

def get_size(root):
    if root is RedBlackTree.nill:
        return 0
    return 1 + get_size(root.left_child) + get_size(root.right_child)

#tempTree = RedBlackTree()
#tempTree.insert(5)
#tempTree.insert(6)
#tempTree.insert(1)
#tempTree.insert(8)
#tempTree.insert(2)
#tempTree.insert(3)

#print(get_tree_height(tempTree.root))
#print(get_black_height(tempTree.root))
#print(get_size(tempTree.root))