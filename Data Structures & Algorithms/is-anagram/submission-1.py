class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alp = "abcdefghijklmnopqrstuvwxyz"
        
        vecOne = [0] * 26
        vecTwo = [0] * 26

        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                vecOne[alp.find(s[i])]+=1
                vecTwo[alp.find(t[i])]+=1

        return vecOne == vecTwo