class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 1
        n = len(s)
        
        if n == 1:
            return 1
        elif n == 0:
            return 0

        r = 0
        l = 0
        for let in s:
            if let not in seen:
                seen.add(let)
                r+=1
            else:
                ans = max(ans,len(seen))
                while let in seen:
                    seen.remove(s[l])
                    l+=1
                seen.add(let)

        return max(ans,len(seen))