class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        numSet = set(nums)
        longestRange = 1

        for num in numSet:
            if num - 1 in numSet:
                continue
            else:
                lr = 1
                cn = num
                while cn + 1 in numSet:
                    cn += 1 
                    lr += 1
                
                if lr>longestRange:
                    longestRange = lr

        return longestRange    