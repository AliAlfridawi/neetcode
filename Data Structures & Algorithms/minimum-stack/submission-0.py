class MinStack:

    def __init__(self):
        self.stack = []
        self.minList = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minList)==0:
            self.minList.append(val)
        elif self.minList[-1] < self.stack[-1]:
            self.minList.append(self.minList[-1])
        else:
            self.minList.append(self.stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minList.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minList[-1]
