class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        if len(s) % 2 == 1:
            return False
        for i in s:
            if i == "{" or i =="(" or i == "[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                cur = stack.pop()
                if cur == "{" and i != "}":
                    return False 
                elif cur == "[" and i != "]":
                    return False
                elif cur == "(" and i  != ")":
                    return False
        return len(stack) == 0 and True