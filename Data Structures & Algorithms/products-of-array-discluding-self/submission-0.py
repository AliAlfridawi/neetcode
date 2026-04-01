class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numOfZeros = 0
        multTotal = 1

        for i in nums:
            if i == 0:
                numOfZeros += 1
            else:
                multTotal *= i
        
        if numOfZeros>1:
            return [0]*n
        elif numOfZeros>0:
            ans = [0] * n
            for i in range(n):
                if nums[i] == 0:
                    ans[i] = multTotal
        else:
            ans = [1] * n
            for i in range(n):
                ans[i] = multTotal//nums[i]

        return ans 