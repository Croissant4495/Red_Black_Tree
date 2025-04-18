class Node:
    def __init__(self, value):
        self.value = value
        self.parent:Node = None
        self.left_child:Node = None
        self.right_child:Node = None
        self.color = 1                  # 0 -> Black , 1 -> Red

    def set_left_child(self, child):
        self.left_child = child
    
    def set_right_child(self, child):
        self.right_child = child

    def set_parent(self, parent):
        self.parent = parent

    def toggle_color(self):
        if self.color == 1:
            self.color = 0
        else:
            self.color = 1
        # self.color = not self.color   # not 1 is "None" not "0"

class RedBlackTree:
    nill = Node(None)
    
    def __init__(self):
       self.root = RedBlackTree.nill
       self.nillify(self.root)
       self.temp = 0
    
    def nillify(self, node):
        node.set_left_child(RedBlackTree.nill)
        node.set_right_child(RedBlackTree.nill)
        node.set_parent(RedBlackTree.nill)

    def search(self, node, value):
        if node != RedBlackTree.nill:
            if value == node.value:
                return True
            elif value < node.value:
                return self.search(node.left_child, value)
            elif value > node.value:
                return self.search(node.right_child, value)
        return False

    def get_direction_from_parent(self, node:Node):
        # left child  : -1
        # right child :  1
        if node.parent.left_child == node:
            return -1
        elif node.parent.right_child == node:
            return 1
        else:
            return 0
        
    def get_uncle(self, node:Node):
        direction = self.get_direction_from_parent(node.parent)
        if direction == -1:
            return node.parent.parent.right_child
        elif direction == 1:
                return node.parent.parent.left_child
        else:
            return RedBlackTree.nill
    

    def determine_rotations(self, node:Node):
        node_dir = self.get_direction_from_parent(node)
        parent_dir = self.get_direction_from_parent(node.parent)
        if node_dir and parent_dir:
            if node_dir == parent_dir:
                return 3                      # Case 3
            return 2                          # Case 2

    def rotate_left(self, node:Node):
        right_child = node.right_child
        node.right_child = right_child.left_child
        if right_child.left_child != RedBlackTree.nill:
            right_child.left_child.parent = node
        right_child.left_child = node
        right_child.parent = node.parent
        direction = self.get_direction_from_parent(node)
        if direction == -1:
            node.parent.left_child = right_child
        elif direction == 1:
            node.parent.right_child = right_child
        else:
            self.root = right_child
        node.parent = right_child
        # node.right_child.parent = node

    def rotate_right(self, node:Node):
        left_child = node.left_child
        node.left_child = left_child.right_child
        if left_child.right_child != RedBlackTree.nill:
            left_child.right_child.parent = node
        left_child.right_child = node
        left_child.parent = node.parent
        direction = self.get_direction_from_parent(node)
        if direction == -1:
            node.parent.left_child = left_child
        elif direction == 1:
            node.parent.right_child = left_child
        else:
            self.root = left_child
        node.parent = left_child

    def fix_up(self, node:Node):
        if node == self.root:
            node.color = 0
            return
        if node.color and node.parent.color:
            if self.get_uncle(node) != RedBlackTree.nill and self.get_uncle(node).color: # check if uncle exists before checking his color
                # Case 1
                self.get_uncle(node).toggle_color()
                node.parent.toggle_color()
                node.parent.parent.toggle_color()
                self.fix_up(node.parent.parent)
            else:   # code below is ugly but works
                # print("not case 1 but case ")
                # print(self.determine_rotations(node))
                case = self.determine_rotations(node)
                direction = self.get_direction_from_parent(node)
                
                if case == 2:
                    if direction == -1:
                        self.rotate_right(node.parent)
                        node = node.right_child
                    elif direction == 1:
                        self.rotate_left(node.parent)
                        node = node.left_child
                    else:
                        print("error")
                # case 3 always happens after case 2 but we replaced the node with its child
                node.parent.toggle_color()
                node.parent.parent.toggle_color()
                direction = self.get_direction_from_parent(node)
                if direction == -1:
                    self.rotate_right(node.parent.parent)
                elif direction == 1:
                    self.rotate_left(node.parent.parent)
                else:
                    print("error")


    def insert(self, value):
        if self.search(self.root, value):
            return False
        new = Node(value)
        self.nillify(new)

        parent = RedBlackTree.nill
        current = self.root
        
        while current != RedBlackTree.nill:
            parent = current
            if value > current.value:
                current = current.right_child
            else:
                current = current.left_child
        
        if parent == RedBlackTree.nill:
            self.root = new
        else:
            if value > parent.value:
                parent.right_child = new
            else:
                parent.left_child = new 
            new.parent = parent
        
        self.fix_up(new)
        return True

    def traverse(self, node:Node):
        if node != RedBlackTree.nill:
            self.traverse(node.left_child)
            print(node.value)
            self.traverse(node.right_child)

    def preorder_traversal(self, node:Node):
        if node != RedBlackTree.nill:
            print(f"Node {node.value} has index {self.temp} of color {node.color}")
            self.temp += 1
            self.preorder_traversal(node.left_child)
            self.preorder_traversal(node.right_child)
    def get_tree_height(self, root):
        if root is RedBlackTree.nill:
            return 0
        left_height = self.get_tree_height(root.left_child)
        right_height = self.get_tree_height(root.right_child)
        return 1 + max(left_height, right_height)


    def get_black_height(self, root):
        if root is RedBlackTree.nill:
            return 1
        if root.color == 0 and root.parent != RedBlackTree.nill:
            return 1 + self.get_black_height(root.left_child)
        else:
            return self.get_black_height(root.left_child)
        

    def get_size(self, root):
        if root is RedBlackTree.nill:
            return 0
        return 1 + self.get_size(root.left_child) + self.get_size(root.right_child)


# tempTree = RedBlackTree()
# tempTree.insert(10)
# tempTree.insert(1)
# tempTree.insert(12)
# tempTree.insert(4)
# tempTree.insert(8)
# tempTree.insert(19)
# tempTree.insert(2)
# tempTree.insert(21)

# tempTree.preorder_traversal(tempTree.root)
# print(tempTree.get_tree_height(tempTree.root))
# print(tempTree.get_black_height(tempTree.root))
# print(tempTree.get_size(tempTree.root))