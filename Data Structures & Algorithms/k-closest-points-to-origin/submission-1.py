class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lis = []

        for i in points:
            dis = (i[0] ** 2) + (i[1] ** 2)
            lis.append((dis,i[0],i[1]))
        
        heapq.heapify(lis)
        ans = [] 
        
        while k > 0 and lis:
            popped = heapq.heappop(lis)
            ans.append((popped[1], popped[2]))
            k -= 1

        return ans
