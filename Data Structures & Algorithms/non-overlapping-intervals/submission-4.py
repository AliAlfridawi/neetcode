class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals
        intervals.sort(key = lambda x:x[0])
        ans = 0
        i = 0

        while i < len(intervals)-1:
            if intervals[i][1] > intervals[i+1][0]:
                ans += 1

                diff1 = intervals[i][1]
                diff2 = intervals[i+1][1]

                if diff1 >= diff2:
                    intervals.pop(i)
                else:
                    intervals.pop(i+1)
            else:
                i+=1
                
                

        return ans