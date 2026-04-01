class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mSet = set(nums)
        return len(nums)!=len(mSet)