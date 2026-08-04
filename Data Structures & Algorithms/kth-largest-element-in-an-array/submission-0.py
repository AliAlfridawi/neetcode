class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lis = []

        for i in nums:
            lis.append(-i)
        
        heapq.heapify(lis)

        while k>1:
            heapq.heappop(lis)
            k-=1

        return -heapq.heappop(lis)