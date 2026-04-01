class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        times = [0] * n

        positionSpeed = []
        for positon in range(n):
            positionSpeed.append([position[positon],speed[positon]])
        
        positionSpeed = sorted(positionSpeed, key = lambda x:x[0])

        for i in range(n):
            times[i] = (target-positionSpeed[i][0]) / positionSpeed[i][1]

        for i in range(len(times)-2,-1,-1):
            if times[i] <= times[i+1]:
                n-=1
                times[i] = times[i+1]
            

        return n