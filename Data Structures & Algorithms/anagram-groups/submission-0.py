class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        ans = []

        for str in strs:
            sort = "".join(sorted(str))
            if sort in dic:
                dic[sort].append(str)
            else:
                dic[sort]=[]
                dic[sort].append(str)
        
        for lis in dic.values():
            ans.append(lis)
            
        return ans