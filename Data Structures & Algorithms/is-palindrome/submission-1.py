class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ''
        for c in s:
            if c.isalnum():
                ns += c.lower()
        
        p1 = 0
        p2 = len(ns)-1
        print(ns)
        while p1 < p2:
            if ns[p1]!=ns[p2]:
                return False
            p1+=1
            p2-=1
        
        return True