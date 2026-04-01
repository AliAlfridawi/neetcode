class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        times = [0] * n

        positionSpeed = []
        for pos in range(n):
            tS = (position[pos], (target-position[pos])/speed[pos])
            positionSpeed.append(tS)
        
        positionSpeed.sort()

        for i in range(len(times)-2,-1,-1):
            if positionSpeed[i][1]<=positionSpeed[i+1][1]:
                positionSpeed[i]=(0,positionSpeed[i+1][1])
                n-=1
            

        return n