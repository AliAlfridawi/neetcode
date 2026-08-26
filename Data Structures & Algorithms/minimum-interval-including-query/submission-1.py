class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x:x[0])
        sortedQueries = sorted(queries)
        res = {}
        minHeap = []
        i = 0

        for query in sortedQueries:
            while i < len(intervals) and intervals[i][0] <= query:
                heapq.heappush(minHeap, (intervals[i][1] - intervals[i][0] + 1,intervals[i][1]))
                i += 1

            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            res[query] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]
        