class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #solution_brute
        n=len(board)
        lignes = [set() for i in range(n)]
        colonnes = [set() for i in range(n)]
        boxes = [[set() for i in range(3)] for i in range(3)]
        for i in range(n):
            for j in range(n):
                x = board[i][j]
                if x == ".":
                    continue
                if x in lignes[i]:
                    return False
                lignes[i].add(x)
                if x in colonnes[j]:
                    return False
                colonnes[j].add(x)
                k = i // 3
                m = j // 3 
                if x in boxes[k][m]:
                    return False
                boxes[k][m].add(x)
        return True
            
            
            
            