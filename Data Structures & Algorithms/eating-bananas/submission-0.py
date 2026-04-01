class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)-1
        l=1
        r = max(piles)
        k = r
        # Find K
        while l<=r:
            mid = (l + r) // 2
            tally = 0
            for i in piles:
                tally = tally + math.ceil(float(i)/mid)
            if tally <= h:
                r = mid-1
                k = mid
            else:
                l = mid+1
        return k