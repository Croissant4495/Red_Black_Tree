from classes import *
class RB_dictionary(RedBlackTree):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.load_dict()

    def load_dict(self):
        with open(self.filename) as f:
            for word in f.readlines():
                self.insert(word.strip().lower())
                # print("inserting "+ word.strip().lower())
        f.close();
    
    def add_new_word(self, word):
        with open(self.filename, "a") as file:
            file.write(word+"\n")
        file.close()

    def insert_word(self, value):
        if super().insert(value):
            self.add_new_word(value)

    def search_for_word(self, node, value):
        if super().search(node, value.lower()) == True:
            print("YES")
        else: 
            print("NO")
            
        

tempD = RB_dictionary("Dictionary.txt")
tempD.preorder_traversal(tempD.root)
tempD.search_for_word(tempD.root,"multimedia")
print(f"tree height: {tempD.get_tree_height(tempD.root)}")
print(f"tree black height: {tempD.get_black_height(tempD.root)}")
print(f"tree size: {tempD.get_size(tempD.root)}")
# tempD.insert_word("banana")
# tempD.search_for_word(tempD.root,"abandon ")
