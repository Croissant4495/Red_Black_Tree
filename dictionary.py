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
        

# tempD = RB_dictionary("our_sample.txt")
# tempD.search_for_word(tempD.root,"banana")
# tempD.insert_word("banana")
# tempD.search_for_word(tempD.root,"abandon ")
