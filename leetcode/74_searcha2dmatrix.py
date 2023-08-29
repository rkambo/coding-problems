class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1
        
        for i in range(len(matrix)):
            row = matrix[i]
            if target >= row[l] and target <= row[r]:
                while l <= r:
                    mid = (r + l + 1) // 2
                    if row[mid] == target:
                        return True
                    if row[mid] < target:
                        l += 1
                    else:
                        r -= 1
        return False