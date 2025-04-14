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
        self.color = not self.color

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
            elif value < node.value and node.left_child != None:
                return self.search(node.left_child, value)
            elif value > node.value and node.right_child != None:
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
        node.parent.right_child = node.left_child
        node.left_child = node.parent

        direction = self.get_direction_from_parent(node.parent)
        if direction == -1:
            node.parent.parent.left_child = node
        elif direction == 1:
            node.parent.parent.right_child = node
        else:
            self.root = node
        node.parent = node.parent.parent
        node.left_child.parent = node

    def rotate_right(self, node:Node):
        node.parent.left_child = node.right_child
        node.right_child = node.parent

        direction = self.get_direction_from_parent(node.parent)
        if direction == -1:
            node.parent.parent.left_child = node
        elif direction == 1:
            node.parent.parent.right_child = node
        else:
            self.root = node
        node.parent = node.parent.parent
        node.right_child.parent = node

    def fix_up(self, node:Node):
        if node == self.root:
            node.color = 0
            return
        if node.color and node.parent.color:
            if self.get_uncle(node).color:
                # Case 1
                self.get_uncle(node).toggle_color()
                node.parent.toggle_color()
                node.parent.parent.toggle_color()
                self.fix_up(node.parent.parent)
            else:
                self.determine_rotations(node)


    def insert(self, value):
        if self.search(self.root, value):
            return
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

    def traverse(self, node:Node):
        if node != RedBlackTree.nill:
            self.traverse(node.left_child)
            print(node.value)
            self.traverse(node.right_child)

    def preorder_traversal(self, node:Node):
        if node != RedBlackTree.nill:
            print(f"Node {node.value} has index {self.temp}")
            self.temp += 1
            self.preorder_traversal(node.left_child)
            self.preorder_traversal(node.right_child)
    
tempTree = RedBlackTree()
tempTree.insert(5)
tempTree.insert(6)
tempTree.insert(1)
tempTree.insert(8)
tempTree.insert(2)
tempTree.insert(3)
tempTree.preorder_traversal(tempTree.root)
print("_______________")
tempTree.rotate_left(tempTree.root.right_child)
tempTree.rotate_right(tempTree.root.left_child)
tempTree.preorder_traversal(tempTree.root)
