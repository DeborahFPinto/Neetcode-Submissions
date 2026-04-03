class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        linhaprocurar = -1
        i = 0

        while i < (len(matrix) - 1) and linhaprocurar == -1:
            if matrix[i][0] == target:
                return True
            
            if matrix[i][0] < target and matrix[i+1][0] > target:
                linhaprocurar = i
            
            i += 1

        if linhaprocurar == -1:
            if matrix[i][0] == target:
                return True
            elif matrix[i][0] < target:
                linhaprocurar = i
            else:
                return False

        for j in range(len(matrix[linhaprocurar])):
            if matrix[linhaprocurar][j] == target:
                return True

        return False