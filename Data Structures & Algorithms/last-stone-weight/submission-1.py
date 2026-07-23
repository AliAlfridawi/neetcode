class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            print(stones)
            firstStone = heapq.heappop(stones)
            secondStone = heapq.heappop(stones)

            result = abs(firstStone - secondStone)
            if result == 0:
                continue
            else:
                heapq.heappush(stones, -result)


        
        return 0 if len(stones) == 0 else -stones[0]