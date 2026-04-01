class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        size = len(speed)
        ans = size
        speedPosition = []
        for i in range(size):
            speedPosition.append([position[i],speed[i]])
        
        speedPosition.sort()

        stack = []
        
        for i in range(size):
            stack.append((target-speedPosition[i][0])/speedPosition[i][1])
            
        for i in range(size-2,-1,-1):
            if stack[i]<=stack[i+1]:
                ans-=1
                stack[i]=stack[i+1]
                
        
        return ans