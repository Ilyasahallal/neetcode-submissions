class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        perimeter = 0
        for i in range(n) :
            for j in range(m):
                if grid[i][j] == 1:
                    nombre_voisins = 0
                    if j != 0:
                        voisin_horiz_gauche = grid[i][j-1]
                        if voisin_horiz_gauche == 1 :
                            nombre_voisins += 1
                    if j != m-1:
                        voisin_horiz_droit = grid[i][j+1]
                        if voisin_horiz_droit == 1:
                            nombre_voisins += 1
                    if i != 0 :
                        voisin_verti_gauche = grid[i-1][j]
                        if voisin_verti_gauche == 1 :
                            nombre_voisins += 1
                    if i!= n-1 :                 
                        voisin_verti_droit = grid[i+1][j]
                        if voisin_verti_droit == 1:
                            nombre_voisins += 1
                    perimeter += 4 - nombre_voisins
        return perimeter
                

        