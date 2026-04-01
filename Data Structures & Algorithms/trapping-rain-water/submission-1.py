class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftHeights = [0] * n
        rightHeights = [0] * n

        for i in range(1, n):
            if leftHeights[i-1]>height[i-1]:
                leftHeights[i] = leftHeights[i-1]
            else:
                leftHeights[i] = height[i-1]
        
        for i in range(n-2,-1,-1):
            rightHeights[i] = max(height[i+1],rightHeights[i+1])


        ans = 0
        for i in range(n):
            ans += max(min(rightHeights[i],leftHeights[i])-height[i],0)
        return ans 