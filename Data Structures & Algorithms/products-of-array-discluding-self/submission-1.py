class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [0] * length
        suffix = [0] * length
        ans = [0] * length
        
        prefix[0] = 1
        suffix[-1] = 1

        for i in range(1,length):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]

        for i in range(length):
            ans[i] = prefix[i] * suffix[i]
        
        return ans