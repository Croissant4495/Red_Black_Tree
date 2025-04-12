class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.color = 0                  # 0 -> Black , 1 -> Red

    def set_left_child(self, child):
        self.left_child = child
    
    def set_right_child(self, child):
        self.right_child = child

    def set_parent(self, parent):
        self.parent = parent

    def toggle_color(self):
        self.color = not self.color

class Tree:
    def __init__(self):
       self.root = None
    
    def search(self, value):
        pass

    def insert(self, value):
        if self.search(value):
            return
        new = Node(value)
        
        