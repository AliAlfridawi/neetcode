class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        p2 = 1
        
        n = len(prices)
        if n == 1: 
            return 0

        ans = max(0,prices[p2]-prices[p1])

        while p2 < n-1:
            if prices[p1] > prices[p2]:
                p1+= 1
            else:
                p2+=1
            ans = max(ans,prices[p2]-prices[p1])

        return ans