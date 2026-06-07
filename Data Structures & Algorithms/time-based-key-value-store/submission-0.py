class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        val = [value,timestamp]
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append(val)

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        value = self.timeMap.get(key,[])

        l, r = 0, len(value) - 1

        while l <= r:
            m = (r + l) // 2
            if value[m][1] <= timestamp:
                l = m + 1
                res = value[m][0]
            else:
                r = m - 1
        return res