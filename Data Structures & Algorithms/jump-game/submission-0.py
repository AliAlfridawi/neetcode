class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1

        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == n:
                return True
            if nums[i] == 0:
                return False
            end = min(n+1, nums[i] + i + 1)
            for j in range(i + 1, end):
                if dfs(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        return dfs(0)