class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        a = 0
        b = (n*m) - 1
        while a <= b :
            millieu = (a+b) // 2
            row = millieu // m
            column = millieu % m
            if target == matrix[row][column] : 
                return True
            elif target < matrix[row][column] :
                b = millieu - 1
            else :
                a = millieu + 1
        return False