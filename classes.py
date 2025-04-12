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
    
    def nillify(self, node):
        node.set_left_child(RedBlackTree.nill)
        node.set_right_child(RedBlackTree.nill)
        node.set_parent(RedBlackTree.nill)

    def search(self, node, value):
        if value == node.value:
            return True
        elif value < node.value and node.left_child != None:
            return self.search(node.left_child, value)
        elif value > node.value and node.right_child != None:
            return self.search(node.right_child, value)
        else:
            return False

    def fix_up(self, node:Node):
        pass

    def insert(self, value):
        if self.search(value):
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
        