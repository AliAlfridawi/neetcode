class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lens1 = len(s1)
        lens2 = len(s2)

        r1 = [0] * 26
        r2 = [0] * 26

        if lens1 > lens2:
            return False
        
        for i in s1:
            r1[ord(i) - ord('a')] += 1

        l, r = 0, 0

        while r < lens2:
            if r - l > lens1 - 1:
                r2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            else:
                r2[ord(s2[r]) - ord('a')] += 1
                r += 1
            if r2 == r1:
                return True
            

        return r2 == r1