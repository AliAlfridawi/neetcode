class trieNode:
    def __init__(self):
        self.tm = {}
        self.isEnd = False
    
    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.tm:
                cur.tm[c] = trieNode()
            cur = cur.tm[c] 
        cur.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        prefixTrie = trieNode()

        for word in words:
            prefixTrie.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or board[r][c] not in node.tm:
                return
            visit.add((r,c))
            node = node.tm[board[r][c]]
            word += board[r][c]
            if node.isEnd:
                res.add(word)

            dfs(r-1,c, node, word)
            dfs(r+1,c, node, word)
            dfs(r,c-1, node, word)
            dfs(r,c+1, node, word)
            visit.remove((r,c))
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,prefixTrie,"")
        
        
        return list(res)