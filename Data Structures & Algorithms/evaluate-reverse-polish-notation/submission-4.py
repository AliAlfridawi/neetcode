class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        curSum = 0

        for token in tokens:
            if token == "+":
                curSum = stack.pop() + stack.pop()
                stack.append(curSum)
            elif token == "-":
                first = stack.pop()
                second = stack.pop()
                curSum = second - first
                stack.append(curSum)
            elif token == "*":
                curSum = stack.pop() * stack.pop()
                stack.append(curSum)
            elif token == "/":
                first = stack.pop()
                second = stack.pop()
                curSum = int(second / first)
                stack.append(curSum)
            else:
                stack.append(int(token))

        return stack.pop()
