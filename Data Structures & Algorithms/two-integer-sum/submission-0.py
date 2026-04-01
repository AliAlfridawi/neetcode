class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = dict()
        n = len(nums)

        for i in range(n):
            if nums[i] in dictionary:
                return [dictionary[nums[i]],i]
            else:
                dictionary[target-nums[i]]=i

        return [-1,-1]