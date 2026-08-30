class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #solution_brute
        n=len(board)
        #On verifie d'abord les lignes
        for i in range(n):
            seen=set()
            for x in board[i]:
                if x == ".":
                    continue
                if x in seen:
                    return False
                seen.add(x)
        #On verifie d'abord les colonnes
        for i in range(n):
            seen=set()
            for j in range(n):
                x=board[j][i]
                if x == ".":
                    continue
                if x in seen:
                    return False
                seen.add(x)
        #On verifie d'abord les boxes 3x3
        for l in range(3):
            for k in range(3):
                seen=set()
                for i in range(3*l,3*l+3):
                    for j in range(3*k,3*k+3):
                        x=board[i][j]
                        if x == ".":
                            continue
                        if x in seen:
                            return False
                        seen.add(x)   
        return True
            
            
            
            
            