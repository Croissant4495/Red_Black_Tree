from classes import *
class RB_dictionary(RedBlackTree):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.load_dict()

    def load_dict(self):
        successful = 0
        failed = 0
        words = []
        
        with open(self.filename) as f:
            for line in f.readlines():
                line = line.strip()
                if line and not line.startswith('//'):
                    word = line.lower()
                    words.append(word)
                    if super().insert(word):
                        successful += 1
                    else:
                        failed += 1
                        print(f"Failed to insert: {word}")
        return successful
    
    def add_new_word(self, word):
        with open(self.filename, "a") as file:
            file.write("\n"+ word)
        file.close()

    def insert_word(self, value):
        if super().insert(value):
            self.add_new_word(value)

    def search_for_word(self, node, value):
        if super().search(node, value.strip().lower()) == True:
            print("YES")
        else: 
            print("NO")
            
        
tempD = RB_dictionary("Dictionary.txt")
print(f"tree height: {tempD.get_tree_height(tempD.root)}")
print(f"tree black height: {tempD.get_black_height(tempD.root)}")
print(f"tree size: {tempD.get_size(tempD.root)}")
tempD.insert_word("GitHubS")