class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        maxf = 0
        c = ""

        for task in tasks:
            if task not in freq:
                freq[task] = 0
            freq[task] += 1

            if freq[task] > maxf:
                c = task
                maxf = freq[task]
        
        i = 0
        for key in freq:
            if freq[key] == maxf:
                i+=1
        
        time = (maxf-1) * (n+1) + i

        return max(len(tasks), time)