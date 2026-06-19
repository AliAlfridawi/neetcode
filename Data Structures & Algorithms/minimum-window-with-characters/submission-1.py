class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t) or t == "":
            return ""       

        win1, win2 = {}, {}

        for c in t:
            win1[c] = win1.get(c,0) + 1

        l, have, need = 0, 0, len(win1)
        res = [-1,-1]
        resLen = float('infinity')
        
        for i in range(len(s)):
            c = s[i]
            win2[c] = win2.get(c, 0) + 1
            
            if c in win1 and win1[c] == win2[c]:
                have += 1
            
            while have == need:
                lc = s[l]
                if resLen > i - l:
                    resLen = i-l
                    res = [l,i]
                win2[lc] -= 1
                if lc in win1 and win2[lc] < win1[lc]:
                    have -=1
                
                l += 1
        return s[res[0]:res[1]+1]