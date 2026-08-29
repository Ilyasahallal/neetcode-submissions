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
            colonne=[]
            for j in range(n):
                colonne.append(board[j][i])
            seen=set()
            for x in colonne:
                if x == ".":
                    continue
                if x in seen:
                    return False
                seen.add(x)
        #On verifie d'abord les box 3x3
        #box1
        seen=set()
        for i in range(0,3):
            box=[]
            for j in range(0,3):
                box.append(board[i][j])
            for x in box:
                if x == ".":
                    continue
                if x in seen:
                    return False
                seen.add(x)
        #box2
        seen=set()
        for i in range(0,3):
            box=[]
            for j in range(3,6):
                box.append(board[i][j])
            for x in box:
                if x == ".":
                    continue
                if x in seen:
                    return False
                seen.add(x)
        #box3
        seen=set()
        for i in range(0,3):
            box=[]
            for j in range(6,9):
                box.append(board[i][j])
            for x in box:
                if x == ".":
                    continue
                if x in seen:
                    return False
                seen.add(x)
        #box4
        seen=set()
        for i in range(3,6):
            box=[]
            for j in range(0,3):
                box.append(board[i][j])
            for x in box:
                if x == ".":
                    continue
                if x in seen:
                    return False
                seen.add(x)
        #box5
        seen=set()
        for i in range(3,6):
            box=[]
            for j in range(3,6):
                box.append(board[i][j])
            for x in box:
                if x == ".":
                    continue
                if x in seen:
                    return False
                seen.add(x)
        #box6
        seen=set()
        for i in range(3,6):
            box=[]
            for j in range(6,9):
                box.append(board[i][j])
            for x in box:
                if x == ".":
                    continue
                if x in seen:
                    return False
                seen.add(x)
        #box7
        seen=set()
        for i in range(6,9):
            box=[]
            for j in range(0,3):
                box.append(board[i][j])
            for x in box:
                if x == ".":
                    continue
                if x in seen:
                    return False
                seen.add(x)
        #box8
        seen=set()
        for i in range(6,9):
            box=[]
            for j in range(3,6):
                box.append(board[i][j])
            for x in box:
                if x == ".":
                    continue
                if x in seen:
                    return False
                seen.add(x)
        #box9
        seen=set()
        for i in range(6,9):
            box=[]
            for j in range(6,9):
                box.append(board[i][j])
            for x in box:
                if x == ".":
                    continue
                if x in seen:
                    return False
                seen.add(x)
        return True

