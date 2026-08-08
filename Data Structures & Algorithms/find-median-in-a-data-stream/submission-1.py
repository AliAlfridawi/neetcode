class MedianFinder:

    def __init__(self):
        self.big = []
        self.small = []

    def addNum(self, num: int) -> None:
        if len(self.big) > 0 and self.big[0] < num:
            heapq.heappush(self.big, num)
        else:
            heapq.heappush(self.small, -num)

        if len(self.big) - len(self.small) > 1:
            x = heapq.heappop(self.big)
            heapq.heappush(self.small, -x)
        elif len(self.small) - len(self.big) > 1:
            x = heapq.heappop(self.small)
            heapq.heappush(self.big,-x)

    def findMedian(self) -> float:
        if len(self.big) > len(self.small):
            return self.big[0]
        elif len(self.big) < len(self.small):
            return -self.small[0]
        else:
            return (self.big[0] - self.small[0]) / 2
        