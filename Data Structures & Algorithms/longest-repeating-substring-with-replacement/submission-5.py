class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        ans = 0

        for c in charSet:
            l = 0
            r = 0
            count = 0

            while r < len(s):
                if s[r] == c:
                    count += 1

                if (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                ans = max(ans, r - l + 1)
                r += 1

        return ans