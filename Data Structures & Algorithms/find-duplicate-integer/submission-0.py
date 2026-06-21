class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x = set()
        
        for num in nums:
            if num in x:
                return num
            x.add(num)
        
        return -1