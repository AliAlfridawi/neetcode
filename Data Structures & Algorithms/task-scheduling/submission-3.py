class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        maxf = 0
        c = ""

        for task in tasks:
            if task not in freq:
                freq[task] = 0
            
            freq[task] += 1

            if maxf < freq[task]:
                c = task
                maxf = freq[task]
        
        idle = (maxf - 1) * n

        for task in freq:
            if task is not c:
                idle -= min(maxf-1, freq[task])

        return len(tasks) if idle <= 0 else len(tasks) + idle