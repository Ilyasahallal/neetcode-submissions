class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       n = len(matrix)
       m = len(matrix[0]) 
       row = 0
       while row < n :
        a = 0
        b = m -1
        while a <= b :
            millieu = (a+b) // 2
            if target == matrix[row][millieu] :
                return True
            elif target < matrix[row][millieu]  :
                b= millieu - 1
            else :
                a = millieu + 1
        row = row + 1
       return False



