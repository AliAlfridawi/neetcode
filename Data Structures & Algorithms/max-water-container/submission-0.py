class Solution:
    def maxArea(self, heights: List[int]) -> int:
       p1 = 0 
       p2 = len(heights)-1
       distance = p2 
       longest = 0
       while p1<p2: 
        minHeight = min(heights[p1],heights[p2])
        if minHeight * distance > longest:
            longest = minHeight * distance
        if minHeight == heights[p1]:
            p1+=1
        else:
            p2-=1
        distance-=1
       return longest
