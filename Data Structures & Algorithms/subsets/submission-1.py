class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def dfs(nums,cur):
            if nums == []:
                ans.append(cur.copy())
                return
            else:
                dfs(nums[1:], cur)
                dfs(nums[1:], cur + [nums[0]])
            
        dfs(nums,subset)
        return ans