import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}
        n = len(nums)

        for i in nums:
            dic[i] = 1 + dic.get(i,0)
        
        arr = [[] for _ in range(n+1)] 
        for n,c in dic.items():
            arr[c].append(n)

        ans = []

        for i in range(len(arr)-1, 0, -1):
            for j in arr[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans
        return ans