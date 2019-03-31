backtracks=0
def findnextcelltofill(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                return(i,j)

    return -1,-1

def isvalid(grid,i,j,e):
    rowok=all([grid[i][x]!=e for x in  range(9)])
    if rowok:
        columnok=all([grid[x][j]!=e for x in range(9)])
        if columnok:
            sectopx,sectopy=3*(i//3),3*(j//3)
            for x in range(sectopx,sectopx+3):
                for y in range(sectopy,sectopy+3):
                    if grid[x][y]==e:
                        return False

            return True
    return False

def solvesudoku(grid,i=0,j=0):
    global backtracks
    i,j=findnextcelltofill(grid)
    if i==-1:
        return True
    for e in range(1,10):
        if isvalid(grid,i,j,e):
            grid[i][j]=e
            if solvesudoku(grid,i,j):
                return True

            backtracks +=1
            grid[i][j]=0

    return False

def printsudoku(grid):
    for row in grid:
        print(row)
    return



l1=[]
for i in range(9):
    l1.append(list(map(int,input().split())))
solvesudoku(l1)
printsudoku(l1)
print ('Backtracks = ', backtracks)
