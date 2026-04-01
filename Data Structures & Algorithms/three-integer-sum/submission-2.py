class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            else:
                p1 = i+1
                p2 = n-1
                while p1<p2:
                    tot = nums[i] + nums[p1] + nums[p2]
                    if tot == 0:
                        ans.add(tuple([nums[i],nums[p1],nums[p2]]))
                        p1+=1
                    elif tot>0:
                        p2-=1
                    else:
                        p1+=1

        return [list(i) for i in ans]