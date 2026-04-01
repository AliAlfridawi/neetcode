import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = dict()
        n = len(nums)

        for i in nums:
            dic[i] = 1 + dic.get(i,0)
        
        arr = [[] for _ in range(n+1)] 
        for i in dic:
            arr[dic[i]].append(i)

        ans = []

        while len(ans) != k:
            if arr[n] != []:
                for i in arr[n]:
                    ans.append(i)
            n-=1

        return ans