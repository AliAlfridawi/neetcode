class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals
        intervals.sort(key = lambda x:x[0])
        ans = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            print(prevEnd)
            if start >= prevEnd:
                prevEnd = end
            else:
                ans += 1
                prevEnd = min(end, prevEnd)
                
                

        return ans