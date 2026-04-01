class MinStack:

    def __init__(self):
        self.vals = []
        self.mi = []

    def push(self,val):
        self.vals.append(val)
        if len(self.mi)==0 or self.mi[-1]>=val:
            self.mi.append(val)
        else:
            self.mi.append(self.mi[-1])
    def pop(self):
        self.vals.pop()
        self.mi.pop()
    def top(self):
        return self.vals[-1]
    def getMin(self):
        return self.mi[-1]
