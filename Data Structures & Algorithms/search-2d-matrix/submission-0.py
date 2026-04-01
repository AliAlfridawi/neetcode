class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix[0])-1

        # Finding target row
        left = 0 
        right = len(matrix)-1
        row = -1
        while left<=right:
            mid = (left+right)//2
            if matrix[mid][0] <= target and matrix[mid][n] >= target:
                row = mid
                left = right + 1
            else:
                if matrix[mid][0] > target:
                    right = mid-1
                else:
                    left = mid+1
        if row == -1:
            return False
        else:
            left = 0
            right = n
            while left <= right:
                mid = (left+right)//2
                if matrix[row][mid]== target:
                    return True
                else:
                    if matrix[row][mid] > target:
                        right = mid-1
                    else:
                        left = mid+1
            
        return False