class TreeRoot:
    def __init__(self):
        self.children = [None] * 26 
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TreeRoot()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            index = ord(c) - ord('a')
            if cur.children[index] == None:
                cur.children[index] = TreeRoot()
            cur = cur.children[index]
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        cur = self.root
        count = 0
        for c in word:
            index = ord(c) - ord('a')
            if cur.children[index] == None:
                return False
            cur = cur.children[index]
        return cur.endOfWord



    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        count = 0
        for c in prefix:
            index = ord(c) - ord('a')
            if cur.children[index] == None:
                return False
            cur = cur.children[index]
        return True
        