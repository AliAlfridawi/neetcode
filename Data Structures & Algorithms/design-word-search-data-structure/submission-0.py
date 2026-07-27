class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.trieMap = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()    

    def addWord(self, word: str) -> None:
        cur = self.root 

        for c in word:
            if c not in cur.trieMap:
                cur.trieMap[c] = TrieNode()
                
            cur = cur.trieMap[c]

        cur.isEnd = True 

    def search(self, word: str) -> bool:
        def dfs(index, root):
            cur = root

            for i in range(index, len(word)):
                if word[i] == ".":
                    for subTree in cur.trieMap.values():
                        if dfs(i+1, subTree):
                            return True
                    return False
                else:
                    if word[i] not in cur.trieMap:
                        return False
                    cur = cur.trieMap[word[i]]
                
            return cur.isEnd
        
        return dfs(0,self.root)
