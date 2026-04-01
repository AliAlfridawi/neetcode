class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = heights[0]
        size = len(heights)

        stack = []

        for index,height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                i,h = stack.pop()
                ans = max(ans, h * (index-i ))
                start = i
            stack.append([start,height])

        
        for i, h in stack:
            ans = max(ans, h*(size-i))

            

        return ans